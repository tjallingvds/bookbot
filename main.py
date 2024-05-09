def main():
    text = get_book()
    return text
    
    
def get_book():
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_words(book):
    word_list = book.split()
    return len(word_list)

def count_characters(book): 
    char_count = {}
    text_lower = book.lower()
    list_chars = list(text_lower)
    for i in list_chars:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count

def book_report(total_words, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(total_words) + " words found in the document \n")
    for i in char_count.keys():
        if i.isalpha():
            print("The '" + str(i) + "' character was found " + str(char_count[i]) + " times.")
    print("--- End report ---")

