import sys
def map():
    for line in sys.stdin: 
        words = line.split(" ")
        for word in words:
            print(" ".join([word.strip(), "1"]))


if __name__ == "__main__":
    map()