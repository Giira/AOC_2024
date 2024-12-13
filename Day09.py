from tqdm import tqdm

with open("Day09.txt") as f:
    data = [int(char) for char in list(f.read().strip())]


def part_1(data):
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
                indices.append(len(output) - 1)

    for k in range(len(output) - 1, 0, -1):
        if indices[0] < k:
            if output[k] != ".":
                output[indices.pop(0)] = output[k]
                output[k] = "."
    
    while output[-1] == ".":
        output.pop(-1)

    checksum = 0
    for l in range(len(output)):
        checksum += output[l] * l
    return checksum

if __name__ == "__main__":
    print("======== Part 1 ========")
    print(part_1(data))
    
    print("======== Part 2 ========")
    # print(part_2(data))
