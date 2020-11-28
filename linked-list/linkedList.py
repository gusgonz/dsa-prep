class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        curr = self
        stringOutput = ''
        while curr:
            stringOutput += str(curr.value)
            curr = curr.next
        return stringOutput


print(Node(0, Node(1, Node(2))))
