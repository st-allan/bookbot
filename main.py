import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
from stats import counter_words, character_counter, sorted_list_of_dictionaries

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    message = get_book_text(sys.argv[1])
    num_words = counter_words(message)
    print(f"{num_words} words found in the document")
    number_characters = character_counter(message)
    print(number_characters)
    print(f'''
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------")
          ''')
    sorted_list = sorted_list_of_dictionaries(number_characters)
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()


