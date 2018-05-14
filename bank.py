import account_buy
import rub_doll
def main():
    money = int(input('Введите сумму\n'))
    d = rub_doll.conv(money)
    vop = input("Хотите ли вы посчитать процентную ставку для введенной суммы?\nЕсли да,"
                "то введите 1, если нет, то 2\n")
    if vop =="1":
        rate = int(input('Введите ставку\n'))
        period = int(input('Введите период\n'))
        result = account_buy.calculate_income(rate,period,money)
        print('Ваша ставка: ',rate,'\n'+'Период: ',period,'\n''Ваша сумма: ',money,'\n''Результат:',result)
    else:
        print("="*30)
        print("Спасибо за использование")
if __name__ == '__main__':
    main()

