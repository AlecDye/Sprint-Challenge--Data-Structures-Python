class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    # ideal solution uses recursion and not a loop
    def reverse_list(self, node, prev):
        # While loop, doesn't pass test anyway
        # current = self.head
        # prev = None
        # while current:
        #     next_pointer = current.next_node
        #     current.next_node = prev
        #     prev = current
        #     current = next_pointer
        # self.head = prev

        # not a loop but acts like one
        if node is not None:
            # current node we are visiting
            current = node.next_node
            # redirect pointer to provided prev value
            node.next_node = prev
            # recursion (not a loop)
            self.reverse_list(current, node)
        # final node condition
        else:
            self.head = prev

