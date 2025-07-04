import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.getenv('GITHUB_TOKEN')

        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'X-GitHub-Api-Version': '2022-11-28'
        }

        # Testa o token ao iniciar
        self.verifica_token()

    def verifica_token(self):
        """Verifica se o token é válido."""
        response = requests.get(f'{self.api_base_url}/user', headers=self.headers)
        if response.status_code != 200:
            print("❌ Token inválido:", response.status_code, response.json())
        else:
            print("✅ Token válido para:", response.json().get('login'))

    def lista_repositorios(self):
        repos_list = []

        for page_num in range(1, 20):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)

                print(f"Status Code da página {page_num}: {response.status_code}")

                if response.status_code != 200:
                    print(f"Erro: {response.json()}")
                    continue

                page_data = response.json()
                if isinstance(page_data, list):
                    repos_list.append(page_data)
                else:
                    print(f"Resposta inesperada na página {page_num}: {page_data}")

            except Exception as e:
                print(f"Erro na página {page_num}: {e}")
                continue

        return repos_list

    def nomes_repos(self, repos_list):
        repo_names = []
        for page in repos_list:
            for repo in page:
                try:
                    repo_names.append(repo['name'])
                except:
                    pass
        return repo_names

    def nomes_linguagens(self, repos_list):
        repo_languages = []
        for page in repos_list:
            for repo in page:
                try:
                    repo_languages.append(repo['language'])
                except:
                    pass
        return repo_languages

    def cria_df_linguagens(self):
        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)

        dados = pd.DataFrame()
        dados['repository_name'] = nomes
        dados['language'] = linguagens

        return dados

if __name__ == '__main__':
    
    amazon_rep = DadosRepositorios('amzn')
    ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()

    
    netflix_rep = DadosRepositorios('netflix')
    ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()

    
    spotify_rep = DadosRepositorios('spotify')
    ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()

    
    os.makedirs('dados', exist_ok=True)

    # Salvando os dados em CSV
    ling_mais_usadas_amzn.to_csv('dados/linguagens_amzn.csv', index=False)
    ling_mais_usadas_netflix.to_csv('dados/linguagens_netflix.csv', index=False)
    ling_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv', index=False)

    print("✅ Arquivos CSV gerados com sucesso na pasta 'dados/'")
