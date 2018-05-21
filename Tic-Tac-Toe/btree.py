from btnode import BTNode
from board import Board
import random
import copy


class BTree():
    """constructor of the BTree."""
    def __init__(self, turn):
        self.root = None
        self.turn = turn
        self.left_sum = 0
        self.right_sum = 0

    def clear(self):
        """clear the tree"""
        self.root = None

    def isEmpty(self):
        """check if tree is empty"""
        if self.root == None:
            return True
        return False

    def add_left(self, value):
        self.root.left = BTNode(value)

    def add_right(self, value):
        self.root.right = BTNode(value)

    def set_initial_root(self, value):
        self.root = BTNode(value)

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()

        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.value)
                recurse(node.right)

        recurse(self.root)
        return lyst

    def generate_coord(self):
        return random.choice(self.root.value.availible_cells)

    @staticmethod
    def new_generation(rootnode):
        def generate_coord(availible_cells):
            return random.choice(availible_cells)

        if not rootnode.value.check_winner():

            board1 = copy.deepcopy(rootnode.value)
            if rootnode.value._lastMove[0] == "X":
                turn = "O"
            else:
                turn = "X"

            coord1 = generate_coord(rootnode.value.availible_cells)
            board1.put(turn, coord1)


            # Create board 2 with coord option 2
            board2 = copy.deepcopy(rootnode.value)

            coord2 = generate_coord(rootnode.value.availible_cells)
            while coord2 == coord1:
                coord2 = generate_coord(rootnode.value.availible_cells)
            board2.put(turn, coord2)

            # place those boards as right and left children of the root
            rootnode.left = BTNode(board1)

            rootnode.right = BTNode(board2)

    def grow_tree(self):
        def add_children(node):
            if not node.value.check_winner:
                new_generation(node.left)
                new_generation(node.right)

                add_children(node.left)
                add_children(node.right)
        add_children(self.root)


    def best_move(self):
        """RETURNS BEST COORD FROW TWO GIVEN"""

        def recursion(node, turn):
            if node:
                if node.value.check_winner() == "DRAW":
                    return 0
                elif node.value.check_winner() == turn:
                    return 1
                elif node.value.check_winner() == None:
                    return recursion(node.left, turn) + recursion(node.right, turn)
                else:
                    return -1
            else:
                return 0
        left = self.root.left.value._lastMove[1]
        right = self.root.right.value._lastMove[1]

        self.grow_tree()

        if recursion(self.root.left, self.turn) > recursion(self.root.right, self.turn):
            return left
        else:
            return right
