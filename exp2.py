def remove_repeated(size, a):
    i = 0
    while i < size:
        j = i + 1
        while j < size:
            if a[i] == a[j]:
                a.pop(j)
                size -= 1
            else:
                j += 1
        i += 1
    return size

def insert_element_at(position, a, size):
    a.insert(position, 23)
    return size + 1

def print_grid(cipherkey):
    print("\nPlayfair Cipher Key Grid:")
    for i in range(5):
        for j in range(5):
            print(chr(cipherkey[i][j] + ord('A')), end=' ')
        print()

def playfair_cipher():
    numstr = []
    numkey = []
    cipherkey = [[0]*5 for _ in range(5)]
    flag = -1

    str_input = input("\nEnter a string: ")
    str_input = ''.join([ch.upper() for ch in str_input if ch != ' '])

    print(f"Entered String is: {str_input}")
    size = len(str_input)

    for char in str_input:
        numstr.append(ord(char) - ord('A'))
    lennumstr = len(numstr)

    key = input("\nEnter a key (non-repeating elements): ")
    key = ''.join([ch.upper() for ch in key if ch != ' '])

    print(f"Entered Key is: {key}")

    k = 0
    for i in range(len(key) + 26):
        if i < len(key):
            if key[i] == 'J':
                flag = 8
            numkey.append(ord(key[i]) - ord('A'))
        else:
            if k != 9 and k != flag:
                numkey.append(k)
            k += 1

    lenkey = remove_repeated(len(numkey), numkey)

    print("\nEntered key converted according to Playfair Cipher rule:")
    print(''.join([chr(numkey[i] + ord('A')) for i in range(lenkey)]))

    k = 0
    for i in range(5):
        for j in range(5):
            cipherkey[i][j] = numkey[k]
            k += 1

    print_grid(cipherkey)

    i = 0
    while i < lennumstr:
        if i + 1 < lennumstr and numstr[i] == numstr[i + 1]:
            lennumstr = insert_element_at(i + 1, numstr, lennumstr)
        i += 2

    if lennumstr % 2 != 0:
        lennumstr = insert_element_at(lennumstr, numstr, lennumstr)
    
    print("Prepared Message for Encryption: ", end="")
    print(''.join([chr(numstr[i] + ord('A')) for i in range(lennumstr)]))

    numcipher = []

    for k in range(0, lennumstr, 2):
        row1, col1 = -1, -1
        row2, col2 = -1, -1

        for i in range(5):
            for j in range(5):
                if numstr[k] == cipherkey[i][j]:
                    row1, col1 = i, j
                if numstr[k + 1] == cipherkey[i][j]:
                    row2, col2 = i, j

        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1

        numcipher.append(cipherkey[row1][col1])
        numcipher.append(cipherkey[row2][col2])

    print("\nCipher Text is: ", end="")
    print(''.join([chr(numcipher[i] + ord('A')) for i in range(len(numcipher))]))

if __name__ == "__main__":
    playfair_cipher()