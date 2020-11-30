class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        output = ''
        curr = self
        while curr:
            output += str(curr.value)
            curr = curr.next
        return output


def removeValues(head, value):
    if (head == None):
        return head

    if head == value:
        return removeValues(head.next)

    prev = head
    curr = head.next

    while curr:
        if curr.value == value:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return head


# Input: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6, val = 6
# Output: 1 -> 2 -> 3 -> 4 -> 5
linkedList = Node(1, Node(2, Node(6, Node(3, Node(4, Node(5, Node(6)))))))
print(removeValues(linkedList, 6))
