import pandas as pd
import matplotlib.pyplot as plt
# import streamlit as st

df = pd.read_csv("D:\\Bennett University\\Sem 3\\Projects\\DataScience\\trialone\\edac.csv")

def distinct_region():
    templ = df["Region"]
    tempset = set(templ)
    return list(tempset)

# unique_regions = distinct_region()
# print(unique_regions)

tempdf = df.loc[df["Region"] == "Western Europe"]
plt.plot(tempdf["Region"])
plt.show()
