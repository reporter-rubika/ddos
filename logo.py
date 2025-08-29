from pyfiglet import Figlet

G = '\033[32m'
RESET = '\033[0m'

f = Figlet(font='big')  

ascii_art = f.renderText('HR Team')

print(G + ascii_art + RESET)