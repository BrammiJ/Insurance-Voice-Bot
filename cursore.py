from time import sleep
import sys
line_1 = "You have woken up in a mysterious maze"
for x in line_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)