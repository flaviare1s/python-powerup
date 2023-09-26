#Olá, Mundo!
# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui #para instalar : pip install pyautogui
import time

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas)

pyautogui.PAUSE = 0.5

# Abrir o Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Esperar o site carregar
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=727, y=407, clicks=1)
pyautogui.write("emaildeteste@gmail.com")

pyautogui.press("tab")
pyautogui.write("senha1234")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Passo 3: Importar a base de dados de produtos
# Pandas: pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto
pyautogui.click(x=624, y=299, clicks=1)

#preencher os campos
pyautogui.write("MOLO000251")
pyautogui.press("tab")
pyautogui.write("Logitech")
pyautogui.press("tab")
pyautogui.write("Mouse")
pyautogui.press("tab")
pyautogui.write("1")
pyautogui.press("tab")
pyautogui.write("25.95")
pyautogui.press("tab")
pyautogui.write("6.5")
pyautogui.press("tab")
pyautogui.write("NaN")

#apertar para enviar
pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.scroll(50000)

# Passo 5: Repetir o cadastro para todos os produtos









