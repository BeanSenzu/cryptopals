import base64
import sys
def main():


    potential_key_sizes = []
    input = open("question_6_input.txt")

    lines = input.readlines(80)
    input.close()
    line = "".join(lines)
   

   
    input_line = base64.b64decode(line)
    print(input_line)
  
   

    smallest_edit_distance =  sys.maxsize
    #find the potential key size from 2 - 40
    for key_size in range(2,41):
        first_key_size_worth_of_bytes = bytearray()
        second_key_size_worth_of_bytes = bytearray()
        for i in range(0, key_size):
            first_key_size_worth_of_bytes.append(input_line[i])
            second_key_size_worth_of_bytes.append(input_line[i+key_size])
        normalized_edit_distance = get_edit_distance(first_key_size_worth_of_bytes,second_key_size_worth_of_bytes) / key_size
        potential_key = key_size, normalized_edit_distance
        potential_key_sizes.append(potential_key)

    print(sorted(potential_key_sizes, key=lambda x:x[1]))
    narrowed_down_keys = sorted(potential_key_sizes, key=lambda x:x[1])[:3]

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