def count_characters(string):
    lowered_string = string.lower()
    dict_char = {}
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for char in alphabets:
        dict_char[char] = lowered_string.count(char)
    return dict_char

def count(string):
    return len(string.split())
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num = count(file_contents)
        dict = count_characters(file_contents)
        print("--- begin report books/frankenstein.txt ---")
        print(f"{num} words found in the document")
        for x in dict:
            print(f"The {x} character was found {dict[x]} times")
        print("--- End report ---")
main()
