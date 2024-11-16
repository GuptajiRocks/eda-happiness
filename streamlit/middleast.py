import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def country_dystopia_me(df):
    tempdf = df.loc[df["Region"] == "Middle East and Northern Africa"]
    plt.figure(figsize=(10, 6))
    plt.bar(tempdf["Country"][:5], height=tempdf["Dystopia Residual"][:5])
    plt.title("Country Dystopia Score of Middle East Countries - Top 5")
    plt.xlabel("Countries")
    plt.ylabel("Dystopia Residual")
    plt.show()

def middleast_compare(df):
    tempdf = df.loc[df["Region"] == "Middle East and Northern Africa"]
    # print(tempdf)
    plt.figure(figsize=(10, 6))
    plt.bar(tempdf["Country"], height=tempdf["Freedom"])
    plt.show()

def gdp_vs_trust_me(df):
    tempdf = df[["Country","Region", "Economy", "Trust"]]
    cols_to_normalize = ['Economy', 'Trust']
    scaler = MinMaxScaler()
    tempdf[cols_to_normalize] = scaler.fit_transform(tempdf[cols_to_normalize])
    fdf = tempdf[tempdf['Region'] == "Middle East and Northern Africa"]
    jdf = fdf[["Country", "Economy", "Trust"]]
    jdf.plot(x="Country", kind="bar", figsize=(10,6))
    plt.title('GDP and Trust Score - Middle East')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def freedom_vs_trust_me(df):
    tempdf = df[["Country","Region", "Freedom", "Trust"]]
    cols_to_normalize = ['Freedom', 'Trust']
    scaler = MinMaxScaler()
    tempdf[cols_to_normalize] = scaler.fit_transform(tempdf[cols_to_normalize])
    fdf = tempdf[tempdf['Region'] == "Middle East and Northern Africa"]
    jdf = fdf[["Country", "Freedom", "Trust"]]
    jdf.plot(x="Country", kind="bar", figsize=(10,6))
    plt.title('Freedom vs Trust Score - Middle East')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()
