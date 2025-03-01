"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    # pylint: disable=unused-argument,missing-module-docstring
    def __init__(self, data: Iterable = (), priorities = (), max_size: int = None):
        self.data = []
        self.priorities = []
        for element in data:
            self.data.insert(0, element)
            self.priorities.insert(0, len(self.priorities))

    def put(self, element, priority):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        self.priorities.insert(0, priority)
        self.data.insert(0, element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        prioritized_index = min(self.priorities)
        self.priorities.pop(prioritized_index)
        return self.data.pop(prioritized_index)

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return not self.data

    # pylint: disable=no-self-use
    def full(self) -> bool:
        """
        Return whether queue_ is full or not
        :return: True if queue_ is full.
                 False if queue_ is not full
        """
        return False

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return len(self.data)

    def top(self):
        """
        Return the first element in queue_
        :return: Item from queue_
        """
        return self.data[-1]

    # pylint: disable=no-self-use
    def capacity(self) -> int:
        """
        Return the maximal size of queue_
        :return: Maximal size of queue_
        """
        return 0
