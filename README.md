🎬 MOVIE RECOMMENDER SYSTEM - CONTENT-BASED ENGINE 🔍

Welcome to the Movie Recommender System repository! This project uses Natural Language Processing, Machine Learning, and Streamlit to help users discover movies similar to the ones they love. It's a smart, fast, and intuitive content-based movie recommendation engine built from scratch.

───────────────────────────────────────────────────────────────

📌 PROJECT FEATURES:
────────────────────

✅ Built using:
   - Python
   - NLP (Natural Language Processing)
   - Scikit-learn (CountVectorizer + Cosine Similarity)
   - Streamlit (for frontend app)
   - Pickle (for model serialization)

✅ Key Components:
   - Exploratory Data Analysis (EDA)
   - Data cleaning and preprocessing
   - Feature engineering using text data (genres, cast, crew, keywords, overview)
   - Stemming and token normalization
   - Bag-of-Words model with CountVectorizer (top 5000 words)
   - Cosine Similarity-based recommendation system
   - Release-date weighting to fine-tune recommendations

✅ Final App:
   - A simple interface where the user selects a movie and number of recommendations
   - Returns similar movies with a smart relevance algorithm

───────────────────────────────────────────────────────────────

📁 DATASETS USED:
─────────────────

🎞️ tmdb_5000_movies.csv  
🔸 Columns: budget, genres, homepage, id, keywords, language, title, overview, release_date, revenue, runtime, status, tagline, vote_average, etc.

🎞️ tmdb_5000_credits.csv  
🔸 Columns: movie_id, title, cast, crew

📌 Source: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata  
📌 Original Data: The Movie Database (TMDB)

───────────────────────────────────────────────────────────────

💾 HOW TO RUN LOCALLY:
──────────────────────

1. **Clone the repository:**
git clone https://github.com/yourusername/movie_recommender_system.gitcd movie_recommender_system

2. **Install requirements:**
pip install -r requirements.txt


3. **Important Note:**
- The file `similarity.pkl` exceeds 100 MB and is **NOT included in the GitHub repo** due to GitHub's file size restrictions.
- To generate it:
  ➤ Run the Jupyter notebook first (provided in the repo)  
  ➤ It will create `similarity.pkl` and `movies.pkl` in your current folder  
  ➤ These files are required for `app.py` to run correctly

4. **Run the app:**
streamlit run app.py

───────────────────────────────────────────────────────────────

📸 SCREENSHOTS:
───────────────

Screenshots showcasing the app in action are provided in the notebook.  
Check out how the UI looks and how smooth the recommendations work!

───────────────────────────────────────────────────────────────

🧠 HOW IT WORKS:
────────────────

1. **Data Preprocessing:**  
→ Extracts and cleans genre, cast, crew, keywords, and overview fields  
→ Converts stringified JSON to Python lists  
→ Applies stemming to normalize tokens  
→ Removes internal spaces to ensure unique identifiers  

2. **Vectorization:**  
→ Uses CountVectorizer with top 5000 words and removes English stopwords  
→ Generates sparse vectors for each movie's combined text fields  

3. **Similarity Computation:**  
→ Cosine Similarity is computed for every pair of movies  
→ Release date difference is also factored into final ranking  

4. **Recommendation:**  
→ For a selected movie, returns top N most similar movies  
→ Ensures relevance both in content and timeline  

───────────────────────────────────────────────────────────────

✨ CREDITS:
───────────

Made with ❤️ by [Your Name]  
Tools used: Python, NLTK, Sklearn, Pandas, Streamlit, TMDB API, Kaggle  
Project inspired by the idea of helping users find meaningful movie recommendations beyond generic lists.

───────────────────────────────────────────────────────────────

📬 FEEDBACK & CONTRIBUTIONS:
─────────────────────────────

Found a bug? Want to suggest a feature?  
Feel free to open an issue or submit a pull request!

---

"Cinema is a mirror by which we often see ourselves."  
This recommender ensures that reflection leads to something you'll love to watch next. 🎥✨

