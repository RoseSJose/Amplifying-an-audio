import sys
import struct

def amplify(input_file, output_file, amplification):
  #opening files to read and write
  i = open(input_file, "rb")
  o = open(output_file, "wb")
  
  head = i.read(44) #read the first 44 charcters of the file
  #wav files have the first 44 characters as the header
  o.write(head) #writing the header to the output file
  
  sample = i.read(2)
  while sample:
    ip_data = struct.unpack('h', sample) #unpacking into a python object
    #h is for short size of 2
    val = ip_data[0]
    val = int(val * amplification)
    op_data = struct.pack('h', val)
    o.write(op_data)
    sample = i.read(2)
    
  i.close()
  o.close()
  
def main():
  #sys.argv contains the command line arguments given to the program
  source = sys.argv[1]
  target = sys.argv[2]
  amplification = float(sys.argv[3])
  amplify(source, target, amplification)

main()
