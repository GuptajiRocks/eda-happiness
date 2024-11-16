import matplotlib.pyplot as plt
import pandas as pd

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