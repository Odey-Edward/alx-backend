#!/usr/bin/env python3
"""File contain Server class definition"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """initialization method"""
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

    @staticmethod
    def index_range(page=0, page_size=0):
        """return a tuple containing paginated indexies"""
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return start_index, end_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return an array of data items for a particular page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        page_index = self.index_range(page, page_size)

        data_set = self.dataset()

        return data_set[page_index[0]:page_index[1]]







