import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_job(text):
    try:
        text_vec = vectorizer.transform([text])
        prediction = model.predict(text_vec)[0]
        prob = model.predict_proba(text_vec)[0]

        confidence = max(prob)

        # Get feature importance
        feature_names = vectorizer.get_feature_names_out()
        coefs = model.coef_[0]

        indices = text_vec.toarray()[0].nonzero()[0]

        important_words = []

        for i in indices:
            word = feature_names[i]
            weight = coefs[i]
            important_words.append((word, weight))

        # Sort words by importance
        important_words = sorted(important_words, key=lambda x: abs(x[1]), reverse=True)[:5]

        reasons = [word for word, _ in important_words]

        return prediction, confidence, reasons

    except:
        return None, None, []