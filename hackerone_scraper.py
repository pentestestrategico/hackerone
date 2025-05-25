import requests
import time

# Banner com informações do autor
def print_banner():
    banner = """
    ###############################################
    # Script HackerOne Program Domains Scraper    #
    # Autor: Fabio Luiz                            #
    # Canal YouTube: PentestEstratégico            #
    # Email: fabioluizrl2@gmail.com                #
    ###############################################
    """
    print(banner)

print_banner()

# Substitua pelos seus dados de API
USERNAME = 'seu usuario aqui'
API_TOKEN = 'sua chave api do hackerone'

# Cabeçalhos da requisição
headers = {
    'Accept': 'application/json'
}

# URL base da API HackerOne
base_url = 'https://api.hackerone.com/v1/hackers/programs'

# Parâmetros de paginação
page = 1
per_page = 100
program_handles = []

# Etapa 1: Obter a lista de programas públicos
while True:
    params = {
        'page[number]': page,
        'page[size]': per_page
    }

    response = requests.get(base_url, auth=(USERNAME, API_TOKEN), headers=headers, params=params)

    if response.status_code != 200:
        print(f'Erro na requisição: {response.status_code}')
        break

    data = response.json()
    if not data['data']:
        break

    for program in data['data']:
        handle = program['attributes'].get('handle')
        if handle:
            program_handles.append(handle)

    page += 1
    time.sleep(1)  # Evitar sobrecarregar a API

# Etapa 2: Para cada programa, obter os ativos do tipo URL
program_domains = []

for handle in program_handles:
    scope_url = f'https://api.hackerone.com/v1/hackers/programs/{handle}/structured_scopes'
    response = requests.get(scope_url, auth=(USERNAME, API_TOKEN), headers=headers)

    if response.status_code != 200:
        print(f'Erro ao obter escopo para {handle}: {response.status_code}')
        continue

    data = response.json()
    for asset in data.get('data', []):
        attributes = asset.get('attributes', {})
        asset_type = attributes.get('asset_type')
        asset_identifier = attributes.get('asset_identifier')
        eligible_for_submission = attributes.get('eligible_for_submission', False)
        archived_at = attributes.get('archived_at')

        if asset_type == 'URL' and eligible_for_submission and archived_at is None:
            print(f'{handle} -> {asset_identifier}')
            program_domains.append(asset_identifier)

    time.sleep(1)  # Evitar sobrecarregar a API

# Salvar os domínios em um arquivo txt
with open('program_domains.txt', 'w') as file:
    for domain in program_domains:
        file.write(domain + '\n')

print(f'\n{len(program_domains)} domínios salvos em program_domains.txt')
