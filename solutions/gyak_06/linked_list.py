#######################################
##### Linked List (Láncolt Lista) #####
#######################################

# Define a single node in the linked list
class Node:
    def __init__(self, data):
        # The data the node holds
        self.data = data
        # A reference (pointer) to the next node in the list
        self.next = None


# Define the LinkedList class to manage nodes
class LinkedList:
    def __init__(self):
        # Initialize the list as empty (no head node yet)
        self.head = None

    # Method to add a new node to the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data

        # If the list is empty, make this node the head
        if not self.head:
            self.head = new_node
            return

        # Otherwise, traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next

        # Attach the new node at the end
        current.next = new_node

    # Method to delete a node by its data value
    def delete(self, data):
        current = self.head  # Start from the head

        # Case 1: The list is empty
        if not current:
            print("List is empty.")
            return

        # Case 2: The head node is the one to delete
        if current.data == data:
            self.head = current.next  # Move head to the next node
            return

        # Case 3: Search for the node to delete
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        # If the node was not found in the list
        if not current:
            print(f"{data} not found in list.")
            return

        # Skip over the node to remove it from the list
        prev.next = current.next

    # Method to print all elements of the linked list
    def display(self):
        current = self.head
        # Traverse through all nodes
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Marks the end of the list


# Example usage of the LinkedList class
lst = LinkedList()    # Create a new empty linked list
lst.append(10)        # Add first node
lst.append(20)        # Add second node
lst.append(30)        # Add third node
lst.display()         # Output: 10 -> 20 -> 30 -> None
