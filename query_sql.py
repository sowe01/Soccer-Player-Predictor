import sqlalchemy as db
import pandas as pd
import numpy as np
import os
import json
from dotenv import load_dotenv
load_dotenv()


url= os.getenv('PASSWORD')
engine = db.create_engine(url)
connection = engine.connect()


def getDataUser(user):
    ''' devuelve la informacion de un jugador ''' 
    query = """
       SELECT * FROM mydb.soccer WHERE short_name='{}';
    """.format(user)
    df= pd.read_sql_query(query, engine)
    #print(df)
    return df.to_json(orient='records')

def getdataframe():
    '''devuelve las 10 primeras entradas del dataframe'''
    query = """
       SELECT * FROM mydb.soccer LIMIT 10;
    """.format()
    df= pd.read_sql_query(query, engine)
    #print(df)
    return df.to_json(orient='records')

def getpredict(short_name):
    ''' devuelve la predicción '''
    query = """
       SELECT short_name, overall_20, overall FROM mydb.soccer WHERE short_name='{}'
    """.format(short_name)
    df= pd.read_sql_query(query, engine)
    #print(df)
    return df.to_json(orient='records')

def age(n, m):
    '''elige en un rango de edad entre n y m ordenados por la predicción'''
    query = """
       SELECT * FROM mydb.soccer Where age > '{}' and age < '{}' ORDER BY overall desc LIMIT 10
    """.format(n, m)
    df= pd.read_sql_query(query, engine)
    return df.to_json(orient='records')


def getmaxevol():
    ''' prevision de los que mas van a mejorar '''
    query = """
       SELECT short_name, evol FROM mydb.soccer ORDER BY evol desc LIMIT 11
    """.format()
    df= pd.read_sql_query(query, engine)
    #print(df)
    return df.to_json(orient='records')

def getminevol():
    ''' prevision de los que mas van a empeorar '''
    query = """
       SELECT short_name, evol FROM mydb.soccer  ORDER BY evol asc LIMIT 11
    """.format()
    df= pd.read_sql_query(query, engine)
    #print(df)
    return df.to_json(orient='records')