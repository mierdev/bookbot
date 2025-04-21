def word_count(book_words: list) -> int:
    count_words: int = len(book_words)
    return count_words


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


def sorted_character_count_list(character_count: dict) -> list:
    sorted_list: list = sorted(
        character_count.items(), key=lambda x: x[1], reverse=True
    )
    return sorted_list
