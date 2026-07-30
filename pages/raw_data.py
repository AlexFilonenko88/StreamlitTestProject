import streamlit as st
import pandas as pd


df = pd.read_csv('data.csv')
st.session_state['df'] = df

price_by_categories = df.groupby('category').price.sum().reset_index()

col_1, col_2 = st.columns(2)

with col_1:
    st.dataframe(df)

with col_2:
    st.dataframe(price_by_categories)

with st.expander('Подробная информация'):
    st.write(df.describe())