def anagram(s1, s2):
    s1 = s1.lower().replace(' ', '')
    s2 = s2.lower().replace(' ', '')

    return sorted(s1) == sorted(s2)


print(anagram('how are you', 'you are how'))