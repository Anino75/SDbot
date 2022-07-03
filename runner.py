import os
import time
from datetime import datetime
import main

cur_dir = os.path.abspath('.')

print(f'Running from {cur_dir}')
print(f'[{datetime.now().strftime("%d:%m:%Y %H:%M:%S")}] Booting...')

main.debug = False
while True:
    main.run_bot()
    print(f'[{datetime.now().strftime("%d:%m:%Y %H:%M:%S")}] Error: Connection Closed!')
    time.sleep(10)
    print(f'[{datetime.now().strftime("%d:%m:%Y %H:%M:%S")}] Rebooting...')
