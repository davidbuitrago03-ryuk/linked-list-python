class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def __contains__(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next

    def prepend(self, data):
        new_node = Node(data=data, next=self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def append(self, data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def find(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr

    def remove(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if curr is None:
            return
        if prev is None:
            self.head = curr.next
        else:
            prev.next = curr.next
            curr.next = None
        if curr == self.tail:
            self.tail = prev

    def reverse(self):
        curr = self.head
        prev_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head, self.tail = prev_node, self.head

    def reverse_recursive(self, node=None):
        if node is None:
            node = self.head
        if node is None or node.next is None:
            self.head = node
            return node
        rest = self.reverse_recursive(node.next)
        node.next.next = node
        node.next = None
        self.tail = self.head
        return rest


if __name__ == '__main__':
    ll = LinkedList()

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    print("Lista inicial:      ", ll)
    print("Longitud:           ", len(ll))
    print("Contiene el 2:      ", 2 in ll)
    print("Buscar el 3:        ", ll.find(3))

    ll.remove(2)
    print("Tras eliminar el 2: ", ll)

    ll.reverse()
    print("Invertida:          ", ll)

    ll.reverse_recursive()
    print("Invertida de nuevo: ", ll)

    print("Recorrido con for:  ", end=" ")
    for valor in ll:
        print(valor, end=" ")
    print()