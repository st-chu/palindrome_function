def palindrom(word):
    '''
        type(palindrom) >> <class 'bool'>
        return True when the word is a palindrome
        arguments: word
        type(word) >> <class 'str'>
    '''
    if word == word[::-1]:
        return True
    else:
        return False


print(palindrom('oko'))
print(palindrom('zielony'))