from menu import *
import os

def clear_screen():
    # Check the platform (Windows or Unix-based)
    if os.name == 'posix':  # Unix-based systems
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')

def main():
    main_menu()

main()