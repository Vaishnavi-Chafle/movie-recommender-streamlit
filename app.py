import streamlit as st
import pickle
import pandas as pd
import requests

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Page config
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark theme
st.markdown("""
    <style>
    /* Overall background and base text color */
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #e0e0e0;
    }

    /* Selectbox label */
    label[for="movie_selector"] {
        color: #000000 !important;  /* Only this label in black */
        font-weight: bold;
        font-size: 16px;
    }

    /* General text */
    .css-10trblm, .css-1v0mbdj, .css-1cpxqw2, .css-ffhzg2, .css-1d391kg {
        color: #e0e0e0 !important;
    }

    /* Button style */
    .stButton > button {
        background-color: #00FFAA;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# App title
st.title('🎬 Movie Recommender System with Posters')

# Function to fetch movie poster from OMDb API
def fetch_poster_omdb(movie_title):
    api_key = "76a82709"  # Replace with your actual OMDb API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["Response"] == "True" and data["Poster"] != "N/A":
        return data["Poster"]
    else:
        return "https://via.placeholder.com/300x450.png?text=Poster+Not+Available"

# Recommendation logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster_omdb(title))

    return recommended_movies, recommended_posters

# Select movie
selected_movie_name = st.selectbox(
    "🎥 Type or select a movie:",
    movies['title'].values,
    key="movie_selector"
)

# Show recommendations
if st.button("🎯 Show Recommendations", key="recommend_btn"):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.markdown(
                f"<p style='color:#e0e0e0; font-weight:bold; text-align:center'>{names[i]}</p>",
                unsafe_allow_html=True
            )







