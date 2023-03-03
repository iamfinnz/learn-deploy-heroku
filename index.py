import cv2
import numpy as np
import matplotlib.pyplot as plt

ref = cv2.imread(r"C:\Users\MSI GF63\Documents\TEMPLATE MATCHING\COBA3\ocr_a_reference.png")
ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
plt.imshow(ref)
 
#hold the window
plt.waitforbuttonpress()
plt.close('all')