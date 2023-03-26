# psycopg2 library is necessary
import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine(
    f"postgresql://thiagogham:{os.environ['PGPASS']}@database-igti-enem.cfocszuomufc.us-east-1.rds.amazonaws.com:5432/postgres"
)

df = pd.read_csv("data/enem2020.csv", sep=';')

df.to_sql('enem2020', con=engine, if_exists='replace', index=False, chunksize=10000)