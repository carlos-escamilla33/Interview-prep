class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0

    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break

    return cycle_length


def find_start(head, cycle_length):
    pointer1 = head
    pointer2 = head

    while cycle_length > 0:
        pointer2 = pointer2.next
        cycle_length -= 1

    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1


def findCycleStart(head):
    cycle_length = 0
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        print("slow: ", slow.val)
        print("fast: ", fast.val)
        if slow == fast:
            cycle_length = calculate_cycle_length(slow)
            break

    return find_start(head, cycle_length)


print(findCycleStart(head).val)
