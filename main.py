import sys
from stats import count_words, count_chars, get_sorted_list

def get_book_text(file_path):
    file_contents = file_path.read()
    return file_contents

def print_char_count(char_count):
    for char in char_count:
        if char["char"].isalpha():
            num = char["num"]
            print(f"{char["char"]}: {num}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path) as fp:
        text = get_book_text(fp)
        sorted_list = get_sorted_list(count_chars(text))

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {count_words(text)} total words")
        print("--------- Character Count -------")
        print_char_count(sorted_list)
        print("============= END ===============")

main()



