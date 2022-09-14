import os

# User prompt fuction with information on how to use the program
def menu_prompt():
    """
    This function clears the screen each time and prints a user prompt with instructions on how to use the program
    """    
    os.system('cls||clear')
    print("|===============================================================================================|\n|\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\tWelcome to your Contacts Database\t\t\t\t\t\t\t|")
    print("|\tPlease Select from the menu below\t\t\t\t\t\t\t|")
    print('|\tAdd Contact - \t\tA\t\t\t\t\t\t\t\t|')
    print('|\tEdit Contact - \t\tE\t\t\t\t\t\t\t\t|')
    print('|\tDel Contact - \t\tD\t\t\t\t\t\t\t\t|')
    print('|\tShow Contact - \t\tS\t\t\t\t\t\t\t\t|')
    print('|\tShow all Contact - \tSA\t\t\t\t\t\t\t\t|')
    print('|\tExit Program - \t\tEX\t\t\t\t\t\t\t\t|')
    print('|\t\t\t\t\t\t\t\t\t\t\t\t|')
    print("|===============================================================================================|")

# function to prompt user to press any key to contine - program execution is fronzen until a key press happens
def press_to_continue():
    """
    This function freezes the program execution and prints a press any key to continue message.
    Once a key is pressed it exits
    """   
    os.system("/bin/bash -c 'read -s -n 1 -p \"\n\tPress any key to continue...\"'\n")
    os.system('cls||clear')
    print()