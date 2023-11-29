# print_changed_files.py
import sys

def print_changed_files():
    for line in sys.stdin:
        print(line.strip())

if __name__ == "__main__":
    print_changed_files()
