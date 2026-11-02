
import cv2
import numpy as np
from pathlib import Path

# Step 1: Get the image path
image_path = Path(__file__).resolve().parent / "virat.jpg"

# Step 2: Read the input image
image = cv2.imread(str(image_path))

# Step 3: Check whether image is loaded
if image is None:
    print("Error: Image not found!")
    print("Expected image location:", image_path)
else:
    # Step 4: Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 5: Convert grayscale image into binary
    _, binary = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    # Step 6: Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Step 7: Apply dilation
    dilated = cv2.dilate(
        binary,
        kernel,
        iterations=1
    )

    # Step 8: Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Dilated Image", dilated)

    # Step 9: Wait for a key press
    cv2.waitKey(0)

    # Step 10: Close all windows
    cv2.destroyAllWindows()

    print("Image dilation completed successfully.")
