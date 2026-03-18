Feature: Processamento e Identificação de Ondas de Calor

  # Cenários de Processamento de Dados
  Cenário: Processamento automático de dados válidos
    Dado que os arquivos de dados estejam disponíveis e corretos
    Quando forem importados
    Então o sistema deve processá-los automaticamente em até 10 minutos

  Cenário: Processamento de dados pré-tratados
    Dado que os dados estejam previamente tratados
    Quando forem carregados
    Então o sistema deve pular etapas de limpeza e ir direto ao processamento

  Cenário: Falha na importação de arquivos previstos
    Dado que os arquivos de previsão estejam ausentes
    Quando o sistema tentar importar
    Então deve gerar um alerta visual e registrar o erro

  Cenário: Falha na importação de arquivos observados
    Dado que os dados observados estejam indisponíveis
    Quando o sistema tentar importar
    Então deve processar apenas os dados previstos

  Cenário: Falha geral de importação
    Dado que nenhum dado esteja disponível
    Quando a coleta ocorrer
    Então o sistema deve usar dados do dia anterior e exibir aviso

  # Identificação de Ondas de Calor
  Cenário: Identificação com critérios padrão
    Dado que existam dados dos últimos 5 dias com temperatura ≥ 5°C acima da média
    Quando o sistema processar os dados
    Então deve marcar a localidade como em onda de calor

  Cenário: Registro de evento identificado
    Dado que uma onda de calor tenha sido detectada
    Quando for confirmada
    Então o sistema deve registrar e destacar no mapa e lista

  Cenário: Identificação com critérios personalizados
    Dado que o usuário configure 3 dias e 3°C
    E os dados atendam aos critérios
    Quando reprocessar os dados
    Então o sistema deve identificar a onda de calor corretamente

  Cenário: Rejeição de critério inválido (grau negativo)
    Dado que o usuário insira -2°C como parâmetro
    Quando clicar em "Salvar"
    Então o sistema deve impedir e exibir erro

  Cenário: Inserção de valor acima do limite permitido
    Dado que o usuário tente inserir 20 dias
    Quando tentar salvar
    Então o botão "+" deve estar desabilitado e o valor rejeitado

  Cenário: Inserção de valor de referência manual
    Dado que o usuário ative o botão de valor personalizado
    Quando inserir 31.5°C
    Então o sistema deve utilizar esse valor no cálculo

  Cenário: Retorno aos parâmetros padrão
    Dado que o usuário tenha alterado os critérios
    Quando clicar em "Restaurar Padrão"
    Então os valores devem voltar a 5 dias e 5°C

  Cenário: Cálculo com valor personalizado de referência
    Dado que o usuário insira um valor de referência manual
    Quando o sistema reprocessar
    Então deve calcular usando o valor personalizado

  Cenário: Comparação entre configurações diferentes
    Dado que o analista altere os critérios duas vezes
    Quando gerar dois relatórios
    Então deve ser possível comparar os efeitos dos parâmetros

  # Visualização no Mapa e Interface
  Cenário: Exibir cidade afetada no mapa
    Dado que uma cidade esteja em onda de calor
    Quando o usuário abrir o mapa
    Então a cidade deve estar destacada com legenda e tooltip

  Cenário: Exibir subestação impactada
    Dado que uma subestação esteja em cidade afetada
    Quando o usuário acessar o mapa
    Então o ativo deve estar listado como impactado

  Cenário: Acessar aba “Boletim de Ondas de Calor”
    Dado que o sistema esteja atualizado
    Quando o usuário acessar essa aba
    Então os dados de calor devem estar sincronizados

  Cenário: Acessar aba “Centro de Carga”
    Dado que haja dados energéticos associados
    Quando o usuário acessar essa aba
    Então os dados devem estar disponíveis e relacionados à onda de calor

  Cenário: Interação com gráficos
    Dado que haja gráfico carregado
    Quando o usuário passar o mouse sobre um ponto
    Então deve exibir os valores em tooltip

  Cenário: Interação com mapa por clique
    Dado que uma cidade esteja marcada
    Quando o usuário clicar nela
    Então deve exibir detalhes da temperatura e dias acima da média

  Cenário: Exibir legenda de severidade
    Dado que diferentes níveis de onda de calor existam
    Quando o usuário visualizar o mapa
    Então as legendas devem indicar intensidade (leve, moderada, severa)

  Cenário: Dados ausentes no mapa
    Dado que não haja ondas de calor em andamento
    Quando o usuário acessar o mapa
    Então o status "Ausente" deve ser exibido

  # Alertas e Notificações
  Cenário: Enviar e-mail em falha de importação
    Dado que a coleta falhe
    Quando o erro for registrado
    Então o sistema deve enviar notificação por e-mail ao responsável

  Cenário: Operar com previsão ausente
    Dado que apenas dados observados estejam disponíveis
    Quando a importação ocorrer
    Então o sistema deve continuar operando normalmente

  Cenário: Operar com observações ausentes
    Dado que apenas os dados previstos estejam disponíveis
    Quando o sistema rodar
    Então ele deve processar apenas a previsão
