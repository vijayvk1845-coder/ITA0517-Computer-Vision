
import cv2
import numpy as np
from pathlib import Path

# Locate the image in the same folder as this program
image_path = Path(__file__).resolve().parent / "virat.jpg"

# Read image
image = cv2.imread(str(image_path))

if image is None:
    print("Error: Image not found!")
    print("Image path:", image_path)

else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert to binary image
    _, binary = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    # Create 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(
        binary, kernel, iterations=1
    )

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Dilated Image", dilated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Image dilation completed successfully.")
