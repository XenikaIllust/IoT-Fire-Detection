'''
import cv2
vidcap = cv2.VideoCapture('example.mp4')
framerate = round(vidcap.get(cv2.CAP_PROP_FPS))
success,image = vidcap.read()
count = 0
success = True

while success:
    success,image = vidcap.read()
    #print(vidcap.get(cv2.CAP_PROP_POS_MSEC))
    if round(count / framerate) == 0:
        cv2.imwrite("./data/frame" + str(count) + ".jpg", image)
        print(count)
    count += 1

    #if count // framerate == 0:
    #    cv2.imwrite("./data/frame" + str(count) + ".jpg", image)     # save frame as JPEG file
'''


import numpy as np
import cv2

cap = cv2.VideoCapture('example.mp4')
framerate = round(cap.get(cv2.CAP_PROP_FPS))
framecount = 0
im_count = 0
success = True

while success:
    # Capture frame-by-frame
    success, image = cap.read()
    framecount += 1

    # Check if this is the frame closest to 1 seconds
    if framecount == (framerate * 1):
      framecount = 0
      cv2.imwrite('./data/' + str(im_count) + '.jpg', image)
      im_count += 1

    # Check end of video
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


"""
import cv2
import time

cap = cv2.VideoCapture('example.mp4')
framerate = round(cap.get(cv2.CAP_PROP_FPS))
framecount = 0

while(True):
    # Capture frame-by-frame
    success, image = cap.read()
    framecount += 1

    # Check if this is the frame closest to 1 second
    if framecount == (framerate * 1):
        time.sleep(1)
        framecount = 0
        cv2.imshow('image',image)

    # Check end of video
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
"""