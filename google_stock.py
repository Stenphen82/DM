import pandas as pd
import datetime

def quarter_volume():

    df_data=pd.read_csv('GOOGL.csv')
    date_index=pd.to_datetime(df_data.Date)
    df_data.Date=date_index
    df_data_dated=df_data.set_index('Date')

    df_quarter=df_data_dated.resample('Q').mean()
    df_quarter.Volume=df_data_dated.Volume.resample('Q').sum()

    df_quarter.sort_values(by='Volume',ascending=False,inplace=True)
   
    return df_quarter

if __name__=='__main__':
    quarter_volume()


