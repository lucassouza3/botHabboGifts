from Resources._trocaDePersonagem.sairHabbo import sairHabbo


def changeAvatar():
    import pyautogui
    from time import sleep
    pyautogui.click(976, 359)  #clique área em branco
    sleep(2)
    pyautogui.press('end')  #FimPagina
    pyautogui.click(610, 534)  #Escolher último personagem
