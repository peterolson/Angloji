from PIL import Image
import os


def split_image(image_path, grid_size=30, output_dir="split", offset=0):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Compute size of each sub-image
    sub_width = width // grid_size
    sub_height = height // grid_size

    # Make output directory
    os.makedirs(output_dir, exist_ok=True)

    # Loop over grid and save each tile
    count = offset + 1
    for row in range(grid_size):
        for col in range(grid_size):
            left = col * sub_width
            upper = row * sub_height
            right = left + sub_width
            lower = upper + sub_height
            tile = img.crop((left, upper, right, lower))
            tile.save(os.path.join(output_dir, f"{count:04}.png"))
            count += 1
            if count >= 4048:
                print("Reached maximum tile count of 4048. Stopping.")
                return

    print(f"Saved {count} images to '{output_dir}'.")


# Example usage
for i in range(1, 6):
    split_image(f"{i}.jpg", offset=(i - 1) * 30 * 30)
