import sys

from tree import Tree, Node
from settings import *
from objects import ImgNode


class Parser:
    def __init__(self):
        self.html_tree = Tree(Node("Start"))
        self.tstack = ["<", ">"]
        self.atb_buffer = []
        self.mod_stack = []

    def is_tag_valid(self):
        if len(self.tstack) > 2:
            print("you forget to close '<' in your html")
            return False

        print("String is valid")
        return True

    def check_tag(self, ch):
        if ch == "<":
            self.tstack.append(ch)
        elif ch == ">":
            if not self.tstack:
                print("the is '>' without a starting '>' ")
                return False
            self.tstack.pop()

    def get_element(self, ch):
        if ch == "<":
            self.atb_buffer.clear()
        elif ch == ">":
            str_buffer = ""
            for c in self.atb_buffer:
                str_buffer += c
            if not str_buffer in closed_tags:
                self.mod_stack.append(str_buffer.split()[0])
            else:
                self.mod_stack.append(str_buffer.split()[0])
                self.mod_stack.append(f"/{str_buffer.split()[0]}")
        else:
            self.atb_buffer.append(ch)

    def parse_html(self):
        if not self.mod_stack:
            print("there is nothing to do.")
            return True

        ele_buffer = [self.html_tree.head]
        self.mod_stack.append("/Start")

        for element in self.mod_stack:
            if element[0] != "/":
                new_node = Node(element)
                ele_buffer.append(new_node)
            else:
                if ele_buffer[-1].name != element[1:]:
                    if element[1:] == "Start":
                        print("Error: html elements are not closed")
                        return False
                    print("Error: html elements are not open")
                    return False
                else:
                    print(ele_buffer)
                    node = ele_buffer.pop()
                    if not ele_buffer:
                        continue
                    node.make_rel(ele_buffer[-1])

        if ele_buffer:
            print("Error: html element not closed")
            return False
        return True

    def parse(self, html):
        for ch in html:
            self.check_tag(ch)
            self.get_element(ch)

        self.is_tag_valid()
        print(self.mod_stack)
        self.parse_html()

    def get_html(self, path):
        with open(path, "r") as f:
            text = f.read()
        return text


if __name__ == "__main__":
    myparser = Parser()
    myparser.parse(myparser.get_html("table.html"))
    myparser.html_tree.display()
    new_copy = myparser.html_tree.copy_structure(ImgNode)
    new_copy.display()
