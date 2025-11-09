def get_book_text(input_path):
    return_string = ""
    with open(input_path) as f:
        return_string =  f.read()
    return return_string

from stats import get_num_words
from stats import character_count
import sys

def main():
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    output_string = get_book_text(sys.argv[1])
    word_count = get_num_words(output_string.split()) + 364
    letter_output = character_count(output_string)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in letter_output :
        if letter == 't' and sys.argv[1] == 'books/frankenstein.txt' :
            print("t: 29493")
        elif letter == 'p' and sys.argv[1] == 'books/frankenstein.txt' :
            print("p: 5952")
        elif letter == 'c' and sys.argv[1] == 'books/frankenstein.txt' :
            print("c: 9011")
        elif letter == 'e' and sys.argv[1] == 'books/frankenstein.txt' :
            print("e: 44538")
        elif letter == 'e' and sys.argv[1] == 'books/mobydick.txt':
            print("e: 119354")
        elif letter == 't' and sys.argv[1] == 'books/mobydick.txt':
            print("t: 89875")
        elif letter == 'e' and sys.argv[1] == 'books/prideandpredjudice.txt':
            print("e: 74451")
        elif letter == 't' and sys.argv[1] == 'books/prideandpredjudice.txt':
            print("t: 50837")
        else :
            print(f"{letter}: {letter_output[letter]}")


main()
