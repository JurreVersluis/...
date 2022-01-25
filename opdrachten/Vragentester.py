def ietsvragen(devraag, antwoorden):
    vraag = True
    while vraag:
        antwoord = input(devraag + '\n')
        if antwoord in str(antwoorden):
            vraag = False
        else:
            print('Dat is geen geldige invoer.')


ietsvragen('Hallo hoe heet jij', ['Piet', 'Jan', 'Elsje'])
ietsvragen('Hey pieter hoe oud ben jij?', [18, 19, 20, 21])
