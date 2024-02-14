


import os
import sys


this_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(this_dir, ".."))
sys.path.insert(0, base_dir)

from app.core.compiler import main

if __name__ == "__main__":
    main()

