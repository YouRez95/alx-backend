#!/usr/bin/env python3
"""
    function
        index_range
"""


def index_range(page: int, page_size: int):
    """
        return a tuple of size two containing a start
        index and an end index corresponding
        to the range of indexes to return in a list
    """
    size = (page_size * (page - 1), page_size * page)
    return size
