from tqdm import tqdm

with open("Day11.txt") as f:
    data = [int(number.strip()) for number in f.read().split(" ")]
print(data)


def apply_rules(data):
    i = 0
    while i < len(data):
        if data[i] == 0:
            data[i] = 1
        elif len(str(data[i])) % 2 == 0:
            split_length = int(len(str(data[i])) / 2)
            a, b = str(data[i])[:split_length], str(data[i])[split_length:]
            data = data[:i] + [int(a), int(b)] + data[i + 1:]
            i += 1
        else:
            data[i] *= 2024


        i += 1
    return data

def part_1(data, blinks):
    for i in tqdm(range(blinks)):
        data = apply_rules(data)
    return len(data)


if __name__ == "__main__":
    print("======== Part 1 ========")
    print(part_1(data, 25))
    
    print("======== Part 2 ========")
    # print(part_1(data, 75))
