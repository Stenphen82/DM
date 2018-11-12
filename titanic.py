from matplotlib import pyplot as plt
import seaborn as sns

def plot():
    df = sns.load_dataset("titanic")
    fig, axes = plt.subplots(nrows=1, ncols=3,figsize=(15, 5))
    
    df1=df.age
    df2=df1.dropna()
    
    sns.distplot(df2,ax=axes[0])
    sns.countplot(x="sex", hue="alive",data=df,ax=axes[1])
    sns.countplot(x="class", hue="alive", data=df,ax=axes[2])
    plt.show()   
    return axes

if __name__=='__main__':
    plot()
