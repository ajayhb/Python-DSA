class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_list():
    """Creates a list of whole numbers"""
    seq = input("Enter the sequence of integers: ").split()
    int_seq = [int(i) for i in seq]
    head = None
    tail = None
    for number in int_seq:
        if number < 0:
            break
        node = Node(number)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node

    return head, tail

def traverse_list(head):
    """Prints every element from head to tail"""
    if head is None:
        return -1
    curr = head
    print_list = []
    while curr:
        print_list.append(curr.data)
        curr = curr.next
    return ' '.join(map(str, print_list))

def count_no_of_elements(head):
    """Counts the total number of elements in the list"""
    if head is None:
        return 0
    curr = head
    counter = 0
    while curr:
        curr = curr.next
        counter += 1
    return counter

def insert_element(head, tail, elem, posn):
    """Inserts an element in the linkedlist"""
    no_of_elem = count_no_of_elements(head)

    if None in (head, tail):
        return -1, -1

    if posn <= 0 or posn > no_of_elem + 1:
        print("Position must be between 1 and (count of elements + 1)")
        return head, tail

    if posn == 1:       # Insert at the beginning
        element = Node(elem)
        element.next = head
        head = element
        print(f"{elem} inserted")
        return head, tail

    elif posn == no_of_elem + 1:  # Insert at the end
        element = Node(elem)
        tail.next = element
        tail = element
        print(f"{elem} inserted")
        return head, tail

    else:                  # Insert in between
        counter = 1
        curr = head
        while counter != (posn - 1):
            curr = curr.next
            counter += 1
        element = Node(elem)
        element.next = curr.next
        curr.next = element
        print(f"{elem} inserted")
        return head, tail

def delete_elem(head, tail, elem):
    """Deletes a particular element from the LinkedList"""
    curr = head
    prev_elem = head

    while curr:
        if curr.data == elem:
            break
        else:
            prev = curr
            curr = curr.next

    if curr == head:        # Delete the first element
        head = curr.next
        curr = None
        print(f"{elem} deleted from head")
        return head, tail

    if curr == tail:       #  Delete the last element
        tail = prev
        prev.next = None
        curr = None
        print(f"{elem} deleted from tail")
        return head, tail

    if curr:                # Delete in between
        prev.next = curr.next
        curr.next = None
        curr = None
        print(f"{elem} deleted!")
        return head, tail

    else:
        print("Element to be deleted was not found in the list")
        return head, tail

def reverse_the_list(head, tail):
    """Reverses a linkedlist"""
    if head == tail:
        return head, tail

    if None in (head, tail):
        return -1, -1

    curr = head
    ahead = head.next

    if ahead.next is not None:
        alternate = ahead.next
    else:
        alternate = ahead

    head.next = None
    tail = curr

    while alternate:
        ahead.next = curr
        curr = ahead
        if ahead == alternate:
            head = ahead
            return head, tail
        else:
            ahead = alternate

        if alternate.next is not None:
            alternate = alternate.next
        else:
            head = alternate
            head.next = curr
            return head, tail

if __name__ == "__main__":
    head, tail = create_list() # 2 3 5 8 6 9 0 7 1 -1 2 3
    trav = traverse_list(head)
    print(f"Original list: {trav}")
    no_of_elem = count_no_of_elements(head)
    print(f"Total number of elements: {no_of_elem}")
    head, tail = insert_element(head, tail, 11, 14)
    head, tail = insert_element(head, tail, 11, 0)
    head, tail = insert_element(head, tail, 11, 1)
    head, tail = insert_element(head, tail, 11, 1)
    head, tail = insert_element(head, tail, 11, 12)
    head, tail = insert_element(head, tail, 11, 13)
    head, tail = insert_element(head, tail, 11, 5)
    head, tail = delete_elem(head, tail, 11)
    head, tail = delete_elem(head, tail, 11)
    head, tail = delete_elem(head, tail, 11)
    head, tail = delete_elem(head, tail, 11)
    head, tail = delete_elem(head, tail, 5)
    head, tail = delete_elem(head, tail, 50)
    head, tail = delete_elem(head, tail, 1)
    head, tail = delete_elem(head, tail, 0)
    if head != -1:
        trav = traverse_list(head)
        print(f"Original List: {trav}")
    head, tail = reverse_the_list(head, tail)
    if head != -1:
        trav = traverse_list(head)
        print(f"Reversed List: {trav}")
    else:
        print(head)
    no_of_elem = count_no_of_elements(head)
    print(f"Total number of elements: {no_of_elem}")
