from PIL import Image, ImageDraw 
from typing import List
from models.point import Point 

class DrawingService:
    def __init__(self, w : int, h : int):
        self.img = Image.new("RGB", (w, h), color = "white")
        self.draw = ImageDraw.Draw(self.img)

    def drawRectangle(self, left : int, top : int, right: int, bottom: int, fillColor : str, outlineColor : str):
        self.draw.rectangle([left, top, right, bottom], fill= fillColor, outlineColor = outlineColor, width=3)

    def save(self, fileName : str):
        self.img.save(fileName)
        self.img.show()

    def drawLine(self, x1 : int, y1 : int, x2 : int, y2 : int, color : str):
        self.draw.line((x1, y1, x2, y2), fill = color)

    def drawArc(self, left : int, top : int, right: int, bottom: int, color : str):
        self.draw.arc((left, top, right, bottom), fill = color)

    def drawCircle(self, centerX : int, centerY : int, radius : int, fillColor : str, outlineColor : str):
        self.draw.circle((centerX, centerY), radius, fill = fillColor, outline = outlineColor, width = 2)

    def drawPoints(self, points : List[Point], color : str):
        for point in points:
            self.draw.point((point.x, point.y), fill = color)

    def drawPolygons(self, polygonPoints : List[Point], fillColor : str, outlineColor : str, outlineWidth : int = 3):
        polygonCoordinates = [(polygon.x, polygon.y) for polygon in polygonPoints]
        self.draw.polygon(polygonCoordinates, fill = fillColor, outline = outlineColor, width = outlineWidth)
