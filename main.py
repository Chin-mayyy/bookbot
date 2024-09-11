def count_characters(string):
    lowered_string = string.lower()
    dict_char = {}
    for char in lowered_string:
        if char in dict_char:
            dict_char[char] += 1
        else:
            dict_char[char] = 1
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
