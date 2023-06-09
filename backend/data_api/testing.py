import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# print(sys.path)
# take away the last folder name
BASE_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
print(BASE_DIR)

import notioner as n


print(n.get_pages())