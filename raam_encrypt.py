import hashlib
def raam_enc(path, key):
    print(key)
    fin = open(path, 'rb')
    # storing image data in variable "image"
    image = fin.read()
    fin.close()
    path = path.split('/')[-1]
    # converting image into byte array to
    # perform encryption easily on numeric data
    image = bytearray(image)
    print("initial image data : ",image)
    imagedata = []
    for index, values in enumerate(image):
        imagedata =imagedata + [values]
    print("initial image values : ",imagedata)

    remainder = (len(imagedata) + 64) % len(key)
    adder_len = len(key) - remainder
    print("remainder : ", remainder)
    if adder_len <= 2:
        for i in range(adder_len):
            imagedata = imagedata + [ord('Z')]
    else:
        if adder_len - 2 < 10:
            for i in range(adder_len-2):
                imagedata = imagedata + [ord('Z')]
            imagedata = imagedata + [0] + [adder_len - 2]
        else:
            for i in range(adder_len):
                imagedata = imagedata + [ord('Z')]
            imagedata = imagedata + [0] + [adder_len - 2]

    keyencode = hashlib.sha256(key.encode())
    key256 = keyencode.hexdigest()
    keyhash = []
    for i in key256:
        keyhash.append(ord(i))
    plainText2 = keyhash[:32] + imagedata + keyhash[32:]
    print("plainText2 = " , plainText2)
    print("value of Q = ", len(plainText2) // len(key))
    count = 0

    sendtext = []

    # +++++++++++++++++++++++++++++++ Key Generation ++++++++++++++++++++++++


    test_str = key
    binary = ''

    res = ''.join(format(ord(i), '07b') for i in test_str)
    ns = ''
    # rearranging the binary of original string to get another value;
    for i in range(7):
        for j in range(len(res) // 7):
            ns = ns + res[j * 7 + i]
    print("\n===============================================================")

# appending the rearranged bits to the binary of original string
    res = res + ns
    print("\n===============================================================")
    ns = ''

# rearranging the original + rearranged appended bits
    for i in range(7):
        for j in range(len(res) // 7):
            ns = ns + res[j * 7 + i]
# Again appending the above bits to the earlier appended + original bits
    res = res + ns
    print("\n===============================================================")
    ns = res



# converting binary into char and storing it in string_data variable
# and printing binary value followed by its char value here all 4 key are joind
# in a single string so we will have to seperate it in next step.
    string_data = ""
    for i in range(0, len(ns), 7):
        temp_bin = ns[i:i + 7]
        print(temp_bin, end='\t')
        string_data = string_data + chr(int(temp_bin, 2))
        print(chr(int(temp_bin, 2)))
    print(string_data)
    print(len(string_data))

# print(string_data[16])
# print(string_data[17], ord(string_data[17]), format(ord(string_data[17]), '07b'))
# print(string_data[18])

    key_matrix = []  # it will store the all 10 key value
    key1 = string_data
    length = len(test_str)

# this will seperate the 4 key from single string and store it in 'key_matrix';
    for i in range(4):
        keychunk = key1[i * length:(i + 1) * length]
        key_matrix.append(keychunk)

# now other 4 key will be generated by adding last half of previous key and
# first half of next key
    counter = length // 2
    for i in range(3):
        key = key1[counter:counter + length]
        key_matrix.append(key)
        counter = counter + length
    key8 = key1[counter:] + key1[:length // 2]  # 8th key is generated by adding last half
# of 4th key with first half of first key

    key_matrix.append(key8)

# now other two matrix will be generated by adding 1/4th of each of first 4 key
    z = length // 4
    last = length - (3 * z)
    key9 = key_matrix[0][-z:] + key_matrix[1][-z:] + key_matrix[2][-z:] + key_matrix[3][-last:]
    key10 = key_matrix[0][:z] + key_matrix[1][:z] + key_matrix[2][:z] + key_matrix[3][:last]
    key_matrix.append(key9)
    key_matrix.append(key10)

    print(key_matrix)

# +++++++++++++++++++++++++ End Of Key Generation Function ++++++++++++++++++++++++

# =========================== Encryption Function ===============================
    def encrypt(text, key):
        # text=this.text
        for x in range(10):
            j = 0
            matrix = []
            count = 0
            for i in range(len(text) // len(key)):
                k = len(key) * (i + 1)
                range1 = text[j:k]
                matrix.append(range1)
                j = k
                count = count + 1
            print("Matrix No : ", x + 1, " is generated")

            text = []
            for i in range(len(key)):
                for j in range(count):
                    text.append(matrix[j][i] ^ ord(key_matrix[x][i]))
        print("final text values : ", text)
        text = bytearray(text)
        print("final text array : ", text)
        #global path
        name = 'encrypt_' + path
        fin = open(name, 'wb')
    # writing encrypted data in image
        fin.write(text)
        print(text)
        fin.close()
    encrypt(plainText2, key)
    #input()