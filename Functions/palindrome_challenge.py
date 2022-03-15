def palindrome_sentence(sentence):
    sentence = ''.join(e for e in sentence if e.isalpha()).strip()
    if not sentence:
        return False
    else:
        return sentence[::-1].casefold() == sentence.casefold()


sentence = input("Please enter a sentence to check:")
if palindrome_sentence(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print(f"'{sentence}' is not a palindrome")
