
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) #headless=False comando roda sem visualizar
    page = browser.new_page() #Abre um navegador
    page.goto("https://google.com") #Link
    page.locator('xpath=//*[@id="APjFqb"]').click() #click na busca
    page.fill('xpath=//*[@id="APjFqb"]',"teste") #Texto que será preenchido
    page.keyboard.press('Enter') #Enter 
    page.wait_for_timeout(50000) #tempo que app ficará aberta
    browser.close() #fechar
  
