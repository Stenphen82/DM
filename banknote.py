import pandas as pd
import numpy as np
from sklearn.svm import SVC

def get_accuracy(test_labels, pred_labels):
    correct = np.sum(test_labels == pred_labels) 
    n = len(test_labels)
    acc = correct/n
    print(acc)
    return acc


def identify():
    df_train=pd.read_csv('banknote_train.csv')
    df_test=pd.read_csv('banknote_test.csv')
    
    train_data = df_train.iloc[:, :-1]
    train_target=df_train['class']

    model = SVC() 
    model.fit(train_data, train_target) 
    predict=model.predict(train_data)
    get_accuracy(train_target,predict)    
    
    predict=model.predict(df_test)

    df_test['class']=predict.reshape(-1,1)
    return df_test

if __name__=='__main__':
    identify()
