# Main Problem
cryptic_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ASCII alphabet math
ascii_alphabet = [ord(letter) for letter in alphabet]
max_ascii = max(ascii_alphabet)
min_ascii = min(ascii_alphabet)

def decrypt(input, offset = 2):
    
    # convert input to ascii
    ascii_input = [ord(letter) for letter in input]
    output = []

    # translate ascii input and wrap if necessary
    for input_number in ascii_input:
        output_number = input_number + offset

        if output_number > max_ascii:
            output_number = min_ascii + (output_number - max_ascii-1)

        output.append(output_number)
    
    # get back to strings
    char_output = [chr(num) for num in output]
    translated_output = ''.join(char_output)
    return translated_output
    
print(cryptic_text)

print(decrypt(cryptic_text))