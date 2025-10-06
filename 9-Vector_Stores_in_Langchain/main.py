from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document

load_dotenv()

llm = ChatGroq(
    model='openai/gpt-oss-20b'
)

doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
    metadata={"team": "Royal Challengers Bangalore"}
)
doc2 = Document(
    page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
    metadata={"team": "Mumbai Indians"}
)
doc3 = Document(
    page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
    metadata={"team": "Chennai Super Kings"}
)
doc4 = Document(
    page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
    metadata={"team": "Mumbai Indians"}
)
doc5 = Document(
    page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
    metadata={"team": "Chennai Super Kings"}
)

docs = [doc1, doc2, doc3, doc4, doc5]

# Initialize embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create FAISS vector store
vector_store = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)

# Save vector store
vector_store.save_local("my_faiss_db")
print("Vector store created and saved!")

# View documents
print(f"\nTotal documents: {vector_store.index.ntotal}")
for doc_id, doc in vector_store.docstore._dict.items():
    print(f"\nID: {doc_id}")
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")

# Search documents
results = vector_store.similarity_search(
    query='Who among these are a bowler?',
    k=2
)
print("\n--- Search Results ---")
for doc in results:
    print(f"\n{doc.page_content}")

# Search with similarity score
results_with_scores = vector_store.similarity_search_with_score(
    query='Who among these are a bowler?',
    k=2
)
print("\n--- Search Results with Scores ---")
for doc, score in results_with_scores:
    print(f"\nScore: {score}")
    print(f"{doc.page_content}")

# Metadata filtering
all_docs = vector_store.similarity_search("", k=10)
filtered_docs = [doc for doc in all_docs if doc.metadata.get("team") == "Chennai Super Kings"]
print("\n--- Chennai Super Kings Players ---")
for doc in filtered_docs:
    print(f"\n{doc.page_content}")

# Add/Update documents
updated_doc1 = Document(
    page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
    metadata={"team": "Royal Challengers Bangalore"}
)
vector_store.add_documents([updated_doc1])
vector_store.save_local("my_faiss_db")
print("\n--- Document Updated ---")

# View documents after update
print(f"\nTotal documents after update: {vector_store.index.ntotal}")

# Delete document
doc_ids = list(vector_store.docstore._dict.keys())
if doc_ids:
    vector_store.delete([doc_ids[0]])
    vector_store.save_local("my_faiss_db")
    print(f"\nDeleted document: {doc_ids[0]}")

# View documents after deletion
print(f"\nTotal documents after deletion: {vector_store.index.ntotal}")
for doc_id, doc in vector_store.docstore._dict.items():
    print(f"\nID: {doc_id}")
    print(f"Content: {doc.page_content[:100]}...")

# Load saved vector store (for future use)
# loaded_vector_store = FAISS.load_local("my_faiss_db", embedding_model, allow_dangerous_deserialization=True)