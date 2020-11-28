class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        stringOutput = ''
        curr = self
        while curr:
            stringOutput += str(curr.value)
            curr = curr.next
        return stringOutput

# Reverse a singly linked list iteratively
# first solution: iterate through linked list and store in list object. then reverse it and turn into linked list


def reverseLinkedList(head):
    curr = head
    array = []

    while curr:
        array.append(curr.value)
        curr = curr.next

    newHead = None

    for item in reversed(array):
        if newHead is None:
            newHead = Node(item)
            newCurr = newHead
        else:
            newCurr.next = Node(item)
            newCurr = newCurr.next

    return newHead


linkedList = Node(5, Node(3, Node(7)))
print(reverseLinkedList(linkedList))

# time O(n), space O(n)
