def main():
  book_title = "Frankenstein"
  book_file = "books/frankenstein.txt"
  book_words = get_book_text(book_file)
  amount_of_words = count_words(book_words)
  amount_of_letters = count_letters(book_words)

  report(book_file, book_title, amount_of_words, amount_of_letters)

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

def report(book_path, book_title, words_count, characters_count):
  print(f"--- Begin report of {book_path} ---")
  
  print("\n\n")

  print(f"Book title: {book_title}")
  print(f"Amount of words in this book: {words_count}")
  
  print("\n\n")

  
  for each in characters_count:
    print(f"The '{each}' character was found {characters_count[each]} times")

  print("\n\n")

  print("--- End report ---")



main()