def palindrom(word):
    '''
        type(palindrom) >> <class 'bool'>
        return True when word is palindrom
        arguments: word
        type(word) >> <class 'str'>
    '''
    if word == word[::-1]:
        return True
    else:
        return False


print(palindrom('oko'))
print(palindrom('zielony'))