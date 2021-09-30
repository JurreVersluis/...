lijst = {}
d = True
f = True
watwilje = ''
hoeveelwilje = ''


def vragen():
    global b
    b = True
    global d
    while d:
        global watwilje
        watwilje = input('welk product zou je aan je boodschappenlijst toe willen voegen?\n')
        print(f'{watwilje} is toegevoegd aan je boodschappenlijst!')
        d = False


def vraag2():
    c = True
    global hoeveelwilje
    while c:
        try:
            hoeveelwilje = int(input(f'Hoeveel wil je van dit product?\n'))
            if hoeveelwilje > 0:
                c = False
        except ValueError:
            print('U kunt geen getal met een punt of komma invoeren. Ook zijn letters niet mogelijk!')


while f:
    vragen()
    vraag2()
    if watwilje in lijst:
        lijst[watwilje] += hoeveelwilje
    else:
        lijst[watwilje] = hoeveelwilje
    while b:
        nogmeer = input('Wil je nogmeer toevoegen?\n'.lower())
        if nogmeer == 'nee':
            print('---!Boodschappenlijstje!---')
            for x in lijst:
                print(repr(x), ":", lijst[x])
            d = False
            f = False
            b = False

        elif nogmeer == 'ja':
            d = True
            b = False
    b = False