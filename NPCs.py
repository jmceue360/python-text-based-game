import random


#Type Classes
class Hero:
    def __init__(self, name):
                self.name = name
                self.maxhealth = 300
                self.health = 100
                self.maxarmor = 250
                self.armor = 0
                self.base_attack = 5
                self.hunger = 100
                self.thirst = 100
                self.money = 10000000000000
                self.salary = 1000000
                self.meds = 3
                self.saying1 = ""
                self.saying2 = ""
                self.weap = ["Randomness"]
                self.curweap = ["Randomness"]
                self.driverslicense = False
                self.home = False
                self.fleechance = False
                self.sickness = False


class Villain:
    def __init__(self, name):
                self.name = name
                self.maxhealth = 500
                self.health = 150
                self.maxarmor = 400
                self.armor = 10
                self.base_attack = 5
                self.hunger = 100
                self.thirst = 100
                self.money = 10000000000000
                self.salary = 1000000
                self.meds = 3
                self.saying1 = ""
                self.saying2 = ""
                self.weap = ["Randomness"]
                self.curweap = ["Randomness"]
                self.driverslicense = False
                self.home = False
                self.fleechance = False
                self.sickness = False


####-Logic
# def typerandomizer():
#     global typepick
#     random.choice(typepick)
#     typepick = ['N', 'H', 'V']
#     if typepick == 'N':
#         normalplayer()
#     elif typepick == 'H':
#         heroplayer()
#     elif typepick == 'V':
#         villainplayer()
#
# def normalplayer():
#     global playerig
#
#     random.choice(playerig)
#     playerig = ['Normal', 'Hero', 'Villain']
#
#
# def heroplayer():
#     global playerig
#     random.choice(playerig)
#     playerig = ['Normal', 'Hero', 'Villain']
#
#
# def villainplayer():
#     global playerig
#     random.choice(playerig)
#     playerig = ['Normal', 'Hero', 'Villain']


######-NPC_NAMES
def gender():
    global gendernpc
    random.choice(gendernpc)
    gendernpc = ['male_npc', 'female_npc']
    if gendernpc == 'male_npc':
        male()
    elif gendernpc == 'female_npc':
        female()


def male():
    global malenpcnames
    while gender == 'male_npc':
      random.choice(malenpcnames)
      malenpcnames = ['Jacob', 'Liam', 'Kyle', 'Noah', "Bob", "Sean", "Marcus", "Micheal", 'Mike', "Jeff", "Owen", "Jayden", "William", "James",
                "Logan", "Benjamin", "Mason", "Elijah", "Oliver", "Lucas", "Alexander", "Ethan","Luke", 'Daniel', "Matthew", "Aiden","Henry",
                "Joseph", "Jackson", "Samuel", "Sebastian", "David", "Wyatt","John"]


def female():
    global femalenpcnames
    while gender == 'female_npc':
      random.choice(femalenpcnames)
      femalenpcnames = ["Angel", "Emma", "Samantha", "Sabrina", "Sally", "Debbie", "Jasmine", "Layla", "Nora", "Zoey","Lilly","Mila", "Luna",
                  "Olivia", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia", "Evelyn", "Abigail", "Harper", "Emily","Penelope",
                  'Elizabeth', "Avery", "Riley", "Sofia", "Ella", "Madison", "Scarlett", "Victoria", "Grace", "Chloe", "Camila"]


#####-PLAYER_NAMES
def gender_ig():
    global genderig
    random.choice(genderig)
    genderig = ['male_ig', 'female_ig']
    if genderig == 'male_ig':
        Male()
    elif genderig == 'female_ig':
        Female()


def Male():
    global maleig_names
    while gender == 'male_ig':
      Mname = raw_input(random.choice(maleig_names))
      maleig_names = ["Jacob", "Liam", "Kyle", "Noah", "Bob", "Sean", "Marcus", "Micheal", 'Mike', "Jeff", "Owen", "Jayden",
                "William", "James", "Logan", "Benjamin", "Mason", "Elijah", "Oliver", "Lucas", "Alexander", "Ethan","Luke",
                'Daniel', "Matthew", "Aiden", "Henry", "Joseph", "Jackson", "Samuel", "Sebastian", "David", "Wyatt", "John"]

def Female():
    global femaleig_names
    while gender == 'female_ig':
      random.choice(femaleig_names)
      femaleig_names = ["Angel", "Emma", "Samantha", "Sabrina", "Sally", "Debbie", "Jasmine", "Layla", "Nora", "Zoey", "Lilly","Mila", "Luna",
                  "Olivia", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia", "Evelyn", "Abigail", "Harper", "Emily", "Penelope",
                  'Elizabeth', "Avery", "Riley", "Sofia", "Ella", "Madison", "Scarlett", "Victoria", "Grace", "Chloe", "Camila"]


####-NPC&PLAYER
class Character:
    def __init__(self, name):
        assert isinstance(name, object)
        self.name = name
        self.maxhealth = 200
        self.health = 100
        self.maxarmor = 250
        self.armor = 0
        self.base_attack = 1
        self.maxhunger = 100
        self.hunger = 0
        self.maxthirst = 100
        self.thirst = 0
        self.maxmoney = 10000000000000
        self.money = 0
        self.meds = 5
        self.saying1 = ""
        self.saying2 = ""
        self.weap = ["Fists"]
        self.curweap = ["Fists"]
        self.driverslicense = False
        self.home = False
        self.fleechance = False
        self.sickness = False


class Player(Character):
    global genderig
    def __init__(self, name):
        Character.__init__(self, name)
        self.name = gender_ig
        self.maxhealth = 200
        self.health = 100
        self.maxarmor = 250
        self.armor = 0
        self.base_attack = 1
        self.maxhunger = 100
        self.hunger = 0
        self.maxthirst = 100
        self.thirst = 0
        self.money = 0
        self.meds = 0
        self.weap = ["Fists"]
        self.curweap = ["Fists"]
        self.driverslicense = False
        self.home = True
        self.homeType = "Parent's Basement"
        self.fleechance = False
        self.sickness = False


class NPC(Character):
    global gendernpc
    def __init__(self, name):
        Character.__init__(self, name)
        self.name = gendernpc
        self.type = [people_dict, authorities_dict, animals_dict, shops_dict]
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.hunger = 0
        self.gold = 40
        self.meds = 0
        self.saying1 = ""
        self.saying2 = ""


####-Authorities
def randomnpcs():
    global people_dict
    people_dict = {"Neigbor": {"name": "random.name", "gender": "random.choice()", "health": 30, "attack": 20},
                    "Villager": {"name": "random.name", "gender": "random.choice()", "health": 50, "attack": 30},
                    "Homeless": {"name": "random.name", "gender": "random.choice()", "health": 60, "attack": 40},
                    "Business person": {"name": "random.name", "health": 20, "attack": 50},
                    "Druggie": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "Child": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "Teen": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "Parent/Guardian": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "Russian": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "German": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "French": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "Mime": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "American": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "Japanese": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "Chinese": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "Korean": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "Indian": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "Gamer": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "Youtuber": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "Celebrity": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "Musician": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "Common person": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                    "Rich person": {"name": "random.name", "gender": "random.choice()", "health": 20, "attack": 50}}


####-Authorities
def authorities():
    global authorities_dict
    authorities_dict = {"Police": {"name": "random.name", "gender": "random.choice()", "health": 30, "attack": 20},
                        "SWAT team": {"name": "random.name", "gender": "random.choice()", "health": 50, "attack": 30},
                        "Military": {"name": "random.name", "gender": "random.choice()", "health": 60, "attack": 40},
                        "The President": {"name": "random.name", "health": 20, "attack": 50},
                        "FBI-agent": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                        "Government official": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                        "Mayor": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                        "National Security": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                        "Secret Service": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                        "CIA-agent": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                        "Detective": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                        "Congress": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                        "Pawn-shop": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                        "Pawn-shop": {"name": "random.name", "gender": "random.choice()", "health": 10, "attack": 20},
                        "": {"name": "random.name", "gender": "random.choice()", "health": 20, "attack": 50}}


####-Animals
def pets():
    global animals_dict
    animals_dict = {"Dog": {"name": "random.name", "health": 20, "attack": 5},
                    "Cat": {"name": "random.name", "health": 10, "attack": 20},
                    "Turtle": {"name": "random.name", "health": 10, "attack": 20},
                    "Monkey": {"name": "random.name", "health": 10, "attack": 20},
                    "Gerbil": {"name": "random.name", "health": 10, "attack": 20},
                    "Hamster": {"name": "random.name", "health": 10, "attack": 20},
                    "Mouse": {"name": "random.name", "health": 10, "attack": 20},
                    "Fish": {"name": "random.name", "health": 10, "attack": 20},
                    "Horse": {"name": "random.name", "health": 10, "attack": 20},
                    "Pony": {"name": "random.name", "health": 10, "attack": 20},
                    "Creepy Crawly": {"name": "random.name", "health": 10, "attack": 20},
                    "Spider": {"name": "random.name", "health": 10, "attack": 20},
                    "Lizard": {"name": "random.name", "health": 10, "attack": 20},
                    "Bird": {"name": "random.name", "health": 100, "attack": 10}}

####-NPCshops
def traders():
    global shops_dict
    shops_dict = {"Real Estate": {"name": "Imp", "health": 20, "attack": 5},
                  "Pawn shop": {"name": "random.name", "health": 10, "attack": 20},
                  "Tech store": {"name": "random.name", "health": 10, "attack": 20},
                  "Pet-Supply Deluxe": {"name": "random.name", "health": 10, "attack": 20},
                  "The Great Mall": {"name": "random.name", "health": 10, "attack": 20},
                  "Convienence store": {"name": "random.name", "health": 10, "attack": 20},
                  "Gift-shop": {"name": "random.name", "health": 10, "attack": 20},
                  "Candy store": {"name": "random.name", "health": 10, "attack": 20},
                  "Pet store": {"name": "random.name", "health": 10, "attack": 20},
                  "The Pound": {"name": "random.name", "health": 10, "attack": 20},
                  "Restaurant": {"name": "random.name", "health": 10, "attack": 20},
                  "Pawn-shop": {"name": "random.name", "health": 10, "attack": 20},
                  "Pawn-shop": {"name": "random.name", "health": 10, "attack": 20},
                  "food-market": {"name": "Orge", "health": 100, "attack": 10}}

class trader:
    def __init__(self, specialty, items):
        self.specialty


####-Baddies
def badpeople():
    global baddies_dict
    baddies_dict = {"ISIS Member": {"name": "random.name", "health": 20, "attack": 5},
                    "Theif": {"name": "random.name", "health": 10, "attack": 20},
                    "Hitman": {"name": "random.name", "health": 10, "attack": 20},
                    "Mercenaries": {"name": "random.name", "health": 10, "attack": 20},
                    "Demonic cult": {"name": "random.name", "health": 10, "attack": 20},
                    "Gang member": {"name": "random.name", "health": 10, "attack": 20},
                    "Crime Boss": {"name": "random.name", "health": 10, "attack": 20},
                    "Terrorist": {"name": "random.name", "health": 10, "attack": 20},
                    "Drug Dealer": {"name": "random.name", "health": 10, "attack": 20},
                    "Scammer": {"name": "random.name", "health": 10, "attack": 20},
                    "": {"name": "random.name", "health": 10, "attack": 20},
                    "Pawn-shop": {"name": "random.name", "health": 10, "attack": 20},
                    "Pawn-shop": {"name": "random.name", "health": 10, "attack": 20},
                    "Pawn-shop": {"name": "random.name", "health": 10, "attack": 20},
                    "Ogre": {"name": "Orge", "health": 100, "attack": 10}}

####-Heroes
def heroes():
    global heroes_dict
    heroes_dict = {"Spooderman": {"Type": "Hero", "gender": "Male", "health": 30, "attack": 20},
                   "Spiderpig": {"Type": "Hero", "gender": "random.choice()", "health": 50, "attack": 30},
                   "Dankpool": {"Type": "Hero", "gender": "random.choice()", "health": 60, "attack": 40},
                   "Aquakid": {"Type": "Hero", "health": 20, "attack": 50},
                   "Docter Cringe": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "Captain Communist": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "White Panther": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "The Crimson Stain": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "The Thingy": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "Jo Mama": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "The Incredible-Edible-Egghead": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "Dolphin Lad": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "The Turkish Turd": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "Captain Spunky": {"name": "random.", "gender": "random.choice()", "health": 10, "attack": 20},
                   "Random-Man": {"Type": "Hero", "gender": "random.choice()", "health": 20, "attack": 50},
                   "Captain Hurt-You": {"Type": "Hero", "gender": "random.choice()", "health": 50, "attack": 30},
                   "The Incredible Thimble": {"Type": "Hero", "gender": "random.choice()", "health": 60, "attack": 40},
                   "Mr. Potato Head": {"Type": "Hero", "health": 20, "attack": 50},
                   "The Spanker and his sidekick, Monkey Boy": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "Stretch Dude": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "Clobber Girl": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "Transmaster": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "Sir Dumps-a-lot": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "The Man-purse": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "Three Fingered McGee": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "Basement Bobby": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "Dr Three Legs": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "The Fist": {"Type": "Hero", "gender": "random.choice()", "health": 10, "attack": 20},
                   "Squirrel Girl": {"Type": "Hero", "gender": "random.choice()", "health": 20, "attack": 50}}

####-Villains
def villains():
    global villians_dict
    villians_dict = {"The Tapeinator": {"Type": "Villain", "gender": "Male", "health": 30, "attack": 20},
                     "The Midnight Man": {"Type": "Villain", "gender": "random.choice()", "health": 50, "attack": 30},
                     "Obsidian Gal": {"name": "Villain", "gender": "random.choice()", "health": 60, "attack": 40},
                     "Decay Man": {"Type": "Villain", "health": 20, "attack": 50},
                     "Viruscide": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Death Angel": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Dr. Overkill": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Hellfury The Fallen": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Shadowclaw": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Furyfire The Terrifying": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Terrorthought The Shredder": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Slylure The Ressurected": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Seekermaw The Worm-ridden": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Fangwire": {"name": "random.", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Deathflare The Cremator": {"Type": "Villain", "gender": "random.choice()", "health": 20, "attack": 50},
                     "Aquafear The Mystic": {"Type": "Villain", "gender": "random.choice()", "health": 50, "attack": 30},
                     "Cursethorn The Slimy": {"Type": "Villain", "gender": "random.choice()", "health": 60, "attack": 40},
                     "Blazedart The Sorcerous": {"Type": "Villain", "health": 20, "attack": 50},
                     "Arclove The Eater": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Dashshade": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Charnelterror The Crusher": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Blastgut The Ruler": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Tombshiver The Foul": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Firedrip": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Wavechain The Haunter": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Carnaldamn The Undying": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Magicsludge The Master": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Nailblaze The Toxic": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Dr. Venom": {"Type": "Villain", "gender": "random.choice()", "health": 10, "attack": 20},
                     "Charmsnare The Skeletal": {"Type": "Villain", "gender": "random.choice()", "health": 20, "attack": 50}}
