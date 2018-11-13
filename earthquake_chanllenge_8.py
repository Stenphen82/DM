import pandas as pd
from pandas import DataFrame

def clean():

    df_clean = None
    df=pd.read_csv('earthquake.csv')
    df1=df.place.str.split(', ', 1, expand=True)
    df2=df1[df1.columns[1]]
    df_new = df.loc[:,['time','latitude','longitude','depth','mag']]
    df_new['region']=df2
    df_clean=df_new.dropna().drop_duplicates()

    return df_clean


def mag_region():
    df_clean = clean()
    df_clean['mag_sep']=pd.cut(df_clean.mag,bins=[0,2,5,7,9,20],right=False,labels=['micro','light','strong','major','great'])
    df_mag=df_clean[['mag_sep','region']]
    df_mag['times']=1
    df_mag=df_mag.groupby(by=['mag_sep','region']).sum() 
    df_mag=df_mag.dropna()

    df_micro=df_mag.loc['micro',:].sort_values(by='times',ascending=False)
    df_micro['mag']='micro'
    df_light=df_mag.loc['light',:].sort_values(by='times',ascending=False)
    df_light['mag']='light'
    df_strong=df_mag.loc['strong',:].sort_values(by='times',ascending=False)
    df_strong['mag']='strong'
    df_major=df_mag.loc['major',:].sort_values(by='times',ascending=False)
    df_major['mag']='major'
    df_great=df_mag.loc['great',:].sort_values(by='times',ascending=False)
    df_great['mag']='great'

    df_mag=pd.concat([df_micro.iloc[:1],df_light.iloc[:1],df_strong.iloc[:1],df_major.iloc[:1],df_great.iloc[:1]])
    df_final=df_mag.reset_index().set_index('mag')
    df_final.times=df_final.times.astype('int')
    print(df_final)
    return df_final

if __name__=='__main__':
    mag_region()
