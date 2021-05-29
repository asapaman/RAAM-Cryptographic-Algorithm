def enc(path, key):
    try:
        keylength = len(key)

        fin = open(path, 'rb')
    # storing image data in variable "image"
        image = fin.read()
        fin.close()
        path = path.split('/')[-1]

        # converting image into byte array to
    # perform encryption easily on numeric data
        image = bytearray(image)
    # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
      #      print("rindex:", index, "\tvalues: ", values)
            image[index] = values ^ ord(key[index % keylength])

    # opening file for writting purpose
        path = "enc_"+path
        fin = open(path, 'wb')

    # writing encrypted data in image
        fin.write(image)
        fin.close()
        print('Encryption Done...')


    except Exception:
        print('Error caught : ', Exception.__name__)


def dec(path, key):
    # try block to handle the exception
    try:
        # print path of image file and decryption key that we are using
        print('The path of file : ', path)
        print('Note : Encryption key and Decryption key must be same.')
        print('Key for Decryption : ', key)
        keylength = len(key)

        # open file for reading purpose

        fin = open(path, 'rb')
        # storing image data in variable "image"
        image = fin.read()
        fin.close()
        path = path.split('/')[-1]

        # converting image into byte array to perform decryption easily on numeric data
        image = bytearray(image)
        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ ord(key[index % keylength])
        # opening file for writting purpose
        path = "dec_" + path
        fin = open(path, 'wb')

        # writing decryption data in image
        fin.write(image)
        fin.close()
        print('Decryption Done...')


    except Exception:
        print('Error caught : ', Exception.__name__)
