with open("Day06.txt") as f:
    data = [list(line.strip()) for line in f.readlines()]


NROWS = len(data)
NCOLS = len(data[0])


def find_start(data):
    for i in range(NROWS):
        for j in range(NCOLS):
            if data[i][j] == "^":
                return i, j


def make_move(direction, i, j):
    data[i][j] = "X"
    if direction == "N":
        if data[i-1][j] != "." and data[i-1][j] != "X":
            direction = "E"
        else:
            i -= 1
    elif direction == "E":
        if data[i][j+1] != "." and data[i][j+1] != "X":
            direction = "S"
        else:
            j += 1
    elif direction == "S":
        if data[i+1][j] != "." and data[i+1][j] != "X":
            direction = "W"
        else:
            i += 1
    elif direction == "W":
        if data[i][j-1] != "." and data[i][j-1] != "X":
            direction = "N"
        else:
            j -= 1
    return direction, i, j

def part_1(data):
    i, j = find_start(data)
    direction = "N"
    while 0 < i < NROWS -1 and 0 < j < NCOLS:
        direction, i, j = make_move(direction, i, j)
    count = 1
    for line in data:
        count += line.count("X")
    return count
    

if __name__ == "__main__":
    print("======== Part 1 ========")
    print(part_1(data))
