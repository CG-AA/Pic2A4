from PIL import Image
import os

# find all images in the current directory
for file in os.listdir('.'):
    if file.endswith('.jpg'):
        img = Image.open(file)

        # define the size of A4 paper in pixels
        dpi = 300
        a4_width_px = int(210 / 25.4 * dpi)  # 210 mm
        a4_height_px = int(297 / 25.4 * dpi) # 297 mm

        # calculate the number of slices
        img_width, img_height = img.size
        num_slices = (img_height + a4_height_px - 1) // a4_height_px  # round up

        # slice the image
        for i in range(num_slices):
            # calculate the box area
            top = i * a4_height_px
            bottom = min((i + 1) * a4_height_px, img_height)
            box = (0, top, img_width, bottom)

            # crop the image&save
            slice_img = img.crop(box)
            slice_img.save(f'output_page_{i + 1}.jpg', 'JPEG')