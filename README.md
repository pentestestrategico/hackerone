Claro! Aqui está um `README.md` completo, pronto para ser usado no seu repositório GitHub:

---

````markdown
# HackerOne Program URL Scraper

Este script Python automatiza a coleta dos domínios públicos de empresas participantes do programa de Bug Bounty da HackerOne. Ele utiliza a API oficial da HackerOne para listar os programas públicos e, em seguida, extrai os ativos do tipo `URL` que estão no escopo válido para submissão de vulnerabilidades.

## 🛠️ Funcionalidades

- Conecta-se à API da HackerOne usando autenticação básica.
- Lista todos os programas públicos de bug bounty.
- Acessa os ativos estruturados de cada programa.
- Filtra e extrai apenas os domínios (URLs) elegíveis e não arquivados.
- Salva os domínios em um arquivo `program_domains.txt`.

## 📦 Requisitos

- Python 3.6+
- Biblioteca `requests`

Instale o `requests` com:

```bash
pip install requests
````

## 🔐 Autenticação

Você precisará gerar um token de API na sua conta HackerOne:

1. Vá até [HackerOne Account Settings](https://hackerone.com/settings/api).
2. Gere um novo token de API.
3. Use o identificador como `USERNAME` e o token como `API_TOKEN` no script.

## 🚀 Como usar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/hackerone-url-scraper.git
cd hackerone-url-scraper
```

2. Edite o script e adicione seu `USERNAME` e `API_TOKEN` nas variáveis correspondentes.

3. Execute o script:

```bash
python hackerone_scraper.py
```

4. O resultado será salvo em `program_domains.txt` no mesmo diretório.

## 🧠 Observações

* Apenas domínios com tipo `URL`, não arquivados e elegíveis para submissão são listados.
* Adicionado `time.sleep(1)` entre as requisições para respeitar limites da API.

## 📄 Licença

MIT

## 👨‍💻 Autor

Canal no YouTube: [Pentest Estratégico](https://www.youtube.com/@pentestestrategico)
Desenvolvido por: **Fábio Luiz**
📧 Email: [fabioluizrl2@gmail.com](mailto:fabioluizrl2@gmail.com)


