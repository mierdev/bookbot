import sys


# check if user added a path to document
def check_user_input():
    if len(sys.argv) < 2:
        print("Please define a path to the document you want to analyze.")
        print("")
        print("Usage:")
        print("python3 main.py <path_to_book>")
        print("")
        sys.exit(1)


# get all the text in a document
def get_doc_text(file_path: str) -> str:
    with open(file_path) as doc:
        doc_contents = doc.read()
    return doc_contents


# get a list of all the words in a document
def get_words(doc_text: str) -> list:
    return doc_text.split()
