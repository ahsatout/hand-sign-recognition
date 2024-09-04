
# Hand Sign Recognition

This project implements a machine learning model for recognizing hand signs using  webcam. The project is divided into four main scripts:

1. **Capture Hand Pictures**: A script to capture images of hand signs using a webcam.
2. **Feature Extraction**: A script to loop through captured images, extract relevant features, and save them for training.
3. **Model Training**: A script to train a RandomForest algorithm on the extracted features and save the trained model.
4. **Real-Time Detection**: A script to open the webcam and detect hand signs in real-time using the trained model.



## Directory Structure

```
hand-sign-recognition/
│
├── colllect.py      # Script to capture hand images
├── create_datasset.py         # Script to loop through directories and extract features then save it in a file
├── train_classifier.py              # Script to train the model and serialize it
├── classifier.py         # Script to open the camera and detect hand signs in real time
├── model.py                      # pre trained model
├── data.pickle                      # a ready dataset
├── data/                       # Directory to store the captured hand images and features
├── README.md                   # Documentation for the project
└── requirements.txt            # List of dependencies
```

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/ahsatout/hand-sign-recognition.git
   cd hand-sign-recognition
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### 1. Capture Hand Images
   Use this script to capture images of different hand signs.

   ```bash
   python collect.py
   ```

   The images will be saved in the `data/` directory. 

### 2. Extract Features
   Run this script to extract features from the captured images.

   ```bash
   python create_dataset.py
   ```

   The extracted features will be saved for training.

### 3. Train the Model
   Use this script to train the machine learning model using the extracted features.

   ```bash
   python train_classifier.py
   ```

   The trained model will be saved as model.p

### 4. Detect Hand Signs
   Finally, use this script to open your webcam and start detecting hand signs in real-time.

   ```bash
   python classifier.py
   ```

## For Any Help or Questions

Feel free to contact me via Linkedin or my email : hakim.satout@gmail.com

