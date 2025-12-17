import os

# Current working directory
print("Current Directory:", os.getcwd())

# List files and folders
print("Files and folders:", os.listdir())

# Create a new folder
os.mkdir("demo_folder")
print("Folder created")

# Check if folder exists
print("Folder exists:", os.path.exists("demo_folder"))

# Rename folder
os.rename("demo_folder", "new_folder")
print("Folder renamed")

# Remove folder
os.rmdir("new_folder")
print("Folder removed")