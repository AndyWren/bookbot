from collections import Counter


def count_words(output):
    return len(output.split())


def occurrences(output):
    s = output.lower()
    return Counter(s)
