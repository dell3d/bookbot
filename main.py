from stats import word_count, count_chars, chars_dict_to_sorted_list, report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <filepath>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    wc = word_count(text)
    char_dict = count_chars(text)
    sorted_char_dict = chars_dict_to_sorted_list(char_dict)
    report_string = report(sorted_char_dict, wc)
    print(report_string)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()