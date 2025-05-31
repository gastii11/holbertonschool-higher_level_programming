#!/usr/bin/python3

class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1

    try:
        return next(self.iterator)
    except StopIterable:
        self.count -= 1
        raise

    def get_count(self):
        return self.count