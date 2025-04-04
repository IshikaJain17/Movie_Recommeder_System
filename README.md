# Movie Recommender System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A content-based movie recommendation system that suggests similar movies based on user preferences.

## Features

- Recommends movies based on content similarity
- Uses TMDB 5000 dataset for comprehensive recommendations
- Simple Flask-based web interface
- Deployable with Heroku (Procfile included)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/IshikaJain17/Movie_Recommeder_System.git
cd Movie_Recommeder_System
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download the dataset files:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`
Place them in the project root directory

## Usage

Run the Flask application:
```bash
python app.py
```

Access the web interface at `http://localhost:5000`

## Technology Stack

- Python 3
- Flask (Web Framework)
- Pandas (Data Processing)
- Scikit-learn (Machine Learning)
- Heroku (Deployment)

## Dataset

The system uses the [TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata) containing:
- 5000 movies
- Metadata including cast, crew, plot keywords, etc.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
