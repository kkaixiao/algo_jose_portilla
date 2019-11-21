def anagram(s1, s2):
    s1 = s1.lower().replace(' ', '')
    s2 = s2.lower().replace(' ', '')

    if len(s1) != len(s2):
        return False

    count = {}

    for char in s1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in s2:
        if char in count:
            count[char] -= 1

    for k,v in count.items():
        if v > 0:
            return False

    return True


print(anagram('how are you', 'you are wow'))