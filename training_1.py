import cv2
import numpy as np
import os

# set video file path of input video with name and extension
vid = cv2.VideoCapture('D:\Fathima\Python\human recog1\data\Running\production ID_4440942.mp4')



if not os.path.exists('images'):
      os.makedirs('images')

# for frame identity
index = 839
while(True):
    # Extract images
    ret, frame = vid.read()
    # end of frames
    if not ret:
        break
    # Saves images
    name = './images/Running/frame' + str(index) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    # next frame
    index += 1