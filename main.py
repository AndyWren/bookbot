from collections import Counter
import string

def read_book(path_to_book):
    with open(path_to_book, 'r') as f:
        return f.read()

def count_words(output):
    return len(output.split())

def occurrences(output):
    s = output.lower()
    return Counter(s)

def report(book, word_count, letter_count):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document")
    print()
    for letter, count in letter_count.most_common():
        if letter in string.ascii_lowercase:
            print(f"The '{letter}' character was found {count} times")

    print("--- End report ---")

if __name__ == '__main__':
    path_to_book = "books/frankenstein.txt"

    output = read_book(path_to_book)
    word_count = count_words(output)
    letter_count = occurrences(output)
    report(path_to_book, word_count, letter_count)
