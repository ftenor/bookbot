def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_chars(text):
    char_dict = {}
    text_lower = text.lower()
    for char in text_lower:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] = char_dict[char] + 1
    return char_dict

def get_sorted_list(chars):
    sorted_list = []
    for char in chars:
        temp = {
            "char": char,
            "num": chars[char]
        }
        sorted_list.append(temp)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(items):
    return items["num"]