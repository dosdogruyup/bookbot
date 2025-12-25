def get_num_words(text):
    return len(text.split())
def get_num_chars(text):
    text = text.lower()
    char_dict = {}
    for c in text:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict