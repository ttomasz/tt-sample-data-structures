"""Sample implementation of a linked list."""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, first_node_value):
        self.head = Node(first_node_value)

    def __str__(self):
        return "Linked list - values: " + self.as_list().__str__()

    def as_list(self) -> list:
        """Function returns a list with all the values from the linked list."""
        array = []
        temp = self.head
        while temp:
            array.append(temp.value)
            temp = temp.next
        return array

    def add(self, value):
        """Function adds a new node with given value to the end of the linked list."""
        new_node = Node(value)
        temp = self.head
        if temp is None:
            self.head = new_node
        else:
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def remove_last(self):
        """Function removes the last node from the linked list."""
        previous_node = None
        last_node = self.head
        if self.head:
            if last_node.next:
                while last_node.next:
                    previous_node = last_node
                    last_node = last_node.next
                previous_node.next = None
            else:
                self.head = None

    def remove_first(self):
        """Function removes the first element of the linked list."""
        if self.head:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None

    def add_at_the_beginning(self, value):
        """Function adds a new node with given value at the beginning of the linked list
        moving the rest of the values one step further."""
        temp = self.head
        self.head = Node(value)
        self.head.next = temp
