import pandas as pd
import numpy as np
from pandas import DataFrame
from matplotlib import pyplot as plt

def co2_gdp_plot():
    df_climate_Data = pd.read_excel("ClimateChange.xlsx", sheetname='Data')

    df_CO2=df_climate_Data[(df_climate_Data['Series code']=='EN.ATM.CO2E.KT')]    
    df_GDP=df_climate_Data[(df_climate_Data['Series code']=='NY.GDP.MKTP.CD')]
    
    df_GDP=df_GDP.drop(df_GDP.columns[1:6],axis=1)
    
    df_GDP_value=df_GDP.drop(df_GDP.columns[0:1],axis=1)
    df_GDP_value=df_GDP_value.replace('..',np.nan)
    df_GDP_value=df_GDP_value.fillna(method='ffill',axis=1)
    df_GDP_value=df_GDP_value.fillna(method='bfill',axis=1)
    df_GDP_value=df_GDP_value.fillna(0)

    df_GDP_value['GDP-SUM'] = df_GDP_value.apply(lambda x: x.sum(), axis=1)
    df_GDP_final=DataFrame(df_GDP['Country code']).join(df_GDP_value)
    df_GDP_final=df_GDP_final.drop(df_GDP_final.columns[1:-1],axis=1)
    
    
    df_CO2=df_CO2.drop(df_CO2.columns[1:6],axis=1)
    
    df_CO2_value=df_CO2.drop(df_CO2.columns[0:1],axis=1)
    df_CO2_value=df_CO2_value.replace('..',np.nan)
    df_CO2_value=df_CO2_value.fillna(method='ffill',axis=1)
    df_CO2_value=df_CO2_value.fillna(method='bfill',axis=1)
    df_CO2_value=df_CO2_value.fillna(0)

    df_CO2_value['CO2-SUM'] = df_CO2_value.apply(lambda x: x.sum(), axis=1)
    df_CO2_final=DataFrame(df_CO2['Country code']).join(df_CO2_value)
    df_CO2_final=df_CO2_final.drop(df_CO2_final.columns[1:-1],axis=1)
    
    df_merge=pd.merge(df_CO2_final,df_GDP_final,on='Country code')

    df_merge=df_merge.set_index('Country code')
    
    df_min_max = (df_merge - df_merge.min()) / (df_merge.max() - df_merge.min())
    
    china=[float('%.3f'% df_min_max.loc['CHN'][0]),float('%.3f'% df_min_max.loc['CHN'][1])]

    fig, axes = plt.subplots()

    axes.set_xlabel('Countries')
    axes.set_ylabel('Values')
    axes.set_title('GDP-CO2')
    country_label=['CHN', 'USA', 'GBR', 'FRA','RUS']
    position_value=[]
    df_new=df_min_max.reset_index()
    for item in country_label:
        position = df_new[df_new['Country code']==item].index.tolist()[0]
        position_value.append(int(position))

    axes.set_xticks(position_value)
    axes.set_xticklabels(country_label,rotation=90)
    df_min_max.plot(ax=axes)
    plt.show()
	
    return axes,china

