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

from tinydb import TinyDB
from tinydb import Query

#creating instnace of the TinyDB class
ContactsDb = TinyDB('contacts.json')
ContactsDb.truncate() #EMPTY JSON FOR THE MOMENT

#used for each contact's unique user id
user_id = len(ContactsDb) + 1

#create instance of the tinydb Query class
QueryDb = Query()


#ceate instance of console for printing displays
#using import print would result in all numbers being printed cyan
console = Console()

# #counter for key in dict and creating empty dict that will be id(int): contact(object)
# contact_id = 1
# contacts_dict = {}



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
                        contact_type = 'Contact'
                        #Panel printing a heading
                        #set_details method called on Contact class returns the user input -> user input
                        #create contact dictionary with set_details returned variables
                        #insert contact into TinyDB json file
                        #increment user id
                        console.print(Panel.fit("[magenta]Enter your Contact's details", title="[cyan]Adding a Contact"))
                        f_name, l_name, phone = classes.Contact.set_details()
                        contact = {'id': user_id, 'type': contact_type, 'first_name': f_name, 'last_name': l_name, 'phone': phone}
                        ContactsDb.insert(contact)
                        user_id += 1
                        break
                    case 'CC':
                        contact_type = 'Close Contact'
                        #Panel printing a heading
                        #set_details method called on CloseContact class returns the user input -> user input
                        #create contact dictionary with set_details returned variables
                        #insert contact into TinyDB json file
                        #increment user id
                        console.print(Panel.fit("[magenta]Enter your Contact's details", title="[cyan]Adding a Close Contact"))
                        f_name, l_name, phone, address = classes.CloseContact.set_details()
                        contact = {'id': user_id, 'type': contact_type, 'first_name': f_name, 'last_name': l_name, 'phone': phone, 'address': address}
                        ContactsDb.insert(contact)
                        user_id += 1
                        break
                    case 'FC':
                        contact_type = 'Family Contact'
                        #Panel printing a heading
                        #set_details method called on FamilyContact class returns the user input -> user input
                        #create contact dictionary with set_details returned variables
                        #insert contact into TinyDB json file
                        #increment user id
                        console.print(Panel.fit("[magenta]Enter your Contact's details", title="[cyan]Adding a Family Contact"))
                        f_name, l_name, phone, address, pet_name, fav_drink = classes.FamilyContact.set_details()
                        contact = {'id': user_id, 'type': contact_type, 'first_name': f_name, 'last_name': l_name, 'phone': phone, 'address': address, 'pet': pet_name, 'fav_drink': fav_drink}
                        ContactsDb.insert(contact)
                        user_id += 1
                        break
                    case 'WC':
                        contact_type = 'Work Contact'
                        #Panel printing a heading
                        #set_details method called on WorkContact class returns the user input -> user input
                        #create contact dictionary with set_details returned variables
                        #insert contact into TinyDB json file
                        #increment user id
                        console.print(Panel.fit("[magenta]Enter your Contact's details", title="[cyan]Adding a Work Contact"))
                        f_name, l_name, phone, address, w_address, w_phone, skills = classes.WorkContact.set_details()
                        contact = {'id': user_id, 'type': contact_type, 'first_name': f_name, 'last_name': l_name, 'phone': phone, 'address': address, 'work_address': w_address, 'work_phone': w_phone, 'skills': skills}
                        ContactsDb.insert(contact)
                        user_id += 1
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

            #If contacts databse is empty, show error message
            if not ContactsDb:
                os.system('cls||clear')
                search_again = False
                console.print(Panel.fit('[magenta]You cannot edit any contacts.\nYour Contacts Book is empty.', title='[cyan]Editing a Contact'))
                prompt = Prompt.ask("Press Enter to continue...", default="")

            #while search_again is true prompt user to enter a name to search for
            while search_again:
                os.system('cls||clear')
                console.print(Panel.fit('[magenta]Search for a contact to edit', title='[cyan]Editing a Contact'))
                edit_choice = input('Enter a contact\'s first name to edit >> ')

                search_result = ContactsDb.search(QueryDb.first_name == edit_choice)

                if search_result:
                    os.system('cls||clear')
                    console.print(Panel.fit('[magenta]Searching for the contact......', title='[cyan]Editing a Contact'))
                    for idx, v in enumerate(search_result):
                        print('===================')
                        for key, val in search_result[idx].items():
                            print(f'{key}\t-----> {val}')
                        print('===================')
                    confirm_edit = Confirm.ask('Are you sure you want to edit contact....')

                    if confirm_edit:
                        match search_result[0]['type']:
                            case 'Contact':
                                f_name, l_name, phone = classes.Contact.set_details()
                                ContactsDb.update({'first_name': f_name}, QueryDb.first_name == search_result[0]['first_name'])
                                ContactsDb.update({'last_name': l_name}, QueryDb.last_name == search_result[0]['last_name'])
                                ContactsDb.update({'phone': phone}, QueryDb.phone == search_result[0]['phone'])

                            case 'Close Contact':
                                f_name, l_name, phone, address = classes.CloseContact.set_details()
                                ContactsDb.update({'first_name': f_name}, QueryDb.first_name == search_result[0]['first_name'])
                                ContactsDb.update({'last_name': l_name}, QueryDb.last_name == search_result[0]['last_name'])
                                ContactsDb.update({'phone': phone}, QueryDb.phone == search_result[0]['phone'])
                                ContactsDb.update({'address': address}, QueryDb.address == search_result[0]['address'])

                            case 'Family Contact':
                                f_name, l_name, phone, address, pet_name, fav_drink = classes.FamilyContact.set_details()
                                ContactsDb.update({'first_name': f_name}, QueryDb.first_name == search_result[0]['first_name'])
                                ContactsDb.update({'last_name': l_name}, QueryDb.last_name == search_result[0]['last_name'])
                                ContactsDb.update({'phone': phone}, QueryDb.phone == search_result[0]['phone'])
                                ContactsDb.update({'address': address}, QueryDb.address == search_result[0]['address'])
                                ContactsDb.update({'pet': pet_name}, QueryDb.pet == search_result[0]['pet'])

                            case 'Work Contact':
                                f_name, l_name, phone, address, w_address, w_phone, skills = classes.WorkContact.set_details()
                                ContactsDb.update({'first_name': f_name}, QueryDb.first_name == search_result[0]['first_name'])
                                ContactsDb.update({'last_name': l_name}, QueryDb.last_name == search_result[0]['last_name'])
                                ContactsDb.update({'phone': phone}, QueryDb.phone == search_result[0]['phone'])
                                ContactsDb.update({'address': address}, QueryDb.address == search_result[0]['address'])
                                ContactsDb.update({'work_address': w_address}, QueryDb.work_address == search_result[0]['work_address'])
                                ContactsDb.update({'work_phone': w_phone}, QueryDb.work_phone == search_result[0]['work_phone'])
                                ContactsDb.update({'skills': skills}, QueryDb.skills == search_result[0]['skills'])

                        prompt = Prompt.ask("Press Enter to continue...", default="")
                        search_again = False
                        break
                    else:
                        break
                #contact was not fouund
                #user can search again or exit
                else:
                    os.system('cls||clear')
                    console.print(Panel.fit('[magenta]That contact does not exist', title='[cyan]Editing a Contact'))
                    search_again = Confirm.ask('Would you like to search for another contact to edit?')

        #Delete a contact
        case 'D':
            # variable used to control while loop
            search_again = True

            #If contacts dict is empty, show error message
            if not ContactsDb:
                os.system('cls||clear')
                search_again = False
                console.print(Panel.fit('[magenta]You cannot delete any contacts.\nYour Contacts Book is empty.', title='[cyan]Deleting a Contact'))
                prompt = Prompt.ask("Press Enter to continue...", default="")

            #while search_again is true prompt user to enter a name to search for
            while search_again:
                os.system('cls||clear')
                console.print(Panel.fit('[magenta]Search for a contact to delete', title='[cyan]Deleting a Contact'))
                del_choice = input('Enter a contact name to delete >> ')

                search_result = ContactsDb.search(QueryDb.first_name == del_choice)

                if search_result:
                    os.system('cls||clear')
                    console.print(Panel.fit('[magenta]Searching for the contact......', title='[cyan]Deleting a Contact'))
                    for idx, v in enumerate(search_result):
                        print('===================')
                        for key, val in search_result[idx].items():
                            print(f'{key}\t-----> {val}')
                        print('===================')
                    confirm_delete = Confirm.ask('Are you sure you want to Delete contact....')

                    if confirm_delete:
                        ContactsDb.remove(QueryDb.first_name == search_result[0]['first_name'])
                        search_again = False
                
                #contact was not fouund
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
                if not ContactsDb:
                    os.system('cls||clear')
                    search_again = False
                    console.print(Panel.fit('[magenta]You cannot display any contacts.\nYour Contacts Book is empty.', title='[cyan]Displaying a Contact'))
                    prompt = Prompt.ask("Press Enter to continue...", default="")

                #while search_again is true prompt user to enter a name to search for
                while search_again:
                    os.system('cls||clear')
                    console.print(Panel.fit('[magenta]Search for a contact to display', title='[cyan]Displaying a Contact'))
                    display_choice = input('Enter a contact name to display >> ')

                    search_result = ContactsDb.search(QueryDb.first_name == display_choice)

                    if search_result:
                        os.system('cls||clear')
                        console.print(Panel.fit('[magenta]Searching for the contact......', title='[cyan]Displaying a Contact'))
                        for idx, v in enumerate(search_result):
                            print('===================')
                            for key, val in search_result[idx].items():
                                print(f'{key}\t-----> {val}')
                            print('===================')
                        confirm_display = Confirm.ask('Do you want to search for another contact? ?')
                        if not confirm_display:
                            search_again = False
                            break
                    # contact no found
                    # user can search again or exit
                    else:
                        os.system('cls||clear')
                        console.print(Panel.fit('[magenta]That contact does not exist', title='[cyan]Displaying a Contact'))
                        search_again = Confirm.ask('Would you like to search for another contact to Display?')








            # # variable used to control while loop
            # search_again = True

            # #If contacts dict is empty, show error message
            # if not contacts_dict:
            #     os.system('cls||clear')
            #     search_again = False
            #     console.print(Panel.fit('[magenta]You cannot display any contacts.\nYour Contacts Book is empty.', title='[cyan]Displaying a Contact'))
            #     prompt = Prompt.ask("Press Enter to continue...", default="")

            # #while search_again is true prompt user to enter a name to search for
            # while search_again:
            #     os.system('cls||clear')
            #     console.print(Panel.fit('[magenta]Search for a contact to display', title='[cyan]Displaying a Contact'))
            #     display_choice = input('Enter a contact name to edit >> ')

            #     #iterate through contacts_dict
            #     #if contact found, prompt user to search for another contact
            #     for v in contacts_dict.values():
            #         if v.f_name == display_choice:
            #             print(v.get_details())
            #             confirm_delete = Confirm.ask('Do you want to search for another contact? ?')
            #             if not confirm_delete:
            #                 search_again = False
            #                 break
            #             break
                #contact no found
                #user can search again or exit
                # else:
                #     os.system('cls||clear')
                #     console.print(Panel.fit('[magenta]That contact does not exist', title='[cyan]Displaying a Contact'))
                #     search_again = Confirm.ask('Would you like to search for another contact to Display?')
        
        #Display all contacts
        case 'DA':
                whole_db = ContactsDb.all()
                for idx, v in enumerate(whole_db):
                    print('===================')
                    for key, val in whole_db[idx].items():
                        print(f'{key}\t-----> {val}')
                    print('===================')

                prompt = Prompt.ask("Press Enter to continue...", default="")

        case 'Q':
            break






