from stats import get_num_words, get_num_chars
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print(f"Found {get_num_words(book_text)} total words")
    print(get_num_chars(book_text))
main()