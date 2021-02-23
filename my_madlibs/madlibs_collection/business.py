# business madlib
# news reference: https://edition.cnn.com/2021/02/11/investing/elon-musk-pay-wealth-tesla-stock-options/index.html

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
    name1 = input('Name: ')
    next_sound.play()
    name2 = input('Another name: ')
    next_sound.play()
    name3 = input('Yet another name: ')
    next_sound.play()
    comperative = input('Comperative: ')
    next_sound.play()
    superlative1 = input('Superlative: ')
    next_sound.play()
    superlative2 = input('Another superlative: ')
    next_sound.play()
    company1 = input('Company name: ')
    next_sound.play()
    company2 = input('Another company name: ')
    next_sound.play()
    noun = input('Noun: ')
    print('-----------')


    # define a madlib

    madlib_out = f"{name1}, the world's {superlative1} person, is about to get a whole lot {comperative}! \
The rise in {company1}'s {noun}, has made {name1} the {superlative2} person on the planet, according to \
{name2}, surpassing {company2} founder, {name3}." 


    # allow players to re-enter the words
    reveal_sound.play()
    ready = input('Enter "ok" to continue or "nope" to change the inputs: ').lower()

    if ready == 'ok':
        print('-----------')
        print(madlib_out)
        print('-----------')
    elif ready == 'nope':
        print('-----------')
        madlib()
        print('-----------')
    else:
        print('-----------')
        print('Game Ended!')
        print('-----------')

if __name__ == '__main__':
    madlib()