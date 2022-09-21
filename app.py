#Importing modules
import os
import sys
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.console import Console
# from rich import print
from rich.table import Table
from rich.panel import Panel
from tinydb import TinyDB
from tinydb import Query



# #importing classes and functions
# import classes
# import functions as f

def contacts_app():

    # ////////////////////////////////////////////////////////////CLASSES///////////////////////////////////////////////////////////////////

    # import functions as f

    #base class - minimum information stored in this class
    class Contact:
        def __init__(self, id, f_name, l_name, phone, class_type='c'):
            self.id = id
            self.f_name = f_name
            self.l_name = l_name
            self.phone = phone
            self.class_type = class_type
        
        #this method allows user input to be gathered before the object is created
        @classmethod
        def set_details(cls):

            #calling functions to validate user input
            first_name = validate_name('First')
            last_name = validate_name('Last')
            phone = validate_phone()

            #user input is returned
            return first_name, last_name, phone

    #new class with more detailed information
    class CloseContact(Contact):
        def __init__(self, id, f_name, l_name, phone, address, class_type='cc'):
            super().__init__(id, f_name, l_name, phone)
            self.address = address
            self.class_type = class_type

        #class method inherits all input from from derived set_details method
        #adds extra input for address
        @classmethod
        def set_details(cls):
            first_name, last_name, phone = super().set_details()
            address = input('Enter Address >> ')

            #user input is returned
            return first_name, last_name, phone, address

    class FamilyContact(CloseContact):
        def __init__(self, id, f_name, l_name, phone, address, pet_name, fav_drink, class_type='fc'):
            super().__init__(id, f_name, l_name, phone, address)
            self.pet_name = pet_name
            self.fav_drink = fav_drink
            self.class_type = class_type

        #class method inherits all input from from derived set_details method
        #adds extra input for pet name and fav_drink
        @classmethod
        def set_details(cls):
            first_name, last_name, phone, address = super().set_details()
            pet_name = input('Enter Pet\'s Name >> ')
            fav_drink = input('Enter Favourite Drink >> ')

            #user input is returned
            return first_name, last_name, phone, address, pet_name, fav_drink
                
    class WorkContact(CloseContact):
        def __init__(self, id, f_name, l_name, phone, address, work_address, work_phone, skills, class_type='wc'):
            super().__init__(id, f_name, l_name, phone, address)
            self.work_address = work_address
            self.work_phone = work_phone
            self.skills = skills
            self.class_type = class_type


        #class method inherits all input from from derived set_details method
        #adds extra input for work address, work phone and skills
        @classmethod
        def set_details(cls):
            first_name, last_name, phone, address = super().set_details()
            work_address = input('Enter Work Address >> ')
            
            #validate user input for phone number
            work_phone = validate_phone()
            
            skills = input('Enter Skills >> ')

            #user input is returned
            return first_name, last_name, phone, address, work_address, work_phone, skills

    # ////////////////////////////////////////////////////////////CLASSES///////////////////////////////////////////////////////////////////

    # ////////////////////////////////////////////////////////////FUNCTIONS///////////////////////////////////////////////////////////////////

    def menu_prompt():
        """_summary_
            Menu_prompt function clears the screen each time and displays a table with Home Menu options and keyboard keys to access menu
        """   
        #clear screen and create and instance of Console from Rich module
        os.system('cls||clear')
        console = Console()

        print()
        console.print(
            Panel.fit("[magenta]\nPlease make a selection   \nfrom the menu below\n",
            title="[cyan]Home")
        )
        
        #create a table
        table = Table()
    
        #add columns and headings
        table.add_column('Home | Operation', style='cyan', justify='left', no_wrap=True)
        table.add_column('Key', justify='left', style='magenta')

        #add rows with menu options
        table.add_row('Add Contact', 'A')
        table.add_row('Edit Contact', 'E')
        table.add_row('Delete Contact', 'D')
        table.add_row('Display Contact', 'DC')
        table.add_row('Display all Contacts', 'DA')
        table.add_row('Quit Application', 'Q')

        #display table
        console.print(table)

    def add_contact_prompt():
        """_summary_
            add_contact_prompt function clears the screen each time and displays a table with Add Contact Menu options and keyboard keys to access menu
        """  
        #clear screen and create and instance of Console from Rich module  
        os.system('cls||clear')
        console = Console()

        print()
        console.print(
            Panel.fit("[magenta]\nPlease make a selection from the\nmenu below\n",
            title="[cyan]Add Contact")
        )
        #create a table
        table = Table()
        
        #add columns and headings
        table.add_column('Add | Operation', style='cyan', justify='left', no_wrap=True)
        table.add_column('Key', justify='left', style='magenta')

        #add rows with menu options
        table.add_row('Add Contact', 'C')
        table.add_row('Add Close Contact', 'CC')
        table.add_row('Add Family Contact Contact', 'FC')
        table.add_row('Add Work Contact', 'WC')
        table.add_row('Home', 'H')
        table.add_row('Quit Application', 'Q')

        #display table
        console.print(table)


    def display_table(list):
        """_summary_
            display_table function recives a list of search results and dsiplays them in a table
        Args:
            list (list): a list of results matching user's search input
        """

        #clear screen and create and instance of Console from Rich module 
        os.system('cls||clear')
        console = Console()

        #create a table
        table = Table(title="Your Contacts")

        #add columns and headings
        table.add_column("Id", style="cyan", no_wrap=True)
        table.add_column("First name", style="magenta")
        table.add_column("Last name", style="magenta")
        table.add_column("Phone", style="green")
        table.add_column("Address", style="green")
        table.add_column("Pet", style="green")
        table.add_column("Favourite Drink", style="green")
        table.add_column("Work Address", style="green")
        table.add_column("Work Phone", style="green")
        table.add_column("Skills", style="green")

        #iterate through list of results to add each row to the table.
        #if / elif used to print each type of contact - Contact, Close Contact, Family Contact, Work Contact
        for idx, val in enumerate(list):
            if len(val) == 5:
                table.add_row(list[idx]['id'], list[idx]['first_name'], list[idx]['last_name'], list[idx]['phone'])
            elif len(val) == 6:
                table.add_row(list[idx]['id'], list[idx]['first_name'], list[idx]['last_name'], list[idx]['phone'],  list[idx]['address'])
            elif len(val) == 8:
                table.add_row(list[idx]['id'], list[idx]['first_name'], list[idx]['last_name'], list[idx]['phone'],  list[idx]['address'], list[idx]['pet'], list[idx]['fav_drink'])
            elif len(val) == 9:
                table.add_row(list[idx]['id'], list[idx]['first_name'], list[idx]['last_name'], list[idx]['phone'],  list[idx]['address'], '', '', list[idx]['work_address'], list[idx]['work_phone'], list[idx]['skills'])

        #display table
        console.print(table)


    def continue_prompt():
        """_summary_
            Prompts user to press Enter to continue. Execution is frozen untill keypress
        Returns:
            string: returns user input. Used for ID selection for multipe search results. No need for error
            correction here as its done in the while look with a generator expression
        """  
        console = Console()
        with console.status('Press Enter to continue...'):  
            prompt = Prompt.ask('', default='')

        return prompt

    def add_contact(id, contact_type, first_name, last_name, phone, address, pet_name, fav_drink, work_address, work_phone, skills):
        """_summary_
        add_contact will receive as arguments all the available variables for all the four types of contacts.
        When the function is called, arguments that arent needed are set to None.
        If statments and booleans based on conrtact type are used to reduce repeition of variables that are used by all the contact
        types - first_name, last_name, phone etc.
        Args:
            id (_type_): string
            contact_type (_type_): string
            first_name (_type_): string
            last_name (_type_): string
            phone (_type_): string or None
            address (_type_): string or None
            pet_name (_type_): string or None
            fav_drink (_type_): string or None
            work_address (_type_): string or None
            work_phone (_type_): string or None
            skills (_type_): string or None

        Returns:
            _type_: dictionary
        """    
        if contact_type == 'Contact' or contact_type == 'Close Contact' or contact_type == 'Family Contact' or contact_type == 'Work Contact':
            contact = {'id': str(id), 'type': contact_type, 'first_name': first_name, 'last_name': last_name, 'phone': phone}

            if contact_type == 'Contact':
                return contact

        if contact_type == 'Close Contact' or contact_type == 'Family Contact' or contact_type == 'Work Contact':
            contact['address'] = address

            if contact_type == 'Close Contact':
                return contact
        
        if contact_type == 'Family Contact':
            contact['pet'] = pet_name
            contact['fav_drink'] = fav_drink

            return contact
        
        if contact_type == 'Work Contact':
            contact['work_address'] = work_address
            contact['work_phone'] = work_phone
            contact['skills'] = skills

            return contact

    def empty_database_alert(database, action, title_action):
        """
        Function will give uesr an error when attempting to Edit, Delete, Display or Display all contacts when database is empty.

        Args:
            database (list): Contacts database
            action (string): the action being ettempted - edit delete, display.
            title_action (string): action verb for panel title

        Returns:
            boolean: return search again boolean for outer while loop
        """    
        console = Console()
        if not database:
            os.system('cls||clear')
            search_again = False
            console.print(Panel.fit(f'[magenta]\nYou cannot {action} any contacts.\nYour Contacts Book is empty.\n', title_align='left', title=f'[cyan]{title_action} a Contact'))
            continue_prompt()
            return search_again

        search_again = True
        return True

    def validate_name(string):
        """
        Function receives a string to guide user to what input they are entering.
        If string is all white space, will prompt user to enter valid name.
        Returns the string stripped of leading and trailing whitespace.
        Args:
            string (string): Name to prompt user on what data they are inputing

        Returns:
            string: sting with no leading or trailing spaces
        """  

        user_input = input(f'Enter {string} Name >> ')

        while len(user_input) < 1 or user_input.isspace():

            print(f'You need to enter a {string} Name for your Contact!\n')
            user_input = input(f'Enter {string} Name >> ')

        return user_input.strip()
        
    def validate_phone():
        """
        User input is stripped of leading and trailing white space.
        user input is copied in a temp variable. then all spaces are removed from string.
        isdigit is used to test whether onl numbers have been entered.
        Once string is just numbers, assign phone temp to phone - phone is a copy of phone temp but
        with the original whitespace inbetween numbers.
        Returns:
            string: returns a string that is numeric only and no leading or trailing whitespace.
            White space is allowed inbetween numbers.
        """    
        phone = input('Enter Phone Number >> ').strip()
        while True:
            phone_temp = phone
            phone_test = phone_temp.replace(' ','')

            if not phone_test.isdigit():
                print('Phone number can only contain numbers!\n')
                phone = input('Enter Phone Number >> ').strip()
            else:
                phone = phone_temp
                break

        return phone


    def confirm_edit_delete(action, search_result_from_search, search_result_from_get=None):
        console = Console()
        display_table(search_result_from_search)
        print()
        if len(search_result_from_search) > 1:
            console.print(Panel.fit(f'\nContact Selected - [cyan]{search_result_from_get["id"]}[/cyan]: [magenta]{search_result_from_get["first_name"]} {search_result_from_get["last_name"]}\n',
                title_align='left', title='[cyan]Contact Found!', subtitle_align='left', subtitle=f'[cyan]Confirm {action}?'))
            print()
            confirm = Confirm.ask(f'Are you sure you want to {action} [cyan]{search_result_from_get["id"]}[/cyan]: [magenta]{search_result_from_get["first_name"]} {search_result_from_get["last_name"]}[/magenta] ?')

            return confirm
        else:
            console.print(Panel.fit(f'\nContact Selected - [cyan]{search_result_from_search[0]["id"]}[/cyan]: [magenta]{search_result_from_search[0]["first_name"]} {search_result_from_search[0]["last_name"]}\n', 
                title_align='left', title='[cyan]Contact Found!', subtitle_align='left', subtitle='[cyan]Confirm edit?'))
            print()
            confirm = Confirm.ask(f'Are you sure you want to {action} [cyan]{search_result_from_search[0]["id"]}[/cyan]: [magenta]{search_result_from_search[0]["first_name"]} {search_result_from_search[0]["last_name"]}[/magenta] ?')

            return confirm


    #importing classes and functions
    # import classes
    # import functions as f


    #create instance of the tinydb Query class
    QueryDb = Query()

    #ceate instance of console for printing displays
    console = Console()

    user_id = 0

    #prompt user to open new contact book or existing contact book
    print()
    console.print(
        Panel.fit("[magenta]\nPlease Choose and option:\n\n - Open New Contacts Book\n - Open an Existing Contacts Book\n - Quit Application\n",
        title="[cyan]Welcome to your Contacts Book")
    )

    #prompting user choice using Prompt method from Rich Module
    db_choice = Prompt.ask('Please make a selection: ', choices=['New', 'Existing', 'Quit'])
    #if choice is 'New', initalise user_id to 0
    #create and instance of TinyDB clss and assign it to empty contacts json file
    #user .all method to assign contents of database to contact variable
    if db_choice == 'New':
        user_id = 0
        ContactsDb = TinyDB('contacts.json')
        ContactsDb.truncate()                #USED HERE FOR EMPTY DATABASE EACH TIME - WILL NOT SAVE CONTACTS
        contacts = ContactsDb.all()

    #choice 'Existing' 
    #create and instance of TinyDB clss and assign it to empty contacts json file
    #user .all method to assign contents of database to contact variable
    elif db_choice == 'Existing':
        ContactsDb = TinyDB('mock-data.json')
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
        menu_prompt()

        #use Prompt from rich.prompt module to give a selection menu to the user
        # assign choice to menu_choice and clear screen
        menu_choice = Prompt.ask('Please make a selection: ', choices=['A', 'E', 'D', 'DC', 'DA', 'Q'])
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
                    add_contact_prompt()
                    add_choice = Prompt.ask('Please make a selection: ', choices=['C', 'CC', 'FC', 'WC', 'H', 'Q'])
                    os.system('cls||clear')

                    #match case for different types of contacts to be created
                    match add_choice.upper():
                        case 'C':
                            contact_type = 'Contact'
                            
                            #displaying panel heading
                            #call Contact class set_details method to retrieve contact details
                            console.print(Panel.fit("[magenta]\nEnter your Contact's details\n", title="[cyan]Adding a Contact"))
                            f_name, l_name, phone = Contact.set_details()

                            #call add_contact function to create the contact with user input
                            contact = add_contact(
                                id=user_id, contact_type='Contact', first_name=f_name, last_name=l_name, phone=phone, 
                                address=None, pet_name=None, fav_drink=None, work_address=None, work_phone=None, skills=None
                                )

                            #add contact to database and increment user_id by 1
                            ContactsDb.insert(contact)
                            user_id += 1
                            break

                        case 'CC':
                            contact_type = 'Close Contact'
                            #as above

                            #call CloseContact class set_details method to retrieve contact details
                            console.print(Panel.fit("[magenta]\nEnter your Contact's details\n", title="[cyan]Adding a Close Contact"))
                            f_name, l_name, phone, address = CloseContact.set_details()

                            contact = add_contact(
                                id=user_id, contact_type='Close Contact', first_name=f_name, last_name=l_name, phone=phone, 
                                address=address, pet_name=None, fav_drink=None, work_address=None, work_phone=None, skills=None
                                )

                            ContactsDb.insert(contact)
                            user_id += 1
                            break

                        case 'FC':
                            contact_type = 'Family Contact'
                            #as above

                            #call FamilyContact class set_details method to retrieve contact details
                            console.print(Panel.fit("[magenta]\nEnter your Contact's details\n", title="[cyan]Adding a Family Contact"))
                            f_name, l_name, phone, address, pet_name, fav_drink = FamilyContact.set_details()

                            contact = add_contact(
                                id=user_id, contact_type='Family Contact', first_name=f_name, last_name=l_name, phone=phone, 
                                address=address, pet_name=pet_name, fav_drink=fav_drink, work_address=None, work_phone=None, skills=None
                                )

                            ContactsDb.insert(contact)
                            user_id += 1
                            break

                        case 'WC':
                            contact_type = 'Work Contact'
                            #as above

                            #call WorkContact class set_details method to retrieve contact details
                            console.print(Panel.fit("[magenta]\nEnter your Contact's details\n", title="[cyan]Adding a Work Contact"))
                            f_name, l_name, phone, address, w_address, w_phone, skills = WorkContact.set_details()

                            contact = add_contact(
                                id=user_id, contact_type='Work Contact', first_name=f_name, last_name=l_name, phone=phone, 
                                address=address, pet_name=None, fav_drink=None, work_address=w_address, work_phone=w_phone, skills=skills
                                )

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
                search_again = empty_database_alert(ContactsDb, 'Edit', 'Editing')

                #while search_again is true prompt user to enter a name to search for
                while search_again:
                    os.system('cls||clear')
                    console.print(Panel.fit('[magenta]\nSearch for a contact to edit\n', title_align='left', title='[cyan]Editing a Contact'))
                    edit_choice = input('Enter a contact\'s first name to edit >> ')

                    #use TinyDB search method to return matches for first name
                    #TinyDB search method will return a list of dictionaries if multiple contacts are found
                    search_result = ContactsDb.search(QueryDb.first_name == edit_choice)

                    #if contact is found iterate through database and display contact information in a table
                    if search_result:
                        display_table(search_result)

                        #if there are multiple contacts with the same first name
                        #prompt user to select ID of contact to edit
                        if len(search_result) > 1:
                            console.print(Panel.fit(f'\n[magenta]There are multiple contacts named {edit_choice}.\n', title_align='left', title='[cyan]Choose a contact ID', subtitle_align='left', subtitle='[cyan]Editing a Contact'))
                            search_id = Prompt.ask('\nSelect an ID to Edit >> ', default='Home')
                            # search_id = input('Select an ID to edit >> ')

                            if search_id == 'Home':
                                break

                            #use get method on the multiple reults to retrieve contact with ID entered
                            single_search_result = ContactsDb.get(QueryDb.id == search_id)

                            #User validation cruicial here so that correct ID is edited
                            # #generator expression to continually loop while the ID entered isnt a valid ID
                            while not next((item for item in search_result if item['id'] == search_id), None):
                                # os.system('cls||clear')
                                display_table(search_result)
                                console.print(Panel.fit(f'\n[cyan]{search_id}[/cyan] is not a valid ID.\n', title_align='left', title='[cyan]Editing a Contact'))
                                search_id = continue_prompt()
                                
                                #original ID wasn not valid, so assign the valid ID at the end of this while loop
                                single_search_result = ContactsDb.get(QueryDb.id == search_id)

                        #two seperate confirmatons are needed here. One for the result of Query.search() and one for Query.get()
                        #Query.search() returns a list of with one or more dicts and Query.get() returns a single dict

                        if len(search_result) > 1:
                            confirm_edit = confirm_edit_delete('Edit', search_result, single_search_result)
                        else:
                            confirm_edit = confirm_edit_delete('Edit', search_result)

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
                                    f_name, l_name, phone = Contact.set_details()

                                    #user input assigned to contact - using.doc_id method to assign to contact that selected by user
                                    ContactsDb.update({'first_name': f_name}, doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'last_name': l_name}, doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'phone': phone}, doc_ids=[search_result[0].doc_id])

                                case 'Close Contact':
                                    #as above
                                    f_name, l_name, phone, address = CloseContact.set_details()
                                    ContactsDb.update({'first_name': f_name}, doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'last_name': l_name}, doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'phone': phone}, doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'address': address}, doc_ids=[search_result[0].doc_id])

                                case 'Family Contact':
                                    #as above
                                    f_name, l_name, phone, address, pet_name, fav_drink = FamilyContact.set_details()
                                    ContactsDb.update({'first_name': f_name}, doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'last_name': l_name}, doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'phone': phone}, doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'address': address}, doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'pet': pet_name}, doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'fav_drink': fav_drink}, doc_ids=[search_result[0].doc_id])

                                case 'Work Contact':
                                    #as above
                                    f_name, l_name, phone, address, w_address, w_phone, skills = WorkContact.set_details()
                                    ContactsDb.update({'first_name': f_name},doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'last_name': l_name}, doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'phone': phone}, doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'address': address}, doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'work_address': w_address}, doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'work_phone': w_phone}, doc_ids=[search_result[0].doc_id])
                                    ContactsDb.update({'skills': skills}, doc_ids=[search_result[0].doc_id])

                            # prompt = Prompt.ask("Press Enter to continue...", default="")
                            prompt = continue_prompt()
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
                                    f_name, l_name, phone = Contact.set_details()

                                    #user input assigned to contact - using.doc_id method to assign to contact that selected by user
                                    ContactsDb.update({'first_name': f_name}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'last_name': l_name}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'phone': phone}, doc_ids=[single_search_result.doc_id])

                                case 'Close Contact':
                                    #as above
                                    f_name, l_name, phone, address = CloseContact.set_details()
                                    ContactsDb.update({'first_name': f_name}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'last_name': l_name}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'phone': phone}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'address': address}, doc_ids=[single_search_result.doc_id])

                                case 'Family Contact':
                                    #as above
                                    f_name, l_name, phone, address, pet_name, fav_drink = FamilyContact.set_details()
                                    ContactsDb.update({'first_name': f_name}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'last_name': l_name}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'phone': phone}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'address': address}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'pet': pet_name}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'fav_drink': fav_drink}, doc_ids=[single_search_result.doc_id])

                                case 'Work Contact':
                                    #as above
                                    f_name, l_name, phone, address, w_address, w_phone, skills = WorkContact.set_details()
                                    ContactsDb.update({'first_name': f_name}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'last_name': l_name}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'phone': phone}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'address': address}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'work_address': w_address}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'work_phone': w_phone}, doc_ids=[single_search_result.doc_id])
                                    ContactsDb.update({'skills': skills}, doc_ids=[single_search_result.doc_id])

                            # call continue_prompt function to stop screen refreshing
                            prompt = continue_prompt()
                            search_again = False
                            break

                        else:
                            break

                    #contact was not fouund
                    #user can search again or exit
                    elif not search_result:
                        os.system('cls||clear')
                        console.print(Panel.fit('\n[magenta]That contact does not exist\n', title_align='left', title='[cyan]Editing a Contact'))
                        search_again = Confirm.ask('Would you like to search for another contact to edit?')

            #Delete a contact
            case 'D':
                # variable used to control while loop
                search_again = True

                #If contacts databse is empty, show error message
                search_again = empty_database_alert(ContactsDb, 'Delete', 'Deleting')

                #while search_again is true prompt user to enter a name to search for
                while search_again:
                    os.system('cls||clear')
                    console.print(Panel.fit('\n[magenta]Search for a contact to delete\n', title_align='left', title='[cyan]Deleting a Contact'))
                    del_choice = input('Enter a contact name to delete >> ')

                    #use TinyDB search method to return matches for first name
                    #TinyDB search method will return a list of dictionaries if multiple contacts are found
                    search_result = ContactsDb.search(QueryDb.first_name == del_choice)

                    #if contact is found iterate through dict to display contact information
                    if search_result:
                        os.system('cls||clear')
                        display_table(search_result)

                        #if there are multiple contacts with the same first name
                        #prompt user to select ID of contact to edit
                        if len(search_result) > 1:
                            console.print(Panel.fit(f'\n[magenta]There are multiple contacts named {del_choice}.\n', title_align='left', title='[cyan]Choose a contact ID', subtitle_align='left', subtitle='[cyan]Deleting a Contact'))
                            # search_id = input('Select an ID to Delete >> ')

                            search_id = Prompt.ask('\nSelect an ID to Delete >> ', default='Home')

                            if search_id == 'Home':
                                break


                            #use get method to retrieve contact with ID entered
                            single_search_result = ContactsDb.get(QueryDb.id == search_id)

                            #generator expression to continually loop while the ID entered isnt a valid ID
                            while not next((item for item in search_result if item['id'] == search_id), None):
                                display_table(search_result)
                                # valid ID has not been entered. display prompt to reenter valid ID
                                console.print(Panel.fit(f'\n[cyan]{search_id}[/cyan] is not a valid ID.\n', title='[cyan]Deleting a Contact'))
                                search_id = continue_prompt()
                                
                                #original ID wasn not valid, so assign the valid ID now and exit loop
                                single_search_result = ContactsDb.get(QueryDb.id == search_id)

                        #two seperate confirmatons are needed here. One for the result of Query.search() and one for Query.get()
                        #Query.search() returns a list of with one or more dicts and Query.get() returns a single dict

                        if len(search_result) > 1:
                            confirm_delete = confirm_edit_delete('Delete', search_result, single_search_result)
                        else:
                            confirm_delete = confirm_edit_delete('Delete', search_result)

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
                        console.print(Panel.fit('\n[magenta]That contact does not exist\n', title_align='left', title='[cyan]Deleting a Contact'))
                        search_again = Confirm.ask('Would you like to search for another contact to delete?')
            
            #Display a contact
            case 'DC':
                    # variable used to control while loop
                    search_again = True

                    #If contacts databse is empty, show error message
                    search_again = empty_database_alert(ContactsDb, 'Display', 'Displaying')

                    #while search_again is true prompt user to enter a name to search for
                    while search_again:
                        os.system('cls||clear')
                        console.print(Panel.fit('\n[magenta]Search for a contact to display\n', title_align='left', title='[cyan]Displaying a Contact'))
                        display_choice = input('Enter a contact name to display >> ')

                        #use TinyDB search method to return dictionary that matches first name
                        #search will return all results matching the name.
                        search_result = ContactsDb.search(QueryDb.first_name == display_choice)

                        #if contact is found iterate through dict to display contact information
                        if search_result:
                            display_table(search_result)

                            #confirm user wants to search for another contact
                            print()
                            confirm_display = Confirm.ask('Do you want to search for another contact?')

                            # ?if user selects no, break out to home menu
                            if not confirm_display:
                                search_again = False
                                break

                        # contact no found
                        # user can search again or exit
                        else:
                            os.system('cls||clear')
                            console.print(Panel.fit('\n[magenta]That contact does not exist\n', title_align='left', title='[cyan]Displaying a Contact'))
                            search_again = Confirm.ask('Would you like to search for another contact to Display?')

            #Display all contacts
            case 'DA':
                
                #If contacts databse is empty, show error message
                search_again = empty_database_alert(ContactsDb, 'Display', 'Displaying')

                if search_again:
                # else:
                    #display the entire database in a table
                    whole_db = ContactsDb.all()
                    display_table(whole_db)
                    continue_prompt()

            case 'Q':
                break

contacts_app()