Face Recognition
--------

This repository contains various scripts utilizing OpenCV Python library for image and video processing. The main tasks performed by these scripts include image display, video display, camera feed capture, face detection, and eye detection.

### Scripts Description

1.  **Image Display Script**This script reads an image file and displays it in a window. The window remains open until a key is pressed.
    
2.  **Video File Display Script**This script captures frames from a video file and displays them continuously in a window. The window remains active, displaying the frames in sequence, until the 's' key is pressed to terminate the process.
    
3.  **Camera Feed Display Script**This script captures live video feed from the default camera (usually the webcam) and displays the frames in real-time in a window. The display continues until the 's' key is pressed to stop the feed.
    
4.  **Image Face Detection Script**This script reads an image file and converts it to grayscale. Using a pre-trained Haar Cascade classifier (haarcascade\_frontalface\_default.xml), it detects faces in the image and draws rectangles around the detected faces. The result is displayed in a window.
    
5.  **Live Face and Eye Detection Script**This script captures live video feed from the default camera, converts the frames to grayscale, and performs face and eye detection using Haar Cascade classifiers (haarcascade\_frontalface\_default.xml and haarcascade\_eye.xml). Detected faces are enclosed in rectangles and displayed in real-time. The process can be stopped by pressing the 's' key.
    

### Dependencies

*   **OpenCV**: Import the OpenCV library to handle image and video capture, reading, display, and manipulation. It also provides the pre-trained Haar Cascade classifiers used for face and eye detection.
