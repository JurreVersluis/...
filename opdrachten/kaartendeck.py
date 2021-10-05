Allekaarten = True
kaart = ''
deck = {'harten 2', 'harten 3', 'harten 4', 'harten 5', 'harten 6', 'harten 7', 'harten 8', 'harten 9', 'harten 10', 'harten boer', 'harten vrouw', 'harten heer', 'harten aas',
        'ruiten 2', 'ruiten 3', 'ruiten 4', 'ruiten 5', 'ruiten 6', 'ruiten 7', 'ruiten 8', 'ruiten 9', 'ruiten 10', 'ruiten boer', 'ruiten vrouw', 'ruiten heer', 'ruiten aas',
        'klaver 2', 'klaver 3', 'klaver 4', 'klaver 5', 'klaver 6', 'klaver 7', 'klaver 8', 'klaver 9', 'klaver 10', 'klaver boer','klaver vrouw', 'klaver heer', 'klaver aas',
        'schoppen 2', 'schoppen 3', 'schoppen 4', 'schoppen 5', 'schoppen 6', 'schoppen 7', 'schoppen 8', 'schoppen 9', 'schoppen boer', 'schoppen 10', 'schoppen vrouw', 'schoppen heer', 'schoppen aas', 'joker', 'joker', 'joker'}
kaarten = list()
for i in range(7):
        kaart = (deck.pop())
        kaarten.append(kaart)
        print(f'kaart {i + 1}: {kaarten[i]}')

print('')
print(f'De overige kaarten: {deck}')

