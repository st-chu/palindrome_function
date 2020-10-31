def palindrom(sentence):
    '''
        type(palindrom) >> <class 'bool'>
        return True when the word is a palindrome
        arguments: sentence
        type(sentence) >> <class 'str'>
    '''
    sentence = sentence.lower()
    sentence = sentence.replace(' ', '')
    if sentence == sentence[::-1]:
        return True
    else:
        return False


print(palindrom('A to kiwi zdziwi kota'))
print(palindrom('zielony'))