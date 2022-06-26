from itertools import chain

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class Iterator:

    def __init__(self, nested_list):
        self.start = -1
        self.end = len(nested_list)


    def __iter__(self):
        return self


    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self


    def __str__(self):
        chain(*nested_list)
        return '\n'.join(str(elem) for elem in chain(*nested_list))


if __name__ == '__main__':
    for elem in Iterator(nested_list):
        print(elem)