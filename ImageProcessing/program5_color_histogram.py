
import cv2
import matplotlib.pyplot as plt

# Function to analyze the color histogram
def analyze_histogram(image):
    colors = ('b', 'g', 'r')
    labels = ('Blue', 'Green', 'Red')

    plt.figure(figsize=(10, 5))

    # Calculate histogram for each color channel
    for channel, color, label in zip(range(3), colors, labels):
        hist = cv2.calcHist(
            [image], [channel], None, [256], [0, 256]
        )

        plt.plot(hist, color=color, label=label)

    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity (0-255)")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# Read the input image
image = cv2.imread("virat.jpg")

# Check image
if image is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully.")

    # Analyze histogram
    analyze_histogram(image)
