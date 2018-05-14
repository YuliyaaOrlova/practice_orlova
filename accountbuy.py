def calculate_income(rate,period,money):
    if money<=0:
        return 0
    for i in range(1,period+1):
        money = round(money+money*rate/100/12,2)
        return money
