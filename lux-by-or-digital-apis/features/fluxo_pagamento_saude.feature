# language: pt
Funcionalidade: Processamento de Liquidação Financeira Enterprise
  Contexto: 
    Dado que o motor de regras da Orli Digital Health está ativo
  Cenário: Validar integração e Webhook de Notificação
    Quando o serviço envia os dados para a API
    Então a API deve retornar status 201
    E o Playwright intercepta o Webhook "EFETIVADO"
