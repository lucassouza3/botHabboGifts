import pyautogui
import pyperclip
from time import sleep
from Resources._trocaDePersonagem.sairHabbo import sairHabbo
from Resources._trocaDePersonagem.troca import changeAvatar


def entrar():
    i = 0
    for i in range(0, 5):
        sleep(10)
        #Botão download
        pyautogui.click(1206, 201)
        sleep(3)
        # Inicie e faça login: (x = 689, y = 242)
        pyautogui.click(689, 242)
        sleep(3)
        #Launcher
        pyautogui.click(569, 428)
        sleep(2)
        #Maximizar
        pyautogui.hotkey('win', 'up')
        sleep(20)
        pyautogui.click(936, 384)  #C.A vencciido
        sleep(2)
        #Abrir janela no client
        pyautogui.click(585, 226)
        #looping coletar

        for i in range(2):
            pyautogui.click(692, 432)  #meio
            sleep(1)
            pyautogui.click(483, 456)  #lado

        #sai looping
        pyautogui.click(692, 432)  #meio
        sleep(2)
        pyautogui.hotkey('alt', 'f4')
        personagens = 'https://www.habbo.com.br/settings/avatars'
        pyautogui.click(1027, 52)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyperclip.copy(personagens)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        sleep(5)
        '''     pyautogui.click(1180, 111)  #fechar janela no client
        sleep(1)
        pyautogui.click(1315, 74)  #Botão mais
        sleep(1)
        pyautogui.click(1227, 109)  #Personagens
        pyautogui.hotkey('alt', 'f4')'''
        changeAvatar()
        i += 1
    sairHabbo()