import os

from datetime import datetime

title = 'Time information'

time = datetime.now()

current_time = time.strftime("%H:%M:%S")

def check():
    command = f'''

    osascript -e 'display notification "Time now: {current_time}" with title  "{title}"'
    '''

    os.system(command)


check()    