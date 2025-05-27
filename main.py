import sys
from get_and_check_data import check_user_input, get_doc_text
from stats import word_count, character_count, sort_dictionary
from report import print_report


def main():
    # check if user added a valid path to the document
    check_user_input()

    # set variables
    path_to_doc: str = sys.argv[1]
    doc_text: str = get_doc_text(f"{path_to_doc}")
    doc_words: list = doc_text.split()

    # get stats
    doc_word_count: int = word_count(doc_words)
    doc_character_count: dict = character_count(doc_text)
    doc_character_count_sorted: list = sort_dictionary(doc_character_count)

    # print report
    print_report(path_to_doc, doc_word_count, doc_character_count_sorted)


# run main.py
if __name__ == "__main__":
    main()
