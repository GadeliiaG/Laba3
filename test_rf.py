# -*- coding: utf-8 -*-
"""Test_RF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QbSifojrVd83yYN3PQMUK_pjIUNAlVmr
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from random_forest_model import predict_subscription_status

def test_predict_subscription_status():
    # Загрузите данные
    data = pd.read_csv('bank.csv', sep=';')
    X = data.drop('y', axis=1)
    y = data['y']
    X = pd.get_dummies(X, drop_first=True)

    # Разделите данные на тренировочную и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Обучите модель
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Предскажите результаты
    y_pred = model.predict(X_test)

    # Посчитайте точность модели
    accuracy = accuracy_score(y_test, y_pred)

    # Выведите точность
    print(f"Точность модели: {accuracy}")

    # Теперь проверим функцию predict_subscription_status
    result = predict_subscription_status(X_test)

    # Ожидаемый результат - это предсказанные значения модели
    expected_result = y_pred.tolist()

    # Проверьте результаты
    assert result == expected_result

# Запустите тест
test_predict_subscription_status()
