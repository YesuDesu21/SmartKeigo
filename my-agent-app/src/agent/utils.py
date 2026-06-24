import cohere
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

co = cohere.ClientV2(os.getenv("COHERE_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

def initialize_pinecone_index():
    ## Create an index for dense vectors with integrated embedding
    index_name = "keigo-templates"
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=1024,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

    sample_text = "お世話になっております。〇〇会社の佐藤です。件記の件について..."
    response = co.embed(texts=[sample_text], model="embed-multilingual-v3.0", input_type="search_document")
    # Debug: print response structure
    print(f"Response type: {type(response)}")
    print(f"Response embeddings type: {type(response.embeddings)}")
    print(f"Response embeddings dir: {dir(response.embeddings)}")
    vector_array = response.embeddings.float[0]
    

    index = pc.Index(index_name)
    index.upsert(vectors=[{"id": "tmpl_1", "values": vector_array, "metadata": {"text": sample_text}}])
    print("Database initialized successfully!")

def RAG_retrieve(query: str, top_k: int = 3):
    """Retrieve similar Keigo templates from Pinecone using Cohere embeddings.
    
    Args:
        query: The user's input text to find similar templates for
        top_k: Number of similar templates to retrieve
        
    Returns:
        String containing the retrieved template texts as context
    """
    # Embed the query using Cohere
    query_response = co.embed(
        texts=[query], 
        model="embed-multilingual-v3.0", 
        input_type="search_query"
    )
    query_vector = query_response.embeddings.float_[0]
    
    # Query Pinecone index
    index = pc.Index("keigo-templates")
    search_results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )
    
    # Extract template texts from results
    templates = []
    for match in search_results["matches"]:
        if "metadata" in match and "text" in match["metadata"]:
            templates.append(match["metadata"]["text"])
    
    # Return as formatted context string
    if templates:
        context = "\n\n".join([f"参考テンプレート {i+1}: {tmpl}" for i, tmpl in enumerate(templates)])
        return context
    else:
        return "該当するテンプレートが見つかりませんでした。"
