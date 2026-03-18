from pytest_bdd import scenarios, given, when, then, parsers
import pytest

scenarios('features/profissional_novo.feature')

@pytest.fixture
def base_dados():
    return {"user": "luciana@teste.com", "pass": "123456"}

# --- LOGIN ---
@given("que o usuário está na página de login", target_fixture="res")
def step_dado():
    return {}

@when(parsers.re(r'ele informa o email "(?P<email>.*)" e a senha "(?P<senha>.*)"'))
def step_quando(res, email, senha, base_dados):
    # PRIORIDADE 1: Verificar se está vazio (o que causou o erro)
    if not senha or senha == "":
        res["st"] = "erro_campo_vazio"
    # PRIORIDADE 2: Verificar formato
    elif "@" not in email or email.startswith("@"):
        res["st"] = "erro_formato"
    # PRIORIDADE 3: Sucesso
    elif email == base_dados["user"] and senha == base_dados["pass"]:
        res["st"] = "sucesso"
    # PRIORIDADE 4: Senha errada para usuário conhecido
    elif email == base_dados["user"]:
        res["st"] = "erro_senha"
    # PRIORIDADE 5: Usuário não existe
    else:
        res["st"] = "erro_usuario"

@then(parsers.re(r'o resultado deve ser "(?P<resultado_esperado>.*)"'))
def step_entao(res, resultado_esperado):
    assert res.get("st") == resultado_esperado

# --- COMPRA ---
@given("que o usuário está logado no sistema", target_fixture="comp")
def step_logado():
    return {}

@when(parsers.re(r'ele tenta comprar o produto "(?P<produto>.*)" com o cartão "(?P<cartao>.*)"'))
def step_compra(comp, produto, cartao):
    status_map = {"VALIDO": "aprovada", "ROUBADO": "bloqueada"}
    comp["st"] = status_map.get(cartao, "recusada")

@then(parsers.re(r'a compra deve ser "(?P<status>.*)"'))
def step_valida_compra(comp, status):
    assert comp.get("st") == status
