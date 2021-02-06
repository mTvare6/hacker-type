import sys
import tty
import os
import termios
import itertools
import random


def alternating_size_chunks(iterable, steps):
    n = 0
    step = itertools.cycle(steps)
    while n < len(iterable):
        next_step = next(step)
        yield iterable[n:n + next_step]
        n += next_step
        

url = "https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh"
file_content=os.popen('curl "'+uri+'" 2>/dev/null').read()
print("\r")
content = list(alternating_size_chunks(file_content, (random.randrange(2, 5), random.randrange(2, 5), random.randrange(2, 5))))



def speed_type():
    if len(content) == 0:
        sys.exit(0)
    print(content[0], end="", flush=True)
    del content[0]
def getkey():
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    try:
        while True:
            b = os.read(sys.stdin.fileno(), 3).decode()
            if len(b) == 3:
                k = ord(b[2])
            else:
                k = ord(b)
            key_mapping = {
                27: 'esc'
            }
            return key_mapping.get(k, chr(k))
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
try:
    while True:
        k = getkey()
        if k == 'esc':
            quit()
        else:
            speed_type()
except (KeyboardInterrupt, SystemExit):
#    os.system('stty sane')
#    print('stopping.')
    pass
