import numpy as np 
import cv2 

sample_fbands_data = [[[[159,  56, 189,  38],
  [140,  68,  64, 123],
  [190,  28, 122, 128],
  [127,  76,  98, 134],
  [171,  36, 188,  26],
  [115,  88,  91,  44],
  [ 64,  41,  55, 105],
  [ 88,  34,  20,  50]],

 [[182,  89, 143, 141],
  [ 36, 107,  62,  47],
  [190,  36, 146,  81],
  [131,  47, 139, 137],
  [ 97,  48,  62, 105],
  [144,  36,  62, 145],
  [ 67,  34,  91,  55],
  [108,  57,  81,  87]],

 [[160,  36, 107,  74],
  [ 55,  76,  55,  57],
  [135,  88,  91, 145],
  [109,  34,  27,  82],
  [ 34,  57, 183,  52],
  [ 84,  41, 173, 142],
  [ 28,  44, 189,  27],
  [ 75,  91, 111,  68]]]]


sample_data = np.array(sample_fbands_data)

while True:
    # loop over frames from the data stream
    for frame_data in sample_data:
        print(frame_data)
        
        # split the frame into separate bands
        b, g, r, ir = cv2.split(frame_data)

        # create a false-color composite image from the Red, Green, and IR bands
        #false_color = cv2.merge((ir, g, r))

        # display the original frame and the false-color composite image
        cv2.imshow('Original', frame_data)
        #cv2.imshow('False-Color Composite', false_color)

    # wait for a key press and check if the "q" key was pressed
    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        break

# close all windows
cv2.destroyAllWindows()