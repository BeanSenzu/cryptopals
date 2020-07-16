def main():
    
    plaintext =  bytes("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal" , 'utf-8')   
    key = bytearray("ICE", 'utf-8')
    key_index = 0
    ciphertext = bytearray()
    key_length = len(key)

    for byte in plaintext:
        ciphertext.append(byte ^ key[key_index % key_length])
        key_index += 1
    
    expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    print(ciphertext.hex() == expected)


if __name__ == "__main__":
    main()