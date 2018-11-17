"""Sample implementation of a queue."""


class Queue:
    def __init__(self):
        self.__queue = []

    def __str__(self):
        return "Queue: " + self.__queue.__str__()

    def add(self, element):
        """Function adds an element at the end of the queue."""
        self.__queue.append(element)

    def get(self):
        """Function returns the oldest element and removes it from the queue. Returns None if queue is empty."""
        if len(self.__queue) == 0:
            return None
        elif len(self.__queue) == 1:
            return self.__queue.pop()
        else:
            temp = self.__queue[0]
            self.__queue = self.__queue[1:]
            return temp
