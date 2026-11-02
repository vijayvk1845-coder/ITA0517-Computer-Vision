
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

# Apply closing operation
closed = cv2.morphologyEx(
    binary, cv2.MORPH_CLOSE, kernel, iterations=1
)

# Save output image
cv2.imwrite("closing_image.jpg", closed)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary)
cv2.imshow("Closing Image", closed)

print("Closing operation completed.")
print("Saved: closing_image.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()
