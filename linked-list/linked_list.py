class Node(object):
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.next = succeeding
        self.previous = previous


class LinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None

    def push(self, value):
        if(self.is_empty()):
            self.first = Node(value, None, None)
            self.last = self.first
        else:
            node = Node(value, self.first, None)
            self.first.previous = node
            self.first = node

    def pop(self):
        if(self.is_empty()):
            raise Exception("Trying to invoke pop() on empty Linked List!")
        else:
            node = self.first
            self.first = self.first.next
            return node.value

    def unshift(self, value):
        if(self.is_empty()):
            self.last = Node(value, None, None)
            self.first = self.last
        else:
            node = Node(value, None, self.last)
            self.last.next = node
            self.last = node

    def shift(self):
        if(self.is_empty()):
            raise Exception("Trying to invoke shift() on empty Linked List!")
        else:
            node = self.last
            self.last = self.last.previous
            return node.value

    def is_empty(self):
        return self.first == None and self.last == None
