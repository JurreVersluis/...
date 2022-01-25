import time
import pyautogui
kleuren = ['Rood', 'Blauw', 'Geel', 'Groen']
time.sleep(3)
for i in range(4):
    kleur = kleuren[i]
    for i in range(10):
        pyautogui.write(f"'{kleur} {i}', ")
    for i in range(1 , 10):
        pyautogui.write(f"'{kleur} {i}', ")
pyautogui.press('enter')
for i in range(4):
    kleur = kleuren[i]
    for b in range(2):
        pyautogui.write(f"'{kleur} pak 2 kaart.', ")
for i in range(4):
    kleur = kleuren[i]
    for b in range(2):
        pyautogui.write(f"'{kleur} keer om kaart.', ")
for i in range(4):
    kleur = kleuren[i]
    for b in range(2):
        pyautogui.write(f"'{kleur} sla beurt over kaart.', ")
for i in range(4):
    pyautogui.write("'4 kaarten pakken.', ")
for i in range(4):
    pyautogui.write("'kleur keuzekaart.', ")
