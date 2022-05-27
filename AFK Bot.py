from pyautogui import press
from time import sleep

print("*---------------------*")
sleep(0.5)
print("    Howert AFK Bot")
sleep(0.5)
print("*---------------------*")
sleep(0.5)
print("Program W,A,S,D tuşlarıyla kendi kendine hareket ederek oyun tarafından atılmadan afk kalmanızı sağlar.")
sleep(0.5)
input("Başlamak için bir tuşa tıklayın.")
print("Afk botu başlatılıyor. Oyun ekranına geçiniz.")
sleep(3)
def afkbot():
    press('w')
    press('w')
    press('w')
    sleep(2)
    press('s')
    press('s')
    press('s')
    sleep(3)
    press('a')
    press('a')
    press('a')
    sleep(3)
    press('d')
    press('d')
    press('d')

while True:
    afkbot()
