import streamlit as st
import matplotlib.pyplot as plt
from app import category

if 'df' in st.session_state:
    df = st.session_state['df']

    if 'category' not in st.session_state:
        category = 'Electronics'
    st.session_state['category'] = category

    category = st.selectbox('Категории', df.category.unique())

    st.session_state['category'] = category


    filtered_df = df[df['category'] == category]

    fig, ax = plt.subplots()
    ax.hist(filtered_df.price)
    st.pyplot(fig)
else:
    st.write('Загрузите данные')