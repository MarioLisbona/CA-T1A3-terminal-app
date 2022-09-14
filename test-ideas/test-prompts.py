
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.console import Console
from rich.table import Table
from rich import print

# name = Prompt.ask('Enter your name', choices=['Paul', 'Jessica', 'Duncan'], default='Paul')


# is_rich_great = Confirm.ask('Do you like rich?')
# assert is_rich_great


table = Table(title=print("[bold yellow]\nWelcome to your Contacts Database\nPlease Select from the menu below[/bold yellow]"))
table.add_column('Operation', style='cyan', justify='left', no_wrap=True)
table.add_column('Key', justify='left', style='green')

table.add_row('Add Contact', 'A')
table.add_row('Edit Contact', 'E')
table.add_row('Delete Contact', 'D')
table.add_row('Display Contact', 'DI')
table.add_row('Display all Contacts', 'DS')

console = Console()
console.print(table)

console.rule("[bold red]Chapter 2")

console.print([1, 2, 3])
console.print("[blue underline]Looks like a link")
console.print("FOO", style="white on blue")


