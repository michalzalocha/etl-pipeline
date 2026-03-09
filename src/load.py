import pandas as pd
import psycopg2
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://netflixuser:netflixpass@localhost:5433/netflixdb"
)

df = pd.read_csv("data/netflix_titles.csv")

df.to_sql(
    "netflix_titles",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully")