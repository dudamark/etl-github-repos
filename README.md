# 🚀 ETL GitHub API: Linguagens de Repositórios de Grandes Empresas

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![GitHub API](https://img.shields.io/badge/GitHub%20API-v3-brightgreen)](https://docs.github.com/en/rest)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Este projeto realiza um fluxo **ETL (Extração, Transformação e Carga)** utilizando a [API do GitHub](https://docs.github.com/en/rest), extraindo dados dos repositórios públicos de empresas como:

- 🛒 **Amazon** (`amzn`)
- 🎬 **Netflix** (`netflix`)
- 🎵 **Spotify** (`spotify`)

Com os dados extraídos, o sistema:
- 🔍 Identifica as linguagens mais usadas
- 📁 Gera arquivos `.csv` para cada empresa
- ☁️ Cria um repositório no GitHub e faz upload automático via API

---

## ⚙️ Pré-requisitos

- Python `3.9+`
- Token GitHub com permissão `public_repo`
- Conta GitHub válida

---

## 🚀 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/dudamark/etl-github-repos.git
cd etl-github-repos
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv myvenv
.\myvenv\Scripts/activate  # Windows
# source myvenv/bin/activate  # Linux/macOS
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

> Ou, manualmente:
>
> ```bash
> pip install requests python-dotenv pandas
> ```

---

## 🔐 Configuração do `.env`

Crie um arquivo `.env` com o seguinte conteúdo:

```env
GITHUB_TOKEN=seu_token_aqui
```

- Você pode gerar um token em: [https://github.com/settings/tokens](https://github.com/settings/tokens)
- Marque ao menos `public_repo`

---

## 🧪 Execução

### 1. Extração dos dados

```bash
python dados_repos.py
```

Gera arquivos `.csv` com as linguagens utilizadas pelos repositórios.

### 2. Upload dos arquivos no GitHub

```bash
python manipula_repos.py
```

- Cria um repositório chamado `linguagens-repositorios-empresas`
- Envia os arquivos `.csv` gerados para ele

---

## 📦 Gerar `requirements.txt` (opcional)

```bash
pip freeze > requirements.txt
```

---

## 📄 Licença

Distribuído sob a licença MIT. Veja o arquivo [`LICENSE`](LICENSE) para mais detalhes.

---

## 🙋‍♀️ Contato

Desenvolvido por [@dudamark](https://github.com/dudamark).  
Contribuições, issues e feedbacks são sempre bem-vindos!
