from itertools import chain


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

def one_list(ls: list) -> list:
    chain(*nested_list)
    res = [elem for elem in chain(*nested_list)]
    return res


def show():
    for obj in one_list():
        yield obj
        obj += 1


if __name__ == '__main__':
    some_ls = []
    for item in one_list(nested_list):
        some_ls.append(item)

#print(some_ls)