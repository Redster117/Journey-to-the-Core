"""Testing cave system map."""
import os
import colorama
from map import Map


def clear_console():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

HIGHLIGHT = "\033[93m"
RESET = "\033[0m"

def print_compass(current_direction=None):
    """Prints a compass with 8 directions. Highlights current direction if given."""

    def marked_direction(direction):
        return (
            f"{HIGHLIGHT}{direction}{RESET}"
            if direction == current_direction else direction
        )

    print("\nCompass:")
    print(f"    {marked_direction('North West')}  {marked_direction('North')}  {marked_direction('North East')}")
    print(f"    {marked_direction('West')}          ◉          {marked_direction('East')}")
    print(f"    {marked_direction('South West')}  {marked_direction('South')}  {marked_direction('South East')}\n")


def print_ascii_map(current_area, discovered_areas):
    colorama.init()

    def draw_box(name, width):
        top   = " " + "_" * width
        label = f"{HIGHLIGHT}{name.center(width)}{RESET}" if name == current_area.get_name() else name.center(width)
        mid   = f"|{label}|"
        bot   = " " + "─" * width
        return [top, mid, bot]

    # 4 direction arrows
    def arrow_up(pad):
        return [" " * pad + "Ʌ", " " * pad + "│"]

    def arrow_down(pad):
        return [" " * pad + "│", " " * pad + "V"]

    def arrow_left(pad, length=5):
        return [" " * pad + "<" + "─" * length]

    def arrow_right(pad, length=5):
        return [" " * pad + "─" * length + ">"]

    # Straight lines
    def vertical(pad, length=2):
        return [" " * pad + "│" for _ in range(length)]

    def horizontal(pad, length=2):
        return [" " * pad + "─" * length]
    
    # Straight lines with ◆ (used for corners in corridors & tunnels)
    def corner_up(pad, length=1):
        return [" " * pad + "◆"] + [" " * pad + "│" for _ in range(length)]

    def corner_down(pad, length=3):
        return [" " * pad + "│" for _ in range(length)] + [" " * pad + "◆"]

    def corner_left(pad, length=5):
        return [" " * pad + "◆" + "─" * length]

    def corner_right(pad, length=5):
        return [" " * pad + "─" * length + "◆"]

    def corner_connector_vertical(pad, length=5):
        return [" " * pad + "│" for _ in range(length) + "◆"]

    def corner_connector_horizontal(pad, length=5):
        return [" " * pad + "◆" + "─" * length + "◆"]

    # 1) Cave → Small Opening
    if "The Cave" in discovered_areas and "The Small Opening" in discovered_areas:
        cave_box = draw_box("The Cave", width=11)
        opening_box = draw_box("The Small Opening", width=18)
        for i, (line_c, line_o) in enumerate(zip(cave_box, opening_box)):
            if i == 1:
                # Only print the arrow on the middle line
                arrow = " ─────> "
            else:
                arrow = "         "
            print(line_c + arrow + line_o)
    elif "The Cave" in discovered_areas:
        for line in draw_box("The Cave", width=11):
            print(line)

    # 2) First Fork North East Path
    # Dark Tunnel not Discovered
    if "Second Fork" in discovered_areas and "Eastern Corridor 1" in discovered_areas and "Northern Tunnel" in discovered_areas and "North East Corridor" in discovered_areas and "The Dark Tunnel" not in discovered_areas and "First Fork" in discovered_areas:
        first_fork_box = draw_box("First Fork", width=15)
        dark_tunnel_box = draw_box("The Dark Tunnel", width=17)
        second_fork_box = draw_box("Second Fork", width=15)

        print(" " * 30 + "│" + " " * 25 + "◆" + "─" * 11 + "◆")
        print(" " * 30 + "│" + " " * 25 + "◆" + " " * 11 + "│")
        print(" " * 30 + "│" * 1 + " " * 8 + first_fork_box[0] + "/" + " " * 5 + second_fork_box[0])
        print(" " * 29 + " ◆──────> " + first_fork_box[1] + " " * 5 + second_fork_box[1])
        print(" " * 39 + first_fork_box[2] + " " * 6 + second_fork_box[2])

    # Dark Tunnel Discovered
    elif "Second Fork" in discovered_areas and "Eastern Corridor 1" in discovered_areas and "Northern Tunnel" in discovered_areas and "North East Corridor" in discovered_areas and "The Dark Tunnel" in discovered_areas and "First Fork" in discovered_areas:
        first_fork_box = draw_box("First Fork", width=15)
        dark_tunnel_box = draw_box("The Dark Tunnel", width=17)
        second_fork_box = draw_box("Second Fork", width=15)

        print(" " * 8 + "│" + " " * 22 + "│" + " " * 25 + "◆" + "─" * 11 + "◆")
        print(" " * 8 + "V" + " " * 22 + "│" + " " * 25 + "◆" + " " * 11 + "│")
        print(dark_tunnel_box[0] + " " * 13 + "│" * 1 + " " * 8 + first_fork_box[0] + "/" + " " * 5 + second_fork_box[0])
        print(dark_tunnel_box[1] + " " * 11 + " ◆──────> " + first_fork_box[1] + " " * 5 + second_fork_box[1])
        print(dark_tunnel_box[2] + " " * 22 + first_fork_box[2] + " " * 6 + second_fork_box[2])
    
    # Dark Tunnel not Discovered
    elif "Eastern Corridor 1" in discovered_areas and "Northern Tunnel" in discovered_areas and "North East Corridor" in discovered_areas and "The Dark Tunnel" not in discovered_areas and "First Fork" in discovered_areas:
        first_fork_box = draw_box("First Fork", width=15)

        print(" " * 30 + "│" + " " * 25 + "◆" + "─" * 11 + "◆")
        print(" " * 30 + "│" + " " * 25 + "◆" + " " * 11 + "│")
        print(" " * 30 + "│" * 1 + " " * 8 + first_fork_box[0] + "/" + " " * 12 + "│")
        print(" " * 29 + " ◆──────> " + first_fork_box[1])
        print(" " * 39 + first_fork_box[2])
    
    # Dark Tunnel Discovered
    elif "Eastern Corridor 1" in discovered_areas and "Northern Tunnel" in discovered_areas and "North East Corridor" in discovered_areas and "The Dark Tunnel" in discovered_areas and "First Fork" in discovered_areas:
        first_fork_box = draw_box("First Fork", width=15)
        dark_tunnel_box = draw_box("The Dark Tunnel", width=17)

        print(" " * 8 + "│" + " " * 22 + "│" + " " * 25 + "◆" + "─" * 11 + "◆")
        print(" " * 8 + "V" + " " * 22 + "│" + " " * 25 + "◆" + " " * 11 + "│")
        print(dark_tunnel_box[0] + " " * 13 + "│" * 1 + " " * 8 + first_fork_box[0] + "/" + " " * 12 + "│")
        print(dark_tunnel_box[1] + " " * 11 + " ◆──────> " + first_fork_box[1])
        print(dark_tunnel_box[2] + " " * 22 + first_fork_box[2])
    
    # Dark Tunnel Discovered
    elif "Northern Tunnel" in discovered_areas and "North East Corridor" in discovered_areas and "The Dark Tunnel" in discovered_areas and "First Fork" in discovered_areas:
        first_fork_box = draw_box("First Fork", width=15)
        dark_tunnel_box = draw_box("The Dark Tunnel", width=17)

        print(" " * 8 + "│" + " " * 22 + "│" + " " * 25 + "◆")
        print(" " * 8 + "V" + " " * 22 + "│" + " " * 25 + "◆")
        print(dark_tunnel_box[0] + " " * 13 + "│" * 1 + " " * 8 + first_fork_box[0] + "/")
        print(dark_tunnel_box[1] + " " * 11 + " ◆──────> " + first_fork_box[1])
        print(dark_tunnel_box[2] + " " * 22 + first_fork_box[2])
    
    # Dark Tunnel not Discovered
    elif "Northern Tunnel" in discovered_areas and "North East Corridor" in discovered_areas and "The Dark Tunnel" not in discovered_areas:
        first_fork_box = draw_box("First Fork", width=15)
        print(" " * 30 + "│")
        print(" " * 30 + "│" + " " * 25 + "◆")
        print(" " * 30 + "│" + " " * 25 + "◆")
        print(" " * 30 + "│" + " " * 8 + first_fork_box[0] + "/")
        print(" " * 29 + " ◆──────> " + first_fork_box[1])
        print(" " * 39 + first_fork_box[2])

    # Dark Tunnel Discovered
    elif "North East Corridor" in discovered_areas and "The Dark Tunnel" in discovered_areas and "First Fork" in discovered_areas:
        first_fork_box = draw_box("First Fork", width=15)
        dark_tunnel_box = draw_box("The Dark Tunnel", width=17)

        print(" " * 8 + "│" + " " * 22 + "│")
        print(" " * 8 + "V" + " " * 22 + "│" + " " * 25 + "◆")
        print(dark_tunnel_box[0] + " " * 13 + "│" * 1 + " " * 8 + first_fork_box[0] + "/")
        print(dark_tunnel_box[1] + " " * 11 + " ◆──────> " + first_fork_box[1])
        print(dark_tunnel_box[2] + " " * 22 + first_fork_box[2])

    # Dark Tunnel Discovered
    elif "The Dark Tunnel" in discovered_areas and "First Fork" in discovered_areas:
        first_fork_box = draw_box("First Fork", width=15)
        dark_tunnel_box = draw_box("The Dark Tunnel", width=17)

        print(" " * 8 + "│" + " " * 22 + "│")
        print(" " * 8 + "V" + " " * 22 + "│")
        print(dark_tunnel_box[0] + " " * 13 + "│" * 1 + " " * 8 + first_fork_box[0])
        print(dark_tunnel_box[1] + " " * 11 + " ◆──────> " + first_fork_box[1])
        print(dark_tunnel_box[2] + " " * 22 + first_fork_box[2])
    
    # Dark Tunnel not Discovered
    elif "North East Corridor" in discovered_areas and "The Dark Tunnel" not in discovered_areas:
        first_fork_box = draw_box("First Fork", width=15)
        # vertical from Small Opening
        for line in vertical(pad=30):
            print(line)
        print(" " * 30 + "│" + " " * 25 + "◆")
        print(" " * 30 + "│" + " " * 8 + first_fork_box[0] + "/")
        print(" " * 29 + " ◆──────> " + first_fork_box[1])
        print(" " * 39 + first_fork_box[2])
  
    elif "The Dark Tunnel" in discovered_areas:
        for line in arrow_down(pad=8):
            print(line)
        for line in draw_box("The Dark Tunnel", width=17):
            print(line)

    elif "First Fork" in discovered_areas:
        # vertical from Small Opening
        for line in vertical(pad=30):
            print(line)
        first_fork_box = draw_box("First Fork", width=15)
        # top of First Fork
        print(" " * 30 + "│" + " " * 8 + first_fork_box[0])
        # mid of First Fork
        print(" " * 29 + " ◆──────> " + first_fork_box[1])
        # bot of First Fork
        print(" " * 39 + first_fork_box[2])

    # 3) First Fork → South Path
    if "Southern Dead End" in discovered_areas and "Dead End" not in discovered_areas:
        print(" " * 68 + "│")
        print(" " * 68 + "│")
        print(" " * 68 + "V")
        print(" " * 60 + "Southern Dead End")
    
    elif "Southern Dead End" in discovered_areas and "Dead End" in discovered_areas:
        print(" " * 47 + "│" + " " * 21 + "│")
        print(" " * 47 + "│" + " " * 21 + "│")
        print(" " * 47 + "◆" + "─" * 3 + "◆" + " " * 17 + "V")
        print(" " * 52 + "│" + " " * 8 + "Southern Dead End")
        print(" " * 35 + "Dead End" + " " * 9 + "│")
        print(" " * 39 + "│" + " " * 12 + "│")
        print(" " * 39 + "◆" + "─" * 12 + "◆")

    elif "Dead End" in discovered_areas:
        print(" " * 47 + "│")
        print(" " * 47 + "│")
        print(" " * 47 + "◆" + "─" * 3 + "◆")
        print(" " * 52 + "│")
        print(" " * 35 + "Dead End" + " " * 9 + "│")
        print(" " * 39 + "│" + " " * 12 + "│")
        print(" " * 39 + "◆" + "─" * 12 + "◆")
        
    else: 
        if "Eastern Corridor 2" in discovered_areas:
            for line in vertical(pad=47, length=2):
                print(line)
        
        if "Southern Tunnel 2" in discovered_areas:
            for line in corner_connector_horizontal(pad=47, length=5):
                print(line)
    
        if "West Corridor" in discovered_areas:
            for line in vertical(pad=53, length=3):
                print(line)
        
        if "Northern Corridor" in discovered_areas:
            for line in corner_connector_horizontal(pad=40, length=12):
                print(line)

    if "Northern Dead End 1" in discovered_areas:
        fifth_fork_box = draw_box("Fifth Fork", width=12)
        arrow_right = "──────> "
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        third_fork_box = draw_box("Third Fork", width=13)
        fourth_fork_returned_box = draw_box("Fourth Fork ", width=12)
        print(" " * 36 + "◆" + "─" * 18 + "◆")
        print(" " * 36 + "│" + " " * 18 + "│")
        print(" " * 36 + "│" + " " * 18 + "│")
        print(" " * 26 + " " * 4 + fourth_fork_returned_box[0] + " " * 12 + "│")
        print(" " * 26 + "◆" + "─" * 3 + fourth_fork_returned_box[1] + "─" * 11 + "◆")
        print(" " * 26 + "│" + " " * 3 + fourth_fork_returned_box[2] + " " * 13 + "Dead End")
        print(" " * 26 + "│" + " " * 25 + "◆" + "─" * 7 + "◆")
        print(deeper_cave_box[0] + " " * 9 + third_fork_box[0] + " " * 16 + "│")
        print(deeper_cave_box[1] + arrow_right + third_fork_box[1] + " " * 12 + "◆" + "─" * 2 + "◆")
        print(deeper_cave_box[2] + " " * 9 + third_fork_box[2] + " " * 13 + "│")

    elif "Eastern Tunnel 4" in discovered_areas:
        fifth_fork_box = draw_box("Fifth Fork", width=12)
        arrow_right = "──────> "
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        third_fork_box = draw_box("Third Fork", width=13)
        fourth_fork_returned_box = draw_box("Fourth Fork ", width=12)
        print(" " * 36 + "◆" + "─" * 18 + "◆")
        print(" " * 36 + "│" + " " * 18 + "│")
        print(" " * 36 + "│" + " " * 18 + "│")
        print(" " * 26 + " " * 4 + fourth_fork_returned_box[0] + " " * 12 + "│")
        print(" " * 26 + "◆" + "─" * 3 + fourth_fork_returned_box[1] + "─" * 11 + "◆")
        print(" " * 26 + "│" + " " * 3 + fourth_fork_returned_box[2])
        print(" " * 26 + "│" + " " * 25 + "◆" + "─" * 7 + "◆")
        print(deeper_cave_box[0] + " " * 9 + third_fork_box[0] + " " * 16 + "│")
        print(deeper_cave_box[1] + arrow_right + third_fork_box[1] + " " * 12 + "◆" + "─" * 2 + "◆")
        print(deeper_cave_box[2] + " " * 9 + third_fork_box[2] + " " * 13 + "│")

    elif "Northern Tunnel 4" in discovered_areas:
        fifth_fork_box = draw_box("Fifth Fork", width=12)
        arrow_right = "──────> "
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        third_fork_box = draw_box("Third Fork", width=13)
        fourth_fork_returned_box = draw_box("Fourth Fork ", width=12)
        print(" " * 36 + "◆" + "─" * 18 + "◆")
        print(" " * 36 + "│" + " " * 18 + "│")
        print(" " * 36 + "│" + " " * 18 + "│")
        print(" " * 26 + " " * 4 + fourth_fork_returned_box[0] + " " * 12 + "│")
        print(" " * 26 + "◆" + "─" * 3 + fourth_fork_returned_box[1] + "─" * 11 + "◆")
        print(" " * 26 + "│" + " " * 3 + fourth_fork_returned_box[2])
        print(" " * 26 + "│" + " " * 25 + "◆")
        print(deeper_cave_box[0] + " " * 9 + third_fork_box[0] + " " * 16 + "│")
        print(deeper_cave_box[1] + arrow_right + third_fork_box[1] + " " * 12 + "◆" + "─" * 2 + "◆")
        print(deeper_cave_box[2] + " " * 9 + third_fork_box[2] + " " * 13 + "│")

    elif "Eastern Tunnel 3" in discovered_areas:
        fifth_fork_box = draw_box("Fifth Fork", width=12)
        arrow_right = "──────> "
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        third_fork_box = draw_box("Third Fork", width=13)
        fourth_fork_returned_box = draw_box("Fourth Fork ", width=12)
        print(" " * 36 + "◆" + "─" * 18 + "◆")
        print(" " * 36 + "│" + " " * 18 + "│")
        print(" " * 36 + "│" + " " * 18 + "│")
        print(" " * 26 + " " * 4 + fourth_fork_returned_box[0] + " " * 12 + "│")
        print(" " * 26 + "◆" + "─" * 3 + fourth_fork_returned_box[1] + "─" * 11 + "◆")
        print(" " * 26 + "│" + " " * 3 + fourth_fork_returned_box[2])
        print(" " * 26 + "│")
        print(deeper_cave_box[0] + " " * 9 + third_fork_box[0])
        print(deeper_cave_box[1] + arrow_right + third_fork_box[1] + " " * 12 + "◆" + "─" * 2 + "◆")
        print(deeper_cave_box[2] + " " * 9 + third_fork_box[2] + " " * 13 + "│")

    elif "Northern Tunnel 3" in discovered_areas:
        fifth_fork_box = draw_box("Fifth Fork", width=12)
        arrow_right = "──────> "
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        third_fork_box = draw_box("Third Fork", width=13)
        fourth_fork_returned_box = draw_box("Fourth Fork ", width=12)
        print(" " * 36 + "◆" + "─" * 18 + "◆")
        print(" " * 36 + "│" + " " * 18 + "│")
        print(" " * 36 + "│" + " " * 18 + "│")
        print(" " * 26 + " " * 4 + fourth_fork_returned_box[0] + " " * 12 + "│")
        print(" " * 26 + "◆" + "─" * 3 + fourth_fork_returned_box[1] + "─" * 11 + "◆")
        print(" " * 26 + "│" + " " * 3 + fourth_fork_returned_box[2])
        print(" " * 26 + "│")
        print(deeper_cave_box[0] + " " * 9 + third_fork_box[0])
        print(deeper_cave_box[1] + arrow_right + third_fork_box[1] + " " * 12 + "◆")
        print(deeper_cave_box[2] + " " * 9 + third_fork_box[2] + " " * 13 + "│")

    elif "Fourth Fork " in discovered_areas:
        fourth_fork_returned_box = draw_box("Fourth Fork ", width=12)
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        third_fork_box = draw_box("Third Fork", width=13)
        arrow_right = " ─────> "
        print(" " * 36 + "◆" + "─" * 18 + "◆")
        print(" " * 36 + "│" + " " * 18 + "│")
        print(" " * 36 + "│" + " " * 18 + "│")
        print(" " * 26 + " " * 4 + fourth_fork_returned_box[0] + " " * 12 + "│")
        print(" " * 26 + "◆" + "─" * 3 + fourth_fork_returned_box[1] + "─" * 11 + "◆")
        print(" " * 26 + "│" + " " * 3 + fourth_fork_returned_box[2])
        print(" " * 26 + "│")
        print(deeper_cave_box[0] + " " * 9 + third_fork_box[0])
        print(deeper_cave_box[1] + arrow_right + third_fork_box[1])
        print(deeper_cave_box[2] + " " * 9 + third_fork_box[2])

    elif "Western Tunnel" in discovered_areas:
        fourth_fork_box = draw_box("Fourth Fork", width=12)
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        third_fork_box = draw_box("Third Fork", width=13)
        arrow_right = " ─────> "
        print(" " * 36 + "◆" + "─" * 24 + "◆")
        print(" " * 36 + "│" + " " * 24 + "│")
        print(" " * 30 + fourth_fork_box[0] + " " * 18 + "│")
        print(" " * 26 + "◆" + "─" * 3 + fourth_fork_box[1] + "─" * 17 + "◆")
        print(" " * 26 + "│" + " " * 3 + fourth_fork_box[2])
        print(" " * 26 + "│")
        print(deeper_cave_box[0] + " " * 9 + third_fork_box[0])
        print(deeper_cave_box[1] + arrow_right + third_fork_box[1])
        print(deeper_cave_box[2] + " " * 9 + third_fork_box[2])

    elif "Southern Tunnel 3" in discovered_areas:
        fourth_fork_box = draw_box("Fourth Fork", width=12)
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        third_fork_box = draw_box("Third Fork", width=13)
        arrow_right = " ─────> "
        print(" " * 36 + "◆" + "─" * 18 + "◆")
        print(" " * 36 + "│" + " " * 18 + "│")
        print(" " * 36 + "│" + " " * 18 + "│")
        print(" " * 26 + " " * 4 + fourth_fork_box[0] + " " * 12 + "│")
        print(" " * 26 + "◆" + "─" * 3 + fourth_fork_box[1] + " " * 11 + "◆")
        print(" " * 26 + "│" + " " * 3 + fourth_fork_box[2])
        print(" " * 26 + "│")
        print(deeper_cave_box[0] + " " * 9 + third_fork_box[0])
        print(deeper_cave_box[1] + arrow_right + third_fork_box[1])
        print(deeper_cave_box[2] + " " * 9 + third_fork_box[2])

    elif "Northern Tunnel 1 " in discovered_areas:
        fourth_fork_box = draw_box("Fourth Fork", width=12)
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        third_fork_box = draw_box("Third Fork", width=13)
        arrow_right = " ─────> "
        print(" " * 61 + "◆")
        print(" " * 61 + "│")
        print(" " * 30 + fourth_fork_box[0] + " " * 18 + "│")
        print(" " * 26 + "◆" + "─" * 3 + fourth_fork_box[1] + "─" * 17 + "◆")
        print(" " * 26 + "│" + " " * 3 + fourth_fork_box[2])
        print(" " * 26 + "│")
        print(deeper_cave_box[0] + " " * 9 + third_fork_box[0])
        print(deeper_cave_box[1] + arrow_right + third_fork_box[1])
        print(deeper_cave_box[2] + " " * 9 + third_fork_box[2])

    elif "Eastern Tunnel 1" in discovered_areas:
        fourth_fork_box = draw_box("Fourth Fork", width=12)
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        third_fork_box = draw_box("Third Fork", width=13)
        arrow_right = " ─────> "
        print(" " * 36 + "◆" + "─" * 18 + "◆")
        print(" " * 36 + "│")
        print(" " * 36 + "│")
        print(" " * 26 + " " * 4 + fourth_fork_box[0])
        print(" " * 26 + "◆" + "─" * 3 + fourth_fork_box[1])
        print(" " * 26 + "│" + " " * 3 + fourth_fork_box[2])
        print(" " * 26 + "│")
        print(deeper_cave_box[0] + " " * 9 + third_fork_box[0])
        print(deeper_cave_box[1] + arrow_right + third_fork_box[1])
        print(deeper_cave_box[2] + " " * 9 + third_fork_box[2])
    
    elif "Eastern Tunnel 1 " in discovered_areas:
        fourth_fork_box = draw_box("Fourth Fork", width=12)
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        third_fork_box = draw_box("Third Fork", width=13)
        arrow_right = " ─────> "
        print(" " * 26 + " " * 4 + fourth_fork_box[0])
        print(" " * 26 + "◆" + "─" * 3 + fourth_fork_box[1] + "─" * 17 + "◆")
        print(" " * 26 + "│" + " " * 3 + fourth_fork_box[2])
        print(" " * 26 + "│")
        print(deeper_cave_box[0] + " " * 9 + third_fork_box[0])
        print(deeper_cave_box[1] + arrow_right + third_fork_box[1])
        print(deeper_cave_box[2] + " " * 9 + third_fork_box[2])

    elif "Northern Tunnel 1" in discovered_areas:
        fourth_fork_box = draw_box("Fourth Fork", width=12)
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        third_fork_box = draw_box("Third Fork", width=13)
        arrow_right = " ─────> "
        print(" " * 36 + "◆")
        print(" " * 36 + "│")
        print(" " * 36 + "│")
        print(" " * 26 + " " * 4 + fourth_fork_box[0])
        print(" " * 26 + "◆" + "─" * 3 + fourth_fork_box[1])
        print(" " * 26 + "│" + " " * 3 + fourth_fork_box[2])
        print(" " * 26 + "│")
        print(deeper_cave_box[0] + " " * 9 + third_fork_box[0])
        print(deeper_cave_box[1] + arrow_right + third_fork_box[1])
        print(deeper_cave_box[2] + " " * 9 + third_fork_box[2])

    elif "Fourth Fork" in discovered_areas:
        fourth_fork_box = draw_box("Fourth Fork", width=12)
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        third_fork_box = draw_box("Third Fork", width=13)
        arrow_right = " ─────> "
        print(" " * 26 + " " * 4 + fourth_fork_box[0])
        print(" " * 26 + "◆" + "─" * 3 + fourth_fork_box[1])
        print(" " * 26 + "│" + " " * 3 + fourth_fork_box[2])
        print(" " * 26 + "│")
        print(deeper_cave_box[0] + " " * 9 + third_fork_box[0])
        print(deeper_cave_box[1] + arrow_right + third_fork_box[1])
        print(deeper_cave_box[2] + " " * 9 + third_fork_box[2])

    elif "Northern Corridor 1" in discovered_areas:
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        third_fork_box = draw_box("Third Fork", width=13)
        arrow_right = " ─────> "
        print(" " * 26 + "◆")
        print(" " * 26 + "│")
        print(" " * 26 + "│")
        print(deeper_cave_box[0] + " " * 9 + third_fork_box[0])
        print(deeper_cave_box[1] + arrow_right + third_fork_box[1])
        print(deeper_cave_box[2] + " " * 9 + third_fork_box[2])

    elif "Third Fork" in discovered_areas:
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        third_fork_box = draw_box("Third Fork", width=13)
        for i, (line_c, line_o) in enumerate(zip(deeper_cave_box, third_fork_box)):
            if i == 1:
                # Only print the arrow on the middle line
                arrow = " ─────> "
            else:
                arrow = "         "
            print(line_c + arrow + line_o)
    
    elif "Deeper Cave" in discovered_areas:
        deeper_cave_box = draw_box("Deeper Cave", width=12)
        print(deeper_cave_box[0])
        print(deeper_cave_box[1])
        print(deeper_cave_box[2])

    if "South Eastern Tunnel" in discovered_areas:
        fifth_fork_box = draw_box("Fifth Fork", width=12)
        arrow_right = "──────> "
        print(" " * 29 + "│" + " " * 16 + "◆" + "─" * 2 + "◆")
        print(" " * 29 + "│" + " " * 16 + "│")
        print(" " * 29 + "│" + " " * 8 + fifth_fork_box[0])
        print(" " * 29 + "◆" + arrow_right + fifth_fork_box[1] + "─" * 3 + "◆")
        print(" " * 38 + fifth_fork_box[2] + " " *  4 + "│")
        print(" " * 55 + "◆" + "─" * 3 + "◆")


    elif "Eastern Corridor 4" in discovered_areas:
        fifth_fork_box = draw_box("Fifth Fork", width=12)
        arrow_right = "──────> "
        print(" " * 29 + "│" + " " * 16 + "◆" + "─" * 2 + "◆")
        print(" " * 29 + "│" + " " * 16 + "│")
        print(" " * 29 + "│" + " " * 8 + fifth_fork_box[0])
        print(" " * 29 + "◆" + arrow_right + fifth_fork_box[1] + "─" * 3 + "◆")
        print(" " * 38 + fifth_fork_box[2] + " " *  4 + "│")
        print(" " * 55 + "◆")

    elif "Southern Corridor 1" in discovered_areas:
        fifth_fork_box = draw_box("Fifth Fork", width=12)
        arrow_right = "──────> "
        print(" " * 29 + "│" + " " * 16 + "◆" + "─" * 2 + "◆")
        print(" " * 29 + "│" + " " * 16 + "│")
        print(" " * 29 + "│" + " " * 8 + fifth_fork_box[0])
        print(" " * 29 + "◆" + arrow_right + fifth_fork_box[1] + "─" * 3 + "◆")
        print(" " * 38 + fifth_fork_box[2])

    elif "Eastern Tunnel 2" in discovered_areas:
        fifth_fork_box = draw_box("Fifth Fork", width=12)
        arrow_right = "──────> "
        print(" " * 29 + "│" + " " * 16 + "◆" + "─" * 2 + "◆")
        print(" " * 29 + "│" + " " * 16 + "│")
        print(" " * 29 + "│" + " " * 8 + fifth_fork_box[0])
        print(" " * 29 + "◆" + arrow_right + fifth_fork_box[1])
        print(" " * 38 + fifth_fork_box[2])


    elif "Northern Tunnel 2" in discovered_areas:
        fifth_fork_box = draw_box("Fifth Fork", width=12)
        arrow_right = "──────> "
        print(" " * 29 + "│" + " " * 16 + "◆")
        print(" " * 29 + "│" + " " * 16 + "│")
        print(" " * 29 + "│" + " " * 8 + fifth_fork_box[0])
        print(" " * 29 + "◆" + arrow_right + fifth_fork_box[1])
        print(" " * 38 + fifth_fork_box[2])

    elif "Fifth Fork" in discovered_areas:
        fifth_fork_box = draw_box("Fifth Fork", width=12)
        arrow_right = "──────> "
        print(" " * 29 + "│")
        print(" " * 29 + "│")
        print(" " * 29 + "│" + " " * 8 + fifth_fork_box[0])
        print(" " * 29 + "◆" + arrow_right + fifth_fork_box[1])
        print(" " * 38 + fifth_fork_box[2])

    elif "Southern Corridor" in discovered_areas:
        for line in corner_down(pad=29):
            print(line)
    
    print("\nLegend: Yellow = Current Location | Hidden areas stay invisible\n")


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
first_fork = Map("First Fork")
first_fork.set_description("""Your path has split to two. Which way will you go?
                            Hint: Enter map to open map
                            Hint: Enter cp/compass to reveal a compass
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

# Area 10: Northern Corridor
northern_corridor = Map("Northern Corridor")

# Area 11: Dead End
northern_dead_end = Map("Dead End")
northern_dead_end.set_description("""You have reached a dead end, return to the last
point you came from to continue your journey.""")

# Area 12: North-East Path
north_east_corridor = Map("North East Corridor")

# Area 13: Northern Path
northern_tunnel = Map("Northern Tunnel")

# Area 14: East Corridor from North
eastern_corridor_1 = Map("Eastern Corridor 1")

# Area 15: Second Fork
second_fork = Map("Second Fork")
second_fork.set_description("""You have found another divided path!
                - Right (East)
                - Forward (South)""")

# Area 16: Southern Dead End
southern_dead_end = Map("Southern Dead End")
southern_dead_end.set_description("""You have stumbled upon a dead end. Go back and
choose another path.""")

# Area 17: Deeper Cave
deeper_cave = Map("Deeper Cave")
deeper_cave.set_description("""Congratulations! You have reached the deeper parts of
the cave. Be aware you may find some hostile monsters and requires you to fight.
Good luck.""")

# Area 18: Third Fork
third_fork = Map("Third Fork")
third_fork.set_description("""You have found a third fork in the cave
                           - Left (North)
                           - Right (South)""")

# Area 19: Northern Corridor 1
northern_corridor_1 = Map("Northern Corridor 1")

# Area 20: Fourth Fork
fourth_fork = Map("Fourth Fork")
fourth_fork.set_description("""You have found a fourth fork in the cave
                            - Left (North)
                            - Straight (East)""")

# Area 21: Northern Tunnel 1 (Loop)
northern_tunnel_1 = Map("Northern Tunnel 1")

# Area 22: Eastern Tunnel 1 (Loop)
eastern_tunnel_1 = Map("Eastern Tunnel 1")

# Area 23: Southern Tunnel 3 (Loop)
southern_tunnel_3 = Map("Southern Tunnel 3")

# Area 24: Fourth Fork Returned
fourth_fork_returned = Map("Fourth Fork ")
fourth_fork_returned.set_description("""You have found a fourth fork in the cave
                            - Left (North)
                            - Straight (East)""")

# Area 25: Fourth Fork East Path
eastern_tunnel_2 = Map("Eastern Tunnel 1 ")

# Area 26: Northern Tunnel East Path
northern_tunnel_2 = Map("Northern Tunnel 1 ")

# Area 27: Western Tunnel East Path
western_tunnel = Map ("Western Tunnel")

# Area 28: Third Fork South Path
southern_corridor = Map("Southern Corridor")

# Area 29: Southern Corridor → Eastern Corridor
eastern_corridor_3 = Map("Eastern Corridor 3")

# Area 30: Fifth Fork
fifth_fork = Map("Fifth Fork")
fifth_fork.set_description("""You have found a fifth fork in the deeper cave
                            - Left (North)
                            - Straight (East)""")

# Area 31: Fifth Fork - North Path (Zigzag)
northern_tunnel_3 = Map("Northern Tunnel 2")

# Area 32: North → East
eastern_tunnel_3 = Map("Eastern Tunnel 2")

# Area 33: East → North
northern_tunnel_4 = Map("Northern Tunnel 3")

# Area 34: North → East
eastern_tunnel_4 = Map("Eastern Tunnel 3")

# Area 35: East → North
northern_tunnel_5 = Map("Northern Tunnel 4")

# Area 36: North → East
eastern_tunnel_5 = Map("Eastern Tunnel 4")

# Area 37: North → Northern Dead End
northern_dead_end_1 = Map("Northern Dead End 1")

# Area 38: Fifth Fork - East Path
southern_corridor_1 = Map("Southern Corridor 1")

# Area 39: South → East
eastern_corridor_4 = Map("Eastern Corridor 4")

# Area 40: East → South East
south_eastern_tunnel = Map("South Eastern Tunnel")

# Area 41: South East → East
eastern_tunnel_6 = Map("Eastern Tunnel 6")

# Area 42: East → South
southern_tunnel_4 = Map("Southern Tunnel 4")

# Area 43: South → South East
south_eastern_corridor = Map("South Eastern Corridor")

# Area 44: South East → East
eastern_corridor_5 = Map("Eastern Corridor 5")

# Area 45: East → North (Zigzag)
northern_corridor_2 = Map("Northern Corridor 2")

# Area 46: North → East
eastern_corridor_7 = Map("Eastern Corridor 7")

# Area 47: East → North
northern_corridor_3 = Map("Northern Corridor 3")

# Area 48: North → East
eastern_corridor_8 = Map("Eastern Corridor 8")

# Area 49: East → Infernal Hollow
infernal_hollow = Map("Infernal Hollow")
infernal_hollow.set_description("""Amazing Job! You have finally reached the lowest level
of the cave. Remember that the cave system is larger than the deeper parts of the cave
in which you just passed. Good luck!""")


# Beginning of the Cave
cave.link_areas(small_opening, "East")
small_opening.link_areas_opposite(cave, "West")
cave.link_areas(dark_tunnel, "South")
dark_tunnel.link_areas(cave, "North")

# Small Opening onward
small_opening.link_areas(southern_tunnel_1, "South")
southern_tunnel_1.link_areas(first_fork, "East")

# First Fork - North East Path
first_fork.link_areas(north_east_corridor, "North East")
north_east_corridor.link_areas(northern_tunnel, "North")
northern_tunnel.link_areas(eastern_corridor_1, "East")
eastern_corridor_1.link_areas(second_fork, "South")

# First Fork - North East Path - Reversed
second_fork.link_areas_opposite(eastern_corridor_1, "North")
eastern_corridor_1.link_areas_opposite(northern_tunnel, "West")
northern_tunnel.link_areas_opposite(north_east_corridor, "South")
north_east_corridor.link_areas_opposite(first_fork, "South West")

# First Fork - South Path
first_fork.link_areas(eastern_corridor_2, "South")
eastern_corridor_2.link_areas(southern_tunnel_2, "East")
southern_tunnel_2.link_areas(west_corridor, "South")
west_corridor.link_areas(northern_corridor, "West")
northern_corridor.link_areas(northern_dead_end, "North")

# First Fork - South Path - Reversed
northern_dead_end.link_areas_opposite(northern_corridor, "South")
northern_corridor.link_areas_opposite(west_corridor, "East")
west_corridor.link_areas_opposite(southern_tunnel_2, "North")
southern_tunnel_2.link_areas_opposite(eastern_corridor_2, "West")
eastern_corridor_2.link_areas_opposite(first_fork, "North")

# Second fork
second_fork.link_areas(deeper_cave, "East")
second_fork.link_areas(southern_dead_end, "South")
southern_dead_end.link_areas(second_fork, "North")  # Goes back to the second fork

# Deeper Cave (Level 2)
deeper_cave.link_areas(third_fork, "East")

# Third Fork - North Path
third_fork.link_areas(northern_corridor_1, "North")
northern_corridor_1.link_areas(fourth_fork, "East")

# Fourth Fork - North Path - North Path - Loop
fourth_fork.link_areas(northern_tunnel_1, "North")
northern_tunnel_1.link_areas(eastern_tunnel_1, "East")
eastern_tunnel_1.link_areas(southern_tunnel_3, "South")
southern_tunnel_3.link_areas(fourth_fork_returned, "West")
northern_tunnel_1.link_areas_opposite(fourth_fork_returned, "South")
eastern_tunnel_1.link_areas_opposite(northern_tunnel_1, "West")
southern_tunnel_3.link_areas_opposite(eastern_tunnel_1, "North")
fourth_fork_returned.link_areas_opposite(southern_tunnel_3, "East")

# Fourth Fork - North Path - East Path - Loop
fourth_fork.link_areas(eastern_tunnel_2, "East")
eastern_tunnel_2.link_areas(northern_tunnel_2, "North")
northern_tunnel_2.link_areas(western_tunnel, "West")
western_tunnel.link_areas(fourth_fork, "South")

# Fourth Fork → Third Fork
fourth_fork_returned.link_areas_opposite(northern_corridor_1, "West")
northern_corridor_1.link_areas_opposite(third_fork, "South")

# Third Fork - South Path
third_fork.link_areas(southern_corridor, "South")
southern_corridor.link_areas_opposite(third_fork, "North")
southern_corridor.link_areas(fifth_fork, "East")
fifth_fork.link_areas_opposite(southern_corridor, "West")


# Fifth Fork - North Path
fifth_fork.link_areas(northern_tunnel_3, "North")
northern_tunnel_3.link_areas(eastern_tunnel_3, "East")
eastern_tunnel_3.link_areas(northern_tunnel_4, "North")
northern_tunnel_4.link_areas(eastern_tunnel_4, "East")
eastern_tunnel_4.link_areas(northern_tunnel_5, "North")
northern_tunnel_5.link_areas(eastern_tunnel_5, "East")
eastern_tunnel_5.link_areas(northern_dead_end_1, "North")

#Fifth Fork - North Path - Reversed
northern_tunnel_3.link_areas_opposite(fifth_fork, "South")
eastern_tunnel_3.link_areas_opposite(northern_tunnel_3, "West")
northern_tunnel_4.link_areas_opposite(eastern_tunnel_3, "South")
eastern_tunnel_4.link_areas_opposite(northern_tunnel_4, "West")
northern_tunnel_5.link_areas_opposite(eastern_tunnel_4, "South")
eastern_tunnel_5.link_areas_opposite(northern_tunnel_5, "West")
northern_dead_end_1.link_areas_opposite(eastern_tunnel_5, "South")

# Fifth Fork - East Path
fifth_fork.link_areas(southern_corridor_1, "East")
southern_corridor_1.link_areas(eastern_corridor_4, "South")
eastern_corridor_4.link_areas(south_eastern_tunnel, "East")
south_eastern_tunnel.link_areas(eastern_tunnel_6, "South East")
eastern_tunnel_6.link_areas(southern_tunnel_4, "East")
southern_tunnel_4.link_areas(south_eastern_corridor, "South")
south_eastern_corridor.link_areas(eastern_corridor_5, "South East")
eastern_corridor_5.link_areas(northern_corridor_2, "East")
northern_corridor_2.link_areas(eastern_corridor_7, "North")
eastern_corridor_7.link_areas(northern_corridor_3, "East")
northern_corridor_3.link_areas(eastern_corridor_8, "North")

#Fifth Fork - East Path - Reversed
eastern_corridor_8.link_areas_opposite(northern_corridor_3, "South")
northern_corridor_3.link_areas_opposite(eastern_corridor_7, "West")
eastern_corridor_7.link_areas_opposite(northern_corridor_2, "South")
northern_corridor_2.link_areas_opposite(eastern_corridor_5, "West")
eastern_corridor_5.link_areas_opposite(south_eastern_corridor, "North West")
south_eastern_corridor.link_areas_opposite(southern_tunnel_4, "North")
southern_tunnel_4.link_areas_opposite(eastern_tunnel_6, "West")
eastern_tunnel_6.link_areas_opposite(south_eastern_tunnel, "North West")
south_eastern_tunnel.link_areas_opposite(eastern_corridor_4, "West")
eastern_corridor_4.link_areas_opposite(southern_corridor_1, "North")
southern_corridor_1.link_areas_opposite(fifth_fork, "West")



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
    if command.lower() == "cp" or command.lower() == "compass":
        print_compass(facing_direction)
        if facing_direction:
            print(f"You are currently facing: {facing_direction}")
        continue

    #Developer Commands
    if command.lower() == "level 1":
        discovered_areas.add("The Dark Tunnel")
        discovered_areas.add("The Small Opening")
        discovered_areas.add("First Fork")
        discovered_areas.add("Dead End")
        discovered_areas.add("North East Corridor")
        discovered_areas.add("Northern Tunnel")
        discovered_areas.add("Eastern Corridor 1")
        discovered_areas.add("Southern Dead End")
        discovered_areas.add("Second Fork")
        current_area = second_fork
    
    if command.lower() == "level 2":
        discovered_areas.add("The Dark Tunnel")
        discovered_areas.add("The Small Opening")
        discovered_areas.add("First Fork")
        discovered_areas.add("Dead End")
        discovered_areas.add("North East Corridor")
        discovered_areas.add("Northern Tunnel")
        discovered_areas.add("Eastern Corridor 1")
        discovered_areas.add("Southern Dead End")
        discovered_areas.add("Second Fork")
        #Level 2
        discovered_areas.add("Deeper Cave")
        discovered_areas.add("Third Fork")
        discovered_areas.add("Northern Corridor")
        discovered_areas.add("Fourth Fork")
        discovered_areas.add("Northern Tunnel 1")
        discovered_areas.add("Eastern Tunnel 1")
        discovered_areas.add("Southern Tunnel 3")
        discovered_areas.add("Fourth Fork ")
        discovered_areas.add("Eastern Tunnel 1 ")
        discovered_areas.add("Northern Tunnel 1 ")
        discovered_areas.add("Southern Corridor")
        discovered_areas.add("Fifth Fork")
        discovered_areas.add("Northern Tunnel 2")
        discovered_areas.add("Eastern Tunnel 2")
        discovered_areas.add("Northern Tunnel 3")
        discovered_areas.add("Eastern Tunnel 3")
        discovered_areas.add("Northern Tunnel 4")
        discovered_areas.add("Eastern Tunnel 4")
        discovered_areas.add("Northern Tunnel 5")
        discovered_areas.add("Eastern Tunnel 5")
        discovered_areas.add("Northern Dead End 1")
        #discovered_areas.add("Southern Corridor 1")
        #discovered_areas.add("Eastern Corridor 4")
        #discovered_areas.add("South Eastern Tunnel")
        #discovered_areas.add("Eastern Tunnel 6")
        #discovered_areas.add("Southern Tunnel 4")
        #discovered_areas.add("South Eastern Corridor")
        #discovered_areas.add("Eastern Corridor 5")
        #discovered_areas.add("Northern Corridor 2")
        #discovered_areas.add("Eastern Corridor 7")
        #discovered_areas.add("Northern Corridor 3")
        #discovered_areas.add("Eastern Corridor 8")
        current_area = fifth_fork

    # Map Display
    if command.lower() == "map":
        clear_console()
        if current_area in [second_fork, first_fork, cave, dark_tunnel, small_opening, northern_dead_end, north_east_corridor,
                            northern_tunnel, eastern_corridor_2, southern_dead_end, southern_tunnel_2, west_corridor, northern_corridor,
                            ]:
            # Level 1 map
            level_1_areas = {area for area in discovered_areas if area in [
                "The Cave", "The Dark Tunnel", "The Small Opening", "First Fork",
                "Dead End", "North East Corridor", "Northern Tunnel", "Eastern Corridor 2",
                "Southern Dead End", "Second Fork", "Southern Tunnel 2", "West Corridor", "Northern Corridor",
                "Eastern Corridor 1"
            ]}
            print_ascii_map(current_area, level_1_areas)
        elif current_area in [
            third_fork, deeper_cave, northern_corridor, fourth_fork, northern_tunnel_1, eastern_tunnel_1, southern_tunnel_3, 
            fourth_fork_returned, eastern_tunnel_2, northern_tunnel_2, western_tunnel, southern_corridor, fifth_fork, northern_tunnel_3,
            eastern_tunnel_3, northern_tunnel_4, eastern_tunnel_4, northern_tunnel_5, eastern_tunnel_5, northern_dead_end_1, southern_corridor_1,
            eastern_corridor_4, south_eastern_tunnel, eastern_tunnel_6, southern_tunnel_4, south_eastern_corridor, eastern_corridor_5,
            northern_corridor_2, eastern_corridor_7, northern_corridor_3, eastern_corridor_8
            
        ]:
            # Level 2 map
            level_2_areas = {area for area in discovered_areas if area in [
                "Deeper Cave", "Third Fork", "Northern Corridor 1", "Fourth Fork",
                "Northern Tunnel 1", "Eastern Tunnel 1", "Southern Tunnel 3", "Fourth Fork ",
                "Eastern Tunnel 1 ", "Northern Tunnel 1 ", "Southern Tunnel 3 ", "Western Tunnel",
                "Southern Corridor", "Fifth Fork", "Northern Tunnel 2", "Eastern Tunnel 2", "Northern Tunnel 3",
                "Eastern Tunnel 3", "Northern Tunnel 4", "Eastern Tunnel 4", "Northern Tunnel 5", "Eastern Tunnel 5",
                "Northern Dead End 1", "Southern Corridor 1", "Eastern Corridor 4", "South Eastern Tunnel", "Eastern Tunnel 6",
                "Southern Tunnel 4", "South Eastern Corridor", "Eastern Corridor 5", "Northern Corridor 2",
                "Eastern Corridor 7", "Northern Corridor 3", "Eastern Corridor 8"
            ]}
            print_ascii_map(current_area, level_2_areas)
        else:
            print("You are in an unknown area. No map available.")
    
    elif command.lower() == "testing map 1":
        print(""" ___________          __________________
|  The Cave | ─────> |The Small Opening |
 ───────────          ──────────────────
        │                      │                         ◆───────────◆
        V                      │                         ◆           │
 _________________             │         _______________/      _______________
| The Dark Tunnel |            ◆──────> |   First Fork  |     |  Second Fork  |
 ─────────────────                       ───────────────       ───────────────
                                               │
                                               │
                                               ◆───◆
                                                    │
                                   Dead End         │
                                       │            │
                                       ◆────────────◆
              """)

    elif command.lower() == "testing map 2":
        print("""                                    ◆──────────────────◆
                                    │                  │
                                    │                  │
                               ____________            │
                          ◆───|Fourth Fork |───────────◆
                          │    ────────────             Dead End
                          │                         ◆───────◆
 ____________          _____________                │
|Deeper Cave |──────> |  Third Fork |            ◆──◆
 ────────────          ─────────────             │
                             │                ◆──◆
                             │                │
                             │         ____________
                             ◆──────> | Fifth Fork |
                                       ────────────""")

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
