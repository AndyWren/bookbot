import sys
from stats import count_words, occurrences


def read_book(path_to_book):
    with open(path_to_book, "r") as f:
        return f.read()


def report(book, word_count, letter_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter, count in letter_count.most_common():
        if letter.isalpha():
            print(f"{letter}: {count}")
    print("============= END ===============")


def main(path_to_book: str):
    output = read_book(path_to_book)
    word_count = count_words(output)
    letter_count = occurrences(output)
    report(path_to_book, word_count, letter_count)


if __name__ == "__main__":
    arguements = sys.argv
    if len(arguements) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = arguements[1]
    main(path_to_book=path_to_book)
