from finance_calculator import *

def main():
    incomes = []
    expenses = []
    
    print("ВЕРСИЯ 2.0")

    print("=== Калькулятор личных средств ===")

    # Ввод доходов
    while True:
        label = input("Источник дохода (или Enter для завершения): ").strip()
        if not label:
            break
        amount = float(input(f"Сумма для '{label}': "))
        incomes = add_income(incomes, label, amount)

    # Ввод расходов
    while True:
        label = input("Статья расходов (или Enter для завершения): ").strip()
        if not label:
            break
        amount = float(input(f"Сумма для '{label}': "))
        expenses = add_expense(expenses, label, amount)

    print("\n--- Результаты ---")
    print(f"Доходы: {total_income(incomes):.2f}")
    print(f"Расходы: {total_expenses(expenses):.2f}")
    print(f"Остаток: {balance(incomes, expenses):.2f}")
    print(f"Норма сбережений: {savings_rate(incomes, expenses):.2f}%")

if __name__ == "__main__":
    main()