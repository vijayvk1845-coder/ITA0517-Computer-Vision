
import cv2

# Read the input image
image = cv2.imread("virat.jpg")

# Check whether image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Display original image
    cv2.imshow("Original Image", image)

    # Display edge image
    cv2.imshow("Canny Edge Image", edges)

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
