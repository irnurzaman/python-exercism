def is_pangram(sentence):

    # Initiate alphabet dictionary
    alphabet = {}
    for i in range(97, 123):
        alphabet[chr(i)] = 0

    sentence = sentence.lower()
    for char in sentence:
        if char in alphabet:
            alphabet[char] += 1

    if 0 in alphabet.values():
        return False
    else:
        return True
