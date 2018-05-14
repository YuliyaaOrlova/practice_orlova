import sys
def conv(money):
    money1 = input('Какую валюту вы хотите посчитать?\nДля помощи введите -help\n')
    if money1.lower() == 'доллар':
        course_dollar = int(input('Введите текущий курс доллара к рублю\n'))
        val_vib = input('Если вы хотетие посчитать из рублей в доллар,\n введите 1 если нет, введите 2\n')
        #money = int(input('Введите нужную сумму\n'))
        if val_vib == '2':
            cash = money*course_dollar
            print('Вы получите '+str(cash)+' рублей')
        elif val_vib =='1':
            cash = money/course_dollar
            print('Вы получите '+str(cash)+' долларов')
    elif money1.lower()== 'евро':
        course_euro  = int(input('Введите текущий курч евро к рублю'))
        val_vib = input('Если вы хотетие посчитать из рублей в евро, введите 1 \n если нет, введите 2\n')
        money = int(input('Введите нужную сумму\n'))
        if val_vib == '2':
            cash = money*course_euro
            print('Вы получите '+str(cash)+' рублей')
        else:
            cash = money/course_euro
            print('Вы получите '+str(cash)+' евро') 
    elif money1 == '-help':
        print('Валюта, которая есть в нашем калькуляторе:\nДоллар\nЕвро')
        sys.exit()