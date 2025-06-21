"""Info about the map."""
import os
from map import Map


def clear_console():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_compass(current_direction):
    """Print an 8-point compass highlighting the current direction."""
    RESET = "\033[0m"
    HIGHLIGHT = "\033[93m"  # Yellow color code

    def mark(direction_name):
        """Highlight the direction if it matches current_direction."""
        if direction_name == current_direction:
            return f"{HIGHLIGHT}{direction_name}{RESET}"
        return direction_name

    print()
    print("        " + mark("North"))
    print("   " + mark("North West") + "       " + mark("North East"))
    print(mark("West") + "       (You)       " + mark("East"))
    print("   " + mark("South West") + "       " + mark("South East"))
    print("        " + mark("South"))
    print()


# Map/area objects
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

south = Map(" ")

east = Map(" ")


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
south3.set_description("""You have stumbled upon a dead end. Go back and
choose another path.""")


# Two ways in the cave
cave.link_areas(small_opening, "East")
cave.link_areas(dark_tunnel, "South")
dark_tunnel.link_areas(cave, "North")  # Back to cave
# Proceed through the small opening
small_opening.link_areas(south, "South")
south.link_areas(east, "East")
east.link_areas(two_ways, "West")
two_ways.link_areas(north, "North East")


current_area = cave
last_direction = None  # Variable tracking current facing direction

directions = [
    "North", "East", "South", "West",
    "North East", "North West", "South East", "South West"
]

while True:
    print("\n")
    current_area.get_details()

    # Update facing direction if current area is a direction node
    if current_area.get_name().strip() in directions:
        last_direction = current_area.get_name().strip()

    command = input("> ").strip()

    if command.upper() == "M":
        if last_direction:
            print_compass(last_direction)
        else:
            print("You are not currently facing any direction.")
        continue

    if command in directions:
        current_area = current_area.move(command)
