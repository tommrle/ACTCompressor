from sequence_tree import sequence_tree


def lz77_process_string(data):
    root = sequence_tree()
    index = 0
    while index < len(data):
        # print "+++++++++++++"
        # print data
        # print index
        # print data[index:index+3]
        startIndex = root.search(data[index:index+3], index)
        if startIndex is not False:
            newAbbreviation = "["
            newAbbreviation += str(index - startIndex)
            newAbbreviation += ","
            newAbbreviation += str(3)
            newAbbreviation += "]"
            data = data[0:index] + newAbbreviation + data[index+3:len(data)]
            index += len(newAbbreviation)
            # print "index updated to: " + str(index)
        else:
            index += 1
        # print "actual index " + str(index)
        # print "============="
    return data


def lz77_process_string_classic(data, window_size=256, min_length=3, max_length=17):
    index = 0
    compressed_data = data
    compressed_data_index = 0
    while index + min_length < len(data):
        window_start = index - window_size
        if window_start < 0:
            window_start = 0

        while window_start + min_length < index:
            if data[window_start:window_start+min_length] == data[index:index+min_length]:
                length = min_length
                while index+length < len(data) and data[window_start+length] == data[index+length] and length < max_length:
                    length += 1
                new_abbreviation = "["
                new_abbreviation += str(index-window_start)
                new_abbreviation += ","
                new_abbreviation += str(length)
                new_abbreviation += "]"
                compressed_data = compressed_data[:compressed_data_index] + new_abbreviation + compressed_data[compressed_data_index+length:]
                index += length
                compressed_data_index += len(new_abbreviation)
                break

            window_start += 1
        index += 1
        compressed_data_index += 1
    return compressed_data

def lz77_decompress(compressed_data):
    index=0
    while index < len(compressed_data):
        if compressed_data[index] == '[':
            segment_end=index
            while segment_end < len(compressed_data) and compressed_data[segment_end] != ']':
                segment_end += 1
            repeat_data = compressed_data[index+1:segment_end]
            distance = int(repeat_data.split(',')[0])
            length = int(repeat_data.split(',')[1])
            new_segment = compressed_data[(index-distance):(index-distance+length)]
            compressed_data = compressed_data[:index] + new_segment + compressed_data[segment_end+1:]
            index += length
        index += 1
    return compressed_data