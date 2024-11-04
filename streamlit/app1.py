import pandas as pd
import matplotlib.pyplot as plt
# import streamlit as st

df = pd.read_csv("D:\\Bennett University\\Sem 3\\Projects\\DataScience\\trialone\\dataset\\edac.csv")

def distinct_region():
    templ = df["Region"]
    tempset = set(templ)
    return list(tempset)

unique_regions = distinct_region()
print(unique_regions)

def western_europe_comparison():
    tempdf = df.loc[df["Region"] == "Western Europe"]
    plt.figure(figsize=(10, 6))
    plt.bar(tempdf["Country"], height=tempdf["Freedom"])
    plt.show()
    # print(tempdf)

def middleast_compare():
    tempdf = df.loc[df["Region"] == "Middle East and Northern Africa"]
    # print(tempdf)
    plt.figure(figsize=(10, 6))
    plt.bar(tempdf["Country"], height=tempdf["Freedom"])
    plt.show()

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


latin_america_compare()
    
