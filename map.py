"""Map class for Journey to the Core."""

# Direction opposites for bidirectional movement
opposite_directions = {
    "North": "South", "South": "North",
    "East": "West", "West": "East",
    "North East": "South West", "South West": "North East",
    "North West": "South East", "South East": "North West"
}


class Map:
    """Defines attributes and methods for various location objects."""

    def __init__(self, area_name):
        self.name = area_name
        self.description = " "
        self.linked_areas = {}
        self.character = None

    def set_name(self, area_name):
        self.name = area_name

    def get_name(self):
        return self.name

    def set_description(self, area_description):
        self.description = area_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def get_details(self):
        direction_names = ["North", "East", "South", "West",
                           "North East", "North West", "South East", "South West"]

        if self.name.strip() in direction_names:
            print(f"You are now heading: {self.name.strip()}")
        else:
            print(self.name)
            print("--------")
            print(self.description)
            for direction in self.linked_areas:
                print(direction)

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def link_areas(self, area_to_link, direction, bidirectional=False):
        """Links this area to another area in a specified direction.
           If bidirectional is True, links the reverse direction too."""
        self.linked_areas[direction] = area_to_link

        if bidirectional:
            reverse = opposite_directions.get(direction)
            if reverse:
                area_to_link.linked_areas[reverse] = self

    def link_areas_opposite(self, area_to_link, direction):
        """Links this area to another area in a specified direction, but hides it
        from get_details()."""
        # Store hidden links in a separate dictionary
        if not hasattr(self, 'hidden_linked_areas'):
            self.hidden_linked_areas = {}
        self.hidden_linked_areas[direction] = area_to_link

    def move(self, direction):
        """Moves to a linked area in the specified direction (visible or hidden)."""
        if direction in self.linked_areas:
            return self.linked_areas[direction]
        elif hasattr(self, 'hidden_linked_areas') and direction in self.hidden_linked_areas:
            return self.hidden_linked_areas[direction]
        else:
            print("You shall not pass here.")
            return self
