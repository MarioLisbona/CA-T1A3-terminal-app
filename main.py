#Importing modules
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

#While true will always loop.
#Break statments and Q to quit will end the application
#show menu a and get user's menu choice
while True:
    #call function to display add contact menu
    f.menu_prompt()
    #assign input for menu and clear screen
    menu_choice = Prompt.ask('Please make a selecttion: ', choices=['A', 'E', 'D', 'DC', 'DA', 'Q'])
    os.system('cls||clear')

    # match case user input with upper for A, E, D, DC, DA, Q to quit Application
    match menu_choice.upper():

        #Add a contact
        case 'A':
            #new while loop and match case to choose what type of contact to enter
            # add_choice = None

            #While true will always loop.
            #Break statments and Q to quit will end the application
            while True:
                #call function to display add contact menu
                #use Prompy from rich.prompt module to give a selection menu to the user and assign choice to add_choice
                f.add_contact_prompt()
                add_choice = Prompt.ask('Please make a selecttion: ', choices=['C', 'CC', 'FC', 'WC', 'H', 'Q'])
                os.system('cls||clear')

                # Creating a new instance of each class that is chosen - Contact, CloseContact, FamilyContact or WorkContact
                # using the class method set_details() to get user input for contact
                #incremendting contact ID each time a contact is created
                match add_choice.upper():
                    case 'C':
                        #Panel printing a heading
                        #set_details method called on Contact class returns the user input
                        #dict entry created with with contact_id as key and an instance of contact class as the value
                        #set_details method return variables used as arguments for object instance
                        #increment contact_id for key contacts_dict
                        console.print(Panel.fit("[magenta]Enter your Contact's details", title="[cyan]Adding a Contact"))
                        f_name, l_name, phone = classes.Contact.set_details()
                        contacts_dict[contact_id] = classes.Contact(contact_id, f_name, l_name, phone)
                        contact_id += 1
                        break
                    case 'CC':
                        #same as above but object created as instance of CloseContact class
                        console.print(Panel.fit("[magenta]Enter your Contact's details", title="[cyan]Adding a Close Contact"))
                        f_name, l_name, phone, address = classes.CloseContact.set_details()
                        contacts_dict[contact_id] = classes.CloseContact(contact_id, f_name, l_name, phone, address)
                        contact_id += 1
                        break
                    case 'FC':
                        #same as above but object created as instance of FamilyContact class
                        console.print(Panel.fit("[magenta]Enter your Contact's details", title="[cyan]Adding a Family Contact"))
                        f_name, l_name, phone, address, pet_name, fav_drink = classes.FamilyContact.set_details()
                        contacts_dict[contact_id] = classes.FamilyContact(contact_id, f_name, l_name, phone, address, pet_name, fav_drink)
                        contact_id += 1
                        break
                    case 'WC':
                        #same as above but object created as instance of WorkContact class
                        console.print(Panel.fit("[magenta]Enter your Contact's details", title="[cyan]Adding a Work Contact"))
                        f_name, l_name, phone, address, w_address, w_phone, skills = classes.WorkContact.set_details()
                        contacts_dict[contact_id] = classes.WorkContact(contact_id, f_name, l_name, phone, address, w_address, w_phone, skills)
                        contact_id += 1
                        break
                    #return to home menu
                    case 'H':
                        break
                    #Exit Application
                    case 'Q':
                        sys.exit()
        #Edit a contact         
        case 'E':
            # variable used to control while loop
            search_again = True

            #If contacts dict is empty, show error message
            if not contacts_dict:
                os.system('cls||clear')
                search_again = False
                console.print(Panel.fit('[magenta]You cannot edit any contacts.\nYour Contacts Book is empty.', title='[cyan]Editing a Contact'))
                prompt = Prompt.ask("Press Enter to continue...", default="")

            #while search_again is true prompt user to enter a name to search for
            while search_again:
                os.system('cls||clear')
                console.print(Panel.fit('[magenta]Search for a contact to edit', title='[cyan]Editing a Contact'))
                edit_choice = input('Enter a contact name to edit >> ')

                #iterate through contacts_dict
                #if value is found match case v.class_type - This allows calling the correct class methods to edit the contact
                for v in contacts_dict.values():
                    if v.f_name == edit_choice:
                        match v.class_type:
                            case 'c':
                                #call function that shows promps confirming user wants to edit a contact
                                #returns false if user doesnt want to edit and breaks out of for loop
                                if not f.confirm_edit(v):
                                    search_again = False
                                    break
                                #user confirms edit and set_details method is called to edit contact
                                # search_again set to false to end while loop
                                f_name, l_name, phone = classes.Contact.set_details()
                                v.update_contact(f_name, l_name, phone)
                                search_again = False
                                break
                                #same as above but editing an instance of CloseContact class
                            case 'cc':
                                if not f.confirm_edit(v):
                                    search_again = False
                                    break
                                f_name, l_name, phone, address = classes.CloseContact.set_details()
                                v.update_contact(f_name, l_name, phone, address)
                                search_again = False
                                break
                            case 'fc':
                                #same as above but editing an instance of FamilyContact class
                                if not f.confirm_edit(v):
                                    search_again = False
                                    break
                                f_name, l_name, phone, address, pet, drink = classes.FamilyContact.set_details()
                                v.update_contact(f_name, l_name, phone, address, pet, drink)
                                search_again = False
                                break
                            case 'wc':
                                #same as above but editing an instance of WorkContact class
                                if not f.confirm_edit(v):
                                    search_again = False
                                    break
                                f_name, l_name, phone, address, w_address, w_phone, skills = classes.WorkContact.set_details()
                                v.update_contact(f_name, l_name, phone, address, w_address, w_phone, skills)
                                search_again = False
                                break
                #contact was not fouund
                #user can search again or exit
                else:
                    os.system('cls||clear')
                    console.print(Panel.fit('[magenta]That contact does not exist', title='[cyan]Editing a Contact'))
                    search_again = Confirm.ask('Would you like to search for another contact to edit?')

        #Edit a contact  
        case 'D':
            # variable used to control while loop
            search_again = True

            #If contacts dict is empty, show error message
            if not contacts_dict:
                os.system('cls||clear')
                search_again = False
                console.print(Panel.fit('[magenta]You cannot delete any contacts.\nYour Contacts Book is empty.', title='[cyan]Deleting a Contact'))
                prompt = Prompt.ask("Press Enter to continue...", default="")

            #while search_again is true prompt user to enter a name to search for
            while search_again:
                os.system('cls||clear')
                console.print(Panel.fit('[magenta]Search for a contact to delete', title='[cyan]Deleting a Contact'))
                del_choice = input('Enter a contact name to delete >> ')

                #iterate through contacts_dict
                #if contact found, prompt user to delete contact
                for k, v in contacts_dict.items():
                    if v.f_name == del_choice:
                        print(v.get_details())
                        confirm_delete = Confirm.ask(f'A you sure you want to delete {v.f_name} {v.l_name} ?')
                        if confirm_delete:
                            del contacts_dict[k]
                            search_again = False
                            break
                #contact no found
                #user can search again or exit
                else:
                    os.system('cls||clear')
                    console.print(Panel.fit('[magenta]That contact does not exist', title='[cyan]Deleting a Contact'))
                    search_again = Confirm.ask('Would you like to search for another contact to delete?')
        
        #Display a contact
        case 'DC':
            # variable used to control while loop
            search_again = True

            #If contacts dict is empty, show error message
            if not contacts_dict:
                os.system('cls||clear')
                search_again = False
                console.print(Panel.fit('[magenta]You cannot display any contacts.\nYour Contacts Book is empty.', title='[cyan]Displaying a Contact'))
                prompt = Prompt.ask("Press Enter to continue...", default="")

            #while search_again is true prompt user to enter a name to search for
            while search_again:
                os.system('cls||clear')
                console.print(Panel.fit('[magenta]Search for a contact to display', title='[cyan]Displaying a Contact'))
                display_choice = input('Enter a contact name to edit >> ')

                #iterate through contacts_dict
                #if contact found, prompt user to search for another contact
                for v in contacts_dict.values():
                    if v.f_name == display_choice:
                        print(v.get_details())
                        confirm_delete = Confirm.ask('Do you want to search for another contact? ?')
                        if not confirm_delete:
                            search_again = False
                            break
                        break
                #contact no found
                #user can search again or exit
                else:
                    os.system('cls||clear')
                    console.print(Panel.fit('[magenta]That contact does not exist', title='[cyan]Displaying a Contact'))
                    search_again = Confirm.ask('Would you like to search for another contact to Display?')
        
        #Display all contacts
        case 'DA':
            # variable used to control while loop
            search_again = True

            # If contacts dict is empty, show error message
            if not contacts_dict:
                os.system('cls||clear')
                search_again = False
                console.print(Panel.fit('[magenta]You cannot display any contacts.\nYour Contacts Book is empty.', title='[cyan]Displaying all Contacts'))
                prompt = Prompt.ask("Press Enter to continue...", default="")

            #iterate through contacts_dict and display contacts
            #prompt user to continer then go back to main menu
            for k, v in contacts_dict.items():
                print('==========================================')
                print(v.get_details())
                print('\n==========================================')
                prompt = Prompt.ask("Press Enter to continue...", default="")

        case 'Q':
            break






