with open("Day05.txt") as f:
    rules, pages = f.read().split("\n\n")
    rules = [line.strip().split("|") for line in rules.split("\n")]
    pages = [line.strip().split(",") for line in pages.split("\n")]
    data = rules, pages

def part_1(data):
    total = 0
    incorrect_page_sets = []
    for page_set in data[1]:
        valid = True
        for rule in data[0]:
            if rule[0] in page_set and rule[1] in page_set:
                if page_set.index(rule[0]) > page_set.index(rule[1]):
                    valid = False
        if valid:
            total += int(page_set[int(len(page_set) // 2)])
        else:
            incorrect_page_sets.append(page_set)
    return total, incorrect_page_sets


def part_2(rules, page_sets):
    total = 0
    for page_set in page_sets:
        valid = False
        while not valid:
            passage = False
            for rule in rules:
                if rule[0] in page_set and rule[1] in page_set:
                    if page_set.index(rule[0]) > page_set.index(rule[1]):
                        page_set.pop(page_set.index(rule[0]))
                        page_set = page_set[:page_set.index(rule[1])] + [rule[0]] + page_set[page_set.index(rule[1]):]
                        passage = True
                        break
            if not passage:
                valid = True
        total += int(page_set[int(len(page_set) // 2)])
    return total


if __name__ == "__main__":
    print("======== Part 1 ========")
    print(part_1(data)[0])

    print("======== Part 2 ========")
    print(part_2(data[0], part_1(data)[1]))
