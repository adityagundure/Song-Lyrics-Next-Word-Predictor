# Project: LyricNext — Song Lyrics Next-Word Predictor

**Short name:** LyricNext  
**Based on:** `topSongsLyrics1950_2019.csv` (lyrics dataset)  
**Tech stack:** Python, TensorFlow/Keras, NLTK, Pandas, NumPy, Matplotlib, Streamlit

---

## Project Summary (auto-gene<img width="1912" height="781" alt="Screenshot 2025-11-23 190708" src="https://github.com/user-attachments/assets/b03d185d-be6d-46ad-9fc1-cd5f188ffd8c" />
rated from notebook `/mnt/data/NEXT.ipynb`)

This project trains a neural language model on a dataset of popular song lyrics (`topSongsLyrics1950_2019.csv`) to predict the next word(s) given a lyric prompt. The notebook uses text preprocessing (tokenization, padding), sequence modeling with TensorFlow/Keras, and includes at least one visualization. A `predict_next_word` helper function exists in the notebook.
<img width="1912" height="781" alt="Screenshot 2025-11-23 190708" src="https://github.com/user-attachments/assets/5508085f-f483-40b3-8549-3806e35b8f5b" />




---

## Project goals

1. Train a next-word prediction model for song lyrics (RNN/GRU/LSTM or Transformer-based).
2. Expose the model via a simple, user-friendly Streamlit web app.
3. Host the app on Streamlit Community Cloud or deploy via GitHub & CI.
4. Provide reproducible steps and a clear README for contributors.

---

## Files in this repo

- `notebooks/NEXT.ipynb` — core analysis and model training (original notebook).
- `app.py` — Streamlit app (skeleton) to serve the model and accept user inputs.
- `requirements.txt` — Python dependencies.
- `README.md` — this file.

---

## Quickstart (run locally)

1. Clone the repo:
```bash
git clone <your-github-repo-url>
cd <repo-name>
```

2. Create virtual environment and install:
```bash
python -m venv venv
# Windows
venv\\Scripts\\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

3. Place the dataset and any saved model weights into `data/` and `models/` respectively:
```
mkdir data models
mv /path/to/topSongsLyrics1950_2019.csv data/
```

4. Run the Streamlit app:
```bash
streamlit run app.py
```

---

## How to connect & deploy to Streamlit (Streamlit Community Cloud)

1. Push repo to GitHub (see "Connecting to GitHub" below).  
2. Sign in to [Streamlit Community Cloud](https://streamlit.io/cloud) and click **New app** → pick your GitHub repository → select branch and `app.py` as the entrypoint → **Deploy**.  
3. Add any secret environment variables (like MODEL_PATH) in the app settings if you store large model weights in external storage (S3, Google Drive, etc.).

---

## Connect to GitHub (setup and push)

1. Initialize & commit:
```bash
git init
git add .
git commit -m "Initial commit — LyricNext"
```

2. Create GitHub repo (use GitHub UI or CLI), then push:
```bash
git remote add origin git@github.com:yourusername/lyricnext.git
git branch -M main
git push -u origin main
```

3. (Optional) Add a small GitHub Actions workflow `.github/workflows/python-app.yml` to run tests or build artifacts on push.

---

## Streamlit app structure (app.py skeleton)

- Loads tokenizer and model from `models/`.
- Displays a text input for a lyric prompt.
- Shows predicted next-word suggestions.
- Option to generate several words sequentially to create a short lyric continuation.
- (Optional) Button to download the generated lyric.

---

## Development notes & TODOs

- Save tokenizer and model weights after training (`tokenizer.json` or pickle + `model.h5` or SavedModel dir).
- Add proper error handling for missing model files.
- Consider using a small sample of the dataset for quick prototyping and CI tests.
- Add unit tests for preprocessing and prediction functions.

---


