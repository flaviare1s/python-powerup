#Olá, Mundo!
# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui

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

# Passo 2: Fazer login
# Passo 3: Importar a base de dados de produtos
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o cadastro para todos os produtos









