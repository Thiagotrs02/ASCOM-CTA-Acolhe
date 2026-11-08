# 🤝 ASCOM CTA Acolhe — Sistema de Triagem e Gestão de Acolhimento Noturno

> **Projeto Prático de Engenharia de Software (MVP)**  
> Sistema de gestão socioassistencial desenvolvido para otimizar o atendimento no Centro Temporário de Acolhimento (CTA) da **ASCOM São Mateus**, reduzindo o tempo de entrada e eliminando duplicidades de cadastros decorrentes de erros de grafia nas fichas da abordagem de rua (SEAS).

---

## 🎯 Problema e ODS Alinhado

* **Problema:** Acolhimento noturno lento e duplicação constante de prontuários provocada por divergências fonéticas/ortográficas no registo de nomes em fichas de papel trazidas pelas equipas do SEAS.
* **Impacto Social (ODS 10):** Alinhado à **Meta 10.2 da ONU (Redução das Desigualdades)**, promovendo a inclusão social e o atendimento humanizado, rápido e acessível à população em situação de vulnerabilidade.

---

## 🚀 Funcionalidades Principais (MVP)

1. **🔐 Autenticação Segura (Tela 1):** Login de operadores e educadores sociais com proteção contra ataques de força bruta, sessões protegidas e hashing de passwords (Argon2id/bcrypt).
2. **🔍 Triagem e Busca Antiduplicação (Tela 2):** Consulta inteligente de assistidos por nome aproximado e data de nascimento utilizando o algoritmo fonético `RapidFuzz`, com pontuação de similaridade (%) em tempo real ($\le 2,5\text{s}$).
3. **🛌 Alocação de Leitos e Acolhimento (Tela 3):** Mapa visual e interativo do estado dos leitos (livre/ocupado) com comunicação multi-sensorial e confirmação de entrada num clique.

---

## 🎨 Acessibilidade e Inclusão (WCAG 2.1 AA)

* **Navegação 100% por Teclado:** Suporte completo via `Tab` com indicador de foco destacado (`3px`).
* **Comunicação Multi-sensorial:** O estado dos leitos e alertas não dependem apenas de cor (verde/vermelho), utilizando rótulos claros, símbolos visuais, atributos `aria-label` e alto contraste ($\ge 4,5:1$).
* **Interface Adaptada:** Botões e áreas de clique dimensionados ($\ge 44\times44\text{px}$) para facilitar a operação sob baixa iluminação e em monitores padrão.

---

## 🛠️ Pilha Tecnológica e Arquitetura

O projeto adota o padrão de arquitetura monolítica **MVC (Model-View-Controller)**:

* **Linguagem:** Python 3.10+
* **Framework Web (Controller):** Flask
* **Interface (View):** HTML5 Semântico, CSS3 Customizado e JavaScript Nativo
* **Banco de Dados (Model):** SQLite / PostgreSQL via ORM SQLAlchemy
* **Algoritmo Antiduplicação:** `RapidFuzz` (distância de Levenshtein e correspondência fonética)
* **Segurança:** Proteção contra SQL Injection (SQLAlchemy), XSS (Jinja2 Autoescape) e credenciais mascaradas

---

## 📁 Estrutura do Repositório

```text
ASCOM-CTA-Acolhe/
├── app.py                # Servidor Flask e rotas da aplicação (Controller e Model)
├── requirements.txt      # Dependências do projeto (Flask, RapidFuzz, SQLAlchemy, pytest)
├── README.md             # Documentação oficial do repositório
├── templates/            # Pasta das views (HTML/CSS/JS)
│   └── index.html        # Interface visual interativa do protótipo
└── tests/                # Testes automatizados
    └── test_antiduplicacao.py # Testes unitários do algoritmo antiduplicação
🔧 Como Executar o Projeto Localmente
Pré-requisitos
Python 3.10 ou superior instalado.

Git configurado.

Passo a Passo
Clonar o repositório:

Bash
git clone [https://github.com/Thiagotrs02/ASCOM-CTA-Acolhe.git](https://github.com/Thiagotrs02/ASCOM-CTA-Acolhe.git)
cd ASCOM-CTA-Acolhe
Criar e ativar o ambiente virtual:

Bash
python -m venv venv
# No Windows (Prompt / PowerShell):
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate
Instalar as dependências:

Bash
pip install -r requirements.txt
Executar a aplicação:

Bash
python app.py
Aceder no navegador:
Abra http://127.0.0.1:5000 no seu browser.

🧪 Testes Automatizados e CI/CD
O projeto conta com rotinas de testes unitários para garantir a precisão do algoritmo de busca por similaridade fonética e a prevenção de cadastros duplicados.

Para executar os testes localmente:

Bash
pytest
A pipeline de Integração Contínua (GitHub Actions) executa automaticamente a verificação de código e os testes a cada Pull Request ou push na branch main.

📜 Licença
Este projeto é desenvolvido para fins exclusivamente académicos e de impacto social no âmbito das disciplinas de Engenharia de Software para o Centro Temporário de Acolhimento da ASCOM São Mateus.
