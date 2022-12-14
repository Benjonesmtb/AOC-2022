import os
import numpy as np

DATA_FILE = os.path.join(os.path.dirname(__file__), "day8.txt")


def calc_scenic_score(left, right, up, down, height) -> int:
    score = 1
    for dir in [left, right, up, down]:
        count = 0
        for t in dir:
            count += 1
            if t >= height:
                break
        score *= count

    return score


def main(f=DATA_FILE) -> tuple:
    p1, p2 = None, None
    with open(DATA_FILE, "r") as f:
        lines = f.readlines()

    trees = np.array([np.array([int(c) for c in l.strip()]) for l in lines])
    visibility = np.full(tuple(trees.shape), 4)

    rows = trees.shape[1]
    cols = trees.shape[0]
    xmax = [-1] * cols
    for y in range(rows):
        ymax = -1
        for x in range(cols):
            height = trees[y][x]
            if height <= xmax[x]:
                visibility[y][x] -= 1
            if height <= ymax:
                visibility[y][x] -= 1
            ymax = max(ymax, height)
            xmax[x] = max(xmax[x], height)

    xmax = [-1] * cols
    for y in range(rows - 1, -1, -1):
        ymax = -1
        for x in range(cols - 1, -1, -1):
            height = trees[y][x]
            if height <= xmax[x]:
                visibility[y][x] -= 1
            if height <= ymax:
                visibility[y][x] -= 1
            ymax = max(ymax, height)
            xmax[x] = max(xmax[x], height)

    p1 = np.count_nonzero(visibility)

    max_score = 0
    for y, x in np.ndindex(trees.shape):
        height = trees[y][x]
        left = np.flip(trees[y, :x])
        right = trees[y, x + 1 :]
        up = np.flip(trees[:y, x])
        down = trees[y + 1 :, x]

        score = calc_scenic_score(left, right, up, down, height)
        max_score = max(max_score, score)

    p2 = max_score
    return p1, p2


if __name__ == "__main__":
    p1, p2 = main()
    print(p1)
    print(p2)