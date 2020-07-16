def main():

    frequency_table = {
        "a" : 8.497,
        "b" : 1.492,
        "c" : 2.202,
        "d" : 4.253,
        "e" : 11.162,
        "f" : 2.228,
        "g" : 2.015,
        "h" : 6.094,
        "i" : 7.546,
        "j" : 0.153,
        "k" : 1.292,
        "l" : 4.025,
        "m" : 2.406,
        "n" : 6.749,
        "o" : 7.507,
        "p" : 1.929,
        "q" : 0.095,
        "r" : 7.587,
        "s" : 6.327,
        "t" : 9.356,
        "u" : 2.758,
        "v" : 0.978,
        "w" : 2.560,
        "x" : 0.150,	
        "y" : 1.994,	
        "z" : 0.077,
        "'" : 0.02,
        "," : 0.02,
        " " : 0.02
    }


    input = open("question_4_input.txt")
    result_list = []
    iterations = 0;

    for line in input:
        ciphertext = bytearray.fromhex(line.replace("\n", ""))
        for x in range(0,256):
            key = bytes([x])
            keystream = key * len(ciphertext)
            potential_plaintext = byte_XOR(ciphertext, keystream, frequency_table) 
            result_list.append(potential_plaintext)
    input.close()

    result_list = sorted(result_list, key=lambda x: x[1], reverse=True)
    print(result_list[0])
   

    
def byte_XOR(ciphertext, keystream, frequency_table):
    
    byte_string = bytearray(b'')
    character_freq = 0;
    
    for (x,y) in zip(ciphertext, keystream):
        result = x ^ y
        if chr(result) in frequency_table:
            character_freq += frequency_table[chr(result)]
        byte_string.append(x ^ y)
    
    return byte_string, character_freq
   


if __name__ == "__main__":
    main()