import streamlit as st
import pandas as pd


df = pd.read_csv('data.csv')

st.dataframe(df)

st.session_state['df'] = df