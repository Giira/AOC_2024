with open("Day05.txt") as f:
    rules, pages = f.read().split("\n\n")
    rules = [line.strip().split("|") for line in rules.split("\n")]
    pages = [line.strip().split(",") for line in pages.split("\n")]
    data = rules, pages

def part_1(data):
    total = 0
    for page_set in data[1]:
        valid = True
        for rule in data[0]:
            if rule[0] in page_set and rule[1] in page_set:
                if page_set.index(rule[0]) > page_set.index(rule[1]):
                    valid = False
        if valid:
            total += int(page_set[int(len(page_set) // 2)])
    return total


def part_2(data):
    pass


if __name__ == "__main__":
    print("======== Part 1 ========")
    print(part_1(data))

    print("======== Part 2 ========")
    print(part_2(data))
