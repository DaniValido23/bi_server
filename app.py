from fastapi import FastAPI
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

app = FastAPI()

# Datos de ejemplo
data = {
    'title': ['Curso de Python', 'Introducción a la Fotografía', 'Curso de Finanzas', 'Java Programming Masterclass', 'Aprende SQL desde cero']
}

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['title'])
X = X.toarray()

model = MultinomialNB()
model.fit(X, np.zeros(X.shape[0]))

@app.post("/predict_category/")
async def predict_category(title: str):
    X_new = vectorizer.transform([title])
    X_new = X_new.toarray()
    predicted_category = model.predict(X_new)[0]
    return {"category": predicted_category}

@app.post("/assign_values/")
async def assign_values(title: str):
    return {"message": "Values assigned"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

