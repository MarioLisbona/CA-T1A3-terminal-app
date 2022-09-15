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
    table.add_column('Operation', style='cyan', justify='left', no_wrap=True)
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
    table = Table(title=print("[bold yellow]\nAdding a Contact\nPlease Select from the menu below[/bold yellow]"))
    table.add_column('Operation', style='cyan', justify='left', no_wrap=True)
    table.add_column('Key', justify='left', style='magenta')

    table.add_row('Add a Contact', 'C')
    table.add_row('Add a Close Contact', 'CC')
    table.add_row('Add a Family Contact Contact', 'FC')
    table.add_row('Add a Work Contact', 'WC')
    table.add_row('Home', 'H')
    table.add_row('Quit Application', 'Q')

    console = Console()
    console.print(table)


def confirm_edit(contact):
    os.system('cls||clear')
    console.print(Panel.fit('[magenta]Searching for the contact......', title='[cyan]Editing a Contact'))
    confirm_edit = Confirm.ask(f'A you sure you want to edit\nID: {contact.id} - {contact.f_name} {contact.l_name} ?')
    if not confirm_edit:
        return False
    os.system('cls||clear')
    console.print(Panel.fit(f'[magenta]ID {contact.id}: {contact.f_name} {contact.l_name}', title='[cyan]Editing a Contact'))
    return True