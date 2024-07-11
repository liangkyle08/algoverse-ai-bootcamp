import random
import time

from utils.getkeys import key_check
import pydirectinput
import keyboard
import time
import cv2
from utils.grabscreen import grab_screen
from utils.directkeys import PressKey, ReleaseKey, W, D, A
from fastai.vision.all import *

def label_func(x):
    return x.parent.name
learn_inf = load_learner("C:/Users/liang/OneDrive/Documents/GitHub/algoverse-ai-bootcamp/fall_guys/Fall-Guys-AI/data/export.pkl");
print("loaded learner")

# Sleep time after actions
sleepy = 0.1

# Wait for 'B' to start
print("Waiting for 'B' to start...")
keyboard.wait('B')
time.sleep(sleepy)

# Hold down 'W' key for continuous forward movement
print("Starting game...")
keyboard.press('w')

try:
    while True:
        # Capture game screen
        image = grab_screen(region=(0, 0, 1920, 1080))
        
        # Convert to grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Apply Canny edge detection
        image = cv2.Canny(image, threshold1=119, threshold2=250)
        # Resize image
        image = cv2.resize(image, (224, 224))
        
        # Get model prediction
        result = learn_inf.predict(image)
        action = result[0]
        
        # Implement action based on model prediction
        if action == 'jump':
            keyboard.press('SPACE')  # Example: Press space to jump
            time.sleep(sleepy)
            keyboard.release('SPACE')
        elif action == 'LEFT':
            keyboard.press('a')  # Example: Press 'a' to move left
            time.sleep(sleepy)
            keyboard.release('a')
        elif action == 'right':
            keyboard.press('d')  # Example: Press 'd' to move right
            time.sleep(sleepy)
            keyboard.release('d')
        # Add more actions as needed
        
        # End simulation by pressing 'H' (example termination condition)
        if keyboard.is_pressed('h'):
            break
        
except KeyboardInterrupt:
    print("Script interrupted.")

finally:
    # Release 'W' key to stop forward movement
    keyboard.release('w')
    print("Game ended.")