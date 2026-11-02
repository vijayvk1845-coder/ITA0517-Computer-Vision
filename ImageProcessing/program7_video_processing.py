
import cv2

# Read the video
cap = cv2.VideoCapture("video.mp4")

# Check video
if not cap.isOpened():
    print("Error: Cannot open video!")
else:
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    # Original frame delay
    delay = max(1, int(1000 / fps))

    def play_video(title, wait_time, skip=1):
        # Start video from beginning
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        print("Playing:", title)

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            cv2.imshow(title, frame)

            # Press Q to stop
            key = cv2.waitKey(wait_time) & 0xFF

            if key == ord('q'):
                return False

            # Skip frames for fast motion
            for _ in range(skip - 1):
                if not cap.grab():
                    break

        return True

    # Normal speed
    if play_video("Normal Speed", delay):
        # Slow motion (approximately half speed)
        if play_video("Slow Motion", delay * 2):
            # Fast motion (approximately double speed)
            play_video("Fast Motion", delay, skip=2)

    cap.release()
    cv2.destroyAllWindows()
    print("Video processing completed.")
