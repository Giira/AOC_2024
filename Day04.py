import re

with open("Day04.txt") as f:
    data = [line.strip() for line in f.readlines()]

ncols = len(data[0])
nrows = len(data)


def count_orthogonal(data, v_data):
    horizontal = 0
    for row in data:
        horizontal += len(re.findall(r"(XMAS)", row))
        horizontal += len(re.findall(r"(SAMX)", row))
    vertical  = 0
    for col in v_data:
        vertical += len(re.findall(r"(XMAS)", col))
        vertical += len(re.findall(r"(SAMX)", col))
    return horizontal + vertical


def count_diagonal(data):
    d_count = 0
    for i in range(nrows):
        for j in range(ncols):
            if data[i][j] == "X":
                if i >= 3 and j >= 3:
                    if data[i-1][j-1] == "M":
                        if data[i-2][j-2] == "A":
                            if data[i-3][j-3] == "S":
                                d_count += 1
                if i <= nrows - 4 and j >= 3:
                    if data[i+1][j-1] == "M":
                        if data[i+2][j-2] == "A":
                            if data[i+3][j-3] == "S":
                                d_count += 1
                if i >= 3 and j <= ncols - 4:
                    if data[i-1][j+1] == "M":
                        if data[i-2][j+2] == "A":
                            if data[i-3][j+3] == "S":
                                d_count += 1
                if i <= nrows -4 and j <= ncols -4:
                    if data[i+1][j+1] == "M":
                        if data[i+2][j+2] == "A":
                            if data[i+3][j+3] == "S":
                                d_count += 1
    return d_count

def main(data):
    v_data = []
    for i in range(ncols):
        v_data.append("")
    for row in data:
        for j in range(ncols):
            v_data[j] += row[j]
    return count_orthogonal(data, v_data) + count_diagonal(data)
            

if __name__ == "__main__":
    print("======== Part 1 ========")
    print(main(data))
