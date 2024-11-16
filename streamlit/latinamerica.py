import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def latin_america_compare(df):
    tempdf = df.loc[df["Region"] == "Latin America and Caribbean"]
    plt.figure(figsize=(10, 6))
    plt.subplot(1,2,1)
    plt.bar(tempdf["Country"][:7], height=tempdf["Freedom"][:7])
    plt.xlabel("Countries")
    plt.ylabel("Freedom Rating")
    plt.subplot(1,2,2)
    plt.bar(tempdf["Country"][:7], height=tempdf["Economy"][:7])
    plt.xlabel("Countries")
    plt.ylabel("Economy (GDP Per Capita)")
    plt.show()

def country_dystopia_la(df):
    tempdf = df.loc[df["Region"] == "Latin America and Caribbean"]
    plt.figure(figsize=(10, 6))
    plt.bar(tempdf["Country"][:5], height=tempdf["Dystopia Residual"][:5])
    plt.title("Country Dystopia Score of Latin American Countries - Top 5")
    plt.xlabel("Countries")
    plt.ylabel("Dystopia Residual")
    plt.show()

def la_compare(df):
    tempdf = df.loc[df["Region"] == "Latin America and Caribbean"]
    # print(tempdf)
    plt.figure(figsize=(10, 6))
    plt.bar(tempdf["Country"], height=tempdf["Freedom"])
    plt.show()

def gdp_vs_trust_la(df):
    tempdf = df[["Country","Region", "Economy", "Trust"]]
    cols_to_normalize = ['Economy', 'Trust']
    scaler = MinMaxScaler()
    tempdf[cols_to_normalize] = scaler.fit_transform(tempdf[cols_to_normalize])
    fdf = tempdf[tempdf['Region'] == "Latin America and Caribbean"]
    jdf = fdf[["Country", "Economy", "Trust"]]
    jdf.plot(x="Country", kind="bar", figsize=(10,6))
    plt.title('GDP and Trust Score - Latin America and Caribbean')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def freedom_vs_trust_la(df):
    tempdf = df[["Country","Region", "Freedom", "Trust"]]
    cols_to_normalize = ['Freedom', 'Trust']
    scaler = MinMaxScaler()
    tempdf[cols_to_normalize] = scaler.fit_transform(tempdf[cols_to_normalize])
    fdf = tempdf[tempdf['Region'] == "Latin America and Caribbean"]
    jdf = fdf[["Country", "Freedom", "Trust"]]
    jdf.plot(x="Country", kind="bar", figsize=(10,6))
    plt.title('Freedom vs Trust Score - Latin America and Caribbean')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def eco_vs_heal_la(df):
    tempdf = df[["Country","Region", "Economy", "Health"]]
    cols_to_normalize = ['Economy', 'Health']
    scaler = MinMaxScaler()
    tempdf[cols_to_normalize] = scaler.fit_transform(tempdf[cols_to_normalize])
    fdf = tempdf[tempdf['Region'] == "Latin America and Caribbean"]
    jdf = fdf[["Country", "Economy", "Health"]]
    jdf.plot(x="Country", kind="bar", figsize=(10,6))
    plt.title('GDP vs Health Index - Latin America and Caribbean')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def eco_vs_geno_la(df):
    tempdf = df[["Country","Region", "Economy", "Generosity"]]
    cols_to_normalize = ['Economy', 'Generosity']
    scaler = MinMaxScaler()
    tempdf[cols_to_normalize] = scaler.fit_transform(tempdf[cols_to_normalize])
    fdf = tempdf[tempdf['Region'] == "Latin America and Caribbean"]
    jdf = fdf[["Country", "Economy", "Generosity"]]
    jdf.plot(x="Country", kind="bar", figsize=(10,6))
    plt.title('GDP vs Generosity Index - Latin America and Caribbean')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def fam_vs_rank_la(df):
    # need to sort the array so as to find a median.
    tempdf = df[["Country","Region", "Family", "Happiness Score"]]
    tempdf = tempdf.sort_values(by="Family")
    cols_to_normalize = ["Family", "Happiness Score"]
    scaler = MinMaxScaler()
    tempdf[cols_to_normalize] = scaler.fit_transform(tempdf[cols_to_normalize])
    fdf = tempdf[tempdf['Region'] == "Latin America and Caribbean"]
    jdf = fdf[["Country", "Family", "Happiness Score"]]
    jdf.plot(x="Country", kind="bar", figsize=(10,6))
    plt.title('Family Index vs Happiness Score - Latin America and Caribbean')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def corr_bw_fam_and_rank_la(df):
    tempdf = df[["Country","Region", "Family", "Happiness Score"]]
    tempdf = tempdf.sort_values(by="Family")
    fdf = tempdf[tempdf['Region'] == "Latin America and Caribbean"]
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
