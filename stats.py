# strip words from punctuation
def strip_words(doc_words: list[str]) -> list:
    copy_doc_words: list = doc_words.copy()
    stripped_words: list = []
    for word in copy_doc_words:
        word_stripped = word.strip("„“”,.-!:;#$*%<>_+=[]{}()|~`? ")
        if word_stripped.isalpha():
            stripped_words.append(word_stripped)
    return stripped_words


# count all the characters in a document
def character_count(doc_text: str) -> dict:
    count_characters: dict[str, int] = {}
    for character in doc_text.lower():
        if character.isalpha():
            count_characters[character] = count_characters.get(character, 0) + 1
    return count_characters


# count all the words in a document
def word_count_all(doc_words: list[str]) -> int:
    count_words: int = len(doc_words)
    return count_words


# count individual words in a document
def word_count_individual(doc_words: list[str]) -> dict:
    copy_doc_words: list[str] = doc_words
    count_individual_words: dict[str, int] = {}
    for word in copy_doc_words:
        lowercase = word.lower()
        count_individual_words[lowercase] = count_individual_words.get(lowercase, 0) + 1
    return count_individual_words


# top 10 words
def top_ten_words(words_sorted: list[tuple]) -> list[tuple]:
    copy_words_sorted: list[tuple] = words_sorted.copy()
    top_ten: list[tuple] = []
    for word in copy_words_sorted:
        if len(top_ten) < 10:
            top_ten.append(tuple(word))
    return top_ten


# sort dictionary (descending)
def sort_dictionary(unsorted_dictionary: dict) -> list[tuple]:
    copy_unsorted_dictionary: dict[str, str] = unsorted_dictionary.copy()
    # .items() gets all the items in a dictionary in the form (key, value) so you can then do [1] to sort by the values as opposed to the keys
    return sorted(
        copy_unsorted_dictionary.items(), key=lambda sort: sort[1], reverse=True
    )
