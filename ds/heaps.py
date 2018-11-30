"""Sample implementation of min and max binary heaps."""
from math import floor


class Heap:
    """Base class for implementing Heaps"""
    def __init__(self):
        self.heap = []

    def _up_heap(self, index: int):
        # To be overridden
        pass

    def _down_heap(self, index: int = 0):
        # To be overridden
        pass

    def _first_value(self):
        """Function returns first value from heap without modifying the heap. Returns None if heap is empty."""
        try:
            temp = self.heap[0]
        except IndexError:
            return None
        return temp

    def insert(self, value):
        """Function inserts given value into heap and returns inserted value."""
        self.heap.append(value)
        self._up_heap(len(self.heap) - 1)
        return value

    def extract(self):
        """Function extracts min value from heap, removes it from heap and rebuilds the heap.
        Returns None if heap is empty."""
        first_value = self._first_value()
        if first_value is not None:
            if len(self.heap) == 1:
                self.heap.pop()
            else:
                self.heap[0] = self.heap.pop()
                self._down_heap()
        return first_value


class MinHeap(Heap):
    """Min Heap"""

    def __str__(self):
        return "MinHeap - array representation: " + self.heap.__str__()

    def _up_heap(self, index: int):
        parent_index = floor((index - 1) / 2)
        parent_value = self.heap[parent_index]
        child_value = self.heap[index]
        if index == 0 or parent_value < child_value:
            return None
        else:
            temp = parent_value
            self.heap[parent_index] = child_value
            self.heap[index] = temp
            return self._up_heap(parent_index)

    def _down_heap(self, index: int = 0):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] < self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] < self.heap[largest]:
            largest = right

        if largest != index:
            temp = self.heap[index]
            self.heap[index] = self.heap[largest]
            self.heap[largest] = temp
            return self._down_heap(largest)
        else:
            return None

    def min_value(self):
        """Function returns min value from heap without modifying the heap. Returns None if heap is empty."""
        return self._first_value()


class MaxHeap(Heap):
    """Max Heap"""

    def __str__(self):
        return "MaxHeap - array representation: " + self.heap.__str__()

    def _up_heap(self, index: int):
        parent_index = floor((index - 1) / 2)
        parent_value = self.heap[parent_index]
        child_value = self.heap[index]
        if index == 0 or parent_value > child_value:
            return None
        else:
            temp = parent_value
            self.heap[parent_index] = child_value
            self.heap[index] = temp
            return self._up_heap(parent_index)

    def _down_heap(self, index: int = 0):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            temp = self.heap[index]
            self.heap[index] = self.heap[largest]
            self.heap[largest] = temp
            return self._down_heap(largest)
        else:
            return None

    def max_value(self):
        """Function returns max value from heap without modifying the heap. Returns None if heap is empty."""
        return self._first_value()
