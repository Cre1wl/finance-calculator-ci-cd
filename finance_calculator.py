def add_income(incomes, label, amount):
    """Добавляет источник дохода. Возвращает новый список."""
    return [*incomes, {"label": label, "amount": float(amount)}]

def add_expense(expenses, label, amount):
    """Добавляет статью расходов. Возвращает новый список."""
    return [*expenses, {"label": label, "amount": float(amount)}]

def total_income(incomes):
    """Сумма всех доходов."""
    return sum(item["amount"] for item in incomes)

def total_expenses(expenses):
    """Сумма всех расходов."""
    return sum(item["amount"] for item in expenses)

def balance(incomes, expenses):
    """Остаток средств (доходы минус расходы)."""
    return total_income(incomes) - total_expenses(expenses)

def savings_rate(incomes, expenses):
    """Норма сбережений в процентах. Если доходов нет — возвращает 0.0."""
    income = total_income(incomes)
    if income == 0:
        return 0.0
    return (income - total_expenses(expenses)) / income * 100