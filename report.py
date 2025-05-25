def print_report(path: str, word_count: int, character_count: list):
    print("============ BOOKBOT ============")
    print(f"Analyzing document found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in character_count:
        print(f"{character[0]}: {character[1]}")
    print("============= END ===============")
