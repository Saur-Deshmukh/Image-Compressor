# Image-Compressor
This Python script leverages the Tinify API to compress images within a designated folder, minimizing their file size while preserving their quality.
## Features
* Compresses images using the Tinify API.
* Compresses all the images present in the folder.
* Generates optimized images in the same folder.
## Setup

1. **Clone the repository**

2. **Tinify API Key:**
   - Obtain an API key from [Tinify](https://tinypng.com/developers) and replace the placeholder in the script with your key:

     ```python
     tinify.key = 'your_tinify_api_key'
     ```

3. **Installation:**
   - Install the Tinify Python package:

     ```bash
     pip install tinify
     ```
## Run the Script
Execute the script to compress images:
    ```bash
    python main.py
    ```
## Notes
* Please note that the script and the images shold be in the same folder.
* The optimized image will end with '-compressed-resized'.
## Contributing
Feel free to contribute to this project by opening issues or creating pull requests.
