"""Info about the map."""
import os
from map import Map


def clear_console():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')


# ANSI color codes for highlighting (only works in supported terminals)
RESET = "\033[0m"
HIGHLIGHT = "\033[93m"  # Yellow


def print_compass(current_direction=None):
    """Prints a compass with 8 directions. Highlights current direction if given."""

    def mark(direction):
        return (
            f"{HIGHLIGHT}{direction}{RESET}"
            if direction == current_direction else direction
        )

    print("\nCompass:")
    print(f"    {mark('North West')}  {mark('North')}  {mark('North East')}")
    print(f"    {mark('West')}          ◉          {mark('East')}")
    print(f"    {mark('South West')}  {mark('South')}  {mark('South East')}\n")


def print_ascii_map(current_area, discovered_areas):
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    def area_block(name):
        if name == current_area.get_name():
            return f"{YELLOW}{name[:15].center(15)}{RESET}"
        elif name in discovered_areas:
            return name[:15].center(15)
        else:
            return " " * 15

    grid = [
        " " * 40 + "JOURNEY TO THE CORE - LEVEL 1 MAP",
        "",
        area_block("House") + " → " + area_block("Front Door") + " → " + area_block("Garage") + " → " + area_block("Cave Entrance"),
        " " * 32 + "↓",
        area_block("The Cave"),
        " " * 32 + "↓",
        area_block("The Dark Tunnel"),
        " " * 32 + "↓",
        area_block("The Small Opening"),
        " " * 32 + "↓",
        area_block("Southern Tunnel 1"),
        " " * 32 + "↓",
        area_block("First Split"),
        " " * 28 + "/           \\",
        area_block("North East Corridor") + "     " + area_block("Eastern Corridor 2"),
        "     ↓                          ↓",
        area_block("Northern Tunnel") + "     " + area_block("Southern Tunnel 2"),
        "     ↓                          ↓",
        area_block("Eastern Corridor 1") + "     " + area_block("West Corridor"),
        "     ↓                          ↓",
        area_block("Second Split") + "     " + area_block("North Corridor"),
        "     ↓                          ↓",
        area_block("Deeper Cave") + "     " + area_block("Dead End"),
    ]

    print("\n" + "\n".join(grid))
    print("\nLegend: Yellow = Current Location | Hidden = Undiscovered")


# Map/area objects
clear_console()

# Area 1: Cave
cave = Map("The Cave")
cave.set_description("""You enter the cave and notice two paths:
                        - a dark tunnel directed forward (South)
                        - a small opening going left (East).""")

# Area 2: Dark Tunnel
dark_tunnel = Map("The Dark Tunnel")
dark_tunnel.set_description("""You reached a dead end and found nothing else.
Go back to your previous position and try again.""")

# Area 3: Small Opening
small_opening = Map("The Small Opening")
small_opening.set_description("""You proceed through the small opening and continue your
walk through the cave.""")

# Area 4: First Southern Tunnel after east_corridor_1
southern_tunnel_1 = Map("Southern Tunnel 1")

# Area 5: Fork - Two Ways
two_way_fork_1 = Map("First Split")
two_way_fork_1.set_description("""Your path has split to two. Which way will you go?
                            Hint: Enter N to see your current facing direction.
                            Hint: Enter M to reveal a compass
                         - Left (North East)
                         - Right (South)""")

# Area 6: South Corridor
south_corridor = Map("South Corridor")

# Area 7: East Corridor from South
eastern_corridor_2 = Map("Eastern Corridor 2")

# Area 8: Southern Tunnel 2
southern_tunnel_2 = Map("Southern Tunnel 2")

# Area 9: West Corridor
west_corridor = Map("West Corridor")

# Area 10: North Corridor
north_corridor = Map("North Corridor")

# Area 11: Dead End
northern_dead_end = Map("Dead End")
northern_dead_end.set_description("""You have reached a dead end, return to the last
point you came from to continue your journey.""")

# Area 12: Return to the first fork Area 12 - 16
north_corridor_return = Map("North Corridor Return")

# Area 13: West Corridor Return
west_corridor_return = Map("West Corridor Return")

# Area 14: Southern Tunnel 2 - Return
southern_tunnel_2_return = Map("Southern Tunnel 2 Return")

# Area 15: Eastern Corridor 2 - Return
eastern_corridor_2_return = Map("Eastern Corridor 2 Return")

# Area 16: South Corridor Return
south_corridor_return = Map("South Corridor Return")

# Area 17: North-East Path
north_east_corridor = Map("North East Corridor")

# Area 18: Northern Path
northern_tunnel = Map("Northern Tunnel")

# Area 19: East Corridor from North
eastern_corridor_1 = Map("Eastern Corridor 1")

# Area 20: Second Split
two_way_fork_2 = Map("Second Split")
two_way_fork_2.set_description("""You have found another divided path!
                 - Forward (South)
                 - Right (East)""")

# Area 21: Final Dead End
southern_dead_end = Map("Southern Dead End")
southern_dead_end.set_description("""You have stumbled upon a dead end. Go back and
choose another path.""")

# Area 22: Deeper Cave
deeper_cave = Map("Deeper Cave")
deeper_cave.set_description("""Congratulations! You have reached the deeper parts of
the cave. Be aware you may find some hostile monsters and requires you to fight.
Good luck.""")


# Beginning of the Cave
cave.link_areas(small_opening, "East")
small_opening.link_areas_opposite(cave, "West")
cave.link_areas(dark_tunnel, "South")
dark_tunnel.link_areas(cave, "North")

# Small Opening onward
small_opening.link_areas(southern_tunnel_1, "South")
southern_tunnel_1.link_areas(two_way_fork_1, "East")

# First Fork
two_way_fork_1.link_areas(north_east_corridor, "North East")
north_east_corridor.link_areas(northern_tunnel, "North")
northern_tunnel.link_areas(eastern_corridor_1, "East")
eastern_corridor_1.link_areas(two_way_fork_2, "South")

# First Fork - South Path
two_way_fork_1.link_areas(eastern_corridor_2, "South")
eastern_corridor_2.link_areas(southern_tunnel_2, "East")
southern_tunnel_2.link_areas(west_corridor, "South")
west_corridor.link_areas(north_corridor, "West")
north_corridor.link_areas(northern_dead_end, "North")

# First Fork - South Path (Goes back to the first fork)
northern_dead_end.link_areas(north_corridor_return, "South")
north_corridor_return.link_areas(west_corridor_return, "East")
west_corridor_return.link_areas(southern_tunnel_2_return, "North")
southern_tunnel_2_return.link_areas(eastern_corridor_2_return, "West")
eastern_corridor_2_return.link_areas(two_way_fork_1, "North")

# Second fork
two_way_fork_2.link_areas(southern_dead_end, "South")
two_way_fork_2.link_areas(deeper_cave, "East")
southern_dead_end.link_areas(two_way_fork_2, "North")  # Goes back to the second fork


current_area = cave
facing_direction = None  # Tracks the player's current facing direction
discovered_areas = set()
discovered_areas.add(current_area.get_name())

while True:
    print("\n")
    current_area.get_details()
    if current_area.get_character():
        current_area.get_character().describe()

    command = input("> ").strip()

    # Compass Display
    if command.upper() == "M":
        print_compass(facing_direction)
        if facing_direction:
            print(f"You are currently facing: {facing_direction}")
        continue

    if command.lower() == "map":
        print_ascii_map(current_area, discovered_areas)
        continue

    # Movement (Full Direction Names & Shortcuts)
    direction_map = {
        "north": "North", "n": "North",
        "east": "East", "e": "East",
        "south": "South", "s": "South",
        "west": "West", "w": "West",
        "northeast": "North East", "north east": "North East", "ne": "North East",
        "northwest": "North West", "north west": "North West", "nw": "North West",
        "southeast": "South East", "south east": "South East", "se": "South East",
        "southwest": "South West", "south west": "South West", "sw": "South West"
    }

    move_direction = direction_map.get(command.lower(), command)

    if move_direction in [
        "North", "East", "South", "West",
        "North East", "North West", "South East", "South West"
    ]:
        facing_direction = move_direction
        next_area = current_area.move(move_direction)
        if next_area != current_area:
            clear_console()
            current_area = next_area
            discovered_areas.add(current_area.get_name())
        continue

    print("Unrecognized command. Type a direction, 'map', 'M' for compass.")
