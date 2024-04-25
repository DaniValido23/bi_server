from surprise import Dataset, Reader
from surprise import KNNBasic
from surprise import accuracy
import pandas as pd

# Ejemplo de datos (id, usuario, item, rating)
data = {
    'uid': ['A', 'A', 'A', 'B', 'B', 'C'],
    'iid': ['Curso1', 'Curso2', 'Curso3', 'Curso1', 'Curso2', 'Curso3'],
    'rating': [5, 4, 3, 5, 2, 4]
}
df = pd.DataFrame(data)

reader = Reader(rating_scale=(1, 5))

dataset = Dataset.load_from_df(df[['uid', 'iid', 'rating']], reader)


sim_options = {
    'name': 'cosine', 
    'user_based': False  
}
algo = KNNBasic(sim_options=sim_options)

uid = 'C'
iid = 'Curso2'
pred = algo.predict(uid, iid)
print(f'Predicción para el usuario {uid} en el item {iid}: {pred.est}')
