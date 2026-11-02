
import cv2
from pathlib import Path

# Read input image
image_path = Path(__file__).resolve().parent / "virat.jpg"
image = cv2.imread(str(image_path))

if image is None:
    print("Error: Image not found!")
    print("Check image path:", image_path)

else:
    # Get original image dimensions
    height, width = image.shape[:2]

    print("Original Size:", width, "x", height)

    # Resize image to bigger size (2x)
    bigger = cv2.resize(
        image, None, fx=2, fy=2,
        interpolation=cv2.INTER_LINEAR
    )

    # Resize image to smaller size (0.5x)
    smaller = cv2.resize(
        image, None, fx=0.5, fy=0.5,
        interpolation=cv2.INTER_AREA
    )

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)

    # Print resized dimensions
    print("Bigger Size:", bigger.shape[1], "x", bigger.shape[0])
    print("Smaller Size:", smaller.shape[1], "x", smaller.shape[0])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Image scaling completed successfully.")
