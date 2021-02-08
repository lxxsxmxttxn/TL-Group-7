import pandas as pd
import numpy as np


Happiness2015 = pd.read_csv("C://Users/leslee.barrios/Desktop/Tech Labs/PROJECT/Data/Happiness/2015.csv")
Happiness2016 = pd.read_csv("C://Users/leslee.barrios/Desktop/Tech Labs/PROJECT/Data/Happiness/2016.csv")
Suicide = pd.read_csv("C://Users/leslee.barrios/Desktop/Tech Labs/PROJECT/Data/who_suicide_statistics.csv")

print(Happiness2015.head())
print(Happiness2016.head())
print(Suicide)

suicide_2015 = Suicide[(Suicide['year'] == 2015) & (Suicide['suicides_no'] > 0.0)]
print(suicide_2015)
suicide_2016 = Suicide[(Suicide['year'] == 2016) & (Suicide['suicides_no'] > 0.0)]
print(suicide_2016)

suicide2015_grouped_country = suicide_2015.groupby('country')
mean_suicide2015 = suicide2015_grouped_country.mean()
mean_suicide2015 = mean_suicide2015.reset_index().reset_index()
suicide2015_final = mean_suicide2015.sort_values(by='suicides_no', ascending=False)
print(suicide2015_final)


suicide2016_grouped_country = suicide_2016.groupby('country')
mean_suicide2016 = suicide2016_grouped_country.mean()
mean_suicide2016 = mean_suicide2016.reset_index().reset_index()
suicide2016_final = mean_suicide2016.sort_values(by='suicides_no', ascending=False)
print(suicide2016_final)





