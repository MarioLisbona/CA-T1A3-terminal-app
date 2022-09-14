
from rich.prompt import Prompt
from rich.prompt import Confirm

from rich import print

name = Prompt.ask('Enter your name', choices=['Paul', 'Jessica', 'Duncan'], default='Paul')

print(name)


is_rich_great = Confirm.ask('Do you like rich?')
print(is_rich_great)







