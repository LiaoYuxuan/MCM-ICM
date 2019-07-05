from LinkedListDS.Node import Node


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.counter = 0

    def traverse_list(self):
        actualNode = self.head
        while actualNode is not None:
            print("%d->" % actualNode.data, end="")
            actualNode = actualNode.next
        print("null")

    # O(1)
    def insert_start(self, data):
        self.counter += 1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        # True表示插入成功
        return True

    # O(1)
    def size(self):
        # return 'The size of the List is ' + str(self.counter)
        return self.counter

    # O(n)
    def insert_end(self, data):
        if self.head is None:
            self.insert_start(data)
            return True

        self.counter += 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.next is not None:
            actualNode = actualNode.next

        actualNode.next = newNode
        # True表示插入成功
        return True

    def remove(self, data):
        if self.head:
            if data == self.head.data:
                self.head = self.head.next
                self.counter -= 1
                return True
            else:
                result = self.head.next.remove(data, self.head)
                if result:
                    self.counter -= 1
                return result
        else:
            return False
