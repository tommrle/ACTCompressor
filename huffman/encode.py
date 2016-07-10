# this encodes the string produced by the LZ77 compressor with the huffman encoding produced by Aaron

import json
from pprint import pprint

tempFile = open("fileNameHere.json.json")
huffTree = json.load(tempFile)
tempFile.close()
pprint(huffTree)


def stuff(thing):
    encoded = ""
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
    print(length)

    if length == 3:
        result = bin(257)[2:]
    elif length == 4:
        result = bin(258)[2:]
    elif length == 5:
        result = bin(259)[2:]
    elif length == 6:
        result = bin(260)[2:]
    elif length == 7:
        result = bin(261)[2:]
    elif length == 8:
        result = bin(262)[2:]
    elif length == 9:
        result = bin(263)[2:]
    elif length == 10:
        result = bin(264)[2:]
    elif length <= 12:
        result = bin(265)[2:] + bin(length - 11)[2:]
    elif length <= 14:
        result = bin(266)[2:] + bin(length - 13)[2:]
    elif length <= 16:
        result = bin(267)[2:] + bin(length - 15)[2:]
    elif length <= 18:
        result = bin(268)[2:] + bin(length - 17)[2:]
    elif length <= 22:
        result = bin(269)[2:] + bin(length - 19)[2:]
    elif length <= 26:
        result = bin(270)[2:] + bin(length - 23)[2:]
    elif length <= 30:
        result = bin(271)[2:] + bin(length - 27)[2:]
    elif length <= 34:
        result = bin(272)[2:] + bin(length - 31)[2:]
    elif length <= 42:
        result = bin(273)[2:] + bin(length - 35)[2:]
    elif length <= 50:
        result = bin(274)[2:] + bin(length - 43)[2:]
    elif length <= 58:
        result = bin(275)[2:] + bin(length - 51)[2:]
    elif length <= 66:
        result = bin(276)[2:] + bin(length - 59)[2:]
    elif length <= 82:
        result = bin(277)[2:] + bin(length - 67)[2:]
    elif length <= 98:
        result = bin(278)[2:] + bin(length - 83)[2:]
    elif length <= 114:
        result = bin(279)[2:] + bin(length - 99)[2:]
    elif length <= 130:
        result = bin(280)[2:] + bin(length - 115)[2:]
    elif length <= 162:
        result = bin(281)[2:] + bin(length - 131)[2:]
    elif length <= 194:
        result = bin(282)[2:] + bin(length - 163)[2:]
    elif length <= 226:
        result = bin(283)[2:] + bin(length - 195)[2:]
    elif length <= 257:
        result = bin(284)[2:] + bin(length - 227)[2:]
    else:
        result = bin(285)[2:]

    print (result)

    if dist == 1:
        result += bin(257)[2:]
    elif dist == 2:
        result += bin(258)[2:]
    elif dist == 3:
        result += bin(259)[2:]
    elif dist == 4:
        result += bin(260)[2:]
    elif dist <= 6:
        result += bin(261)[2:] + bin(dist - 5)[2:]
    elif dist <= 8:
        result += bin(262)[2:] + bin(dist - 7)[2:]
    elif dist <= 12:
        result += bin(263)[2:] + bin(dist - 9)[2:]
    elif dist <= 16:
        result += bin(264)[2:] + bin(dist - 13)[2:]
    elif dist <= 24:
        result += bin(265)[2:] + bin(dist - 17)[2:]
    elif dist <= 32:
        result += bin(266)[2:] + bin(dist - 13)[2:]
    elif dist <= 48:
        result += bin(267)[2:] + bin(dist - 15)[2:]
    elif dist <= 64:
        result += bin(268)[2:] + bin(dist - 17)[2:]
    elif dist <= 96:
        result += bin(269)[2:] + bin(dist - 19)[2:]
    elif dist <= 128:
        result += bin(270)[2:] + bin(dist - 23)[2:]
    elif dist <= 192:
        result += bin(271)[2:] + bin(dist - 27)[2:]
    elif dist <= 256:
        result += bin(272)[2:] + bin(dist - 31)[2:]
    elif dist <= 384:
        result += bin(273)[2:] + bin(dist - 35)[2:]
    elif dist <= 512:
        result += bin(274)[2:] + bin(dist - 43)[2:]
    elif dist <= 768:
        result += bin(275)[2:] + bin(dist - 51)[2:]
    elif dist <= 1024:
        result += bin(276)[2:] + bin(dist - 59)[2:]
    elif dist <= 1536:
        result += bin(277)[2:] + bin(dist - 67)[2:]
    elif dist <= 2048:
        result += bin(278)[2:] + bin(dist - 83)[2:]
    elif dist <= 3072:
        result += bin(279)[2:] + bin(dist - 99)[2:]
    elif dist <= 4096:
        result += bin(280)[2:] + bin(dist - 115)[2:]
    elif dist <= 6144:
        result += bin(281)[2:] + bin(dist - 131)[2:]
    elif dist <= 8192:
        result += bin(282)[2:] + bin(dist - 163)[2:]
    elif dist <= 12288:
        result += bin(283)[2:] + bin(dist - 195)[2:]
    elif dist <= 16384:
        result += bin(284)[2:] + bin(dist - 227)[2:]
    elif dist <= 24576:
        result += bin(284)[2:] + bin(dist - 227)[2:]
    else:
        result += bin(285)[2:]


stuff("hi there [14,1]")
