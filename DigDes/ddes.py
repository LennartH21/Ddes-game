# importing modules
import sys
import pygame
import random
from pygame.locals import *


# creating board
pygame.init()
pygame.font.init()
size = (945, 693)
board = pygame.image.load('BoardGame.png')
board = pygame.transform.scale(board, (945, 693))
pygame.display.set_caption('Sinip - Turn Based Game')
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
screen.blit(board, (0, 0))
pygame.display.update() 

# creating variables

rollfont = pygame.font.SysFont("arial", 40)
chancefont = pygame.font.SysFont("arial", 30)
endfont = pygame.font.SysFont("arial", 80)
startscreenfont = pygame.font.SysFont("arial", 30)
font = pygame.font.SysFont("arial", 60)
dice1 = pygame.image.load("dice1.png")
dice1 = pygame.transform.scale(dice1, (100, 100))
dice2 = pygame.image.load("dice2.png")
dice2 = pygame.transform.scale(dice2, (100, 100))
dice3 = pygame.image.load("dice3.png")
dice3 = pygame.transform.scale(dice3, (100, 100))
dice4 = pygame.image.load("dice4.png")
dice4 = pygame.transform.scale(dice4, (100, 100))
dice5 = pygame.image.load("dice5.png")
dice5 = pygame.transform.scale(dice5, (100, 100))
dice6 = pygame.image.load("dice6.png")
dice6 = pygame.transform.scale(dice6, (100, 100))
redimg = pygame.image.load(r'redplayer.png')
redimg = pygame.transform.scale(redimg, (85, 75))
yellowimg = pygame.image.load(r'yellowplayer.png')
yellowimg = pygame.transform.scale(yellowimg, (85, 75))
blueimg = pygame.image.load(r'blueplayer.png')
blueimg = pygame.transform.scale(blueimg, (85, 75))
greenimg = pygame.image.load(r'greenplayer.png')
greenimg = pygame.transform.scale(greenimg, (85, 75))
text1 = 'Welcome to Sinip, the rules are pretty simple.'
text2 = 'Press the spacebar when it is your turn to roll the dice.'
text3 = 'You will be moved forward by what you have rolled.'
text4 = 'Chance cards give you a 50/50 chance of moving forward or back.'
text5 = 'You can choose whether you want to'
text6 = 'or don’t want to take the chance.'
text7 = 'First one to reach the finish line wins the game!'
chancetext1 = 'You landed on chance!'
chancetext2 = 'if you take the chance'
chancetext3 = 'you have a 50/50 chance of moving forward or back'
chancetext4 = 'press y to take the chance, and n not to'
run = True
rolling_dice = True
playerrolled = 0
redtilenum = 0
greentilenum = 0
yellowtilenum = 0
bluetilenum = 0
font = pygame.font.SysFont("arial", 60)
playinggame = True

# tile to coordinates
poscoords = {
    0: (75, 570),
    1: (75, 490),
    2: (75, 425),
    3: (75, 340),
    4: (75, 260),
    5: (75, 180),
    6: (75, 100),
    7: (160, 100),
    8: (240, 100),
    9: (330, 100),
    10: (330, 180),
    11: (330, 260),
    12: (330, 340),
    13: (330, 425),
    14: (330, 590),
    15: (330, 505),
    16: (420, 590),
    17: (505, 590),
    18: (505, 505),
    19: (505, 425),
    20: (505, 340),
    21: (505, 260), 
    22: (505, 180),
    23: (505, 100),
    24: (590, 100),
    25: (675, 100),
    26: (765, 100),
    27: (765, 180),
    28: (765, 260),
    29: (765, 340),
    30: (765, 425), 
    31: (765, 487),
    32: (765, 570)
}


# creating functions

def printboard():
    screen.blit(board, (0, 0))
    pygame.display.update()


def dochance(position):
    if position == 9 or position == 26:
        chanceon = True
        rollchance = 0
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 945, 693))
        chancet1 = endfont.render(chancetext1, True, (0, 0, 0))
        chancet2 = chancefont.render(chancetext2, True, (0, 0, 0))
        chancet3 = chancefont.render(chancetext3, True, (0, 0, 0))
        chancet4 = chancefont.render(chancetext4, True, (0, 0, 0))
        screen.blit(chancet1, (50, 175))
        screen.blit(chancet2, (50, 275))
        screen.blit(chancet3, (50, 325))
        screen.blit(chancet4, (50, 375))
        pygame.display.update()
        while chanceon == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key  == K_y:
                            rollchance = random.randint(1, 2)
                            if rollchance == 1:
                                if position == 9:
                                    printboard()
                                    return -2
                                elif position == 26:
                                    printboard()
                                    return -3
                            elif rollchance == 2:
                                if position == 9:
                                    printboard()
                                    return 2
                                elif position == 26:
                                    printboard()
                                    return 3        
                        elif event.key == K_n:
                            printboard()
                            return 0
    else:
        return 0 

def div3(divby3):
    divby3/=3.0
    return (divby3).is_integer()

def div2(divby2):
    divby2/=2.0
    return (divby2).is_integer()

def div4(divby4):
    divby4/=4.0
    return (divby4).is_integer()

def startscreen():
    starttext1 = startscreenfont.render(text1, True, (0, 0, 0))
    starttext2 = startscreenfont.render(text2, True, (0, 0, 0))
    starttext3 = startscreenfont.render(text3, True, (0, 0, 0))
    starttext4 = startscreenfont.render(text4, True, (0, 0, 0))
    starttext5 = startscreenfont.render(text5, True, (0, 0, 0))
    starttext6 = startscreenfont.render(text6, True, (0, 0, 0))
    starttext7 = startscreenfont.render(text7, True, (0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 945, 693))
    screen.blit(starttext1, (50, 225))
    screen.blit(starttext2, (50, 275))
    screen.blit(starttext3, (50, 325))
    screen.blit(starttext4, (50, 375))
    screen.blit(starttext5, (50, 425))
    screen.blit(starttext6, (50, 475))
    screen.blit(starttext7, (50, 525))
    pygame.display.update()

def endscreen(wintext):
    pygame.display.update()
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 945, 693))
    wintext1 = endfont.render(wintext + " won", True, (0, 0, 0))
    screen.blit(wintext1, (275, 250))
    pygame.display.update()
    pygame.time.wait(5000)
    pygame.display.quit()
    pygame.quit()
    sys.exit()
    sys.quit()

def redplayer(dicenum):
    if redtilenum < 32:
        screen.blit(redimg, poscoords[dicenum])
        pygame.display.update()
    elif redtilenum:
        screen.blit(redimg, poscoords[32])
        pygame.display.update()
        print("Game won by red")
        endscreen("Red")
        playinggame = False
    print(str(dicenum) + " red")

def yellowplayer(dicenum):
    if yellowtilenum < 32:
        screen.blit(yellowimg, poscoords[dicenum])
        pygame.display.update()
    elif yellowtilenum:
        screen.blit(yellowimg, poscoords[32])
        pygame.display.update()
        print("Game won by yellow")
        endscreen("Yellow")
        playinggame = False
    print(str(dicenum) + " yellow")

def greenplayer(dicenum):
    if greentilenum < 32:
        screen.blit(greenimg, poscoords[dicenum])
        pygame.display.update()
    elif greentilenum:
        screen.blit(greenimg, poscoords[32])
        pygame.display.update()
        print("Game won by green")
        endscreen("Green")
        playinggame = False
    print(str(dicenum) + " green")

def blueplayer(dicenum):
    chancenum = dochance(dicenum)
    dicenum+=chancenum
    if bluetilenum < 32:
        screen.blit(blueimg, poscoords[dicenum])
        pygame.display.update()
    elif bluetilenum:
        screen.blit(blueimg, poscoords[32])
        pygame.display.update()
        print("Game won by blue")
        endscreen("Blue")
        playinggame = False
    print(str(dicenum) + " blue")



def startgame():
    starting = True
    pygame.draw.circle(screen, (255, 0, 0), (472,346), 150)
    text = font.render("Click To ", True, (0, 0, 0))
    text2 = font.render("Start", True, (0, 0, 0))
    startscreen()
    screen.blit(text2, (400, 100))
    screen.blit(text, (360, 50))
    pygame.display.update()
    while starting == True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:    
                starting = False
                screen.blit(board, [0, 0])
                pygame.display.update()



def blueturn():
    global bluetilenum
    playerturn = True
    rolltimes = 50
    while playerturn == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    while rolltimes > 0:
                        playerrolled = random.randint(1, 6)
                        if playerrolled == 1:
                            screen.blit(dice1, [420, 346])
                        elif playerrolled == 2:
                            screen.blit(dice2, [420, 346])
                        elif playerrolled == 3:
                            screen.blit(dice3, [420, 346])
                        elif playerrolled == 4:
                            screen.blit(dice4, [420, 346])
                        elif playerrolled == 5:
                            screen.blit(dice5, [420, 346])
                        elif playerrolled == 6:
                            screen.blit(dice6, [420, 346])
                        rolltimes-=1
                        rolltext = rollfont.render("You rolled a " + str(playerrolled), True, (0, 0, 0))
                        screen.blit(rolltext, (355,300))
                        pygame.display.update()
                        pygame.time.wait(10)
                        screen.blit(board, (0, 0))
                        if rolltimes == 0:
                            bluetilenum+=playerrolled
                            pygame.time.wait(2500)
                            screen.blit(board, (0, 0))
                            pygame.display.update()
                            blueplayer(bluetilenum)
                            return "Hey Mr. Hare, the exit button won't work any other way so I just put this here :/"
    
    rolltext = rollfont.render("You rolled a " + str(playerrolled), True, (0, 0, 0))
    screen.blit(rolltext, (355,300))
    pygame.display.update()
    pygame.time.wait(5000)
    screen.blit(board, [0, 0])
    pygame.display.update()
    return "this is purely because the close function stops working if I don't do this, also hello Mr. Hare, sorry for the inefficient code."
                    
def greenturn():
    global greentilenum
    greenrolled = random.randint(1, 6)
    greentilenum+=greenrolled
    greenplayer(greentilenum)

def yellowturn():
    global yellowtilenum
    yellowrolled = random.randint(1, 6)
    yellowtilenum+=yellowrolled
    yellowplayer(yellowtilenum)

def redturn():
    global redtilenum
    redrolled = random.randint(1, 6)
    redtilenum+=redrolled
    redplayer(redtilenum)

def playgame():
    turn = 1
    while playinggame:
        if turn == 1:
            blueturn()
            print("blue went " + str(turn))
        elif turn == 3:
            yellowturn()
            print("yellow went " + str(turn))
        elif div2(turn-3) == True and div4(turn-3) == True:
            yellowturn()
            print("yellow went " + str(turn))
        elif div2(turn) == True and div4(turn) == True:
            greenturn() 
            print("green went " + str(turn))
        elif div4(turn) == False and div2(turn) == True:
            redturn()
            print("red went " + str(turn))
        else:
            blueturn()
            print("blue went " + str(turn))
        turn+=1




#calling functions for game for game

startgame()
playgame()
endgame()

# to quit

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
            pygame.display.quit()
            pygame.quit()
            exit()
            sys.exit()
            sys.quit()



pygame.display.flip()
