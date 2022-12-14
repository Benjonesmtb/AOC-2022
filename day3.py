def part_1():
    with open('day3Input.txt') as f:
        data = f.read().split('\n')
    
    score = 0

    for line in data:
        n = len(line)//2
        part_1, part_2 = line[:n],line[n:]

        for item in list(set.intersection(set(part_1),set(part_2))):

                if item.isupper():
                    score += ord(item)-ord('A') + 27
                else:
                    score += ord(item)- ord('a')+1

    print('Answer to day 3 part 1 is' , score)

    return data

def part_2(*args):
    data = args[0]
    n = len(data)
    score = 0

    for i in range(n//3):
        item_1 = data[i*3+0]
        item_2 = data[i * 3 + 1]
        item_3 = data[i * 3 + 2]
        badge = list(set.intersection(set(item_1),set(item_2),set(item_3)))[0]

        if badge.isupper():
            score += ord(badge) - ord('A') + 27
        elif badge.islower():
            score += ord(badge) - ord('a') + 1

    print('Answer to day 3 part 2 is', score)

data = part_1()
part_2(data)