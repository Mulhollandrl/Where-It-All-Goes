import sys
import os

def exit():
    sys.exit(1)

def invalidityCheck(directory):
    if os.access(directory, os.R_OK):
        return False
    else:
        return True
