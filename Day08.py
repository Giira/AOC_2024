from tqdm import tqdm
with open("Day08.txt") as f:
    data = [list(line.strip()) for line in f.readlines()]


HEIGHT = len(data)
WIDTH = len(data[0])


def tuple_sub(tuple_1, tuple_2):
    output = tuple(a-b for a,b in zip(tuple_1, tuple_2))
    return output


def tuple_add(tuple_1, tuple_2):
    output = tuple(a+b for a,b in zip(tuple_1, tuple_2))
    return output


def tuple_lcf(difference):
    if difference[0] >= difference[1]:
        big = difference[0]
    else:
        big = difference[1]
    for i in range(big, -1):
        if difference[0] % i == 0 and difference[1] % i == 0:
            return (int(difference[0] / i), int(difference[1] / i))
    return difference
    

def get_nodes(data):
    nodes = {}
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if data[i][j] != ".":
                if data[i][j] in nodes:
                    nodes[data[i][j]]["antennae"].append((i,j))
                else:
                    nodes[data[i][j]] = {"antennae": [(i,j)],
                                         "anti_node": set()}
    return nodes


def solve(data):
    nodes = get_nodes(data)
    antinode_all = set()
    antinode_extra = set()
    for node in tqdm(nodes):
        for a in range(len(nodes[node]["antennae"]) - 1):
            current = nodes[node]["antennae"][a]
            antinode_extra.add(current)
            for node_2 in nodes[node]["antennae"][a + 1:]:
                difference = tuple_sub(current, node_2)
                line_vector = tuple_lcf(difference)
                centre = current
                while 0 <= centre[0] <= HEIGHT - 1 and 0 <= centre[1] <= WIDTH - 1:
                    centre = tuple_sub(centre, line_vector)
                    if 0 <= centre[0] <= HEIGHT - 1 and 0 <= centre[1] <= WIDTH - 1:
                        antinode_extra.add(centre)
                centre = current
                while 0 <= centre[0] <= HEIGHT - 1 and 0 <= centre[1] <= WIDTH - 1:
                    centre = tuple_add(centre, line_vector)
                    if 0 <= centre[0] <= HEIGHT - 1 and 0 <= centre[1] <= WIDTH - 1:
                        antinode_extra.add(centre)
                antinodes = [tuple_sub(node_2, difference), tuple_add(current, difference)]
                for antinode in antinodes:
                    if 0 <= antinode[0] <= HEIGHT - 1 and 0 <= antinode[1] <= WIDTH - 1:
                        nodes[node]["anti_node"].add(antinode)
        antinode_all = antinode_all | nodes[node]["anti_node"]
    return len(list(antinode_all)), len(list(antinode_extra))

if __name__ == "__main__":
    print("======== Part 1 ========")
    print(solve(data)[0])
    
    print("======== Part 2 ========")
    print(solve(data)[1])
