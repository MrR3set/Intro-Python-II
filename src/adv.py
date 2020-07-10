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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


print("Start game")
print("-"*50)

playerObject = Player("Sarah", room["outside"])

userInput = str
print(f'Greetings {playerObject.name} lets begin our adventure!')


# 
def movementHandler():
    if userInput == "n":
        if playerObject.currentPos.n_to:
            playerObject.currentPos = playerObject.currentPos.n_to
        else:
            print("You cannot move North")
    elif userInput == "w":
        if playerObject.currentPos.w_to:
            playerObject.currentPos = playerObject.currentPos.w_to
        else:
            print("You cannot move West")
    elif userInput == "s":
        if playerObject.currentPos.s_to:
            playerObject.currentPos = playerObject.currentPos.s_to
        else:
            print("You cannot move South")
    elif userInput == "e":
        if playerObject.currentPos.e_to:
            playerObject.currentPos = playerObject.currentPos.e_to
        else:
            print("You cannot move East")
    elif userInput == "h":
        print("Valid options are n s e w")
    elif userInput == "l":
        print("You can see this items in the room", playerObject.currentPos.inventory)
    elif userInput == "i":
        print("You have this items ", playerObject.inventory)
    elif userInput == "q":
        print("Goodbye")
    else:
        print("Invalid command")

def handleInventory():
    item = userInput.split(" ")[1] #Item that will be handled
    if "take" in userInput or "get" in userInput:
        if item in playerObject.currentPos.inventory:
            print("Taking ", item)
            playerObject.currentPos.inventory.remove(item)
            playerObject.inventory.append(item)
        else:
            print(f'{item} is not in the room inventory')
    elif "drop" in userInput:
        if item in playerObject.inventory:
            print("droping ", item)
            playerObject.inventory.remove(item)
            playerObject.currentPos.inventory.append(item)
            
        else:
            print(f'{userInput.split(" ")[1]} is not in the player inventory')


while userInput != "q":
    print(f"Youre currently {playerObject.currentPos.name}\n{playerObject.currentPos.description}")
    userInput = input("What should we do?\n>>")


    if len(userInput.split(" ")) == 2:
        handleInventory()
    else:
        movementHandler()



