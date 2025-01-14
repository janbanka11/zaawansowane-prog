from PIL import Image
import pytesseract

def read_text_from_image(image_path):
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text

image_file = "test.png"
result = read_text_from_image(image_file)
print(result)
print("\n===============\n")
image_file = "book-cover.jpg"
result = read_text_from_image(image_file)
print(result)
