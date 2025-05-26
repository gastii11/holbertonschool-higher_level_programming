#!/usr/bin/python3
"""clase que hereda list"""


class MyList(list):

    """MyList hereda list"""
    def print_sorted(self):
        print(sorted(self))
