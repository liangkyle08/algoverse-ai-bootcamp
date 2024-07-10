import numpy as np
import cv2
import time
import os

from utils.grabscreen import grab_screen
from utils.getkeys import key_check

# File paths for saving data
file_name = "C:/Users/liang/OneDrive/Documents/GitHub/algoverse-ai-bootcamp/fall_guys/Fall-Guys-AI Skeleton/data/training_data.npy"
file_name2 = "C:/Users/liang/OneDrive/Documents/GitHub/algoverse-ai-bootcamp/fall_guys/Fall-Guys-AI Skeleton/data/target_data.npy"

# Function to load existing data or initialize empty lists
def get_data():
    if os.path.isfile(file_name) and os.path.isfile(file_name2):
        image_data = np.load(file_name, allow_pickle=True).tolist()
        targets = np.load(file_name2, allow_pickle=True).tolist()
    else:
        image_data = []
        targets = []
    return image_data, targets

# Function to save data to the specified file paths
def save_data(image_data, targets):
    np.save(file_name, np.array(image_data))
    np.save(file_name2, np.array(targets))

# Load existing data or initialize empty lists
image_data, targets = get_data()
collecting_data = False
program_running = True

print("Press 'B' to start collecting data, 'H' to halt, and 'Q' to quit.")

# Main loop
while program_running:
    keys = key_check()

    if 'B' in keys:
        collecting_data = True
        print("Started collecting data.")
    elif 'H' in keys:
        collecting_data = False
        print("Stopped collecting data.")
    elif 'Q' in keys:
        print("Quitting...")
        program_running = False
        break

    # If collecting data, capture screen and process the image
    if collecting_data:
        last_time = time.time()

        # Capture screen
        image = grab_screen(region=(0, 0, 1920, 1080))  # Adjust this based on your screen resolution
        # Convert to grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Apply Canny edge detection
        image = cv2.Canny(image, threshold1=119, threshold2=250)
        # Resize image
        image = cv2.resize(image, (224, 224))

        # Append processed image to image_data
        image_data.append(image)

        # Record key presses and append to targets
        keys = key_check()
        print(keys)
        targets.append(keys)

        # Debug line to display the processed image
        cv2.imshow('Processed Image', image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        print('Loop took {} seconds'.format(time.time() - last_time))

# Save collected data
save_data(image_data, targets)

print("Data saved.")
