import streamlit as st
import pandas as pd
import pickle
import requests #for api

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=218b31b0f7a9f51423c8d44537128b21&language=en-US'.format(movie_id))
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie): #for top 5 movie recommendation
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x:x[1])[1:6]  #sorting the data on the basis of distance which is [1] and enumerated function for index of that particular movie vector [1:6] for fetching top 5 similar movies

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list :
       movie_id = movies.iloc[i[0]].movie_id
       recommended_movies.append(movies.iloc[i[0]].title) #i[0] means movie index not distance :) and new_def.iloc for fetching text of that index and .title is for movie name
       #fetch poster from API
       recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'How would you like to be contracted?',
movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5  = st.columns(5)
    with col1 :
        st.header(names[0])
        st.image(posters[0])
    with col2 :
        st.header(names[1])
        st.image(posters[1])
    with col3 :
        st.header(names[2])
        st.image(posters[2])
    with col4 :
        st.header(names[3])
        st.image(posters[3])
    with col5 :
        st.header(names[4])
        st.image(posters[4])