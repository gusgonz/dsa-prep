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


# time O(n), space O(n)


# 1 -> 2 -> 3 -> null
# 3 -> 2 -> 1 -> null

# prev = 3 -> 2 -> 1 -> null
# curr = null
# next = null


def reverseLinkedList2(head):
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next

    return prev

# time O(n), space O(1)


linkedList = Node(5, Node(3, Node(7)))
print(reverseLinkedList(linkedList))
print(reverseLinkedList2(linkedList))
