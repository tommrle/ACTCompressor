from lz77 import lz77_string_encode
from huffman import encode

input="hello im testing. I am just going to write a whole bunch of words here and see what happens."
print lz77_string_encode.lz77_process_string(input)
output = encode.encode(lz77_string_encode.lz77_process_string(input), "./dataImport/data.json")

print output

print str(len(input)*8)+" down to "+str(len(output))
