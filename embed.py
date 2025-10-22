import os

from chromadb import ClientAPI, QueryResult
from chromadb.types import Collection
from google.ai.generativelanguage_v1 import GenerateContentResponse

import chunk
import chromadb
# 向量数据库选择的是chromadb
import google.generativeai as genai
# from google import genai    暂时用不了genai

# (in terminal) 配置一次性API KEY
# export GOOGLE_API_KEY=AIzaSyD0g2m8cYC3q3EdlagEovnfYuRe_LcTVew
# echo $GOOGLE_API_KEY 打印检查

# google_client = genai.Client() 旧版失效了
# 配置 API KEY
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# EMBEDDING_MODEL = "gemini-embedding-exp-03-07" 实验版有效期将近
EMBEDDING_MODEL = "models/embedding-001"
LLM_MODEL = "gemini-2.5-flash-preview-05-20"

chromadb_client: ClientAPI = chromadb.PersistentClient("./chroma.db")
chromadb_collection: Collection = chromadb_client.get_or_create_collection("database")

# Google 将embedding模型分成了两个类别, 一个用来存储, 一个用来查询, 方便区分文本和用户query
# 给一个参数用来区分存和查
# 具体值可以参考Gemini官方文档

def embed(text: str, store: bool) -> list[float]:
    # noinspection PyArgumentList
    result = genai.embed_content(
        model=EMBEDDING_MODEL,
        content=text,
        task_type = "RETRIEVAL_DOCUMENT" if store else "RETRIEVAL_QUERY"
    )

    # assert 表示自动检查结果是否符合预期
    # 这里写了0, 但是实际开发中需要进行更加稳妥的错误处理
    embedding = result.get("embedding")
    assert embedding, "Embedding 返回为空, 请检查输入或者API KEY"
    return embedding

def create_db() -> None:
    for idx, c in enumerate(chunk.get_chunks()):
        print(f"Process: {c}")
        embedding: list[float] = embed(c, store=True)
        chromadb_collection.upsert(
            ids=str(idx),
            documents=c,
            embeddings=embedding
        )

def query_db(question: str) -> list[str]:
    question_embdding: list[float] = embed(question, store=False)
    result: QueryResult = chromadb_collection.query(
        query_embeddings=question_embdding,
        n_results=5
    )
    assert result["documents"]
    return result["documents"][0]

if __name__ == '__main__':
    # chunks: list[str] = chunk.get_chunks()
    # print(embed(chunks[0], True))
    question = " "
    # create_db()
    chunks: list[str] = query_db(question)
    # for c in chunks:
        # print(c)
        # print("----------------")

    # 将query和RAG得到的精炼文本, 发送给LLM进行思考
    prompt = "Please answer user's question according to context\n"
    prompt += f"Question: {question}\n"
    prompt += "Context: \n"
    for c in chunks:
        prompt += f"{c}\n"
        prompt += "--------------------\n"

    result: GenerateContentResponse = genai.models.generate_content(
        model=LLM_MODEL,
        contents=prompt
    )
    print(result)
