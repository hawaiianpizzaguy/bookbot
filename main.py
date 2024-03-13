def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    total_words = get_word_count(book_text)
    character_dict = get_character_count_dict(book_text)
    sorted_character_dict = sorted_dict_list(character_dict)

    print(f"---- Start of report for {book_path}")
    print(f"This book has {total_words} words")
    print(f"The most used characters and times they are used: {sorted_character_dict}")

def get_book_text(path):
    with open(path) as book:
        return book.read()
    
def get_word_count(book):
    words = book.split()
    return len(words)

def get_character_count_dict(book):
    book_lower = book.lower()
    character_dict = {}
    for letter in book_lower:
        if letter in character_dict:
            character_dict[letter] += 1
        else:
            character_dict[letter] = 1
    return character_dict
    
def value_to_sort_on(dict):
    return dict["number"]

def sorted_dict_list(character_dict):
    sorted_list = []
    for char in character_dict:
        sorted_list.append({"char": char, "number": character_dict[char]})
    sorted_list.sort(reverse=True, key=value_to_sort_on)
    return sorted_list

main()