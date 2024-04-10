#!/usr/bin/python3
""" Locked class """


class LockedClass():
    """There is no attribute creation unless attribute = firs_name"""
    __slots__ = ['first_name']

    def __init__(self):
        """The Init method"""
        pass
