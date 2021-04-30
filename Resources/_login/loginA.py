from Resources._entrarCliente.site import entrarSite
from Resources._entrarCliente.entrar import entrar
from Resources._trocaDePersonagem.troca import changeAvatar


def login(email, senha):
    from time import sleep
    import pyautogui
    import pyperclip

    pyautogui.PAUSE = 1
    entrarSite()
    i = 0
    while i != len(email):
        for j in range(10):
            #2º Passo - Fazer Login
            #2.1 - Login
            pyperclip.copy(email[i])
            pyautogui.click(414, 141)
            pyautogui.hotkey('ctrl', 'a')
            sleep(1)
            pyautogui.press('backspace')
            pyautogui.hotkey('ctrl', 'v')
            #2.2 - Senha
            pyperclip.copy(senha[i])
            pyautogui.click(651, 138)
            sleep(1)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.hotkey('ctrl', 'v')
            #Botão vamos lá
            pyautogui.click(729, 141)
            sleep(1)
            #Você é humano?
            pyautogui.click(579, 327)

            entrar()
            sleep(10)
        i += 1
