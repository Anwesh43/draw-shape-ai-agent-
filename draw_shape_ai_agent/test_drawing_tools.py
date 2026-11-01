from tools.drawing_tools import drawPoints, drawPolygons, drawCircle, drawRectangle, drawArc, drawLine, saveImage
import time 

if __name__ == "__main__":
    drawCircle(centerX = 200, centerY=200, radius = 50, fillColor="green", outlineColor="black")
    time.sleep(1)
    drawRectangle(left = 50, top = 50, right = 100, bottom = 100, fillColor="red", outlineColor="black")
    time.sleep(1)
    saveImage("test_drawing.png")