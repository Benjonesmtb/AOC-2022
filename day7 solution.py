import os
import re
lines = []
data = open("input7.txt", "r")
file = data.read()
for line in file.splitlines():
    lines.append(line)
    
currentDir = ""
dirs = {}
subdirs = {}

for line in lines:
    if line[0] == '$':
        c, cmd, *args = line.split()
        if cmd == 'cd':
            path ,= args
            if path[0] == '/':
                currentDir = path
            else:
                currentDir = os.path.normpath(os.path.join(currentDir, path))
            if currentDir not in dirs:
                dirs[currentDir] = 0
                subdirs[currentDir] = []
    else:
        sz, fname = line.split()
        if sz != 'dir':
            dirs[currentDir] += int(sz)
        else:
            subdirs[currentDir].append(os.path.normpath(os.path.join(currentDir, fname)))

dirsizes = {}

def dirsize(dirname):
    dsize = dirs[dirname]
    for i in subdirs[dirname]:
        if i in dirs:
            dsize += dirsize(i)
    return dsize
totsize = 0

# part 1
for d in dirs:
    dsize = dirsize(d)
    if dsize <= 100000:
        totsize += dsize
print(totsize)

# part 2
totsize = dirsize('/')
unused = 70000000 - totsize
ms = None
for d in dirs:
    ds = dirsize(d)
    if unused + ds >= 30000000:
        if ms is None or ms > ds:
            ms = ds
print(ms)