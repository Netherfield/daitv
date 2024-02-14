


import os
import sys


this_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(this_dir, ".."))
sys.path.insert(0, base_dir)

from app.queries import *

if __name__ == "__main__":
    # users()
    # ratings()

    os.system("pyclean .")

