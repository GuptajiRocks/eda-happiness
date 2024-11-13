import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

# Importing differnt files from directories and their functions
from middleast import *
from missfunc import *

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

def western_europe_comparison():
    tempdf = df.loc[df["Region"] == "Western Europe"]
    plt.figure(figsize=(10, 6))
    plt.bar(tempdf["Country"], height=tempdf["Freedom"])
    plt.show()
    # print(tempdf)

def north_america_compare():
    tempdf = df.loc[df["Region"] == "North America"]
    plt.figure(figsize=(10, 6))
    plt.subplot(1,2,1)
    plt.bar(tempdf["Country"], height=tempdf["Freedom"])
    plt.xlabel("Countries")
    plt.ylabel("Freedom Rating")
    plt.subplot(1,2,2)
    plt.bar(tempdf["Country"], height=tempdf["Economy (GDP per Capita)"])
    plt.xlabel("Countries")
    plt.ylabel("Economy (GDP Per Capita)")
    plt.show()

def latin_america_compare():
    tempdf = df.loc[df["Region"] == "Latin America and Caribbean"]
    plt.figure(figsize=(10, 6))
    plt.subplot(1,2,1)
    plt.bar(tempdf["Country"], height=tempdf["Freedom"])
    plt.xlabel("Countries")
    plt.ylabel("Freedom Rating")
    plt.subplot(1,2,2)
    plt.bar(tempdf["Country"], height=tempdf["Economy (GDP per Capita)"])
    plt.xlabel("Countries")
    plt.ylabel("Economy (GDP Per Capita)")
    plt.show()

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
    tempdf = df[["Country", "Economy (GDP per Capita)", "Trust"]]
    tempdf.plot(x="Country", kind="bar", figsize=(10,6))
    plt.title('GDP and Trust Score by Country')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

compare_economy_trust()