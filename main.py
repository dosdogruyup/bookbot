import sys
from stats import get_num_words, get_num_chars, to_listed_dicts
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_char_count(dict_list):
    for d in dict_list: 
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")

def main():
    book_loc = ""
    if len(sys.argv) == 2:
        book_loc = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    
    print(f"Analyzing book found at {book_loc}")
    book_text = get_book_text(book_loc)
    
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    
    print("--------- Character Count -------")
    print_char_count(to_listed_dicts(get_num_chars(book_text)))
main()