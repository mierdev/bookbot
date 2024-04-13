def main():
  book_title = "Frankenstein"
  book_file = "books/frankenstein.txt"
  book_words = get_book_text(book_file)
  amount_of_words = count_words(book_words)
  amount_of_letters = count_letters(book_words)
  list_of_characters = convert_to_list_of_dictionaries(amount_of_letters)

  report(book_file, book_title, amount_of_words, list_of_characters)

def get_book_text(book):
  with open(book) as text:
    return text.read()

def count_words(words):
  loose_words = words.split()
  return len(loose_words)

def count_letters(words):
  character_dictionary = {}
  lowercase = "".join(words.lower())

  for character in lowercase:
    if character.isalpha() == True:
      if character not in character_dictionary:
        character_dictionary.update({character: 1})
      else:
        character_dictionary[character] += 1

  return character_dictionary

def convert_to_list_of_dictionaries(characters_count):
  list_of_characters = []
  for each in characters_count:
    #list_of_characters.append({each: characters_count[each]})
    list_of_characters.append({"character": each, "count": characters_count[each]})
  
  return list_of_characters


def report(book_path, book_title, words_count, characters_count):
  print(f"--- Begin report of {book_path} ---")

  print("\n")

  print(f"Book title: {book_title}")
  print(f"Amount of words in this book: {words_count}")
  
  print("\n")

  for each in characters_count:
   print(f"The '{each["character"]}' character was found {each["count"]} times")

  print("\n")

  print("--- End report ---")



main()