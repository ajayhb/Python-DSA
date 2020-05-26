class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def create_list():
    """Creates a list of whole numbers from scratch"""
    seq = input("Enter the sequence: ").split()
    int_seq = [int(i) for i in seq]
    head = None
    tail = None
    for num in int_seq:
        if num == -1:
            break
        number = Node(num)
        if head is None:
            head = number
            tail = number
        else:
            tail.next = number
            number.prev = tail
            tail = number
            tail.next = head
            head.prev = tail
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

def traverse_list_fwd(head):
    """Prints all elements from head to tail in forward direction"""
    if head is None:
        return -1
    curr = head
    arr = []
    while curr.next != head:
        arr.append(curr.data)
        curr = curr.next
    arr.append(curr.data)
    return ' '.join(map(str, arr))

def traverse_list_rev(tail):
    """Prints all elements from tail to head in reverse direction"""
    if tail is None:
        return -1
    curr = tail
    arr = []
    while curr.prev != tail:
        arr.append(curr.data)
        curr = curr.prev
    arr.append(curr.data)
    return " ".join(map(str, arr))

def insert_in_list(head, tail, elem, posn):
    """Inserts an element into the List"""
    count_elem = count_elements(head)
    if posn <= 0 or posn > (count_elem + 1):
        print("Position must be in between 1 and total_elements + 1")
        return head, tail

    if None in (head, tail):
        return -1, -1

    element = Node(elem)

    if posn == 1:        # Insert in first position
        element.next = head
        head.prev = element
        element.prev = tail
        tail.next = element
        head = element
        print(f"{elem} inserted in fst position")
        return head, tail

    elif posn == count_elem + 1:  # Insert in last position
        element.next = head
        element.prev = tail
        tail.next = element
        head.prev = element
        tail = element
        print(f"{elem} inserted in last position")
        return head, tail

    else:                      # Insert in between
        curr = head
        count = 1
        while count != (posn - 1):
            curr = curr.next
            count += 1

        element.next = curr.next
        curr.next = element
        element.prev = curr
        element.next.prev = element
        print(f"{elem} inserted in between")
        return head, tail

def delete_from_list(head, tail, elem):
    """Deletes an element from the list"""
    if None in (head, tail):
        return -1, -1
    count_elem = count_elements(head)
    if count_elem == 1:
        if elem == head.data:
            head = tail = None
            return -1, -1
        else:
            print("Element to be deleted was not found in this single node list")
            return head, tail

    if elem == head.data: # Delete the first element
        curr = head
        tail.next = curr.next
        curr.next.prev = tail
        head = head.next
        curr = None
        print(f"{elem} deleted from fst position")
        return head, tail

    elif elem == tail.data: # Delete the last element
        curr = tail
        tail = curr.prev
        tail.next = curr.next
        curr.next.prev = tail
        curr = None
        print(f"{elem} deleted from last position")
        return head, tail

    else:                        # Delete the middle elem if it exists
        curr = head
        while curr.next != head:
            curr = curr.next
            if curr.data == elem:
                break
            else:
                continue
        if curr.data == elem:   # Element to be deleted found in between
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr = None
            print(f"{elem} deleted")
            return head, tail
        else:
            print("Element to be deleted was not found!")
            return head, tail

if __name__ == "__main__":
    head, tail = create_list() # 2 3 5 8 6 9 0 7 1 -1 2 3
    trav = traverse_list_fwd(head)
    print(f"Original list: {trav}")
    no_of_elem = count_elements(head)
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
        trav = traverse_list_fwd(head)
        print(f"Original List: {trav}")
    trav = traverse_list_rev(tail)
    print(f"Reversed List: {trav}")
    no_of_elem = count_elements(head)
    print(f"Total number of elements: {no_of_elem}")
