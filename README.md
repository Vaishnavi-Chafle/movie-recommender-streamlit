# 🎬 Movie Recommender System

This is a content-based movie recommendation system built using Python and Streamlit. It suggests similar movies based on cast, crew, genres, keywords, and overview using NLP and cosine similarity.

🔗 **Live Demo:** [Click here to try the app](https://movie-recommender-app-ecyzoukues5furdysm47xi.streamlit.app/)  
📂 **Dataset:** TMDb 5000 Movies + Credits  
🧰 **Tech Stack:** Python, Pandas, scikit-learn, Streamlit, OMDb API

---

## 💡 Features

- 🎯 Recommend 5 similar movies based on selected movie title
- 🧠 NLP + Cosine Similarity on combined text features
- 🖼 Fetches real-time posters from OMDb API
- 🌙 Dark theme UI using custom Streamlit HTML/CSS
- 🔐 API key stored securely using `st.secrets`
- 🚀 Deployed on Streamlit Cloud

---

## 🧠 How It Works

1. Combines features from columns like genres, keywords, overview, cast, and crew
2. Uses CountVectorizer to convert text into feature vectors
3. Computes cosine similarity to find similar movies
4. Displays top 5 recommended movies with poster images

---

## 📦 Installation (For Local Use)

```bash
git clone https://github.com/YOUR-USERNAME/movie-recommender-system.git
cd movie-recommender-system
pip install -r requirements.txt
streamlit run app.py

## 📸 Screenshot
![App Screenshot](screenshoti.png)
