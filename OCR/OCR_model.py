import easyocr


class OCR_Model:

    def __init__(self):
        self.reader = easyocr.Reader(['ru', 'en'])

    def read_image(self, image):
        text = self.reader.readtext(image, detail=0, paragraph=True)
        return text
