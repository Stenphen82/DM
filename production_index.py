import pandas as pd
import warnings
from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from pandas.plotting import autocorrelation_plot
from statsmodels.sandbox.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.stattools import arma_order_select_ic
from statsmodels.tsa.arima_model import ARIMA

def arima():

    series_ch = pd.read_csv("http://labfile.oss.aliyuncs.com/courses/1176/agriculture.csv", index_col=0)
    series_ch.plot(figsize=(9, 6))
    
    fig, axes = plt.subplots(ncols=3, nrows=1, figsize=(15, 3))
    diff_ch = series_ch.diff().dropna()  
    axes[0].plot(diff_ch)  
    autocorrelation_plot(diff_ch, ax=axes[1])  
    axes[2].plot(acorr_ljungbox(diff_ch)[1]) 
    
    fig, axes = plt.subplots(ncols=3, nrows=1, figsize=(15, 3))
    diff_ch1 = series_ch.diff(periods=2).dropna() 
    axes[0].plot(diff_ch1)  
    autocorrelation_plot(diff_ch1, ax=axes[1])  
    axes[2].plot(acorr_ljungbox(diff_ch1)[1]) 
        
    fig, axes = plt.subplots(ncols=3, nrows=1, figsize=(15, 3))
    diff_ch2 = series_ch.diff().diff().dropna()  
    axes[0].plot(diff_ch2)  
    autocorrelation_plot(diff_ch2, ax=axes[1])  
    axes[2].plot(acorr_ljungbox(diff_ch2)[1])
        
    fig, axes = plt.subplots(ncols=3, nrows=1, figsize=(15, 3))
    diff_ch3 = series_ch.diff().diff().diff().dropna()      
    axes[0].plot(diff_ch3)  
    autocorrelation_plot(diff_ch3, ax=axes[1])  
    axes[2].plot(acorr_ljungbox(diff_ch3)[1])
    
    d=1
        
    p,q=arma_order_select_ic(diff_ch, ic='aic')['aic_min_order']
    print('p,d,q',p,d,q)
    return p,d,q

if __name__=='__main__':
    arima()

