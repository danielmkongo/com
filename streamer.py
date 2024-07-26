import cv2
import socket
import numpy as np

# Initialize UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('45.79.53.206', 5555)

# OpenCV video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 15)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Serialize frame
    encoded, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
    udp_socket.sendto(buffer.tobytes(), server_address)

cap.release()
udp_socket.close()
cv2.destroyAllWindows()
