import asyncpg
import mysql.connector
from pymongo import MongoClient
from fastapi import FastAPI, HTTPException
from typing import List

async def connect_postgres():
    return await asyncpg.connect(user='mysql', password='35-**cDCG5FFDdG*2fc5F1F--3G1eBff', database='railway', host='35-**cDCG5FFDdG*2fc5F1F--3G1eBff')

def connect_mysql():
    return mysql.connector.connect(user='postgres', password='ohqAdtKehFepWIkjHbuFDotMDsauYOXo', database='railway', host='roundhouse.proxy.rlwy.net')

def connect_mongo():
    client = MongoClient('mongodb://mongo:nWnDnROSbPLpAUiENqkucJpXBDERiSCF@viaduct.proxy.rlwy.net:34143')
    return client['udemy']


app = FastAPI()

@app.get("/datos_postgres")
async def get_datos_postgres():
    conn = await connect_postgres()
    query = "SELECT * FROM CourseraDataset_Clean"
    datos = await conn.fetch(query)
    await conn.close()
    return datos

@app.get("/datos_mysql")
def get_datos_mysql():
    conn = connect_mysql()
    cursor = conn.cursor()
    query = "SELECT * FROM all_courses_of_Udacity_updated"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.close()
    return datos

@app.get("/datos_mongo")
def get_datos_mongo():
    db = connect_mongo()
    collection = db['udemy']
    datos = list(collection.find())
    return datos