
from playwright.sync_api import sync_playwright
import time
from url import *

def chrome():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False para rodar sem visualizar
        page = browser.new_page()  #Abre um navegador
        page.goto(URL) #Link
        time.sleep(1) #Tempo
        page.locator('xpath=//*[@id="APjFqb"]').click()  # click na busca
        page.fill('xpath=//*[@id="APjFqb"]', "euro")  # Texto que será preenchido
        time.sleep(1) #Tempo
        page.keyboard.press('Enter') # Enter

        try:
            # Identificar e imprimir o conteúdo da tabela
            table_locator = page.locator("//*[@id='knowledge-currency__updatable-data-column']/div[1]/div[2]/span[1]")
            table_content = table_locator.inner_text()
            print(table_content)
        except Exception as e:
            print(f"Erro ao acessar a tabela: {e}")

        input("Pressione Enter para fechar")
        browser.close()  # fechar

chrome()
