# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

import decimal

CMD_DEPOSIT = 'п' # пополнить
CMD_WITHDRAW = 'с' # снять
CMD_EXIT = 'в' # внести
RICHNESS_SUM = decimal.Decimal(5_000_000) # богатство
RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100) # налог
WITHDRAW_PERCENT = decimal.Decimal(15) / decimal.Decimal(1000) # 1,5 % от суммы снятия
ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(100) # бонус на каждую 3 операцию
MUTIPLICIRY = 50 # кратность пополнения и снятия
MIN_REMOVAL = 30 # min сумма снятия
MAX_REMOVAL = 600 # max сумма снятия
COUNT_OPER = 3 # 3 операции
account = decimal.Decimal(0)
count = 0


def exit_():
    print(f'Возмите карту, на которой {account} у.е.')
    exit()


def richnes():
    global account
    percent = account * RICHNESS_TAX
    account -= percent
    print(f'Удержан налог на богатство 10% в размере {percent} у.е.\n'
          f'Итого на карте осталось {account} у.е.')

def deposit_withdraw():
    global account
    global count
    ammount = 1
    while ammount % 50 != 0:
        ammount = decimal.Decimal(input(f'Введите сумму кратную {MUTIPLICIRY}: '))
    if command == CMD_DEPOSIT:
        account += ammount
        count += 1
        print(f'Пополнение карты на {ammount} у.е.\nИтого на какрте {account} у.е.')
    elif command == CMD_WITHDRAW:
        withdraw_tax = ammount * WITHDRAW_PERCENT
        withdraw_tax = (MIN_REMOVAL if withdraw_tax < MIN_REMOVAL else
                        MAX_REMOVAL if withdraw_tax > MAX_REMOVAL else withdraw_tax)
        if account >= ammount + withdraw_tax:
            count += 1
            account -= (ammount + withdraw_tax)
            print(f'Снятие с карты {ammount} у.е.\nКомиссия за снятие {withdraw_tax}\n'
                  f'На карте осталось {account} у.е.')
        else:
            print(f'Недостаточно средств на карте\n'
                  f'Затребованная сумма {ammount} у.е., Комиссия {withdraw_tax} у.е.'
                  f'На карте {account} у.е.')


def count_oper():
    global account
    bonus_percent = account * ADD_PERCENT
    account += bonus_percent
    print(f'На счёт начислено 3%, составляющие {bonus_percent} у.е.\n'
          f'Итого на карте {account} у.е.')


while True:
    command = input(f'Пополнить - "{CMD_DEPOSIT}", Снять - "{CMD_WITHDRAW}", Выйти - "{CMD_EXIT}": ')
    if command == CMD_EXIT:
        exit_()
    if account > RICHNESS_SUM:
        richnes()

    if command in (CMD_DEPOSIT, CMD_WITHDRAW):
        deposit_withdraw()

    if count and count % COUNT_OPER == 0:
        count_oper()