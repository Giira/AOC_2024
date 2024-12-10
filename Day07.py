from itertools import product

with open("Day07.txt") as f:
    data = [[line.split(":")[0], line.split(":")[1].strip().split(" ")] for line in f.readlines()]


def part_1(data):
    count = 0
    for calculation in data:
        operators = ["+", "*"]
        goal = int(calculation[0])
        parameters = calculation[1]
        operator_perms = list(map(list, product(operators, repeat=(len(parameters) - 1))))
        start = parameters[0]
        expressions = []
        for perm in operator_perms:
            tmp = []
            for b in range(len(parameters) - 1):
                tmp.append("(")
            tmp.append(start)
            counter = 1
            for operator in perm:
                tmp.append(operator)
                tmp.append(parameters[counter])
                tmp.append(")")
                counter += 1
            expressions.append(tmp)            
        expressions = ["".join(expression) for expression in expressions]
        output = []
        for expression in expressions:
            output.append(eval(expression))
        if goal in output:
            count += goal
    return count 
        

def part_2(data):
    pass


if __name__ == "__main__":
    print("======== Part 1 ========")
    print(part_1(data))
    

    print("======== Part 2 ========")
    print(part_2(data))