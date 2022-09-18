#Importing modules
from ast import Break
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.console import Console
from rich.table import Table
# from rich import print
from rich.panel import Panel
import classes
import functions as f
import os
import sys

from tinydb import TinyDB
from tinydb import Query

#creating instnace of the TinyDB class
#ContactsDb = TinyDB('mock-data.json') #MOCK DATA JSON FILE

#creating instnace of the TinyDB class and assigning the json file
ContactsDb = TinyDB('contacts.json')
# ContactsDb.truncate() #EMPTY JSON FOR THE MOMENT ------USE THIS TO START WITH AN EMPTY DATABASE

#create unique user identifer
#iterate though database to find the ID of the last entry (highest number)
#add 1

contacts = ContactsDb.all()
for contact in contacts:
    user_id = contact.doc_id

user_id += 1

#create instance of the tinydb Query class
QueryDb = Query()

#ceate instance of console for printing displays
#using import print would result in all numbers being printed cyan
console = Console()

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
                        contact = {'id': str(user_id), 'type': contact_type, 'first_name': f_name, 'last_name': l_name, 'phone': phone}
                        ContactsDb.insert(contact)
                        user_id += 1
                        break

                    case 'CC':
                        contact_type = 'Close Contact'
                        #as above
                        console.print(Panel.fit("[magenta]Enter your Contact's details", title="[cyan]Adding a Close Contact"))
                        f_name, l_name, phone, address = classes.CloseContact.set_details()
                        contact = {'id': str(user_id), 'type': contact_type, 'first_name': f_name, 'last_name': l_name, 'phone': phone, 'address': address}
                        ContactsDb.insert(contact)
                        user_id += 1
                        break

                    case 'FC':
                        contact_type = 'Family Contact'
                        #as above
                        console.print(Panel.fit("[magenta]Enter your Contact's details", title="[cyan]Adding a Family Contact"))
                        f_name, l_name, phone, address, pet_name, fav_drink = classes.FamilyContact.set_details()
                        contact = {'id': str(user_id), 'type': contact_type, 'first_name': f_name, 'last_name': l_name, 'phone': phone, 'address': address, 'pet': pet_name, 'fav_drink': fav_drink}
                        ContactsDb.insert(contact)
                        user_id += 1
                        break

                    case 'WC':
                        contact_type = 'Work Contact'
                        #as above
                        console.print(Panel.fit("[magenta]Enter your Contact's details", title="[cyan]Adding a Work Contact"))
                        f_name, l_name, phone, address, w_address, w_phone, skills = classes.WorkContact.set_details()
                        contact = {'id': str(user_id), 'type': contact_type, 'first_name': f_name, 'last_name': l_name, 'phone': phone, 'address': address, 'work_address': w_address, 'work_phone': w_phone, 'skills': skills}
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
            # variable used to control while loop - becomes False when user no longer wants to search for a contact
            search_again = True

            #If contacts databse is empty, show error message
            if not ContactsDb:
                os.system('cls||clear')
                search_again = False
                console.print(Panel.fit('[magenta]You cannot edit any contacts.\nYour Contacts Book is empty.', title='[cyan]Editing a Contact'))
                # prompt = Prompt.ask("Press Enter to continue...", default="")
                f.press_to_continue()

            #while search_again is true prompt user to enter a name to search for
            while search_again:
                os.system('cls||clear')
                console.print(Panel.fit('[magenta]Search for a contact to edit', title='[cyan]Editing a Contact'))
                edit_choice = input('Enter a contact\'s first name to edit >> ')

                #use TinyDB search method to return dictionary that matches first name
                #search will return all results matching  first name. 

                search_result = ContactsDb.search(QueryDb.first_name == edit_choice)
                print('search result type', type(search_result))
                # print(search_result) ///////////////////////DEBUGing////////////////////////
                # f.press_to_continue()///////////////////////DEBUGing////////////////////////
                

                #if contact is found iterate through database and display contact information in a table
                if search_result:
                    os.system('cls||clear')
                    f.display_table(search_result)

                    #if there are multiple contacts with the same first name
                    #prompt user to select ID of contact to edit
                    if len(search_result) > 1:
                        search_id = input(f'\nThere are multiple contacts named {edit_choice}. Select an ID to edit >> ')
                        #use get method to retrieve contact with ID entered
                        single_search_result = ContactsDb.get(QueryDb.id == search_id)
                        print('single search result type',type(single_search_result))
                        # print(single_search_result) ///////////////////////DEBUGing////////////////////////
                        # f.press_to_continue() ///////////////////////DEBUGing////////////////////////

                        #generator expression to continually loop while the ID entered isnt a valid ID
                        while not next((item for item in search_result if item['id'] == search_id), None):
                            os.system('cls||clear')
                            f.display_table(search_result)
                            console.print(Panel.fit(f'\n[cyan]{search_id}[/cyan] is not a valid ID.', title='[cyan]Editing a Contact'))
                            # search_id = Prompt.ask('Please choose a valid ID >> ', default="")
                            search_id = f.press_to_continue()
                            
                            #original ID wasn not valid, so assign the valid ID now and exit loop
                            single_search_result = ContactsDb.get(QueryDb.id == search_id)

                    #two seperate confirmatiosn are needed here. One for the result of Query.search() and oone for Query.get()
                    #Query.search() returns a list of dicts and Query.get() returns a dict
                    if len(search_result) > 1:
                        #show Contact selected and prompt user to edit
                        os.system('cls||clear')
                        f.display_table(search_result)
                        console.print(Panel.fit(f'Contact Selected - [cyan]{single_search_result["id"]}[/cyan]: [magenta]{single_search_result["first_name"]} {single_search_result["last_name"]}', title='[cyan]Editing a Contact'))
                        confirm_edit = Confirm.ask(f'Are you sure you want to edit [cyan]{single_search_result["id"]}[/cyan]: [magenta]{single_search_result["first_name"]} {single_search_result["last_name"]}[/magenta] ?')
                    else:
                        #show Contact selected and prompt user to edit
                        os.system('cls||clear')
                        f.display_table(search_result)
                        console.print(Panel.fit(f'Contact Selected - [cyan]{search_result[0]["id"]}[/cyan]: [magenta]{search_result[0]["first_name"]} {search_result[0]["last_name"]}', title='[cyan]Editing a Contact'))
                        confirm_edit = Confirm.ask(f'Are you sure you want to edit [cyan]{search_result[0]["id"]}[/cyan]: [magenta]{search_result[0]["first_name"]} {search_result[0]["last_name"]}[/magenta] ?')
                        
                    

                    #match case for contact, Close contact, Family contact and work contact
                    #once contact type is established upse tinyDB update method to update contact with that ID
                    #this match case is for when only a single result returns using TinyDB search method
                    #MSecond match case is used for the finer search is resolved using ID

                    #using 'type' key to establish what kind of contact needs updating.
                    #lots of repitition here - need to try and DRY it
                    if confirm_edit and len(search_result) == 1:
                        match search_result[0]['type']:
                            case 'Contact':
                                #use set_details method to gather contact deatails from user
                                f_name, l_name, phone = classes.Contact.set_details()

                                #user input assigned to contact - using.doc_id method to assign to contact that selected by user
                                ContactsDb.update({'first_name': f_name}, doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'last_name': l_name}, doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'phone': phone}, doc_ids=[search_result[0].doc_id])

                            case 'Close Contact':
                                #as above
                                f_name, l_name, phone, address = classes.CloseContact.set_details()
                                ContactsDb.update({'first_name': f_name}, doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'last_name': l_name}, doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'phone': phone}, doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'address': address}, doc_ids=[search_result[0].doc_id])

                            case 'Family Contact':
                                #as above
                                f_name, l_name, phone, address, pet_name, fav_drink = classes.FamilyContact.set_details()
                                ContactsDb.update({'first_name': f_name}, doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'last_name': l_name}, doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'phone': phone}, doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'address': address}, doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'pet': pet_name}, doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'fav_drink': fav_drink}, doc_ids=[search_result[0].doc_id])

                            case 'Work Contact':
                                #as above
                                f_name, l_name, phone, address, w_address, w_phone, skills = classes.WorkContact.set_details()
                                ContactsDb.update({'first_name': f_name},doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'last_name': l_name}, doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'phone': phone}, doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'address': address}, doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'work_address': w_address}, doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'work_phone': w_phone}, doc_ids=[search_result[0].doc_id])
                                ContactsDb.update({'skills': skills}, doc_ids=[search_result[0].doc_id])

                        # prompt = Prompt.ask("Press Enter to continue...", default="")
                        prompt = f.press_to_continue()
                        search_again = False
                        break

                    #match case for contact, Close contact, Family contact and work contact
                    #once contact type is established upse tinyDB update method to update contact with that ID
                    #this match case is for when only a single result returns using TinyDB search method
                    #this match case is for when multiple records are returned - Get is the used to find single record with ID


                    #using 'type' key to establish what kind of contact needs updating.
                    #lots of repitition here - need to try and DRY it
                    elif confirm_edit and len(search_result) > 1:
                        match single_search_result['type']:
                            case 'Contact':
                                #use set_details method to gather contact deatails from user
                                f_name, l_name, phone = classes.Contact.set_details()

                                #user input assigned to contact - using.doc_id method to assign to contact that selected by user
                                ContactsDb.update({'first_name': f_name}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'last_name': l_name}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'phone': phone}, doc_ids=[single_search_result.doc_id])

                            case 'Close Contact':
                                #as above
                                f_name, l_name, phone, address = classes.CloseContact.set_details()
                                ContactsDb.update({'first_name': f_name}, single_search_result.doc_id)
                                ContactsDb.update({'last_name': l_name}, single_search_result.doc_id)
                                ContactsDb.update({'phone': phone}, single_search_result.doc_id)
                                ContactsDb.update({'address': address}, single_search_result.doc_id)

                            case 'Family Contact':
                                #as above
                                f_name, l_name, phone, address, pet_name, fav_drink = classes.FamilyContact.set_details()
                                ContactsDb.update({'first_name': f_name}, single_search_result.doc_id)
                                ContactsDb.update({'last_name': l_name}, single_search_result.doc_id)
                                ContactsDb.update({'phone': phone}, single_search_result.doc_id)
                                ContactsDb.update({'address': address}, single_search_result.doc_id)
                                ContactsDb.update({'pet': pet_name}, single_search_result.doc_id)
                                ContactsDb.update({'fav_drink': fav_drink}, single_search_result.doc_id)

                            case 'Work Contact':
                                #as above
                                f_name, l_name, phone, address, w_address, w_phone, skills = classes.WorkContact.set_details()
                                ContactsDb.update({'first_name': f_name}, single_search_result.doc_id)
                                ContactsDb.update({'last_name': l_name}, single_search_result.doc_id)
                                ContactsDb.update({'phone': phone}, single_search_result.doc_id)
                                ContactsDb.update({'address': address}, single_search_result.doc_id)
                                ContactsDb.update({'work_address': w_address}, single_search_result.doc_id)
                                ContactsDb.update({'work_phone': w_phone}, single_search_result.doc_id)
                                ContactsDb.update({'skills': skills}, single_search_result.doc_id)

                        #prompt user to press to continue. Stops screen refreshing after breaking ot of math case
                        # prompt = Prompt.ask("Press Enter to continue...", default="")
                        prompt = f.press_to_continue()
                        search_again = False
                        break

                    else:
                        break

                #contact was not fouund
                #user can search again or exit
                elif not search_result:
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
                # prompt = Prompt.ask("Press Enter to continue...", default="")
                prompt = f.press_to_continue()

            #while search_again is true prompt user to enter a name to search for
            while search_again:
                os.system('cls||clear')
                console.print(Panel.fit('[magenta]Search for a contact to delete', title='[cyan]Deleting a Contact'))
                del_choice = input('Enter a contact name to delete >> ')

                #use TinyDB search method to return dictionary that matches first name
                #search will return all results matching the name. need to add some logic to allow user to choose which contact to delete using unique ID
                search_result = ContactsDb.search(QueryDb.first_name == del_choice)

                 #if contact is found iterate through dict to display contact information
                if search_result:
                    os.system('cls||clear')
                    f.display_table(search_result)

                    #if there are multiple contacts with the same first name
                    #prompt user to select ID of contact to edit
                    if len(search_result) > 1:
                        search_id = input(f'\nThere are multiple contacts named {del_choice}. Select an ID to Delete >> ')
                        #use get method to retrieve contact with ID entered
                        single_search_result = ContactsDb.get(QueryDb.id == search_id)

                        #generator expression to continually loop while the ID entered isnt a valid ID
                        while not next((item for item in search_result if item['id'] == search_id), None):
                            os.system('cls||clear')
                            f.display_table(search_result)
                            console.print(Panel.fit(f'\n[cyan]{search_id}[/cyan] is not a valid ID.', title='[cyan]Deleting a Contact'))
                            # search_id = Prompt.ask('Please choose a valid ID >> ', default="")
                            search_id = f.press_to_continue()
                            
                            #original ID wasn not valid, so assign the valid ID now and exit loop
                            single_search_result = ContactsDb.get(QueryDb.id == search_id)
                    # #if there are multiple contacts with the same first name
                    # #prompt user to select one based on ID
                    # if len(search_result) > 1:
                    #     search_id = input('more than one result. Select an ID to edit')

                    #     #use get method to retrieve contact with ID
                    #     single_search_result = ContactsDb.get(QueryDb.id == search_id)
                    #     #PRINTING RAW STRING HERE FOR DEBUGGING
                    #     print(single_search_result['id'])

                    #two seperate confirmatiosn are needed here. One for the result of Query.search() and oone for Query.get()
                    #Query.search() returns a list of dicts and Query.get() returns a dict

                    if len(search_result) > 1:
                        #show Contact selected and prompt user to edit
                        os.system('cls||clear')
                        f.display_table(search_result)
                        console.print(Panel.fit(f'Contact Selected - [cyan]{single_search_result["id"]}[/cyan]: [magenta]{single_search_result["first_name"]} {single_search_result["last_name"]}', title='[cyan]Deleting a Contact'))
                        confirm_delete = Confirm.ask(f'Are you sure you want to delete [cyan]{single_search_result["id"]}[/cyan]: [magenta]{single_search_result["first_name"]} {single_search_result["last_name"]}[/magenta] ?')
                    else:
                        #show Contact selected and prompt user to edit
                        os.system('cls||clear')
                        f.display_table(search_result)
                        console.print(Panel.fit(f'Contact Selected - [cyan]{search_result[0]["id"]}[/cyan]: [magenta]{search_result[0]["first_name"]} {search_result[0]["last_name"]}', title='[cyan]Deleting a Contact'))
                        confirm_delete = Confirm.ask(f'Are you sure you want to delete [cyan]{search_result[0]["id"]}[/cyan]: [magenta]{search_result[0]["first_name"]} {search_result[0]["last_name"]}[/magenta] ?')
                        

                    # #show Contact selected and prompt user to edit
                    # os.system('cls||clear')
                    # f.display_table(search_result)
                    # console.print(Panel.fit(f'Contact Selected - [cyan]{single_search_result["id"]}[/cyan]: [magenta]{single_search_result["first_name"]} {single_search_result["last_name"]}', title='[cyan]Editing a Contact'))
                    # confirm_delete = Confirm.ask(f'Are you sure you want to delete [cyan]{single_search_result["id"]}[/cyan]: [magenta]{single_search_result["first_name"]} {single_search_result["last_name"]}[/magenta] ?')

                    #deleting for when multiple records have come back from search - and a single one has been selected
                    if len(search_result) > 1:
                        #delete contact
                        if confirm_delete:
                            ContactsDb.remove(QueryDb.id == single_search_result['id'])
                            search_again = False
                            break
                        else:
                            break
                    #deleting for when single record has come back from search
                    
                    elif len(search_result) == 1:
                        if confirm_delete:
                            ContactsDb.remove(QueryDb.id == search_result[0]['id'])
                            search_again = False
                            break
                        else:
                            break
                
                #contact was not fouund
                #user can search again or exit
                elif not search_result:
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
                    # prompt = Prompt.ask("Press Enter to continue...", default="")
                    prompt = f.press_to_continue()

                #while search_again is true prompt user to enter a name to search for
                while search_again:
                    os.system('cls||clear')
                    console.print(Panel.fit('[magenta]Search for a contact to display', title='[cyan]Displaying a Contact'))
                    display_choice = input('Enter a contact name to display >> ')

                    #use TinyDB search method to return dictionary that matches first name
                    #search will return all results matching the name.
                    search_result = ContactsDb.search(QueryDb.first_name == display_choice)

                    #if contact is found iterate through dict to display contact information
                    if search_result:
                        os.system('cls||clear')
                        f.display_table(search_result)

                        #confirm user wants to search for another contact
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

        #Display all contacts
        case 'DA':
            #display the entire database in a table
            whole_db = ContactsDb.all()
            f.display_table(whole_db)
            f.press_to_continue()

        case 'Q':
            break






