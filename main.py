import sys
from stats import get_num_words, get_char_counts, get_sorted_char_counts

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: pyhton3 main.py ‹path_to_book›")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    book = get_book_text(book_path)

    num_words = get_num_words(book)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_counts = get_char_counts(book)
    sorted_char_counts = get_sorted_char_counts(char_counts)
    for line in sorted_char_counts:
        print(f"{line["character"]}: {line["count"]}")
    print("============= END ===============")

main()
