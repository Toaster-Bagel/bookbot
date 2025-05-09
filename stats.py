def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()
    return book_contents

def split(path_to_book):
    word_list = []
    word_list = get_book_text(path_to_book).split()
    print(f"Found {len(word_list)} total words")
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
    return letters

def sort_on(s):
    return s["num"]

def set_order(inp):
    dicl = []
    for a, b in inp.items():
        dics = {"char": a, "num": b}
        dicl.append(dics)
    dicl.sort(reverse=True, key=sort_on)
    for j in dicl:
        print(f"{j["char"]}: {j["num"]}")
