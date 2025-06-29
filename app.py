import streamlit as st
import pickle
import pandas as pd
import requests

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set page config
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom dark theme using HTML/CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
        color: #FFFFFF;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #00FFAA;
    }
    .css-1d391kg { color: white; }
    .css-ffhzg2 { color: white; }
    </style>
    """, unsafe_allow_html=True)

# App title
st.title('🎬 Movie Recommender System with Posters')

# Function to fetch poster using OMDb API
def fetch_poster_omdb(movie_title):
    api_key = "76a82709"  # Replace with your actual OMDb API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["Response"] == "True" and data["Poster"] != "N/A":
        return data["Poster"]
    else:
        return "https://via.placeholder.com/300x450.png?text=Poster+Not+Available"

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster_omdb(title))

    return recommended_movies, recommended_posters

# Search/Select movie
selected_movie_name = st.selectbox(
    "🎥 Type or select a movie:",
    movies['title'].values,
    key="movie_selector"
)

# Recommendation button
if st.button("🎯 Show Recommendations", key="recommend_btn"):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.markdown(
                f"<p style='color:#ffffff; font-weight:bold; text-align:center'>{names[i]}</p>",
                unsafe_allow_html=True
            )






