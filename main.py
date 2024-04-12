def main():
  book_title = "Frankenstein"
  book_file = "books/frankenstein.txt"
  words = get_book_text(book_file)
  count = word_count(words)
  print(f"{book_title} has {count} words!")

def get_book_text(book):
  with open(book) as text:
    return text.read()

def word_count(book):
  words = book.split()
  return len(words)



main()