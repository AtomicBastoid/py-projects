import random
import time
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
symbols = ['*', 'o', '+', '@', '✨', '★']

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def confetti(lines=20, width=60):
    for _ in range(lines):
        line = ''
        for _ in range(width):
            if random.random() < 0.05:  # sparse confetti
                color = random.choice(colors)
                symbol = random.choice(symbols)
                line += color + symbol
            else:
                line += ' '
        print(line)
        time.sleep(0.05)

# Run confetti animation
# clear()
# confetti()
# print("\n" + Fore.GREEN + Style.BRIGHT + "🎉 Congrats! 🎉")