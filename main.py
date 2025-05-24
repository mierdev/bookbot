import sys
from get_data import get_doc_text, get_words
from stats import word_count, character_count, sorted_character_count_list
from report import print_report


def main():
    # check if user added path to document
    if len(sys.argv) < 2:
        print("Please define a path to the document you want to analyze.")
        print("")
        print("Usage:")
        print("python3 main.py <path_to_book>")
        print("")
        sys.exit(1)

    # get document path
    path_to_doc: str = sys.argv[1]

    # get document text & words
    doc_text: str = get_doc_text(f"{path_to_doc}")
    doc_words: list = get_words(doc_text)

    # get stats
    doc_word_count: int = word_count(doc_words)
    doc_character_count: dict = character_count(doc_words)
    sorted_doc_character_count: list = sorted_character_count_list(doc_character_count)

    # print report
    print_report(path_to_doc, doc_word_count, sorted_doc_character_count)


main()
