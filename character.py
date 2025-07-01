# """Character class for Cave Exploration Game."""
# class Character:
#     """Defines attributes and methods for map objects."""
#     def __init__(self, char_name, char_description):
#         """Sets character attributes."""
#         self.name = char_name
#         self.description = char_description
#         self.conversation = None
#
#     def describe(self):
#         """Sets the character description."""
#         print(self.name + " is here!")
#         print(self.description)
#
#     def set_conversation(self, conversation):
#         """Sets what the character can say."""
#         self.conversation = conversation
#
#     def talk(self):
#         """Prints the character's conversation."""
#         if self.conversation is not None:
#             print(self.name + " says: " + self.conversation)
#         else:
#             print(self.name + " has nothing to say to you.")
#
#     #def fight(self):
#        # """Declines to fight."""
#         #print(self.name + "does not want to fight a retard like you.")
#         #return True
#
# #class Enemy(Character):
#     #"""Defines attributes and methods for the Enemy sub-class"""
#     #def __init__(self, char_name, char_description):
#         #super().__init__(char_name, char_description)
#         #self.weakness = None
#
#     #def set_weakness(self, item_weakness):
#         #"""Sets the character's weakness"""
#         #self.weakness = item_weakness
#
#     #def get_weakness(self):
#         #"""Gets weakness"""
#         #return self.weakness
#
#     #def fight(self, combat_item):
#         #if combat_item == self.weakness:
#             #print("You fend off " + self.name + " with your " + combat_item)
#             #return True
#         #else:
#             #print(self.name + " swallows you whole! U R DED.")
#             #return False
