# simple madlib

# add sound effects
import pygame 
pygame.init()
pygame.mixer.init()
next_sound = pygame.mixer.Sound('my_madlibs/madlibs_collection/mixkit-unlock-game-notification-253.wav')
reveal_sound = pygame.mixer.Sound('my_madlibs/madlibs_collection/mixkit-happy-bells-notification-937.wav')

def madlib():
    # input prompts
    print('-----------')
    print('Input words as you like!')
    print('-----------')
    next_sound.play()
    noun = input('Noun: ')
    next_sound.play()
    adj1 = input('Adjective: ')
    next_sound.play()
    adj2 = input('Another Adjective: ')
    next_sound.play()
    verb = input('Verb: ')
    next_sound.play()
    movie_character = input('Movie character: ')
    print('-----------')

    # define a madlib
    madlib_out = f'I love {noun} because it is {adj1}. Whenever I feel {adj2}, I always \
{verb} to feel like I have superpower like {movie_character}!'

    reveal_sound.play()
    ready = input('Enter "ok" to continue or "nope" to change the inputs: ').lower()

    if ready == 'ok':
        print('-----------')
        print(madlib_out)
        print('-----------')
    elif ready == 'nope':
        madlib_out_fixed = madlib()
        print('-----------')
        print(madlib_out_fixed)
        print('-----------')
    else:
        print('Game Ended!')
    

if __name__ == '__main__':
    madlib()