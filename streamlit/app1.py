import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Importing differnt files from directories and their functions
from middleast import *
from missfunc import *
from westeur import *
from northamerica import *

# class filer_df:
#     def __init__(self):
#         df = pd.read_csv("D:\\Bennett University\\Sem 3\\Projects\\DataScience\\trialone\\dataset\\edac.csv")
    
#     def df_return():
#         return df

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
    cols_to_normalize = ['Economy', 'Trust']
    scaler = MinMaxScaler()
    tempdf[cols_to_normalize] = scaler.fit_transform(tempdf[cols_to_normalize])
    tempdf = tempdf.groupby("Region").mean().reset_index()
    tempdf.plot(x="Region", kind="bar", figsize=(10,6))
    plt.title('GDP and Trust Score by Country')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

freedom_vs_trust_me(df)