
import cv2
from pathlib import Path

# Step 1: Read the input image
image_path = Path(__file__).resolve().parent / "virat.jpg"
image = cv2.imread(str(image_path))

# Step 2: Check whether image is loaded
if image is None:
    print("Error: Image not found!")
    print("Check image path:", image_path)

else:
    # Step 3: Rotate image 270 degrees clockwise
    rotated = cv2.rotate(
        image,
        cv2.ROTATE_90_COUNTERCLOCKWISE
    )

    # Step 4: Display original and rotated images
    cv2.imshow("Original Image", image)
    cv2.imshow("270 Degree Clockwise Rotation", rotated)

    # Step 5: Print image dimensions
    print("Original Size:", image.shape[1], "x", image.shape[0])
    print("Rotated Size:", rotated.shape[1], "x", rotated.shape[0])

    # Step 6: Save rotated image
    output_path = Path(__file__).resolve().parent / "rotated_270.jpg"
    cv2.imwrite(str(output_path), rotated)

    # Step 7: Wait and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("270 degree clockwise rotation completed successfully.")
    print("Saved image:", output_path)
