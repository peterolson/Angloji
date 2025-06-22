from PIL import Image
import numpy as np
from glob import glob


def preprocess_image(path, size=(64, 64), threshold=128):
    # Load and convert to grayscale
    img = Image.open(path).convert("L")

    # Binarize (black/white)
    img = img.point(lambda p: 0 if p > threshold else 255).convert("1")  # type: ignore

    # Get bounding box of black pixels
    bbox = img.getbbox()
    if not bbox:
        raise ValueError("No black pixels found")

    # Crop to bounding box and resize
    cropped = img.crop(bbox).resize(size)

    # Convert to binary numpy array: 0 (white) or 1 (black)
    return np.array(cropped, dtype=np.uint8)


print("Preprocessing images...")
preprocessed_images = dict()
for img_path in glob("full_set/split/*.png"):
    preprocessed_images[img_path] = preprocess_image(img_path)
print("Preprocessing complete.")


def find_character_id(img_path):
    arr1 = preprocess_image(img_path)

    least_diff = 100
    print(f"Processing {img_path}...")
    best_match: str = ""
    for i, img2_path in enumerate(preprocessed_images.keys()):
        arr2 = preprocessed_images[img2_path]
        diff = np.sum(arr1 != arr2)
        total = arr1.size
        diff = 100.0 * diff / total
        if diff < least_diff:
            least_diff = diff
            best_match = img2_path

    char_id = best_match.split("\\")[-1].split(".")[0]
    return char_id, least_diff


# get all of the images in the posts/split directory

data = []
for img_path in glob("posts/split/*.png"):
    post_char_id = img_path.split("\\")[-1].split(".")[0]
    char_id, least_diff = find_character_id(img_path)
    data.append((post_char_id, char_id, least_diff))

# export the data to a CSV file
import csv

with open("similarity_results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Post Character ID", "Full Set Character ID", "Difference (%)"])
    for row in data:
        writer.writerow(row)
