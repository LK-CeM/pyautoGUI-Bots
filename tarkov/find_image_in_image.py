# Import relevant libraries
import os
import cv2
import numpy as np
import pyautogui as pag


count_dic = {}
# Function to load images from a folder
def load_images_from_folder(folder_path):
    image_list = []

    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)
            if image is not None:
                image_list.append(image)

    return image_list

# Define the folder path
image_folder = 'imgs/'
items_folder = 'items/'

# Load the main image (the one you want to search within)
main_path = os.path.join(image_folder, 'main.png')
main = cv2.imread(main_path)

# Load the image you want to find within the main image
image_to_find_path = os.path.join(image_folder, 'image_to_find.png')
image_to_find = cv2.imread(image_to_find_path)

# Check if image loading was successful
if main is None or image_to_find is None:
    print("Error loading one or both images.")
    exit(1)

# Find the location of the image to find within the main image
result = cv2.matchTemplate(main, image_to_find, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Get the dimensions of the image to find
w, h = image_to_find.shape[1], image_to_find.shape[0]

# If a match is found, paint the pixels
if max_val > 0.8:
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(main, top_left, bottom_right, (0, 0, 255), -1)  # Fill with red

    # Define grid parameters with a grid size of 14x14
    grid_size = 14
    cell_width = 58  # Adjusted to match the grid size
    cell_height = 58  # Adjusted to match the grid size

    # Calculate the bottom left corner of the found image
    bottom_left_corner = (top_left[0], top_left[1] + h + 2)

    # Draw the red grid
    for i in range(grid_size):
        for j in range(grid_size):
            x1 = bottom_left_corner[0] + j * cell_width
            y1 = bottom_left_corner[1] + i * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            cv2.rectangle(main, (x1, y1), (x2, y2), (0, 0, 255), 1)  # Red grid lines

    # Display the main image with the grid
    cv2.imshow('Modified Image with Grid', main)
    cv2.destroyAllWindows()

# Assuming you have a list of item templates (item_images) and a dictionary to keep track of counts
item_images = load_images_from_folder(items_folder)

for i in range(grid_size):
    for j in range(grid_size):
        x1 = bottom_left_corner[0] + j * cell_width
        y1 = bottom_left_corner[1] + i * cell_height
        x2 = x1 + cell_width
        y2 = y1 + cell_height
        cell_content = main[y1:y2, x1:x2]

        # Check if cell_content matches any of the item templates
        match_found = False
        for index, img in enumerate(item_images):
            if pag.locate(img, cell_content, grayscale=False, confidence=0.85) is not None:
                if index in count_dic:
                    count_dic[index] += 1
                else:
                    count_dic[index] = 0
                match_found = True
                break

        if not match_found:
            item_image_path = os.path.join(items_folder, f'Item_{len(item_images) + 1}.png')
            item_images.append(cell_content)
            count_dic[len(item_images)] = 0
            cv2.imwrite(item_image_path, cell_content)

# Sort and print dictionary items by value
sorted_count_dic = dict(sorted(count_dic.items(), key=lambda item: item[1], reverse=True))
for item, count in sorted_count_dic.items():
    if count > 0:
        print(f"Item: {item}, Count: {count}")

# Display the cell content of the top 3 matches by count
top_3_items = list(sorted_count_dic.keys())[:3]

for item in top_3_items:
    item = int(item)
    cv2.imshow(f"Top Match Item {item}", item_images[item])

cv2.destroyAllWindows()
# Combine the top 3 items into one image
top_3_images = [item_images[item] for item in top_3_items]
combined_image = np.hstack(top_3_images)  # Horizontal stacking

# Display the combined image
cv2.imshow("Top 3 Items Combined", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()