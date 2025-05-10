import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI
import os
from dotenv import load_dotenv



@st.cache_resource
def load_data():
    metadata = pd.read_json("movies_metadata.json")
    embeddings = np.load("movie_embeddings.npy")
    return metadata, embeddings

def get_embedding_safe(text, model="text-embedding-3-small"):
    try:
        response = client.embeddings.create(input=[text], model=model)
        return np.array(response.data[0].embedding)
    except Exception as e:
        st.error(f"Embedding error: {e}")
        return None

def recommend_movies(query, metadata, embeddings, top_n=3):
    emb = get_embedding_safe(query)
    if emb is None:
        return pd.DataFrame()

    sims = cosine_similarity([emb], embeddings)[0]
    top_indices = sims.argsort()[-top_n:][::-1]
    top_movies = metadata.iloc[top_indices].copy()
    top_movies["similarity"] = sims[top_indices]
    return top_movies

# Streamlit UI
st.title("🎬 Movie Emotion Recommender")
st.markdown("Enter a feeling or vibe and get movies that match emotionally!")

# Ask user for their OpenAI API key
user_api_key = st.text_input("🔑 Enter your OpenAI API key", type="password")

# Don't run anything unless API key is provided
if not user_api_key:
    st.warning("Please enter your OpenAI API key to use the recommender.")
    st.stop()

# Set up OpenAI client using user key
from openai import OpenAI
client = OpenAI(api_key=user_api_key)

query = st.text_input("What are you in the mood for?", placeholder="e.g. nostalgic and bittersweet love")

if query:
    with st.spinner("Finding matching movies..."):
        metadata, embeddings = load_data()
        results = recommend_movies(query, metadata, embeddings)

    if not results.empty:
        st.success("Here are some movies you might like:")
        for _, row in results.iterrows():
            st.markdown(f"**🎞️ {row['title']}**")
            st.markdown(f"🌀 *{row['combined_tags_text']}*")
            st.markdown("---")
    else:
        st.warning("Couldn't find anything—try rephrasing your description.")
