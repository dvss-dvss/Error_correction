"""
Помилки (номери рядків через пробіл): !!!
"""


class NoMoneyToWithdrawError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PaymentError(Exception):
    def __init__(self, message):
        super().__init__(message)


def print_accounts(accounts):
    """Друк акаунтів."""
    print(f"Список клієнтів ({len(accounts)}): ")
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print(f"{i}. {name} {value}")


def transfer_money(accounts, account_from, account_to, value):
    if account_from not in accounts or account_to not in accounts:
        raise PaymentError("Один з акаунтів не знайдено")
    
    if accounts[account_from] < value:
        raise NoMoneyToWithdrawError("Недостатньо коштів на рахунку")
    
    initial_from = accounts[account_from]
    initial_to = accounts[account_to]
    
    try:
        accounts[account_from] -= value
        accounts[account_to] += value
    except Exception as e:
        accounts[account_from] = initial_from
        accounts[account_to] = initial_to
        raise PaymentError(f"Помилка при переказі: {str(e)}")


if __name__ == "__main__":
    accounts = {
        "Василь Іванов": 100,
        "Іван Васильєв": 1500,
        "Петро Бондаренко": 400
    }
    print_accounts(accounts)

    payment_info = {
        "account_from": "Василь Іванов",
        "account_to": "Іван Васильєв"
    }

    print("Переказ від {account_from} для {account_to}...".
          format(**payment_info))

    payment_info["value"] = int(input("Сума = "))

    transfer_money(accounts, **payment_info)

    print("OK!")

    print_accounts(accounts)
