import edgeimpulse_linux
import cv2
import numpy as np
model = edgeimpulse_linux.EimModel("path_to_your_model.eim")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
print("Error: Could not access the camera.")
exit()
print("Running Inference...")
while True:
ret, frame = cap.read()
if not ret:
print("Error: Failed to capture image.")
Break
normalized_frame = resized_frame.astype(np.float32) / 255.0
result = model.classify(normalized_frame)
print(f"Predicted Class: {result['label']} with Confidence: {result['confidence']}")
cv2.putText(frame, f"Class: {result['label']} ({result['confidence']:.2f})",
(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imshow("Live Object Detection", frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
break
cap.release()
cv2.destroyAllWindows()
