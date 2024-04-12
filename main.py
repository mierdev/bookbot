def main():
  book_title = "Frankenstein"
  book_file = "books/frankenstein.txt"
  words = get_book_text(book_file)
  amount_of_words = count_words(words)
  amount_of_letters = count_letters(words)

  print(f"{book_title} has {amount_of_words} words!")
  print(amount_of_letters)

def get_book_text(book):
  with open(book) as text:
    return text.read()

def count_words(book):
  words = book.split()
  return len(words)

def count_letters(words):
  letters_dictionary = {}
  for word in words:
    lowercase = word.lower().split()
    
    # AARRRGGGHHH

  return letters_dictionary



main()