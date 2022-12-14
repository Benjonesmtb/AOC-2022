data = open("input13.txt", "r")
file = data.read()
content = []
count = 0

for line in file.splitlines():
    content.append(line)

print(content[0])
#for i in range(len(content)):
    #if content[i-1] == content[i-1].sort():
        #count = count + 1