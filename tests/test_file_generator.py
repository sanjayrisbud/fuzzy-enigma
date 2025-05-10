"""
Unit tests for file_generator.py
"""
import pandas as pd
import pytest

import file_generator
from file_generator import FileGenerator
from tree import Tree


class TestFileGenerator:
    """ Unit tests for FileGenerator class. """

    def test_build_list_of_trees_from_df(self):
        """ Unit test for build_list_of_trees_from_df() """
        file_generator1 = FileGenerator(None)
        trees1 = file_generator1.build_list_of_trees_from_df()
        assert trees1 == []
        df = pd.DataFrame([1], columns=["a"])
        file_generator2 = FileGenerator(df)
        trees2 = file_generator2.build_list_of_trees_from_df()
        assert trees2 == []

    def test_build_category_tree_from_inputs(self):
        """ Unit test for build_category_tree_from_inputs() """
        df = pd.DataFrame([[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]], columns=["Base URL", "a", "b", "c"])
        file_generator1 = FileGenerator(df)
        trees = file_generator1.build_list_of_trees_from_df()
        file_generator1.build_category_tree_from_inputs(trees)
        assert isinstance(file_generator1.category_tree, Tree)

    @pytest.mark.parametrize("df, expected_result",
                             [
                                 (None, None),
                                 (pd.DataFrame([[0, 1, 2, 3]], columns=["Base URL", "a", "b", "c"]),
                                  {"label": 1, "id": 2, "link": 3, "children": []}),
                                 (pd.DataFrame([[0, 1, 2, 3], [0, 4, 5, 6]], columns=["Base URL", "a", "b", "c"]),
                                  [
                                      {"label": 1, "id": 2, "link": 3, "children": []},
                                      {"label": 4, "id": 5, "link": 6, "children": []}
                                  ]
                                  ),
                             ])
    def test_write_category_tree(self, df, expected_result):
        """ Unit test for write_category_tree() """
        file_generator1 = FileGenerator(df)
        trees = file_generator1.build_list_of_trees_from_df()
        file_generator1.build_category_tree_from_inputs(trees)
        file_generator1.write_category_tree()
        assert file_generator1.json == expected_result


def test_main():
    """ Unit test for main() """
    df = pd.DataFrame([[0, 1, 2, 3]], columns=["Base URL", "a", "b", "c"])
    _, data = file_generator.main(df)
    assert data == {"label": 1, "id": 2, "link": 3, "children": []}
