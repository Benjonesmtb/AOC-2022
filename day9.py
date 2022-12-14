with open("day9.txt") as f:
    ls = f.read().strip().split("\n")

moves = [(l[0], int(l[1:])) for l in ls]

dz = {"R": 1, "L": -1, "U": 1j, "D": -1j}


def sign(a):
    return (a > 0) - (a < 0)


def new_tail(head, tail):
    if abs(head - tail) < 2:
        return tail
    tail += sign(head.real - tail.real)
    tail += sign(head.imag - tail.imag) * 1j
    return tail


# Part 1
head = 0
tail = 0
visited = {0}

for direction, distance in moves:
    for _ in range(distance):
        head += dz[direction]
        tail = new_tail(head, tail)
        visited.add(tail)

print(len(visited))

# Part 2
parts = [0 for _ in range(10)]  # 0 is H
visited = {0}
for direction, distance in moves:
    for _ in range(distance):
        parts[0] += dz[direction]
        for i in range(1, 10):
            parts[i] = new_tail(parts[i - 1], parts[i])
        visited.add(parts[-1])

print(len(visited))
