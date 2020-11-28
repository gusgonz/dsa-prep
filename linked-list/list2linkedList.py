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


def list2linkedList(inputList):
    head = None

    for value in inputList:
        if not head:
            head = Node(value)
            curr = head
        else:
            curr.next = Node(value)
            curr = curr.next

    return head


print(list2linkedList([0, 1, 2]))
