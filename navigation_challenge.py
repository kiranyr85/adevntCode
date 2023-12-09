import sys

map = {
    'AAA': ('BBB', 'CCC'),
    'BBB': ('DDD', 'EEE'),
    'CCC': ('ZZZ', 'GGG'),
    'DDD': ('DDD', 'DDD'),
    'EEE': ('EEE', 'EEE'),
    'GGG': ('GGG', 'GGG'),
    'ZZZ': ('ZZZ', 'ZZZ')
}


class node:
    def __init__(self, name: str, data_tuple: tuple):
        self.name = name
        self.R = data_tuple[0]
        self.L = data_tuple[1]

    def __str__(self):
        return f"{self.name} : ({self.R},{self.L})"


class_map = {}
for key, value in map.items():
    class_map[key] = node(key, value)
    # print(f"Created classfor key {key}: {class_map[key]}")


def traverse_path(start_point, path):
    next_point = start_point
    for step in path:
        print(class_map[next_point])
        if step == 'L':
            next_point = class_map[next_point].L
        elif step == 'R':
            next_point = class_map[next_point].R
        else:
            print("Wrong direction... Try only Left (L) Right (R) combination LRLLR....")


def prune_path_letters(path: str):
    temp_set = set()
    for x in path.upper():
        if x not in ('L', 'R'):
            temp_set.add(x)
    if len(temp_set) > 0:
        print("Wrong letters", temp_set)
        return False
    else:
        return True


def main():
    print("Welcome to path navigator...")
    print(f"Path points are {class_map.keys()}")
    start_point = None
    path = None
    while True:
        start_point = input("Enter start point from above path list:")
        if start_point not in class_map.keys():
            print("Wrong path point. Please try again")
        else:
            break
    while True:
        path = input("Enter navigation steps like LR LRL ...:")
        if not prune_path_letters(path):
            print("Try again with valid path....")
        else:
            break
    # Print path points
    traverse_path(start_point, path)


if __name__ == '__main__':
    try:
        while True:
            print("Start navigation......")
            main()
    except (KeyboardInterrupt, SystemExit) as e:
        print('program stopped manually')
        sys.exit()
