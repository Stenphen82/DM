import pandas as pd
import numpy as np
df_csv=pd.read_csv("nyc-east-river-bicycle-counts.csv")
df_bridge=df_csv[df_csv.columns[6:8]]
x=df_bridge[df_bridge.columns[0]]
y=df_bridge[df_bridge.columns[1]]

def gradient_descent():
    w=0
    b=0
    lr=0.000000001
    num_iter = 10000
    n = len(x)   

    for i in range(num_iter):
        yi = w * x + b
        J_cost = (1/n)*sum([val**2 for val in (y - yi)])
        wd = -(2/n)*sum(x*(y-yi))
        bd = -(2/n)*sum(y-yi)
        w = w - lr * wd
        b =b - lr * bd

    return w, b

if __name__=='__main__':
    w,b=gradient_descent()
    print("w {}, b {}".format(w,b))
