from tqdm import tqdm

with open("Day10.txt") as f:
    data = [[char for char in line.strip()] for line in f.readlines()]


HEIGHT = len(data)
WIDTH = len(data[0])


class Cell():
    def __init__(self, value: int, x: int, y: int):
        self.value = value
        self.visited = set()
        self.routes = []
        self.x = x
        self.y = y


def get_neighbours(coord):
    neighbours = []
    if coord[0] > 0:
        neighbours.append((coord[0] - 1, coord[1]))
    if coord[0] < HEIGHT - 1:
        neighbours.append((coord[0] + 1, coord[1]))
    if coord[1] > 0:
        neighbours.append((coord[0], coord[1] - 1))
    if coord[1] < WIDTH - 1:
        neighbours.append((coord[0], coord[1] + 1))
    return neighbours


def find_runs(topo_map, start, coord=None):
    if coord is None:
        coord = start
    if topo_map[coord[0]][coord[1]].value == 9:
        topo_map[start[0]][start[1]].visited.add((coord[0], coord[1]))
        topo_map[start[0]][start[1]].routes.append((coord[0], coord[1]))
    for neighbour in get_neighbours(coord):
        if topo_map[coord[0]][coord[1]].value + 1 == topo_map[neighbour[0]][neighbour[1]].value:
            find_runs(topo_map, start, neighbour)


def make_cells(data):
    topo_map = []
    for i in range(HEIGHT):
        topo_map.append([])
        for j in range(WIDTH):
            topo_map[i].append(Cell(int(data[i][j]), i, j))
    return topo_map


def part_1(data):
    topo_map = make_cells(data)
    route_count = 0
    all_route_count = 0
    for line in tqdm(topo_map):
        for cell in line:
            if cell.value == 0:
                start = (cell.x, cell.y)
                find_runs(topo_map, start)
    for line in topo_map:
        for cell in line:
            if cell.value == 0:
                route_count += len(cell.visited)
                all_route_count += len(cell.routes)
    return route_count, all_route_count
    

if __name__ == "__main__":
    print("======== Part 1 ========")
    print(part_1(data)[0])
    
    print("======== Part 2 ========")
    print(part_1(data)[1])
