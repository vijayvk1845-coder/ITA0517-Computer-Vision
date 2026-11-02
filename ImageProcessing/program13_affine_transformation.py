
import cv2
import numpy as np
from pathlib import Path

# Step 1: Read the input image
image_path = Path(__file__).resolve().parent / "virat.jpg"
image = cv2.imread(str(image_path))

if image is None:
    print("Error: Image not found!")
    print("Check image path:", image_path)

else:
    # Step 2: Get image dimensions
    height, width = image.shape[:2]

    # Step 3: Define three points in original image
    source_points = np.float32([
        [0, 0],
        [width - 1, 0],
        [0, height - 1]
    ])

    # Step 4: Define corresponding destination points
    destination_points = np.float32([
        [50, 50],
        [width - 50, 50],
        [100, height - 50]
    ])

    # Step 5: Calculate affine transformation matrix
    matrix = cv2.getAffineTransform(
        source_points,
        destination_points
    )

    # Step 6: Apply affine transformation
    transformed = cv2.warpAffine(
        image,
        matrix,
        (width, height)
    )

    # Step 7: Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Affine Transformed Image", transformed)

    # Step 8: Save transformed image
    output_path = (
        Path(__file__).resolve().parent /
        "affine_transformed.jpg"
    )

    cv2.imwrite(str(output_path), transformed)

    # Step 9: Wait and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Affine transformation completed successfully.")
    print("Saved image:", output_path)
