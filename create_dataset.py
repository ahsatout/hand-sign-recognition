# Importing necessary libraries
import os
import pickle
import mediapipe as mp
import cv2

# Initializing MediaPipe Hands module
mp_hands = mp.solutions.hands
# Importing MediaPipe drawing utilities for visualization
mp_drawing = mp.solutions.drawing_utils
# Importing MediaPipe drawing styles for visualization
mp_drawing_styles = mp.solutions.drawing_styles


# Creating a Hands object for hand tracking
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

#Directory where images are
DATA_DIR = './data'

# Empty list to store hand landmark data and labels
data = []
labels = []

# Looping through each directory in the data directory
for dir_ in os.listdir(DATA_DIR):

    # Looping through each image in the current directory
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        data_aux = []
        # Initializing temporary lists to store x and y coordinates of landmarks
        x_ = []
        y_ = []
        # Reading the image using OpenCV and coverting it to RGB format required by MediaPipe
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Processing the image to detect hand landmarks using MediaPipe Hands
        results = hands.process(img_rgb)

        # Checking if hand landmarks are detected in the image
        if results.multi_hand_landmarks:

            # Looping through each detected hand
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                # Extracting and normalizing coordinates of each landmark
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            data.append(data_aux)
            labels.append(dir_)

# Serializing the data and labels into a pickle file
f = open('data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()