# Ollama Image Renamer

This script renames folders or image files based on the description generated from the image content. It utilizes the Ollama API to generate a brief description of each image in a directory and renames the folders or image files accordingly.

## Features

- Converts images to Base64 encoding.
- Uses Ollama API to generate a description of each image.
- Renames folders or image files based on the generated description.
- Handles non-alphanumeric characters by replacing them with underscores.
- Ensures unique names to avoid conflicts.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/dustinwloring1988/ollama-image-renamer.git
   cd ollama-image-renamer
   ```

2. Install the required Python libraries:

   ```sh
   pip install requests
   ```
   
## Usage

Run the script to rename folders or image files based on the image descriptions.

## Rename Folders

To rename folders based on the image description, run the script without any arguments:

   ```sh
   python app.py
   ```
   
## Rename Image Files

To rename image files based on the description, pass image as an argument:

   ```sh
   python app.py image
   ```
   
## How It Works

1. The script walks through the current directory and its subdirectories to find .png files.
2. For each .png file, it reads and converts the image to Base64.
3. It sends the Base64 encoded image to the Ollama API to get a brief description.
4. Based on the description, it either renames the folder containing the image or the image file itself.

## Example

If an image is described as "sunset over mountains":

1. If renaming folders: The containing folder might be renamed to sunset_over_mountains.
	
2. If renaming image files: The image file might be renamed to sunset_over_mountains.png.

## Configuration

1. Ensure the Ollama API is running locally on http://localhost:11434.
2. Modify the API endpoint in the script if needed.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a pull request.

## Contact

For any inquiries, please open a issue on this project.
