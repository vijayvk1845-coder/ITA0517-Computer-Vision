
import cv2

# Read the input image
image = cv2.imread("virat.jpg")

if image is None:
    print("Error: Image not found!")
else:
    # Convert color image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)

    # Display original grayscale image
    cv2.imshow("Original Grayscale Image", gray)

    # Display equalized image
    cv2.imshow("Histogram Equalized Image", equalized)

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
