#Tree for JSON output

symbol = [' ', '!', 'Z', 'X', 'Q', '?', 'V', 'K', 'q', 'U', 'j', 'z', 'J', 'G', 'Y', 'F', 'O', 'L', 'W', '7', 'x', 'H', 'D', 'E', 'P', 'R', '6', 'B', '8', '3', '4', 'N', 'I', 'C', 'M', 'A', '9', 'S', 'T', '2', '5', 'k', '1', '0', '-', 'v', 'b', 'w', 'y', 'g', 'p', 'f', 'm', 'u', '.', 'c', 'd', 'l', 'h', 'r', 's', 'i', 'n', 'o', 'a', 't', 'e']
frequency = [277, 4102, 5610, 7578, 11659, 24305, 31053, 46580, 54221, 57488, 65856, 66423, 78706, 93212, 94297, 100751, 105700, 106984, 107195, 122008, 123577, 123632, 129632, 138443, 144239, 146448, 156932, 169474, 184476, 190886, 195228, 205409, 223312, 229363, 259474, 280937, 284542, 304971, 325462, 336999, 376926, 460788, 467697, 548277, 550907, 653370, 866156, 1015656, 1062040, 1206747, 1255579, 1296925, 1467376, 1613323, 1835383, 1960412, 2369820, 2553152, 2955858, 4137949, 4186210, 4527332, 4535545, 4729266, 5263779, 5507692, 7741842]

class Node:

	def __init__(self, val, cod, childZero, childOne):
		self.value = val
		self.code = cod
		self.child0 = childZero
		self.child1 = childOne

class Leaf:

	def __init__(self, sym, code):
		self.symbol = sym
		self.finalCode = code


firstLeaf = Leaf(symbol[0], 0)
secondLeaf = Leaf(symbol[1], 1)
nodeLeaf = [firstLeaf, secondLeaf]


freqSum = frequency[0] + frequency[1]
if freqSum <= frequency[2]:
	nodeLeaf.append(Leaf(symbol[2], 0))
	nodeNode = [Node(1, 1, symbol[0], symbol[1])]

else:
	nodeLeaf.append(Leaf(symbol[2], 1))
	nodeNode = [Node(1, 0, symbol[0], symbol[1])]


for x in range (3,len(frequency)-1):
	freqSum = freqSum + frequency[x-1]
	if freqSum <= frequency[x]:
		nodeLeaf.append(Leaf(symbol[x], 0))
		nodeNode.append(Node(x-1, 1, x-2, symbol[x-1]))

	else:
		nodeLeaf.append(Leaf(symbol[x], 1))
		nodeNode.append(Node(x-1, 0, x-2, symbol[x-1]))


codeNumbers = []
for b in nodeLeaf:
	st = str(b.finalCode)
	for c in nodeNode:
		if c.child0 == b.symbol:
			st = st + str(c.code)
			temp = c.value
		elif c.child1 == b.symbol:
			st = st + str(c.code)
			temp = c.value
		elif c.child0 == temp:
			st = st + str(c.code)
			temp = c.value

	codeNumbers.append([b.symbol + " : " + st])


for a in codeNumbers:
	print a

#for x in nodeLeaf:
#	print x.symbol
#	print x.finalCode

#for y in nodeNode:
#	print y.value
#	print y.code
#	print y.child0
#	print y.child1
