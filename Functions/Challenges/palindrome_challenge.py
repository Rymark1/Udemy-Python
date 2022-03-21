def my_palindrome_sentence(sentence):
    sentence = ''.join(e for e in sentence if e.isalpha()).strip()
    if not sentence:
        return False
    else:
        return is_palindrome(sentence)


def his_palindrome_sentence(sentence):
    blank_string = ""
    for char in sentence:
        if char.isalnum():
            blank_string += char

    return is_palindrome(blank_string)


def is_palindrome(sentence):
    return sentence[::-1].casefold() == sentence.casefold()

sentence = input("Please enter a sentence to check:")
if my_palindrome_sentence(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print(f"'{sentence}' is not a palindrome")

if his_palindrome_sentence(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print(f"'{sentence}' is not a palindrome")