from stats import get_num_words
from stats import get_num_char
from stats import sort_func

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    num_words = get_num_words(get_book_text(path))
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_chars = sort_func(get_book_text(path))
    for entry in sorted_chars:
        print(f"{entry['letter']}: {entry['num']}")
    print("============= END ===============")

main()