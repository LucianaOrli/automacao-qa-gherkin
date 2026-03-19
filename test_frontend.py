import pytest
from playwright.sync_api import Page, expect

def test_google_search(page: Page):
    # Vai para o Google
    page.goto("https://www.google.com")
    
    # Clica na barra de pesquisa e digita "Vagas QA Playwright"
    # O seletor 'textarea[name="q"]' é como o robô identifica a barra
    page.fill('textarea[name="q"]', "Vagas QA Playwright")
    
    # Aperta "Enter" no teclado
    page.keyboard.press("Enter")
    
    # Espera o resultado carregar
    page.wait_for_timeout(3000)
    
    print("\n[SUCESSO] O robô pesquisou por vagas de QA!")
