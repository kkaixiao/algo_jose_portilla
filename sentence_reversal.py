def rev_word(s):
    words =[]

    i = 0

    while i < len(s):

        if s[i] != ' ':
            start_point = i
            while (i < len(s)) and (s[i] != ' '):
                i += 1

            words.append(s[start_point: i])

        i += 1

    return_sentence = words[len(words) - 1]

    for i in range(len(words)-2, -1, -1):
        return_sentence = return_sentence + ' ' + (words[i])

    return return_sentence








s = 'Hi John,    are you ready to go?'

print(rev_word(s))