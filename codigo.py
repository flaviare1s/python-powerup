#Olá, Mundo!
# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
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
pyautogui.click(x=735, y=515, clicks=1)
pyautogui.write("senha1234")
# Passo 3: Importar a base de dados de produtos
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o cadastro para todos os produtos









