import random

# a4-6 are inputs that fill in the blank of a madlib, a3 is a3 because of there being 3 options


a4 = input('tell me an noun')
a5 = input('tell me a verb')
a6 = input('tell me a noun')

    
def madlib():
    a3 =random.randint(1,3)

    if a3==1:
        print('My favorite food is', a4,', I love it!')

    elif a3==2:
        print('I think', a5, 'is really funny! I dig it!')

    elif a3==3:
        print('did you hear about',a6,'?', 'It was really suprising.')


madlib()