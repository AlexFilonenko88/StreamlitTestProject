import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')

st.dataframe(df)

category = st.selectbox('Категории', df.category.unique())

filtered_df = df[df['category'] == category]

fig, ax = plt.subplots()
ax.hist(filtered_df.price)
st.pyplot(fig)

#st.line_chart(df.price)
#st.bar_chart(category_sales)