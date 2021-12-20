class Node:
  

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<Node data: %s>" % self.data



class LinkedList:
 

    def __init__(self):
        self.head = None
        # Maintaining a count attribute allows for len() to be implemented in
        # constant time
        self.__count = 0

    def is_empty(self):
        return self.head is None

    def __len__(self):
           
        return self.__count

    def add(self, data):
        new_node  = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return "->".join(nodes)

    def insert (self, data, index):
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

            



l = LinkedList()
l.add(10)
l.add(11)
l.add(3)
l.insert(11, 2)

print(l)