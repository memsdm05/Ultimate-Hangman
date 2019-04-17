# Script that encrypt and decrypt ModTest.py
import random
test = []


def shifttext(shift, inp):
    strs = ''.join([chr(i) for i in range(32, 127)])
    newfile = []
    for x in inp:
        data = ''
        for i in x:
            if i in strs:
                data += strs[(strs.index(i) + shift) % len(strs)]
            else:
                data += i
        newfile.append(data)
    return newfile


def do_encode(scramble=False):
    with open('ModTest.py') as f:
        for line in f:
            test.append(line)

    def import_test():
        try:
            import ModTest  # change this to module name or dont
            return True
        except:
            return False

    def find_shift(lines):
        i = 0
        remember = lines
        while True:
            with open('ModTest.py', 'w') as f:
                f.writelines(shifttext(i, lines))
            i += 1
            if import_test():
                return i % 95
    shift = random.randint(-95, 95)
    if scramble:
        with open('ModTest.py', 'w') as f:
            f.writelines(shifttext(shift, test))
    else:
        with open('ModTest.py', 'w') as f:
            find_shift(test)
