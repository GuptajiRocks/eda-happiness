import matplotlib.pyplot as plt
import pandas as pd

def western_europe_comparison(df):
    tempdf = df.loc[df["Region"] == "Western Europe"]
    plt.figure(figsize=(10, 6))
    plt.bar(tempdf["Country"], height=tempdf["Freedom"])
    plt.show()