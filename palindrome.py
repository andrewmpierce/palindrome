def main():
    sentence = input("What is your sentence?\n")
    sentence1 = sentence.strip('?.!,').lower().replace(' ','')
    return sentence1

def is_palindrome():
    string = main()
    reverse = string[::-1]
    if reverse == string:
        return print("palindrome")
    else:
        return print("Not")


is_palindrome()
