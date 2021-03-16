import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso

#Load happiness report
happiness = pd.read_csv(r"C:\Users\User\Desktop\TL-Group-7-main\TL-Group-7-main\without_Nans.csv")
ind =np.arange(61)
happiness = happiness.set_index(ind, drop =False)
happiness.drop(columns='Region', inplace=True)
happiness.drop(columns='Unnamed: 0.1', inplace=True)
happiness = happiness.astype(float)


X = happiness.drop('suicides_no',1)
y= happiness['suicide_no']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=6)
# Create an instance of Lasso Regression implementation
lasso = Lasso(alpha=1.0)
# Fit the Lasso model
lasso.fit(X_train, y_train)
# Create the model score
lasso.score(X_test, y_test), lasso.score(X_train, y_train)
