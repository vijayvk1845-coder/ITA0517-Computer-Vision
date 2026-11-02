
import cv2
import numpy as np
from pathlib import Path

# Read the input image
image_path = Path(__file__).resolve().parent / "virat.jpg"
image = cv2.imread(str(image_path))

if image is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Select the central ROI
x1 = width // 4
y1 = height // 4
x2 = 3 * width // 4
y2 = 3 * height // 4

# Crop the selected region
roi = image[y1:y2, x1:x2]

# Copy the ROI
copied_roi = roi.copy()

# Create a blank canvas
canvas = np.zeros_like(image)

# Paste the copied ROI at the center
roi_h, roi_w = copied_roi.shape[:2]
paste_x = (width - roi_w) // 2
paste_y = (height - roi_h) // 2

canvas[paste_y:paste_y + roi_h,
       paste_x:paste_x + roi_w] = copied_roi

# Save output images
cv2.imwrite("cropped_roi.jpg", roi)
cv2.imwrite("pasted_roi.jpg", canvas)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Cropped ROI", roi)
cv2.imshow("Pasted ROI", canvas)

print("ROI cropping, copying and pasting completed.")
print("Saved: cropped_roi.jpg and pasted_roi.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()
