import pandas as pd
import pytest
from titanic_analysis import analyze_titanic_data


class TestTitanicAnalysis:
    def setup_method(self):
        """Создаем тестовые данные"""
        self.test_data = pd.DataFrame({
            'Sex': ['male', 'male', 'female', 'female', 'male', 'female'],
            'Survived': [1, 0, 1, 1, 0, 0]
        })

    def test_survived_count(self):
        """Тест подсчета выживших в числах"""

        # arrange
        survived = True
        number = True
        expected_male = 1
        expected_female = 2

        # act
        result = analyze_titanic_data(self.test_data, survived, number)

        # assert
        # Проверяем структуру DataFrame
        assert 'Пол' in result.columns
        assert 'Число' in result.columns

        # Проверяем результаты
        male_row = result[result['Пол'] == 'male']
        female_row = result[result['Пол'] == 'female']
        assert male_row['Число'].iloc[0] == expected_male
        assert female_row['Число'].iloc[0] == expected_female

    def test_survived_percentage(self):
        """Тест подсчета выживших в процентах"""

        # arrange
        survived = True
        number = False
        expected_male = pytest.approx(33.33, 0.01)
        expected_female = pytest.approx(66.67, 0.01)

        # act
        result = analyze_titanic_data(self.test_data, survived, number)

        # assert
        # Проверяем структуру DataFrame
        assert 'Пол' in result.columns
        assert 'Процент' in result.columns

        # Проверяем результаты
        male_row = result[result['Пол'] == 'male']
        female_row = result[result['Пол'] == 'female']
        assert male_row['Процент'].iloc[0] == expected_male
        assert female_row['Процент'].iloc[0] == expected_female

    def test_died_female_percentage(self):
        """Тест подсчета погибших в процентах"""

        # arrange
        survived = False
        number = False
        expected_male = pytest.approx(66.67, 0.01)
        expected_female = pytest.approx(33.33, 0.01)

        # act
        result = analyze_titanic_data(self.test_data, survived, number)

        # assert
        # Проверяем структуру DataFrame
        assert 'Пол' in result.columns
        assert 'Процент' in result.columns

        # Проверяем результаты
        male_row = result[result['Пол'] == 'male']
        female_row = result[result['Пол'] == 'female']
        assert male_row['Процент'].iloc[0] == expected_male
        assert female_row['Процент'].iloc[0] == expected_female

    def test_died_female_count(self):
        """Тест подсчета погибших в числах"""

        # arrange
        survived = False
        number = True
        expected_male = 2
        expected_female = 1

        # act
        result = analyze_titanic_data(self.test_data, survived, number)

        # assert
        # Проверяем структуру DataFrame
        assert 'Пол' in result.columns
        assert 'Число' in result.columns

        # Проверяем результаты
        male_row = result[result['Пол'] == 'male']
        female_row = result[result['Пол'] == 'female']
        assert male_row['Число'].iloc[0] == expected_male
        assert female_row['Число'].iloc[0] == expected_female

    def test_empty_dataframe(self):
        """Тест обработки пустого DataFrame"""
        empty_data = pd.DataFrame(columns=['Sex', 'Survived'])
        expected_male = 0
        expected_female = 0

        # act
        result = analyze_titanic_data(empty_data, True, True)

        # assert
        # Проверяем структуру DataFrame
        assert 'Пол' in result.columns
        assert 'Число' in result.columns

        # Проверяем результаты
        male_row = result[result['Пол'] == 'male']
        female_row = result[result['Пол'] == 'female']
        assert male_row['Число'].iloc[0] == expected_male
        assert female_row['Число'].iloc[0] == expected_female
