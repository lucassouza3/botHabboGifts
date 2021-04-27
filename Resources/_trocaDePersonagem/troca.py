def changeAvatar():
  import pyautogui
  from time import sleep 
  pyautogui.click(1315, 74) #Botão mais
  pyautogui.click(1227, 109) #Personagens
  sleep(5)
  pyautogui.press('end') #FimPagina
  pyautogui.click(610, 534) #Escolher último personagem  

