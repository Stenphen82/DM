import warnings
warnings.filterwarnings('ignore')
import pandas_datareader.data as web
import pandas as pd
import datetime
import numpy as np

def alibaba():
    start = datetime.datetime(2017, 1, 1)
    end = datetime.datetime(2017, 12, 31) 
    alibaba_df = web.DataReader('BABA','yahoo',start,end) 
    rise,fall=0,0
    year_2017 = alibaba_df['2017-01-01':'2017-12-31']

    year_2017_close = year_2017.Close
    log_change = np.log(year_2017_close) - np.log(year_2017_close.shift(1))

    for index,row in alibaba_df.iterrows() :
        if row['Close']>row['Open']:
            rise+=1
        elif row['Close']<row['Open']:
            fall+=1

    print('Rise', rise, 'days')
    print('Fall', fall, 'days')

    return int(rise) ,int(fall)

alibaba()
