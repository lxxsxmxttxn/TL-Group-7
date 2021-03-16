# Import all libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the happiness dataset
happiness = pd.read_csv("./Suicide Score.csv")
happiness = happiness.dropna(subset=["suicide score"])

# initialize the error, starting with no error
sum_error = 0

# How many runs are we doing
amount_runs = 10

# Loop number of runs
for i in range(amount_runs):

    # shuffle our data
    happiness = happiness.sample(frac=1)
    suicides = happiness["suicide score"]
    hap_score = happiness["Happiness Score"]

    # x is our input, y is our output
    x = np.nan_to_num(hap_score, posinf=10)
    y = np.nan_to_num(suicides, posinf=1)

    # Last 20 entries will be our test data
    happiness_X_train = x[:-20].reshape(-1, 1)
    happiness_X_test = x[-20:].reshape(-1, 1)

    suc_y_train = y[:-20]
    suc_y_test = y[-20:]

    # Create linear regression object
    # Change the model
    regr = linear_model.Ridge()
    # Train the model using the training sets
    regr.fit(happiness_X_train, suc_y_train)

    # Make predictions using the testing set
    suc_y_pred = regr.predict(happiness_X_test)

    # Add it to our error
    sum_error += mean_squared_error(suc_y_test, suc_y_pred)

# The error average over the number of runs
avg_error = (sum_error / amount_runs)

print("Mean squared error over all runs: %.2f"
          % avg_error)