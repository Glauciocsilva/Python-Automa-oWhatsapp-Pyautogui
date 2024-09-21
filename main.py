import pyautogui
import webbrowser
from time import sleep
import cv2
import pyperclip

telefones = [559999999999,559999999999,559999999999]
'''
Quais passos manuais preciso fazer
para enviar uma mensagem para várias pessoas?
'''
import pyautogui
import webbrowser
from time import sleep
# 1- lista de números
telefones = ['digite os numeros com cód. país e ddd']

#ou caso tenha uma lista em txt dos números:
'''
telefones = []
with open('nomeDaLista.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    print(telefones)  
'''
# 2 Eviar as mensagnes individualmente
for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}') 
    sleep(2)
    iniciar_conversa = pyautogui.locateCenterOnScreen('iniciar_conversa.png', confidence=0.8)
    pyautogui.click(iniciar_conversa[0], iniciar_conversa[1])
    sleep(10)
    usar_web = pyautogui.locateCenterOnScreen('usar_web.png', confidence=0.8)
    pyautogui.click(usar_web[0], usar_web[1])
    sleep(30)
    pyautogui.typewrite('Digite aqui sua mensagem ')
    sleep(1)
    pyautogui.hotkey('enter')
    pyautogui.click(x=1334,y=18,duration=1)
    
