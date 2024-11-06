import os
from PIL import Image

for file in os.listdir('.'):
    if file.endswith('.jpg'):
        print(f"Processing file: {file}")
        img = Image.open(file)

        # A4 properties
        A4_RATIO = 297 / 210  # height/width ratio of A4
        dpi = 300
        a4_width_px = int(210 / 25.4 * dpi)
        a4_height_px = int(297 / 25.4 * dpi)

        # Calculate scaled dimensions maintaining aspect ratio
        img_width, img_height = img.size
        scaled_width = a4_width_px
        scaled_height = int(scaled_width * (img_height / img_width))
        
        # Resize image to match A4 width
        img = img.resize((scaled_width, scaled_height), Image.Resampling.LANCZOS)
        
        print(f"Scaled dimensions: {scaled_width}x{scaled_height}")
        
        # Calculate slices based on A4 height
        num_slices = (scaled_height + a4_height_px - 1) // a4_height_px
        print(f"Number of slices: {num_slices}")

        # Slice the image
        for i in range(num_slices):
            top = i * a4_height_px
            bottom = min((i + 1) * a4_height_px, scaled_height)
            box = (0, top, scaled_width, bottom)
            
            slice_img = img.crop(box)
            output_filename = f'output_page_{i + 1}.jpg'
            slice_img.save(output_filename, 'JPEG')
            print(f"Saved slice {i + 1} as {output_filename}")