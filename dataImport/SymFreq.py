class SymFreqNode:

    def __init__(self, sym, freq, left_child=None, right_child=None, cod=None):
        self.symbol = sym
        self.frequency = freq
        self.code = cod
        self.children = []
        self.left_child = left_child
        self.right_child = right_child
        self.is_a_leaf_node = False
        self.depth = 0
