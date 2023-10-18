# =========================
#  Module: Vector DB Build
# =========================
import json
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings

def load_env_from_file(file_path):

  with open(file_path, 'r') as f:
    env = json.load(f)

  return env
cfg = load_env_from_file('config/config.json')

# Build vector database
def run_db_build():
    loader = DirectoryLoader(cfg['DATA_PATH'],
                             glob='*.pdf',
                             loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=cfg['CHUNK_SIZE'],
                                                   chunk_overlap=cfg['CHUNK_OVERLAP'])
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs={'device': 'cpu'})

    vectorstore = FAISS.from_documents(texts, embeddings)
    vectorstore.save_local(cfg['DB_FAISS_PATH'])

if __name__ == "__main__":
    run_db_build()
