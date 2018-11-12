import pandas as pd

def clean():

    df_clean = None
    df=pd.read_csv('earthquake.csv')
    df1=df.place.str.split(', ', 1, expand=True)
    df2=df1[df1.columns[1]]
    df_new = df.loc[:,['time','latitude','longitude','depth','mag']]
    df_new['region']=df2
    df_clean=df_new.dropna().drop_duplicates()

    return df_clean

if __name__=='__main__':
    print(clean())
