#!/usr/bin/env python
import random
import pickle
import time
import sys
import os


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0








def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    "Main Menu Screen"
    _clear()
    time.sleep(0.2)
    print("                                  /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| ")
    print("                                  |    Welcome To Life or Death    | ")
    print("                                  |            The Game            | ")
    print("                                  |================================| ")
    print("                                  |    (1) Start the 'GAME'        | ")
    print("                                  |    (2) Load Your Save          | ")
    print("                                  |    (3) Help For Dummies        | ")
    print("                                  |    (4) RAGE QUIT               | ")
    print("                                  |================================| ")
    print("                                  |        Pick a Number           | ")
    print("                                  |================================| ")
    print("                                  |  Copyright 2018 Jakob Mceuen   | ")
    print("                                  |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/ ")
    time.sleep(1.0)
    option = input('                                  --> ')
    if option == '1':
        play()
    elif option == '2':
        main_menu()
    elif option == '3':
        _clear()
        help_menu()
    elif option == '4':
        rage_quit()
    else:
        main_menu()


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
    main_menu()


def load():
    "Load Save"
    _clear()
    print('Function not added YET...')



def play():
    "starting start"
    _clear()
    option = input("'Start a New Save'[y/n] ----> ")
    if option == 'y':
        start()
    elif option == 'Y':
        start()
    elif option == 'yes':
        start()
    elif option == 'Yes':
        start()
    elif option == 'YES':
        start()
    elif option == 'n':
        main_menu()
    elif option == 'N':
        main_menu()
    elif option == 'no':
        main_menu()
    elif option == 'No':
        main_menu()
    elif option == 'NO':
        main_menu()
    elif option == '/':
        load()
    else:
        return option


def start():
    "Start story"
    _clear()
    option == ('ch') + ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    print("You suddenly awaken with a huge migrane and realize you are strapped to a gurney...")
    ch1 = input 



title_pic()
