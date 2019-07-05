class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def remove(self, data, prev):
        if self.data == data:
            prev.next = self.next
            del self.data
            del self.next
            return True
        else:
            if self.next is not None:
                return self.next.remove(data, self)
            else:
                return False
