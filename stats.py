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


# TODO: UNDERSTAND THIS
# sort all character counts from high to low
def character_count_sorted(character_count: dict) -> list[str]:
    original_list: list[tuple] = character_count.copy()
    sorted_list: list[tuple] = sorted(
        original_list.items(), key=lambda x: x[1], reverse=True
    )
    return sorted_list
