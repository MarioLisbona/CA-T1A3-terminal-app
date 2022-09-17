import os
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print

console = Console()

# User prompt fuction with information on how to use the program
def menu_prompt():
    """
    This function clears the screen each time and prints a user prompt with instructions on how to use the program
    """    
    os.system('cls||clear')
    table = Table(title=print("[bold yellow]\nWelcome to your Contacts Database\nPlease Select from the menu below[/bold yellow]"))
 
    table.add_column('Home | Operation', style='cyan', justify='left', no_wrap=True)
    table.add_column('Key', justify='left', style='magenta')

    table.add_row('Add Contact', 'A')
    table.add_row('Edit Contact', 'E')
    table.add_row('Delete Contact', 'D')
    table.add_row('Display Contact', 'DC')
    table.add_row('Display all Contacts', 'DA')
    table.add_row('Quit Application', 'Q')

    console = Console()
    console.print(table)

def add_contact_prompt():
    """
    This function clears the screen each time and prints a user prompt with instructions on how to use the program
    """    
    os.system('cls||clear')
    table = Table(title=print("[bold yellow]\nAdding a Contact. Please Select from the menu below[/bold yellow]"))
    table.add_column('Add | Operation', style='cyan', justify='left', no_wrap=True)
    table.add_column('Key', justify='left', style='magenta')

    table.add_row('Add a Contact', 'C')
    table.add_row('Add a Close Contact', 'CC')
    table.add_row('Add a Family Contact Contact', 'FC')
    table.add_row('Add a Work Contact', 'WC')
    table.add_row('Home', 'H')
    table.add_row('Quit Application', 'Q')

    console = Console()
    console.print(table)


def display_table(list):
    table = Table(title="Your Contacts")

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

    for idx, val in enumerate(list):
        if len(val) == 5:
            table.add_row(list[idx]['id'], list[idx]['first_name'], list[idx]['last_name'], list[idx]['phone'])
        elif len(val) == 6:
            table.add_row(list[idx]['id'], list[idx]['first_name'], list[idx]['last_name'], list[idx]['phone'],  list[idx]['address'])
        elif len(val) == 8:
            table.add_row(list[idx]['id'], list[idx]['first_name'], list[idx]['last_name'], list[idx]['phone'],  list[idx]['address'], list[idx]['pet'], list[idx]['fav_drink'])
        elif len(val) == 9:
            table.add_row(list[idx]['id'], list[idx]['first_name'], list[idx]['last_name'], list[idx]['phone'],  list[idx]['address'], '', '', list[idx]['work_address'], list[idx]['work_phone'], list[idx]['skills'])

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

def press_to_continue():
    prompt = Prompt.ask("Press Enter to continue...", default="")

    return prompt