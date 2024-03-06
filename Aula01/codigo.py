# Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Fazer login

# Importar a base de dados
# Cadastrar 1 produto
# Repetir o processo de cadastro ate acabar

import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5
# pyautogui.hotkey("ctrl", "c")

pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

time.sleep(1)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(7)

# clica no campo de texto
pyautogui.click(558, 375) #peguei posição usando o auxiliar.py
# pyautogui.click(558, 375, clicks=2, button="primary")

pyautogui.write("email@email.com")
pyautogui.press("tab")
pyautogui.write("senha1234")
pyautogui.press("enter")
time.sleep(7)
pyautogui.click(602, 323)

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(599, 256)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(obs)
    
    pyautogui.press("tab")

    pyautogui.press("enter")

    time.sleep(2)

    pyautogui.scroll(5000)

#pyautogui.press("home")
