from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import CohereEmbeddings
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai=os.getenv("openai_apikey")
my_key_google=os.getenv("google_apikey")
my_key_cohere=os.getenv("cohere_apikey")
my_key_hf=os.getenv("hf_apikey")

llm_gemini=ChatGoogleGenerativeAI(google_api_key=my_key_google,model="gemini-pro")

# OpenAI Embeddings
embeddings=OpenAIEmbeddings(api_key=my_key_openai)

# COHERE Embeddings
# embeddings=CohereEmbeddings(cohere_api_key=my_key_cohere,model="embed-english-v3.0")  # For language support other than English; model="embed-multilingual-v3.0"

# HUGGINGFACE Embeddings
# embeddings=HuggingFaceInferenceAPIEmbeddings(api_key=my_key_hf,model_name="sentence-transformers/all-MiniLM-L6-v2")


def ask_gemini(prompt):
    AI_Response=llm_gemini.invoke(prompt)

    return AI_Response.content


def rag_with_video_transcript(transcript_docs,prompt):

    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0,
        length_function=len
    )

    splitted_documents=text_splitter.split_documents(transcript_docs)

    vectorstore = FAISS.from_documents(splitted_documents, embeddings)
    retriever = vectorstore.as_retriever()

    relevant_documents = retriever.get_relevant_documents(prompt)

    context_data = ""

    for document in relevant_documents:
        context_data = context_data + " " + document.page_content

    final_prompt = f"""I have a question like this: {prompt} 
    To answer this question, we have this information: {context_data}.
    To answer this question, use the information I have given you here. Never go beyond these
    """
    AI_Response = ask_gemini(final_prompt)

    return AI_Response, relevant_documents





