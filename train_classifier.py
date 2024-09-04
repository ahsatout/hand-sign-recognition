import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np




# Function to clean data by removing samples with incomplete features to avoid any kind of heterogeneity in our dataset
def clean_data(data, labels):
  cleaned_data = []
  cleaned_labels = []
  for i, sample in enumerate(data):
    if len(sample) == 42:
      cleaned_data.append(sample)
      cleaned_labels.append(labels[i])
  return np.array(cleaned_data), np.array(cleaned_labels)

# Load serialized data
data_dict = pickle.load(open('./data.pickle', 'rb'))

# Apply our function of cleaning
data, labels = clean_data(data_dict['data'],data_dict['labels'])

# Initialize a Random Forest classifier model
model = RandomForestClassifier()

# Train the model on the cleaned data
model.fit(data, labels)

print("Congrats! You have trained your classifier successfully on the provided data.")


# Serialize the trained model to a file named model.p'
with open('model.p', 'wb') as f:
  pickle.dump({'model': model}, f)