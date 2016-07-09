# this encodes the string produced by the LZ77 compressor with the huffman encoding produced by Aaron

import json
from pprint import pprint

tempFile = open("fileNameHere")
huffTree = json.load(tempFile)
tempFile.close()
pprint(huffTree)


def stuff(thing):
    encoded = ""
    inPair = False
    i = 0
    while i < len(thing):
        currentChar = thing[i]
        if currentChar == "[" or currentChar == "]":
            j = i
            ended = False
            i += 1
            while not ended:
                if thing[i] == "]":
                    ended = True
                i += 1
            encodePair(thing[j+1:i-1])
        else:
            encoded += huffTree[currentChar]
            i += 1
    print (encoded)


def encodePair(pair):
    i = 0
    while pair[i] != ",":
        i += 1
    length = int(pair[:i])
    i += 1
    dist = int(pair[i:])

    if length == 3:
        result=bin(257)[2:]
    elif length == 4:
        result=bin(258)[2:]
    elif length == 5:
        result=bin(259)[2:]
    elif length == 6:
        result=bin(260)[2:]
    elif length == 7:
        result=bin(261)[2:]
    elif length == 8:
        result=bin(262)[2:]
    elif length == 9:
        result=bin(263)[2:]
    elif length == 10:
        result=bin(264)[2:]
    elif length <= 12:
        result=bin(265)[2:] + bin(11-length)[2:0]
    elif length <= 14:
        result=bin(266)[2:] + bin(13-length)[2:0]
    elif length <= 16:
        result=bin(267)[2:] + bin(15-length)[2:0]
    elif length <= 18:
        result=bin(268)[2:] + bin(17-length)[2:0]
    elif length <= 22:
        result=bin(269)[2:]
    elif length <= 26:
        result=bin(270)[2:]
    elif length <= 30:
        result=bin(271)[2:]
    elif length <= 34:
        result=bin(272)[2:]
    elif length <= 42:
        result=bin(273)[2:]
    elif length <= 50:
        result=bin(274)[2:]
    elif length <= 58:
        result=bin(275)[2:]
    elif length <= 66:
        result=bin(276)[2:]
    elif length <= 82:
        result=bin(277)[2:]
    elif length <= 98:
        result=bin(278)[2:]
    elif length <= 114:
        result=bin(279)[2:]
    elif length <= 130:
        result=bin(280)[2:]
    elif length <= 162:
        result=bin(281)[2:]
    elif length <= 194:
        result=bin(282)[2:]
    elif length <= 226:
        result=bin(283)[2:]
    elif length <= 257:
        result=bin(284)[2:]
    else:
        result=bin(285)[2:]
    print (result)


stuff("hi there [3,1]")
print(bin(256)[2:])
print(bin(256)[2:] + bin(18-18)[2:])
