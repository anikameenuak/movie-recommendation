import streamlit as st
import pickle
import pandas as pd
import streamlit as st

# This is the "Python way" to style your app directly
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
    }
    .stButton>button {
        color: #00E6FF;
        border-radius: 20px;
        border: 2px solid #00E6FF;
    }
    .bright-text {
        color: #00FF00;
        font-size: 20px;
        font-weight: bold;
        text-shadow: 0 0 10px #00FF00;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Movie Recommender")

# 1. Load the saved data
movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# 2. UI Setup


st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Select a movie to get recommendations:",
    movies['title'].values
)

# 3. Recommendation Logic
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movies = []
    for i in distances[1:6]: # Get top 5
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.markdown(f'<p class="bright-text">{i}</p>', unsafe_allow_html=True)