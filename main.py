#Importing modules
import os
import sys
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.console import Console
from rich.panel import Panel
from tinydb import TinyDB
from tinydb import Query

#use this when importing classes and functions for PyPI packaging
# import my_contacts.classes as classes
# import my_contacts.functions as f

#importing classes and functions modules
import functions as f
import classes



#create instance of the tinydb Query class
QueryDb = Query()

#ceate instance of console for printing displays
console = Console()

#prompt user to open new contact book or existing contact book
os.system('cls||clear')
print()
console.print(
    Panel.fit("""[magenta]\nPlease Choose and option:
    \n\n - Open New Contacts Book\n - Open an Existing Contacts Book\n - Quit Application\n""",
    title="[cyan]Welcome to your Contacts Book")
)

#prompting user choice using Prompt method from Rich Module
db_choice = Prompt.ask('Please make a selection: ', choices=['New', 'Existing', 'Quit'])
#if choice is 'New', initalise user_id to 0
#create and instance of TinyDB clss and assign it to empty contacts json file
#user .all method to assign contents of database to contact variable
if db_choice == 'New':
    user_id = 0
    ContactsDb = TinyDB('./data/contacts.json')
    #truncate here to start a new database each time the application is run
    ContactsDb.truncate()                
    contacts = ContactsDb.all()

#choice 'Existing'
#create and instance of TinyDB clss and assign it to empty contacts json file
#user .all method to assign contents of database to contact variable
elif db_choice == 'Existing':
    user_id = 0
    ContactsDb = TinyDB('./data/mock-data.json')
    contacts = ContactsDb.all()

#quit application
elif db_choice == 'Quit':
    sys.exit()

#assigning unique ID variable for user contact
#iterate over database entries to find the last (highest) id generated by TinyDB
for contact in contacts:
    user_id = contact.doc_id

#increment user_id to make it 1 above current last id.
user_id += 1

#variable for user menu choice - used to match case
menu_choice = None

#While true will always loop.
#Break statments and match caes 'Q' to quit will end the application
#show menu and get user's menu choice
while True:
    #call function to display menu
    f.menu_prompt()

    #use Prompt from rich.prompt module to give a selection menu to the user
    # assign choice to menu_choice and clear screen
    menu_choice = Prompt.ask('Please make a selection: ',
    choices=['A', 'E', 'D', 'DC', 'DA', 'Q'])
    os.system('cls||clear')

    # match case user input with upper for A, E, D, DC, DA, Q to quit Application
    match menu_choice:

        #Add a contact
        case 'A':
            #new while loop and match case to choose what type of contact to enter
            #While true will always loop.
            #Break statments and match case 'Q' to quit will end the application
            while True:

                #call function to display add contact menu
                #use Prompt from rich.prompt module to give a selection menu to the user and assign choice to add_choice
                f.add_contact_prompt()
                add_choice = Prompt.ask('Please make a selection: ',
                choices=['C', 'CC', 'FC', 'WC', 'H', 'Q'])
                os.system('cls||clear')

                #match case for different types of contacts to be created
                match add_choice.upper():
                    case 'C':
                        contact_type = 'Contact'

                        #displaying panel heading
                        #call Contact class set_details method to retrieve contact details
                        console.print(Panel.fit("[magenta]\nEnter your Contact's details\n",
                        title="[cyan]Adding a Contact"))
                        f_name, l_name, phone = classes.Contact.set_details()

                        #call add_contact function to create the contact with user input
                        contact = f.add_contact(
                            id=user_id, contact_type='Contact', first_name=f_name,
                            last_name=l_name, phone=phone, address=None, pet_name=None,
                            fav_drink=None, work_address=None, work_phone=None, skills=None
                            )

                        #add contact to database and increment user_id by 1
                        ContactsDb.insert(contact)
                        user_id += 1
                        # break

                    case 'CC':
                        contact_type = 'Close Contact'
                        #as above

                        #call CloseContact class set_details method to retrieve contact details
                        console.print(Panel.fit("[magenta]\nEnter your Contact's details\n",
                        title="[cyan]Adding a Close Contact"))
                        f_name, l_name, phone, address = classes.CloseContact.set_details()

                        contact = f.add_contact(
                            id=user_id, contact_type='Close Contact', first_name=f_name,
                            last_name=l_name, phone=phone, address=address, pet_name=None,
                            fav_drink=None, work_address=None, work_phone=None, skills=None
                            )

                        ContactsDb.insert(contact)
                        user_id += 1
                        # break

                    case 'FC':
                        contact_type = 'Family Contact'
                        #as above

                        #call FamilyContact class set_details method to retrieve contact details
                        console.print(Panel.fit("[magenta]\nEnter your Contact's details\n",
                        title="[cyan]Adding a Family Contact"))
                        f_name, l_name, phone, address, pet_name, fav_drink = classes.FamilyContact.set_details()

                        contact = f.add_contact(
                            id=user_id, contact_type='Family Contact', first_name=f_name,
                            last_name=l_name, phone=phone, address=address, pet_name=pet_name,
                            fav_drink=fav_drink, work_address=None, work_phone=None, skills=None
                            )

                        ContactsDb.insert(contact)
                        user_id += 1
                        # break

                    case 'WC':
                        contact_type = 'Work Contact'
                        #as above

                        #call WorkContact class set_details method to retrieve contact details
                        console.print(Panel.fit("[magenta]\nEnter your Contact's details\n",
                        title="[cyan]Adding a Work Contact"))
                        f_name, l_name, phone, address, w_address, w_phone, skills = classes.WorkContact.set_details()

                        contact = f.add_contact(
                            id=user_id, contact_type='Work Contact', first_name=f_name,
                            last_name=l_name, phone=phone, address=address, pet_name=None,
                            fav_drink=None, work_address=w_address, work_phone=w_phone, skills=skills
                            )

                        ContactsDb.insert(contact)
                        user_id += 1
                        # break

                    #return to home menu
                    case 'H':
                        break

                    #Exit Application
                    case 'Q':
                        sys.exit()

        #Edit a contact         
        case 'E':
            # variable used to control while loop
            # becomes False when user no longer wants to search for a contact
            search_again = True

            #If contacts databse is empty, show error message
            search_again = f.empty_database_alert(ContactsDb, 'Edit', 'Editing')

            #while search_again is true prompt user to enter a name to search for
            while search_again:
                os.system('cls||clear')
                console.print(Panel.fit('[magenta]\nSearch for a contact to edit\n',
                title_align='left', title='[cyan]Editing a Contact'))
                edit_choice = input('Enter a contact\'s first name to edit >> ')

                #use TinyDB search method to return matches for first name
                #TinyDB search method will return a list of dictionaries
                #if multiple contacts are found
                search_result = ContactsDb.search(QueryDb.first_name == edit_choice)

                #if contact is found iterate through database
                # and display contact information in a table
                if search_result:
                    f.display_table(search_result)

                    #if there are multiple contacts with the same first name
                    #prompt user to select ID of contact to edit
                    if len(search_result) > 1:
                        console.print(Panel.fit(f'\n[magenta]There are multiple contacts named {edit_choice}.\n',
                        title_align='left', title='[cyan]Choose a contact ID',
                        subtitle_align='left', subtitle='[cyan]Editing a Contact'))
                        search_id = Prompt.ask('\nSelect an ID to Edit >> ', default='Home')

                        #If deault of home is selected break to menu
                        if search_id == 'Home':
                            break

                        #use get method on the multiple reults to retrieve contact with ID entered
                        single_search_result = ContactsDb.get(QueryDb.id == search_id)

                        # #generator expression to continually loop while the ID entered isnt a valid ID
                        while not next((item for item in search_result if item['id'] == search_id), None):

                            f.display_table(search_result)
                            # valid ID has not been entered. display prompt to re-enter valid ID
                            console.print(Panel.fit(f'\n[cyan]{search_id}[/cyan] is not a valid ID.\n',
                            title_align='left', title='[cyan]Editing a Contact'))
                            search_id = input('\nSelect an ID to Edit >> ')
        
                            #original ID wasn not valid, so assign the valid ID at the end of this while loop
                            single_search_result = ContactsDb.get(QueryDb.id == search_id)

                    #two seperate confirmatons are needed here.
                    #One for the result of Query.search() and one for Query.get()
                    #Query.search() returns a list of with one or more dicts
                    #and Query.get() returns a single dict

                    if len(search_result) > 1:
                        confirm_edit = f.confirm_edit_delete('Edit', search_result, single_search_result)
                    else:
                        confirm_edit = f.confirm_edit_delete('Edit', search_result)

                    #match case for contact, Close contact, Family contact and work contact
                    #once contact type is established upse tinyDB update method to update contact with that ID
                    #this match case is for when only a single result is found and returned by TinySB search() method
                    #Second match case is used for when multiple contacts are found and get() method is subsequently used to select single contact with ID

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
                        prompt = f.continue_prompt()
                        search_again = False
                        break

                    #match case for contact, Close contact, Family contact and work contact
                    #once contact type is established upse tinyDB update method to update contact with that ID
                    #Previous match case is for when only a single result is found and returned by TinySB search() method
                    ##This match case is used for when multiple contacts are found and get() method is subsequently used to select single contact with ID

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
                                ContactsDb.update({'first_name': f_name}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'last_name': l_name}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'phone': phone}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'address': address}, doc_ids=[single_search_result.doc_id])

                            case 'Family Contact':
                                #as above
                                f_name, l_name, phone, address, pet_name, fav_drink = classes.FamilyContact.set_details()
                                ContactsDb.update({'first_name': f_name}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'last_name': l_name}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'phone': phone}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'address': address}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'pet': pet_name}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'fav_drink': fav_drink}, doc_ids=[single_search_result.doc_id])

                            case 'Work Contact':
                                #as above
                                f_name, l_name, phone, address, w_address, w_phone, skills = classes.WorkContact.set_details()
                                ContactsDb.update({'first_name': f_name}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'last_name': l_name}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'phone': phone}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'address': address}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'work_address': w_address}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'work_phone': w_phone}, doc_ids=[single_search_result.doc_id])
                                ContactsDb.update({'skills': skills}, doc_ids=[single_search_result.doc_id])

                        # call continue_prompt function to stop screen refreshing
                        prompt = f.continue_prompt()
                        search_again = False
                        break

                    else:
                        break

                #contact was not fouund
                #user can search again or exit
                elif not search_result:
                    os.system('cls||clear')
                    console.print(Panel.fit('\n[magenta]That contact does not exist\n',
                    title_align='left', title='[cyan]Editing a Contact'))
                    search_again = Confirm.ask('Would you like to search for another contact to edit?')

        #Delete a contact
        case 'D':
            # variable used to control while loop
            search_again = True

            #If contacts databse is empty, show error message
            search_again = f.empty_database_alert(ContactsDb, 'Delete', 'Deleting')

            #while search_again is true prompt user to enter a name to search for
            while search_again:
                os.system('cls||clear')
                console.print(Panel.fit('\n[magenta]Search for a contact to delete\n',
                title_align='left', title='[cyan]Deleting a Contact'))
                del_choice = input('Enter a contact name to delete >> ')

                #use TinyDB search method to return matches for first name
                #TinyDB search method will return a list of dictionaries if multiple contacts are found
                search_result = ContactsDb.search(QueryDb.first_name == del_choice)

                #if contact is found iterate through dict to display contact information
                if search_result:
                    os.system('cls||clear')
                    f.display_table(search_result)

                    #if there are multiple contacts with the same first name
                    #prompt user to select ID of contact to edit
                    if len(search_result) > 1:
                        console.print(Panel.fit(f'\n[magenta]There are multiple contacts named {del_choice}.\n',
                        title_align='left', title='[cyan]Choose a contact ID',
                        subtitle_align='left', subtitle='[cyan]Deleting a Contact'))

                        search_id = Prompt.ask('\nSelect an ID to Delete >> ', default='Home')

                        #If deault of home is selected break to menu
                        if search_id == 'Home':
                            break


                        #use get method to retrieve contact with ID entered
                        single_search_result = ContactsDb.get(QueryDb.id == search_id)

                        #generator expression to continually loop while the ID entered isnt a valid ID
                        while not next((item for item in search_result if item['id'] == search_id), None):
                            f.display_table(search_result)
                            # valid ID has not been entered. display prompt to reenter valid ID
                            console.print(Panel.fit(f'\n[cyan]{search_id}[/cyan] is not a valid ID.\n',
                            title='[cyan]Deleting a Contact'))
                            search_id = search_id = input('\nSelect an ID to Delete >> ')
                            
                            #original ID wasn not valid, so assign the valid ID now and exit loop
                            single_search_result = ContactsDb.get(QueryDb.id == search_id)

                    #two seperate confirmatons are needed here. One for the result of Query.search() and one for Query.get()
                    #Query.search() returns a list of with one or more dicts and Query.get() returns a single dict

                    if len(search_result) > 1:
                        confirm_delete = f.confirm_edit_delete('Delete', search_result, single_search_result)
                    else:
                        confirm_delete = f.confirm_edit_delete('Delete', search_result)

                    #deleting when multiple records have come back from search - and a single one has been selected
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
                    console.print(Panel.fit('\n[magenta]That contact does not exist\n',
                    title_align='left', title='[cyan]Deleting a Contact'))
                    search_again = Confirm.ask('Would you like to search for another contact to delete?')
        
        #Display a contact
        case 'DC':
                # variable used to control while loop
                search_again = True

                #If contacts databse is empty, show error message
                search_again = f.empty_database_alert(ContactsDb, 'Display', 'Displaying')

                #while search_again is true prompt user to enter a name to search for
                while search_again:
                    os.system('cls||clear')
                    console.print(Panel.fit('\n[magenta]Search for a contact to display\n',
                    title_align='left', title='[cyan]Displaying a Contact'))
                    display_choice = input('Enter a contact name to display >> ')

                    #use TinyDB search method to return dictionary that matches first name
                    #search will return all results matching the name.
                    search_result = ContactsDb.search(QueryDb.first_name == display_choice)

                    #if contact is found iterate through dict to display contact information
                    if search_result:
                        f.display_table(search_result)

                        #confirm user wants to search for another contact
                        print()
                        confirm_display = Confirm.ask('Do you want to search for another contact?')

                        #if user selects no, break out to home menu
                        if not confirm_display:
                            search_again = False
                            break

                    # contact no found
                    # user can search again or exit
                    else:
                        os.system('cls||clear')
                        console.print(Panel.fit('\n[magenta]That contact does not exist\n',
                        title_align='left', title='[cyan]Displaying a Contact'))
                        search_again = Confirm.ask('Would you like to search for another contact to Display?')

        #Display all contacts
        case 'DA':
            
            #If contacts databse is empty, show error message
            search_again = f.empty_database_alert(ContactsDb, 'Display', 'Displaying')

            if search_again:
            # else:
                #display the entire database in a table
                whole_db = ContactsDb.all()
                f.display_table(whole_db)
                f.continue_prompt()

        case 'Q':
            break

