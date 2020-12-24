# Copyright ReportLab Europe Ltd. 2000-2017
# see license.txt for license details
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import widgetbase
from reportlab.graphics.widgets import signsandsymbols
from reportlab.graphics.charts.piecharts import Pie

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
    cn_bullet,
    getStory,
    pencilnote,
    startKeep,
    endKeep,
    caption,
    cn_caption,
    styleSheet,
    cn_styleSheet,
    draw,
    cn_draw,
    getJustFontPaths,
)


# heading2("Widgets")
cn_heading2("小部件")

disc(
    """
We now describe widgets and how they relate to shapes.
Using many examples it is shown how widgets make reusable
graphics components.
"""
)
cn_disc('现在，我们描述小部件及其与形状的关系。 '
        '通过许多示例，展示了小部件如何使可重用图形组件成为现实。')

# heading3("Shapes vs. Widgets")
cn_heading3('$Shapes vs. Widgets$')

disc(
    """Up until now, Drawings have been 'pure data'. There is no code in them
    to actually do anything, except assist the programmer in checking and
    inspecting the drawing. In fact, that's the cornerstone of the whole
    concept and is what lets us achieve portability - a renderer only
    needs to implement the primitive shapes."""
)
cn_disc('到目前为止，图纸一直是 "$pure data$"(纯数据)。'
        '除了协助程序员检查和检验图纸外，它们中没有任何代码可以真正做任何事情。'
        '事实上，这是整个概念的基石，也是让我们实现可移植性的原因'
        '--渲染器只需要实现原始形状。')

disc(
    """We want to build reusable graphic objects, including a powerful chart
    library. To do this we need to reuse more tangible things than
    rectangles and circles. We should be able to write objects for other
    to reuse - arrows, gears, text boxes, UML diagram nodes, even fully
    fledged charts."""
)
cn_disc('我们希望构建可重复使用的图形对象，包括一个强大的图表库。'
        '要做到这一点，我们需要重用比矩形和圆形更有形的东西。'
        '我们应该能够编写对象供其他人重用 '
        '--箭头、齿轮、文本框、UML图节点，甚至是完全成熟的图表。')

disc(
    """
The Widget standard is a standard built on top of the shapes module.
Anyone can write new widgets, and we can build up libraries of them.
Widgets support the $getProperties()$ and $setProperties()$ methods,
so you can inspect and modify as well as document them in a uniform
way.
"""
)
cn_disc('小部件标准是建立在shapes模块之上的标准，'
        '任何人都可以编写新的小部件，我们可以建立它们的库。'
        '$Widget$ 支持 $getProperties()$ 和 $setProperties()$ 方法，'
        '所以你可以检查和修改，也可以用统一的方式记录它们。')

bullet("A widget is a reusable shape ")
bullet(
    """it can be initialized with no arguments
    when its $draw()$ method is called it creates a primitive Shape or a
    Group to represent itself"""
)
bullet(
    """It can have any parameters you want, and they can drive the way it is
    drawn"""
)
bullet(
    """it has a $demo()$ method which should return an attractively drawn
    example of itself in a 200x100 rectangle. This is the cornerstone of
    the automatic documentation tools. The $demo()$ method should also have
    a well written docstring, since that is printed too!"""
)
cn_bullet('小部件是一个可重复使用的形状')
cn_bullet('当调用 $draw()$ 方法时，它可以在没有参数的情况下进行初始化，'
          '它创建了一个原始形状或一个组来表示自己。')
cn_bullet('它可以有任何你想要的参数，它们可以驱动它的绘制方式。')
cn_bullet('它有一个$demo()$方法，该方法应以200x100矩形返回一个精美的绘制示例。 '
          '这是自动文档编制工具的基础。 $demo()$方法也应该有一个写得很好的文档字符串，因为它也可以打印！')

disc("""Widgets run contrary to the idea that a drawing is just a bundle of
shapes; surely they have their own code? The way they work is that a
widget can convert itself to a group of primitive shapes. If some of
its components are themselves widgets, they will get converted too.
This happens automatically during rendering; the renderer will not see
your chart widget, but just a collection of rectangles, lines and
strings. You can also explicitly 'flatten out' a drawing, causing all
widgets to be converted to primitives.""")

cn_disc('小部件与图形只是一捆形状的想法背道而驰。 他们肯定有自己的代码吗？ '
        '它们的工作方式是，小部件可以将自身转换为一组原始形状。 '
        '如果其某些组件本身就是小部件，它们也将被转换。 '
        '这在渲染过程中自动发生。 '
        '渲染器将看不到图表小部件，而只会看到矩形，直线和字符串的集合。 '
        '您还可以显式 “$flatten out$” (扁平化) 工程图，从而将所有小部件都转换为基元。')

# heading3("Using a Widget")
cn_heading3('使用一个小部件')

disc(
    """
Let's imagine a simple new widget.
We will use a widget to draw a face, then show how it was implemented."""
)
cn_disc('让我们想象一个简单的新部件。'
        '我们将使用一个小部件来绘制一张脸，然后展示它是如何实现的。')

eg(
    """
>>> from reportlab.lib import colors
>>> from reportlab.graphics import shapes
>>> from reportlab.graphics import widgetbase
>>> from reportlab.graphics import renderPDF
>>> d = shapes.Drawing(200, 100)
>>> f = widgetbase.Face()
>>> f.skinColor = colors.yellow
>>> f.mood = "sad"
>>> d.add(f)
>>> renderPDF.drawToFile(d, 'face.pdf', 'A Face')
"""
)

d = Drawing(200, 120)
f = widgetbase.Face()
f.x = 50
f.y = 10
f.skinColor = colors.yellow
f.mood = "sad"
d.add(f)
# draw(d, 'A sample widget')
cn_draw(d, '小部件示例')

disc(
    """
Let's see what properties it has available, using the $setProperties()$
method we have seen earlier:
"""
)
cn_disc('让我们看看它有哪些可用的属性，使用我们前面看到的 $setProperties()$ 方法。')

eg(
    """
>>> f.dumpProperties()
eyeColor = Color(0.00,0.00,1.00)
mood = sad
size = 80
skinColor = Color(1.00,1.00,0.00)
x = 10
y = 10
>>>
"""
)

disc(
    """
One thing which seems strange about the above code is that we did not
set the size or position when we made the face.
This is a necessary trade-off to allow a uniform interface for
constructing widgets and documenting them - they cannot require
arguments in their $__init__()$ method.
Instead, they are generally designed to fit in a 200 x 100
window, and you move or resize them by setting properties such as
x, y, width and so on after creation.
"""
)
cn_disc('上面的代码似乎奇怪的一件事是，当我们制作面孔时，我们没有设置大小或位置。 '
        '这是必要的折衷方案，以允许使用一个统一的界面来构造小部件并对其进行记录'
        '-它们不能在其 $__init__()$ 方法中要求参数。 '
        '取而代之的是，通常将它们设计为适合200 x 100的窗口，'
        '然后在创建后通过设置诸如 $x, y, width$ 等属性来移动或调整它们的大小。')

disc(
    """
In addition, a widget always provides a $demo()$ method.
Simple ones like this always do something sensible before setting
properties, but more complex ones like a chart would not have any
data to plot. The documentation tool calls $demo()$ so that your fancy new chart
class can create a drawing showing what it can do.
"""
)
cn_disc('此外，一个小部件总是提供一个$demo()$方法。'
        '像这样简单的总是在设置属性之前做一些合理的事情，但更复杂的像图表这样的就没有任何数据可供绘制。'
        '文档工具会调用$demo()$，'
        '这样你的花哨的新图表类就可以创建一张图来展示它的能力。')

disc(
    """
Here are a handful of simple widgets available in the module
<i>signsandsymbols.py</i>:
"""
)
cn_disc('以下是一些简单的小部件，可在模块 <i>$signsandsymbols.py$</i> 中使用。')

d = Drawing(230, 230)

ne = signsandsymbols.NoEntry()
ds = signsandsymbols.DangerSign()
fd = signsandsymbols.FloppyDisk()
ns = signsandsymbols.NoSmoking()

ne.x, ne.y = 10, 10
ds.x, ds.y = 120, 10
fd.x, fd.y = 10, 120
ns.x, ns.y = 120, 120

d.add(ne)
d.add(ds)
d.add(fd)
d.add(ns)

# draw(d, 'A few samples from signsandsymbols.py')
cn_draw(d, '一些来自 $signandsymbols.py$ 的例子。')

disc(
    """
And this is the code needed to generate them as seen in the drawing above:
"""
)
cn_disc('而这是生成它们所需要的代码，如上图所示。')

eg(
    """
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.widgets import signsandsymbols

d = Drawing(230, 230)

ne = signsandsymbols.NoEntry()
ds = signsandsymbols.DangerSign()
fd = signsandsymbols.FloppyDisk()
ns = signsandsymbols.NoSmoking()

ne.x, ne.y = 10, 10
ds.x, ds.y = 120, 10
fd.x, fd.y = 10, 120
ns.x, ns.y = 120, 120

d.add(ne)
d.add(ds)
d.add(fd)
d.add(ns)
"""
)

# heading3("Compound Widgets")
cn_heading3('复合小部件')

disc(
    """Let's imagine a compound widget which draws two faces side by side.
    This is easy to build when you have the Face widget."""
)
cn_disc('让我们想象一下，一个复合小组件可以并排绘制两个面孔。'
        '当你有了 $Face widget$ 时，就可以很容易地构建这个小部件。')

eg(
    """
>>> tf = widgetbase.TwoFaces()
>>> tf.faceOne.mood
'happy'
>>> tf.faceTwo.mood
'sad'
>>> tf.dumpProperties()
faceOne.eyeColor = Color(0.00,0.00,1.00)
faceOne.mood = happy
faceOne.size = 80
faceOne.skinColor = None
faceOne.x = 10
faceOne.y = 10
faceTwo.eyeColor = Color(0.00,0.00,1.00)
faceTwo.mood = sad
faceTwo.size = 80
faceTwo.skinColor = None
faceTwo.x = 100
faceTwo.y = 10
>>>
"""
)

disc(
    """The attributes 'faceOne' and 'faceTwo' are deliberately exposed so you
    can get at them directly. There could also be top-level attributes,
    but there aren't in this case."""
)
cn_disc("故意暴露了'$faceOne$'和'$faceTwo$'这两个属性，这样你就可以直接获取它们。也可以有顶层属性，但本例中没有。")

# heading3("Verifying Widgets")
cn_heading3('校验小部件')

disc(
    """The widget designer decides the policy on verification, but by default
    they work like shapes - checking every assignment - if the designer
    has provided the checking information."""
)
cn_disc('小组件设计者决定验证的策略，但默认情况下，'
        '如果设计者提供了检查信息，它们就会像形状一样工作--检查每一个任务。')

# heading3("Implementing Widgets")
cn_heading3('实现小部件')

disc(
    """We tried to make it as easy to implement widgets as possible. Here's
    the code for a Face widget which does not do any type checking:"""
)
cn_disc('我们试图让它尽可能容易地实现小部件。下面是一个不做任何类型检查的 $Face$ 小组件的代码。')

eg(
    """
class Face(Widget):
    \"\"\"This draws a face with two eyes, mouth and nose.\"\"\"

    def __init__(self):
        self.x = 10
        self.y = 10
        self.size = 80
        self.skinColor = None
        self.eyeColor = colors.blue
        self.mood = 'happy'

    def draw(self):
        s = self.size  # abbreviate as we will use this a lot
        g = shapes.Group()
        g.transform = [1,0,0,1,self.x, self.y]
        # background
        g.add(shapes.Circle(s * 0.5, s * 0.5, s * 0.5,
                            fillColor=self.skinColor))
        # CODE OMITTED TO MAKE MORE SHAPES
        return g
"""
)

disc(
    """We left out all the code to draw the shapes in this document, but you
    can find it in the distribution in $widgetbase.py$."""
)
cn_disc('我们在这个文档中省略了所有绘制形状的代码，但你可以在 $widgetbase.py$ 中找到它。')

disc(
    """By default, any attribute without a leading underscore is returned by
    setProperties. This is a deliberate policy to encourage consistent
    coding conventions."""
)
cn_disc('默认情况下，任何没有前导下划线的属性都会被 $setProperties$ 返回。这是为了鼓励一致的编码惯例而特意制定的政策。')

disc(
    """Once your widget works, you probably want to add support for
    verification. This involves adding a dictionary to the class called
    $_verifyMap$, which map from attribute names to 'checking functions'.
    The $widgetbase.py$ module defines a bunch of checking functions with names
    like $isNumber$, $isListOfShapes$ and so on. You can also simply use $None$,
    which means that the attribute must be present but can have any type.
    And you can and should write your own checking functions. We want to
    restrict the "mood" custom attribute to the values "happy", "sad" or
    "ok". So we do this:"""
)
cn_disc('一旦你的 $widget$ 工作了，你可能想要添加对验证的支持。'
        '这涉及到在类中添加一个名为 $_verifyMap$ 的字典，它从属性名映射到 "检查函数"。'
        '$widgetbase.py$ 模块定义了一堆检查函数，比如 $isNumber$, $isListOfShapes$ 等等。'
        '你也可以简单地使用 $None$，这意味着属性必须存在，但可以有任何类型。'
        '而且你可以也应该写你自己的检查函数。'
        '我们想将 "$mood$" 自定义属性限制为 "$happy$"、"$sad$"或 "$ok$" 等值。'
        '所以我们这样做:')

eg(
    """
class Face(Widget):
    \"\"\"This draws a face with two eyes.  It exposes a
    couple of properties to configure itself and hides
    all other details\"\"\"
    def checkMood(moodName):
        return (moodName in ('happy','sad','ok'))
    _verifyMap = {
        'x': shapes.isNumber,
        'y': shapes.isNumber,
        'size': shapes.isNumber,
        'skinColor':shapes.isColorOrNone,
        'eyeColor': shapes.isColorOrNone,
        'mood': checkMood
        }
"""
)

disc(
    """This checking will be performed on every attribute assignment; or, if
    $config.shapeChecking$ is off, whenever you call $myFace.verify()$."""
)
cn_disc('这个检查将在每次属性分配时执行；'
        '或者，如果$config.shapeChecking$是关闭的，'
        '每当你调用$myFace.verify()$时，这个检查就会被执行。')

# heading3("Documenting Widgets")
cn_heading3('记录小部件')

disc(
    """
We are working on a generic tool to document any Python package or
module; this is already checked into ReportLab and will be used to
generate a reference for the ReportLab package.
When it encounters widgets, it adds extra sections to the
manual including:"""
)
cn_disc('我们正在开发一个通用工具来记录任何Python包或模块；'
        '它已经记录到到 $ReportLab$ 中，并将用于为 $ReportLab$包生成一个引用。'
        '当它遇到小部件时，它会在手册中添加额外的章节，包括：')

bullet("the doc string for your widget class ")
bullet(
    "the code snippet from your <i>demo()</i> method, so people can see how "
    "to use it"
)
bullet("the drawing produced by the <i>demo()</i> method ")
bullet("the property dump for the widget in the drawing. ")
cn_bullet('您的小组件类的文档字符串')
cn_bullet('从您的<i>$demo()$</i>方法中提取的代码片段，以便人们可以看到如何使用它')
cn_bullet('由<i>$demo()$</i>方法产生的图画。')
cn_bullet('绘图中小组件的属性转储。')

disc(
    """
This tool will mean that we can have guaranteed up-to-date
documentation on our widgets and charts, both on the web site
and in print; and that you can do the same for your own widgets,
too!
"""
)
cn_disc('这个工具意味着我们可以保证在网站和印刷品上的小部件和图表上都有最新的文档； '
        '而且您也可以为自己的小部件做同样的事情！')

# heading3("Widget Design Strategies")
cn_heading3('小工具设计策略')

disc(
    """We could not come up with a consistent architecture for designing
widgets, so we are leaving that problem to the authors! If you do not
like the default verification strategy, or the way
$setProperties/getProperties$ works, you can override them yourself."""
)
cn_disc('我们无法提出一个一致的架构来设计 $widget$，所以我们把这个问题留给了作者！'
        '如果你不喜欢默认的验证策略，或者是 $setProperties/getProperties$ 的工作方式，'
        '你可以自己覆盖它们。')

disc(
    """For simple widgets it is recommended that you do what we did above:
select non-overlapping properties, initialize every property on
$__init__$ and construct everything when $draw()$ is called. You can
instead have $__setattr__$ hooks and have things updated when certain
attributes are set. Consider a pie chart. If you want to expose the
individual slices, you might write code like this:"""
)
cn_disc('对于简单的 $widgets$ ，建议你做我们上面所做的：'
        '选择非重叠的属性，在 $__init__$ 上初始化每个属性，'
        '然后在调用 $draw()$ 时构造一切。你可以使用 $__setattr__$ 钩子，'
        '当某些属性被设置时，就会更新所有的东西。'
        '考虑一个饼图。如果你想暴露各个切片，你可以写这样的代码。')

eg(
    """
from reportlab.graphics.charts import piecharts
pc = piecharts.Pie()
pc.defaultColors = [navy, blue, skyblue] #used in rotation
pc.data = [10,30,50,25]
pc.slices[7].strokeWidth = 5
"""
)
# removed 'pc.backColor = yellow' from above code example

disc(
    """The last line is problematic as we have only created four slices - in
fact we might not have created them yet. Does $pc.slices[7]$ raise an
error? Is it a prescription for what should happen if a seventh wedge
is defined, used to override the default settings? We dump this
problem squarely on the widget author for now, and recommend that you
get a simple one working before exposing 'child objects' whose
existence depends on other properties' values :-)"""
)
cn_disc('最后一行是有问题的，因为我们只创建了四个切片'
        '--事实上，我们可能还没有创建它们。'
        '$pc.slices[7]$是否会引起错误？'
        '如果定义了第七个楔形图，用来覆盖默认设置，这是不是一个解决方案？'
        '我们现在把这个问题直接丢给 $widget$ 作者，并建议您在暴露 "子对象" 之前先做一个简单的工作，'
        '因为子对象的存在取决于其他属性的值 :-)')

disc(
    """We also discussed rules by which parent widgets could pass properties
to their children. There seems to be a general desire for a global way
to say that 'all slices get their lineWidth from the lineWidth of
their parent' without a lot of repetitive coding. We do not have a
universal solution, so again leave that to widget authors. We hope
people will experiment with push-down, pull-down and pattern-matching
approaches and come up with something nice. In the meantime, we
certainly can write monolithic chart widgets which work like the ones
in, say, Visual Basic and Delphi."""
)
cn_disc('我们还讨论了父级小部件可以将属性传递给其子级的规则。 '
        '人们似乎普遍希望以一种全局的方式来表示“所有切片均从其父级的 $lineWidth$ 获得其 $lineWidth$ ”，'
        '而无需进行大量重复编码。 '
        '我们没有通用的解决方案，因此请再次将其留给小部件作者。 '
        '我们希望人们将尝试下推，下拉和模式匹配方法，并提出一些不错的东西。'
        ' 同时，我们当然可以编写整体式的图表小部件，'
        '这些小部件的工作方式类似于Visual Basic和Delphi。')

disc(
    """For now have a look at the following sample code using an early
version of a pie chart widget and the output it generates:"""
)
cn_disc('现在看看下面的示例代码，使用一个早期版本的饼图小组件和它产生的输出。')

eg(
    """
from reportlab.lib.colors import *
from reportlab.graphics import shapes,renderPDF
from reportlab.graphics.charts.piecharts import Pie

d = Drawing(400,200)
d.add(String(100,175,"Without labels", textAnchor="middle"))
d.add(String(300,175,"With labels", textAnchor="middle"))

pc = Pie()
pc.x = 25
pc.y = 50
pc.data = [10,20,30,40,50,60]
pc.slices[0].popout = 5
d.add(pc, 'pie1')

pc2 = Pie()
pc2.x = 150
pc2.y = 50
pc2.data = [10,20,30,40,50,60]
pc2.labels = ['a','b','c','d','e','f']
d.add(pc2, 'pie2')

pc3 = Pie()
pc3.x = 275
pc3.y = 50
pc3.data = [10,20,30,40,50,60]
pc3.labels = ['a','b','c','d','e','f']
pc3.slices.labelRadius = 0.65
pc3.slices.fontName = "Helvetica-Bold"
pc3.slices.fontSize = 16
pc3.slices.fontColor = colors.yellow
d.add(pc3, 'pie3')
"""
)

# Hack to force a new paragraph before the todo() :-(
disc("")

d = Drawing(400, 200)
d.add(String(100, 175, "Without labels", textAnchor="middle"))
d.add(String(300, 175, "With labels", textAnchor="middle"))

pc = Pie()
pc.x = 25
pc.y = 50
pc.data = [10, 20, 30, 40, 50, 60]
pc.slices[0].popout = 5
d.add(pc, 'pie1')

pc2 = Pie()
pc2.x = 150
pc2.y = 50
pc2.data = [10, 20, 30, 40, 50, 60]
pc2.labels = ['a', 'b', 'c', 'd', 'e', 'f']
d.add(pc2, 'pie2')

pc3 = Pie()
pc3.x = 275
pc3.y = 50
pc3.data = [10, 20, 30, 40, 50, 60]
pc3.labels = ['a', 'b', 'c', 'd', 'e', 'f']
pc3.slices.labelRadius = 0.65
pc3.slices.fontName = "Helvetica-Bold"
pc3.slices.fontSize = 16
pc3.slices.fontColor = colors.yellow
d.add(pc3, 'pie3')

# draw(d, 'Some sample Pies')
cn_draw(d, '一些饼图示例')
