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
    fdf = tempdf[tempdf['Region'] == "Central and Eastern Europe"]
    jdf = fdf[["Country", "Freedom", "Trust"]]
    jdf.plot(x="Country", kind="bar", figsize=(10,6))
    plt.title('Freedom vs Trust Score - Central and Eastern Europe')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def eco_vs_heal_me(df):
    tempdf = df[["Country","Region", "Economy", "Health"]]
    cols_to_normalize = ['Economy', 'Health']
    scaler = MinMaxScaler()
    tempdf[cols_to_normalize] = scaler.fit_transform(tempdf[cols_to_normalize])
    fdf = tempdf[tempdf['Region'] == "Middle East and Northern Africa"]
    jdf = fdf[["Country", "Economy", "Health"]]
    jdf.plot(x="Country", kind="bar", figsize=(10,6))
    plt.title('GDP vs Health Index - Middle East')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def eco_vs_geno_me(df):
    tempdf = df[["Country","Region", "Economy", "Generosity"]]
    cols_to_normalize = ['Economy', 'Generosity']
    scaler = MinMaxScaler()
    tempdf[cols_to_normalize] = scaler.fit_transform(tempdf[cols_to_normalize])
    fdf = tempdf[tempdf['Region'] == "Central and Eastern Europe"]
    jdf = fdf[["Country", "Economy", "Generosity"]]
    jdf.plot(x="Country", kind="bar", figsize=(10,6))
    plt.title('GDP vs Generosity Index - Central and Eastern Europe')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def fam_vs_rank_me(df):
    # need to sort the array so as to find a median.
    tempdf = df[["Country","Region", "Family", "Happiness Score"]]
    tempdf = tempdf.sort_values(by="Family")
    cols_to_normalize = ["Family", "Happiness Score"]
    scaler = MinMaxScaler()
    tempdf[cols_to_normalize] = scaler.fit_transform(tempdf[cols_to_normalize])
    fdf = tempdf[tempdf['Region'] == "Middle East and Northern Africa"]
    jdf = fdf[["Country", "Family", "Happiness Score"]]
    jdf.plot(x="Country", kind="bar", figsize=(10,6))
    plt.title('Family Index vs Happiness Score - Middle East')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def corr_bw_fam_and_rank_me(df):
    tempdf = df[["Country","Region", "Family", "Happiness Score"]]
    tempdf = tempdf.sort_values(by="Family")
    fdf = tempdf[tempdf['Region'] == "Middle East and Northern Africa"]
    jdf = fdf[["Country", "Family", "Happiness Score"]]
    corr_val = jdf["Family"].corr(df["Happiness Score"])

    if corr_val > 0.7:
        print(f"The corrleation value of: {corr_val} indicates a strong positive correlation")
    elif corr_val < 0.7 and corr_val > 0.5:
        print(f"The corrleation value of: {corr_val} indicates a weak positive correlation")
    elif corr_val > 0.3 and corr_val < 0.5:
        print(f"The corrleation value of: {corr_val} indicates a weak negative correlation")
    else:
        print(f"The corrleation value of: {corr_val} indicates a strong negative correlation")


def boxp_me(df):
    tempdf = df.loc[df["Region"] == "Middle East and Northern Africa"]
    tempdf.boxplot(column="Economy", by="Happiness Score", figsize=(15,15))
    plt.title("Boxplot between Economy and Happiness Score - Middle East")
    plt.show()


