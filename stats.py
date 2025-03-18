char_count = {}

def get_num_words(file_contents):
    all_words = file_contents.split()
    num_words = len(all_words)
    return num_words

def get_num_char(file_contents):
    all_lower = str.lower(file_contents)
    all_char = list(all_lower)
    for letter in list(map(chr,range(ord('a'),ord('z')+1))):
        char_count[letter] = all_char.count(letter)
    return char_count