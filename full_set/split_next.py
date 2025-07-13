import os
from PIL import Image


def split_image(
    image_path: str, columns: int, rows: int, output_dir="split", start=0, skip=0
):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Compute size of each sub-image
    sub_width = width // columns
    sub_height = height // rows

    # Make output directory
    os.makedirs(output_dir, exist_ok=True)

    # Loop over grid and save each tile
    count = start
    save_list = []
    for row in range(rows):
        for col in range(columns):
            left = col * sub_width
            upper = row * sub_height
            right = left + sub_width
            lower = upper + sub_height
            tile = img.crop((left, upper, right, lower))
            save_list.append((tile, f"{count}.png"))
            count += 1

    for tile, filename in save_list[:-skip] if skip > 0 else save_list:
        tile.save(os.path.join(output_dir, filename))

    print(f"Saved {image_path} images to '{output_dir}'.")


split_image("6.jpg", columns=8, rows=10, output_dir="split", start=4048, skip=3)
split_image("7.jpg", columns=15, rows=15, output_dir="split", start=4125, skip=0)
split_image(
    "8.jpg", columns=15, rows=15, output_dir="split", start=4125 + 1 * 15 * 15, skip=0
)
split_image(
    "9.jpg", columns=15, rows=15, output_dir="split", start=4125 + 2 * 15 * 15, skip=0
)
split_image(
    "10.jpg", columns=15, rows=15, output_dir="split", start=4125 + 3 * 15 * 15, skip=0
)
split_image(
    "11.jpg", columns=15, rows=15, output_dir="split", start=4125 + 4 * 15 * 15, skip=0
)
split_image(
    "12.jpg", columns=15, rows=15, output_dir="split", start=4125 + 5 * 15 * 15, skip=0
)
split_image(
    "13.jpg", columns=15, rows=15, output_dir="split", start=4125 + 6 * 15 * 15, skip=0
)
split_image(
    "14.jpg", columns=15, rows=15, output_dir="split", start=4125 + 7 * 15 * 15, skip=0
)
split_image(
    "15.jpg",
    columns=15,
    rows=15,
    output_dir="split",
    start=4125 + 8 * 15 * 15,
    skip=12 * 15,
)
