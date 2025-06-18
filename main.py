"""Info about the map."""
import os
from map import Map
#from character import Enemy

def clear_console():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')


#Directions
north = Map(" ")
north_east = Map(" ")
east = Map(" ")
south_east = Map(" ")
south = Map(" ")
south_west = Map(" ")
west = Map(" ")
north_west = Map(" ")


#Map/area objects
clear_console()
house = Map("Your home")
house.set_description("""You're currently having breakfast, until you hear the doorbell ring.
Go outside to check.""")

front_door = Map("Front door")
front_door.set_description("""As your open your front door, you notice no one except a map on
your doorstep, which leads to a unique cave. As a miner, you choose to follow the map and head
to your garage to prepare.""")

garage = Map("Your Garage")
garage.set_description("""You bring your torch, pickaxe, compass, and some food for your journey.
You then begin driving your ute to the designated cave.""")

def garage_move(_direction):
    """Handles movement from the garage to the cave entrance."""
    clear_console()
    return cave_entrance

garage.move = garage_move

cave_entrance = Map("The Cave Entrance")
cave_entrance.set_description("You exit your ute and walked into the cave entrance.")

cave = Map("The Cave")
cave.set_description("""You enter the cave and notice two ways:
                        - a dark tunnel directed forward (South)
                        - a small opening going left (East).""")

small_opening = Map("The Small Opening")
small_opening.set_description("""You proceed through the small opening and continue your
walk through the cave.""")

dark_tunnel = Map("The Dark Tunnel")
dark_tunnel.set_description("""You reached a dead end and found nothing else, go back and
turn left (East) instead.""")

two_ways = Map("Two Ways")
two_ways.set_description("""Your path has split to two. Which way will you go?
                         - Left (North East)
                         - Right (South)""")

left_way = Map("Left Way")
left_way.set_description("You have chosen the left way.")

two_ways2 = Map(" ")
two_ways2.set_description("""You have found another divided path,
                 - Forward (East)
                 - Right (South)""")






#blorpington = Enemy("Blorpington", "A Wumpus")
#blorpington.describe()
#blorpington.set_conversation("Greetings :)")
#blorpington.talk()
#blorpington.set_weakness("Glock")
#dungeon.set_character(blorpington)

house.link_areas(front_door, "South")
front_door.link_areas(garage, "East")
garage.link_areas(cave_entrance, "South")
cave_entrance.link_areas(cave, "South")
#Two ways in the cave
cave.link_areas(small_opening, "East")
cave.link_areas(dark_tunnel, "South")
dark_tunnel.link_areas(cave, "North") #back to cave
#Proceed through the small opening
small_opening.link_areas(south, "South")
south.link_areas(east, "East")
east.link_areas(two_ways, "West")
two_ways.link_areas(north, "North East")
north.link_areas(east, "North")
#east.link_areas(south, "East")
#south.link_areas(two_ways2, "South")


current_area = house
#dead = False
while True:
    print("\n")
    current_area.get_details()
    inhabitated = current_area.get_character()
    if inhabitated is not None:
        inhabitated.describe()
    command = input("> ")
    if command in ["North", "East", "South", "West", "North East", "North West",
                   "South East", "South West"]:
        current_area = current_area.move(command)
    elif command == "Cave":
        clear_console()
        current_area = cave

    #elif command == "Talk":
        #if inhabitated is not None:
            #inhabitated.talk()
    #elif command == "Fight":
        #if inhabitated is not None and isinstance(inhabitated, Enemy):
            #print("What do you want to fight with? ")
            #fight_with = input()
            #if inhabitated.fight(fight_with) is True:
                #print("Bravo, you win.")
                #current_cave.set_character(None)
            #else:
                #print("u lost the fight. ")
                #dead = True
        #else:
            #print("There is no one here to fight with.")
