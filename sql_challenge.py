import sqlite3
import pandas as pd

def count(file,user_id):
    sql_con = sqlite3.connect(file)
    df= pd.read_sql("SELECT SUM(minutes) FROM data WHERE user_id ="+ user_id,sql_con)
    if df.loc[0][0] == None:
        sum_minutes=0
    else:
        sum_minutes=int(df.loc[0][0])
#    print(sum_minutes)
    return sum_minutes

count("users_data.sqlite","8490")
#count("users_data.sqlite","8901111")
