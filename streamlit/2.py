import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


st.title("World Happiness Report - Exploratory Data Analysis")
uploaded_file = "D:\\Bennett University\\Sem 3\\Projects\\DataScience\\trialone\\dataset\\edac.csv"

df = pd.read_csv(uploaded_file)
st.write("### Data Preview")
st.dataframe(df.head())

st.sidebar.header("Data Overview")
if st.sidebar.checkbox("Show Data Summary"):
    st.write("### Summary Statistics")
    st.write(df.describe())

st.sidebar.header("Data Information")
if st.sidebar.checkbox("Show data information"):
    st.write("Dataset information")
    df_info_string = df.info(memory_usage='deep')
    st.write(df_info_string)

if st.sidebar.checkbox("Show Missing Values"):
    st.write("### Missing Values in Each Column")
    st.write(df.isnull().sum())

st.sidebar.header("Column Analysis")
selected_column = st.sidebar.selectbox("Select a column", df.columns)

if st.sidebar.checkbox("Show Value Counts"):
    st.write(f"### Value Counts for {selected_column}")
    st.write(df[selected_column].value_counts())

st.sidebar.header("Correlation Analysis")
if st.sidebar.checkbox("Show Correlation Matrix and Heatmap"):
    corr_matrix = df.corr()
    st.write("### Correlation Matrix")
    st.write(corr_matrix)
    st.write("### Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

st.sidebar.header("Histogram")
if st.sidebar.checkbox("Show Histogram"):
    bins = st.sidebar.slider("Number of Bins", 5, 100, 30)
    fig, ax = plt.subplots()
    sns.histplot(df[selected_column], bins=bins, kde=True, ax=ax)
    st.write(f"### Histogram for {selected_column}")
    st.pyplot(fig)

st.sidebar.header("Boxplot")
if st.sidebar.checkbox("Show Boxplot"):
    fig, ax = plt.subplots()
    sns.boxplot(x=df[selected_column], ax=ax)
    st.write(f"### Boxplot for {selected_column}")
    st.pyplot(fig)

st.sidebar.header("Scatter Plot")
numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
x_axis = st.sidebar.selectbox("Select X-axis", numeric_columns, index=numeric_columns.index("Economy (GDP per Capita)"))
y_axis = st.sidebar.selectbox("Select Y-axis", numeric_columns, index=numeric_columns.index("Happiness Score"))

if st.sidebar.checkbox("Show Scatter Plot"):
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
    st.write(f"### Scatter Plot: {x_axis} vs {y_axis}")
    st.pyplot(fig)

st.sidebar.header("Pairplot")
if st.sidebar.checkbox("Show Pairplot"):
    selected_pairplot_columns = st.sidebar.multiselect("Select columns for pairplot", numeric_columns, default=numeric_columns[:4])
    if selected_pairplot_columns:
        st.write("### Pairplot")
        pairplot_fig = sns.pairplot(df[selected_pairplot_columns])
        st.pyplot(pairplot_fig)

st.sidebar.header("Bar Plot")
if st.sidebar.checkbox("Show Bar Plot"):
    selected_barplot_columns = st.sidebar.selectbox("Select columns for BarPlot", numeric_columns)
    if selected_barplot_columns:
        fig, ax = plt.subplots()
        st.write("Bar Plot")
        sns.barplot(x=df[selected_barplot_columns])
        st.pyplot(fig)

st.sidebar.header("Line Plot")
if st.sidebar.checkbox("Show Line Plot"):
    selected_line_plot = st.sidebar.selectbox("Select columns to plot")
    
