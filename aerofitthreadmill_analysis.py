#import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

#setting the page configuration of streamlit dashboard
st.set_page_config(page_title = "Aerofit Treadmill Analysis",layout = "wide")
st.title("Aerofit Treadmill data Analysis Dashhboard")

#upload the Dataset
uploaded_file = st.file_uploader("phase upload your dataset",type = ["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    #basic data dataset
    st.subheader("Dataset preview")
    st.dataframe(df.head())

    #shape of the dataset 
    st.subheader("Shape of the dataset")
    st.write("Number of rows and columns in the dataset are :",df.shape)
    st.write("column nmaes of my dataset are:",df.columns.tolist())

    #create few checkboxes
    st.subheader("Statistics of the Dataset")
    data_info = st.checkbox("Show Data Type")
    missing_value = st.checkbox("Show the Statistical of the dataset")
    statistics = st.checkbox("show the statistical summary of the dataset")
    
    if data_info:
        st.write("The data types in this dataset are:",df.info())
    if missing_value:
        st.write("Please upload the Dataset first for the exploratory data analysis",df.isna().sum(axis = 0))
    if statistics:
        st.write("Dataset statisstics are:",df.describe()) 

    # Radio Button for Statistics
    stats_option = st.radio(
        "Choose statistical information:",
        ["Data Types", "Missing Values", "Summary"]
    )

    if stats_option == "Data Types":
        st.write(df.dtypes)
    elif stats_option == "Missing Values":
        st.write(df.isna().sum())
    elif stats_option == "Summary":
        st.write(df.describe())     
          
    #visual analysis of our dataset
    # column selector
    numeric_cols = df.select_dtypes(include =["int64","float64"]).columns.tolist()
    categorical_cols = df.select_dtypes(include = ["object"]).columns.tolist()
    st.write(numeric_cols)
    st.write(categorical_cols)

    #uni-variate  analysis
    #count plot
    st.subheader("count plot")
    selected_cols = st.selectbox("select a numeric column:",numeric_cols)
    fig,ax = plt.subplots()
    sns.countplot(x = df[selected_cols],ax = ax)
    st.pyplot(fig)

    #count plot for catagoricalcolumns
    st.subheader("count plot")
    cat_cols = st.selectbox("select a numeric column: ",categorical_cols)
    fig,ax = plt.subplots()
    sns.countplot(x = df[cat_cols],ax = ax) 
    st.pyplot(fig)



    #box plot
    st.subheader("Box plots for checking the outliers")
    box_cols = st.selectbox("select a numericcolumn:",numeric_cols)
    fig,ax = plt.subplots()
    sns.boxplot(x = df[box_cols],ax = ax)
    st.pyplot(fig)

    #hist plot

    #bi-viraiate
    st.subheader("Bi-variate of our dataset: categorical vs numerical")
    num_cols = st.selectbox("select a numeric column:",numeric_cols,key = 'num1')
    category_cols = st.selectbox("select a categorical column:",categorical_cols,key ="")
    fig,ax = plt.subplots()
    sns.boxplot(x = df[num_cols],y = df[category_cols],ax = ax)
    st.pyplot(fig)

    #multi-variate analysis
    #heatmap of our dataset to check the co-relation
    st.subheader("co-relation heatmap")
    fig,ax = plt.subplots(figsize =(10,6))
    sns.heatmap(df[numeric_cols].corr(),annot = True,cmap = "magma",ax = ax)
    st.pyplot(fig)

    #pairplot
    st.subheader("pairplot of our dataset")
    fig = sns.pairplot(df[numeric_cols])
    st.pyplot(fig)


else:
    st.write("please upload the dataset first for the exploratort data analysis")