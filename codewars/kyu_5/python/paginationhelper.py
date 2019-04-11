# https://www.codewars.com/kata/paginationhelper/

import math

class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self._collection = collection
        self._items_per_page = items_per_page
    
    def item_count(self):
        return len(self._collection)
    
    def page_count(self):
        q, r = divmod(self.item_count(), self._items_per_page)
        if r != 0:
            q += 1
        return q

    def page_item_count(self, page_index):
        q, _ = divmod(self.item_count(), self._items_per_page)
        if page_index <= q - 1:
            return self._items_per_page
        if page_index == q:
            return self.item_count() - self._items_per_page * q
        return -1
    
    def page_index(self, item_index):
        if not self._collection:
            return -1
        if item_index < 0:
            return -1
        if item_index > self.item_count() - 1:
            return -1
        if item_index == 0:
            return 0
        q, _ = divmod(item_index, self._items_per_page)
        if q < self.page_count():
            return q
        return -1
