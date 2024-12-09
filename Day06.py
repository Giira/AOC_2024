with open("Day06.txt") as f:
    data = [list(line.strip()) for line in f.readlines()]


NROWS = len(data)
NCOLS = len(data[0])


def find_start(data):
    for i in range(NROWS):
        for j in range(NCOLS):
            if data[i][j] == "^":
                return i, j


start = find_start(data)


def make_move(direction, i, j):
    move = (i,j)
    data[i][j] = "X"
    if direction == "N":
        if data[i-1][j] == "#":
            direction = "E"
        else:
            i -= 1
    elif direction == "E":
        if data[i][j+1] == "#":
            direction = "S"
        else:
            j += 1
    elif direction == "S":
        if data[i+1][j] == "#":
            direction = "W"
        else:
            i += 1
    elif direction == "W":
        if data[i][j-1] == "#":
            direction = "N"
        else:
            j -= 1
    move = (move, (i, j))
    return direction, i, j, move


def part_1(data):
    locations = [(start, "N")]
    i, j = start
    direction = "N"
    while 0 < i < NROWS - 1 and 0 < j < NCOLS - 1:
        direction, i, j, move = make_move(direction, i, j)
        if locations[-1][0] != (i, j):
            locations.append(((i,j), direction))
    data[i][j] = "X"
    locations.append(((i, j), direction))
    count = 0
    for line in data:
        count += line.count("X")
    return count, locations
    

def part_2(data):
    count = 0
    i, j = start
    blockages = set()
    for a in range(len(locations) - 2):
        moves = set()
        if start != (locations[a+1][0][0], locations[a+1][0][1]):
            if (locations[a+1][0][0], locations[a+1][0][1]) not in blockages:
                data[locations[a+1][0][0]][locations[a+1][0][1]] = "#"
                blockages.add((locations[a+1][0][0], locations[a+1][0][1]))
        direction, i, j = locations[a][1], locations[a][0][0], locations[a][0][1]
        while 0 < i < NROWS - 1 and 0 < j < NCOLS - 1:
            direction, i, j, move = make_move(direction, i, j)
            if move not in moves and move[0] != move[1]:
                moves.add(move)
            elif move[0] == move[1]:
                continue
            else:
                count += 1
                break
        data[locations[a+1][0][0]][locations[a+1][0][1]] = "."
    return count


if __name__ == "__main__":
    print("======== Part 1 ========")
    count, locations = part_1(data)
    print(count)

    print("======== Part 2 ========")
    print(part_2(data))
