from stats import get_num_words

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(frankenstein)
    print(f"{num_words} words found in the documents")

main()