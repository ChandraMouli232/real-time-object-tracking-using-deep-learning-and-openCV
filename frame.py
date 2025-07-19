import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

def detect_and_draw_box(img, confidence=0.6):
    bbox, label, conf = cv.detect_common_objects(img, confidence=confidence)
    output_image = draw_bbox(img, bbox, label, conf)
    return output_image

# Capture video from webcam
vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    if not ret:
        break
    output_frame = detect_and_draw_box(frame)
    cv2.imshow('frame', output_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

def detect_and_draw_box(img, confidence=0.6):
    bbox, label, conf = cv.detect_common_objects(img, confidence=confidence)
    output_image = draw_bbox(img, bbox, label, conf)
    return output_image

# Capture video from webcam
vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    if not ret:
        break
    output_frame = detect_and_draw_box(frame)
    cv2.imshow('frame', output_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()