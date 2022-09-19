import os
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print

# User prompt fuction with information on how to use the program
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
        list (_type_): a list of results matching user's search input
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

















# ===========================functions will not edit as expected=====================
# def update_single_result_contact(data_base, result, f_name, l_name, phone):
#     data_base.update({'first_name': f_name}, doc_ids=[result[0].doc_id])
#     data_base.update({'first_name': l_name}, doc_ids=[result[0].doc_id])
#     data_base.update({'first_name': phone}, doc_ids=[result[0].doc_id])

# def update_single_result_close_contact(data_base, query, result, f_name, l_name, phone, address):
#     data_base.update({'first_name': f_name}, query.first_name == result[0]['first_name'])
#     data_base.update({'first_name': l_name}, query.first_name == result[0]['last_name'])
#     data_base.update({'first_name': phone}, query.first_name == result[0]['phone'])
#     data_base.update({'address': address}, query.address == result[0]['address'])

# def update_single_result_family_contact(data_base, query, result, f_name, l_name, phone, address, pet_name, fav_drink):
#     data_base.update({'first_name': f_name}, query.first_name == result[0]['first_name'])
#     data_base.update({'first_name': l_name}, query.first_name == result[0]['last_name'])
#     data_base.update({'first_name': phone}, query.first_name == result[0]['phone'])
#     data_base.update({'address': address}, query.address == result[0]['address'])
#     data_base.update({'pet': pet_name}, query.pet == result[0]['pet'])
#     data_base.update({'fav_drink': fav_drink}, query.fav_drink == result[0]['fav_drink'])

# def update_single_result_work_contact(data_base, query, result, f_name, l_name, phone, address, w_address, w_phone, skills):
#     data_base.update({'first_name': f_name}, query.first_name == result[0]['first_name'])
#     data_base.update({'first_name': l_name}, query.first_name == result[0]['last_name'])
#     data_base.update({'first_name': phone}, query.first_name == result[0]['phone'])
#     data_base.update({'address': address}, query.address == result[0]['address'])
#     data_base.update({'work_address': w_address}, query.work_address == result[0]['work_address'])
#     data_base.update({'work_phone': w_phone}, query.work_phone == result[0]['work_phone'])
#     data_base.update({'skills': skills}, query.skills == result[0]['skills'])
    


# def confirm_edit(contact):
#     os.system('cls||clear')
#     console.print(Panel.fit('[magenta]Searching for the contact......', title='[cyan]Editing a Contact'))
#     confirm_edit = Confirm.ask(f'A you sure you want to edit\nID: {contact.id} - {contact.f_name} {contact.l_name} ?')
#     if not confirm_edit:
#         return False
#     os.system('cls||clear')
#     console.print(Panel.fit(f'[magenta]ID {contact.id}: {contact.f_name} {contact.l_name}', title='[cyan]Editing a Contact'))
#     return True

def continue_prompt():
    
    prompt = Prompt.ask("Press Enter to continue...", default="")

    return prompt

def add_contact(id, contact_type, first_name, last_name, phone, address, pet_name, fav_drink, work_address, work_phone, skills):
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
