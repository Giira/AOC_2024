from tqdm import tqdm

with open("Day11.txt") as f:
    data = [int(number.strip()) for number in f.read().split(" ")]


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


def solve(data, blinks):
    for i in tqdm(range(blinks)):
        data = apply_rules(data)
    return len(data)


data_to_dic = {number: 1 for number in data}


def apply_rules_dic(data_dic):
    data_dic_2 = {}
    for number in data_dic:
        if number == 0:
            if 1 not in data_dic_2:
                data_dic_2[1] = data_dic[0]
            else:
                data_dic_2[1] += data_dic[0]
        elif len(str(number)) % 2 == 0:
            split_len = int(len(str(number)) / 2)
            splits = [int(str(number)[:split_len]), int(str(number)[split_len:])]
            for num in splits:
                if num not in data_dic_2:
                    data_dic_2[num] = data_dic[number]
                else:
                    data_dic_2[num] += data_dic[number]
        else:
            if number * 2024 not in data_dic_2:
                data_dic_2[number * 2024] = data_dic[number]
            else:
                data_dic_2[number * 2024] += data_dic[number]
    return data_dic_2


def solve_2(dic, blinks):
    for i in tqdm(range(blinks)):
        dic = apply_rules_dic(dic)
    count = 0
    for key, value in dic.items():
        count += value
    return count


if __name__ == "__main__":
    print("======== Part 1 ========")
    print(solve(data, 25))
    
    print("======== Part 2 ========")
    print(solve_2(data_to_dic, 75))
