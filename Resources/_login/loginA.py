from Resources._entrarCliente.entrar import entrar
from Resources._trocaDePersonagem.troca import changeAvatar


def login(email, senha):
    from time import sleep
    import pyautogui
    import pyperclip
    pyautogui.PAUSE = 1
    #1º Passo - Entrar no site.
    pyautogui.hotkey('alt', 'tab')
    sleep(1)
    pyautogui.hotkey('ctrl', 't')  #nova aba
    site = 'https://www.habbo.com.br/'
    sleep(5)
    #manda o conteúdo de site para a área de transferência
    pyperclip.copy(site)
    pyautogui.hotkey('ctrl', 'v')  #cola conteúdo da área de transferência
    pyautogui.press('enter')
    sleep(3)
    #2º Passo - Fazer Login
    #2.1 - Login
    pyperclip.copy(email)
    pyautogui.click(414, 141)
    pyautogui.hotkey('ctrl', 'a')
    sleep(1)
    pyautogui.press('backspace')
    pyautogui.hotkey('ctrl', 'v')
    #2.2 - Senha
    pyperclip.copy(senha)
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
    changeAvatar()
