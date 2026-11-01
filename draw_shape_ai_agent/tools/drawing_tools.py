from services.drawing_service import DrawingService
from typing import List 
from models.point import Point 

ds = DrawingService(w = 500, h = 500)

def drawRectangle(left : int, top : int, right: int, bottom : int, fillColor : str, outlineColor : str):
    print(f"Calling drawRectangle tool {left} {top} {right} {bottom}")
    return ds.drawRectangle(left=left, top=top, right=right, bottom=bottom, fillColor=fillColor, outlineColor=outlineColor)

def drawLine(startX : int, startY : int, endX : int, endY : int, color : str):
    print(f"Calling drawLine tool from ({startX}, {startY}) to ({endX}, {endY}) with {color}")
    return ds.drawLine(x1 = startX, x2 = endX, y1 = startY, y2 = endY, color = color)

def drawArc(left : int, top : int, right: int, bottom: int, start: int, end : int, color : str):
    print(f"Calling drawArc tool {left} {top} {right} {bottom} {color} with {start} deg and {end}deg")
    return ds.drawArc(left = left, top = top, right = right, bottom=bottom, start = start, end = end, color = color)

def drawCircle(centerX : int, centerY : int, radius : int, fillColor : str, outlineColor : str):
    print(f"Calling drawCircle tool at ({centerX}, {centerY}) with {radius}")
    return ds.drawCircle(centerX= centerX, centerY=centerY, radius=radius, fillColor=fillColor, outlineColor=outlineColor)

def drawPoints(points : List[Point], color : str):
    print(f"Calling drawPoints with {len(points)} size")
    return ds.drawPoints(points=points, color=color)

def drawPolygon(polygonPoints : List[Point], fillColor : str, outlineColor : str, outlineWidth : int = 3):
    print(f"Calling drawPolygons tool with {len(polygonPoints)}")
    return ds.drawPolygons(polygonPoints=polygonPoints, fillColor=fillColor, outlineColor=outlineColor, outlineWidth=outlineWidth)

def saveImage(fileName : str):
    print(f"Calling saveImage tool with {fileName}")
    return ds.save(fileName=fileName)

def writeHTML(htmlStr : str, fileName : str):
    print(f"calling writeHTML tool to {fileName}")
    with open(fileName, "w") as f:
        f.write(htmlStr)
    return {
        "status": "success",
        "message": f"html written to {fileName}"
    }

def getTools():
    tools = []
    tools.append(drawRectangle)
    tools.append(drawLine)
    tools.append(drawArc)
    tools.append(drawCircle)
    tools.append(drawPoints)
    tools.append(drawPolygon)
    tools.append(saveImage)
    tools.append(writeHTML)
    return tools 