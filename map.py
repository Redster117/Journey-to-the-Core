"""Map class for Journey to the Core."""


class Map:
    """Defines attributes and methods for various location objects."""
    def __init__(self, area_name):
        """Sets class attributes."""
        self.name = area_name
        self.description = " "
        self.linked_areas = {}
        self.character = None

    def set_name(self, area_name):
        """Sets the area name"""
        self.name = area_name

    def get_name(self):
        """Gets the area name"""
        return self.name

    def set_description(self, area_description):
        """Sets the area description."""
        self.description = area_description

    def get_description(self):
        """Gets the area description."""
        return self.description

    def describe(self):
        """Sets the area description."""
        print(self.description)

    def link_areas(self, area_to_link, direction):
        """Links this area to another area in a specified direction."""
        self.linked_areas[direction] = area_to_link

    def get_details(self):
        """Displays area info unless it's just a directional node."""
        direction_names = ["North", "East", "South", "West",
                           "North East", "North West", "South East", "South West"]

        if self.name.strip() in direction_names:
            print(f"You are now heading: {self.name.strip()}")
        else:
            print(self.name)
            print("--------")
            print(self.description)
            for direction, _ in self.linked_areas.items():
                print(direction)  # Just show the direction, not area name

    def move(self, direction):
        """Moves to a linked area in the specified direction."""
        if direction in self.linked_areas:
            return self.linked_areas[direction]
        else:
            print("You shall not pass here.")
            return self

    def set_character(self, new_character):
        """Sets the name of character objects in the area object"""
        self.character = new_character

    def get_character(self):
        """Returns the name of the character objects in this area"""
        return self.character
