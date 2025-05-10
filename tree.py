"""
Classes to abstract a tree and a tree node.
"""


class Node:
    """ This class abstracts a tree node. """

    def __init__(self, name, cat_id, link):
        self.name = name
        self.cat_id = cat_id
        self.link = link
        self.children = []

    def add_child(self, child_node):
        """ Add a link to a child node. """
        self.children.append(child_node)

    def get_child_with_same_cat(self, other):
        """ Return the child node with the same id as the given node. """
        for node in self.children:
            if node.cat_id == other.cat_id:
                return node
        return None

    def to_dict(self):
        """ Return a dictionary representation of this node. """
        return {
            "label": self.name,
            "id": self.cat_id,
            "link": self.link,
            "children": [node.to_dict() for node in self.children],
        }

    def __str__(self):
        return f"{self.name}->{[str(child) for child in self.children]}"


class Tree:
    """ Abstraction of tree data structure. """

    def __init__(self):
        self.root = None

    def from_dict(self, row, column_names, levels):
        """ Create a tree from the supplied dictionary. """
        self.root = current = Node("Base", "0", row["Base URL"])
        for i in range(levels):
            cat_name = row.get(column_names[i * 3 + 1])
            cat_id = row.get(column_names[i * 3 + 2])
            cat_url = row.get(column_names[i * 3 + 3])
            if cat_id != cat_id:  # if cat_id is Nan, this will be True!
                break
            new_node = Node(cat_name, cat_id, cat_url)
            current.add_child(new_node)
            current = new_node
        return self.root

    def merge(self, other):
        """ Add the supplied tree's unique nodes to this tree. """
        if self.root is None:
            self.root = other
            return
        current = self.root
        while len(other.children) != 0:
            other = other.children[0]
            rover = current.get_child_with_same_cat(other)
            if rover is None:
                # "other" is a Node for a new category
                # hence need to append it as a child of "current"
                current.add_child(other)
                break
            current = rover

    def to_dict(self):
        """ Return a dictionary representation of this tree. """
        return self.root.to_dict()
