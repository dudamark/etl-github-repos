import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

class ManipulaRepositorios:

    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.getenv('GITHUB_TOKEN')

        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'X-GitHub-Api-Version': '2022-11-28'
        }

        
        self.verifica_token()

    def verifica_token(self):
        """Verifica se o token está válido e autenticado"""
        response = requests.get(f'{self.api_base_url}/user', headers=self.headers)
        if response.status_code != 200:
            print("❌ Token inválido:", response.status_code, response.json())
        else:
            print(f"✅ Token válido. Usuário autenticado: {response.json().get('login')}")

    def cria_repo(self, nome_repo):
        data = {
            "name": nome_repo,
            "description": "Dados dos repositórios de algumas empresas",
            "private": False
        }
        response = requests.post(f"{self.api_base_url}/user/repos", json=data, headers=self.headers)
        print(f'📁 Status da criação do repositório "{nome_repo}": {response.status_code}')
        if response.status_code != 201:
            print("⚠️ Detalhes:", response.json())

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):
        # Verifica se o arquivo existe
        if not os.path.exists(caminho_arquivo):
            print(f"❌ Arquivo não encontrado: {caminho_arquivo}")
            return

        # Codifica o conteúdo do arquivo
        with open(caminho_arquivo, "rb") as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content).decode("utf-8")

        # Upload via GitHub API
        url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}"
        data = {
            "message": f"Adicionando o arquivo {nome_arquivo}",
            "content": encoded_content
        }

        response = requests.put(url, json=data, headers=self.headers)
        print(f'📤 Upload "{nome_arquivo}": {response.status_code}')
        if response.status_code not in (201, 200):
            print("⚠️ Erro:", response.json())

if __name__ == '__main__':
    
    novo_repo = ManipulaRepositorios('dudamark')

    # Nome do repositório a ser criado
    nome_repo = 'linguagens-repositorios-empresas'

    # Criação do repositório (ignorado se já existe)
    novo_repo.cria_repo(nome_repo)

    # Upload de arquivos CSV
    novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'dados/linguagens_amzn.csv')
    novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv')
    novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv')

