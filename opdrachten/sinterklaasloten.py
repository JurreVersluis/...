import builtins
import random


def input(input_string, allowed: list = None, incorrect_message: str = 'Sorry, dat snap ik niet...'):
    while (antwoord := builtins.input(input_string).lower()) is not None and not (
            allowed is None or antwoord in allowed):
        print(incorrect_message)
    return antwoord

meer = True
deelNemers = []
deelNemersToevoegen = list()
gekoppeld = {

}
while meer:
    naam = input('Wie wil je toevoegen?')
    if deelNemers.__contains__(naam):
        print('Dat is geen unieke naam.')
    else:
        if len(naam) > 20:
            print('die naam is iets telang!')
        else:
            deelNemers.append(naam)
            if len(deelNemers) > 1:
                iedereenGehad = input('Heb je alle spelers al toegevoegd? 1, Ja. 2, Nee.\n', [str(i) for i in range(1, 3)])
                if iedereenGehad == '1':
                    meer = False

deelNemersToevoegen = deelNemers.copy()
hetzelfde = 1
while hetzelfde > 0:
    hetzelfde = 0
    random.shuffle(deelNemersToevoegen)
    for i in range(len(deelNemers)):
        if deelNemers[i] == deelNemersToevoegen[i]:
            hetzelfde += 1


for i in range(len(deelNemers)):
    print(deelNemers[i] + ' heeft: '+ deelNemersToevoegen[i])





