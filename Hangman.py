words = [
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'daiquiri',
    'dirndl',
    'disavow',
    'dizzying',
    'duplex',
    'dwarves',
    'embezzle',
    'equip',
    'espionage',
    'exodus',
    'faking',
    'fishhook',
    'fixable',
    'fjord',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'frizzled',
    'fuchsia',
    'funny',
    'gabby',
    'galaxy',
    'galvanize',
    'gazebo',
    'gizmo',
    'glowworm',
    'glyph',
    'gnarly',
    'gnostic',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jaywalk',
    'jazziest',
    'jazzy',
    'jelly',
    'jigsaw',
    'jinx',
    'jiujitsu',
    'jockey',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'klutz',
    'knapsack',
    'larynx',
    'lengths',
    'lucky',
    'luxury',
    'lymph',
    'marquis',
    'matrix',
    'megahertz',
    'microwave',
    'mnemonic',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numskull',
    'nymph',
    'onyx',
    'ovary',
    'oxidize',
    'oxygen',
    'pajama',
    'peekaboo',
    'phlegm',
    'pixel',
    'pizazz',
    'pneumonia',
    'polka',
    'pshaw',
    'psyche',
    'puppy',
    'puzzling',
    'quartz',
    'queue',
    'quips',
    'quixotic',
    'quiz',
    'quizzes',
    'quorum',
    'razzmatazz',
    'rhubarb',
    'rhythm',
    'rickshaw',
    'schnapps',
    'scratch',
    'shiv',
    'snazzy',
    'sphinx',
    'spritz',
    'squawk',
    'staff',
    'strength',
    'strengths',
    'stretch',
    'stronghold',
    'stymied',
    'subway',
    'swivel',
    'syndrome',
    'thriftless',
    'thumbscrew',
    'topaz',
    'transcript',
    'transgress',
    'transplant',
    'diphthong',
    'twelfth',
    'twelfths',
    'unknown',
    'unworthy',
    'unzip',
    'uptown',
    'vaporize',
    'vixen',
    'vodka',
    'voodoo',
    'vortex',
    'voyeurism',
    'walkway',
    'waltz',
    'wave',
    'wavy',
    'waxy',
    'wellspring',
    'wheezy',
    'whiskey',
    'whizzing',
    'whomever',
    'wimpy',
    'witchcraft',
    'wizard',
    'woozy',
    'wristwatch',
    'xylophone',
    'yachtsman',
    'yippee',
    'yoked',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zigzagging',
    'zilch',
    'zipper',
    'zodiac',
    'zombie',
]

import pygame
from ListOfWords import words
from random import choice
from sys import exit
from time import sleep
from string import ascii_lowercase
pygame.init()

# Fonts
pygame.font.init()
main_font = pygame.font.SysFont('comicsans', 50)
end_font = pygame.font.SysFont('comicsans', 200)

# Colors
white = (255, 255, 255)
body_color = (140, 140, 140)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Main Surface
WIDTH, HEIGHT = 1366, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

# Variables
FPS = 15
clock = pygame.time.Clock()
word = choice(words)
letters_left = word
char_pres = []
char_pres_blit = None
word_width, word_height = WIDTH//2, HEIGHT//2

# The Hangman Surface and variables connected
hangman_width, hangman_height = 500, 600
Hangman = pygame.Surface((hangman_width, hangman_height))
rec_width, rec_height = 30, 10
line_width = 19
body_length = 180
middle = hangman_width // 2 + line_width // 2


def check_letters():
    global letters_left
    global char_pres_blit

    char_pres_blit = main_font.render(' '.join(char_pres), True, white)
    for letter in char_pres:
        if letter in word:
            letters_left = letters_left.replace(letter, '')


def hangman_state(state):
    # The width of the lines is 15
    if state == 0:
        pygame.draw.line(
            Hangman,
            white,
            (0, line_width/2),
            (middle, line_width/2),
            line_width,
        )
        pygame.draw.line(
            Hangman,
            white,
            (line_width/2, 0),
            (line_width/2, hangman_height),
            line_width
        )
        pygame.draw.line(
            Hangman,
            white,
            (middle, 0),
            (middle, hangman_height//6),
            line_width
        )
    elif state == 1:
        pygame.draw.circle(
            Hangman,
            body_color,
            (middle, hangman_height//6),
            line_width*2,
            0,
        )
    elif state == 2:
        pygame.draw.circle(
            Hangman,
            black,
            (middle - 13, hangman_height//6.7),
            5,
            0,
        )
    elif state == 3:
        pygame.draw.circle(
            Hangman,
            black,
            (middle + 13, hangman_height//6.7),
            5,
            0,
        )
    elif state == 4:
        pygame.draw.line(
            Hangman,
            red,
            (middle+22, hangman_height//5.4),
            (middle-22, hangman_height//5.4),
            7
        )
    elif state == 5:
        pygame.draw.line(
            Hangman,
            body_color,
            (middle, hangman_height//5),
            (middle, hangman_height//6 + body_length),
            line_width
        )
    elif state == 6:
        pygame.draw.line(
            Hangman,
            body_color,
            (middle, hangman_height/6 + body_length),
            (middle - 70, hangman_height/6 + body_length + 100),
            line_width
        )
    elif state == 7:
        pygame.draw.line(
            Hangman,
            body_color,
            (middle, hangman_height/6 + body_length),
            (middle + 70, hangman_height/6 + body_length + 100),
            line_width
        )
    elif state == 8:
        pygame.draw.line(
            Hangman,
            body_color,
            (middle, hangman_height/3.5),
            (middle + 70, hangman_height/6 + body_length),
            line_width,
        )
    elif state == 9:
        pygame.draw.line(
            Hangman,
            body_color,
            (middle, hangman_height/3.5),
            (middle - 70, hangman_height/6 + body_length),
            line_width,
        )


def won_or_lost(let_left, state):
    if let_left == '':
        WIN.fill(black)
        Hangman.fill(black)
        WIN.blit(end_font.render('YOU WON', True, green), (0, 0))
        pygame.display.update()
        sleep(2)
        main()
    elif state == 9:
        WIN.fill(black)
        WIN.blit(Hangman, (0, HEIGHT - hangman_height))
        Hangman.fill(black)
        WIN.blit(end_font.render('YOU LOST', True, red), (0, 0))
        pygame.display.update()
        sleep(2)
        main()


def draw(word_len):
    list_of_cords = range(0, (word_len * 2) * rec_width, rec_width * 2)

    WIN.fill(black)
    for cord in list_of_cords:
        cur_letter = word[list_of_cords.index(cord)]
        if cur_letter in char_pres:
            WIN.blit(main_font.render(cur_letter, True, white), (cord + word_width, word_height))
        else:
            pygame.draw.rect(
                WIN,
                white,
                pygame.Rect((cord + word_width, word_height), (rec_width, rec_height))
            )
    WIN.blit(char_pres_blit, (0, 0))
    WIN.blit(Hangman, (0, HEIGHT - hangman_height))

    pygame.display.update()


def main():
    global word
    global letters_left
    global char_pres
    global char_pres_blit

    word = choice(words)
    letters_left = word
    char_pres = []
    char_pres_blit = None
    print(word)
    alphabet = list(ascii_lowercase)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) in alphabet and pygame.key.name(event.key) not in char_pres:
                    char_pres.append(pygame.key.name(event.key))
                    char_pres.sort()

        state2 = char_pres.copy()
        state = []
        for let in state2:
            if let not in word:
                state.append(let)
        state = len(state)
        hangman_state(state)
        won_or_lost(letters_left, state)
        check_letters()

        draw(len(word))
    main()


if __name__ == "__main__":
    main()
