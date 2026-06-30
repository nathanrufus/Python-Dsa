import os
from pathlib import Path 

# File Operations in Python

# 1. OPENING FILES
file = open('example.txt', 'r')  # read mode
file = open('example.txt', 'w')  # write mode
file = open('example.txt', 'a')  # append mode
file = open('example.txt', 'rb') # read binary
file = open('example.txt', 'wb') # write binary
file = open('example.txt', 'x')  # create (exclusive)

# 2. READING FILES
content = file.read()           # read entire file
line = file.readline()          # read one line
lines = file.readlines()        # read all lines as list
for line in file:               # iterate through lines
    pass

# 3. WRITING FILES
file.write('text')              # write string
file.writelines(['a', 'b'])     # write list of strings

# 4. FILE POINTER OPERATIONS
file.seek(0)                    # move to position
position = file.tell()          # current position
file.truncate(10)               # truncate to size

# 5. CLOSING FILES
file.close()                    # close file
with open('file.txt') as f:     # context manager (auto close)
    content = f.read()

# 6. FILE METHODS
file.flush()                    # flush buffer
file.isatty()                   # check if tty
file.readable()                 # check if readable
file.writable()                 # check if writable
file.seekable()                 # check if seekable
file.name                       # get filename
file.mode                       # get mode
file.closed                     # check if closed

# 7. OS MODULE OPERATIONS
os.remove('file.txt')           # delete file
os.rename('old.txt', 'new.txt') # rename
os.path.exists('file.txt')      # check existence
os.path.getsize('file.txt')     # get size
os.path.isfile('file.txt')      # check if file
os.getcwd()                     # current directory
os.listdir('.')                 # list directory
os.mkdir('dirname')             # create directory
os.makedirs('path/to/dir')      # create nested
os.rmdir('dirname')             # remove directory
os.remove('file.txt')           # remove file
os.stat('file.txt')             # get stats

# 8. PATHLIB MODULE (modern)
p = Path('file.txt')
p.read_text()                   # read file
p.write_text('content')         # write file
p.exists()                      # check existence
p.unlink()                      # delete file
p.mkdir()                       # create directory
p.stat()                        # get stats
p.iterdir()                     # list directory