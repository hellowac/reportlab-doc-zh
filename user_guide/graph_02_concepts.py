# Copyright ReportLab Europe Ltd. 2000-2017
# see license.txt for license details

from reportlab.graphics import testshapes
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
    handnote,
    draw,
)


# heading2("General Concepts")
cn_heading2('一般概念')

disc(
    """
In this section we will present some of the more fundamental principles of 
the graphics library, which will show-up later in various places.
"""
)
cn_disc('在本节中，我们将介绍图形库的一些比较基本的原理，这些原理会在后面的各个地方出现。')

# heading3("Drawings and Renderers")
cn_heading3('图纸和渲染器')

disc(
    """
A <i>Drawing</i> is a platform-independent description of a collection of
shapes. It is not directly associated with PDF, Postscript or any other output
format. Fortunately, most vector graphics systems have followed the Postscript
model and it is possible to describe shapes unambiguously.
"""
)
cn_disc('<i>Drawing</i>是一个独立于平台的形状集合的描述。'
        '它不直接与 PDF、Postscript 或任何其他输出格式相关联。'
        '幸运的是，大多数矢量图形系统都遵循Postscript模型，'
        '因此可以毫不含糊地描述形状。')

disc(
    """
A drawing contains a number of primitive <i>Shapes</i>.
Normal shapes are those widely known as rectangles, circles, lines,
etc. One special (logic) shape is a <i>Group</i>, which can hold other
shapes and apply a transformation to them. Groups represent composites of 
shapes and allow to treat the composite as if it were a single shape.
Just about anything can be built up from a small number of basic shapes.
"""
)
cn_disc('一张图中包含了许多原始的<i>Shape</i> (形状)。'
        '普通形状是那些广为人知的矩形、圆形、线条等。'
        '一个特殊的（逻辑）形状是<i>Group</i> (组)，'
        '它可以容纳其他形状并对它们进行变换。'
        ' $Group$ 代表了 $Shape$ 的组合，并允许将 $Group$ '
        '合当作一个单一的 $Shape$ 来处理。'
        '几乎所有的东西都可以从少量的基本 $Shape$ (形状)建立起来。')

disc(
    """
The package provides several <i>Renderers</i> which know how to draw a
drawing into different formats. These include PDF (renderPDF), Postscript (
renderPS), and bitmap output (renderPM). The bitmap renderer uses Raph 
Levien's <i>libart</i> rasterizer and Fredrik Lundh's <i>Python Imaging 
Library</i> (PIL). The SVG renderer makes use of Python's standard library 
XML modules, so you don't need to install the XML-SIG's additional package 
named PyXML. If you have the right extensions installed, you can generate 
drawings in bitmap form for the web as well as vector form for PDF documents,
and get "identical output".
"""
)
cn_disc('该包提供了几个<i>Renderers</i> (渲染器)，它们知道如何将图纸绘制成不同的格式。'
        '其中包括 $PDF (renderPDF)$、$Postscript (renderPS)$ 和位图输出 $(renderPM)$。'
        '位图渲染器使用 $Raph Levien$ 的 <i>libart</i> 栅格化器'
        '和 $Fredrik Lundh$ 的 <i>Python Imaging Library</i> (PIL)。'
        '$SVG$ 渲染器使用了 $Python$ 的标准库 $XML$ 模块，'
        '所以你不需要安装 $XML-SIG$ 的附加包 $PyXML$。'
        '如果你安装了正确的扩展，你可以为网络生成位图形式的图画，'
        '也可以为 $PDF$ 文档生成矢量形式的图画，并得到 "相同的输出"。')

disc(
    """
The PDF renderer has special "privileges" - a Drawing object is also
a <i>Flowable</i> and, hence, can be placed directly in the story
of any Platypus document, or drawn directly on a <i>Canvas</i> with
one line of code. In addition, the PDF renderer has a utility function to make
a one-page PDF document quickly.
"""
)
cn_disc('$PDF$ 渲染器具有特殊的 "特权" '
        '-- 一个 $Drawing$ 对象也是一个<i>Flowable</i>，'
        '因此，可以直接放在任何 $Platypus$ 文档的故事中，或者直接用一行代码在<i>Canvas</i>上绘制。'
        '此外，$PDF$ 渲染器还有一个实用功能，可以快速制作一页$PDF$文档。')

disc(
    """
The SVG renderer is special as it is still pretty experimental.
The SVG code it generates is not really optimised in any way and
maps only the features available in ReportLab Graphics (RLG) to
SVG. This means there is no support for SVG animation, interactivity,
scripting or more sophisticated clipping, masking or graduation
shapes. So, be careful, and please report any bugs you find!
"""
)
cn_disc('$SVG$ 渲染器很特别，因为它仍然是相当的实验性的。'
        '它所生成的 $SVG$ 代码并没有经过任何优化，'
        '只是将 $ReportLab Graphics (RLG)$ 中可用的功能映射到 $SVG$ 中。'
        '这意味着不支持 $SVG$ 动画、交互性、脚本或更复杂的剪切、遮罩或渐变形状。'
        '因此，请小心，并请报告您发现的任何错误。')

# heading3("Coordinate System")
cn_heading3('坐标系统')

disc(
    """
The Y-direction in our X-Y coordinate system points from the
bottom <i>up</i>.
This is consistent with PDF, Postscript and mathematical notation.
It also appears to be more natural for people, especially when
working with charts.
Note that in other graphics models (such as SVG) the Y-coordinate
points <i>down</i>.
For the SVG renderer this is actually no problem as it will take
your drawings and flip things as needed, so your SVG output looks
just as expected.
"""
)
cn_disc('在我们的$X-Y$坐标系中，$Y$ 方向从底部<i>向上</i>。'
        '这与 $PDF$、$Postscript$ 和数学符号一致。'
        '对人们来说，这似乎也更自然，尤其是在处理图表时。'
        '请注意，在其他图形模型中（如$SVG$），$Y$ 坐标点<i>向下</i>。'
        '对于 $SVG$ 渲染器来说，这实际上是没有问题的，'
        '因为它将根据需要对您的图纸进行翻转，'
        '因此您的 $SVG$ 输出看起来和预期的一样。')

disc(
    """
The X-coordinate points, as usual, from left to right.
So far there doesn't seem to be any model advocating the opposite
direction - at least not yet (with interesting exceptions, as it
seems, for Arabs looking at time series charts...).
"""
)
cn_disc(' $X$ 坐标一如既往地从左到右。'
        '到目前为止，似乎没有任何模型主张反方向'
        ' -- 至少目前还没有（似乎有一些有趣的例外，阿拉伯人在看时间序列图时...）。')

# heading3("Getting Started")
cn_heading3('开始')

disc(
    """
Let's create a simple drawing containing the string "Hello World" and some 
special characters,
displayed on top of a coloured rectangle. After creating it we will save the 
drawing to a standalone PDF file.
"""
)
cn_disc('让我们创建一个简单的图形，包含字符串 "Hello World "和一些特殊的字符，'
        '显示在一个彩色的矩形之上。'
        '创建完成后，我们将把图画保存到一个独立的PDF文件中。')

eg(
    """
    from reportlab.lib import colors
    from reportlab.graphics.shapes import *

    d = Drawing(400, 200)
    d.add(Rect(50, 50, 300, 100, fillColor=colors.yellow))
    d.add(String(150,100, 'Hello World', fontSize=18, fillColor=colors.red))
    d.add(String(180,86, 'Special characters \\
                 \\xc2\\xa2\\xc2\\xa9\\xc2\\xae\\xc2\\xa3\\xce\\xb1\\xce\\xb2',
                 fillColor=colors.red))

    from reportlab.graphics import renderPDF
    renderPDF.drawToFile(d, 'example1.pdf', 'My First Drawing')
"""
)

disc("This will produce a PDF file containing the following graphic:")
cn_disc('这将产生一个包含以下图形的PDF文件。')

t = testshapes.getDrawing01()
draw(t, "'Hello World'")

disc(
    """
Each renderer is allowed to do whatever is appropriate for its format,
and may have whatever API is needed.
If it refers to a file format, it usually has a $drawToFile$ function,
and that's all you need to know about the renderer.
Let's save the same drawing in Encapsulated Postscript format:
"""
)
cn_disc('每个渲染器都可以做任何适合其格式的事情，并且可以有任何需要的API。'
        '如果它指的是一种文件格式，它通常有一个 $drawToFile$ 函数，'
        '这就是你需要知道的关于渲染器的所有信息。'
        '让我们以 $Encapsulated Postscript$ 格式保存同一张图。')

##eg("""
##    from reportlab.graphics import renderPS
##    renderPS.drawToFile(D, 'example1.eps', 'My First Drawing')
##""")
eg(
    """
    from reportlab.graphics import renderPS
    renderPS.drawToFile(d, 'example1.eps')
"""
)

disc(
    """
This will produce an EPS file with the identical drawing, which
may be imported into publishing tools such as Quark Express.
If we wanted to generate the same drawing as a bitmap file for
a website, say, all we need to do is write code like this:
"""
)
cn_disc('这将生成一个具有相同图形的EPS文件，'
        '可以导入到Quark Express等出版工具中。'
        '如果我们想生成同样的图形作为网站的位图文件，'
        '比如说，我们需要做的就是写这样的代码。')

eg(
    """
    from reportlab.graphics import renderPM
    renderPM.drawToFile(d, 'example1.png', 'PNG')
"""
)

disc(
    """
Many other bitmap formats, like GIF, JPG, TIFF, BMP and PPN are
genuinely available, making it unlikely you'll need to add external
postprocessing steps to convert to the final format you need.
"""
)
cn_disc('许多其他的位图格式，如GIF、JPG、TIFF、BMP和PPN都是真正可用的，'
        '这使得你不太可能需要添加外部的后处理步骤来转换为你需要的最终格式。')

disc(
    """
To produce an SVG file containing the identical drawing, which
may be imported into graphical editing tools such as Illustrator
all we need to do is write code like this:
"""
)
cn_disc('要生成一个包含相同图形的SVG文件，'
        '并将其导入到 $Illustrator$ 等图形编辑工具中，'
        '我们需要做的就是编写这样的代码。')

eg(
    """
    from reportlab.graphics import renderSVG
    renderSVG.drawToFile(d, 'example1.svg')
"""
)

# heading3("Attribute Verification")
cn_heading3('属性验证')

disc(
    """
Python is very dynamic and lets us execute statements at run time that
can easily be the source for unexpected behaviour.
One subtle 'error' is when assigning to an attribute that the framework
doesn't know about because the used attribute's name contains a typo.
Python lets you get away with it (adding a new attribute to an object,
say), but the graphics framework will not detect this 'typo' without
taking special counter-measures.
"""
)
cn_disc('Python是非常动态的，让我们在运行时执行的语句很容易成为意外行为的来源。'
        '一个微妙的 "错误 "是当分配到一个框架不知道的属性时，因为使用的属性的名字包含了一个错别字。'
        'Python 让你可以逃过一劫(比如说，给一个对象添加一个新的属性)，'
        '但图形框架在不采取特殊对策的情况下，是不会检测到这个"错别字"的。')

disc(
    """
There are two verification techniques to avoid this situation.
The default is for every object to check every assignment at run
time, such that you can only assign to 'legal' attributes.
This is what happens by default.
As this imposes a small performance penalty, this behaviour can
be turned off when you need it to be.
"""
)
cn_disc('有两种验证技术可以避免这种情况。'
        '默认情况下，每个对象在运行时都会检查每一次赋值，这样你就只能赋值给 "合法"的属性。'
        '这就是默认情况。由'
        '于这样做会带来很小的性能损失，所以在你需要的时候可以关闭这种行为。')

eg(
    """
>>> r = Rect(10,10,200,100, fillColor=colors.red)
>>>
>>> r.fullColor = colors.green # note the typo
>>> r.x = 'not a number'       # illegal argument type
>>> del r.width                # that should confuse it
"""
)

disc(
    """
These statements would be caught by the compiler in a statically
typed language, but Python lets you get away with it.
The first error could leave you staring at the picture trying to
figure out why the colors were wrong.
The second error would probably become clear only later, when
some back-end tries to draw the rectangle.
The third, though less likely, results in an invalid object that
would not know how to draw itself.
"""
)
cn_disc('这些语句在静态类型的语言中会被编译器捕获，'
        '但是 Python 让你摆脱了它。'
        '第一个错误可能会让你盯着图片想弄清楚为什么颜色是错的。'
        '第二个错误可能只有在以后，当一些后端试图绘制矩形时才会变得清晰。'
        '第三种错误，虽然可能性较小，但会导致一个不知道如何绘制的无效对象。')

eg(
    """
>>> r = shapes.Rect(10,10,200,80)
>>> r.fullColor = colors.green
Traceback (most recent call last):
  File "<interactive input>", line 1, in ?
  File "C:\\code\\users\\andy\\graphics\\shapes.py", line 254, in __setattr__
    validateSetattr(self,attr,value)    #from reportlab.lib.attrmap
  File "C:\\code\\users\\andy\\lib\\attrmap.py", line 74, in validateSetattr
    raise AttributeError, "Illegal attribute '%s' in class %s" % (name, 
    obj.__class__.__name__)
AttributeError: Illegal attribute 'fullColor' in class Rect
>>>
"""
)

disc(
    """
This imposes a performance penalty, so this behaviour can be turned
off when you need it to be.
To do this, you should use the following lines of code before you
first import reportlab.graphics.shapes:
"""
)
cn_disc('这将带来性能上的惩罚，所以当你需要这种行为时，可以将其关闭。'
        '要做到这一点，您应该在第一次导入 ^reportlab.graphics.shapes^ 之前使用以下代码行。')

eg(
    """
>>> import reportlab.rl_config
>>> reportlab.rl_config.shapeChecking = 0
>>> from reportlab.graphics import shapes
>>>
"""
)

disc(
    """
Once you turn off $shapeChecking$, the classes are actually built
without the verification hook; code should get faster, then.
Currently the penalty seems to be about 25% on batches of charts,
so it is hardly worth disabling.
However, if we move the renderers to C in future (which is eminently
possible), the remaining 75% would shrink to almost nothing and
the saving from verification would be significant.
"""
)
cn_disc('一旦你关闭了 ^reportlab.rl_config.shapeChecking^，'
        '类实际上是在没有验证钩子的情况下构建的；'
        '那么，代码应该会变得更快。'
        '目前，对成批图表的惩罚似乎是25%，所以几乎不值得禁用。'
        '然而，如果我们将来把渲染器转移到C语言上（这是很有可能的），'
        '剩下的75%就会缩减到几乎没有，而且从验证中节省的成本也会很可观。')

disc(
    """
Each object, including the drawing itself, has a $verify()$ method.
This either succeeds, or raises an exception.
If you turn off automatic verification, then you should explicitly
call $verify()$ in testing when developing the code, or perhaps
once in a batch process.
"""
)
cn_disc('每个对象，包括绘图本身，都有一个$verify()$方法。'
        '这个方法要么成功，要么引发一个异常。'
        '如果你关闭了自动验证，那么你应该在开发代码时，'
        '在测试中明确地调用 $verify()$，'
        '或者在一个批处理中调用一次。')

# heading3("Property Editing")
cn_heading3('属性编辑')

disc(
    """
A cornerstone of the reportlab/graphics which we will cover below is
that you can automatically document widgets.
This means getting hold of all of their editable properties,
including those of their subcomponents.
"""
)
cn_disc('我们将在下面介绍的 $reportlab/graphics$ 的一个基石是，'
        '你可以自动记录 $widget$ 。'
        '这意味着你可以掌握它们所有的可编辑属性，包括它们的子组件。')

disc(
    """
Another goal is to be able to create GUIs and config files for
drawings. A generic GUI can be built to show all editable properties
of a drawing, and let you modify them and see the results.
The Visual Basic or Delphi development environment are good
examples of this kind of thing.
In a batch charting application, a file could list all the
properties of all the components in a chart, and be merged
with a database query to make a batch of charts.
"""
)
cn_disc('另一个目标是能够为图纸创建GUI和配置文件。'
        '可以建立一个通用的GUI来显示图纸的所有可编辑的属性，'
        '并让你修改这些属性并查看结果。'
        '$Visual Basic$ 或 $Delphi$ 开发环境是这类东西的好例子。'
        '在批处理图表应用程序中，一个文件可以列出图表中所有组件的所有属性，'
        '并与数据库查询合并，以制作一批图表。')

disc(
    """
To support these applications we have two interfaces, $getProperties$
and $setProperties$, as well as a convenience method $dumpProperties$.
The first returns a dictionary of the editable properties of an
object; the second sets them en masse.
If an object has publicly exposed 'children' then one can recursively
set and get their properties too.
This will make much more sense when we look at <i>Widgets</i> later on,
but we need to put the support into the base of the framework.
"""
)
cn_disc('为了支持这些应用，我们有两个接口，'
        '$getProperties$ 和 $setProperties$，'
        '以及一个方便的方法$dumpProperties$。'
        '第一个方法返回一个对象的可编辑属性的字典；'
        '第二个方法则集体设置这些属性。'
        '如果一个对象有公开的 "子对象"，那么我们也可以递归地设置和获取它们的属性。'
        '当我们稍后看<i>Widgets</i>时，这将更有意义，但我们需要将支持放到框架的基础上。')

eg(
    """
>>> r = shapes.Rect(0,0,200,100)
>>> import pprint
>>> pprint.pprint(r.getProperties())
{'fillColor': Color(0.00,0.00,0.00),
 'height': 100,
 'rx': 0,
 'ry': 0,
 'strokeColor': Color(0.00,0.00,0.00),
 'strokeDashArray': None,
 'strokeLineCap': 0,
 'strokeLineJoin': 0,
 'strokeMiterLimit': 0,
 'strokeWidth': 1,
 'width': 200,
 'x': 0,
 'y': 0}
>>> r.setProperties({'x':20, 'y':30, 'strokeColor': colors.red})
>>> r.dumpProperties()
fillColor = Color(0.00,0.00,0.00)
height = 100
rx = 0
ry = 0
strokeColor = Color(1.00,0.00,0.00)
strokeDashArray = None
strokeLineCap = 0
strokeLineJoin = 0
strokeMiterLimit = 0
strokeWidth = 1
width = 200
x = 20
y = 30
>>>  """
)

pencilnote()

disc(
    """
<i>Note: $pprint$ is the standard Python library module that allows
you to 'pretty print' output over multiple lines rather than having
one very long line.</i>
"""
)
cn_disc('<i><font color=red>注意</font>：$pprint$是标准的Python库模块，'
        '它允许您在多行上 "漂亮地打印" 输出，而不是只有一行很长的内容。')

disc(
    """
These three methods don't seem to do much here, but as we will see
they make our widgets framework much more powerful when dealing with
non-primitive objects.
"""
)
cn_disc('这三种方法在这里似乎并没有什么作用，'
        '但正如我们将看到的那样，'
        '它们使我们的 $widgets$ 框架在处理非原始对象时更加强大。')

# heading3("Naming Children")
cn_heading3('Children 命名')

disc(
    """
You can add objects to the $Drawing$ and $Group$ objects.
These normally go into a list of contents.
However, you may also give objects a name when adding them.
This allows you to refer to and possibly change any element
of a drawing after constructing it.
"""
)
cn_disc('您可以将对象添加到$Drawing$和$Group$对象中。'
        '这些对象通常会进入一个内容列表中。'
        '然而，你也可以在添加对象时给它们一个名字。'
        '这允许您在构造一个绘图后引用并可能改变它的任何元素。')

eg(
    """
>>> d = shapes.Drawing(400, 200)
>>> s = shapes.String(10, 10, 'Hello World')
>>> d.add(s, 'caption')
>>> s.caption.text
'Hello World'
>>>
"""
)

disc(
    """
Note that you can use the same shape instance in several contexts
in a drawing; if you choose to use the same $Circle$ object in many
locations (e.g. a scatter plot) and use different names to access
it, it will still be a shared object and the changes will be
global.
"""
)
cn_disc('请注意，您可以在绘图中的多个上下文中使用相同的形状实例；'
        '如果您选择在许多位置（如散点图）使用相同的$Circle$对象，'
        '并使用不同的名称来访问它，它仍然是一个共享对象，'
        '并且更改将是全局的。')

disc(
    'This provides one paradigm for creating and modifying interactive '
    'drawings.')
cn_disc('这为创建和修改交互式图纸提供了一种范式。')
