import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
tekens = ['@', '#', '$', '%', '&', '_', '?']
cijfers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
gekozenletters = []
randomgetal6 = random.randrange(4,7)

randomletters = random.randrange(14, 17)
for i in range(randomletters):
    r = random.choice(letters)
    gekozenletters.append(r)

hoofdletters = random.randrange(1,7)
for i in range(hoofdletters):
    gekozenletters[i] = gekozenletters[i].upper()

for i in range(10):
    randomgetal = random.randrange(0, 5)
    randomizer = gekozenletters.pop(randomgetal)
    gekozenletters.append(randomizer)

for i in range(3):
    randomgetal2 = random.randrange(1, (len(gekozenletters) - 1))
    randomgetal3 = random.randrange(0,7)
    randomteken = tekens[randomgetal3]
    gekozenletters.insert(randomgetal2, randomteken)


for i in range(randomgetal6):
    randomgetal5 = random.randrange(0, 9)
    randomnummer = cijfers[randomgetal5]
    randomgetal4 = random.randrange(3, (len(gekozenletters)))
    gekozenletters.insert(randomgetal4, randomnummer)
lengte = len(gekozenletters)

som = 24 - lengte
som2 = lengte - 24

if som > 0:
    for i in range(som):
        d = random.choice(letters)
        gekozenletters.append(d)

if som2 > 0:
    gekozenletters.pop(-1)

print(len(gekozenletters))
print(gekozenletters)
