import cv2
import os

def resize(path):
    img = cv2.imread(path)
    res = cv2.resize(img, (640, 480), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(path, res)


path_train = "image labels ala carte"

paths = [path_train]

for path in paths:
    for filename in os.listdir(path):
        resize(path + "/" + filename)