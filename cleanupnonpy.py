import os
import time
from curtsies.fmtfuncs import cyan, bold, green, red, yellow

d = 'repos'
for dirpath, dirnames, filenames in os.walk("repos"):
    for f in filenames:
        path = os.path.join(dirpath, f)

        if path.endswith('.py'):
            print(green(f"Keeping {path}"))
        else:
            print(red(f"Deleting {path}"))
            
            if d in path:
                os.remove(path)
            else:
                print(yellow("Something went wrong"))
                time.sleep(60)
    # time.sleep(0.5)