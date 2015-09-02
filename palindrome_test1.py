import re

def main():
    sentence = input("What is your sentence?\n")
    return sentence

def is_palindrome(sentence):
    stripped = re.sub(r'[^A-Za-z]','', sentence).lower()
    reverse = stripped[::-1]
    if reverse == stripped:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
