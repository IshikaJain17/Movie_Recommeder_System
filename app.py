import streamlit as st
import pandas as pd
import pickle
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TMDB_API_KEY = os.getenv('TMDB_API_KEY')

def fetch_poster(movie_id):
    """Fetch movie poster URL from TMDB API for given movie ID"""
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    """
    Generate top 5 movie recommendations based on content similarity
    
    Args:
        movie (str): Movie title to base recommendations on
    
    Returns:
        tuple: (recommended_movie_titles, recommended_movie_posters)
    """
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    # Get top 5 most similar movies (skip first as it's the input movie itself)
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Load preprocessed movie data and similarity matrix
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
# Streamlit UI components
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'Select a movie to get recommendations:',
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