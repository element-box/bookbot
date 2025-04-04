import os.path
import sys

from stats import get_word_count
from stats import get_char_count 
from stats import get_stats 

def get_book_text(file_path: os.path) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main(book: os.path):
    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {book}...")
    frank_text = get_book_text(book)
    print("----------- Word Count ----------")
    get_word_count(frank_text)
    print("--------- Character Count -------")
    character_count = get_char_count(frank_text)
    sorted_char_count: list[dict] = get_stats(character_count)
    for char in sorted_char_count:
        if char['letter'].isalpha():
            print(f"{char['letter']}: {char['count']}")

    print("============= END ===============")   

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])