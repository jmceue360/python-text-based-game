#!/usr/bin/env python
import time
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    """Main Menu Screen"""
    os.system('cls')
    print """
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                              Welcome To EARTH-2086:                                          |
|                                                 A New Beginning                                              |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                (1) Start Your New Life                                       |
|                                                (2) Load Your Save                                            |
|                                                (3) Help For Dummies                                          |
|                                                (4) RAGE QUIT                                                 |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                  Pick a Number                                               |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                             Copyright 2018 Jakob Mceuen                                      |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"""
    option = raw_input('-----> ')
    if option == '1':
        cutscene()
    elif option == '2':
        main_menu()
    elif option == '3':
        os.system('cls')
        help_menu()
    elif option == '4':
        rage_quit()
    else:
        main_menu()


def help_menu():
    """Help Menu"""
    os.system('cls')
    print"""
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                             Welcome To The                                                  |
|                                          Help Menu For Noobs                                                |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|01)                                                                                                          |
|02)                                                                                                          |
|03)                                                                                                          |
|04)                                                                                                          |
|05)                                                                                                          |
|06)                                                                                                          |
|07)                                                                                                          |
|08)                                                                                                          |
|09)                                                                                                          |
|10)                                                                                                          |
|11)                                                                                                          |
|12)                                                                                                          |
|13)                                                                                                          |
|14)                                                                                                          |
|15)                                                                                                          |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|==============================|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                       |(1) Main Menu  (2) Extra Hints|                                      |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|==============================|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"""
    option = raw_input('-----> ')
    if option == '1':
        main_menu()
    elif option == '2':
        hints()
    else:
        help_menu()


def rage_quit():
    """Quit Game"""
    os.system('cls')
    print """
|===========================================================================================================|
|                                                |Rage Quit?|                                               |
|===========================================================================================================|
|                                                  (1) YES?                                                 |
|                                                  (2) NO?                                                  |
|===========================================================================================================|"""
    option = raw_input('-----> ')
    if option == '1':
        sys.exit()
    elif option == '2':
        main_menu()
    else:
        rage_quit()


def hints():
    """Extra Help Menu"""
    print """
|==========================================================================================================|
|                                                  Extra Help                                              |
|                                                  For Noobs                                               |
|==========================================================================================================|
|01)                                                                                                       |
|02)                                                                                                       |
|03)                                                                                                       |
|04)                                                                                                       |
|05)                                                                                                       |
|06)                                                                                                       |
|07)                                                                                                       |
|08)                                                                                                       |
|09)                                                                                                       |
|10)                                                                                                       |
|11)                                                                                                       |
|12)                                                                                                       |
|13)                                                                                                       |
|14)                                                                                                       |
|15)                                                                                                       |
|=========================================|=============|==================================================|
|                                         |(1) Main Menu|                                                  |
|=========================================|=============|==================================================|"""
    option = raw_input('-----> ')
    if option == '1':
        main_menu()
    else:
        hints()


def load():
    """Load Save"""
    os.system('cls')
    print "hi"


def cutscene():
    """Story Start"""
    os.system('cls')
    story_pic_1()


def char_create():
    """Character Create"""
    print "      Are you a Male or a Female?"


def play():
    """Gameplay Start"""
    os.system('cls')
    print "WHATS UP DUDE! NOT FINISHED YET!"


def title_pic():
    """Title Text Picture"""
    os.system('cls')
    time.sleep(1.5)
    print """
=====================================================================================================================================
    EEEEEEEEEEEEEEEEEEEEEE               AAA               RRRRRRRRRRRRRRRRR   TTTTTTTTTTTTTTTTTTTTTTTHHHHHHHHH     HHHHHHHHH
    E::::::::::::::::::::E              A:::A              R::::::::::::::::R  T:::::::::::::::::::::TH:::::::H     H:::::::H
    E::::::::::::::::::::E             A:::::A             R::::::RRRRRR:::::R T:::::::::::::::::::::TH:::::::H     H:::::::H
    EE::::::EEEEEEEEE::::E            A:::::::A            RR:::::R     R:::::RT:::::TT:::::::TT:::::THH::::::H     H::::::HH
      E:::::E       EEEEEE           A:::::::::A             R::::R     R:::::RTTTTTT  T:::::T  TTTTTT  H:::::H     H:::::H
      E:::::E                       A:::::A:::::A            R::::R     R:::::R        T:::::T          H:::::H     H:::::H   ::::::
      E::::::EEEEEEEEEE            A:::::A A:::::A           R::::RRRRRR:::::R         T:::::T          H::::::HHHHH::::::H   ::::::
      E:::::::::::::::E           A:::::A   A:::::A          R:::::::::::::RR          T:::::T          H:::::::::::::::::H   ::::::
      E:::::::::::::::E          A:::::A     A:::::A         R::::RRRRRR:::::R         T:::::T          H:::::::::::::::::H
      E::::::EEEEEEEEEE         A:::::AAAAAAAAA:::::A        R::::R     R:::::R        T:::::T          H::::::HHHHH::::::H
      E:::::E                  A:::::::::::::::::::::A       R::::R     R:::::R        T:::::T          H:::::H     H:::::H
      E:::::E       EEEEEE    A:::::AAAAAAAAAAAAA:::::A      R::::R     R:::::R        T:::::T          H:::::H     H:::::H   ::::::
    EE::::::EEEEEEEE:::::E   A:::::A             A:::::A   RR:::::R     R:::::R      TT:::::::TT      HH::::::H     H::::::HH ::::::
    E::::::::::::::::::::E  A:::::A               A:::::A  R::::::R     R:::::R      T:::::::::T      H:::::::H     H:::::::H ::::::
    E::::::::::::::::::::E A:::::A                 A:::::A R::::::R     R:::::R      T:::::::::T      H:::::::H     H:::::::H
    EEEEEEEEEEEEEEEEEEEEEEAAAAAAA                   AAAAAAARRRRRRRR     RRRRRRR      TTTTTTTTTTT      HHHHHHHHH     HHHHHHHHH
=====================================================================================================================================
                        222222222222222         000000000          888888888             66666666
                        2:::::::::::::::22     00:::::::::00      88:::::::::88          6::::::6
                        2::::::222222:::::2  00:::::::::::::00  88:::::::::::::88       6::::::6
                        2222222     2:::::2 0:::::::000:::::::08::::::88888::::::8     6::::::6
                                    2:::::2 0::::::0   0::::::08:::::8     8:::::8    6::::::6
                                    2:::::2 0:::::0     0:::::08:::::8     8:::::8   6::::::6
                                 2222::::2  0:::::0     0:::::0 8:::::88888:::::8   6::::::6
                            22222::::::22   0:::::0 000 0:::::0  8:::::::::::::8   6::::::::66666
                          22::::::::222     0:::::0 000 0:::::0 8:::::88888:::::8 6::::::::::::::66
                         2:::::22222        0:::::0     0:::::08:::::8     8:::::86::::::66666:::::6
                        2:::::2             0:::::0     0:::::08:::::8     8:::::86:::::6     6:::::6
                        2:::::2             0::::::0   0::::::08:::::8     8:::::86:::::6     6:::::6
                        2:::::2       2222220:::::::000:::::::08::::::88888::::::86::::::66666::::::6
                        2::::::2222222:::::2 00:::::::::::::00  88:::::::::::::88  66:::::::::::::66
                        2::::::::::::::::::2   00:::::::::00      88:::::::::88      66:::::::::66
                        22222222222222222222     000000000          888888888          666666666
                    ===================================================================================="""
    time.sleep(5.0)

def story1():
    os.system('cls')
    time.sleep(0.5)
    print """  In 2018 President Donald Trump confronted Kim Jong Un, leader of North Korea about his nuclear program  """

    time.sleep(1.0)
    option = raw_input('Continue?[Yes/No]---> ')
    if option == 'yes':
        story2()
    elif option == 'Yes':
        story2()
    elif option == 'YES':
        story2()
    elif option == 'no':
        main_menu()
    elif option == 'No':
        main_menu()
    elif option == 'NO':
        main_menu()
    else:
        story1()


def story2():
    os.system('cls')
    time.sleep(0.5)
    print """  Things were going fine for a couple of years of the two leaders working together against Russia"""

    time.sleep(1.0)
    option = raw_input('Continue?[Yes/No]---> ')
    if option == 'yes':
        story3()
    elif option == 'Yes':
        story3()
    elif option == 'YES':
        story3()
    elif option == 'no':
        main_menu()
    elif option == 'No':
        main_menu()
    elif option == 'NO':
        main_menu()
    else:
        story2()


def story3():
    os.system('cls')
    time.sleep(0.5)
    print """IM NOT DONE WITH THE WHOLE STORY YET!"""

    time.sleep(1.0)
    option = raw_input('Continue?[Yes/No]---> ')
    if option == 'yes':
        menu_menu()
    elif option == 'Yes':
        main_menu()
    elif option == 'YES':
        main_menu()
    elif option == 'no':
        sys.exit()
    elif option == 'No':
        sys.exit()
    elif option == 'NO':
        sys.exit()
    else:
        story3()


title_pic()
clear_screen()
main_menu()
