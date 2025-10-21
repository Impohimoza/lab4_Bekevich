# titanic_analysis.py
import pandas as pd
import numpy as np

def analyze_titanic_data(df, survived, number):
    """
    Анализирует данные пассажиров Титаника
    Args:
        df: DataFrame с данными
        survived: 'True' или 'False'
        number: 'True' или 'False'
    Returns:
        DataFrame с результатами
    """
    if number:
        res_male = df[(df['Sex'] == 'male') & (df['Survived'] == survived)].shape[0]
        res_female = df[(df['Sex'] == 'female') & (df['Survived'] == survived)].shape[0]

        result_df = pd.DataFrame({
            'Пол': ['male', 'female'],
            'Число': [res_male, res_female]
        })
    else:
        res_male = df[(df['Sex'] == 'male') & (df['Survived'] == survived)].shape[0]
        male_count = df[df['Sex'] == 'male'].shape[0]
        res_female = df[(df['Sex'] == 'female') & (df['Survived'] == survived)].shape[0]
        female_count = df[df['Sex'] == 'female'].shape[0]

        male_percent = round(res_male / male_count * 100, 2) if male_count > 0 else 0
        female_percent = round(res_female / female_count * 100, 2) if female_count > 0 else 0

        result_df = pd.DataFrame({
            'Пол': ['male', 'female'],
            'Процент': [male_percent, female_percent]
        })

    return result_df
