# language: pt
Funcionalidade: Automação de Cadastro em Plataformas ATS

  Cenário: Preenchimento veloz de formulários repetitivos
    Dado que o robô Lux by Or identifica um formulário da Gupy
    Quando o Playwright mapeia todos os campos de "Experiência Profissional"
    E injeta os dados do meu currículo Python/Cyber/QA em milissegundos
    E anexa o PDF autenticado
    Então o sistema deve processar a candidatura sem erros de "timeout"
    E o vídeo de evidência deve provar que a automação economizou 40 minutos de vida humana
