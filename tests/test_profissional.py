from pytest_bdd import given, when, then, scenarios

# Carregar os cenários do arquivo .feature
scenarios('profissional.feature')

# Definições de passo (Step Definitions)

@given('os arquivos de dados estejam disponíveis e corretos')
def step_given_arquivos_disponiveis():
    print("Os arquivos de dados estão disponíveis e corretos.")

@given('os dados estejam previamente tratados')
def step_given_dados_previamente_tratados():
    print("Os dados estão previamente tratados.")

@given('os arquivos de previsão estejam ausentes')
def step_given_arquivos_previsao_ausentes():
    print("Os arquivos de previsão estão ausentes.")

@given('os dados observados estejam indisponíveis')
def step_given_dados_observados_indisponiveis():
    print("Os dados observados estão indisponíveis.")

@given('nenhum dado esteja disponível')
def step_given_nenhum_dado_disponivel():
    print("Nenhum dado está disponível.")

