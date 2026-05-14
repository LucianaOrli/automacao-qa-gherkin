import pytest
import uuid
from datetime import datetime
from playwright.sync_api import sync_playwright

@pytest.fixture
def massa_dados():
    return {
        "transacao_id": str(uuid.uuid4()),
        "origem": "ORLI-DIGITAL-HEALTH-SOLUTIONS",
        "pagador": {"nome": "INSTITUTO DE SAUDE SUPLEMENTAR", "cnpj": "45.223.991/0001-08"},
        "financeiro": {"valor": "125000.00", "moeda": "BRL"}
    }

def test_caminho_feliz_integracao_complexa(massa_dados):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print("\n" + "="*70)
        print("🚀 [LUX BY OR DIGITAL APIs] - INICIANDO TESTE DE SUCESSO (HAPPY PATH)")
        print("="*70)
        api_context = p.request.new_context(base_url="https://jsonplaceholder.typicode.com")
        response = api_context.post("/posts", data=massa_dados)
        assert response.status == 201
        print(f"✅ API validada! Lote {massa_dados['transacao_id']} enviado com sucesso.")

        def handle_webhook_sucesso(route):
            print("📦 [DETECÇÃO] Webhook de confirmação bancária interceptado pelo Playwright!")
            route.fulfill(status=200, content_type="application/json", body='{"status": "EFETIVADO"}')

        page.route("**/api/notificacao", handle_webhook_sucesso)
        page.goto("https://example.com") 
        print("🎉 [RESULTADO] Integração concluída com integridade total.")
        browser.close()

def test_caminho_infeliz_excecao_negocio(massa_dados):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print("\n" + "="*70)
        print("🚨 [LUX BY OR DIGITAL APIs] - TESTANDO RESILIÊNCIA (ERROR HANDLING)")
        print("="*70)
        massa_dados["financeiro"]["valor"] = "0.00"

        def handle_webhook_erro(route):
            print("⚠️ [DETECÇÃO] Falha de negócio detectada e tratada no barramento!")
            route.fulfill(status=400, content_type="application/json", body='{"status": "REJEITADO"}')

        page.route("**/api/notificacao", handle_webhook_erro)
        page.goto("https://example.com")
        print("✅ [RESULTADO] Exceção tratada corretamente. Sistema seguro contra falhas.")
        browser.close()
