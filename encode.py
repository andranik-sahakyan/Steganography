#!/usr/bin/env python

from PIL import Image
import numpy as np
import random


# Message to Encode
message = input('[?] Message to Encrpyt: ')
binary = '0' + bin(int.from_bytes(message.encode(), 'big'))[2:]

# Password used to decode message
try:
    pin = int(input('[?] Enter Encryption Pin: '))
except ValueError:
   print('[!] Encryption Pin must only contain digits')

random.seed(pin)

# Open Input Image
file = input('[?] Path to input file: ')
im = Image.open(file)
x, y = im.size
RGB_matrix = np.array(im)

pixels_encoded = []

for i in range(0, len(binary), 2):
    # Generate uniqe random pixel
    pixel = (random.randint(0, x - 1), random.randint(0, y - 1))
    while pixel in pixels_encoded:
        pixel = (randint(0, x), randint(0, y))

    r, g, b = im.getpixel((pixel[0], pixel[1]))

    # Encode 2 bits of data in least significant bits
    r = '0' + bin(r)[2:]
    r_new = r[:6] + binary[i: i + 2]
    RGB_matrix[pixel[1], pixel[0]] = [r_new, g, b]
    pixels_encoded.append(pixel)

    
# Add termination sequence
# This will be removed in next iteration
for i in range(4):
    pixel = (random.randint(0, x), random.randint(0, y))
    while pixel in pixels_encoded:
        pixel = (randint(0, x), randint(0, y))

    r, g, b = im.getpixel((pixel[0], pixel[1]))
    r = '0' + bin(r)[2:]
    r_new = r[:6] + '11'
    RGB_matrix[pixel[1], pixel[0]] = [r_new, g, b]
    pixels_encoded.append(pixel)


# Export encoded image
outfile = input('[?] Name of Encoded Output File: ')
out = Image.fromarray(RGB_matrix)
out.save(outfile)

print('[*] Successfully Encrypted Message in {}'.format(outfile))


'''
SAMPLE RUN
$ ./encode.py
[?] Message to Encrpyt: Dharma Initiative experiments initiate tomorrow.
[?] Enter Encryption Pin: 4815162342
[?] Path to input file: galaxy1.tif
[?] Name of Encoded Image File: code.tif
[*] Successfully Encryped Message in code.tif
'''