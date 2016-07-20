#Tree for JSON output

import json
from SymFreq import SymFreqNode

#input data ***switch to excel import***
symbol = [' ', '!', 'Z', 'X', 'Q', '?', 'V', 'K', 'q', 'U', 'j', 'z', 'J',
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



def createArrayOfLeafNodesFromSymbolsAndFrequencies():
    symArr = []
    for index in range(0,len(symbol)):
        n = SymFreqNode(symbol[index], frequency[index])
        n.is_a_leaf_node = True
        symArr.append(n)
    return symArr

def BeginTree(leaf1, leaf2):
    symbolFrequencyList.remove(leaf1)
    symbolFrequencyList.remove(leaf2)
    n = SymFreqNode('node1',leaf1.frequency+leaf2.frequency);
    n.add_child(leaf1, leaf2)
    symbolFrequencyList.append(n)

def getSymbolWithLowestFrequencyAndRemove(list):
    # temp = list[0]
    # for small in list:
    #     if small.frequency < temp.frequency:
    #         temp = small
    # list.remove(temp)
    # return temp
    list.sort(key=lambda sym_freq_node: sym_freq_node.depth)
    temp = list[0]
    list.remove(temp)
    return temp

def CreateNextNode(list):
    lowest_frequency_symbol = getSymbolWithLowestFrequencyAndRemove(list)

    if lowest_frequency_symbol.is_a_leaf_node:
        leaves.append(lowest_frequency_symbol)
    else:
        nodes.append(lowest_frequency_symbol)

    lowest_frequency_symbol.code = 0

    second_lowest_frequency_symbol = getSymbolWithLowestFrequencyAndRemove(list)

    if second_lowest_frequency_symbol.is_a_leaf_node:
        leaves.append(second_lowest_frequency_symbol)
    else:
        nodes.append(second_lowest_frequency_symbol)

    second_lowest_frequency_symbol.code = 1

    #TODO: give tempNode a better name
    tempNode = SymFreqNode('node' + str(counter), lowest_frequency_symbol.frequency + second_lowest_frequency_symbol.frequency)
    tempNode.depth = max(lowest_frequency_symbol.depth, second_lowest_frequency_symbol.depth) + 1
    tempNode.left_child = lowest_frequency_symbol
    tempNode.right_child = second_lowest_frequency_symbol
    symbolFrequencyList.append(tempNode)

#############################################################################

#create all arrays needed to track tree
#symbolFrequencyList = []

nodes = []
leaves = []
huffman_codes = {}

#create single array of symbols and frequencies
symbolFrequencyList = createArrayOfLeafNodesFromSymbolsAndFrequencies()

#calculate the first two leaves of the tree
BeginTree(symbolFrequencyList[0], symbolFrequencyList[1])

#calculate next smallest frequencies and assigns leaves and nodes code values
counter = 2
while len(symbolFrequencyList) > 1:
    CreateNextNode(symbolFrequencyList)
    counter += 1


#build the Huffman code list for export to JSON
temp = nodes[0].symbol
for leaf in leaves:
    huff_code = str(leaf.code)
    # for node in nodes:
        # if node.children[0] == leaf.symbol:
        #     huff_code = str(node.code) + huff_code
        #     temp = node.symbol
        # elif node.children[1] == leaf.symbol:
        #     huff_code = str(node.code) + huff_code
        #     temp = node.symbol
        # elif node.children[0] == temp:
        #     huff_code = str(node.code) + huff_code
        #     temp = node.symbol
        # elif node.children[1] == temp:
        #     huff_code = str(node.code) + huff_code
        #     temp = node.symbol

    huffman_codes[leaf.symbol] = huff_code

##uncomment to see output
print json.dumps(huffman_codes, sort_keys = True, indent = 4)

#write key for Huffman codes to JSON file
with open('data.json', 'w') as outfile:
    json.dump(huffman_codes, outfile, sort_keys = True)
