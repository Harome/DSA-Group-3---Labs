
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    # Create a dummy node to serve as the head of the merged list
    dummy = ListNode()
    current = dummy

    while list1 is not None and list2 is not None:
        # Compare the values of the current nodes in both lists
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        # Move the pointer in the merged list
        current = current.next

    # If any list is not fully traversed, append the remaining nodes
    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    # Create the merged list starting from the next of the dummy node
    merged_list_head = dummy.next

    # Sort the merged list
    sorted_result = []
    current = merged_list_head
    while current is not None:
        sorted_result.append(current.value)
        current = current.next
    sorted_result.sort()

    # Create a new linked list for the sorted result
    sorted_list_head = ListNode()
    current = sorted_list_head
    for value in sorted_result:
        current.next = ListNode(value)
        current = current.next

    return sorted_list_head.next

def print_list(head):
    values = []
    while head is not None:
        values.append(head.value)
        head = head.next
    return values

def create_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Function to get user input for the lists
def get_user_input_list():
    user_input = input("Do you want to input your own lists? (yes/no): ").lower()
    if user_input == "yes":
        list1 = get_user_input_list("Enter values for list1 (comma-separated): ")
        list2 = get_user_input_list("Enter values for list2 (comma-separated): ")
    else:
        list1 = create_list([1, 2, 4,1])
        list2 = create_list([1, 3, 4,5])

    return list1, list2

# Main function to execute when the script is run
def main():
    list1, list2 = get_user_input_list()
    merged_list = merge_sorted_lists(list1, list2)

    print("Merged List:")
    print_list(merged_list)

if __name__ == "__main__":
    main()
