import streamlit as st
import matplotlib.pyplot as plt


if 'df' in st.session_state:
    df = st.session_state['df']

    if 'category' not in st.session_state:
        category = 'Electronics'

    category = st.selectbox('Категории', df.category.unique())
    st.session_state['category'] = category

    filtered_df = df[df['category'] == category]

    tab_1, tab_2 = st.tabs(['Гистограмма', 'Линейный график'])
    with tab_1:
        fig, ax = plt.subplots()
        ax.hist(filtered_df.price)
        st.pyplot(fig)
    with tab_2:
        st.line_chart(filtered_df.price)
else:
    st.write('Загрузите данные')