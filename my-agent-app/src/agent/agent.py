from langchain_groq import ChatGroq
from .state import KeigoState
from .utils import RAG_retrieve
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

llm = ChatGroq(
    model="llama-3.3-70b-versatile", 
    temperature=0.3,  # Low temperature for consistent business translation/validation
    api_key=os.getenv("GROQ_API_KEY")
)
# Node 1: The Analyzer Agent
def language_analyzer(state: KeigoState):
    user_text = state["raw_input"]
    prompt = f"分析してください。この文章の受信者は誰ですか？客、上司、それとも同僚？文章：{user_text}"
    response = llm.invoke(prompt)
    return {"audience": response.content} # Updates 'audience' key

# Node 2: The Keigo Specialist Agent
def keigo_specialist(state: KeigoState):
    user_text = state["raw_input"]
    target_audience = state["audience"]
    
    # Retrieve similar templates using RAG
    rag_context = RAG_retrieve(user_text)
    
    prompt = f"""相手は{target_audience}です。以下の参考テンプレートを参考にして、この日本語を完璧な敬語に翻訳してください：

{rag_context}

ユーザー入力：{user_text}"""
    
    response = llm.invoke(prompt)
    return {"draft_keigo": response.content} # Updates 'draft_keigo' key

# Node 3: The Cultural Coach Agent
def cultural_coach(state: KeigoState):
    draft = state["draft_keigo"]
    prompt = f"このビジネスメールの表現に不自然な点やマナー違反はありますか？合格なら「OK」、不合格なら修正点を書いてください。修正対象：{draft}"
    response = llm.invoke(prompt)
    
    if "OK" in response.content:
        return {"is_approved": True, "feedback": "問題なし"}
    else:
        return {"is_approved": False, "feedback": response.content}
