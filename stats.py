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

def helper_func(dict_list):
    return dict_list["num"]

def to_listed_dicts(char_dict):
    dict_list = []
    for k in char_dict:
        dict_list.append({"char": k, "num": char_dict[k]})
    dict_list.sort(key = helper_func, reverse = True)
    return dict_list