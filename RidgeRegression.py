import pandas as pd
import numpy as np
data = pd.read_csv(r"C:\Users\Annika\Desktop\Techlabs Project\TL-Group-7\without_Nans.csv")
ind = np.arange(61)
data = data.set_index(ind, drop=False)
data.drop(columns='Region', inplace=True)
data.drop(columns='Unnamed: 0.1', inplace=True)
data = data.astype(float)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

X = data.drop('suicides_no',1)
y = data['suicides_no']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.1,random_state=5)
reg = Ridge()
reg.fit(X_train,y_train)
y_pred = reg.predict(X_test)
print(y_pred)
print(y_test)
print(reg.score(y_pred, y_test))