from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].w_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].w_to = room['overlook']
room['foyer'].d_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].a_to = room['foyer']
room['narrow'].w_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player('Miley', room['outside'])
# Write a loop that:
def check_location(move):
# * Prints the current room name
    current = new_player.current_room
    if current.__dict__[f'{move}_to'] == None:
        print('\n **There\'s nothing there! **')
    else:
        new_player.current_room = current.__dict__[f'{move}_to']
while True:
    current = new_player.current_room
    # print(f"\n {current}")
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
    movement_choice = ['w', 'a', 's', 'd']
    print(f'\n****Hello {new_player.name}. Your current location is {current}****')
    choice = input(f'\n =What would you like to do? Move: [north(w), south(s), east(d), west(a), or quit(q)?')
# If the user enters a cardinal direction, attempt to move to the room there.
    if choice in movement_choice:
        check_location(choice)
# Print an error message if the movement isn't allowed.
    # elif choice not in movement_choice:
    #     print('\nForbidden movement input.')
# If the user enters "q", quit the game.
    elif choice == "q":
        print('Thanks for playing!')
        exit()
    else:
        print('\nForbidden movement input.')