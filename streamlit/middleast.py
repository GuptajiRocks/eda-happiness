import matplotlib.pyplot as plt
import pandas as pd

def country_dystopia_southasia(df):
    tempdf = df.loc[df["Region"] == "Latin America and Caribbean"]
    plt.figure(figsize=(10, 6))
    plt.bar(tempdf["Country"][:5], height=tempdf["Dystopia Residual"][:5])
    plt.show()
