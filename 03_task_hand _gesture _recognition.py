import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time

# Global variables for results
detection_result = None

def print_result(result, output_image, timestamp_ms):
    global detection_result
    detection_result = result

# Initialize MediaPipe Hand Landmarker
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='hand_landmarker.task'),
    running_mode=VisionRunningMode.LIVE_STREAM,
    num_hands=1,
    min_hand_detection_confidence=0.7,
    result_callback=print_result)

landmarker = HandLandmarker.create_from_options(options)

# Function to classify gesture based on landmarks
def classify_gesture(landmarks):
    # Landmarks are normalized 0-1
    # Thumb tip: 4, IP: 3
    # Index tip: 8, PIP: 6
    # etc.

    # Assuming hand is oriented with thumb left, fingers up
    # For thumbs up: thumb extended, others curled
    thumb_extended = landmarks[4].y < landmarks[3].y
    index_extended = landmarks[8].y < landmarks[6].y
    middle_extended = landmarks[12].y < landmarks[10].y
    ring_extended = landmarks[16].y < landmarks[14].y
    pinky_extended = landmarks[20].y < landmarks[18].y

    if thumb_extended and not index_extended and not middle_extended and not ring_extended and not pinky_extended:
        return "thumbs_up"
    elif not thumb_extended and not index_extended and not middle_extended and not ring_extended and not pinky_extended:
        return "fist"
    elif thumb_extended and index_extended and middle_extended and ring_extended and pinky_extended:
        return "open_palm"
    else:
        return "unknown"

# Function to map gesture to action
def gesture_to_action(gesture):
    actions = {
        "thumbs_up": "Increase Volume",
        "fist": "Play/Pause",
        "open_palm": "Decrease Volume",
        "unknown": "No Action"
    }
    return actions.get(gesture, "No Action")

# Main function
def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Starting Hand Gesture Recognition. Press 'q' to quit.")

    frame_timestamp_ms = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally for a mirror effect
        frame = cv2.flip(frame, 1)

        # Convert to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create MediaPipe Image
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        # Detect
        landmarker.detect_async(mp_image, frame_timestamp_ms)
        frame_timestamp_ms += 33  # approx 30fps

        gesture = "unknown"
        action = "No Action"

        if detection_result and detection_result.hand_landmarks:
            for hand_landmarks in detection_result.hand_landmarks:
                # Draw landmarks
                for landmark in hand_landmarks:
                    x = int(landmark.x * frame.shape[1])
                    y = int(landmark.y * frame.shape[0])
                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

                # Classify gesture
                gesture = classify_gesture(hand_landmarks)

                # Get action
                action = gesture_to_action(gesture)

                # Display gesture and action on frame
                cv2.putText(frame, f"Gesture: {gesture}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, f"Action: {action}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('Hand Gesture Recognition', frame)

        # Break on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    landmarker.close()

if __name__ == "__main__":
    main()