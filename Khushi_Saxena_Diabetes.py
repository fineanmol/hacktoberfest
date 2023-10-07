import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib 


df=pd.read_csv('diabetes.csv')
print(df.shape)
print (df.head(5))
print(df.isnull().values.any())






from sklearn.linear_model import LogisticRegression
xtrain=xtrain/xtrain.max()
xtest=xtest/xtest.max()
log=LogisticRegression(max_iter=10000)
log.fit(xtrain,ytrain)




log=LogisticRegression()
log.fit(xtrain,ytrain)
pred=log.predict(xtest)


test_acc=log.score(xtest,ytest)
test_acc

train_acc=log.score(xtrain,ytrain)
train_acc