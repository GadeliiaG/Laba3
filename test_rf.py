# -*- coding: utf-8 -*-
"""Test_RF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QbSifojrVd83yYN3PQMUK_pjIUNAlVmr
"""

from random_forest_model import predict_subscription_status

def test_predict_subscription_status():
    data = pd.read_csv('bank.csv', sep = ';')
    X = data.drop('y', axis=1)
    y = data['y']
    X = pd.get_dummies(X, drop_first=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    # Вызовите функцию для предсказания
    result = predict_subscription_status(X_test)

    # Посчет точности модели
    expected_result = accuracy_score(y_test, result)

    # Проверьте результаты
    assert result == expected_result