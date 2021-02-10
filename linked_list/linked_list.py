class Node:
    """Provide a simple node for use with the LinkedList class.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    # get the first node that contains the given data
    def get(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next

    # insert after the first node that contains the given data
    def insert_after(self, data, insert_me):
        node = self.get(data)
        insert_me.next = node.next
        node.next = insert_me

    def delete(self, node):
        if node == self.head:
            self.head = self.head.next
            return
        n = self.head.next
        prev = self.head
        while n:
            if n == node:
                prev.next = n.next
                return
            prev = n
            n = n.next

    def print_list(self):
      node = self.head
      while node:
          print(node.data)
          node = node.next

def main():
    ll = LinkedList()
    i = 0
    j = 1
    while j <= 144:
        node = Node(j)
        ll.push(node)
        i, j = j, i + j
    ll.print_list()
    print('getting 13')
    node = ll.get(13)
    print(node.data)
    print('deleting it')
    ll.delete(node)
    ll.print_list()
    node = Node(666)
    ll.insert_after(8, node)
    ll.print_list()


if __name__ == "__main__":
    main()
