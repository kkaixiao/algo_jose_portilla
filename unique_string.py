def uni_char(s):
    counter = []
    for i in range(len(s)):
        if s[i] not in counter:
            counter.append(s[i])
            continue
        else:
            return False

    return True


print(uni_char('abcdee'))

print(uni_char('abcde'))