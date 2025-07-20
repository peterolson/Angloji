from PIL import Image
import os


def split_image(
    image_path: str, columns: int, rows: int, prefix: str, output_dir="split", skip=0
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
    count = 0
    for row in range(rows):
        for col in range(columns):
            left = col * sub_width
            upper = row * sub_height
            right = left + sub_width
            lower = upper + sub_height
            tile = img.crop((left, upper, right, lower))
            tile.save(
                os.path.join(
                    output_dir, f"{prefix}{convert_index(count, columns, rows) + 1}.png"
                )
            )
            count += 1

    for i in range(skip):
        index = columns * rows - i
        os.remove(os.path.join(output_dir, f"{prefix}{index}.png"))

    print(f"Saved {image_path} images to '{output_dir}'.")


def convert_index(original_index: int, width: int, height: int) -> int:
    row = original_index // width
    col = original_index % width

    from_right = width - 1 - col

    return from_right * height + row


# clear the split directory if it exists
if os.path.exists("split"):
    for file in os.listdir("split"):
        os.remove(os.path.join("split", file))

# Example usage
split_image("1.png", columns=4, rows=5, prefix="p1_")
split_image("2.png", columns=5, rows=4, prefix="p2_")
split_image("3.png", columns=2, rows=2, prefix="p3_")
split_image("4.png", columns=1, rows=2, prefix="p4_")
split_image("5.png", columns=1, rows=2, prefix="p5_")
split_image("6.png", columns=1, rows=3, prefix="p6_")
split_image("phone1.jpg", columns=10, rows=10, prefix="phone1_")
split_image("7.jpg", columns=6, rows=8, prefix="p7_")
split_image("8.jpg", columns=7, rows=7, prefix="p8_", skip=4)
split_image("9.jpg", columns=9, rows=8, prefix="p9_", skip=1)
split_image("10.png", columns=4, rows=7, prefix="p10_", skip=1)
split_image("11.png", columns=4, rows=4, prefix="p11_")
split_image("12.jpg", columns=6, rows=8, prefix="p12_")
split_image("13.jpg", columns=8, rows=8, prefix="p13_", skip=4)
split_image("14.jpg", columns=2, rows=3, prefix="p14_")
split_image("15.jpg", columns=2, rows=3, prefix="p15_")
split_image("16.jpg", columns=2, rows=4, prefix="p16_")
split_image("17.jpg", columns=2, rows=4, prefix="p17_")
split_image("18.jpg", columns=1, rows=3, prefix="p18_")
split_image("19.jpg", columns=3, rows=5, prefix="p19_", skip=2)
