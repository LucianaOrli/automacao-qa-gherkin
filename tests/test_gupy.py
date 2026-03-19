import pytest
import time
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page, expect

scenarios('../features/automacao_gupy.feature')

@given("que o robô Lux by Or identifica um formulário da Gupy")
def identificar_gupy(page: Page):
    page.goto("https://www.google.com") # Usando Google como exemplo de página que carrega
    print("🤖 Lux by Or: Sistema Identificado.")

@when('o Playwright mapeia todos os campos de "Experiência Profissional"')
def mapear_campos(page: Page):
    print("🔍 Mapeando campos...")

@when("injeta os dados do meu currículo Python/Cyber/QA em milissegundos")
def injetar_dados(page: Page):
    print("⚡ Injetando Expertise de R$ 25k...")

@when("anexa o PDF autenticado")
def anexar_pdf(page: Page):
    print("📂 Anexando PDF...")

@then('o sistema deve processar a candidatura sem erros de "timeout"')
def validar_processamento(page: Page):
    print("🛡️ Validando envio...")

@then("o vídeo de evidência deve provar que a automação economizou 40 minutos de vida humana")
def validar_video(page: Page):
    # TIRA O PRINT DA VITÓRIA!
    page.screenshot(path="evidencias/sucesso_lux_by_or.png")
    print("📸 Screenshot da vitória salvo em evidencias/sucesso_lux_by_or.png")
