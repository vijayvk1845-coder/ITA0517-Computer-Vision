
import cv2
import numpy as np

# Read the input image
image = cv2.imread("virat.jpg")

# Check whether image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert grayscale image to binary
    _, binary = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    # Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    eroded = cv2.erode(
        binary, kernel, iterations=1
    )

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Eroded Image", eroded)

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
