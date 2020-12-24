from reportlab.lib.colors import blue, pink, yellow, cyan, brown
from reportlab.lib.units import inch
from utils import (
    heading1,
    cn_heading1,
    heading2,
    cn_heading2,
    heading3,
    cn_heading3,
    heading4,
    cn_heading4,
    disc,
    cn_disc,
    eg,
    cn_eg,
    illust,
    cn_illust,
    CPage,
    parabox,
    parabox2,
    bullet,
    getStory,
    pencilnote,
    startKeep,
    endKeep,
    caption,
    cn_caption,
    styleSheet,
    cn_styleSheet,
    npeg,
    EmbeddedCode,
    todo,
    cn_todo,
    handnote,
)
from utils import examples

# heading1("Writing your own $Flowable$ Objects")
cn_heading1("编写你自己的$Flowable$对象")

disc(
    """
Flowables are intended to be an open standard for creating reusable report 
content, and you can easily create your own objects.  We hope that over time 
we will build up a library of contributions, giving reportlab users a
rich selection of charts, graphics and other "report widgets" they can use in their own reports. This section shows you how to create your own flowables."""
)
cn_disc('Flowables旨在成为创建可重复使用的报表内容的开放标准，您可以轻松创建自己的对象。 '
        '我们希望随着时间的推移，我们将建立一个贡献库，为 $reportlab$ 用户提供丰富的图表、图形和其他 "report widgets"选择，'
        '他们可以在自己的报表中使用。本节将向您展示如何创建您自己的 $flowables$。')

todo(
    """we should put the Figure class in the
standard library, as it is a very useful base."""
)

cn_todo('我们应该把Figure类放在标准库中，因为它是一个非常有用的基础。')


# heading2("A very simple $Flowable$")
cn_heading2('一个非常简单的 $Flowable$')

disc(
    """
Recall the $hand$ function from the $pdfgen$ section of this user guide which
generated a drawing of a hand as a closed figure composed from Bezier curves.
"""
)
cn_disc('回想一下本用户指南中 $pdfgen$ 一节中的 $hand$ 函数，'
        '它生成了一个由贝塞尔曲线构成的闭合图形的手图。')

# illust(examples.hand, "a hand")
cn_illust(examples.hand, "一只手")

disc(
    """
To embed this or any other drawing in a Platypus flowable we must define a
subclass of $Flowable$ with at least a $wrap$ method and a $draw$ method.
"""
)
cn_disc('为了在 $Platypus flowable$ 中嵌入这个或其他绘图，'
        '我们必须定义一个 $Flowable$ 的子类，'
        '至少有一个$wrap$方法和一个$draw$方法。')

eg(examples.testhandannotation)

disc(
    """
The $wrap$ method must provide the size of the drawing -- it is used by
the Platypus mainloop to decide whether this element fits in the space remaining
on the current frame.  The $draw$ method performs the drawing of the object after
the Platypus mainloop has translated the $(0,0)$ origin to an appropriate location
in an appropriate frame.
"""
)
cn_disc('$wrap$方法必须提供绘图的大小'
        '-- $Platypus$ 主循环用它来决定这个元素是否适合当前框架的剩余空间。 '
        '在 $Platypus$ 主循环将 $(0,0)$ 原点转换到适当的框架中的适当位置后，'
        '$draw$方法将执行对象的绘制。')
disc(
    """
Below are some example uses of the $HandAnnotation$ flowable.
"""
)
cn_disc('以下是 $HandAnnotation flowable$ 的一些使用示例。')

handnote()

disc("""The default.""")
cn_disc('默认情况下')

handnote(size=inch)

disc("""Just one inch high.""")
disc('只是一寸高。')

handnote(xoffset=3 * inch, size=inch, strokecolor=blue, fillcolor=cyan)

disc("""One inch high and shifted to the left with blue and cyan.""")
cn_disc('高1英寸，向左偏蓝和青色。')

# heading2("Modifying a Built in $Flowable$")
cn_heading2('修改内置的 $Flowable$')

disc(
    """To modify an existing flowable, you should create a derived class
and override the methods you need to change to get the desired behaviour"""
)
cn_disc(
    """要修改现有的可流动对象，您应该创建一个派生类并覆盖需要更改以获得所需行为的方法。"""
)

disc(
    """As an example to create a rotated image you need to override the wrap
and draw methods of the existing Image class"""
)
cn_disc('作为创建旋转图像的示例，您需要覆盖现有 $Image$ 类的 $wrap$ 和 $draw$ 方法')

I = 'images/replogo.gif'

EmbeddedCode(
    """
class RotatedImage(Image):
    def wrap(self,availWidth,availHeight):
        h, w = Image.wrap(self,availHeight,availWidth)
        return w, h
    def draw(self):
        self.canv.rotate(90)
        Image.draw(self)
I = RotatedImage('%s')
I.hAlign = 'CENTER'
"""
    % I,
    'I',
)
