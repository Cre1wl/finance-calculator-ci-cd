import pytest
from finance_calculator import *

def test_add_income():
    incomes = add_income([], "Зарплата", 50000)
    assert len(incomes) == 1
    assert incomes[0]["amount"] == 50000.0

def test_total_income_empty():
    assert total_income([]) == 0

def test_balance():
    incomes = [{"label": "Зарплата", "amount": 50000}]
    expenses = [{"label": "Аренда", "amount": 20000}]
    assert balance(incomes, expenses) == 30000.0

def test_savings_rate():
    incomes = [{"label": "Зарплата", "amount": 100000}]
    expenses = [{"label": "Траты", "amount": 40000}]
    # Ожидаем 60%
    assert savings_rate(incomes, expenses) == 60.0

def test_savings_rate_zero_income():
    # Если доходов нет, норма сбережений должна быть 0, а не деление на ноль
    assert savings_rate([], [{"label": "Долг", "amount": 5000}]) == 0.0