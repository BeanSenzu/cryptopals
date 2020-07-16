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

    input_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    #Create bytearray of hex string
    ciphertext = bytearray.fromhex(input_string)
    result_list = []
    character_freq = 0
    #Loop through the keys [0,255] to see which key is the correct one
    for x in range(0,256):
        
        key = bytes([x]);
        #Create a keystream of x with length of ciphertext
        keystream = key * len(ciphertext)
        result_list.append(byte_XOR(ciphertext,keystream, frequency_table))

        
    print(sorted(result_list, key=lambda x: x[1], reverse=True))
   

    


def byte_XOR(ciphertext, keystream, frequency_table):
    
    byte_string = bytearray(b'')
    character_freq = 0;
    
    
    for (x,y) in zip(ciphertext, keystream):
        result = x ^ y
        if chr(result).lower() in frequency_table:
            character_freq += frequency_table[chr(result).lower()]
        else:
            character_freq -= 10

        byte_string.append(x ^ y)
    
    return byte_string, character_freq
    


if __name__ == "__main__":
    main()