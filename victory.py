import random
gibson = '03.07.1956'
ordmond = '04.03.1965'
chelentano = '06.02.1938'
keidj = '07.12.1964'
boui = '08.08.1947'
pressli = '08.12.1935'

spisok_date = (gibson,ordmond,chelentano,keidj,boui,pressli)
spisok_name = ('gibson','ordmond','chelentano','keidj','boui','pressli')
result = random.sample(spisok_name,3)
day_list = ['','первое', 'второе', 'третье', 'четвёртое',
        'пятое', 'шестое', 'седьмое', 'восьмое',
        'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
        'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
        'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
        'двадцать первое', 'двадцать второе', 'двадцать третье',
        'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
        'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
        'тридцатое', 'тридцать первое']
month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
           'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
otvet = 0
game=None
while game != 'Нет':

    for i in range(3):
        vvod = input(f'Введите дату рождения {result[i]}: ')

        if vvod in list(spisok_date):
            index = spisok_date.index(vvod)
            if spisok_name[index] == result[i]:
                print('Верно')
                otvet = otvet+1
            else:
                print('Не верно')
        else:
            index_good= spisok_name.index(result[i])
            a= spisok_date[index_good]
            nomber_month = int(a[4:5])
            print(f'Верный ответ: {day_list[int(a[1])]} {month_list[nomber_month]} {a[6:]} ')

    print(f'Кол-во верных ответов: {otvet}')
    print(f'Кол-во не правильных ответо: {3-otvet}')
    game = input('Хотите начать играть заново? ')

