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














# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     chars_dict = get_chars_dict(text)
#     chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

#     print(f"--- Begin report of {book_path} ---")
#     print(f"{num_words} words found in the document")
#     print()

#     for item in chars_sorted_list:
#         if not item["char"].isalpha():
#             continue
#         print(f"The '{item['char']}' character was found {item['num']} times")

#     print("--- End report ---")


# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def sort_on(d):
#     return d["num"]


# def chars_dict_to_sorted_list(num_chars_dict):
#     sorted_list = []
#     for ch in num_chars_dict:
#         sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
#     sorted_list.sort(reverse=True, key=sort_on)
#     return sorted_list


# def get_chars_dict(text):
#     chars = {}
#     for c in text:
#         lowered = c.lower()
#         if lowered in chars:
#             chars[lowered] += 1
#         else:
#             chars[lowered] = 1
#     return chars


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()


# main()