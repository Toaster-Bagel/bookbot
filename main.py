from stats import split
from stats import letter_count
from stats import set_order
import sys

def main(blep):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {blep}")
    print("----------- Word Count ----------")
    split(blep)
    print("--------- Character Count -------")
    set_order(letter_count(blep))
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])