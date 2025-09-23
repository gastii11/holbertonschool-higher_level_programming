#!/usr/bin/python3

class VerboseList(list):
    def append(self, item):
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, x):
        print(f"Extended the list with [{x}] items.")
        super().extend(x)

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        print(f"Popped [{index}] from the list.")
        return super().pop(index)
