data = open("input7.txt", "r")
file = data.read()
content = []
totalSize = 0

for line in file.splitlines():
    content.append(line)


for x in range(len(content)):
    firstChar = content[x-1][0]
    if firstChar == "$":
        command = True
    if command == True: