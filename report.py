def print_report(path: str, word_count: int, character_count: list):
    print("============ BOOKBOT ============")
    print(f"Analyzing document found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # TODO: REFACTER, THIS LOGIC SHOULD BE IN STATS (character count)
    for each in character_count:
        if each[0].isalpha():
            print(f"{each[0]}: {each[1]}")
    print("============= END ===============")
