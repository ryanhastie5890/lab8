from adventure.utils import read_events_from_file
import random
from rich import print
def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[blue][bold red]You[/bold red] stand still, unsure what to do. The forest [bold red]swallows[/bold red] you.[/blue]"

def left_path(event):
    return "[blue]You walk [bold red]left[/bold red]. " + event+"[/blue]\n"

def right_path(event):
    return "[blue]You walk [bold red]right[/bold red]. " + event+"[/blue]\n"

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("[blue]You wake up in a dark forest. You can go [bold red]left or right[/bold red].[/blue]\n")
    while True:
        print("[blue]Which direction do you choose? ([bold red]left/right/exit[/bold red]): [/blue]\n")
        choice = input()
        choice = choice.strip().lower()
        if choice == 'exit':
            print("[blue]Thank you for playing! [bold red]Good Bye![/bold red][/blue]")
            break
        
        print(step(choice, events))
