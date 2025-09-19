from stats import number_of_words_in_string, number_of_times_char_used, sort_by, sorted_list_of_num_of_times_char_used
import sys

def get_book_text(book_file_path):
    book_text = ""
    with open(book_file_path) as book_file:
        book_text = book_file.read()
    return book_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        book_text_string = get_book_text(file_path)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words_in_string(book_text_string)} total words")
        print("--------- Character Count -------")
        dict_of_char_counts = number_of_times_char_used(book_text_string)
        sorted_dict_of_char_counts = sorted_list_of_num_of_times_char_used(dict_of_char_counts)
        for character in sorted_dict_of_char_counts:
            print(f"{character["char"]}: {character["num"]}")
        print("============= END ===============")

main()