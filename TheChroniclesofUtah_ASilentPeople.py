#KYRA CRAWFORD

# restarting my choose your own adv game

import time

Inv = []
if Inv == []:
    print('\n|Your inventory is currently empty|\n')

def NoHelpStick():
    print('You continue along the dirt path, keeping an eye out for strangers along the way.\n')
    print('A large wooden gate stands before you. You look up to see a watchman gaze at you then open the gate.\n Behind which a small plaza with food stands and cloaked pedestrians bustles.\n')

def HelpStick():
    print('You continue along the dirt path, trying to forget the past 30 seconds of your life. ''Why the hell wasnt he wearing pants?''\n')
    print('Anyway, as you reach a clearing in the bushland, a large lake sits, quiet and pleasant.\nA cool mist carresses your face, reminding you of a place you do not remember.')

def TRANG():
    print('After walking for about 5 minutes, you notice a cloaked man sitting on a rock. You approach him for some direction.\n')
    print('The man seems to be distressed, he is slumped over with his head in his hands.\n')
    print('"Excuse me sir, do you know where the closest town is?", you inquire.\n')
    answer=input('The man replies with a groan, lifting his face from his wrinkly hands, "You arent from around here, I can smell it on you.\n You seem young, though. What do you say you help me out, then I tell you where to go?" (yes/no)\nYour reply: ')
    if answer== 'yes':
        print('"Great! But first, do you happen to have a stick or long object?"')
        if '| Stick |' in Inv:
            print('"Yes, I do. I picked it up a few minutes ago."')
            print('"Okay, give it here.", the man snatches the stick from you and skimpers away into the brush. As he runs, you realize he was not wearing pants. Strange.\n')
            Inv.remove('| Stick |')
            print('\n')
            time.sleep(5)
            HelpStick()
        else:
            print('"No, sorry. I did pass one just down the road, though. Its probably still there."\n')
            print('"Okay whatever, thanks for nothing."\n')
            print('You think nothing of his remarks, instead you assume he is a crabby old man who got lost going home.')
            NoHelpStick()

    elif answer== 'no':
        print('"Okay then. Guess they dont teach manners where you come from. Probably an Ari, pfft."\n')
        print('You are hurt by his remarks, although you do not truly understand them.\n')
        NoHelpStick()

def PickStick():
    answer= input('A stick lays in your path, would you like to pick it up? (yes/no)\n')
    if answer== 'yes':
        print('\nStick was added to your inventory')
        Inv.append('| Stick |')
        print('Bag contents:' + Inv[0])
        print('\n')
        dirt2()
    elif answer== 'no':
        print('You step over the stick and continue forwards...\n')
        dirt2()

def bear():
    print("Okay! Let's head on up!\n")
    answer = input('You encounter a brown bear. What do you do? (run/play dead)\n')
    if answer == 'play dead':
        print('You lay on your stomach and wait for the bear to pass you.')
        tbc()
    elif answer == 'run':
        print("You fool! You can't outrun a grizzly bear! You lose!\n")
        gameEnd()

def dirt2():
    print('A sign pointing to the left reads: "TRANGVIL - 1 km". You follow the road.')
    TRANG()

def dirt():
    print('You follow the dirt path straight ahead.\n')
    PickStick()

def paved():
    print('You walk on the pavement, it feels cold beneath your feet.\n')
    tbc()



def back():
    print("No problem, let's turn around...\n")
    answer = input('Before you lay two perpendicular paths, one made of dirt, the other cement along a long highway. Which do you follow? (dirt/paved)\n')
    if answer == 'dirt':
        dirt()
    elif answer == 'paved':
        paved()

#GENERAL GAME CODE (start, end, tbc, etc.)

def gameStart():
    answer = input('Your journey begins at the bottom of a mountain. Would you like to go up the mountain? (yes/no) ')
    if answer == 'yes':
        bear()
    elif answer == 'no':
        back()

def gameEnd():
    time.sleep(2)
    print('The game will restart in ten seconds. Close it now if you wish to stop playing.\n')
    time.sleep(10)

def tbc():
    print('*****This path is not complete yet*****')


while True:
    print('\n')
    print('Welcome to The Chronicles of Utah: A Silent People! This is a text-based Choose Your Own Adventure Game.\n Keep in mind this is in development, so please be careful to follow instructions.\n')
    answer = input('Would you like to play? (yes/no) ')

    if answer == 'yes':
        gameStart()

    elif answer == 'no':
        print('Why did you even open this, then? Get out of here!')
        gameEnd()
