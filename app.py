
print("App starting")
import streamlit as st
print("Imported Streamlit")
import pickle
import requests

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

st.markdown("""
    <style>
    /* Main background - BLACK */
    .stApp {
        background-color: #000000;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
         background-color: #1a1a1a;
        border-right: 2px solid #ff6b6b;
    }
    
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #ff6b6b;
        text-shadow: none !important;
    }
    
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] li {
        color: #ffffff;
    }
    
    /* Header styling */
    h1 {
        color: #ff6b6b;
        text-align: center;
        font-family: 'Arial Black', sans-serif;
        font-weight: 900;
        padding: 20px;
        margin-bottom: 30px;
        font-size: 3.5em;
    }
    
    /* Selectbox container */
    .stSelectbox {
        margin-bottom: 20px;
    }
    
    /* Selectbox label */
    .stSelectbox label {
        color: #ffffff !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }
    
    /* Selectbox input */
    .stSelectbox > div > div {
        background-color: #1a1a1a;
        border: 2px solid #ff6b6b;
        border-radius: 10px;
        color: #ffffff;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b 0%, #c92a2a 100%);
        color: white;
        font-size: 20px;
        font-weight: bold;
        padding: 15px 40px;
        border-radius: 30px;
        border: none;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 10px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #c92a2a 0%, #ff6b6b 100%);
    }
    
    /* Movie title text styling */
    .stText {
        color: #ffffff;
        font-weight: bold;
        text-align: center;
        font-size: 16px;
    }
    
    /* Image styling */
    img {
        border-radius: 15px;
        transition: all 0.15s ease;
        border: 2px solid #333333;
    }
    
    img:hover {
        transform: scale(1.02);
        border-color: #ff6b6b;
    }
    
    /* Column styling */
    [data-testid="column"] {
        background-color: #1a1a1a;
        border-radius: 15px;
        padding: 15px;
        margin: 5px;
        border: 1px solid #333333;
    }
    
    /* Text in columns */
    [data-testid="column"] .stText {
        background-color: #ff6b6b;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 15px;
        font-weight: 900;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500/" + poster_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters


st.header('🎬 Movie Recommender System')

with st.sidebar:
    st.title("🎥 About")
    st.markdown("---")
    st.markdown("""
    ### How it works:
    1. Select a movie you like
    2. Click 'Show Recommendation'
    3. Get 5 similar movies instantly!
    
    ### Features:
    - 🎯 AI-powered recommendations
    - 🎬 5000+ movies database
    - 🖼️ Movie posters
    - ⚡ Lightning fast results
    
    ### Tech Stack:
    - Python
    - Streamlit
    - Machine Learning
    - TMDB API
    """)
    st.markdown("---")
    st.markdown("**Made with ❤️ by Sumit**")

st.markdown("<br>", unsafe_allow_html=True)

movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5) 
    for i, col in enumerate(cols):
        with col:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
