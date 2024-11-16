import matplotlib.pyplot as plt
import pandas as pd

def north_america_compare(df):
    tempdf = df.loc[df["Region"] == "North America"]
    plt.figure(figsize=(10, 6))
    plt.subplot(1,2,1)
    plt.bar(tempdf["Country"], height=tempdf["Freedom"])
    plt.xlabel("Countries")
    plt.ylabel("Freedom Rating")
    plt.subplot(1,2,2)
    plt.bar(tempdf["Country"], height=tempdf["Economy"])
    plt.xlabel("Countries")
    plt.ylabel("Economy (GDP Per Capita)")
    plt.show()