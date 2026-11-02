
import cv2
from pathlib import Path

# Step 1: Read the original image
folder = Path(__file__).resolve().parent
image_path = folder / "virat.jpg"

image = cv2.imread(str(image_path))

# Step 2: Check whether image is loaded
if image is None:
    print("Error: Image not found!")
    print("Check image path:", image_path)

else:
    # Step 3: Copy the original image
    watermarked = image.copy()

    # Step 4: Define watermark text
    watermark = "VIJAY"

    # Step 5: Get image dimensions
    height, width = image.shape[:2]

    # Step 6: Define font and position
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = max(0.5, width / 1000)
    thickness = 2

    # Place watermark near bottom-right corner
    text_size, baseline = cv2.getTextSize(
        watermark, font, font_scale, thickness
    )

    x = max(0, width - text_size[0] - 20)
    y = max(text_size[1], height - 20)

    # Step 7: Add a subtle dark outline
    cv2.putText(
        watermarked, watermark, (x, y),
        font, font_scale, (0, 0, 0),
        thickness + 2, cv2.LINE_AA
    )

    # Step 8: Add white watermark text
    cv2.putText(
        watermarked, watermark, (x, y),
        font, font_scale, (255, 255, 255),
        thickness, cv2.LINE_AA
    )

    # Step 9: Display original and watermarked images
    cv2.imshow("Original Image", image)
    cv2.imshow("Watermarked Image", watermarked)

    # Step 10: Save the result
    output_path = folder / "watermarked_image.jpg"
    success = cv2.imwrite(str(output_path), watermarked)

    # Step 11: Wait and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if success:
        print("Watermark added successfully.")
        print("Saved image:", output_path)
    else:
        print("Error: Could not save output image.")
