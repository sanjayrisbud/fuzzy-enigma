"""
Unit tests for tree.py
"""
from tree import Node, Tree


class TestNode:
    """ Unit tests for Node class. """

    def test_add_child(self):
        """ Unit test for add_child() """
        node = Node("a", "b", "c")
        node.add_child(Node("x", "y", "z"))
        assert node.children[0].cat_id == "y"

    def test_get_child_with_same_cat(self):
        """ Unit test for get_child_with_same_cat() """
        node = Node("a", "b", "c")
        child1 = Node("d", "e", "f")
        child2 = Node("g", "h", "i")
        node.add_child(child1)
        node.add_child(child2)
        other = Node("g", "h", "i")
        assert node.get_child_with_same_cat(other) == child2

    def test_to_dict(self):
        """ Unit test for to_dict() """
        node = Node("a", "b", "c")
        assert node.to_dict() == {"label": "a", "id": "b", "link": "c", "children": []}

    def test_str(self):
        """ Unit test for __str__() """
        node = Node("a", "b", "c")
        assert str(node) == "a->[]"


class TestTree:
    """ Unit tests for Tree class. """

    def test_from_dict(self):
        """ Unit test for from_dict() """
        row = {"Base URL": "base", "Level 1 - Name": "a", "Level 1 - ID": "b", "Level 1 - URL": "c"}
        column_names = ["Base URL", "Level 1 - Name", "Level 1 - ID", "Level 1 - URL"]
        tree1 = Tree()
        tree1.from_dict(row, column_names, levels=1)
        assert len(tree1.root.children) == 1
        tree2 = Tree()
        tree2.from_dict(row, column_names, levels=0)
        assert len(tree2.root.children) == 0
    
    def test_to_dict(self):
        """ Unit test for to_dict() """
        row = {"Base URL": "base", "Level 1 - Name": "a", "Level 1 - ID": "b", "Level 1 - URL": "c"}
        column_names = ["Base URL", "Level 1 - Name", "Level 1 - ID", "Level 1 - URL"]
        tree = Tree()
        tree.from_dict(row, column_names, levels=1)
        expected = {"label": "Base", "id": "0", "link": "base", "children": [
            {"label": "a", "id": "b", "link": "c", "children": []}]}
        assert tree.to_dict() == expected

    def test_merge(self):
        """ Unit test for merge() """
        row1 = {"Base URL": "base", "Level 1 - Name": "a", "Level 1 - ID": "b", "Level 1 - URL": "c"}
        row2 = {"Base URL": "base", "Level 1 - Name": "x", "Level 1 - ID": "y", "Level 1 - URL": "z"}
        column_names = ["Base URL", "Level 1 - Name", "Level 1 - ID", "Level 1 - URL"]
        tree1 = Tree()
        tree1.from_dict(row1, column_names, levels=1)
        tree2 = Tree()
        tree2.from_dict(row2, column_names, levels=1)
        tree1.merge(tree2.root)
        assert len(tree1.root.children) == 2
        assert len(tree2.root.children) == 1
