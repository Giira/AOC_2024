with open("Day01.txt") as f:
    data = [line.strip().split("   ") for line in f.readlines()]


def main(data):
    left = []
    right = []
    for pair in data:
        left.append(pair[0])
        right.append(pair[1])
    left = sorted(left)
    right = sorted(right)

    total = 0
    for i in range(len(left)):
        l_digit = int(left.pop(0))
        r_digit = int(right.pop(0))
        total += abs(r_digit - l_digit)
    
    print("======== Part 1 ========")
    print(total)


main(data)
