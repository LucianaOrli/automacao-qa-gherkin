import pytest
from playwright.sync_api import Page, expect

def test_google_search(page: Page):
    # O Playwright abre o navegador e vai para o site
    page.goto("https://www.google.com")
    
    # Ele verifica se o título da página está correto (QA de verdade!)
    expect(page).to_have_title("Google")
    print("\n[SUCESSO] O navegador abriu o Google e validou o título!")

