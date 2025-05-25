# count all the words in a document
def word_count(doc_words: list) -> int:
    count_words: int = len(doc_words)
    return count_words


# count all tge characters in a document
def character_count(doc_text: str) -> dict:
    count_characters: dict[str, str] = {}
    for character in doc_text.lower():
        count_characters[character] = count_characters.get(character, 0) + 1
    return count_characters


# TODO: UNDERSTAND WHAT THIS DOES
# sort all character counts alphabetically
def sorted_character_count_list(character_count: dict) -> list[str]:
    sorted_list: list = sorted(
        character_count.items(), key=lambda x: x[1], reverse=True
    )
    return sorted_list
