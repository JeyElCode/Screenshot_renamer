import base64
import requests
import os
from PIL import Image
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
folder_path = os.getenv("FOLDER_PATH")

allowed_extensions = [".jpg", ".jpeg", ".png", ".gif"]


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def resize_image_proportionally(original_path, resized_path, max_size=1024):
    with Image.open(original_path) as image:
        width, height = image.size

        # Resize only if it is larger than max_size
        if width > max_size or height > max_size:
            if width > height:
                new_height = int((max_size / width) * height)
                new_size = (max_size, new_height)
            else:
                new_width = int((max_size / height) * width)
                new_size = (new_width, max_size)

            image.thumbnail(new_size)
            image.save(resized_path)
            return True
        else:
            return False  


for filename in os.listdir(folder_path):
    if any(filename.lower().endswith(ext) for ext in allowed_extensions):
        original_path = os.path.join(folder_path, filename)
        resized_path = os.path.join(folder_path, "resized_" + filename)


        resized = resize_image_proportionally(original_path, resized_path)

        if resized:
            base64_image = encode_image(resized_path)
        else:
            base64_image = encode_image(original_path)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
              {
                "role": "user",
                "content": [
                  {
                    "type": "text",
                    "text": "Give me a filename for this image based on its content that is max 30chars long, and add the original file-extention"
                  },
                  {
                    "type": "image_url",
                    "image_url": {
                      "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                  }
                ]
              }
            ],
            "max_tokens": 1000
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        response_data = response.json()

        new_filename = response_data.get('choices', [{}])[0].get('message', {}).get('content')

        os.rename(original_path, os.path.join(folder_path, new_filename))

        #print(f"old filename: {filename} - new filename: {new_filename}")
        #print(f"resizepath: {resized_path}")


        if resized:
            os.remove(resized_path)
