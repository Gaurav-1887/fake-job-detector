import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load data
df = pd.read_csv("jobs.csv")

X = df['text']
y = df['label']

# Improved vectorizer
vectorizer = TfidfVectorizer(
    stop_words='english',
    ngram_range=(1,2),   # bigrams added 🔥
    max_features=5000
)

X_vec = vectorizer.fit_transform(X)

# Better model
model = LogisticRegression(max_iter=200)
model.fit(X_vec, y)

# Save
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Improved model trained!")