from stats import get_num_words
from stats import get_num_char
from stats import sort_func
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    args = sys.argv
    try:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {args[1]}")
        print("----------- Word Count ----------")
        num_words = get_num_words(get_book_text(args[1]))
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        sorted_chars = sort_func(get_book_text(args[1]))
        for entry in sorted_chars:
            print(f"{entry['letter']}: {entry['num']}")
        print("============= END ===============")
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()