import pandas as pd
import numpy as np
from pandas import DataFrame

def caculate_w():
    df_csv=pd.read_csv("nyc-east-river-bicycle-counts.csv")
    df_bridge=df_csv[df_csv.columns[6:8]]
    
    x=[]
    for items in df_bridge['Brooklyn Bridge']:
        a=[1,items]
        x.append(a)
   
    x=np.matrix(x)
    y=np.matrix(df_bridge['Manhattan Bridge'])
    y=y.reshape(len(df_bridge['Manhattan Bridge']),1)
    
    W=(x.T * x).I * x.T * y
    w=round(float(W[1]),2)
    b=round(float(W[0]),2)
    print(w,b)
    return w,b

if __name__=='__main__':
    caculate_w()
