import base64
import sys

def main():

    key_sizes = {}

    #decode input file and place them in an array. Each entry into the array is a decoded input line
    input_file = open("question_6_input.txt")
    decoded_lines = []
    for line in input_file:
        decoded_lines.append(base64.b64decode(line))
    input_file.close()

    #take first two decoded lines
    decoded_line = b''.join(decoded_lines[:2])
    
    #print(len(decoded_lines))

    smallest_edit_distance =  sys.maxsize
    #find the potential key size from 2 - 40
    for key_size in range(2,41):
        first_key_size_worth_of_bytes = bytearray()
        second_key_size_worth_of_bytes = bytearray()
        for i in range(0, key_size):
            first_key_size_worth_of_bytes.append(decoded_line[i])
            second_key_size_worth_of_bytes.append(decoded_line[i+key_size])
        normalized_edit_distance = get_edit_distance(first_key_size_worth_of_bytes,second_key_size_worth_of_bytes) / key_size
        key_sizes[key_size] = normalized_edit_distance

   
    #take the three keys with the lowest edit_distance
    potential_key_sizes = [x[0] for x in sorted(key_sizes.items(), key=lambda x:x[1])[:3]]
   
    #break the ciphertext into blocks of narrowed_down_key_lengths
    potential_key_size_1 = potential_key_sizes[0]
    potential_key_size_2 = potential_key_sizes[1]
    potential_key_size_3 = potential_key_sizes[2]
    key_1_ciphertext_blocks = split_ciphertext_by_key_length(decoded_lines, potential_key_size_1)
    key_2_ciphertext_blocks = split_ciphertext_by_key_length(decoded_lines, potential_key_size_2)
    key_3_ciphertext_blocks = split_ciphertext_by_key_length(decoded_lines, potential_key_size_3)
    
    #print(len(key_1_ciphertext_blocks))
    #print("key_size: {} ciphertext_blocks: {}"  .format(potential_key_size_1, key_1_ciphertext_blocks[:10]))
    # print("key_size: {} ciphertext_blocks: {}"  .format(potential_key_size_2, key_2_ciphertext_blocks[:3]))
    # print("key_size: {} ciphertext_blocks: {}"  .format(potential_key_size_3, key_3_ciphertext_blocks[:3]))
   
    #transpose key_#_ciphertext_blocks *****fill in missing comment lol*****
    key_1_ciphertext_blocks_transpose = transpose_block(key_1_ciphertext_blocks, potential_key_size_1)
    key_2_ciphertext_blocks_transpose = transpose_block(key_2_ciphertext_blocks, potential_key_size_2)
    key_3_ciphertext_blocks_transpose = transpose_block(key_3_ciphertext_blocks, potential_key_size_3)


    #key size = 5
    key_1_character_frequency_table = {
        "0" :{
            "character" : "",
            "frequency" : 0
        },
        "1" :{
            "character" : "",
            "frequency" : 0
        },
        "2" :{
            "character" : "",
            "frequency" : 0
        },
        "3" :{
            "character" : "",
            "frequency" : 0
        },
        "4" :{
            "character" : "",
            "frequency" : 0
        }
    }
    
    #XOR the transposed blocks
    block_number = 0
    for ciphertext_block in key_1_ciphertext_blocks_transpose:
        for key in range(0,256):
            keystream = bytes([key]) * len(ciphertext_block)
            xor_block_and_populate_frequency_table(ciphertext_block, keystream, key_1_character_frequency_table, block_number)
        block_number += 1
    #print(key_1_character_frequency_table)

    #key size = 3
    key_2_character_frequency_table = {
        "0" :{
            "character" : "",
            "frequency" : 0
        },
        "1" :{
            "character" : "",
            "frequency" : 0
        },
        "2" :{
            "character" : "",
            "frequency" : 0
        }
    }

    block_number = 0
    for ciphertext_block in key_2_ciphertext_blocks_transpose:
        for key in range(0,256):
            keystream = bytes([key]) * len(ciphertext_block)
            xor_block_and_populate_frequency_table(ciphertext_block, keystream, key_2_character_frequency_table, block_number)
        block_number += 1
    #print(key_2_character_frequency_table)

    #key size = 2
    key_3_character_frequency_table = {
        "0" :{
            "character" : "",
            "frequency" : 0
        },
        "1" :{
            "character" : "",
            "frequency" : 0
        }
    }

    block_number = 0
    for ciphertext_block in key_3_ciphertext_blocks_transpose:
        for key in range(0,256):
            keystream = bytes([key]) * len(ciphertext_block)
            xor_block_and_populate_frequency_table(ciphertext_block, keystream, key_3_character_frequency_table, block_number)
        block_number += 1
    #print(key_3_character_frequency_table)





#TODO: something is wrong here. I can't tell 
def xor_block_and_populate_frequency_table(block, keystream, frequency_table, block_number):

    
    array = [0] * 256
    for x, y in zip(block, keystream):
        result = x ^ y
        array[result] += 1
    
    max_value = max(array)
    frequency_table[str(block_number)]["character"] = str(chr(array.index(max_value)))
    frequency_table[str(block_number)]["frequency"] = max_value

#TODO: this might be causing issues       
def transpose_block(ciphertext_blocks, key_size):
    
    ciphertext_blocks_transpose = [[]] * key_size

    for i in range(0,len(ciphertext_blocks)):
        ciphertext_block = ciphertext_blocks[i]
        for j in range(0, len(ciphertext_block)):
            if len(ciphertext_blocks_transpose[j]) == 0:
                ciphertext_blocks_transpose[j] = bytearray()
                ciphertext_blocks_transpose[j].append(ciphertext_block[j])
            else:
                ciphertext_blocks_transpose[j].append(ciphertext_block[j])
    print(len(ciphertext_blocks_transpose[1]))
    return ciphertext_blocks_transpose

def split_ciphertext_by_key_length(decoded_lines, key_length):

    ciphertext_blocks = []
    ciphertext_block = bytearray()
    
    remaining_bytes_to_take = key_length
    

    for line in decoded_lines:
        for byte in line:
            if remaining_bytes_to_take == 0:
                ciphertext_blocks.append(ciphertext_block)
                ciphertext_block = bytearray()
                ciphertext_block.append(byte)
                remaining_bytes_to_take = key_length - 1
            else:
                ciphertext_block.append(byte)
                remaining_bytes_to_take -= 1
    
    ciphertext_blocks.append(ciphertext_block)
    return ciphertext_blocks 
    

def get_edit_distance(a, b):

    distance = 0
    
    for x, y in zip(a,b):
        while(x!=0 or y!=0):
            if ((x & 1) ^ (y & 1)):
                distance += 1
            x = x >> 1
            y = y >> 1

    return distance

if __name__ == "__main__":
    main()