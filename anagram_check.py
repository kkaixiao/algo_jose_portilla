def anagram(s1, s2):
    str1 = s1.lower().replace(' ', '')
    str2 = s2.lower().replace(' ', '')

    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        str2 = str2.replace(str1[i], '', 1)

    return len(str2) == 0



print(anagram('how are you', 'you arethow'))