from functools import cache, reduce
from itertools import product
from tqdm import tqdm
import operator

with open("Day07.txt") as f:
    data = [[line.split(":")[0], line.split(":")[1].strip().split(" ")] for line in f.readlines()]


@cache
def get_perms(operators, num_parameters):
    output = list(product(operators, repeat=num_parameters-1))
    return output


def evaluate(num_pair: tuple[int], operators: str):
    match operators:
        case "+":
            return operator.add(*num_pair)
        case "*":
            return operator.mul(*num_pair)
        case "|":
            return int("".join(str(num) for num in num_pair))


def part_1(data):
    count = 0
    operators = "*+"
    for calculation in tqdm(data):
        goal = int(calculation[0])
        parameters = calculation[1]
        num_parameters = len(parameters)
        operator_perms = get_perms(operators, num_parameters)
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
    count_2 = 0
    operators = "*+|"
    for calculation in tqdm(data):
        goal = int(calculation[0])
        parameters = [int(number) for number in calculation[1]]
        num_parameters = len(parameters)
        operator_perms = get_perms(operators, num_parameters)

        for perm in operator_perms:
            output = reduce(lambda current, operator_and_next: evaluate((current, operator_and_next[1]), operator_and_next[0]),
            zip(perm, parameters[1:]), # the list passed to the reduce via lambda
            parameters[0]) # start at the beginning
        
            if output == goal:
                count_2 += goal
                break
    return count_2


if __name__ == "__main__":
    print("======== Part 1 ========")
    print(part_1(data))
    
    print("======== Part 2 ========")
    print(part_2(data))