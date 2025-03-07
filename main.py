from stats import get_num_words, get_char_counts, get_sorted_char_counts

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    book = "books/frankenstein.txt"
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    frankenstein = get_book_text(book)

    num_words = get_num_words(frankenstein)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_counts = get_char_counts(frankenstein)
    sorted_char_counts = get_sorted_char_counts(char_counts)
    for line in sorted_char_counts:
        print(f"{line["character"]}: {line["count"]}")
    print("============= END ===============")

main()
