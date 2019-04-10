import cv2
import numpy as np

keyboard = np.zeros((1000, 1500, 3), np.uint8)

#keys
cv2.rectangle(keyboard, (0, 0), (200, 200), (255, 0, 0), 3)

cv2.imshow("keyboard", keyboard)
cv2.waitKey(0)
cv2.destroyAllWindows()