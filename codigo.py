#Olá, Mundo!
# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui #para instalar : pip install pyautogui
import time

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um textoBOHA000251    Hashtag
# pyautogui.press -> apertar 1 teclaMOMU000111  Multilaser  tipo    categoria   preco_unitario  custo   obs 

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


for linha in tabela.index:

    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=624, y=299, clicks=1)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]

    #preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    pyautogui.write(str(obs))

    #apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000)

# Passo 5: Repetir o cadastro para todos os produtos









