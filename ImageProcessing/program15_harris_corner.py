
import cv2
import numpy as np
from pathlib import Path

# Step 1: Read the input image
image_path = Path(__file__).resolve().parent / "virat.jpg"
image = cv2.imread(str(image_path))

# Step 2: Check whether image is loaded
if image is None:
    print("Error: Image not found!")
    print("Check image path:", image_path)

else:
    # Step 3: Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 4: Convert image to float32
    gray_float = np.float32(gray)

    # Step 5: Apply Harris Corner Detection
    corners = cv2.cornerHarris(
        gray_float,
        blockSize=2,
        ksize=3,
        k=0.04
    )

    # Step 6: Dilate corner response for visibility
    corners = cv2.dilate(corners, None)

    # Step 7: Mark detected corners
    result = image.copy()
    threshold = 0.01 * corners.max()
    result[corners > threshold] = [0, 0, 255]

    # Step 8: Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Harris Corner Detection", result)

    # Step 9: Save output image
    output_path = (
        Path(__file__).resolve().parent /
        "harris_corners.jpg"
    )
    cv2.imwrite(str(output_path), result)

    # Step 10: Wait and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Harris corner detection completed successfully.")
    print("Saved image:", output_path)
