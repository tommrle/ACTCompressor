from sequence_tree import Tree

three_character_sequences = {}
root = Tree()

def lz77_process_string(data):
    index = 0
    while index < len(data):
        print "+++++++++++++"
        print data
        print index
        print data[index:index+3]
        startIndex = root.search(data[index:index+3], index)
        if startIndex is not False:
            newAbbreviation = "["
            newAbbreviation += str(index - startIndex)
            newAbbreviation += ","
            newAbbreviation += str(3)
            newAbbreviation += "]"
            data = data[0:index] + newAbbreviation + data[index+3:len(data)]
            index += len(newAbbreviation)
            print "index updated to: " + str(index)
        else:
            index += 1
        print "actual index " + str(index) 
        print "============="
    return data

print lz77_process_string("hello hello hello");
