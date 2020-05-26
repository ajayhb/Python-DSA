class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_list():
    """Creates a list of whole numbers"""
    seq = input("Enter the sequence: ").split()
    int_seq = [int(i) for i in seq]
    head = None
    tail = None
    for num in int_seq:
        if num < 0:
            break
        n = Node(num)
        if head is None:
            head = n
            tail = n
        else:
            tail.next = n
            tail = n
    tail.next = head
    return head, tail

def count_elements(head):
    """Counts the total number of elements inside the list"""
    if head is None:
        return -1
    count = 1
    curr = head
    while curr.next != head:
        count += 1
        curr = curr.next
    return count

def traverse_list(head):
    """Prints all the elements inside the list"""
    if head is None:
        return -1
    curr = head
    arr = []
    while curr.next != head:
        arr.append(curr.data)
        curr = curr.next
    arr.append(curr.data)
    return ' '.join(map(str, arr))

def insert_into_list(head, tail, elem, posn):
    """Inserts an element inside the list"""
    if None in (head, tail):
        return -1, -1

    total_elements = count_elements(head)
    if posn <= 0 or posn > (total_elements + 1):
        print("Position must be in between 1 and total_elements + 1")
        return head, tail

    if posn == 1: # Insert at first position
        e = Node(elem)
        tail.next = e
        e.next = head
        head = e
        print(f"{elem} inserted")
        return head, tail

    elif posn == total_elements + 1: # Insert at last position
        e = Node(elem)
        tail.next = e
        tail = e
        e.next = head
        print(f"{elem} inserted")
        return head, tail

    else:             # Insert in between
        counter = 1
        curr = head
        while counter != (posn -1):
            curr = curr.next
            counter += 1

        e = Node(elem)
        e.next = curr.next
        curr.next = e
        print(f"{elem} inserted")
        return head, tail

def delete_from_list(head, tail, elem):
    """Deletes an element that is currently present in the list"""
    if None in (head, tail):
        return -1, -1

    curr = head
    prev = head

    if curr.data == elem:      # Delete first element
        tail.next = curr.next
        head = curr.next
        curr = None
        print(f"{elem} deleted from head")
        return head, tail

    while curr != tail:
        prev = curr
        curr = curr.next
        if curr.data == elem:
            break
        else:
            continue

    if curr.data == elem:      # Element found
        if curr == tail:       # Delete Last element
            prev.next = tail.next
            tail = prev
            curr = None
            print(f"{elem} deleted from tail")
            return head, tail
        else:                  # Delete middle element
            prev.next = curr.next
            curr = None
            print(f"{elem} deleted")
            return head, tail
    else:                     # Element to be deleted was NOT found
        print("Element to be deleted was not found")
        return head, tail

def reverse_list(head, tail):
    """Reverses the current list"""
    if None in (head, tail):
        return -1, -1

    count = count_elements(head)
    if count == 1:
        return head, tail

    else:
        curr = head
        ahead = curr.next
        alternative = ahead.next
        curr.next = tail
        ahead.next = curr
    if count == 2:
        head = ahead
        tail = curr
        return head, tail
    else:
        while alternative.next:
            ahead.next = curr
            curr = ahead
            ahead = alternative
            if alternative.next == head:
                alternative.next = curr
                head.next = alternative
                tail = head
                head = alternative
                return head, tail
            else:
                alternative = alternative.next

if __name__ == "__main__":
    head, tail = create_list() # 2 3 5 8 6 9 0 7 1 -1 2 3
    trav = traverse_list(head)
    print(f"Original list: {trav}")
    no_of_elem = count_elements(head)
    print(f"Total number of elements: {no_of_elem}")
    head, tail = insert_into_list(head, tail, 11, 14)
    head, tail = insert_into_list(head, tail, 11, 0)
    head, tail = insert_into_list(head, tail, 11, 1)
    head, tail = insert_into_list(head, tail, 11, 1)
    head, tail = insert_into_list(head, tail, 11, 12)
    head, tail = insert_into_list(head, tail, 11, 13)
    head, tail = insert_into_list(head, tail, 11, 5)
    head, tail = delete_from_list(head, tail, 11)
    head, tail = delete_from_list(head, tail, 11)
    head, tail = delete_from_list(head, tail, 11)
    head, tail = delete_from_list(head, tail, 11)
    head, tail = delete_from_list(head, tail, 5)
    head, tail = delete_from_list(head, tail, 50)
    head, tail = delete_from_list(head, tail, 1)
    head, tail = delete_from_list(head, tail, 0)
    if head != -1:
        trav = traverse_list(head)
        print(f"Original List: {trav}")
    head, tail = reverse_list(head, tail)
    if head != -1:
        trav = traverse_list(head)
        print(f"Reversed List: {trav}")
    else:
        print(head)
    no_of_elem = count_elements(head)
    print(f"Total number of elements: {no_of_elem}")
