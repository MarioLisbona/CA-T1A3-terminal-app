from rich.console import Console
from rich.text import Text
from rich import print
from rich.panel import Panel

# panel = Panel(Text("Hello", justify="right"))
# print(panel)
# console = Console()
# text = Text("Hello, World!")
# text.stylize("bold magenta", 0, 6)
# console.print(text)

# text = Text()
# text.append("Hello", style="bold magenta")
# text.append(" World!")
# console.print(text)

# from rich import print
# from rich.panel import Panel
# from rich.text import Text
# panel = Panel(Text("Hello", justify="right"))
# print(panel)

print(Panel.fit("Hello, [magenta]World!"))

print(Panel.fit("Hello, [red]World!", title="Welcome", subtitle="Thank you"))