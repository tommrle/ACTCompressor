#Tree for JSON output

import json

#input data ***switch to excel import***
symbol = 	[' ', '!', 'Z', 'X', 'Q', '?', 'V', 'K', 'q', 'U', 'j', 'z', 'J', 
			'G', 'Y', 'F', 'O', 'L', 'W', '7', 'x', 'H', 'D', 'E', 'P', 'R', 
			'6', 'B', '8', '3', '4', 'N', 'I', 'C', 'M', 'A', '9', 'S', 'T', 
			'2', '5', 'k', '1', '0', '-', 'v', 'b', 'w', 'y', 'g', 'p', 'f', 
			'm', 'u', '.', 'c', 'd', 'l', 'h', 'r', 's', 'i', 'n', 'o', 'a', 
			't', 'e']

frequency = [277, 4102, 5610, 7578, 11659, 24305, 31053, 46580, 54221, 57488, 
			65856, 66423, 78706, 93212, 94297, 100751, 105700, 106984, 107195, 
			122008, 123577, 123632, 129632, 138443, 144239, 146448, 156932, 
			169474, 184476, 190886, 195228, 205409, 223312, 229363, 259474, 
			280937, 284542, 304971, 325462, 336999, 376926, 460788, 467697, 
			548277, 550907, 653370, 866156, 1015656, 1062040, 1206747, 
			1255579, 1296925, 1467376, 1613323, 1835383, 1960412, 2369820, 
			2553152, 2955858, 4137949, 4186210, 4527332, 4535545, 4729266, 
			5263779, 5507692, 7741842]

class SymFreq:

	def __init__(self, sym, freq, cod):
		self.symbol = sym
		self.frequency = freq
		self.code = cod
		self.children = []

	def add_child(self, child0, child1):
		self.children.append(child0)
		self.children.append(child1)

def CreateArray():

	counter = 0
	for x in symbol:
		n = SymFreq(symbol[counter], frequency[counter], 2)
		symbolFrequency.append(n)
		counter += 1

def BeginTree(leaf1, leaf2, counter):

	symbolFrequency.remove(leaf1)
	symbolFrequency.remove(leaf2)
	n = SymFreq('node' + str(counter) ,leaf1.frequency+leaf2.frequency, 2)
	n.add_child(leaf1, leaf2)
	symbolFrequency.append(n)

def CreateNode(list):

	temp = symbolFrequency[0]
	for small in symbolFrequency:
		if small.frequency < temp.frequency:
			temp = small


	if temp.symbol[0:4] == 'node':
		nodes.append(temp)
	else:
		leaves.append(temp)
	temp.code = 0
	symbolFrequency.remove(temp)


	temp2 = symbolFrequency[0]
	for small in symbolFrequency:
		if small.frequency < temp2.frequency:
			temp2 = small


	if temp2.symbol[0:4] == 'node':
		nodes.append(temp2)
	else:
		leaves.append(temp2)
	temp2.code = 1
	symbolFrequency.remove(temp2)


	n = SymFreq('node' + str(counter) , temp.frequency + temp2.frequency, 2)
	n.add_child(temp.symbol, temp2.symbol)
	symbolFrequency.append(n)

#############################################################################

#create all arrays needed to track tree
symbolFrequency = []
nodes = []
leaves = []
huffman_codes = {}

#create single array of symbols and frequencies
CreateArray()


#calculate the first two leaves of the tree
counter = 1
BeginTree(symbolFrequency[0], symbolFrequency[1], counter)
counter += 1


#calculate next smallest frequencies and assigns leaves and nodes code values
while len(symbolFrequency) > 1:
	CreateNode(symbolFrequency)
	counter += 1


#build the Huffman code list for export to JSON
temp = nodes[0].symbol
for leaf in leaves:
	huff_code = str(leaf.code)
	for node in nodes:
		if node.children[0] == leaf.symbol:
			huff_code = str(node.code) + huff_code
			temp = node.symbol
		elif node.children[1] == leaf.symbol:
			huff_code = str(node.code) + huff_code
			temp = node.symbol
		elif node.children[0] == temp:
			huff_code = str(node.code) + huff_code
			temp = node.symbol
		elif node.children[1] == temp:
			huff_code = str(node.code) + huff_code
			temp = node.symbol

	huffman_codes[leaf.symbol] = huff_code

##uncomment to see output
#print json.dumps(huffman_codes, sort_keys = True, indent = 4)

#write key for Huffman codes to JSON file
with open('data.json', 'w') as outfile:
	json.dump(huffman_codes, outfile, sort_keys = True)
