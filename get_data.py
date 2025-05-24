def get_doc_text(file_path: str) -> str:
    with open(file_path) as doc:
        doc_contents = doc.read()
    return doc_contents


def get_words(doc_text: str) -> list:
    return doc_text.split()
