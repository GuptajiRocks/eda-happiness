import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache
def load_data():
    data = pd.read_csv("D:\\Bennett University\\Sem 3\\Projects\\DataScience\\trialone\\dataset\\edac.csv")
    return data

data = load_data()

# App title
st.title("Comprehensive Exploratory Data Analysis (EDA) App")
st.markdown("### Happiness Report Dataset")

# Sidebar options
st.sidebar.header("Navigation")
options = st.sidebar.radio(
    "Select Analysis Section",
    [
        "Dataset Overview",
        "Data Summaries",
        "Univariate Analysis",
        "Bivariate Analysis",
        "Multivariate Analysis",
        "Regional Analysis",
        "Custom Visualizations",
    ],
)

# Dataset Overview
if options == "Dataset Overview":
    st.header("Dataset Overview")
    st.write("### Dataset Preview")
    st.write(data.head())
    st.write("### Missing Values")
    st.write(data.isnull().sum())

# Data Summaries
if options == "Data Summaries":
    st.header("Data Summaries")
    st.write("### Descriptive Statistics")
    st.write(data.describe())
    st.write("### Categorical Columns Overview")
    for col in data.select_dtypes(include="object").columns:
        st.write(f"**{col}**:")
        st.write(data[col].value_counts())

# Univariate Analysis
if options == "Univariate Analysis":
    st.header("Univariate Analysis")
    column = st.selectbox("Select a column", data.select_dtypes(include=np.number).columns)
    st.write(f"### Distribution of {column}")
    plt.figure(figsize=(8, 4))
    sns.histplot(data[column], kde=True, color="green")
    plt.title(f"Distribution of {column}")
    st.pyplot(plt)

# Bivariate Analysis
if options == "Bivariate Analysis":
    st.header("Bivariate Analysis")
    x_col = st.selectbox("Select X-axis column", data.select_dtypes(include=np.number).columns)
    y_col = st.selectbox("Select Y-axis column", data.select_dtypes(include=np.number).columns)
    st.write(f"### Scatterplot: {x_col} vs {y_col}")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x=x_col, y=y_col, hue="Region")
    plt.title(f"{x_col} vs {y_col}")
    st.pyplot(plt)

# Multivariate Analysis
if options == "Multivariate Analysis":
    st.header("Multivariate Analysis")
    st.write("### Correlation Matrix")
    plt.figure(figsize=(10, 8))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    st.pyplot(plt)

# Regional Analysis
if options == "Regional Analysis":
    st.header("Regional Analysis")
    region = st.selectbox("Select a Region", data["Region"].unique())
    filtered_data = data[data["Region"] == region]
    st.write(f"### Happiness Score in {region}")
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Country", y="Happiness Score", data=filtered_data)
    plt.xticks(rotation=90)
    plt.title(f"Happiness Score in {region}")
    st.pyplot(plt)

# Custom Visualizations
if options == "Custom Visualizations":
    st.header("Custom Visualizations")
    plot_type = st.selectbox("Select Plot Type", ["Bar Plot", "Scatter Plot"])
    
    if plot_type == "Bar Plot":
        x_col = st.selectbox("Select X-axis column", data.columns)
        y_col = st.selectbox("Select Y-axis column", data.select_dtypes(include=np.number).columns)
        st.write(f"### Bar Plot: {x_col} vs {y_col}")
        plt.figure(figsize=(10, 6))
        sns.barplot(x=x_col, y=y_col, data=data)
        plt.xticks(rotation=90)
        st.pyplot(plt)
    
    elif plot_type == "Scatter Plot":
        x_col = st.selectbox("Select X-axis column", data.select_dtypes(include=np.number).columns, key="scatter_x")
        y_col = st.selectbox("Select Y-axis column", data.select_dtypes(include=np.number).columns, key="scatter_y")
        st.write(f"### Scatter Plot: {x_col} vs {y_col}")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=data, x=x_col, y=y_col)
        plt.title(f"{x_col} vs {y_col}")
        st.pyplot(plt)
