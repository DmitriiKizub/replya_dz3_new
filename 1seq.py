spisok = int(input('Введите кол-во эл-ов списка: '))
i = 0
spisok_all = []
while i<spisok:
    vvod = input('Введите цифру')
    spisok_all.append(vvod)
    i=i+1

print(sorted(spisok_all))