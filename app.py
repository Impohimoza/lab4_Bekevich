import pandas as pd
import streamlit as st
from titanic_analysis import analyze_titanic_data


df = pd.read_csv('titanic.csv', delimiter=',')

st.set_page_config(
    page_title="Анализ пассажиров Титаника",
)

st.image("titanic_image.jpg",)
st.title("Анализ пассажиров Титаника")
st.markdown("---")

surv = st.selectbox(
    "Спасен?:",
    ('Да', 'Нет')
)

number_or_percent = st.selectbox(
    "В чем выдавать результат?:",
    ('Число', '%')
)

number_dict = {'Число': True, '%': False}
number = number_dict[number_or_percent]

surv_dict = {'Нет': 0, 'Да': 1}
survived = surv_dict[surv]


if st.button('Запустить анализ'):
    result_df = analyze_titanic_data(df, survived, number)
    st.dataframe(result_df)
