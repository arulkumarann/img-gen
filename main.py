import torch
from diffusers import AutoPipelineForImage2Image
from diffusers.utils import make_image_grid, load_image
from PIL import Image
import requests
from io import BytesIO
import os

class ImageEditor:
    def __init__(self, model_name="stable-diffusion-v1-5/stable-diffusion-v1-5"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.pipeline = AutoPipelineForImage2Image.from_pretrained(
            model_name, torch_dtype=torch.float16, variant="fp16", use_safetensors=True
        )
        self.pipeline.enable_model_cpu_offload()
        print("Model Loaded Successfully.")

    def load_image_from_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content)).convert("RGB")
        else:
            raise ValueError("Failed to load image from URL.")

    def load_image_from_file(self, file_path):
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return Image.open(file_path).convert("RGB")
        else:
            raise ValueError("Invalid file path. Please provide a valid image file.")

    def edit_image(self, init_image, prompt):
        print(f"Generating image with prompt: {prompt}")
        return self.pipeline(prompt, image=init_image).images[0]

    def save_image(self, image, filename):
        image.save(filename)
        print(f"Image saved as {filename}")

    def create_image_grid(self, images, filename="image_grid.png"):
        grid = make_image_grid(images, rows=1, cols=len(images))
        grid.save(filename)
        print(f"Grid saved as {filename}")


def main():
    choice = input("Do you want to use an image from URL or local file? (url/file): ").strip().lower()
    editor = ImageEditor()
    
    if choice == "url":
        url = input("Enter image URL: ")
        init_image = editor.load_image_from_url(url)
    elif choice == "file":
        file_path = input("Enter local file path: ")
        init_image = editor.load_image_from_file(file_path)
    else:
        print("Invalid choice. Exiting.")
        return
    
    prompt = input("Enter your modification prompt: ")
    edited_image = editor.edit_image(init_image, prompt)
    
    editor.save_image(edited_image, "generated_image.png")
    editor.create_image_grid([init_image, edited_image])
    
    print("Process completed successfully!")
    print("Exiting program...")

if __name__ == "__main__":
    main()
