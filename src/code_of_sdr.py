import cv2
import numpy as np
import PIL
from PIL import Image
import serial
import time
arduino = serial.Serial('COM11', 9600, timeout=1)
img = Image.open('my-binary-image (1).png')
img = img.resize((100, 100), PIL.Image.ANTIALIAS)
img.save('resized2.png')
img = cv2.imread("resized2.png",0)
ret,img2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
p = img2.shape
k = np.ndarray(shape=(100, 100), dtype= int)
m = np.ndarray(shape=(100, 100), dtype=int)
rows, cols = img2.shape

for a in range(rows):
    for b in range(cols):
        k[a, b] = img2[a, b]


for i in range(0, 100):
    for j in range(0, 100):
        if i % 2 == 0:
            m[i, j] = k[i, j]
        else:
            m[i, j] = k[i, 99-j]
c=0
print(m)
while len(m):
  for r in range(0, 100):
     if m[0, r] == 0:
         command = str.encode('0')
         arduino.write(command)
         time.sleep(0)
         print(arduino.readline().decode('utf-8'))
         
     else:
         command = str.encode('1')
         arduino.write(command)
         time.sleep(0)
         print(arduino.readline().decode('utf-8'))
     print(c)
     c=c+1
m = np.delete(m,(0),axis=0)

arduino.close()

