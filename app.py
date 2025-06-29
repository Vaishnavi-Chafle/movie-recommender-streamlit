import streamlit as st
import pickle
import pandas as pd
import requests

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('🎬 Movie Recommender System with Posters')


# Function to fetch poster using OMDb API
def fetch_poster_omdb(movie_title):
    api_key = "76a82709"  # Your OMDb API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["Response"] == "True" and data["Poster"] != "N/A":
        return data["Poster"]
    else:
        return "https://via.placeholder.com/300x450.png?text=Poster+Not+Available"


# Recommend movies function
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


# Streamlit UI
selected_movie_name = st.selectbox(
    "Type or select a movie:",
    movies['title'].values
)

if st.button('Show Recommendations'):
    names, posters = recommend(selected_movie_name)

    # Layout for posters
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])






