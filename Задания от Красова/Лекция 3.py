#Функция расчета вхождения символа в строку
def statictic(string):
    dictionary = {}
    for letter in string:
        if letter not in dictionary:
            dictionary[letter] = 1
        elif letter in dictionary:
            dictionary[letter] += 1
        else:
            print('Something wrong!\n')
    k = 0
    s = ''
    for key in dictionary.keys():
        s += str(key) + ' : ' + str(dictionary[key]) + ',  '
        if k == 5:
            k = 0
            print(s, '\n')
            s = ''
        else:
            k += 1
    print('Общее число различных символов в строке: ', len(dictionary))

#Функция поиска подстроки в строке
def substring(string):
    sub = input('Введите регистрозависимую подстроку для поиска: ')
    position = string.find(sub)
    if position == -1:
        print('Данной подстроки в строке нет!')
    else:
        print('Данная подстрока встречается в строке с позиции ',position)

#Функция посимвольного разделения строки и сортировка по алфавиту
def fun(string):
    words = string.split(' ')
    for i in range(len(words) - 1):
        flag = True
        for j in range(len(words) - i - 1):
            if words[j] > words[j + 1]:
                buff = words[j]
                words[j] = words[j + 1]
                words[j + 1] = buff
                flag = False
        if flag:
            break
    print('Слова в алфавитном порядке:\n')
    for word in words:
        print(word, '\n')


def main():
    line = input('Введите строку: ')
    print(line)
    print('\n')
    statictic(line)
    line = line.strip()
    substring(line)
    fun(line)


if __name__ == '__main__':
    main()