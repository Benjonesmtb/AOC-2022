c = 4
for i in range(2):
    for x in range(len(open("input6.txt", "r").read())):
        if c == len(set(open("input6.txt", "r").read()[x:x+c])):
            ans = x+c
            break
    print(ans)
    c = 14