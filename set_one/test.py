import base64

def main():

    input_file = open("question_6_input.txt")
    output = []
    key = bytes([255])
    for line in input_file:
        ciphertext = base64.b64decode(line)
        print(ciphertext)
        keystream = key * len(ciphertext)
        output.append(bxor(keystream, ciphertext))
    input_file.close()

    #print(output)



def bxor(a, b):
    return bytes([x^y for (x,y) in zip(a,b)])

if __name__ == "__main__":
    main()