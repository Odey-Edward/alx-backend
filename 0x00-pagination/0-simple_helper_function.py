#!/usr/bin/env python3
"""return a tuple of size two containing a start index and an end
index corresponding to the range of indexes to return in a list for
those particular pagination parameters."""


def index_range(page=0, page_size=0):
    """return a tuple containing paginated indexies"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
