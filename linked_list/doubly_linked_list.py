class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def create_list():
    """Creates a list of whole numbers"""
    seq = input("Enter the sequence: ").split()
    int_seq = [int(i) for i in seq]
    head = None
    tail = None
    for i in int_seq:
        if i < 0:
            break
        n = Node(i)
        if head is None:
            head = n
            tail = n
        else:                # Tail must be pointing to some node already
            tail.next = n
            n.prev = tail
            tail = n
    return head, tail

def count_integers_in_list(head):
    """Counts the total number of elements in the list"""
    count = 0
    curr = head
    if head is None:
        return -1
    while curr:
        curr = curr.next
        count += 1
    return count

def traverse_list_forward(head):
    """Traverse the LinkedList in forward direction"""
    if head is None:
        return -1
    curr = head
    arr = []
    while curr:
        arr.append(curr.data)
        curr = curr.next
    return ' '.join(map(str, arr))

def traverse_list_backward(tail):
    """Traverse the linked list in backward direction"""
    if tail is None:
        return -1
    curr = tail
    arr = []
    while curr:
        arr.append(curr.data)
        curr = curr.prev
    return ' '.join(map(str, arr))

def insert_in_list(head, tail, elem, posn):
    """Insert an element in the list"""
    if head is None or tail is None:
        return -1, -1

    total_elements = count_integers_in_list(head)
    if posn > (total_elements + 1) or posn <= 0:
        print("Position must be between 1 and (count of elements + 1)")
        return head, tail

    if posn == 1:
        elem_insert = Node(elem)
        elem_insert.next = head
        head.prev = elem_insert
        head = elem_insert
        print(f"{elem} inserted")
        return head, tail

    elif posn == total_elements + 1:
        elem_insert = Node(elem)
        elem_insert.prev = tail
        tail.next = elem_insert
        tail = elem_insert
        print(f"{elem} inserted")
        return head, tail

    else:
        elem_insert = Node(elem)
        count = 1
        curr = head
        while count != (posn - 1):
            curr = curr.next
            count += 1
        elem_insert = Node(elem)
        elem_insert.prev = curr
        elem_insert.next = curr.next
        curr.next.prev = elem_insert
        curr.next = elem_insert
        print(f"{elem} inserted")
        return head, tail

def delete_from_list(head, tail, elem):
    """Delete an element from the list"""
    if head is None or tail is None:
        return -1, -1

    if head.data == elem:
        if head == tail:
            head = tail = None
            return -1, -1

        curr = head
        head = head.next
        head.prev = None
        curr = None
        print(f"{elem} deleted from head")
        return head, tail

    elif tail.data == elem:
        curr = tail
        if tail == head:
            tail == None
            return -1, -1

        tail = tail.prev
        tail.next = None
        curr = None
        print(f"{elem} deleted from tail")
        return head, tail

    else:
        curr = head
        while curr:
            if curr.data == elem:
                break
            else:
                curr = curr.next

        if not curr:
            print("Element to be deleted was not found")
            return head, tail

        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        print(f"{elem} deleted")
        curr = None
        return head, tail

if __name__ == "__main__":
    head, tail = create_list() # 2 3 5 8 6 9 0 7 1 -1 2 3
    trav = traverse_list_forward(head)
    print(f"Original list: {trav}")
    no_of_elem = count_integers_in_list(head)
    print(f"Total number of elements: {no_of_elem}")
    head, tail = insert_in_list(head, tail, 11, 14)
    head, tail = insert_in_list(head, tail, 11, 0)
    head, tail = insert_in_list(head, tail, 11, 1)
    head, tail = insert_in_list(head, tail, 11, 1)
    head, tail = insert_in_list(head, tail, 11, 12)
    head, tail = insert_in_list(head, tail, 11, 13)
    head, tail = insert_in_list(head, tail, 11, 5)
    head, tail = delete_from_list(head, tail, 11)
    head, tail = delete_from_list(head, tail, 11)
    head, tail = delete_from_list(head, tail, 11)
    head, tail = delete_from_list(head, tail, 11)
    head, tail = delete_from_list(head, tail, 5)
    head, tail = delete_from_list(head, tail, 50)
    head, tail = delete_from_list(head, tail, 1)
    head, tail = delete_from_list(head, tail, 0)
    if head != -1:
        trav = traverse_list_forward(head)
        print(f"Original List: {trav}")
    trav = traverse_list_backward(tail)
    print(f"Reversed List: {trav}")
    no_of_elem = count_integers_in_list(head)
    print(f"Total number of elements: {no_of_elem}")
