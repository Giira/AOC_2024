with open("Day02.txt") as f:
    data = [line.strip().split(" ") for line in f.readlines()]


def main(data):
    total_safe = 0
    for report in data:
        safe = True
        if int(report[0]) < int(report[1]):
            ascending = True
        elif int(report[0]) > int(report[1]):
            ascending = False
        else:
            safe = False
        for i in range(len(report) - 1):
            if safe:
                if ascending:
                    if int(report[i]) < int(report[i+1]):
                        if 1 <= abs(int(report[i+1]) - int(report[i])) <= 3:
                            continue
                        else:
                            safe = False
                    else:
                        safe = False
                else:
                    if int(report[i]) > int(report[i+1]):
                        if 1 <= abs(int(report[i]) - int(report[i+1])) <= 3:
                            continue
                        else: safe = False
                    else:
                        safe = False
        if safe:
            total_safe += 1

    
    print("======== Part 1 ========")
    print(total_safe)
    print("======== Part 2 ========")
    # print(total_2)
main(data)
