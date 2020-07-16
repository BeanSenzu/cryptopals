import base64

def main():
    expected_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    hex_bytearray = bytearray.fromhex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
    base64_encoded_bytearray = base64.b64encode(hex_bytearray)
    output = base64_encoded_bytearray.decode('utf-8')
    test(output, expected_string)
    


def test(output, expected):
     print(output == expected)
    
if __name__ == "__main__":
    main()

