import streamlit as st
import os
import numpy as np

st.set_page_config(page_title="LyricNext — Next Word Predictor", layout="centered")

st.title("LyricNext — Song Lyrics Next-Word Predictor")
st.write("Enter a lyric prompt and the model will predict the next word(s).")

prompt = st.text_area("Type a lyric prompt here:", value="I see the stars", height=120)

num_preds = st.slider("How many words to predict (sequential):", 1, 20, 5)

if st.button("Generate"):
    # Placeholder prediction flow - replace with real model loading & inference
    st.info("Loading model and tokenizer...")
    model_path = os.environ.get("MODEL_PATH", "models/model.h5")
    tokenizer_path = os.environ.get("TOKENIZER_PATH", "models/tokenizer.json")
    st.write(f"Model path: `{model_path}`")
    st.write(f"Tokenizer path: `{tokenizer_path}`")
    # TODO: load tokenizer and model, preprocess prompt, generate words
    st.success("This is a skeleton. Replace with real model loading and inference logic.")