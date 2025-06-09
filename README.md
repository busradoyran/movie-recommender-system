# 🎬 Movie Recommender System using Collaborative Filtering

This project is a movie recommendation engine built using **Collaborative Filtering techniques**, aiming to suggest personalized movie recommendations based on user preferences and historical ratings. It demonstrates both memory-based and model-based approaches, and includes evaluation metrics to assess performance.

---

## 📌 Project Goals

- Explore and analyze user-movie rating data
- Implement **baseline recommenders** (popularity, average rating)
- Develop **memory-based CF** (User-User, Item-Item)
- Implement **model-based CF** using **SVD matrix factorization**
- Evaluate recommendations using **RMSE**, **Precision@K**, **Recall@K**
- (Optional) Build a small interactive demo with **Streamlit**

---

## 📂 Project Structure

movie-recommender-system/
- │
- ├── data/ # Raw datasets (MovieLens)
- ├── notebooks/ # Jupyter notebooks (EDA, experiments)
- ├── src/ # Source code
- │ ├── data_loader.py # Data loading functions
- │ ├── baseline.py # Baseline recommenders
- │ ├── memory_based.py # User-User & Item-Item CF
- │ ├── model_based.py # SVD-based recommender (Surprise)
- │ └── evaluation.py # RMSE, Precision@K, Recall@K
- ├── outputs/ # Result plots, logs, metrics
- ├── app/ # (Optional) Streamlit interface
- ├── README.md
- ├── requirements.txt
- └── .gitignore


---

## 🧠 Techniques Used

- 📊 **Exploratory Data Analysis** (EDA) using pandas, seaborn
- 🤝 **Memory-based Collaborative Filtering**
  - User-user similarity (cosine)
  - Item-item similarity
- 📉 **Model-based Collaborative Filtering**
  - Matrix Factorization (SVD from Surprise library)
- 📈 **Evaluation**
  - Root Mean Squared Error (RMSE)
  - Precision@K, Recall@K

---

## 📉 Sample Results

> *Coming soon: Visuals and metrics from the evaluation phase.*

---

## 🚧 Limitations & Future Work

This project focuses on the **core modeling and evaluation** aspects of building a collaborative filtering-based movie recommender. **Real-time performance and full deployment** are not goals in this prototype stage — the priority is a clean, well-documented and evaluated machine learning model.

**Planned Extensions**:
- Add hybrid recommenders (content + collaborative)
- Deploy via REST API (FastAPI) or UI (Streamlit)
- Handle cold-start users with metadata-based fallbacks

---

## 📁 Dataset

- [MovieLens Dataset (Small)](https://grouplens.org/datasets/movielens/)
  - Contains user ratings for movies
  - Widely used for building and benchmarking recommender systems

---

## ⚙️ Setup & Installation

```bash
git clone https://github.com/busradoyran/movie-recommender-system.git
cd movie-recommender-system
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

