def main():
    book_path =  "books/frankenstein.txt"
    text = get_book(book_path)
    count = count_words(text)
    counting = count_characters(text)
    report = dict_to_list(counting)
    report.sort(reverse=True, key=sort_on)
    print_report(count, report)

def get_book(path):
    with open(path) as f:
        return f.read()
    

def count_words(book):
    text = book.split()
    return len(text)


def count_characters(book):
    counting_dict = {}
    lower_book = book.lower()
    for letter in lower_book:
        if letter in counting_dict.keys():
            counting_dict[letter] += 1
        else:
            counting_dict.update({letter:1})
    return counting_dict

def dict_to_list(dict):
    new_list = []
    for k in dict:
        new_list.append({"name": k, "num": dict[k]})
    return new_list

def sort_on(dict):
    return dict["num"]

def print_report(count, list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document\n")
    
    for i in list:
        if i["name"].isalpha():
            print(f"""The {i["name"]} character was found {i["num"]} times""")
    


if __name__ == "__main__":
    main()