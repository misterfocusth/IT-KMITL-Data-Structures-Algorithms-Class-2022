"""Singly Linked List"""
"""IT KMITL - 06066301 Data Structure and Algorithms (Lab)"""


class DataNode:
    def __init__(self, name=""):
        self.name = name
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        pointer = self.head
        result = []
        if (self.count == 0):
            return print("This is an empty list.")
        while pointer != None:
            result.append(pointer.name)
            pointer = pointer.next
        print("Traverse: " + " -> ".join(result))

    def insertFront(self, data):
        new_node = DataNode(data)
        if (self.count == 0):
            self.head = new_node
            self.count += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.count += 1

    def insertLast(self, data):
        new_node = DataNode(data)
        if (self.count == 0):
            self.head = new_node
            self.count += 1
        else:
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = new_node
            self.count += 1

    def insertBefore(self, target, data):
        new_node = DataNode(data)
        if (self.count == 0):
            self.head = new_node
            self.count += 1
        elif self.head.name == target:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node, current_node = None, self.head
            while current_node != None:
                if (current_node.name == target):
                    break
                prev_node = current_node
                current_node = current_node.next
            else:
                return print("Cannot insert, {} does not exist.".format(target))
            prev_node.next = new_node
            new_node.next = current_node
            self.count += 1

    def delete(self, target):
        prev_node, current_node = None, self.head
        while current_node != None:
            if (current_node.name == target):
                break
            prev_node = current_node
            current_node = current_node.next
        else:
            return print("Cannot delete, {} does not exist.".format(target))
        prev_node.next = current_node.next
        current_node.next = None
        self.count -= 1


def main():
    mylist = SinglyLinkedList()
    mylist.insertFront("Dog")
    mylist.insertLast("Cat")
    mylist.insertBefore("Cat", "Bird")
    mylist.traverse()
    mylist.insertBefore("Dog", "Fish")
    mylist.delete("Cat")
    mylist.traverse()
    mylist.insertBefore("Ant", "Duck")
    mylist.traverse()


main()
