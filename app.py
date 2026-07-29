import streamlit as st
import pandas as pd


st.title('Dahboard продаж')
st.write('Приложение обновилось')

df = pd.read_csv('data.csv')
st.dataframe(df)
st.write('Количество строк', len(df))
st.write('Количество столбцов', len(df.columns))