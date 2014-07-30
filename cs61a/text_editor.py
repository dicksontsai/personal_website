# This assignment's inspiration is from Learn Python the Hard Way
from sys import argv
from file_iterator import *

# e.g. python3 text_editor.py test.txt
if len(argv) != 2:
    raise ValueError("Not the right input: Must be disc9.py filename")
script, filename = argv

MODES = ('a', 'w', 'e')
SAVE_MESSAGE = "Your file has been successfully saved and closed."
OVERWRITE_MESSAGE = "Caution: If this file exists, it will be rewritten. Is that all right? Type Ctrl-C to quit or enter to continue"

print("Type a to add to the file, w to write to the file, or e to edit the file.")
print("Type Ctrl-C to quit")
mode = ""
while mode not in MODES: 
    mode = input("?")

if mode == 'w':
    print(OVERWRITE_MESSAGE)
    input("?")

if mode == 'e':
    mode = 'r+'

# Put all of your file-related code within this with clause.
# This with clause will handle opening and closing for you.
with open(filename, mode) as f:
    if mode == 'r+':
        editor = iter(FileReviewer(f))
    else:
        editor = iter(FileIterator(f))
    try:
        # Since editor is an iterator, we can use it in a for loop!
        for line in editor:
            "This is cool, isn't it?"
            # You can put logging stuff here, e.g. count the number
            # lines you have served with this program.
    except StopIteration:
        print(SAVE_MESSAGE)
