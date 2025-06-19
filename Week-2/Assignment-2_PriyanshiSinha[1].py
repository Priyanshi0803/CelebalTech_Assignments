class Node:
    """A Node in a singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly Linked List implementation"""
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Add a node with the given data to the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        # Traversing to the end
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print the entire list"""
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index)"""
        try:
            if n <= 0:
                raise IndexError("Index should be 1 or greater.")

            if not self.head:
                raise Exception("Cannot delete from an empty list.")

            if n == 1:
                deleted_data = self.head.data
                self.head = self.head.next
                print(f"Deleted node {n} with data: {deleted_data}")
                return

            current = self.head
            prev = None
            count = 1

            while current and count < n:
                prev = current
                current = current.next
                count += 1

            if not current:
                raise IndexError("Index out of range.")

            prev.next = current.next
            print(f"Deleted node {n} with data: {current.data}")

        except Exception as e:
            print(f"Error: {e}")


# Implementation
if __name__ == "__main__":
    ll = LinkedList()

    print("Adding nodes:")
    for value in [10, 20, 30, 40, 50]:
        ll.add_node(value)
        ll.print_list()

    print("\nDelete 3rd node:")
    ll.delete_nth_node(3)
    ll.print_list()

    print("\nDelete 1st node:")
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nDelete node at index 10 (out of range):")
    ll.delete_nth_node(10)
    ll.print_list()

    print("\nDelete all remaining nodes:")
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)

    print("\nTry deleting from empty list:")
    ll.delete_nth_node(1)
