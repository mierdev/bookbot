import sys
from get_and_check_data import check_user_input, get_doc_text
from stats import (
    strip_words,
    character_count,
    word_count_all,
    word_count_individual,
    top_ten_words,
    sort_dictionary,
)
from report import print_report


def main() -> None:
    # check if user added a valid path to the document
    check_user_input()

    # set variables
    path_to_doc: str = sys.argv[1]
    doc_text: str = get_doc_text(f"{path_to_doc}")
    doc_words: list = doc_text.split()
    doc_words_stripped: list = strip_words(doc_words)

    # get stats
    doc_word_count_all: int = word_count_all(doc_words_stripped)
    doc_word_count_individual: dict[str, str] = word_count_individual(
        doc_words_stripped
    )
    doc_word_count_sorted: list[tuple] = sort_dictionary(doc_word_count_individual)
    top_ten: list[tuple] = top_ten_words(doc_word_count_sorted)
    doc_character_count: dict[str, str] = character_count(doc_text)
    doc_character_count_sorted: list = sort_dictionary(doc_character_count)

    # print report
    print_report(
        path_to_doc,
        doc_word_count_all,
        top_ten,
        doc_character_count_sorted,
    )


# run main.py
if __name__ == "__main__":
    main()
