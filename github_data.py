import requests
import pandas as pd
import json
from pandas import DataFrame

def issues(repo):
    raw=requests.get('https://api.github.com/repos/'+ repo + '/issues')
    df=pd.DataFrame(raw.json())
    df_user=df.loc[:,['user']]
    names=[]
    i=0
    while i<len(df_user):
        names.append(df_user.loc[i][0].get('login'))
        i=i+1
    
    df_name=DataFrame(names,columns=['user_name'])

    issues_df=df.loc[:,['number','title']].join(df_name)
    print(issues_df)

    return issues_df

issues("numpy/numpy")

