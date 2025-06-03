import warnings
import os
warnings.filterwarnings("ignore")
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain import hub
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import gradio as gr
# Setting langchain key
os.environ['LANGCHAIN_API_KEY'] = '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'

# Loading PDFs from data folder
loader = DirectoryLoader("data", glob='*.pdf', loader_cls=PyPDFLoader)
# Initialising document loader
documents = loader.load()

# Reading docs as chunks of size 1000
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
all_splits = text_splitter.split_documents(documents)

# defining vector store for saving docs in embedded format.
vectorstore = Chroma.from_documents(
    documents=all_splits,
    embedding=OllamaEmbeddings(model="mxbai-embed-large", show_progress=True),
    persist_directory="./chroma_db",
)
# Initialising LLM model for generator purpose
llm = Ollama(model="llama3.1")
retriever = vectorstore.as_retriever()


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def response(message, history):
    # getting prompt template from langchain hub
    rag_prompt = hub.pull("rlm/rag-prompt")
    # Initialising langchain QA chain with Retriever
    qa_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | rag_prompt
            | llm
            | StrOutputParser()
    )
    result = qa_chain.invoke(message)
    return result


if __name__ == "__main__":
    # Starting gradio UI interface
    gr.ChatInterface(response, title="CBAM Chatbot",
                     description="Ask me your questions related to CBAM",
                     theme="soft").launch(share=True)
