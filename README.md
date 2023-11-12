# Screenshot Renamer

## Overview

Screenshot Renamer is a Python script that automatically renames image files in a specified folder based on the content of the images. It uses OpenAI's GPT-4 Vision model to generate descriptive filenames. The script supports various image formats and resizes larger images for processing while maintaining the aspect ratio.

## Features

- **Automatic Image Renaming:** Renames images based on their content using AI.
- **Supports Multiple Formats:** Works with JPG, JPEG and PNG.
- **Image Resizing:** Resizes images larger than 1024 pixels on the longer side to optimize processing.
- **Environment Variables:** Utilizes a `.env` file for secure API key and folder path management.

## Requirements

- Python 3.x
- Pillow library (PIL)
- python-dotenv library
- OpenAI API key

## Installation

1. **Clone the repository:**
   ```sh
   git clone [repo-url]
   cd [repo-name]
   ```

2. **Install required packages:**
   ```sh
   pip install pillow python-dotenv requests
   ```

3. **Set up your `.env` file:**
   Create a `.env` file in the root directory with the following content:
   ```makefile
   OPENAI_API_KEY=your_openai_api_key_here
   FOLDER_PATH=path_to_your_images_folder
   ```

## Usage

Run the script using Python:
```sh
python3 imagescan.py
```
The script will process all images in the specified folder, resize them if necessary, send them to the OpenAI API for content analysis, and rename the files based on the AI's response.

## Important Notes

- Ensure your OpenAI API key has access to the GPT-4 Vision model.
- The script only processes images with extensions specified in `allowed_extensions`.
- Images are renamed in the same directory. Ensure you have backup copies if necessary.

## License

Free to use

## Author

Jørgen Lindalen
