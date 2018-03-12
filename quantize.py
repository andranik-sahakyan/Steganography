import numpy as np
from scipy.fftpack import dct, idct


def forward_dct(block):
  return dct(dct(block.T, norm = 'ortho').T, norm = 'ortho')

def reverse_dct(block):
  return idct(idct(block.T, norm = 'ortho').T, norm = 'ortho')


imageLum = np.matrix([
	[62, 55, 55, 54, 49, 48, 47, 55],
	[62, 57, 54, 52, 48, 47, 48, 53],
	[61, 60, 52, 49, 48, 47, 49, 54],
	[63, 61, 60, 60, 63, 65, 68, 65],
	[67, 67, 70, 74, 79, 85, 91, 92],
	[82, 95, 101, 106, 114, 115, 112, 117],
	[96, 111, 115, 119, 128, 128, 130, 127],
	[109, 121, 127, 133, 139, 141, 140, 133]
])

quantization_table = np.matrix([
	[16, 11, 10, 16, 24, 40, 51, 61],
	[12, 12, 14, 19, 26, 58, 60, 55],
	[14, 13, 16, 24, 40, 57, 69, 56],
	[14, 17, 22, 29, 51, 87, 80, 62],
	[18, 22, 37, 56, 68, 109, 103, 77],
	[24, 35, 55, 64, 81, 104, 113, 92],
	[49, 64, 78, 87, 103, 121, 120, 101],
	[72, 92, 95, 98, 112, 100, 103, 99]
]).T


imageLum -= 128
quantized = np.around(forward_dct(imageLum) / quantization_table).astype(int)

# Reverse
r_quantized = np.multiply(quantized, quantization_table)
r_imageLum = np.around(reverse_dct(r_quantized)).astype(int)
r_imageLum += 128

print(r_imageLum)