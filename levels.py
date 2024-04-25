import asyncpg
from sklearn.linear_model import LinearRegression
import numpy as np
from conecctions import connect_postgres

conn = connect_postgres()


cursor = conn.cursor()

cursor.execute("SELECT num_reviews, rating, level FROM nombre_tabla")
data = cursor.fetchall()

cursor.close()
conn.close()

X = np.array([[d[0], d[1]] for d in data])
y = np.array([d[2] for d in data])

model = LinearRegression()
model.fit(X, y)

def predict_level(num_reviews, rating):
    return model.predict(np.array([[num_reviews, rating]]))[0]

num_reviews = 1200
rating = 4.7
predicted_level = predict_level(num_reviews, rating)
print(f"Predicted Level: {predicted_level}")
