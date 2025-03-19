char_count = {}
char_list = []

def get_num_words(file_contents):
    all_words = file_contents.split()
    num_words = len(all_words)
    return num_words

def sort_on(dict):
    return dict["num"]

def get_num_char(file_contents):
    all_lower = str.lower(file_contents)
    all_char = list(all_lower)
    for letter in list(map(chr,range(ord('a'),ord('z')+1))):
        char_count[letter] = all_char.count(letter)
    return char_count

def sort_func(file_contents):
    all_lower = str.lower(file_contents)
    all_char = list(all_lower)
    for letter in list(map(chr,range(ord('a'),ord('z')+1))):
        letter_dict = {
            "letter": letter,
            "num": all_char.count(letter)
        }
        if letter.isalpha():
            char_list.append(letter_dict)
            char_list.sort(reverse=True, key=sort_on)
    return char_list

