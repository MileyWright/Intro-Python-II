# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.w_to = None
        self.s_to = None
        self.d_to = None
        self.a_to = None
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        return self.items
    
    def remove_item(self, item):
        del self.items[item]

    def __str__(self):
        # if self.items is not None:
        #     return f""
        return f'{self.name}, {self.description}'