from rich.console import Console
from rich.table import Table

table = Table()
table.add_column('Add a Contact', style='cyan', justify='left', no_wrap=True)
table.add_column('Details', justify='left', style='green')

# table.add_row('Add Contact', 'A')
# table.add_row('Edit Contact', 'E')
# table.add_row('Delete Contact', 'D')
# table.add_row('Display Contact', 'DI')
# table.add_row('Display all Contacts', 'DS')

console = Console()
console.print(table)

# console.rule("[bold red]Chapter 2")

# console.print([1, 2, 3])
# console.print("[blue underline]Looks like a link")
# console.print("FOO", style="white on blue")