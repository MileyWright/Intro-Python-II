# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.items = []

    def get_item(self, item):
        self.current_room.remove_item(item)
        self.items.append(item)
        return f"You picked up {item.name}"

    def open_inventory(self):
        for i in self.items:
            if len(self.items) > 0:
                print(i)
            else:
                print('Empty')

    def __str__(self):
        return f'{self.name} is in {self.current_room}'
