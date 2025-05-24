# count all the words in a document
def word_count(doc_words: list) -> int:
    count_words: int = len(doc_words)
    return count_words


# TODO: REFACTOR
# count all the characters in a document
def character_count(words: list) -> dict:
    character_count: dict = {}
    for word in words:
        word: str = word.lower()
        for letter in word:
            if letter not in character_count:
                character_count[letter] = 1
            else:
                character_count[letter] += 1
    return character_count


# TODO: UNDERSTAND WHAT THIS DOES
# sort all character counts alphabetically
def sorted_character_count_list(character_count: dict) -> list:
    sorted_list: list = sorted(
        character_count.items(), key=lambda x: x[1], reverse=True
    )
    return sorted_list
