data = open("input1.txt", "r")
file = data.read()

empty = []

for line in file.splitlines():
    empty.append(line)

final = []
num = 0
for item in empty:
    if item != "":
        num += int(item)
    else:
        final.append(int(num))
        num = 0

sorted = final.sort()

print(len(final))
print(final[len(final)-1])
print(final[len(final)-3] + final[len(final)-2] + final[len(final)-1])

data.close()