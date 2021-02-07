import pandas as pd
data_happy = pd.read_csv("2015.csv", index_col="Country")
print(data_happy)


data_sad = pd.read_csv("who_suicide_statistics.csv")
data_sad = data_sad.sort_index()
print(data_sad.head())
print(data_sad.tail())

years_to_use = data_sad[data_sad.year == 2015]
years_to_use = years_to_use.copy()

repl_countries = {"Republic of Korea": "South Korea", "Russian Federation": "Russia",
                  "Republic of Moldova": "Moldova",
                  "United States of America": "United States",
                  "Occupied Palestinian Territory": "Palestinian Territories",
                  "Iran (Islamic Rep of)": "Iran",
                  "Hong Kong SAR": "Hong Kong"}

for key, value in repl_countries.items():
    years_to_use.loc[years_to_use.country == key, "country"] = value


years_to_use2 = years_to_use.dropna(subset=["suicides_no"])
print(years_to_use2)
ytu_group2 = years_to_use2.groupby(["country"]).sum()
ytu_group2 = ytu_group2.drop(columns=["year"])
print(ytu_group2)

complete = pd.concat([data_happy, ytu_group2], axis=1)
print(complete)
complete.to_csv("complete6.csv")
