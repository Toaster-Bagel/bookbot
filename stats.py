def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()
    return book_contents

def split(path_to_book):
    word_list = []
    word_list = get_book_text(path_to_book).split()
    print(f"{len(word_list)} words found in the document")
    return len(word_list)

def letter_count(text):
    letters = {}
    k = get_book_text(text)
    for word in k:
        p = []
        p = word.lower().split()
        for l in p:
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1
    print(letters)
    return letters
