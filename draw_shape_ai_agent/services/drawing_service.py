from PIL import Image, ImageDraw 

class DrawingService:
    def __init__(self, w : int, h : int):
        self.img = Image.new("RGB", (w, h), color = "white")
        self.draw = ImageDraw.Draw(self.img)

    def drawRectangle(self, left : int, right: int, top : int, bottom: int, fillColor : str, outlineColor : str):
        self.draw.rectangle([left, right, top, bottom], fill= fillColor, outlineColor = outlineColor, width=3)