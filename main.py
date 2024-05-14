import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.7

#Abrir o Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Entrar no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#Daley
time.sleep(2)

#Login
pyautogui.click(x=920, y=486)
pyautogui.write("gustavogomes.bsb68@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345678910")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)

#Lendo a base de dados
tabela = pd.read_csv("produtos.csv")

##Preeechendo a tabela
for linha in tabela.index:
  #Casdastro
  pyautogui.click(x=653, y=336)
  pyautogui.write(str(tabela.loc[linha,"codigo"]))
  pyautogui.press("tab")
  #Marca
  pyautogui.write(str(tabela.loc[linha,"marca"]))
  pyautogui.press("tab")
  #Tipo
  pyautogui.write(str(tabela.loc[linha,"tipo"]))
  pyautogui.press("tab")
  #Categoria
  pyautogui.write(str(tabela.loc[linha,"categoria"]))
  pyautogui.press("tab")
  #Preco
  pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
  pyautogui.press("tab")
  #Custo
  pyautogui.write(str(tabela.loc[linha,"custo"]))
  pyautogui.press("tab")
  #Obs
  obs = str(tabela.loc[linha,"obs"])
  if obs != "nan":
    pyautogui.write(obs)
  #fim
  pyautogui.press("enter")
  pyautogui.scroll(4000)