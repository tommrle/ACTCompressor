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

    def toString(self):
        if (self.is_a_leaf_node):
            return self.symbol+": "+str(self.code)
        leftChild = self.left_child.toString()
        rightChild = self.right_child.toString()
        return "\n{"+self.symbol+": "+leftChild+", "+rightChild+"}"

    def __str__(self, level=0):
        ret = "\t"*level+self.symbol+"\n"
        for child in [self.left_child, self.right_child]:
            if child is not None:
                ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'
