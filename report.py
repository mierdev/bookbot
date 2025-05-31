def print_report(
    path: str, word_count: int, top_ten_words: list, character_count: list
):
    print("============ BOOKBOT ============")
    print(f"Analyzing document found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("---- Top 10 Most Used Words! ----")
    count = 1
    for word in top_ten_words:
        print(f"Nummer {count}: {word[0]} ({word[1]}x)")
        count += 1
    print("-------- Character Count --------")
    for character in character_count:
        print(f"{character[0]}: {character[1]}")
    print("============= END ===============")
