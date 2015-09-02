import re

def main():
    sentence = input("What is your sentence?\n")
    return sentence

def is_palindrome(sentence):
    stripped = re.sub(r'[^A-Za-z]','', sentence).lower()
    if len(stripped) <= 1:
        return True
    elif stripped[0] == stripped[-1]:
        return is_palindrome(stripped[1:-1])
    else: return False

if __name__ == '__main__':
    is_palindrome(main())

#reverse = stripped[::-1]
#if reverse == stripped:
#    return print("True")#True
#else:
#    return print("False")#False
