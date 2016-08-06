# this encodes the string produced by the LZ77 compressor with the huffman encoding produced by Aaron

import json
from pprint import pprint




def encode(stringAfterLZ77, fileName):
    tempFile = open(fileName)
    huffTree = json.load(tempFile)
    tempFile.close()

    encoded = ""
    i = 0
    while i < len(stringAfterLZ77):
        currentChar = stringAfterLZ77[i]
        if currentChar == "[" or currentChar == "]":
            j = i
            ended = False
            i += 1
            while not ended:
                if stringAfterLZ77[i] == "]":
                    ended = True
                i += 1
            encoded += "1"+encodePair(stringAfterLZ77[j+1:i-1])
        else:
            encoded += "0"
            encoded += huffTree[currentChar]
            i += 1
    #print (encoded)
    return encoded


def encodePair(pair):
    i = 0
    while pair[i] != ",":
        i += 1
    length = int(pair[:i])
    i += 1
    dist = int(pair[i:])

    prev = 0
    bits = 0
    if length == 3:
        result = '00000'
    elif length == 4:
        result = '00001'
    elif length == 5:
        result = '00010'
    elif length == 6:
        result = '00011'
    elif length == 7:
        result = '00100'
    elif length == 8:
        result = '00101'
    elif length == 9:
        result = '00110'
    elif length == 10:
        result = '00111'
    elif length <= 12:
        result = '01000' + bin(length - 11)[2:]
        prev = 11
        bits = 1
    elif length <= 14:
        result = '01001' + bin(length - 13)[2:]
        prev = 13
        bits = 1
    elif length <= 16:
        result = '01010' + bin(length - 15)[2:]
        prev = 15
        bits = 1
    elif length <= 18:
        result = '01011' + bin(length - 17)[2:]
        prev = 17
        bits = 1
    elif length <= 22:
        result = '01100' + bin(length - 19)[2:]
        prev = 19
        bits = 2
    elif length <= 26:
        result = '01101' + bin(length - 23)[2:]
        prev = 23
        bits = 2
    elif length <= 30:
        result = '01110' + bin(length - 27)[2:]
        prev = 27
        bits = 2
    elif length <= 34:
        result = '01111' + bin(length - 31)[2:]
        prev = 31
        bits = 2
    elif length <= 42:
        result = '10000' + bin(length - 35)[2:]
        prev = 35
        bits = 3
    elif length <= 50:
        result = '10001' + bin(length - 43)[2:]
        prev = 43
        bits = 3
    elif length <= 58:
        result = '10010' + bin(length - 51)[2:]
        prev = 51
        bits = 3
    elif length <= 66:
        result = '10011' + bin(length - 59)[2:]
        prev = 59
        bits = 3
    elif length <= 82:
        result = '10100' + bin(length - 67)[2:]
        prev = 67
        bits = 4
    elif length <= 98:
        result = '10101' + bin(length - 83)[2:]
        prev = 83
        bits = 4
    elif length <= 114:
        result = '10110' + bin(length - 99)[2:]
        prev = 99
        bits = 4
    elif length <= 130:
        result = '10111' + bin(length - 115)[2:]
        prev = 115
        bits = 4
    elif length <= 162:
        result = '11000' + bin(length - 131)[2:]
        prev = 131
        bits = 5
    elif length <= 194:
        result = '11001' + bin(length - 163)[2:]
        prev = 163
        bits = 5
    elif length <= 226:
        result = '11010' + bin(length - 195)[2:]
        prev = 195
        bits = 5
    elif length <= 257:
        result = '11011' + bin(length - 227)[2:]
        prev = 227
        bits = 5
    else:
        result = '11100'

    if bits > 0:
        post = bin(length - prev)[2:]
        while len(post) < bits:
            post = '0' + post
        result += post

    prev = 0
    bits = 0
    if dist == 1:
        result += '00000'
    elif dist == 2:
        result += '00001'
    elif dist == 3:
        result += '00010'
    elif dist == 4:
        result += '00011'
    elif dist <= 6:
        result += '00100'
        prev = 5
        bits = 1
    elif dist <= 8:
        result += '00101'
        prev = 7
        bits = 2
    elif dist <= 12:
        result += '00110'
        prev = 9
        bits = 2
    elif dist <= 16:
        result += '00111'
        prev = 13
        bits = 2
    elif dist <= 24:
        result += '01000'
        prev = 17
        bits = 3
    elif dist <= 32:
        result += '01001'
        prev = 25
        bits = 3
    elif dist <= 48:
        result += '01010'
        prev = 33
        bits = 4
    elif dist <= 64:
        result += '01011'
        prev = 49
        bits = 4
    elif dist <= 96:
        result += '01100'
        prev = 65
        bits = 5
    elif dist <= 128:
        result += '01101'
        prev = 97
        bits = 5
    elif dist <= 192:
        result += '01110'
        prev = 129
        bits = 6
    elif dist <= 256:
        result += '01111'
        prev = 193
        bits = 6
    elif dist <= 384:
        result += '10000'
        prev = 257
        bits = 7
    elif dist <= 512:
        result += '10001'
        prev = 384
        bits = 7
    elif dist <= 768:
        result += '10010'
        prev = 513
        bits = 8
    elif dist <= 1024:
        result += '10011'
        prev = 169
        bits = 8
    elif dist <= 1536:
        result += '10100'
        prev = 1025
        bits = 9
    elif dist <= 2048:
        result += '10101'
        prev = 1537
        bits = 9
    elif dist <= 3072:
        result += '10110'
        prev = 2049
        bits = 10
    elif dist <= 4096:
        result += '10111'
        prev = 3073
        bits = 10
    elif dist <= 6144:
        result += '11000'
        prev = 4097
        bits = 11
    elif dist <= 8192:
        result += '11001'
        prev = 6145
        bits = 11
    elif dist <= 12288:
        result += '11010'
        prev = 8193
        bits = 12
    elif dist <= 16384:
        result += '11011'
        prev = 12289
        bits = 12
    elif dist <= 24576:
        result += '11100'
        prev = 16385
        bits = 13
    else:
        result += '11101'
        prev = 24577
        bits = 13

    if dist >= 6:
        post = bin(dist - prev)[2:]
        while len(post) < bits:
            post = '0' + post
        result += post
    return result

# print huffTree
#
# input="These are some words here and I dont really know what i should be typing. Should I try to type actual sentences and stuff? Or should I try to do whatever? The world may never know!"
# lenIn=len(input)
# lenOut=len(encode(input))
# print "\n"+str(lenIn*8)+" to "+str(lenOut)
