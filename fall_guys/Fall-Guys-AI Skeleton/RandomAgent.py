import random
import time
import keyboard
from utils.getkeys import key_check
from utils.directkeys import PressKey, ReleaseKey, W, A, D, SPACE
from utils.grabscreen import grab_screen
from fastai.vision.all import *

# Load the trained model
learn_inf = load_learner('path_to_export.pkl')
print("Loaded learner")

# Define a function to release all keys except 'W'
def release_all_except_w():
    keys_to_release = [A, D, SPACE]
    for key in keys_to_release:
        ReleaseKey(key)

# Define a function to move left
def move_left():
    PressKey(A)
    ReleaseKey(D)
    ReleaseKey(SPACE)

# Define a function to move right
def move_right():
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(SPACE)

# Define a function to jump
def jump():
    PressKey(SPACE)
    ReleaseKey(A)
    ReleaseKey(D)

# Sleep time after actions
sleepy = 0.1

# Wait for 'B' to start
print("Waiting for 'B' to start...")
keyboard.wait('B')
time.sleep(sleepy)

# Hold down 'W' key for continuous forward movement
print("Starting game...")
PressKey(W)

try:
    while True:
        # Capture game screen
        image = grab_screen(region=(50, 100, 799, 449))
        
        # Get model prediction
        result = learn_inf.predict(image)
        action = result[0]
        
        # Implement action based on model prediction
        if action == 'jump':
            jump()
        elif action == 'left':
            move_left()
        elif action == 'right':
            move_right()
        else:
            release_all_except_w()
        
        print("~~~ Debugging ~~~")
        print("Action...", action)
        print("W........", keyboard.is_pressed('W'))
        print("A........", keyboard.is_pressed('A'))
        print("D........", keyboard.is_pressed('D'))
        print("SPACE....", keyboard.is_pressed('SPACE'))
        print()

        time.sleep(sleepy)
        
        # End simulation by pressing 'H'
        keys = key_check()
        if 'H' in keys:
            break
        
except KeyboardInterrupt:
    print("Script interrupted.")

finally:
    # Release all keys at the end
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    ReleaseKey(SPACE)
    print("Game ended.")