from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path='7-Documents_loader_in_langchain\PDF', # relative path
    glob='*.pdf',   #pattern to match files.
    loader_cls=PyPDFLoader
)

# docs=loader.load()    # slower -reads all matched files,Good if the corpus is small
docs=loader.lazy_load() # faster -Lower memory use, lower startup latency. Lazy allows streaming pipelines

for document in docs:
    print(document.metadata)