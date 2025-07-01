
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data 
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def inser_node_at_tail(self,data):
        new_node = SinglyLinkedListNode(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

    def print_singly_linked_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next




if __name__ == "__main__":
    Llinst = SinglyLinkedList()

    n = int(input())
    for _ in range(n):
        data = int(input())
        Llinst.inser_node_at_tail(data)
    Llinst.print_singly_linked_list()