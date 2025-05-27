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


# sort all character counts from high to low
def character_count_sorted(character_count: dict) -> list[str]:
    original_dictonary: dict[str, str] = character_count.copy()
    return sorted(original_dictonary.items(), key=lambda sort: sort[1], reverse=True)
