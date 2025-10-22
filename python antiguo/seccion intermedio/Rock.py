import sys
from rich import print
from time import sleep

def printLyrics():
    lines = [
        ("I wanna da-", 0.06), 
        ("I wanna dance in the lights", 0.05),
        ("I wanna ro-", 0.07),
        ("I wanna rock your body", 0.08), 
        ("I wanna go", 0.08), 
        ("I wanna go for a ride", 0.068), 
        ("Hop in the music and", 0.07), 
        ("Rock your body", 0.08), 
        ("Rock that body", 0.069), 
        ("come on, come on", 0.035), 
        ("Rock that body", 0.05),
        ("Rock your body", 0.03),
        ("Rock that body", 0.049), 
        ("come on, come on", 0.035), 
        ("Rock that body", 0.08),
    ]
    
    for line, char_delay in lines:
        for char in line:
            print(f"[bold gold3]{char}[/bold gold3]", end='')
            sys.stdout.flush()
            sleep(char_delay)
        print()  
        sleep(0.1)  

printLyrics()
