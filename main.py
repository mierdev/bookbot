import sys
from stats import word_count, character_count, sorted_character_count_list
from report import print_report


def main():
    # check if user added path to book
    if len(sys.argv) < 2:
        print("Please define a path to the document you want to analyze.")
        print("")
        print("Usage:")
        print("python3 main.py <path_to_book>")
        print("")
        sys.exit(1)

    # books paths
    path_to_book: str = sys.argv[1]

    # get book text & words
    book_text: str = get_book_text(f"{path_to_book}")
    book_words: list = get_words(book_text)

    # get stats
    book_word_count: int = word_count(book_words)
    book_character_count: dict = character_count(book_words)
    sorted_book_character_count: list = sorted_character_count_list(
        book_character_count
    )

    # print report
    print_report(path_to_book, book_word_count, sorted_book_character_count)


def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents


def get_words(book_text: str) -> list:
    return book_text.split()

    print_report(path_to_book, book_word_count, sorted_book_character_count)


main()
