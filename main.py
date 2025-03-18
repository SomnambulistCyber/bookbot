def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def split_words(file_contents):
    words = file_contents.split()
    return words

def main():
    path = "books/frankenstein.txt"
    all_words = split_words(get_book_text(path))
    num_words = len(all_words)
    print(f"{num_words} words found in the document")

main()