import streamlit as st
import pandas as pd

st.header("UK Bank Dataset")
df=pd.read_csv("C:\\Users\\Subham\\Desktop\\Datasets\\P1-UK-Bank-Customers.csv")
st.table(data=df)