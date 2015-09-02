#Test is pointed to palindrome_hard.py
import re

def main():
    sentence = input("What is your sentence?\n")
    return sentence

def is_palindrome(sentence):
    stripped = re.sub(r'[^A-Za-z]','', sentence).lower()
    for x in range(len(stripped)):
        if len(stripped) <=1:
            return True
        elif stripped[0] == stripped[-1]:
            stripped = stripped[1:-1]
        else: return False
if __name__ == '__main__':
    print(is_palindrome(main()))
