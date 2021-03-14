import pandas as pd

data = pd.read_csv("complete7.csv")
print(data)

score_calculation = data["suicides_no"] / data["population"] *1000
data["suicide score"] = score_calculation
print(data)

data.to_csv(r'C:\Users\ADZ26\PycharmProjects\pythonProject2\Suicide Score.csv', index = False)