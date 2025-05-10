"""
    This module contains the main class for the assignment solution.
"""
import logging

from tree import Tree


class FileGenerator:
    """ Main class for assignment solution. """

    def __init__(self, df):
        self.input_df = df
        self.category_tree = None
        self.messages = []
        self.json = None

    def build_list_of_trees_from_df(self):
        """ Build a list of trees from the dataframe representing the input file. """
        if self.input_df is None:
            return []

        trees = []
        column_names = list(self.input_df.columns)
        levels = (len(column_names) - 1) / 3  # 1 column for base url, 3 columns per level
        if (levels == 0) or (levels % 1 != 0):  # levels has to be integer > 0
            message = "Sorry, incorrect number of columns in input file."
            logging.error(message)
            self.messages.append(message)
            return []

        for row in self.input_df.to_dict("records"):
            tree_from_row = Tree().from_dict(row, column_names, int(levels))
            trees.append(tree_from_row)
        return trees

    def build_category_tree_from_inputs(self, subtrees):
        """ Build the category tree from the list of category sub-trees. """
        self.category_tree = Tree()
        for subtree in subtrees:
            self.category_tree.merge(subtree)

    def write_category_tree(self):
        """ Write out the category tree to json file. """
        if not self.category_tree.root:
            message = "Sorry, no categories file to generate, please check your input file."
            logging.error(message)
            self.messages.append(message)
            return
        content = self.category_tree.to_dict()["children"]

        # if there is a single category 1 in the dictionary,
        # write out the JSON as one dict instead of a list of dicts
        if len(content) == 1:
            content = content[0]

        self.json = content


def main(df):
    file_generator = FileGenerator(df)
    trees_from_input = file_generator.build_list_of_trees_from_df()
    file_generator.build_category_tree_from_inputs(trees_from_input)
    file_generator.write_category_tree()
    return file_generator.messages, file_generator.json
