import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Analyze Your Data", layout="wide", page_icon="🚀")
st.title("📊 Analyze Your Data")
st.write("Upload a CSV file and explore your data interactively!")

# Upload CSV
uploaded_file = st.file_uploader("📂 Upload Your CSV File", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        # Convert bool columns to string
        bool_cols = df.select_dtypes(include=['bool']).columns
        df[bool_cols] = df[bool_cols].astype(str)
        
    except Exception as e:
        st.error("❌ Could not read the CSV. Please check the file format.")
        st.exception(e)
    else:
        st.success("✅ File Uploaded Successfully!")

        # Dataset Overview
        st.subheader("### Preview of Data")
        st.dataframe(df.head())

        st.write("## Data Overview")
        st.write("Number Of Rows:", df.shape[0])
        st.write("Number Of Columns:", df.shape[1])
        st.write("Number Of Missing Values:", int(df.isnull().sum().sum()))
        st.write("Number Of Duplicate Records:", df.duplicated().sum())

        st.subheader("Complete Summary Of Dataset")
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

        st.write("### Statistical Summary")
        st.dataframe(df.describe())

        st.write("### Statistical Summary For Non-Numerical Features")
        st.dataframe(df.describe(include='object'))

        # Column selector for analysis
        st.subheader("Select Columns For Analysis")
        selected_columns = st.multiselect("Choose Columns", df.columns.tolist())

        st.subheader("Preview")
        if selected_columns:
            st.dataframe(df[selected_columns].head())
        else:
            st.info("No Columns Selected. Showing Full Dataset.")
            st.dataframe(df.head())


        st.subheader("Showing 10 Records Where Customer Service Calls > 4")
        filtered_df = df[df["customer service calls"] > 4]
        result = filtered_df[["phone number","customer service calls","churn"]]
        st.dataframe(result.head(10))

        st.subheader("International Plan Usage")
        count = df["international plan"].value_counts()
        st.bar_chart(count)
        
else:
    st.info("ℹ️ Please upload a CSV file to get started.")


