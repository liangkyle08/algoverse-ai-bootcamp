from fastai.vision.all import *
import time
import cv2
from utils.grabscreen import grab_screen

def label_func(x): return x.parent.name

def run():
    # Set the path to the directory containing the training data
    path = Path("C:/Users/liang/OneDrive/Documents/GitHub/algoverse-ai-bootcamp/fall_guys/Fall-Guys-AI Skeleton/data")
    
    # Use get_image_files to retrieve filenames of images in the data directory
    fnames = get_image_files(path)
    print(f"Total Images: {len(fnames)}")

    # Create an ImageDataLoaders instance
    dls = ImageDataLoaders.from_path_func(path, fnames, label_func, item_tfms=Resize(224), bs=64, num_workers=4)
    
    # Initialize a CNN learner using resnet18 and error_rate as the evaluation metric
    learn = vision_learner(dls, resnet18, metrics=error_rate)
    
    # Fine-tune the model
    learn.fine_tune(4)  # You can adjust the number of epochs and learning rate if necessary
    
    print("Model trained successfully")
    
    # Export the trained model
    learn.export()

    print("Model exported successfully")

if __name__ == '__main__':
    run()
