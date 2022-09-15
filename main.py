#Importing classes module
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.console import Console
# from rich import print
from rich.panel import Panel
import classes
import functions as f
import os
import sys

#ceate instance of console for printing displays
#using import print would result in all numbers being printed cyan
console = Console()

#counter for key in dict and creating empty dict that will be id(int): contact(object)
contact_id = 1
contacts_dict = {}

#variable for user menu choice used to match case
menu_choice = None

# while user input is not 'EX' (ex is to escape from program)
#show menu a and get user's menu choice
while menu_choice != 'EX':
    f.menu_prompt()
    #assign input for menu and clear screen
    menu_choice = Prompt.ask('Please make a selecttion: ', choices=['A', 'E', 'D', 'DC', 'DA', 'Q'])
    os.system('cls||clear')

    # match case user input with uppyer for A, E, D, S, SA
    match menu_choice.upper():
        case 'A':
            #new while loop and match case to choose what type of contact to enter
            add_choice = None
            while add_choice != 'EX':
                f.add_contact_prompt()
                add_choice = Prompt.ask('Please make a selecttion: ', choices=['C', 'CC', 'FC', 'WC', 'H', 'Q'])
                # add_choice = input('Enter a choice: C, CC, FC, WC or EX >>')
                os.system('cls||clear')

                # Creating a new instance of whatever clss is being entere, Contact, CloseContact, FamilyContact or WorkContact
                # using the class method set_details() to get user input for contact
                #incremendting contact ID each time a contact is created
                match add_choice.upper():
                    case 'C':
                        console.print(Panel.fit("[magenta]Enter your Contact's details", title="[cyan]Adding a Contact"))
                        f_name, l_name, phone = classes.Contact.set_details()
                        contacts_dict[contact_id] = classes.Contact(contact_id, f_name, l_name, phone)
                        contact_id += 1
                        break
                    case 'CC':
                        console.print(Panel.fit("[magenta]Enter your Contact's details", title="[cyan]Adding a Close Contact"))
                        f_name, l_name, phone, address = classes.CloseContact.set_details()
                        contacts_dict[contact_id] = classes.CloseContact(contact_id, f_name, l_name, phone, address)
                        contact_id += 1
                        break
                    case 'FC':
                        console.print(Panel.fit("[magenta]Enter your Contact's details", title="[cyan]Adding a Family Contact"))
                        f_name, l_name, phone, address, pet_name, fav_drink = classes.FamilyContact.set_details()
                        contacts_dict[contact_id] = classes.FamilyContact(contact_id, f_name, l_name, phone, address, pet_name, fav_drink)
                        contact_id += 1
                        break
                    case 'WC':
                        console.print(Panel.fit("[magenta]Enter your Contact's details", title="[cyan]Adding a Work Contact"))
                        f_name, l_name, phone, address, w_address, w_phone, skills = classes.WorkContact.set_details()
                        contacts_dict[contact_id] = classes.WorkContact(contact_id, f_name, l_name, phone, address, w_address, w_phone, skills)
                        contact_id += 1
                        break
                    case 'H':
                        break
                    case 'Q':
                        sys.exit()

        case 'E':
                search_again = True
                while search_again:
                    os.system('cls||clear')

                    console.print(Panel.fit("[magenta]Search for a contact to edit", title="[cyan]Editing a Contact"))
                    edit_choice = input('Enter a contact name to edit >> ')

                    for v in contacts_dict.values():
                        if v.f_name == edit_choice:
                            print(v.get_details())
                            print('Edit details')
                            match v.class_type:
                                case 'c':
                                    f_name, l_name, phone = classes.Contact.set_details()
                                    v.update_contact(f_name, l_name, phone)
                                    search_again = False
                                    break
                                case 'cc':
                                    f_name, l_name, phone, address = classes.CloseContact.set_details()
                                    v.update_contact(f_name, l_name, phone, address)
                                    search_again = False
                                    break
                                case 'fc':
                                    f_name, l_name, phone, address, pet, drink = classes.FamilyContact.set_details()
                                    v.update_contact(f_name, l_name, phone, address, pet, drink)
                                    search_again = False
                                    break
                                case 'wc':
                                    f_name, l_name, phone, address, w_address, w_phone, skills = classes.WorkContact.set_details()
                                    v.update_contact(f_name, l_name, phone, address, w_address, w_phone, skills)
                                    search_again = False
                                    break
                    else:
                        os.system('cls||clear')
                        console.print(Panel.fit("[magenta]That contact does not exist", title="[cyan]Editing a Contact"))
                        search_again = Confirm.ask('Would you like to search for another contact?')
        case 'D':
            print('Deleting a contact')
            del_choice = None
            confirm_delete = None
            while not confirm_delete:
                print("====================================Deleting a contact ==================================")
                print("Enter the contacts name to delete or EX to exit to main menu.")
                print('\n====================================================================================')
                del_choice = input('Enter a contact name to delete >> ')

                match del_choice.upper():
                    case 'EX':
                        break

                    case other:
                        for k, v in contacts_dict.items():
                            if v.f_name == del_choice:
                                print(v.get_details())
                                confirm_delete = Confirm.ask(f'A you sure you want to delete {v.f_name} {v.l_name} ?')
                                if confirm_delete:
                                    del contacts_dict[k]
                                    break
                            
                  
        case 'DC':
            show_choice = None
            while show_choice != 'EX':
                print("====================================Displaying a contact ==================================")
                print("Enter the contacts name to display or EX to exit to main menu.")
                print('\n====================================================================================')
                show_choice = input('Enter a contact name to display >> ')

                match show_choice.upper():
                    case 'EX':
                        break

                    case other:
                        for v in contacts_dict.values():
                            if v.f_name == show_choice:
                                print(v.get_details())
                                break
                        else:
                            print("that contaxt doesnt exist")
        case 'DA':
            os.system('cls||clear')
            print('Showing all contacts')
            for k, v in contacts_dict.items():
            #     if v.f_name == find:
                print('==========================================')
                print(v.get_details())
                print('\n==========================================')
            is_rich_great = Confirm.ask('Do you like rich?')
        case 'Q':
            break






