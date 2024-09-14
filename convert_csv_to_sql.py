import sqlite3
import pandas as pd

conn = sqlite3.connect('ecomm.db')

df = pd.read_csv('E-commerce Customer Behavior - Sheet1.csv')
df.to_sql('E-commerce Customer Behavior - Sheet1', conn, if_exists='replace', index=False)

conn.commit()
conn.close()