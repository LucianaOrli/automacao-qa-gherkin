# language: pt
Funcionalidade: Testes Profissionais QA

  Esquema do Cenário: Validação de Acesso
    Dado que o usuário está na página de login
    Quando ele informa o email "<email>" e a senha "<senha>"
    Então o resultado deve ser "<resultado_esperado>"

    Exemplos:
      | email              | senha    | resultado_esperado |
      | luciana@teste.com  | 123456   | sucesso            |
      | luciana@teste.com  | errada   | erro_senha         |
      | invalido@teste.com | 123456   | erro_usuario       |
      | @vazio.com         | 123456   | erro_formato       |
      | luciana@teste.com  |          | erro_campo_vazio   |

  Esquema do Cenário: Fluxo de Compra
    Dado que o usuário está logado no sistema
    Quando ele tenta comprar o produto "<produto>" com o cartão "<cartao>"
    Então a compra deve ser "<status>"

    Exemplos:
      | produto | cartao    | status    |
      | Teclado | VALIDO    | aprovada  |
      | Mouse   | INVALIDO  | recusada  |
      | Monitor | EXPIRADO  | recusada  |
      | Headset | SEM_SALDO | recusada  |
      | WebCam  | ROUBADO   | bloqueada |
