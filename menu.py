import os
import sys
from players import *
from mathmaking import *

def clear_screen():
    # Check the platform (Windows or Unix-based)
    if os.name == 'posix':  # Unix-based systems
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')

# Function prints main menu and calls functions upon user's request
def main_menu():
    while True:
        print("======Badminton Player Management Software=======")
        print("1. Players")
        print("2. Rankings")
        print("3. Create a Match")
        print("4. Publish")
        print("x. Quit")
        print("=================================================")
        print("\n")
        choice = input("Enter your choice: ")
        clear_screen()
        

        if choice == "1":
            player_menu()
        elif choice == "2":
            # Handle Rankings logic here
            rankings()
            input()
        elif choice == "3":

            player1 = input("Enter player 1: ")
            player2 = input("Enter player 2: ")
            create_match(player1, player2)
            input()

        elif choice == "4":
            # Handle Publish logic here
            print("Publishing...")

        elif choice.lower() == "x":
            print("Exiting the software...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def player_menu(): 
    clear_screen()
    while True:
        print("======Player Menu=======")
        print("1. List Players")
        print("2. Add Players")
        print("3. Delete")
        print("4. Edit")
        print("x. Back")
        print("========================")
        print("\n")
        choice = input("Enter your choice: ")
        clear_screen()
        if choice == "1":
            list_players()
            input("Enter any key to continue")
        elif choice == "2":
            # Handle Rankings logic here
            add_player()
        elif choice == "3":
            create_match()
        elif choice == "4":
            # Handle Publish logic here
            edit_player()
        elif choice.lower() == "x":
            main_menu()
        else:
            print("Invalid choice. Please try again.")
        clear_screen()
