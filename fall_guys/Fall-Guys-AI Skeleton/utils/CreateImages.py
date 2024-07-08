import cv2
import numpy as np
from pathlib import Path

data = np.load("C:/Users/liang/OneDrive/Documents/GitHub/algoverse-ai-bootcamp/fall_guys/Fall-Guys-AI Skeleton/data/training_data.npy", allow_pickle=True)
targets = np.load("C:/Users/liang/OneDrive/Documents/GitHub/algoverse-ai-bootcamp/fall_guys/Fall-Guys-AI Skeleton/data/target_data.npy", allow_pickle=True)

print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')

# Lets see how many of each type of move we have.
unique_elements, counts = np.unique(targets, return_counts=True)
print(np.asarray((unique_elements, counts)))

# Store both data and targets in a list.
# We may want to shuffle down the road.

# Pair image data with targets and store in a list
holder_list = [[data[i], targets[i]] for i in range(len(data))]

# Initialize action counters
count_up = 0
count_left = 0
count_right = 0
count_jump = 0

# Define the path where images will be saved
save_path = Path("C:/Users/liang/OneDrive/Documents/GitHub/algoverse-ai-bootcamp/fall_guys/Fall-Guys-AI Skeleton/data")

# Ensure the save path exists
(save_path / 'up').mkdir(parents=True, exist_ok=True)
(save_path / 'left').mkdir(parents=True, exist_ok=True)
(save_path / 'right').mkdir(parents=True, exist_ok=True)
(save_path / 'jump').mkdir(parents=True, exist_ok=True)

# Ensure the save path exists
(save_path / 'up').mkdir(parents=True, exist_ok=True)
(save_path / 'left').mkdir(parents=True, exist_ok=True)
(save_path / 'right').mkdir(parents=True, exist_ok=True)
(save_path / 'jump').mkdir(parents=True, exist_ok=True)

# Define a function to save images with the correct naming convention
def save_image(image, action, count):
    action_map = {'W': 'up', 'A': 'left', 'D': 'right', 'SPACE': 'jump'}
    action_name = action_map.get(action, 'unknown')
    if action_name != 'unknown':
        filename = save_path / action_name / f"{action_name}_{count}.png"
        cv2.imwrite(str(filename), image)
        print(f"Saved {filename}")

# Loop through each image-target pair in holder_list and save images
for image, action in holder_list:
    if action == 'W':
        count_up += 1
        save_image(image, action, count_up)
    elif action == 'A':
        count_left += 1
        save_image(image, action, count_left)
    elif action == 'D':
        count_right += 1
        save_image(image, action, count_right)
    elif action == 'SPACE':
        count_jump += 1
        save_image(image, action, count_jump)
    else:
        print(f"Unknown action: {action}")

# Optional: Error handling for unexpected cases
try:
    # Ensure all actions are accounted for
    assert len(np.unique(targets)) <= 4
except AssertionError:
    print("Error: Unexpected action found in target data.")

# Print final action counts
print(f"Total Up Actions: {count_up}")
print(f"Total Left Actions: {count_left}")
print(f"Total Right Actions: {count_right}")
print(f"Total Jump Actions: {count_jump}")