#import required libraries
import os
import cv2

#defining where our images will be stored
DATA_DIR = './data'

#defining number of classes/categories we are trying to collect
number_of_classes = 3
#number of images per class
dataset_size = 100

# Capturing video from webcam
cap = cv2.VideoCapture(0)

for j in range(number_of_classes):
    #Creating a directory for each class if it doesn't exist
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))
    #Displaying a message on the video feed to prompt the user to start capturing data for the current class and give him a small  break between each class
    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" Button ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    #Looping to capture the specified number of images for the current class
    counter = 0
    while counter < dataset_size:
        #Capturing a frame from the video feed
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        #Saving the image to disk
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

#Releasing the video capture device and closing all OpenCV windows
cap.release()
cv2.destroyAllWindows()