# Image Editor

A simple Python application that uses Stable Diffusion to modify images based on text prompts. This tool allows you to transform existing images using AI-generated modifications.

## Features

- Load images from URLs or local files
- Edit images using natural language prompts
- Save generated images
- Create side-by-side comparisons of original and edited images

## Requirements

- Python 3.8+
- CUDA-compatible GPU (recommended) for faster processing
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application using:

```bash
python main.py
```

Follow the prompts in the terminal:

1. Choose whether to use an image from a URL or a local file
2. Provide the URL or file path
3. Enter your modification prompt (e.g., "convert to oil painting", "make it winter themed")
4. The application will generate and save:
   - The modified image as `generated_image.png`
   - A side-by-side comparison as `image_grid.png`

## Example

```
Do you want to use an image from URL or local file? (url/file): url
Enter image URL: https://example.com/image.jpg
Enter your modification prompt: convert to watercolor style
Generating image with prompt: convert to watercolor style
Image saved as generated_image.png
Grid saved as image_grid.png
Process completed successfully!
```

## How It Works

The application uses Hugging Face's Diffusers library and the Stable Diffusion image-to-image pipeline. It loads the pre-trained model, processes your input image with the given prompt, and generates a modified version while preserving the overall structure of the original image.

## Customization

You can modify the code to:
- Use different Stable Diffusion models by changing the `model_name` parameter
- Adjust image generation parameters
- Implement batch processing for multiple images