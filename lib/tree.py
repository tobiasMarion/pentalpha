class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

def writeTreeToFile(node, file, level=0):
    tabs = '    ' * level
    file.write(f'{tabs}{node.value}\n')

    for child in node.children:
        writeTreeToFile(child, file, level + 1)