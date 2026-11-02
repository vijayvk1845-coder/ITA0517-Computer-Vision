
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

# Create a structuring element
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT, (5, 5)
)

# Apply closing operation
closed = cv2.morphologyEx(
    gray, cv2.MORPH_CLOSE, kernel
)

# Apply Black Hat operation
blackhat = cv2.morphologyEx(
    gray, cv2.MORPH_BLACKHAT, kernel
)

# Save output image
cv2.imwrite("blackhat_image.jpg", blackhat)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Closing Image", closed)
cv2.imshow("Black Hat Image", blackhat)

print("Black Hat operation completed.")
print("Saved: blackhat_image.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()
