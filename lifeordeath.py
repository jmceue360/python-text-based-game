#!/usr/bin/env python
import jsonpickle
import textwrap
import random
import time
import sys
import os


#Variables


SAVEGAME_FILENAME = 'savegame.json'

game_state = dict()


### Classes ###

class Human(object):
#Represents the human player in the game
    def __init__(self, name, health, strength, gold):
        self.name = name
        self.health = health
        self.strength = strength
        self.gold = gold

class AI(object):
#Represents the enemy player in the game
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength


class creature(object):
#Represents the enemy player in the game
    def __init__(self, type, name, health, strength, weakness):
        self.name = name
        self.health = health
        self.strength = strength


class Items:
    def __init__(self, name, info, weight):
        self.name = name
        self.info = info
        self.weight = weight

###end classess###

###functions for loading, saving, and initializing the game###
def load_game():
    """Load game state from a predefined savegame location and return the
    game state contained in that savegame.
    """
    with open(SAVEGAME_FILENAME, 'r') as savegame:
        state = jsonpickle.decode(savegame.read())
    return state


def save_game():
    """Save the current game state to a savegame in a predefined location.
    """
    global game_state
    with open(SAVEGAME_FILENAME, 'w') as savegame:
        savegame.write(jsonpickle.encode(game_state))


def init_game():
    """If no savegame exists, initialize the game state with some
    default values.
    """
    global game_state
    player = Human('Fred', 100, 10, 1000)
    enemy = AI('Imp', 50, 20)

    state = dict()
    state['players'] = [player]
    state['npcs'] = [enemy]
    return state

###End functions for loading, saving, and initalizing the game###


# Commands = {
#   'quit': Player.quit,
#   'help': Player.help,
#   'status': Player.status,
#   'rest': Player.rest,
#   'examine': Player.examine,
#   'attack': Player.attack,
#   }


def _clear():#clear screen function
    os.system('cls' if os.name == 'nt' else 'clear')

#The main game loop
def Game_Loop():

    global game_state

    while True:
        _clear()
        time.sleep(0.2)
        print("/:::::::::::::::::::::::::::::::::::::::\ ")
        print("::::::  Welcome To Life or Death  ::::::| ")
        print("::::::::::::::  The Game  ::::::::::::::|" )
        print("\:::::::::::::::::::::::::::::::::::::::/ ")
        print("")
        print("  |(1) New Game\n  |(2) Load Save\n  |(3) Help For Dummies\n  |(4) RAGE QUIT\n ")
        time.sleep(1.0)
        try:
            selection = int(input(">>> "))
        except ValueError:
            print()
            print("You can only use numbers 1, 2, 3, or 4.")
            print()
            _clear()
            Game_Loop()
        if selection == 1:
            _clear()
            init_game()
        elif selection == 2:
            _clear()
            load_game()
        elif selection == 3:
            _clear()
            help_menu()
        elif selection == 4:
            _clear()
            rage_quit()
        else:
            Game_Loop()


def help_menu():
    "Help Menu"
    _clear()
    print("""
                                  /~~~~~~~~~~~~~~~~~~~|
                                  |   Welcome To The  |
                                  |Help Menu For Noobs|
                                  |===================|
                                  |  (1) Main Menu    |
                                  |  (2) Extra Tips   |
                                  |===================|
                                  |01)
                                  |02)
                                  |03)
                                  |04)
                                  |05)
                                  |06)
                                  |07)
                                  |08)
                                  |09)
                                  |10)
                                  |11)
                                  |12)
                                  |13)
                                  |14)
                                  |15)
                                  |~~~~~~~~~~~~~~~~~~~/""")
    time.sleep(0.5)
    option = input('                                  --> ')
    if option == '1':
        main_menu()
    elif option == '2':
        hints()
    else:
        help_menu()


def rage_quit():
    "Quit Sequence"
    _clear()
    time.sleep(0.4)
    print("""
                                  /~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
                                  |  R  A  G  E    Q  U  I  T  |
                                  |  ^  ^  ^  ^    ^  ^  ^  ^  |
                                  |============================|
                                  |       (1)  Y E S   ?       |
                                  |       (2)   N O    ?       |
                                  |~~~~~~~~~~~~~~~~~~~~~~~~~~~~/""")
    time.sleep(1.0)
    option = input('                                  --> ')
    if option == '1':
        _clear()
        time.sleep(0.2)
        print("""
                                                  -
""")
        time.sleep(0.3)
        _clear()
        print("""
                                                  \
""")
        time.sleep(0.3)
        _clear()
        print("""
                                                  |
""")
        time.sleep(0.3)
        _clear()
        print("""
                                                  /
""")
        time.sleep(0.3)
        _clear()
        print("""
                                                  -
""")
        time.sleep(0.3)
        _clear()
        print("""
                                                  \
""")
        time.sleep(0.3)
        _clear()
        print("""
                                                  |
""")
        time.sleep(0.3)
        _clear()
        print("""
                                                  /
""")
        time.sleep(0.3)
        _clear()
        print("""
                                                  -
""")
        time.sleep(0.3)
        _clear()
        print("""
                                                  \
""")
        time.sleep(0.3)
        _clear()
        print("""
                                                  |
""")
        time.sleep(0.3)
        _clear()
        print("""
                                                  /
""")
        time.sleep(0.3)
        _clear()
        print("""
                                                  -
""")
        time.sleep(0.3)
        _clear()
        print("""
                                                  \
""")
        time.sleep(0.3)
        _clear()
        print("""
                                                  *
""")
        time.sleep(0.8)
        _clear()
        print("""
                            ###########################################
                            --------->[ W  A  R  N  I  N  G ]<---------
                            |  E M E R G E N C Y     S H U T D O W N  |
                                        | I M M I N E N T |
                            ###########################################

                                 [                                ]
                                                 0%
""")
        time.sleep(3.0)
        _clear()
        print("""
                            ###########################################
                            --------->[ W  A  R  N  I  N  G ]<---------
                            |  E M E R G E N C Y     S H U T D O W N  |
                                        | I M M I N E N T |
                            ###########################################

                                 [▆▆▆                             ]
                                                 5%
""")
        time.sleep(2.0)
        _clear()
        print("""
                            ###########################################
                            --------->[ W  A  R  N  I  N  G ]<---------
                            |  E M E R G E N C Y     S H U T D O W N  |
                                        | I M M I N E N T |
                            ###########################################

                                 [▆▆▆▆▆▆▆                          ]
                                                20%
""")
        time.sleep(5.0)
        _clear()
        print("""
                            ###########################################
                            --------->[ W  A  R  N  I  N  G ]<---------
                            |  E M E R G E N C Y     S H U T D O W N  |
                                        | I M M I N E N T |
                            ###########################################

                                 [▆▆▆▆▆▆▆▆▆▆▆▆▆                     ]
                                                 47%
""")
        time.sleep(4.0)
        _clear()
        print("""
                            ###########################################
                            --------->[ W  A  R  N  I  N  G ]<---------
                            |  E M E R G E N C Y     S H U T D O W N  |
                                        | I M M I N E N T |
                            ###########################################

                                 [▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆             ]
                                                 68%
""")
        time.sleep(5.0)
        _clear()
        print("""
                            ###########################################
                            --------->[ W  A  R  N  I  N  G ]<---------
                            |  E M E R G E N C Y     S H U T D O W N  |
                                        | I M M I N E N T |
                            ###########################################

                                 [▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆ ]
                                                99%
""")
        time.sleep(7.0)
        _clear()
        print("""
                            ###########################################
                            --------->[ W  A  R  N  I  N  G ]<---------
                            |  E M E R G E N C Y     S H U T D O W N  |
                                        | I M M I N E N T |
                            ###########################################

                                 [▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆]
                                                100%
""")
        time.sleep(2.0)
        _clear()
        print("""
                           ▆===`~!#44 ===== ▆▆ ▆▆▆=  ==▆====▆====▆▆\^^#!~) ======▆▆▆ ▆=== ====▆▆▆▆ ===    =▆  ▆▆▆
                           ▆▆▆ ▆▆747%*&}`67$^#% ▆▆▆▆▆▆  ▆E  R  R  O▆ R▆▆▆  4   0▆  4▆▆▆ ▆\   ▆▆▆ ▆▆455563dll▆▆
                               ▆▆▆  =   ▆▆▆ ▆     @@#   R%$%   ▆▆ ▆= ▆▆▆▆      ▆▆▆▆▆▆▆  ▆    ▆▆▆▆  ▆!!46i58i4▆▆▆
                            ▆▆  7t7r6t%^&**▆▆ S▆O C I▆A L  ▆  L I F E     N O▆T     F O▆U N D  ▆▆▆
                           =▆▆▆=▆▆▆▆=== ==▆▆=======   =====▆========= ===▆▆▆  ▆▆=====▆▆=▆▆▆▆▆  ▆▆▆▆▆▆=▆▆ ut▆▆r%^^8▆▆
""")
        time.sleep(4.5)
        print("                                  Thanks For Playing!!! :D      ")
        time.sleep(2.5)
        sys.exit()
    elif option == '2':
        main_menu()
    else:
        rage_quit()


def hints():
    "Extra Help Menu"
    print("""
                                  /~~~~~~~~~~~~~~~~~~~~~~~~~|
                                  |        More Help        |
                                  |        For Noobs        |
                                  |=========================|
                                  |      (1) Main Menu      |
                                  |=========================|
                                  |01)
                                  |02)
                                  |03)
                                  |04)
                                  |05)
                                  |06)
                                  |07)
                                  |08)
                                  |09)
                                  |10)
                                  |11)
                                  |12)
                                  |13)
                                  |14)
                                  |15)
                                  |~~~~~~~~~~~~~~~~~~~~~~~~/""")
    option = input('                                  --> ')
    if option == '1':
        main_menu()
    else:
        return


def title_pic():
    "Title Text Picture"
    _clear()
    time.sleep(1.5)
    print("""
                            :::8888888888888888888888888888888P""""""48888888888888888888888::::88
                            ::::8888888888888888888888P   ____.------.____   488888888888888:::888
                            ::::88888888888888888P __.--""    _._         ""--.__ 4888888888:::888
                            :::::888888888888P _.-"        .-~ | ~-.             "-._ 488888:::888
                            :::::888888888P _-"            |   |   |                 "-_ 488::8888
                            ::::::888888P ,'               |  _:_  |                    .-:~--.._8
                            8:::::88888 ,'            .  .-"~~ | ~~"-.                .~  |      |
                            88:::::88P /_.-~:.   .   :   |     |     |       .        |   |      |
                            888::::8P /|    | `.o    !   |     |     |        :       |   |      |
                            8P_..--~:-.|    |  |    d    |     |     | .       o      |   |      |
                            8|      |  ~.   |  |    o    |  __.:.__  | ;       b      |   |      |
                            8|      |   |   |  |   d8  .-"~~   |   ~~"-.o       8     |   |      |
                            8|      |   |  _|.--~:-98  |       |       |8b      8.:~-.|   |      |
                            8|      A   | |      |  ~. |       |   _.-:~--._   .' |   |   |      |
                            8|      M   | |      |   | |       |  |   |     |  |  |   |   |      |
                            8|      C   | |      |   | |       |  |   |     |  |  |   |   O      |
                            8|      |   | |      |   | |       |  |   |     |  |  |   |   j      |
                            8|      9   | |      |   | |       |  |   |     |  |  |   |   o      |
                            8|      9   | |      |   | |       |  |   |     |  |  |   |   |      |
                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
    time.sleep(6.0)
    Game_Loop()


def start():
    "Start story"
    _clear()
    choice1 = ''
    print("gg")


###End main game functions###

###The "main" function, not to be confused with anything to do with main above it###
def main():
    """Main function. Check if a savegame exists, and if so, load it. Otherwise
    initialize the game state with defaults. Finally, start the game.
    """
    global game_state

    if not os.path.isfile(SAVEGAME_FILENAME):
        game_state = initialize_game()
    else:
        game_state = load_game()
    Game_Loop()


if __name__ == '__main__':
    main()

###end main function###


title_pic()
