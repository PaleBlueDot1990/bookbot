import sys 
from stats import get_num_words
from stats import get_character_frequency
from stats import sort_char_freq

def get_book_text(file_path):
    with open(file_path) as f:
        filecontents = f.read()
        return filecontents

def pretty_print(file_path, num_words, char_freq_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for char_freq in char_freq_list:
        ch = char_freq["character"]
        if ch.isalpha():
            fq = char_freq["frequency"]
            print(f"{ch}: {fq}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)

    char_freq_dict = get_character_frequency(book_text)
    char_freq_list = sort_char_freq(char_freq_dict)
    pretty_print(file_path, num_words, char_freq_list)

main()