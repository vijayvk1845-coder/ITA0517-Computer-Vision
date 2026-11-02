
from pathlib import Path
from ultralytics import YOLO
import cv2

# Get project folder
folder = Path(__file__).resolve().parent

# Input image
image_path = folder / "virat.jpg"

if not image_path.exists():
    print("Error: Image not found!")
    exit()

# Load pretrained YOLO model
# Model downloads automatically when needed
model = YOLO("yolo11n.pt")

# Perform object detection
results = model.predict(
    source=str(image_path),
    conf=0.25,
    save=False,
    verbose=False
)

# Read original image
image = cv2.imread(str(image_path))

# Count detected objects
clock_count = 0

for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        label = model.names[class_id]
        confidence = float(box.conf[0])

        # COCO model supports clock, not wristwatch
        if label == "clock":
            x1, y1, x2, y2 = map(
                int, box.xyxy[0].tolist()
            )

            cv2.rectangle(
                image, (x1, y1), (x2, y2),
                (0, 255, 0), 2
            )

            cv2.putText(
                image,
                f"{label}: {confidence:.2f}",
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 255, 0), 2
            )

            clock_count += 1

# Save result
output_path = folder / "watch_recognition_output.jpg"
cv2.imwrite(str(output_path), image)

print("Object recognition completed.")
print("Clock detections:", clock_count)
print("Saved:", output_path.name)

# Display result
cv2.imshow("Recognition Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
