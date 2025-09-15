<img width="456" height="702" alt="img-chat" src="https://github.com/user-attachments/assets/883d2461-4610-41ec-aa27-30288a1343a4" />

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
