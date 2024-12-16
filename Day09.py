from tqdm import tqdm

with open("Day09.txt") as f:
    data = [int(char) for char in list(f.read().strip())]


def create_list(data):
    output = []
    indices = []
    counter = 0
    for i in range(len(data)):
        if i % 2 == 0:
            for j in range(data[i]):
                output.append(int(counter))
            counter += 1
        else:
            for j in range(data[i]):
                output.append(".")
                indices.append(len(output) -1)
    return output, indices


def create_list_2(data):
    output = []
    counter = 0
    for i in range(len(data)):
        if i % 2 == 0:
            for j in range(data[i], 0, -1):
                output.append((counter, data[i]))
            counter += 1
        else:
            for j in range(data[i], 0, -1):
                output.append((".", j))
    return output
            


def move_left(output, indices):
    for k in range(len(output) -1, 0, -1):
        if indices[0] < k:
            if output[k] != ".":
                output[indices.pop(0)] = output[k]
                output[k] = "."
    
    while output[-1] == ".":
        output.pop(-1)
    return output


def move_block_left(output):
    moved = []
    for i in range(len(output) -1, 0, -1):
        if output[i][0] != "." and output[i] not in moved:
            for j in range(len(output)):
                if output[j][0] == "." and output[j][1] >= output[i][1] and j < i:
                    tmp = i
                    moved.append(output[i])
                    for k in range(output[i][1]):
                        output[j] = output[tmp]
                        output[tmp] = (".", 0)
                        j += 1
                        tmp -= 1
                    break
    while output[-1][0] == ".":
        output.pop(-1)
    return output


def part_1(data):
    output, indices = create_list(data)
    output = move_left(output, indices)

    checksum = 0
    for l in range(len(output)):
        checksum += output[l] * l
    return checksum


def part_2(data):
    output = create_list_2(data)
    output = move_block_left(output)

    checksum = 0
    for l in range(len(output)):
        if output[l][0] != ".":
            checksum += int(output[l][0]) * l
    return checksum

if __name__ == "__main__":
    print("======== Part 1 ========")
    print(part_1(data))
    
    print("======== Part 2 ========")
    print(part_2(data))
