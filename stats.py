# count all the words in a document
def word_count(doc_words: list[str]) -> int:
    count_words: int = len(doc_words)
    return count_words


# count all the characters in a document
def character_count(doc_text: str) -> dict:
    count_characters: dict[str, str] = {}
    for character in doc_text.lower():
        if character.isalpha():
            count_characters[character] = count_characters.get(character, 0) + 1
    return count_characters


# sort dictionary (descending)
def sort_dictionary(unsorted_dictionary: dict) -> list[str]:
    copy_unsorted_dictionary: dict[str, str] = unsorted_dictionary.copy()
    # .items() gets all the items in a dictionary in the form (key, value) so you can then do [1] to sort by the values as opposed to the keys
    return sorted(
        copy_unsorted_dictionary.items(), key=lambda sort: sort[1], reverse=True
    )
