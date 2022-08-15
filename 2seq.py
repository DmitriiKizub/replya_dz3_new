vvod = input('Введите любые цифры через запятую(точку с запятой, /: ')
if ',' in vvod:
    print(set(vvod.split(',')))
elif '/' in vvod:
    print(set(vvod.split('/')))
elif ';' in vvod:
    print(set(vvod.split(';')))

