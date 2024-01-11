class LNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def sorted_linked_list():
    try:
        values = input("Kindly enter sorted values separated by space: ").split()
        values = [int(val) if val.isdigit() or (val[0] == '-' and val[1:].isdigit()) else val for val in values]
        values.sort()
        return linked_list(values)
    except ValueError:
        print("Invalid input. Please enter valid integer values.")
        return None

def linked_list(values):
    dummy = LNode()
    current = dummy

    for value in values:
        current.next = LNode(value)
        current = current.next

    return dummy.next

def merge_sorted_linked_lists(list1, list2):
    dummy = LNode()
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next

print("Enter values for the first linked list:")
linked_list1 = sorted_linked_list()

if linked_list1 is not None:
    print("\nEnter values for the second linked list:")
    linked_list2 = sorted_linked_list()

    if linked_list2 is not None:
        merged_linked_list = merge_sorted_linked_lists(linked_list1, linked_list2)

        print("\nMerged List:", end="-> ")
        while merged_linked_list is not None:
            print(merged_linked_list.value, end=" ->")
            if merged_linked_list.next is not None:
                print(end=" ")
            merged_linked_list = merged_linked_list.next

        print()
