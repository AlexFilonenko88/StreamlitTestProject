import streamlit as st
import pandas as pd


#df = pd.read_csv('data.csv')
file = st.file_uploader(
    'Выбирите CSV файл',
    type=['xlsx', 'csv']
)

required_columns = [
    'product',
    'price',
    'category'
]

if file is not None:
    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
    except (pd.errors.ParserError, pd.errors.EmptyDataError, UnicodeDecodeError, ValueError) as e:
        st.error(f'Не удалось прочитать файл: {e}')
        st.stop()

    if not all(column in df.columns for column in required_columns):
        st.error('Некорректная структура файла')
    else:
        st.session_state['df'] = df

        price_by_categories = df.groupby('category').price.sum().reset_index()

        col_1, col_2 = st.columns(2)

        with col_1:
            st.dataframe(df)

        with col_2:
            st.dataframe(price_by_categories)

        with st.expander('Подробная информация'):
            st.write(df.describe())
else:
    st.write('Данные еще не загружены')