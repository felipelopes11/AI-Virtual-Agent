import pandas as pd
from typing import List, Dict

# Define o caminho para o nosso arquivo CSV.
# O caminho é relativo à raiz do projeto backend.
DATA_PATH = "data/cafes_especiais.csv"

def load_product_data() -> pd.DataFrame:
    """
    Carrega os dados dos produtos do arquivo CSV para um DataFrame do pandas.
    """
    try:
        df = pd.read_csv(DATA_PATH)
        print("Dados dos produtos carregados com sucesso.")
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo de dados não foi encontrado em '{DATA_PATH}'")
        return pd.DataFrame() # Retorna um DataFrame vazio em caso de erro

def format_products_for_rag(products_df: pd.DataFrame) -> List[Dict[str, str]]:
    """
    Formata o DataFrame de produtos para um formato amigável para o RAG.
    Cada produto se torna um documento de texto com seus atributos.
    """
    if products_df.empty:
        return []
    
    documents = []
    for _, row in products_df.iterrows():
        # Cria um texto descritivo para cada café
        doc_content = (
            f"Nome do Café: {row['nome']}\n"
            f"Origem: {row['origem']}\n"
            f"Notas Sensoriais: {row['notas_sensoriais']}\n"
            f"Nível de Acidez: {row['acidez']}\n"
            f"Tipo de Corpo: {row['corpo']}\n"
            f"Preço: R${row['preco']:.2f}"
        )
        # Adiciona metadados para referência futura
        doc_metadata = {"source": row['nome'], "id": row['id']}
        documents.append({"page_content": doc_content, "metadata": doc_metadata})
        
    print(f"{len(documents)} documentos de produtos formatados para o RAG.")
    return documents

# Exemplo de como usar (não é necessário para a API, apenas para teste)
if __name__ == '__main__':
    df = load_product_data()
    if not df.empty:
        formatted_docs = format_products_for_rag(df)
        print("\nExemplo de documento formatado:")
        print(formatted_docs[0])