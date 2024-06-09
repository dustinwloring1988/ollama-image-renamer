import os
import base64
import requests
import random
import sys

# Function to get Base64 encoded image
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to call the Ollama API and get the description
def get_image_description(base64_image):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llava",
            "prompt": "Summarize this image using one to 5 words. Respond using only those words.",
            "stream": False,
            "images": [base64_image]
        }
    )
    return response.json().get("response", "")

# Function to rename folder based on the description
def rename_folder(folder_path, description):
    parent_dir = os.path.dirname(folder_path)
    
    # Replace non-alphanumeric characters with underscores
    new_folder_name = "".join(c if c.isalnum() else "_" for c in description)
    
    # Ensure no leading or trailing underscores
    new_folder_name = new_folder_name.strip('_')
    
    # Remove duplicate underscores
    while '__' in new_folder_name:
        new_folder_name = new_folder_name.replace('__', '_')
    
    new_folder_path = os.path.join(parent_dir, new_folder_name)

    # Check if the folder name already exists
    while os.path.exists(new_folder_path):
        random_suffix = str(random.randint(100, 999))
        new_folder_path = os.path.join(parent_dir, new_folder_name + "_" + random_suffix)

    os.rename(folder_path, new_folder_path)

# Function to rename image file based on the description
def rename_image(image_path, description):
    folder_path = os.path.dirname(image_path)
    
    # Replace non-alphanumeric characters with underscores
    new_file_name = "".join(c if c.isalnum() else "_" for c in description)
    
    # Ensure no leading or trailing underscores
    new_file_name = new_file_name.strip('_')
    
    # Remove duplicate underscores
    while '__' in new_file_name:
        new_file_name = new_file_name.replace('__', '_')
    
    new_image_path = os.path.join(folder_path, new_file_name + os.path.splitext(image_path)[1])

    # Check if the file name already exists
    while os.path.exists(new_image_path):
        random_suffix = str(random.randint(100, 999))
        new_image_path = os.path.join(folder_path, new_file_name + "_" + random_suffix + os.path.splitext(image_path)[1])

    os.rename(image_path, new_image_path)

# Main script
def main():
    rename_target = "folder"
    if len(sys.argv) > 1:
        rename_target = sys.argv[1]

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".png"):
                image_path = os.path.join(root, file)
                base64_image = get_base64_image(image_path)
                description = get_image_description(base64_image)
                
                if rename_target == "image":
                    rename_image(image_path, description)
                else:
                    folder_path = os.path.dirname(image_path)
                    rename_folder(folder_path, description)

if __name__ == "__main__":
    main()
