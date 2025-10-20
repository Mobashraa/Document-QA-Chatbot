
# !pip install langchain langchain-community faiss-cpu openai tiktoken

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# --- STEP 1: Load the document ---
loader = PyPDFLoader("your_file.pdf")  # Replace with your actual file
documents = loader.load()

# --- STEP 2: Create embeddings ---
embeddings = OpenAIEmbeddings(openai_api_key="YOUR_OPENAI_API_KEY")

# --- STEP 3: Store embeddings in FAISS vectorstore ---
vectorstore = FAISS.from_documents(documents, embeddings)

# --- STEP 4: Create a retriever ---
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# --- STEP 5: Initialize the OpenAI LLM ---
llm = ChatOpenAI(
    openai_api_key="YOUR_OPENAI_API_KEY",
    model="gpt-4o-mini",  # You can use 'gpt-4o' or 'gpt-3.5-turbo'
    temperature=0
)

# --- STEP 6: Define the prompt ---
prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant that answers questions based on the provided context.
Be accurate and concise.

Context:
{context}

Question:
{input}

Answer:
""")

# --- STEP 7: Create the chain ---
document_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# --- STEP 8: Ask a question ---
query = "Summarize the key points discussed in this document."
response = retrieval_chain.invoke({"input": query})

print("Answer:", response["answer"])
