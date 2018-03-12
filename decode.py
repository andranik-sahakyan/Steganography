#!/usr/bin/env python

from PIL import Image
import numpy as np
import random

# Password used to decode message
try:
    pin = int(input('[?] Enter Decryption Pin: '))
except ValueError:
   print('[!] Decryption Pin must only contain digits')

random.seed(pin)

# Open Encoded Image
file = input('[?] Path of Encoded Image: ')
im = Image.open(file)
x, y = im.size
RGB_matrix = np.array(im)
binary_message = ''

# Read until termination sequence
while not binary_message.endswith('11111111'):
	pixel = (random.randint(0, x - 1), random.randint(0, y - 1))
	r, g, b = im.getpixel((pixel[0], pixel[1]))
	binary_message += bin(r)[-2:]

decoded = ''
for i in range(0, len(binary_message) - 8, 8):
	decoded += chr(int(binary_message[i: i + 8], 2))

print('[*] Decrypted Message: {}'.format(decoded))


'''
SAMPLE RUN
$ ./decode.py
[?] Enter Decryption Pin: 4815162342
[?] Path of Encoded Image: code.tif
[*] Decrypted Message: Dharma Initiative experiments initiate tomorrow.
'''