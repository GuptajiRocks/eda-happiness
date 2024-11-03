import pandas as pd
import matplotlib.pyplot as plt
# import streamlit as st

df = pd.read_csv("D:\\Bennett University\\Sem 3\\Projects\\DataScience\\trialone\\edac.csv")

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


middleast_compare()
