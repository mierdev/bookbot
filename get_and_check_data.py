import sys
import os


# check if user added a valid path to document
def check_user_input():
    # check if user added a path
    if len(sys.argv) < 2:
        print("Please define a path to the document you want to analyze.\n")
        print("Usage:")
        print("python3 main.py <path_to_book>\n")
        sys.exit(1)
    # check if the document exists
    if os.path.exists(sys.argv[1]):
        pass
    else:
        print("\nOh nooo! 😭\nThis document does not exist...\n")
        sys.exit(1)


# get all the text from a document
def get_doc_text(file_path: str) -> str:
    with open(file_path) as doc:
        doc_contents = doc.read()
    return doc_contents
