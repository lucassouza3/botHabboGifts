from time import sleep
import pyautogui


def entrar():
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
    #Abrir janela no client
    pyautogui.click(585, 226)
    #looping coletar
    for i in range(2):
        pyautogui.click(692, 432)  #meio
        sleep(2)
        pyautogui.click(483, 456)  #lado
    #sai looping
    pyautogui.click(692, 432)  #meio
    sleep(2)
    #fechar janela no client
    pyautogui.click(1180, 111)
