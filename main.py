# Book Bot is a Python program that analyzes the entire book and
# it prints out the number of occurrence of each alphabet letter

def main():
    # Finds the number of words in the book
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = num_of_words(text)

    # Prints a report of the book
    print(f"\n--- Begin report of {book_path} ---")

    print(f"{num_words} words found in the document\n")
    char_count = count_char(text)
    print_report(char_count)

    print("--- End of report ---\n")


# Opens and reads the words in the book
def get_book_text(path):
    with open(path) as f:
        return f.read()


# Splits the words and counts the number of characters
def num_of_words(text):
    words = text.split()
    return len(words)


def count_char(text):
    result = {}
    text_lower = text.lower()
    words = text_lower.split()

    # Counts the number of occurances of each character
    for each_word in words:
        for each_char in each_word:
          if each_char not in result:
              result[each_char] = 1
          else:
              result[each_char] += 1
    return result


def print_report(char_count):

  list_of_dicts = []
  char_map = {}

  # Appends the number of occurances of each character to list_of_dicts
  # simultaneously mapping the number of occurances as the key and the each alphabet letter as the value
  # in the char_map dictionary
  for key, value in char_count.items():
    list_of_dicts.append(value)
    list_of_dicts.sort(reverse=True)
    char_map[value] = key

  # Prints only the letters of the alphabet and its occurance in the report
  for each in list_of_dicts:
     if char_map[each].isalpha():
        print(f"The '{char_map[each]}' character was found {each} time")

main()