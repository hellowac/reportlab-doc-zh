# copyright ReportLab Europe Limited. 2000-2016
# see license.txt for license details
"""
Code to measure the size of, and eventually auto-position, shapes.

The basic philosophy of our framework is that things are explicitly
positioned.  However in some cases one really needs a degree of
auto-positioning, or to write one's own code to position something.
Example "give me a bar chart, legend and title in a drawing size
300x200".  Such a situation one has to take account of the title
string and the length of the words alongside the axis.

This implements a function...

    getBounds(object) -> (x1, y1, x2, y2)

...which tells you the boundng rectangle of any graphic object.
On user nodes, it does this by making it explode itself into
primitives, which can be almost as much work as drawing things.
However, if any object has a getBounds() method (none do yet)
then it will call that instead.  Ideally we would move getBounds
into a method of each widget.

用于测量形状大小并最终自动放置形状的代码。

我们框架的基本理念是明确地定位事物。
但是在某些情况下，确实需要一定程度的自动定位，或者编写自己的代码来定位某些东西。
示例: “给我一张尺寸为300x200的条形图，图例和标题”。
在这种情况下，必须考虑标题字符串和轴旁单词的长度。

这实现了一个功能...

    getBounds(object) -> (x1, y1, x2, y2)

...告诉您任何图形对象的边界矩形。
在用户节点上，它通过使其自身爆炸成图元来实现此目的，而图元几乎可以完成绘制工作。
但是，如果任何对象具有getBounds（）方法（尚无），则它将调用它。
 理想情况下，我们将getBounds移到每个小部件的方法中。
"""

from reportlab.graphics import shapes
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.validators import *
from reportlab.lib.attrmap import *
from reportlab.lib.colors import cyan, magenta
from reportlab.graphics.widgetbase import Widget


#  The functions below would logically be methods of the corresponding
#  objects in due course.  For now, keep them here to avoid complicating
#  our main object model.

# 在适当的时候，下面的函数在逻辑上将是相应对象的方法。
# 现在，将它们保留在此处以避免使我们的主要对象模型复杂化。


def getRectsBounds(rectList):
    xMin, yMin, xMax, yMax = rectList[0]
    for (x1, y1, x2, y2) in rectList[1:]:
        if x1 < xMin:
            xMin = x1
        if x2 > xMax:
            xMax = x2
        if y1 < yMin:
            yMin = y1
        if y2 > yMax:
            yMax = y2
    return (xMin, yMin, xMax, yMax)


def getPointsBounds(pointList):
    """
    Helper function for list of points
    点列表的辅助函数
    """
    xs = []
    ys = []
    first = pointList[0]
    if isinstance(first, (list, tuple)):
        # pairs of things
        for (x, y) in pointList:
            xs.append(x)
            ys.append(y)
    else:
        points = pointList[:]
        while points:
            xs.append(points[0])
            ys.append(points[1])
            points = points[2:]
    return (min(xs), min(ys), max(xs), max(ys))


def getBounds(obj):
    if hasattr(obj, 'getBounds'):
        # this is the preferred "future" solution :-)
        # 这是首选的“未来”解决方案
        return obj.getBounds()
    # else try all the primitive shapes
    # 否则尝试所有原始形状
    elif isinstance(obj, shapes.Line):
        return (obj.x1, obj.y1, obj.x2, obj.y2)
    elif isinstance(obj, shapes.Rect):
        return (obj.x, obj.y, obj.x + obj.width, obj.y + obj.height)
    elif isinstance(obj, shapes.Circle):
        return (obj.cx - obj.r, obj.cy - obj.r, obj.cx + obj.r, obj.cy + obj.r)
    elif isinstance(obj, shapes.Ellipse):
        return (
            obj.cx - obj.rx,
            obj.cy - obj.ry,
            obj.cx + obj.rx,
            obj.cy + obj.ry,
        )
    elif isinstance(obj, shapes.Polygon):
        return getPointsBounds(obj.points)
    elif isinstance(obj, shapes.PolyLine):
        return getPointsBounds(obj.points)
    elif isinstance(obj, shapes.Wedge):
        return getPointsBounds(obj.asPolygon().points)
    elif isinstance(obj, shapes.String):
        w = stringWidth(obj.text, obj.fontName, obj.fontSize)
        x = obj.x
        tA = obj.textAnchor
        if tA != 'start':
            if tA == 'middle':
                x -= 0.5 * w
            elif tA == 'end':
                x -= w
            elif tA == 'numeric':
                x -= shapes.numericXShift(
                    tA, obj.text, w, obj.fontName, obj.fontSize, obj.encoding
                )
        return (x, obj.y - 0.2 * obj.fontSize, x + w, obj.y + obj.fontSize)
    elif isinstance(obj, shapes.Path):
        xs = []
        ys = []
        points = obj.points[:]
        while points:
            xs.append(points[0])
            ys.append(points[1])
            points = points[2:]
        return (min(xs), min(ys), max(xs), max(ys))

    # then groups, which need transformation...
    elif isinstance(obj, shapes.Group):
        # iterate over each thing getting its rect
        if obj.contents:
            b = []
            for elem in obj.contents:
                b.append(getBounds(elem))
            (x1, y1, x2, y2) = getRectsBounds(b)
            trans = obj.transform
            corners = [[x1, y1], [x1, y2], [x2, y1], [x2, y2]]
            newCorners = []
            for corner in corners:
                newCorners.append(shapes.transformPoint(trans, corner))
            return getPointsBounds(newCorners)
        else:
            # empty group needs a sane default; this
            # will happen when interactively creating a group
            # nothing has been added to yet.  The alternative is
            # to handle None as an allowed return value everywhere.
            return (0, 0, 0, 0)

    elif isinstance(obj, shapes.UserNode):
        return getBounds(obj.provideNode())

    else:
        raise ValueError("Don't know how to get bounds of %s" % obj)


class Sizer(Widget):
    _attrMap = AttrMap(
        BASE=shapes.SolidShape,
        contents=AttrMapValue(
            isListOfShapes, desc="Contained drawable elements"
        ),
    )

    def __init__(self, *elements):
        self.contents = []
        self.fillColor = cyan
        self.strokeColor = magenta

        for elem in elements:
            self.add(elem)

    def _addNamedNode(self, name, node):
        'if name is not None add an attribute pointing to node and add to the attrMap'
        if name:
            if name not in list(self._attrMap.keys()):
                self._attrMap[name] = AttrMapValue(isValidChild)
            setattr(self, name, node)

    def add(self, node, name=None):
        """Appends non-None child node to the 'contents' attribute. In addition,
        if a name is provided, it is subsequently accessible by name
        """
        # propagates properties down
        if node is not None:
            assert isValidChild(
                node
            ), "Can only add Shape or UserNode objects to a Group"
            self.contents.append(node)
            self._addNamedNode(name, node)

    def getBounds(self):
        # get bounds of each object
        if self.contents:
            b = []
            for elem in self.contents:
                b.append(getBounds(elem))
            return getRectsBounds(b)
        else:
            return (0, 0, 0, 0)

    def draw(self):
        g = shapes.Group()
        (x1, y1, x2, y2) = self.getBounds()
        r = shapes.Rect(
            x=x1,
            y=y1,
            width=x2 - x1,
            height=y2 - y1,
            fillColor=self.fillColor,
            strokeColor=self.strokeColor,
        )
        g.add(r)
        for elem in self.contents:
            g.add(elem)
        return g
