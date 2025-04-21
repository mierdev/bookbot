import sys
from stats import word_count
from stats import character_count
from stats import sorted_character_count_list


def main():
    # check if user added path to book
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
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


def print_report(
    path_to_book: str,
    book_word_count: int,
    sorted_book_character_count: list,
):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for each in sorted_book_character_count:
        if each[0].isalpha():
            print(f"{each[0]}: {each[1]}")
    print("============= END ===============")


main()
