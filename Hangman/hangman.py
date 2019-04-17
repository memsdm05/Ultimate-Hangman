# Hangman program
# 4-14-19
__author__='Ben Browner'

import time
import traceback
import subprocess
import random
import gallows # I was bored
import EncodeLibTest as cipher
import hardnessTest as dif
words = []
word = ""

foo = False

def error(message=''): # error message for generic prints
    if message == '':
        print('Error, invalid input')
    else:
        print('Error, invalid input; ' + message)




def importWords(): #designed to open and import the data from the words.txt file and store it into the global word list
    global words
    f = open('words.txt')
    for i in f:
        if len(i) < 20:
            words.append(i.rstrip('\n'))

def getNewWord(): #designed to randomly select a word from the list for each game cycledrawBlanks, designed to draw the initial number of blanks to match the length of the random
    global word
    word = random.choice(words)

def drawBlanks(): #draws blanks
    print('___ '*len(word))

def updateDisplay(select, mask=''): #which redraws the blanks when the user guesses a correct letter
    for x in range(len(word)):
        if len(mask) > 1:
            if mask[x] == '1':
                print(' 🔥 ', end=' ')
            elif word[x] in select:
                print(f' {word[x].upper()} ', end=' ')
            else:
                print('___', end=' ')
        else:
            if word[x] in select:
                print(f' {word[x].upper()} ', end=' ')
            else:
                print('___', end=' ')
    print()

def hasWon(guess, counter): # which returns True if the user has correctly guessed all the letters in the random word or False otherwise
    check = 0
    if len(guess) > 0:
        for x in word:
            for i in guess:
                if i == x:
                    check += 1
        return check == len(word)

def dupes(phrase): #does one thing and nothing else, that is it checks for dupes
    new = []
    newphrase = []
    for i in phrase:
        if i not in new:
            new.append(i)
            newphrase.append(i)
    return newphrase

def main(): #the main method that drives the program
    global word, words
    win = False
    jotaro = 0
    phrases = cipher.shifttext(-69, ['4Ufe,KKHRKeN[SGT', '?U[eKYZOTM[OYNeS_eLOXKYe/eKYZOTM[OYNe_U[f', 'VXKVUYZKXU[Yf', '?U[eJOYM[YZeSKf',
                                '_U[lXKeVU]KXeOYeZUUeYZXUTMf', '\\OYGHRKeIUTL[YOUT', "''''''........", ':.+e,/8+9ff', '4U:eZNKeLOXKYf'])
    debug = False # <== SET TO TRUE IF YOU WANT TO SEE THE FULL GAME + WORDS
    sel = 0
    if debug:
        unlocked = 5
    else:
        unlocked = 1
    modes = []
    mask = []
    maskwhere = []
    print('* Welcome to HANGMAN *')
    print('''### HOW TO PLAY ###
    Play the hardest mode to level up and get more modes. Average 
    hangman rules apply. There is sound in the game and it suppliments
    the expirence. Set debug (line 78) to True to unlock the full game.''')
    modes = cipher.shifttext(-34>>1, ["cvx'}r$1a}r+",'Vr%+1^!uv', "_!$~r}1^!uv=1S$'yP", "j!'1a$v&&+1Xr x%&r1^!uv", 'eYV1UVgZ]8d1h`cU1SR_\\'])
    # Play the game to figure out the encoded text or just do a simple [REDACTED] cipher. The ball is in your court.
    if debug: print(modes)
    while True:
        try:
            health = 100
            devil = False
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            if win:
                x = subprocess.Popen(['afplay', 'favorite_song.mp3'])
            else:
                x = subprocess.Popen(['afplay', 'menu.mp3'])
            ## how to play sounds in python with only builtin modules ##
            # afplay is a terminal command that can play most audio file formats.
            # subprocess runs afplay in the background so we dont have to wait for it
            # to finish. If you assign the class Popen to a varible you can kill it
            # via its PID (i think). So I create background music that quites when I
            # want it too.
            while True:
                if jotaro == 0:
                    print('Select Mode (x to quit): ')
                    for i in range(5):
                        if i + 1 <= unlocked:
                            print(f'{i+1}. {modes[i]}')
                        else:  # Little tiny formatter that makes the menu select thing
                            print(f'{i+1}. ████████████ 🔒')
                selection = input('> ')
                if selection.lower() == 'x':
                    x.kill()
                    quit()
                if selection in '12345' and len(selection) == 1:
                    if int(selection) <= unlocked:
                        sel = int(selection)
                        subprocess.Popen('afplay -r 10 secosmic_lo.wav'.split())
                        break
                    else:
                        print("You haven't unlocked the mode yet")
                else:
                    error('only input menu numbers')
                jotaro += 1
                if jotaro >= 5:
                    jotaro = 0
            x.kill() # Stops the music
            importWords()
            if sel != 1:
                words = dif.howhard((sel-2)*10, sel*10) # Each mode other than normal play is 10 more
            getNewWord()
            memes = []
            maskwhere = []
            oofs = 0
            first = True
            if sel == 5:
                devil = True
                mask = '0'*len(word)
                print('##### HOW TO PLAY DEVIL MODE #####')
                print('The devil will randomly set fire to')
                print('any space, filled or not. When a s-')
                print('pace is on fire it deletes the fil-')
                print('led letter. Clear the fire by gues-')
                print('sing correctly')
                print('>> PRESS ENTER TO CONTINUE <<', end='')
                input()
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                subprocess.Popen(('say -v Daniel [[pbas 20]] prepare to die!').split())
                time.sleep(0.5)
                p = subprocess.Popen(['afplay', 'doom.mp3'])
            while True:
                    if first: # do some special formatting when it is first run
                        if debug:
                            print(word)
                        gallows.drawGallows(0)
                        drawBlanks()
                        first = False
                        clear = False
                    else:
                        if debug:
                            print(word)
                        gallows.drawGallows(oofs)
                        if devil:
                            temp = []
                            maskwhere.append(random.randint(0, len(word) - 1))
                            # maskwhere selects where in the word the the fire sould appear
                            # its 10:11 PM right now and I was on 8 cans of coke when I wrote the devil
                            # script so please exuse me if I kinda don't know how it works
                            # IT JUST WORKS -- kinda
                            if clear:
                                subprocess.Popen((f'say -v Daniel {random.choice(phrases)}').split())
                                maskwhere = []
                                for i in range(len(word)):
                                    if mask[i] == '1':
                                        temp.append(word[i])
                                if len(temp) > 0:
                                    for x in temp:
                                        if x in memes:
                                            memes.remove(x)
                            mask = []
                            for i in range(len(word)):
                                if i in maskwhere:
                                    mask.insert(i, '1')
                                else:
                                    mask.insert(i, '0')
                            updateDisplay(memes, mask)
                            clear = False
                        else:
                            updateDisplay(memes)
                    print('Letters guessed:', end=' ')
                    print(memes)
                    if devil:
                        print('👹 Devil\'s Power: ' + str((''.join(mask).count('1'))*len(word)))
                    if hasWon(memes, oofs):
                        print('YOU WON!!!')
                        if devil:
                            p.kill()
                        subprocess.Popen(['afplay', 'win.wav'])
                        if sel == unlocked and not devil:
                            unlocked += 1 # Level up whenever you play the hardest level avilable
                            print('LEVEL UP +1')
                        else:
                            subprocess.Popen(['afplay', 'game.wav'])
                            if debug:
                                print('Yay you completed the game... SIKE. I know what you did with debug and all')
                            else:
                                print('HOLY MOLY YOU DID ALL THE LEVELS WITHOUT DEBUG')
                            print(cipher.shifttext(-31, ["`3?!?2%7!2$?(%2%?)3?9/52?&!6/2)4%?3/.'?LL?qhoshcd@@@@"])[0])
                            win = True
                        break
                    if oofs == 6:
                        if devil:
                            p.kill()
                        subprocess.Popen(['afplay', 'loose.mp3'])
                        print(f'Sorry buddy, the correct word was {word}')
                        break
                    raw = input('Guess a letter or word:  ').lower()
                    if len(raw) > 2:
                        if raw in words:
                            if raw == word: memes = list(dupes(raw)); subprocess.Popen(['afplay', 'ding.wav'])
                            else: oofs += 1; error(); subprocess.Popen(['afplay', 'car_door.wav'])
                        else: error(); oofs += 1; subprocess.Popen(['afplay', 'car_door.wav'])
                    else:
                        if raw not in 'qwertyuiopasdfghjklzxcvbnm' or raw == '':
                            error('enter only letters or words, you dumbbutt')
                            subprocess.Popen(['afplay', 'car_door.wav'])
                            oofs += 1
                        else:
                            if raw not in memes:
                                memes.append(raw)
                            else:
                            # Literally see if you screwed up or not
                                oofs += 1
                                subprocess.Popen(['afplay', 'car_door.wav'])
                                print('already in guess')
                                continue
                            if raw not in word:
                                subprocess.Popen(['afplay', 'car_door.wav'])
                                oofs += 1
                            else:
                                subprocess.Popen(['afplay', 'ding.wav'])
                                clear = True
        except Exception:
            if sel == 5:
                p.kill()
                traceback.print_exc()
                quit()
        # so the doom theme doesnt blast your ears when something goes wrong


if __name__ == '__main__':
    main()