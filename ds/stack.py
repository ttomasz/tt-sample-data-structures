"""Sample implementation of a stack."""


class Stack:
    def __init__(self):
        self.__stack = []

    def __str__(self):
        return "Stack: " + self.__stack.__str__()

    def add(self, element):
        """Function adds an element to the stack."""
        self.__stack.append(element)

    def get(self):
        """Function returns an element from the top of the stack. Returns None if stack is empty."""
        try:
            temp = self.__stack.pop()
        except IndexError:
            temp = None
        return temp
