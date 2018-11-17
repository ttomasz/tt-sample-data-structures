"""Sample implementation of min and max binary heaps."""
from math import floor


class MinHeap:
    def __init__(self):
        self.__heap = []

    def __str__(self):
        return "MinHeap - array representation: " + self.__heap.__str__()

    def __up_heap(self, index: int):
        parent_index = floor((index - 1) / 2)
        parent_value = self.__heap[parent_index]
        child_value = self.__heap[index]
        if index == 0 or parent_value < child_value:
            return None
        else:
            temp = parent_value
            self.__heap[parent_index] = child_value
            self.__heap[index] = temp
            return self.__up_heap(parent_index)

    def __down_heap(self, index: int = 0):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.__heap) and self.__heap[left] < self.__heap[largest]:
            largest = left

        if right < len(self.__heap) and self.__heap[right] < self.__heap[largest]:
            largest = right

        if largest != index:
            temp = self.__heap[index]
            self.__heap[index] = self.__heap[largest]
            self.__heap[largest] = temp
            return self.__down_heap(largest)
        else:
            return None

    def insert(self, value):
        """Function inserts given value into heap and returns inserted value."""
        self.__heap.append(value)
        self.__up_heap(len(self.__heap)-1)
        return value

    def extract(self):
        """Function extracts min value from heap, removes it from heap and rebuilds the heap.
        Returns None if heap is empty."""
        minval = self.min_value()
        if minval:
            if len(self.__heap) == 1:
                self.__heap.pop()
            else:
                self.__heap[0] = self.__heap.pop()
                self.__down_heap()
        return minval

    def min_value(self):
        """Function returns min value from heap without modifying the heap. Returns None if heap is empty."""
        try:
            temp = self.__heap[0]
        except IndexError:
            return None
        return temp


class MaxHeap:
    def __init__(self):
        self.__heap = []

    def __str__(self):
        return "MaxHeap - array representation: " + self.__heap.__str__()

    def __up_heap(self, index: int):
        parent_index = floor((index - 1) / 2)
        parent_value = self.__heap[parent_index]
        child_value = self.__heap[index]
        if index == 0 or parent_value > child_value:
            return None
        else:
            temp = parent_value
            self.__heap[parent_index] = child_value
            self.__heap[index] = temp
            return self.__up_heap(parent_index)

    def __down_heap(self, index: int = 0):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.__heap) and self.__heap[left] > self.__heap[largest]:
            largest = left

        if right < len(self.__heap) and self.__heap[right] > self.__heap[largest]:
            largest = right

        if largest != index:
            temp = self.__heap[index]
            self.__heap[index] = self.__heap[largest]
            self.__heap[largest] = temp
            return self.__down_heap(largest)
        else:
            return None

    def insert(self, value):
        """Function inserts given value into heap and returns inserted value."""
        self.__heap.append(value)
        self.__up_heap(len(self.__heap)-1)
        return value

    def extract(self):
        """Function extracts max value from heap, removes it from heap and rebuilds the heap.
        Returns None if heap is empty."""
        maxval = self.max_value()
        if maxval:
            if len(self.__heap) == 1:
                self.__heap.pop()
            else:
                self.__heap[0] = self.__heap.pop()
                self.__down_heap()
        return maxval

    def max_value(self):
        """Function returns max value from heap without modifying the heap. Returns None if heap is empty."""
        try:
            temp = self.__heap[0]
        except IndexError:
            return None
        return temp
