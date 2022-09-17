from rich import print
from rich.layout import Layout

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text
import os


def menu_prompt():
    """
    This function clears the screen each time and prints a user prompt with instructions on how to use the program
    """    
    # os.system('cls||clear')
    table = Table()
    table.add_column('Operation', style='cyan', justify='left', no_wrap=True)
    table.add_column('Key', justify='left', style='magenta')

    table.add_row('Add Contact', 'A')
    table.add_row('Edit Contact', 'E')
    table.add_row('Delete Contact', 'D')
    table.add_row('Display Contact', 'DC')
    table.add_row('Display all Contacts', 'DA')
    table.add_row('Quit Application', 'Q')

    # console = Console()
    # console.print(table)

    return table

def add_contact_prompt():
    """
    This function clears the screen each time and prints a user prompt with instructions on how to use the program
    """    
    os.system('cls||clear')
    table = Table()
    table.add_column('Operation', style='cyan', justify='left', no_wrap=True)
    table.add_column('Key', justify='left', style='magenta')

    table.add_row('Add a Contact', 'C')
    table.add_row('Add a Close Contact', 'CC')
    table.add_row('Add a Family Contact Contact', 'FC')
    table.add_row('Add a Work Contact', 'WC')
    table.add_row('Home', 'H')
    table.add_row('Quit Application', 'Q')

    # console = Console()
    # console.print(table)

    return table

layout = Layout()

layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)

layout["lower"].split_row(
    Layout(name="left"),
    Layout(name="right"),
)

layout['upper'].ratio  = 2


layout['left'].update(Panel(menu_prompt()))
layout['right'].update(Panel('Contacts Book'))
print(layout)
