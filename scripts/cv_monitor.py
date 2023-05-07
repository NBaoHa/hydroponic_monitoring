import numpy as np 
import cv2 


def initializing_cam(capture: cv2.VideoCapture):
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        
        num_bands = frame.shape[2]
        return num_bands

 
def main(cap: cv2.VideoCapture):
    # loop over frames from the camera
    while True:
        # read a frame from the camera
        ret, frame = cap.read()
      
        # if the frame was not read successfully, break out of the loop
        if not ret:
            break

        # split the frame into its three color channels: Red, Green, and Blue
        b, g, r, ir = cv2.split(frame)
        # blue, green, red color gun order
        false_color = cv2.merge((ir, g, r))
        
        # create three separate windows and display each channel in a different window
        cv2.imshow('Original', frame_data)
        cv2.imshow('False-Color Composite', false_color)
        

        # wait for a key press and check if the "q" key was pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    print("number of bands: {}".format(initializing_cam(cap)))
    main(cap)
    # release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()
