import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

def rule():
    df_data=pd.read_csv('shopping_data.csv',header=None)
    dataset=[]
    for i in range(len(df_data)):
        list_data=list(df_data.loc[i])
        list_no_nan=[]
        for j in range(len(list_data)):
            if isinstance(list_data[j],float):
                break
            else:
                list_no_nan.append(list_data[j])
        dataset.append(list_no_nan)

    te = TransactionEncoder() 
    te_ary = te.fit_transform(dataset) 
    df_te = pd.DataFrame(te_ary, columns=te.columns_)  
    frequent_itemsets = apriori(df_te, min_support=0.05, use_colnames=True)
    association_rules_df=association_rules(frequent_itemsets, metric="confidence", min_threshold=0.2)
    print(frequent_itemsets)
    print(association_rules_df)
    return frequent_itemsets,association_rules_df

if __name__=='__main__':
    rule()


