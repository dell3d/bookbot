def word_count(text):
    return len(text.split())

def count_chars(text):
    chars = text.lower()
    new_dict = {}
    for i in chars:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict  # Changed to return the dictionary instead of printing it

def chars_dict_to_sorted_list(char_dict):
    # Sort the dictionary by count in descending order
    sorted_char_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_char_dict

def report(char_dict, count):
    string = (
        "============ BOOKBOT ============\n"
        "Analyzing book found at books/frankenstein.txt...\n"
        "----------- Word Count ----------\n"
        f"Found {count} total words\n"
        "--------- Character Count -------\n"
    )
    for char, count in char_dict.items():
        if char.isalpha():  # Only include alphabetic characters
            string += f"{char}: {count}\n"
    string += "============= END ==============="
    return string