# Importe a StreamingResponse
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

# Importe AMBAS as funções do nosso agente
from app.core.agent import get_agent_response, get_agent_streaming_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

# Mantemos o endpoint antigo para referência, se necessário
@router.post("/chat")
def handle_chat_message(request: ChatRequest):
    print(f"Recebida mensagem do usuário (endpoint não-streaming): {request.message}")
    response = get_agent_response(request.message)
    return {"reply": response}

# NOVO ENDPOINT PARA STREAMING
@router.post("/chat/stream")
async def handle_chat_streaming_message(request: ChatRequest):
    """
    Recebe uma mensagem e retorna a resposta da IA em streaming, pedaço por pedaço.
    """
    print(f"Recebida mensagem do usuário (endpoint streaming): {request.message}")
    # A função retorna um "gerador", que a StreamingResponse consome
    return StreamingResponse(get_agent_streaming_response(request.message), media_type="text/event-stream")