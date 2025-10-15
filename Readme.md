# Movie Recommender

A lightweight movie recommender system built with Streamlit and Python. This repository contains a small Streamlit app (`app.py`) and a companion Jupyter notebook (`project.ipynb`) used to explore and prepare the dataset and to build the recommendation model.

Live demo: https://cineguide-sumitksr.streamlit.app/

Repository: https://github.com/sumitksr/Movie-Recommender

---

## Overview

This project implements a content-based movie recommender. The model recommends similar movies based on precomputed similarity scores calculated over movie metadata (title, genres, keywords, cast, crew, etc.). The Streamlit app uses a precomputed `movie_list.pkl` and `similarity.pkl` to instantly show five recommended titles and their posters when you select a movie.

## What the notebook does

The Jupyter notebook (`project.ipynb`) contains the exploratory data analysis and the steps used to prepare the features and compute the similarity matrix:

- Load and inspect TMDB movie metadata (movies, credits)
- Clean and normalize text fields (genres, keywords, cast, crew)
- Build combined feature strings for each movie
- Vectorize features using CountVectorizer / TfidfVectorizer (or similar)
- Compute pairwise cosine similarity to produce a `similarity` matrix
- Save `movie_list.pkl` (movie metadata) and `similarity.pkl` (matrix) used by the Streamlit app

## Data

The data used in this project is the TMDB Movie Dataset available on Kaggle:

- TMDB Movie Metadata: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Download the CSV files and place them in the project root. The repo expects the following files (or similar):

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

If you already have preprocessed pickles (`movie_list.pkl` and `similarity.pkl`) you can put them in the project root and run the Streamlit app directly.

## How to run locally

1. Create and activate a Python virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install at least:

```powershell
pip install streamlit pandas scikit-learn requests
```

3. Run the Streamlit app:

```powershell
streamlit run app.py
```

Open the URL shown in the terminal (typically `http://localhost:8501`).


