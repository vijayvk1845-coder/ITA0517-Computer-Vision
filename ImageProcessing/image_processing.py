import cv2

# Read the image
image = cv2.imread("virat.jpg")

# Check whether image was loaded
if image is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully")

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display original image
    cv2.imshow("Original Image", image)

    # Display grayscale image
    cv2.imshow("Grayscale Image", gray_image)

    # Save grayscale image
    cv2.imwrite("gray_image.jpg", gray_image)

    print("Grayscale image saved successfully!")

    # Wait for a key
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()