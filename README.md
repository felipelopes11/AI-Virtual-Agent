☕ Barista Virtual - Agente de Atendimento com IA
📝 Descrição
O Barista Virtual é uma aplicação full-stack que simula um assistente de IA especialista para um e-commerce de cafés especiais. O agente é capaz de responder a perguntas detalhadas sobre os produtos, baseando as suas respostas exclusivamente num catálogo de produtos fornecido, evitando "alucinações" e garantindo precisão.

Este projeto foi construído para demonstrar a aplicação prática de Modelos de Linguagem Grandes (LLMs) numa solução de negócio, com foco em IA local, privacidade de dados e uma arquitetura moderna.

✨ Funcionalidades Principais
Chat em Tempo Real: Interface de chat reativa construída com React.

IA Especialista (RAG): Utiliza a técnica de Retrieval-Augmented Generation para fornecer respostas baseadas num catálogo de produtos específico.

Respostas em Streaming: A resposta da IA é exibida palavra por palavra, melhorando a experiência do utilizador.

IA Local e Privada: Executa o modelo de linguagem Llama 3 localmente com o Ollama, garantindo que nenhum dado sensível é enviado para APIs externas.

API Robusta: Backend construído com FastAPI, garantindo alto desempenho e documentação automática.

🚀 Tecnologias Utilizadas
Backend
Linguagem: Python

Framework API: FastAPI

Servidor: Uvicorn

Frontend
Biblioteca: React

Ferramenta de Construção: Vite

Comunicação API: Axios

Inteligência Artificial
Modelo (LLM): Llama 3 (via Ollama)

Orquestração: LangChain

Base de Dados Vetorial: ChromaDB

Técnica: RAG (Retrieval-Augmented Generation)

🛠️ Como Executar o Projeto Localmente
Pré-requisitos:

Python 3.10+

Node.js e npm

Ollama instalado e a correr

1. Clonar o Repositório

git clone [https://github.com/felipelopes11/Agente-Virtual-IA.git](https://github.com/felipelopes11/Agente-Virtual-IA.git)
cd Agente-Virtual-IA

2. Configurar o Backend

# Navegar para a pasta do backend
cd backend

# Criar e ativar o ambiente virtual
python -m venv venv
# No Windows:
.\\venv\\Scripts\\activate
# No macOS/Linux:
# source venv/bin/activate

# Instalar as dependências
pip install -r requirements.txt

# Descarregar o modelo de IA (se ainda não o tiver)
ollama pull llama3:8b

# Iniciar o servidor
python -m uvicorn app.main:app --reload

O backend estará a ser executado em http://localhost:8000.

3. Configurar o Frontend

# Num novo terminal, navegar para a pasta do frontend
cd frontend

# Instalar as dependências
npm install

# Iniciar o servidor de desenvolvimento
npm run dev

A aplicação estará acessível em http://localhost:5173.
