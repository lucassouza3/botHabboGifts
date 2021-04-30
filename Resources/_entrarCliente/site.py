import pyperclip
import pyautogui
from time import sleep


def entrarSite():
    #1º Passo - Entrar no site.
    pyautogui.hotkey('alt', 'tab')
    sleep(1)
    pyautogui.hotkey('ctrl', 'w')  #apaga ultima aba
    sleep(1)
    pyautogui.hotkey('ctrl', 't')  #nova aba
    site = 'https://www.habbo.com.br/'
    sleep(5)
    #manda o conteúdo de site para a área de transferência
    pyperclip.copy(site)
    pyautogui.hotkey('ctrl', 'v')  #cola conteúdo da área de transferência
    pyautogui.press('enter')
    sleep(3)
