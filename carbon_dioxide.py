import pandas as pd
import numpy as np
from pandas import DataFrame

def co2():
    df_climate_Data = pd.read_excel("ClimateChange.xlsx", sheetname='Data')
    df_climate_Country = pd.read_excel("ClimateChange.xlsx", sheetname='Country')

    df_country=df_climate_Country[['Country name','Income group']]
    df_data=df_climate_Data[(df_climate_Data['Series code']=='EN.ATM.CO2E.KT')]

    df_data=DataFrame(df_data['Country name']).join(df_data[df_data.columns[6:]])

    df_merge=pd.merge(df_country,df_data,on='Country name')

    df_value=df_merge[df_merge.columns[2:]]
    df_value=df_value.replace('..',np.nan)
    df_value=df_value.fillna(method='ffill',axis=1)
    df_value=df_value.fillna(method='bfill',axis=1)
    df_value['Col_sum'] = df_value.apply(lambda x: x.sum(), axis=1)

    df_value['Country name']=df_merge['Country name']
    df_value['Income group']=df_merge['Income group']
    
    df_value=df_value.dropna()
    
    df_clean=df_value.drop(df_value.columns[0:-3],axis=1)
    
    df_group=df_clean.groupby(by=['Income group','Country name']).sum()
    
    df_hio=df_group.loc['High income: OECD',:].sort_values(by='Col_sum',ascending=False)
    
    hio_data=[]
    hio_data.append(float(df_hio.sum()))
    
    df_hio=df_hio.reset_index()
    hio_data.append(df_hio.iloc[0,0])
    hio_data.append(df_hio.iloc[0,1])
    hio_data.append(df_hio.iloc[-1,0])
    hio_data.append(df_hio.iloc[-1,1])
    
    df_hii=df_group.loc['High income: nonOECD',:].sort_values(by='Col_sum',ascending=False)
    
    hii_data=[]
    hii_data.append(float(df_hii.sum()))
    df_hii=df_hii.reset_index()
    hii_data.append(df_hii.iloc[0,0])
    hii_data.append(df_hii.iloc[0,1])
    hii_data.append(df_hii.iloc[-1,0])
    hii_data.append(df_hii.iloc[-1,1])
    
    df_low=df_group.loc['Low income',:].sort_values(by='Col_sum',ascending=False)
    
    low_data=[]
    low_data.append(float(df_low.sum()))
    df_low=df_low.reset_index()
    low_data.append(df_low.iloc[0,0])
    low_data.append(df_low.iloc[0,1])
    low_data.append(df_low.iloc[-1,0])
    low_data.append(df_low.iloc[-1,1])
    
    df_lmi=df_group.loc['Lower middle income',:].sort_values(by='Col_sum',ascending=False)
     
    lmi_data=[]
    lmi_data.append(float(df_lmi.sum()))
    df_lmi=df_lmi.reset_index()
    lmi_data.append(df_lmi.iloc[0,0])
    lmi_data.append(df_lmi.iloc[0,1])
    lmi_data.append(df_lmi.iloc[-1,0])
    lmi_data.append(df_lmi.iloc[-1,1]) 
    
    df_umi=df_group.loc['Upper middle income',:].sort_values(by='Col_sum',ascending=False)
     
    umi_data=[]
    umi_data.append(float(df_umi.sum()))
    df_umi=df_umi.reset_index()
    umi_data.append(df_umi.iloc[0,0])
    umi_data.append(df_umi.iloc[0,1])
    umi_data.append(df_umi.iloc[-1,0])
    umi_data.append(df_umi.iloc[-1,1]) 
    
    s_final=np.vstack((hio_data,hii_data,low_data,lmi_data,umi_data))
    df_final=DataFrame(s_final,columns=['Sum emissions','Highest emission country','Highest emissions','Lowest emission country','Lowest emissions'])
    list_group=['High income: OECD','High income: nonOECD','Low income','Lower middle income','Upper middle income']
    df_final['Income group']=list_group
    df_final=df_final.set_index('Income group')
    df_final['Sum emissions']=df_final['Sum emissions'].astype('float')
    df_final['Highest emissions']=df_final['Highest emissions'].astype('float')
    df_final['Lowest emissions']=df_final['Lowest emissions'].astype('float')

    print(df_final)

    return df_final

if __name__=='__main__':
    co2()
