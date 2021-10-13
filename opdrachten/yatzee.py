import random
import time
import builtins

witLijst = [1, 1, 1, 2, 2, 3]
keuze3 = 0
blauw = 0
rood = 0
wit = 0
roodCheck = True
loop = True
blauwCheck = True
rodeLijst = [-2, '_', '_', '_', '_', '_', '_', '_', '_', '_']
blauweLijst = ['_', '_', '_', '_', '_', '_', '_', '_', '_', -2]
witteLijst = ['_', '_', '_', '_', '_']
alleWaardes = []
honderd = ['100']
print('Welkom bij Yatzeeee!\n')


def input(input_string, allowed: list = None, incorrect_message: str = 'Sorry, dat snap ik niet...'):
    while (antwoord := builtins.input(input_string).lower()) is not None and not (
            allowed is None or antwoord in allowed):
        print(incorrect_message)
    return antwoord


def dobbelen():
    global blauw
    global rood
    global wit
    print('er wordt weer gedobbelt...\n')
    blauw = random.randrange(1, 7)
    rood = random.randrange(1, 7)
    wit = random.choice(witLijst)
    time.sleep(0.4)
    print(f'De blauwe dobbelsteen valt op : {blauw}!')
    time.sleep(0.4)
    print(f'De rode dobbelsteen valt op   : {rood}!')
    time.sleep(0.4)
    print(f'De witte dobbelsteen valt op  : {wit}!')
    time.sleep(0.4)


def score():
    print('')
    print('Rode lijst  : ', *rodeLijst)
    print('Blauwe lijst: ', *blauweLijst)
    print('Witte lijst :     ', *witteLijst)
    return


def vraagRood():
    global cofd
    global loop
    roodCheck = True
    while roodCheck:
        hoger = False
        lager = False
        score()
        getal = int(input(f'Je mag het getal {keuze3} toevoegen op de rode lijn. Welke plek? 1/10?\n(Als je geen zetten meer kan doen, typ 100!)\n', [str(i) for i in range(1, 11)] + honderd)) - 1
        if not getal == 99:
            if rodeLijst[getal] == '_':
                for i in range(getal):
                    if not rodeLijst[i] == '_':
                        if rodeLijst[i] > keuze3:
                            if not rodeLijst[i] == 0:
                                hoger = True
                for i in range(9 - getal):
                    if not rodeLijst[getal + i] == '_':
                        if rodeLijst[getal + i] < keuze3:
                            if not rodeLijst[getal + i] == 0:
                                lager = True

                if hoger == False and lager == False:
                    rodeLijst[getal] = keuze3
                    print('Goed gedaan.')
                    score()
                    roodCheck = False

            if roodCheck == True:
                print('Je moet weer even overnieuw beginnen.')
        else:
            roodCheck = False
            loop = False
            cofd = False

    while cofd:
        getal = int(input(f'Je mag het getal {wit} toevoegen op de witte lijn. Welke plek? 1/5?\n (Als je geen zet meer kan zetten typ 100!)\n', [str(i) for i in range(1, 6)] + honderd)) - 1
        if not getal == 99:
            if witteLijst[getal] == '_':
                witteLijst[getal] = wit
                score()
                cofd = False
        else:
            cofd = False
            loop = False


def vraagBlauw():
    global cofd
    global loop
    blauwCheck = True
    while blauwCheck:
        hoger = False
        lager = False
        score()
        getal = int(input(f'Je mag het getal {keuze3} toevoegen op de blauwe lijn. Welke plek? 1/10?\n(Als je geen zetten meer kan doen, typ 100!)\n', [str(i) for i in range(1, 11)] + honderd)) - 1
        if not getal == 99:
            if blauweLijst[getal] == '_':
                for i in range(getal):
                    if not blauweLijst[i] == '_':
                        if blauweLijst[i] < keuze3:
                            if not blauweLijst[i] == 0:
                                hoger = True
                for i in range(9 - getal):
                    if not blauweLijst[getal + i] == '_':
                        if blauweLijst[getal + i] > keuze3:
                            if not blauweLijst[getal + i] == 0:
                                lager = True

                if hoger == False and lager == False:
                    blauweLijst[getal] = keuze3
                    print('Goed gedaan.')
                    score()
                    blauwCheck = False

            if blauwCheck == True:
                print('Je moet weer even overnieuw beginnen.')
        else:
            blauwCheck = False
            loop = False
            cofd = False

    while cofd:
        getal = int(input(f'Je mag het getal {wit} toevoegen op de witte lijn. Welke plek? 1/5?\n (Als je geen zet meer kan zetten typ 100!)\n', [str(i) for i in range(1, 6)] + honderd)) - 1
        if not getal == 99:
            if witteLijst[getal] == '_':
                witteLijst[getal] = wit
                score()
                cofd = False
        else:
            cofd = False
            loop = False






def welkeKeuzen():
        global laagste
        global keuze3
        global cofd
        alleWaardes.extend((rood, blauw))
        alleWaardes.sort()
        hoogste = alleWaardes[1]
        laagste = alleWaardes[0]
        alleWaardes.clear()
        print('')
        a = blauw + rood + wit
        b = blauw + rood - wit
        c = blauw + rood
        d = hoogste - laagste
        print('a)', a)
        print('b)', b)
        print('c)', c)
        print('d)', d)

        keuze = input('Welke optie kies je?\n', ['a', 'b', 'c', 'd'])
        if keuze == 'a':
            keuze3 = a
            cofd = False
        elif keuze == 'b':
            keuze3 = b
            cofd = False
        elif keuze == 'c':
            keuze3 = c
            cofd = True
        elif keuze == 'd':
            keuze3 = d
            cofd = True

        if rood == blauw:
            keuze2 = input(f'Je mag kiezen op welke lijn het getal {keuze3} komt te staan. a) Rood. b) Blauw.\n', ['a', 'b'])
            if keuze2 == 'a':
                vraagRood()
            elif keuze2 == 'b':
                vraagBlauw()
        else:
            if laagste == rood:
                vraagRood()
            elif laagste == blauw:
                vraagBlauw()





while loop:
    dobbelen()
    welkeKeuzen()
legeVakjes = 0
witTotaal = 0
for i in range(10):
    if rodeLijst[i] == '_':
        rodeLijst[i] = 0
        legeVakjes += 1
for i in range(10):
    if blauweLijst[i] == '_':
        blauweLijst[i] = 0
        legeVakjes += 1
for i in range(5):
    if witteLijst[i] == '_':
        legeVakjes += 1
        witteLijst[i] = 0
    witTotaal += witteLijst[i]


subtotaal1 = 0
for i in range(10):
    subtotaal1 += (rodeLijst[i] * blauweLijst[i])


subTotaal2 = legeVakjes * witTotaal
eindscore = subTotaal1 = subTotaal2
print(f'Uw eindscore is {eindscore}.')



