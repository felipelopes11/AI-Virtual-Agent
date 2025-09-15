from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import chat_endpoints

# Cria a instância principal da aplicação FastAPI
app = FastAPI(
    title="Barista Virtual API",
    description="API para o agente de atendimento inteligente de uma loja de cafés especiais.",
    version="1.0.0"
)

# Configuração do CORS para permitir a comunicação com o frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, restrinja para o domínio do seu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint raiz para verificar se a API está no ar
@app.get("/")
def read_root():
    """
    Endpoint raiz que retorna uma mensagem de boas-vindas.
    """
    return {"message": "Olá! Eu sou o Barista Virtual. Bem-vindo à nossa API."}

# Inclui as rotas de chat, organizando o projeto
app.include_router(chat_endpoints.router, prefix="/api", tags=["Chat"])

