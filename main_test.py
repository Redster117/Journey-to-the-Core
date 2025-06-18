"""Info about the map."""
import os
from map import Map

def clear_console():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')


#Directions (These directions are disabled as it causes issues with the map)
#Remember to copy one of these directions and paste them in the map objects
#If using more than one direction, make sure to number each one as you go to avoid more errors.
#north = Map(" ")
#north_east = Map(" ")
#east = Map(" ")
#south_east = Map(" ")
#south = Map(" ")
#south_west = Map(" ")
#west = Map(" ")
#north_west = Map(" ")

#left_way = Map("Left way")
#left_way.set_description("You have chosen the left way.")

#right_way = Map("Right way")
#right_way.set_description("You have chosen the right way.")

#two_ways = Map(" ")
#two_ways.set_description("""Your path has split to two. Which way will you go?
                        # - Any direction eg. Right (Any cardinal/ordinal direction)
                        # - Any direction eg. Left (Any cardinal/ordinal direction)""")


#Map/area objects
clear_console()
cave = Map("The Cave")
cave.set_description("""You enter the cave and notice two paths:
                        - a dark tunnel directed forward (South)
                        - a small opening going left (East).""")

dark_tunnel = Map("The Dark Tunnel")
dark_tunnel.set_description("""You reached a dead end and found nothing else, go back to
your previous position and try again.""")

small_opening = Map("The Small Opening")
small_opening.set_description("""You proceed through the small opening and continue your
walk through the cave.""")

south = Map("You went South")
south.set_description("Next direction, East")

east = Map("You went East")


two_ways = Map(" ")
two_ways.set_description("""Your path has split to two. Which way will you go?
                            Currently facing: East
                         - Left (North East)
                         - Right (South)""")

north_east = Map("North East")

north = Map("North")

east2 = Map("East")

south2 = Map("South")

two_ways2 = Map(" ")
two_ways2.set_description("""You have found another divided path!
                          Currently Facing: East
                 - Forward (East)
                 - Right (South)""")

south3 = Map("South")
south3.set_description("You have stumbled upon a dead end. Go back and choose another path.")


#Two ways in the cave
cave.link_areas(small_opening, "East")
cave.link_areas(dark_tunnel, "South")
dark_tunnel.link_areas(cave, "North") #Back to cave
#Proceed through the small opening
small_opening.link_areas(south, "South")
south.link_areas(east, "East")
east.link_areas(two_ways, "West")
two_ways.link_areas(north, "North East")


current_area = cave
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
