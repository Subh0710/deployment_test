import streamlit as st
import pandas as pd

st.header("UK Bank Dataset")
df=pd.read_csv("P1-UK-Bank-Customers.csv")
st.table(data=df)
