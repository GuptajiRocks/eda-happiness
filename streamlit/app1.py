import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Importing differnt files from directories and their functions
from middleast import *
from latinamerica import *
from westeur import *
from northamerica import *


# This file shall only contain the overall region based EDA
# rest all country based analysis is done in separate files and shall be called here in the form of a WAP

df = pd.read_csv("D:\\Bennett University\\Sem 3\\Projects\\DataScience\\trialone\\dataset\\edac.csv")

def distinct_region():
    templ = df["Region"]
    tempset = set(templ)
    return list(tempset)

def trial():
    unique_regions = distinct_region()
    print(unique_regions)


def happiness_score_plot():
    tempdf = df.groupby('Region')["Happiness Score"].mean().reset_index()
    plt.title("Region wise Happiness Score")
    plt.bar(tempdf["Region"], tempdf["Happiness Score"])
    plt.show()

def country_error():
    plt.bar(df["Country"], df["Standard Error"])
    plt.title("Displying the standard error in the report")
    plt.xlabel("Countries")
    plt.ylabel("Standard Error")
    plt.show()

def compare_economy_trust():
    tempdf = df[["Region", "Economy", "Trust"]]
    scaler = MinMaxScaler()
    cols_to_normalize = ['Economy']
    tempdf[cols_to_normalize] = scaler.fit_transform(tempdf[cols_to_normalize])
    tempdf = tempdf.groupby("Region").mean().reset_index()
    tempdf.plot(x="Region", kind="bar", figsize=(10,6))
    plt.title('GDP and Trust Score by Country')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def freedom_trust():
    tempdf = df[["Region", "Freedom", "Trust"]]
    scaler = MinMaxScaler()
    cols_to_normalize = ['Freedom', 'Trust']
    tempdf[cols_to_normalize] = scaler.fit_transform(tempdf[cols_to_normalize])
    tempdf = tempdf.groupby("Region").mean().reset_index()
    tempdf.plot(x="Region", kind="barh", figsize=(10,6))
    plt.title('GDP and Trust Score by Country')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def plot_correlation_matrix(tdata):
    data = tdata[["Economy","Family","Health","Freedom"]]
    plt.figure(figsize=(10, 8))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Correlation Matrix")
    plt.show()

def scatterplot_with_regression(data, x, y):
    plt.figure(figsize=(8, 6))
    sns.regplot(data=data, x=x, y=y, scatter_kws={"alpha": 0.6}, line_kws={"color": "red"})
    plt.title(f"Scatterplot with Regression: {x} vs {y}")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

scatterplot_with_regression(df, x="Economy", y="Freedom")