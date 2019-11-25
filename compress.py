
def compress(s):
    prechar = s[0]

    i = 1
    ret_str = ''
    count = 1
    while i < len(s):
        if prechar != s[i]:
            ret_str = ret_str + prechar + str(count)
            count = 1
        else:
            count += 1
        prechar = s[i]
        i += 1
    ret_str = ret_str + prechar + str(count)
    return ret_str


str1 = 'AAAAABBBBCCCDDDDF'

print(compress(str1))