from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path='7-Documents_loader_in_langchain\Social_Network_Ads.csv')

docs=loader.load()

print(len(docs))
print(docs[5])