import os

# Set the directory where the validation data is stored
val_data_dir = "C:/Users/karun/OneDrive/Desktop/Project/CODE/images/val"

# Use os.path.join() to create a path to the validation data directory
val_dir = os.path.join(val_data_dir, "val")

print("Path to validation data: ", val_dir)
