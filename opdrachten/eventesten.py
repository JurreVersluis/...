def printer(hoeveelkeer, wattypen):
    print('------------')
    for i in range(hoeveelkeer):
        print(wattypen)
    print('------------')


while True:
    wat = input('Wat wil je printen?\n')
    try:
        hvl = int(input('Hoeveelkeer wil je dit printen?\n'))
    except ValueError:
        hvl = 0
        print('Je kan daar niks anders dan een getal invoeren.')
    printer(hvl, wat)
