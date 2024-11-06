# MousePicnic Text Adventure Game

# This Python-based text adventure game challenges players to help a little mouse prepare for a picnic.
# Navigate through various rooms, gather essential items, and avoid encounters with the Owl, Fox, and Snake,
# who will end the game if met. The goal is to collect all six items and reach the Back Door to win.

# Features:

# Interactive navigation with commands like "go North" and "get [item name]"
# Unique rooms containing items and characters
# Win condition: Collect all items and reach the exit
# Loss condition: Avoid rooms with villain characters
# Built-in inventory system to track collected items
#_________________
# Author: LogLogic
# Date: 06/16/2022

# A dictionary for the Mouse Picnic Text Game.
# The dictionary links a room to other rooms.
rooms = {
    'at the Main Door': {'South': 'in the Great Hall', 'Item': 'the Owl'},  # villain
    'at the Back Door': {'East': 'in the Bathroom', 'Item': 'the EXIT'},
    'at the Side Door': {'West': 'in the East Hall', 'Item': 'the Fox'},  # villain
    'in the Great Hall': {'South': 'in the Library', 'West': 'in the Bathroom', 'North': 'in the North Hall', 'East': 'in the East Hall', 'Item': 'an empty room'},
    'in the East Hall': {'South': 'in the Kitchen', 'West': 'in the Great Hall', 'North': 'in the Pantry', 'East': 'at the Side Door', 'Item': 'an empty room'},
    'in the North Hall': {'South': 'in the Great Hall', 'West': 'in the Wardrobe', 'North': 'at the Main Door', 'Item': 'an empty room'},
    'in the Library': {'West': 'in the Bedroom', 'North': 'in the Great Hall', 'East': 'in the Dining Room', 'Item': 'the Ultimate PredatorPedia book'},
    'in the Bathroom': {'South': 'in the Bedroom', 'West': 'at the Back Door', 'North': 'in the Wardrobe', 'East': 'in the Great Hall', 'Item': 'a Sun Lotion'},
    'in the Kitchen': {'South': 'in the Dining Room', 'North': 'in the East Hall', 'Item': 'a Picnic Basket'},
    'in the Dining Room': {'West': 'in the Library', 'North': 'in the Kitchen', 'Item': 'a Cup of Tea'},
    'in the Pantry': {'South': 'in the East Hall', 'Item': 'a Kernel'},
    'in the Wardrobe': {'South': 'in the Bathroom', 'East': 'in the North Hall', 'Item': 'the Snake'},  # villain
    'in the Bedroom': {'North': 'in the Bathroom', 'East': 'in the Library', 'Item': 'a Blanket'}
}


# Define instructions.
def instructions():  # Print a main menu and the commands
    print('           _     _ ')
    print('          (_) _ (_)')
    print('           ( @ @ )  ')
    print('            \   /   ')
    print('            ==o==  ')
    print('~ The Mouse Picnic Text Game ~\n')
    print('Help the little mouse get ready for a picnic, \n'
          'collect 6 items, \n'
          'sneak from the roommate Snake, \n'
          'and avoid being invited to the Owl and Fox’s parties.\n')
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("Typ in Exit to stop the game \n")


# Define player’s status
def player_status():
    if user_input[0] == 'go' or user_input[0] == 'Go':
        print("You are {}".format(current_room))
        print("You see {}".format(current_item))
        print("Inventory: {}".format(inventory))
        print("_" * 20)
        pass
    elif user_input[0] == 'get' or user_input[0] == 'Get':
        print("You are {}".format(current_room))
        print("Inventory: {}".format(inventory))
        print("_" * 20)


instructions()  # Call for instructions
current_room = 'in the Great Hall'  # Assign the starting room.
current_item = rooms[current_room]['Item']  # Assign the current item
inventory = []  # create an empty list for inventory

print("You are {}".format(current_room))
print("You see {}".format(current_item))
print("Inventory: {}".format(inventory))
print("_" * 20)

# Game loop.
while True:  # Keep repeating while true
    # Losing case
    if current_item == "the Owl":  # If current item equals to 'the Owl'
        print("NOM...NOM Game over!\n"
              "Thanks for joining the Owl’s party. Hope you enjoyed it.")
        break  # Stop the game
    # Losing case
    elif current_item == "the Fox":  # If current item equals to 'the Fox'
        print("NOM...NOM Game over!\n"
              "Thanks for joining the Fos’s party. Hope you enjoyed it.")
        break  # Stop the game
    # Losing case
    elif current_item == "the Snake":  # If current item equals to 'the Snake'
        print("NOM...NOM Game over!\n"
              "Thanks for playing the game. Hope you enjoyed it.")
        break  # Stop the game
    # Winning case
    elif current_room == "at the Back Door" and len(
            inventory) == 6:  # If current room equals to 'at the Back Door' and number of items in inventory list equals to 6
        print("YAY! You did it! Now your are ready dor the picnic. \n"
              "Enjoy your day! \n"
              "Thanks for playing the game. Hope you enjoyed it.")
        break  # Stop the game
    # Prevent leaving early
    elif current_room == "at the Back Door" and len(inventory) < 6:  # If current room equals to 'at the Back Door' and number of items in inventory list less than 6
        print("Wait a second! You're not ready for the picnic yet! You need to collect all 6 items.")

    user_input = input("What would you like to do?\n")  # Get input from user

    # Command to stop the game
    if user_input == 'Exit':  # If user input Exit
        break  # Break the game

    user_input = user_input.split()  # Split user input
    user_item = ' '.join(user_input[1:])
    if len(user_input) <= 1:  # Check if user provided input
        print("Invalid input.")  # Print "Invalid input."
    else:
        if user_input[0] == 'go' or user_input[0] == 'Go':  # If first element(0) equal to 'go' or 'Go'
            if len(user_input) == 2 and user_input[1] in rooms[current_room]:  # If second element(-1) belongs to dictionary
                current_room = rooms[current_room][user_input[1]]  # Assign the current room to the room associated with the direction
                current_item = rooms[current_room]['Item']  # Assign the current item to the current room
            elif len(user_input) != 2 and user_input[1] in rooms[current_room]:  # Check if user provided correct input
                print("Invalid input.")
            else:  # If there is no such direction in the room,
                print("There is nothing in this direction.")  # Print "There is nothing in this direction."
        elif user_input[0] == 'get' or user_input[0] == 'Get':  # If first element(0) equal to 'get' or 'Get'
            if current_item == 'an empty room':  # If current item equal to 'an empty room'
                print("There is nothing to get")
            else:
                inventory.append(current_item)  # Add item to inventory list
                rooms[current_room]['Item'] = 'an empty room'  # Change the value of Item key associated with current room
        else:  # If first element(0) not equal to 'go'
            print("Invalid input.")  # Print "Invalid input."
        player_status()  # Call for player status
