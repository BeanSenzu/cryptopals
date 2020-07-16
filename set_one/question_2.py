def main():
    input_hex_string = "1c0111001f010100061a024b53535009181c"
    XOR_string = "686974207468652062756c6c277320657965"
    result = ""
    for i in range(0, len(XOR_string)):
        char = hex(int(input_hex_string[i], 16) ^ int(XOR_string[i], 16))
        result += char[2:]
        #print(hex(int(input_hex_string[i], 16) ^ int(XOR_string[i], 16)))

    XOR_output= hex(int(input_hex_string, 16) ^int(XOR_string, 16))
    XOR_output_string = XOR_output[2:]
    expected = "746865206b696420646f6e277420706c6179"
    print(result+ "\n")
    print(expected + "\n")
    test(result, expected)
    


def test(output, expected):
    print(output == expected)

# 4 -> 0100
# a -> 1010
# 2 -> 0010
# 4a2 -> 010010100010
# XOR with 4a2 => 0

if __name__ == "__main__":
    main()