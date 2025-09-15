from langchain_ollama.llms import OllamaLLM
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from app.services.product_service import load_product_data, format_products_for_rag

# Esta função agora cria e retorna os componentes que vamos usar
def setup_agent_components():
    print("Inicializando os componentes do agente de IA...")
    products_df = load_product_data()
    if products_df.empty:
        raise ValueError("O DataFrame de produtos está vazio.")
    
    product_documents_formatted = format_products_for_rag(products_df)
    texts = [doc["page_content"] for doc in product_documents_formatted]
    metadatas = [doc["metadata"] for doc in product_documents_formatted]

    embeddings = OllamaEmbeddings(model="llama3:8b")
    vectorstore = Chroma.from_texts(texts=texts, embedding=embeddings, metadatas=metadatas)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    template = """
    Você é um assistente de loja. Responda à pergunta do cliente de forma breve e direta, usando apenas as informações do contexto abaixo.
    Não repita palavras. Não invente informações. Formate preços como R$ 35,50.

    Contexto:
    {context}

    Pergunta:
    {question}

    Resposta:
    """
    prompt = PromptTemplate.from_template(template)
    
    llm = OllamaLLM(model="llama3:8b", temperature=0.1)
    
    print("Componentes do agente de IA inicializados!")
    return retriever, prompt, llm

# Inicializamos os componentes uma vez
retriever, prompt, llm = setup_agent_components()

# Criamos a cadeia para a resposta não-streaming (que é mais simples)
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def get_agent_response(question: str) -> str:
    try:
        return rag_chain.invoke(question)
    except Exception as e:
        print(f"Erro ao invocar o agente de IA: {e}")
        return "Desculpe, ocorreu um erro."

# --- LÓGICA DE STREAMING ATUALIZADA E DIRETA ---
def get_agent_streaming_response(question: str):
    """
    Executa os passos do RAG manualmente para ter um controlo total sobre o stream
    e evitar os erros de repetição do LangChain.
    """
    print("\n--- [DEBUG] A iniciar a geração de stream (MÉTODO DIRETO) para a pergunta:", question)
    try:
        # 1. Obter o contexto relevante
        retrieved_docs = retriever.invoke(question)
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])
        
        # 2. Formatar o prompt manualmente
        formatted_prompt = prompt.format(context=context, question=question)
        print(f"--- [DEBUG] Prompt formatado enviado para o LLM:\n{formatted_prompt}")

        # 3. Chamar o stream diretamente no LLM
        for chunk in llm.stream(formatted_prompt):
            print(f"--- [DEBUG] Gerado um pedaço (chunk): '{chunk.replace('\n', '\\n')}'")
            yield chunk
        print("--- [DEBUG] Fim da geração do stream ---\n")

    except Exception as e:
        print(f"--- [DEBUG] ERRO durante o streaming: {e}")
        yield "Desculpe, ocorreu um erro ao processar a sua pergunta."

