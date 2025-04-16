import cv2
import mediapipe as mp

class ActionAnalyzer:
    
    def __init__(self):
        file = input("Enter file name: ")
        # Initialize Video Capture
        self.cap = cv2.VideoCapture(file)  # Replace with your video path
        # Initialize MediaPipe Pose
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()
        self.mp_drawing = mp.solutions.drawing_utils  # For drawing lines
        self.mp_drawing_styles = mp.solutions.drawing_styles  # For better styling

    def action(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break  # Exit loop when video ends

            # Resize the frame for faster processing
            frame = cv2.resize(frame, (640, 480))  # Resize to 640x480

            # Convert frame to RGB for MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process frame with MediaPipe Pose
            results = self.pose.process(rgb_frame)

            if results.pose_landmarks:
                # Draw the stick figure (pose landmarks + connections)
                self.mp_drawing.draw_landmarks(
                    frame,
                    results.pose_landmarks,
                    self.mp_pose.POSE_CONNECTIONS,  # Connect joints to form the stick figure
                    landmark_drawing_spec=self.mp_drawing_styles.get_default_pose_landmarks_style()
                )

            # Display Frames
            cv2.imshow('Stick Figure Motion Tracking', frame)

            # Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Cleanup
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    Analyze = ActionAnalyzer()
    Analyze.action()