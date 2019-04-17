from math import *
words = []

def howhard(low, high):
    f = open('words.txt')
    for i in f:
        if len(i) < 20:
            words.append(i.rstrip('\n'))
    f.close()


    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    apple = {}

    for word in words:
        add = 0
        repeat = []
        rep = 0
        for i in word:
            if i in repeat:
                rep += 1
            else:
                repeat.append(i)
        for letter in word:
            add += alphabet.find(letter)
        add *= len(word)
        try:
            add /= rep
        except:
            pass
        apple[word] = (add - 0.75) * (50 - 1) / (2015 - 1) + 1

    applesorted = {}

    for i in sorted(apple.items(), key=lambda x: x[1]):
        applesorted[i[0]] = i[1]

    final = []
    for i in applesorted:
        if float(applesorted[i]) > low and float(applesorted[i]) < high:
            final.append(i)
    return final