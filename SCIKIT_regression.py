import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the happiness dataset
happiness = pd.read_csv("C:/Users/leslee.barrios/Desktop/Tech Labs/PROJECT/TL-Group-7-main/complete6.csv")
print(happiness)

# iterating the columns
for col in happiness.columns:
    print(col)

suicides = happiness["suicides_no"]
population = happiness["population"]
hap_score = happiness["Happiness Score"]
freedom = happiness["Freedom"]

x = np.nan_to_num(hap_score)
y = np.nan_to_num(suicides)

# Use only one feature
# happiness_X = happiness.data[:, np.newaxis, 2]
# Split the data into training/testing sets
happiness_X_train = x[:-20].reshape(-1, 1)
happiness_X_test = x[-20:].reshape(-1, 1)
# print(happiness_X_train)
# Split the targets into training/testing sets
# happiness_y_train = happiness.target[:-20]
# happiness_y_test = happiness.target[-20:]
happiness_y_train = y[:-20]
happiness_y_test = y[-20:]
# Create linear regression object
regr = linear_model.LinearRegression()
# Train the model using the training sets
regr.fit(happiness_X_train, happiness_y_train)

# Make predictions using the testing set
happiness_y_pred = regr.predict(happiness_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(happiness_y_test, happiness_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(happiness_y_test, happiness_y_pred))

# Plot outputs
plt.scatter(happiness_X_test, happiness_y_test, color='black')
plt.plot(happiness_X_test, happiness_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
