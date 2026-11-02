
import cv2
from pathlib import Path

# Read input image
image_path = Path(__file__).resolve().parent / "virat.jpg"
image = cv2.imread(str(image_path))

if image is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert grayscale image to binary
_, binary = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

# Create a structuring element
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT, (5, 5)
)

# Apply dilation
dilated = cv2.dilate(binary, kernel, iterations=1)

# Save the output image
cv2.imwrite("dilated_image.jpg", dilated)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary)
cv2.imshow("Dilated Image", dilated)

print("Dilation operation completed.")
print("Saved: dilated_image.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()
