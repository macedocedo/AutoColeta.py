
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) #headless=False comando roda sem visualizar
    page = browser.new_page() #Abre um navegador
    page.goto("https://google.com") #Link
    page.fill("input[name='q']",'tesssste') #Inputar informação
    page.click("button['btnK']") #selecionar botão
    page.wait_for_timeout(100000) #tempo que app ficará aberta
    print(page.title()) #Mostra a tela
    browser.close() #fechar


    #Fechar navegador
    #browser.close()

    #Input de informação
    #page.fill("input[name='q']",'texto')

    #input de click
    #page.click("button['infodobotão']")
    #page.click("input['infodobotão']")