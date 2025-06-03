
# CBAM Chatbot

A CBAM LLM-RAG based Chatbot




## Prerequisites
1. Install Ollama based on your OS from below link
    https://ollama.com/download

2. Open a terminal and run below commands to pull necessary LLMs to your machine.
    - ollama run llama3.1
    - ollama pull mxbai-embed-large

3. Start Ollama Server
    Open a terminal and run below command
    - OLLAMA_HOST=127.0.0.1:11435 ollama serve


## Steps to execute CBAM Bot
1. Checkout cbam bot code from the Github repo 
2. Inside the code repo, download the cbam docs from below link.
    a. Download the CBAM docs from this https://drive.google.com/drive/folders/17m3GOZ7gKGzb11AzVl1nkL6BXQ41xxm4?usp=share_link
    b. Create an empty folder named as "chroma_db"
3. Go to the code repo and run requirements.txt file  present in the repo as below
    - pip install -r requirements.txt
4. Run the below file for accessing the chatbot
    - python cbam_chat.py
5. After the successful run of file at step3, a link will be shown at the terminal as below where you can click on the link to access the chat interface.
    http://127.0.0.1:7860


## Tools & Technologies
    LLM : Llama3.1
    Embedding : mxbai-embed-large
    Framework : LangChain & Ollama
    Programming Language : Python
    Vector Store : ChromaDB
    User Interface : Gradio
## Authors

- [@sajanakadangara](https://github.com/sajanakadangara)


## License

[Carbmee]

