import streamlit as st


if 'df' in st.session_state:
    df = st.session_state['df']

    category = st.selectbox('Категории', df.category.unique())

    st.session_state['category'] = category
else:
    st.write('Загрузите данные')
