class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.childreen = []

    def make_rel(self, parent):
        parent.childreen.append(self)
        self.parent = parent

    def display(self, tabs=0):
        if self.name != "Start":
            print(tabs * "\t" + f"{self.name}:", end="\n")
            tabs += 1
        for child in self.childreen:
            child.display(tabs)

    def copy_structure(self, other, new_node=None):
        # print("I got called", self.name)
        if not new_node:
            new_node = other()

        for x in range(len(self.childreen)):
            other_child = other()
            other_child.parent = new_node
            new_node.childreen.append(other_child)
            other_child.name = self.childreen[x].name

        for x in range(len(self.childreen)):
            self.childreen[x].copy_structure(other, new_node.childreen[x])

        return new_node

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Tree:
    def __init__(self, head):
        self.head = head

    def display(self, tabs=0):
        self.head.display(0)

    def copy_structure(self, other):
        print("Start copying")
        temp = self.head.copy_structure(other)
        print("Finish copying")
        return temp

    def __repr__(self):
        if not self.head:
            return f"NOne to see"
        return self.head.name
