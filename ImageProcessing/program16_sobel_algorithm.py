
import cv2
from pathlib import Path

# Step 1: Read input image
image_path = Path(__file__).resolve().parent / "virat.jpg"
image = cv2.imread(str(image_path))

# Step 2: Check image
if image is None:
    print("Error: Image not found!")
    print("Check image path:", image_path)

else:
    # Step 3: Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 4: Apply Sobel filter in X direction
    sobel_x = cv2.Sobel(
        gray,
        cv2.CV_64F,
        1, 0,
        ksize=3
    )

    # Step 5: Apply Sobel filter in Y direction
    sobel_y = cv2.Sobel(
        gray,
        cv2.CV_64F,
        0, 1,
        ksize=3
    )

    # Step 6: Calculate gradient magnitude
    magnitude = cv2.magnitude(sobel_x, sobel_y)

    # Step 7: Convert result to 8-bit image
    sobel_output = cv2.convertScaleAbs(magnitude)

    # Step 8: Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Sobel X Filter", cv2.convertScaleAbs(sobel_x))
    cv2.imshow("Sobel Y Filter", cv2.convertScaleAbs(sobel_y))
    cv2.imshow("Sobel Filtered Image", sobel_output)

    # Step 9: Save output
    output_path = (
        Path(__file__).resolve().parent / "sobel_filtered.jpg"
    )
    cv2.imwrite(str(output_path), sobel_output)

    # Step 10: Wait and close
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Sobel filtering completed successfully.")
    print("Saved image:", output_path)
