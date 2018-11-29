import numpy as np
import pandas as pd
from fbprophet import Prophet
import warnings

warnings.filterwarnings('ignore')

def additive():
    df_original = pd.read_csv("http://labfile.oss.aliyuncs.com/courses/1176/Chengdu_HourlyPM25.csv")
    df1=df_original.iloc[:,-2:]
    df1.columns = ['ds', 'y']
    df2=df1.replace(-999,np.nan)
    df3=df2.fillna(method='ffill')
    df4=df3.fillna(method='bfill')
    
    date_index=pd.to_datetime(df4.ds)
    df4.ds=date_index
    df_data_dated=df4.set_index('ds')
    df_day=df_data_dated.resample('D').mean()
    
    df_train=df_day.reset_index()
    
    m = Prophet()  
    m.fit(df_train)
    future = m.make_future_dataframe(periods=365, freq='D')
    
    forecast = m.predict(future)  
    df_forecast=forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    forecast=df_forecast.iloc[-365:,:]
    forecast.set_index('ds',inplace=True)
    forecast.to_csv("forecast.csv")
    return forecast

if __name__=='__main__':
    additive()
