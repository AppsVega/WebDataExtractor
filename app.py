from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
print("="*20)
site = input("URL do site: ")
txpath = input("XPATH do Titulo: ")
pxpath = input("XPATH do Preço: ")
print("="*20)
try:
    driver = webdriver.Chrome()
    driver.get(site)
    Titles = driver.find_elements(By.XPATH,txpath)
    Prices = driver.find_elements(By.XPATH,pxpath)
    workbook = openpyxl.Workbook()
    Sheet_Produtos = workbook["Sheet"]
    Sheet_Produtos['A1'].value = "Nomes"
    Sheet_Produtos['B1'].value = "Preços"
    for Title,Price in zip(Titles,Prices):
        Sheet_Produtos.append([Title.text,Price.text])
    workbook.save("Produtos.xlsx")
except:
    print("Não foi possivel entrar no site ou criar o arquivo xlsx")