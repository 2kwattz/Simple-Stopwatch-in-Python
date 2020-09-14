#code by 2kwattz

import time
import pyfiglet

seconds = 0
minutes = 0
looper = 0

banner =  pyfiglet.figlet_format("Stopwatch")
print(banner)
print("\n Press 1 to start Stopwatch")
userinput = int(input())
if userinput == 1:
    while looper != 1:
        print(f"{minutes} : {seconds}")
        time.sleep(1)
        if seconds == 59:
            seconds = 0
            minutes = minutes + 1

        else:
            seconds = seconds + 1
