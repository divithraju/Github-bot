import os
import random
import json
import subprocess
from datetime import datetime, timedelta

FILE_PATH = './data.json'

def make_commit(n):
    if n == 0:
        subprocess.run(["git", "push"])
        return
    
    x = random.randint(0, 54)
    y = random.randint(0, 6)
    date = datetime.now() - timedelta(weeks=54) + timedelta(weeks=x, days=y)
    date_str = date.strftime('%Y-%m-%dT%H:%M:%S')

    data = {
        'date': date_str
    }
    
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    
    subprocess.run(["git", "add", FILE_PATH])
    subprocess.run(["git", "commit", "-m", date_str, "--date", date_str])
    
    make_commit(n - 1)

# Start the process with 500 commits
make_commit(500)

