

#All letters of English Alphabets
def create_alphabet_file(linesize, filename):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    with open(filename, 'w') as file:
        for i in range(0, len(alphabet), linesize):
            line = alphabet[i:i+linesize]
            file.write(line + '\n')
