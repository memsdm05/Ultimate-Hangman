# Hangman Pretty Print Module
# 4-14-19
__author__ = "Ben Browner"

def drawGallows(i):
    # O ╱|╲╱ ╲
    if i < 0 or i > 6:
        print('wow you think you\'re so cool')
        return
    man = ['         ',
           ' O       ',
           ' O  |    ',
           ' O ⎛|     ',
           ' O ⎛|⎞   ',
           ' O ⎛|⎞╱  ',
           ' O ⎛|⎞╱ ╲'
           ]


    m = man[i]
    print("┏━━━━━━━━┑")
    print("┃╱       ┆")
    print("┃       "+ m[0:3])# O - (Everytime you screw up, I die more and more)
    print("┃       "+ m[3:6])#/|\
    print("┃       "+ m[6:9])#/ \
    print("┃         ")
    print("┻┳┳┳┳┳┳┳┳┳")
    print()


if __name__ == '__main__':
    print('What are you doing. Run hangman.py')