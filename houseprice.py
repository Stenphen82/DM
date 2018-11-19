import pandas as pd
import numpy as np
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error

def beijing(n):
    df_csv=pd.read_csv('beijing_house_price.csv')
    df_csv.dropna(inplace=True)
    df_csv.drop_duplicates(inplace=True)
    df_corr=df_csv.corr()
    index_list=df_corr.iloc[:,-2].abs().sort_values(ascending=False).index.tolist()[1:4]
    df_data=df_csv[[index_list[0],index_list[1],index_list[2]]]
    
    x_train, x_test, y_train, y_test = train_test_split(df_data,df_csv['每平米价格'],test_size=0.3, random_state=10)
    
    poly_features = PolynomialFeatures(n)
    poly_x_train = poly_features.fit_transform(x_train)
    poly_x_test = poly_features.fit_transform(x_test)
    
    model = LinearRegression()  
    model.fit(poly_x_train, y_train)  
    results = model.predict(poly_x_test)
    mae=mean_absolute_error(y_test, results)
    print(mae)
    return mae
	
if __name__=='__main__':
    i=1
    while i < 10:
        beijing(i)
        i=i+1

