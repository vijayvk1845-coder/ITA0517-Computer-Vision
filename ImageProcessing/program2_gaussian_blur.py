
import cv2

# Read the input image
image = cv2.imread("virat.jpg")

# Check image
if image is None:
    print("Error: Image not found!")
else:
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Display original image
    cv2.imshow("Original Image", image)

    # Display blurred image
    cv2.imshow("Gaussian Blur Image", blurred)

    # Wait for key press
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()
