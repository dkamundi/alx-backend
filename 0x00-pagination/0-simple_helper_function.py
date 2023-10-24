#!/usr/bin/env python3

from typing import Tuple
def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given pagination page and page size.
    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start index and end index for the page.
    """
    if page <= 0 or page_size <=0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1)*page_size
    end_index = page * page_size
    
    return start_index, end_index
