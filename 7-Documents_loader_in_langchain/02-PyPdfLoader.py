from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('7-Documents_loader_in_langchain\document.pdf')

docs=loader.load()

print(len(docs))

print(docs[0].page_content) # print the page content of first page of docs

print(docs[1].metadata)