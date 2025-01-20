import cv2


def detect_people(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Nie można załadować obrazu: {image_path}")
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    boxes, _ = hog.detectMultiScale(image, winStride=(8, 8))
    return len(boxes)
