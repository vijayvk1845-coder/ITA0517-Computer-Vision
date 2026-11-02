
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

# Convert to binary image
_, binary = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

# Create a structuring element
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT, (5, 5)
)

# Apply erosion
eroded = cv2.erode(binary, kernel, iterations=1)

# Save output
cv2.imwrite("eroded_image.jpg", eroded)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary)
cv2.imshow("Eroded Image", eroded)

print("Erosion operation completed.")
print("Saved: eroded_image.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()
