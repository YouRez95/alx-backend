#!/usr/bin/env python3
"""
    Class
      Server
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int):
        """
            return a tuple of size two containing a start
            index and an end index corresponding
            to the range of indexes to return in a list
        """
        size = (page_size * (page - 1), page_size * page)
        return size

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            return the appropriate page of the dataset
        """
        assert (isinstance(page, int) and isinstance(page_size, int)
                and page > 0 and page_size > 0)

        indexes = self.index_range(page, page_size)
        return self.dataset()[indexes[0]:indexes[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
            returns a dictionary containing key-value pairs
        """
        data = self.get_page(page, page_size)
        next_page = None if len(data) == 0 else page + 1
        prev_page = None if page == 1 else page - 1
        total_pages = int(math.ceil(len(self.dataset()) / page_size))
        page_size = 0 if len(data) == 0 else page_size
        final_data = {'page_size': page_size, 'page': page,
                      'data': data, 'next_page': next_page,
                      'prev_page': prev_page, 'total_pages': total_pages}
        return final_data
