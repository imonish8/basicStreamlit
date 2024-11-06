import streamlit as st
import pandas as pd
import plotly.express as px
from ucimlrepo import fetch_ucirepo


st.title("Streamlit Data Visualization App")
st.sidebar.header("Upload and Select Options")

uploaded_file = st.sidebar.file_uploader("data", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("## Data Preview")
    st.write(df.head())

    x_column = st.sidebar.selectbox("Select X-axis column", df.columns)
    y_column = st.sidebar.selectbox("Select Y-axis column", df.columns)

    plot_type = st.sidebar.selectbox("Select Plot Type", ["Line Plot", "Bar Plot", "Scatter Plot"])
    st.write("## Visualization")
    if plot_type == "Line Plot":
        fig = px.line(df, x=x_column, y=y_column, title=f"{plot_type} of {y_column} vs {x_column}")
    elif plot_type == "Bar Plot":
        fig = px.bar(df, x=x_column, y=y_column, title=f"{plot_type} of {y_column} vs {x_column}")
    elif plot_type == "Scatter Plot":
        fig = px.scatter(df, x=x_column, y=y_column, title=f"{plot_type} of {y_column} vs {x_column}")

    st.plotly_chart(fig, use_container_width=True)

    st.write("## Data Insights")
    st.write("Mean of selected Y-axis column:", df[y_column].mean())
    st.write("Median of selected Y-axis column:", df[y_column].median())
    st.write("Standard deviation:", df[y_column].std())
else:
    st.info("Please upload a CSV file to visualize and analyze data.")



