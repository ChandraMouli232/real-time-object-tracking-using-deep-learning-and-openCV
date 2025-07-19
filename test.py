import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
def detect_and_draw_box(img, model="yolov3.weights", confidence=0.6):
    output_image = None
    # img_filepath = "images/"+filename
    # img = cv2.imread(img_filepath)
    # cv2.imshow('img',img)
    # cv2.waitKey(0)
    bbox, label, conf = cv.detect_common_objects(img, model=model)
    # print(f"========================nImage processed: {filename}n")
    for l, c in zip(label, conf):
        print(f"Detected object: {l} with confidence level of {c}n")

    bbox1 = []
    label1 = []
    conf1 = []

    for b, l, c in zip(bbox, label, conf):
        if l == 'person':
           bbox1.append(b)
           label1.append(l)
           conf1.append(c)
        continue
    output_image = draw_bbox(img, bbox1, label1, conf1)
    # cv2.imwrite('images_with_boxes/'+filename, output_image)
    # d = {'label': label, 'conf': conf}
    return output_image

vid = cv2.VideoCapture(0)
while(True):      
    ret, frame = vid.read()
    out = detect_and_draw_box(frame)
    cv2.imshow('frame', out)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()