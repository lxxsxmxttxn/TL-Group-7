import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import 2015 happiness data
data_happy = pd.read_csv("2015.csv", index_col="Country")
data_happy = data_happy.rename_axis("Country")
print(data_happy)

# import complete suicide data
data_sad = pd.read_csv("who_suicide_statistics.csv")
data_sad = data_sad.sort_index()
print(data_sad.head())
print(data_sad.tail())

# add oversea territories etc. to the main countries and fix naming differences
repl_countries = {"Republic of Korea": "South Korea", "Russian Federation": "Russia",
                  "Republic of Moldova": "Moldova",
                  "United States of America": "United States",
                  "Occupied Palestinian Territory": "Palestinian Territories",
                  "Iran (Islamic Rep of)": "Iran",
                  "Hong Kong SAR": "Hong Kong",
                  "Anguilla": "United Kingdom",
                  "Aruba": "Netherlands",
                  "Bermuda": "United Kingdom",
                  "Montserrat": "United Kingdom",
                  "Puerto Rico": "United States",
                  "Rodrigues": "Mauritius",
                  "Virgin Islands (USA)": "United States",
                  "Syrian Arab Republic": "Syria",
                  "Venezuela (Bolivarian Republic of)": "Venezuela",
                  "Reunion": "France",
                  "Netherlands Antilles": "Netherlands",
                  "French Guiana": "France",
                  "TFYR Macedonia": "North Macedonia"}

for key, value in repl_countries.items():
    data_sad.loc[data_sad.country == key, "country"] = value

# filter suicide data for only 2015 values
years_to_use = data_sad[data_sad.year == 2015]
years_to_use = years_to_use.copy()

# clean 2015 suicide data
years_to_use2 = years_to_use.dropna(subset=["suicides_no"])
print(years_to_use2)
ytu_group2 = years_to_use2.groupby(["country"]).sum()
ytu_group2 = ytu_group2.drop(columns=["year"])
print(ytu_group2)

# put the two dfs together and save as csv
complete = pd.concat([data_happy, ytu_group2], axis=1)
print(complete)
complete.to_csv("complete7.csv")


# get the average suicide data for all years
sad_2 = data_sad.dropna(subset=["suicides_no"])
sad_2 = sad_2.groupby(["country", "year"]).sum()
sad_2 = sad_2.groupby(["country"]).mean()
sad_2.to_csv("sad_avg.csv")

# get average happiness data for all years
data_happy16 = pd.read_csv("2016.csv", index_col="Country")
data_happy16 = data_happy16.rename_axis("Country")

data_happy17 = pd.read_csv("2017.csv", index_col="Country")
data_happy17 = data_happy17.rename_axis("Country")
data_happy17.rename(columns={"Happiness.Score": "Happiness Score",
                             "Happiness.Rank": "Happiness Rank",
                             "Economy..GDP.per.Capita.": "Economy (GDP per Capita)",
                             "Health..Life.Expectancy.": "Health (Life Expectancy)",
                             "Trust..Government.Corruption.": "Trust (Government Corruption)",
                             "Dystopia.Residual": "Dystopia Residual"}, inplace=True)

data_happy18 = pd.read_csv("2018.csv", index_col="Country or region")
data_happy18 = data_happy18.rename_axis("Country")
data_happy18.rename(columns={"Score": "Happiness Score",
                             "Overall rank": "Happiness Rank",
                             "GDP per capita": "Economy (GDP per Capita)",
                             "Healthy life expectancy": "Health (Life Expectancy)",
                             "Freedom to make life choices": "Freedom",
                             "Perceptions of corruption": "Trust (Government Corruption)"}, inplace=True)

data_happy19 = pd.read_csv("2019.csv", index_col="Country or region")
data_happy19 = data_happy19.rename_axis("Country")
data_happy19.rename(columns={"Score": "Happiness Score",
                             "Overall rank": "Happiness Rank",
                             "GDP per capita": "Economy (GDP per Capita)",
                             "Healthy life expectancy": "Health (Life Expectancy)",
                             "Freedom to make life choices": "Freedom",
                             "Perceptions of corruption": "Trust (Government Corruption)"}, inplace=True)

data_happy20 = pd.read_csv("2020.csv", index_col="Country name")
data_happy20 = data_happy20.rename_axis("Country")
data_happy20.rename(columns={"Ladder score": "Happiness Score",
                             "Standard error of ladder score": "Standard Error",
                             "Logged GDP per capita": "Economy (GDP per Capita)",
                             "Healthy life expectancy": "Health (Life Expectancy)",
                             "Freedom to make life choices": "Freedom",
                             "Perceptions of corruption": "Trust (Government Corruption)",
                             "Dystopia + residual": "Dystopia Residual"}, inplace=True)

all_happy = data_happy.append([data_happy16, data_happy17, data_happy18, data_happy19, data_happy20])
all_happy = all_happy.groupby(["Country"]).mean()

# drop all columns that don't appear in all dfs
columns_to_keep = ["Happiness Rank", "Happiness Score", "Standard Error", "Economy (GDP per Capita)",
                   "Health (Life Expectancy)", "Freedom", "Trust (Government Corruption)", "Generosity",
                   "Dystopia Residual"]
all_happy = all_happy[columns_to_keep]
all_happy.to_csv("happy_avg.csv")

# complete average data, save as csv
complete_avg = pd.concat([all_happy, sad_2], axis=1)
complete_avg.to_csv("complete_avg.csv")

# linear regression try
sns.lmplot(x="Happiness Score", y="suicides_no", data=complete)
plt.show()
