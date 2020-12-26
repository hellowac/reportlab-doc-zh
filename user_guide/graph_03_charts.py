from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Circle
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.axes import XCategoryAxis, YValueAxis, XValueAxis
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.piecharts import sample5, sample7, sample8

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
    npeg,
    EmbeddedCode,
    todo,
    cn_todo,
    handnote,
    draw,
    cn_draw,
)

# heading2("Charts")
cn_heading2("图表")

disc(
    """
The motivation for much of this is to create a flexible chart
package. This section presents a treatment of the ideas behind our charting
model, what the design goals are and what components of the chart package already exist.
"""
)
cn_disc('其中大部分的动机是为了创建一个灵活的图表包。'
        '本节将介绍我们的图表模型背后的想法，'
        '设计目标是什么，以及图表包的哪些组件已经存在。')


# heading3("Design Goals")
cn_heading3('设计目标')

disc("Here are some of the design goals: ")
cn_disc('以下是一些设计目标。')

disc("<i>Make simple top-level use really simple </i>")
cn_disc('让简单的顶层使用变得真正简单')

disc(
    """
<para lindent="+36">It should be possible to create a simple chart with minimum lines of
code, yet have it 'do the right things' with sensible automatic
settings. The pie chart snippets above do this. If a real chart has
many subcomponents, you still should not need to interact with them
unless you want to customize what they do.</para>"""
)
cn_disc('<para lindent="+36">应该可以用最少的代码行来创建一个简单的图表，'
        '并通过合理的自动设置让它 "做正确的事情"。'
        '上面的饼图片段就是这样做的。'
        '如果一个真正的图表有许多子组件，'
        '您仍然不需要与它们交互，除非您想自定义它们的功能。</para>')


disc("<i>Allow precise positioning </i>")
cn_disc('允许精确定位')

disc(
"""<para lindent="+36">An absolute requirement in publishing and graphic design is to control
the placing and style of every element. We will try to have properties
that specify things in fixed sizes and proportions of the drawing,
rather than having automatic resizing. Thus, the 'inner plot
rectangle' will not magically change when you make the font size of
the y labels bigger, even if this means your labels can spill out of
the left edge of the chart rectangle. It is your job to preview the
chart and choose sizes and spaces which will work.</para>"""
)
cn_disc('<para lindent="+36">在出版和平面设计中，一个绝对的要求是控制每个元素的位置和风格。'
        '我们会尽量让属性以固定的尺寸和绘图比例来指定事物，'
        '而不是有自动调整大小的功能。'
        '因此，当你把y标签的字体大小变大时，"内图矩形" 不会神奇地改变，'
        '即使这意味着你的标签可以溢出图表矩形的左边缘。'
        '你的工作是预览图表，并选择能用的大小和空间。</para>')


disc(
"""<para lindent="+36">Some things do need to be automatic. For example, if you want to fit N
bars into a 200 point space and don't know N in advance, we specify
bar separation as a percentage of the width of a bar rather than a
point size, and let the chart work it out. This is still deterministic
and controllable.</para>"""
)
cn_disc('<para lindent="+36">有些事情确实需要自动完成。'
        '例如，如果你想在一个200点的空间里放进N个条形图，而事先又不知道N，'
        '我们就把条形图的分隔指定为条形图宽度的百分比，而不是一个点的大小，让图表来计算。'
        '这样做还是具有确定性和可控性的。</para>')


disc("<i>Control child elements individually or as a group</i>")
cn_disc('<i>单独或分组控制子元素</i>')

disc(
    """<para lindent="+36">We use smart collection classes that let you customize a group of
things, or just one of them. For example you can do this in our
experimental pie chart:</para>"""
)
cn_disc('<para lindent="+36">我们使用智能集合类，让你自定义一组东西，或者只是其中的一个。'
        '例如你可以在我们的实验饼图中这样做。</para>')


eg(
    """
d = Drawing(400,200)
pc = Pie()
pc.x = 150
pc.y = 50
pc.data = [10,20,30,40,50,60]
pc.labels = ['a','b','c','d','e','f']
pc.slices.strokeWidth=0.5
pc.slices[3].popout = 20
pc.slices[3].strokeWidth = 2
pc.slices[3].strokeDashArray = [2,2]
pc.slices[3].labelRadius = 1.75
pc.slices[3].fontColor = colors.red
d.add(pc, '')
"""
)

disc(
"""<para lindent="+36">pc.slices[3] actually lazily creates a little object which holds
information about the slice in question; this will be used to format a
fourth slice at draw-time if there is one.</para>"""
)
cn_disc('<para lindent="+36"> $pc.slices[3]$ 实际上是懒惰地创建了一个小对象，'
        '它保存了有关片子的信息；'
        '如果有第四个片子的话，这个对象将在绘制时被用来格式化。</para>')


disc("<i>Only expose things you should change </i>")
cn_disc('<i>只揭露你应该改变的事情</i>')

disc(
    """<para lindent="+36">It would be wrong from a statistical viewpoint to let you directly
adjust the angle of one of the pie slices in the above example, since
that is determined by the data. So not everything will be exposed
through the public properties. There may be 'back doors' to let you
violate this when you really need to, or methods to provide advanced
functionality, but in general properties will be orthogonal.</para>"""
)
cn_disc('<para lindent="+36">从统计学的角度来看，让你直接调整上面例子中的一个饼片的角度是错误的，因为这是由数据决定的。'
        '所以并不是所有的东西都会通过公共属性暴露出来。'
        '可能会有 "后门 "让你在真正需要的时候违反这一点，'
        '或者提供高级功能的方法，但一般来说，属性会是正交的。</para>')


disc("<i>Composition and component based </i>")
cn_disc('<i>组成和成分</i>')

disc(
"""<para lindent="+36">Charts are built out of reusable child widgets. A Legend is an
easy-to-grasp example. If you need a specialized type of legend (e.g.
circular colour swatches), you should subclass the standard Legend
widget. Then you could either do something like...</para>"""
)
cn_disc('<para lindent="+36">图表是由可重复使用的儿童部件构建的。'
        '图例是一个易于掌握的例子。'
        '如果你需要一个特殊类型的图例（例如圆形色板），'
        '你应该将标准的图例部件子类化。然后你可以做一些像...</para>')

eg(
    """
c = MyChartWithLegend()
c.legend = MyNewLegendClass()    # just change it
c.legend.swatchRadius = 5    # set a property only relevant to the new one
c.data = [10,20,30]   #   and then configure as usual...
"""
)

disc(
"""<para lindent="+36">...or create/modify your own chart or drawing class which creates one
of these by default. This is also very relevant for time series
charts, where there can be many styles of x axis.</para>"""
)
cn_disc('<para lindent="+36">...或者创建/修改你自己的图表或绘图类，默认创建其中一个。'
        '这对于时间序列图来说也是非常重要的，因为在时间序列图中，X轴可以有很多样式。</para>')


disc(
"""<para lindent="+36">Top level chart classes will create a number of such components, and
then either call methods or set private properties to tell them their
height and position - all the stuff which should be done for you and
which you cannot customise. We are working on modelling what the
components should be and will publish their APIs here as a consensus
emerges.</para>"""
)
cn_disc('<para lindent="+36">'
        '顶层图表类会创建一些这样的组件，然后调用方法或设置私有属性来告诉它们的高度和位置'
        '--所有这些东西都应该为你做，而你无法定制。'
        '我们正在努力模拟这些组件应该是什么，'
        '并将在达成共识后在这里发布它们的API。</para>')


disc("<i>Multiples </i>")
cn_disc('<i>倍数</i>')

disc(
"""<para lindent="+36">A corollary of the component approach is that you can create diagrams
with multiple charts, or custom data graphics. Our favourite example
of what we are aiming for is the weather report in our gallery
contributed by a user; we'd like to make it easy to create such
drawings, hook the building blocks up to their legends, and feed that
data in a consistent way.</para>"""
)
cn_disc('<para lindent="+36">组件方法的一个必然结果是，'
        '你可以用多个图表或自定义数据图形来创建图表。'
        '我们最喜欢的例子是我们图库中由用户贡献的天气报告；'
        '我们希望能够轻松创建这样的图，将构件与它们的图例挂钩，'
        '并以一致的方式提供这些数据。</para>')

disc(
    """<para lindent="+36">(If you want to see the image, it is available on our website
<font color="blue"><a href="https://www.reportlab.com/media/imadj/data/RLIMG_e5e5cb85cc0a555f5433528ac38c5884.PDF">here</a></font>)</para>"""
)
cn_disc('<para lindent="+36">(如果你想看图片，可以在我们的网站上找到。'
        '<font color="blue">'
        '<a href="https://www.reportlab.com/media/imadj/'
        'data/RLIMG_e5e5cb85cc0a555f5433528ac38c5884.PDF">'
        '这儿</a></font>)</para>')



##heading3("Key Concepts and Components")
# heading3("Overview")
cn_heading3('概述')

disc(
"""A chart or plot is an object which is placed on a drawing; it is not
itself a drawing. You can thus control where it goes, put several on
the same drawing, or add annotations."""
)
cn_disc('图表或图是一个放置在图纸上的对象，'
        '它本身不是一个图纸。因此，你可以控制它的位置，在同一张图上放几个，或者添加注释。')


disc(
"""Charts have two axes; axes may be Value or Category axes. Axes in turn
have a Labels property which lets you configure all text labels or
each one individually. Most of the configuration details which vary
from chart to chart relate to axis properties, or axis labels."""
)
cn_disc('图表有两个轴，轴可以是 $Value$ 轴或 $Category$ 轴。'
        '轴又有一个 Labels 属性，可以让你配置所有的文本标签或单独配置每个标签。'
        '不同图表的大多数配置细节都与轴属性或轴标签有关。')


disc(
"""Objects expose properties through the interfaces discussed in the
previous section; these are all optional and are there to let the end
user configure the appearance. Things which must be set for a chart to
work, and essential communication between a chart and its components,
are handled through methods."""
)
cn_disc('对象通过上一节中讨论的接口暴露出属性；'
        '这些都是可选的，是为了让最终用户配置外观。'
        '为了使图表工作而必须设置的东西，'
        '以及图表和它的组件之间的基本通信，都是通过方法来处理的。')


disc(
    """You can subclass any chart component and use your replacement instead
of the original provided you implement the essential methods and properties."""
)
cn_disc('你可以对任何图表组件进行子类化，'
        '并使用你的替代品来代替原来的组件，只要你实现了基本的方法和属性。')

# heading2("Labels")
cn_heading2('$Labels$ 属性')

disc(
    """
A label is a string of text attached to some chart element.
They are used on axes, for titles or alongside axes, or attached
to individual data points. Labels may contain newline characters, but only 
one font.
"""
)
cn_disc('标签是附加在某些图表元素上的一串文本。'
        '它们用于坐标轴、标题或坐标轴旁，或附加到单个数据点上。'
        '标签可以包含换行符，但只能用一种字体。')


disc(
"""The text and 'origin' of a label are typically set by its parent
object. They are accessed by methods rather than properties. Thus, the
X axis decides the 'reference point' for each tick mark label and the
numeric or date text for each label. However, the end user can set
properties of the label (or collection of labels) directly to affect
its position relative to this origin and all of its formatting."""
)
cn_disc('标签的文本和 "origin" 通常由其父对象设置。'
        '它们是通过方法而不是属性来访问的。'
        '因此，X轴决定了每个刻度线标签的 "reference point" （参考点）'
        '和每个标签的数字或日期文本。'
        '然而，最终用户可以直接设置标签（或标签集合）的属性，'
        '以影响其相对于该原点的位置及其所有格式化。')

eg(
    """
from reportlab.graphics import shapes
from reportlab.graphics.charts.textlabels import Label

d = Drawing(200, 100)

# mark the origin of the label
d.add(Circle(100,90, 5, fillColor=colors.green))

lab = Label()
lab.setOrigin(100,90)
lab.boxAnchor = 'ne'
lab.angle = 45
lab.dx = 0
lab.dy = -20
lab.boxStrokeColor = colors.green
lab.setText('Some\nMulti-Line\nLabel')

d.add(lab)
"""
)

d = Drawing(200, 100)

# mark the origin of the label
d.add(Circle(100, 90, 5, fillColor=colors.green))

lab = Label()
lab.setOrigin(100, 90)
lab.boxAnchor = 'ne'
lab.angle = 45
lab.dx = 0
lab.dy = -20
lab.boxStrokeColor = colors.green
lab.setText('Some\nMulti-Line\nLabel')

d.add(lab)

# draw(d, 'Label example')
cn_draw(d, '$Label$ 示例')



disc(
    """
In the drawing above, the label is defined relative to the green blob.
The text box should have its north-east corner ten points down from
the origin, and be rotated by 45 degrees about that corner.
"""
)
cn_disc('在上图中，标签是相对于绿色小球定义的。文本框的东北角应在原点向下10点，并围绕该角旋转45度。')


disc(
    """
At present labels have the following properties, which we believe are
sufficient for all charts we have seen to date:
"""
)
cn_disc('目前，标签具有以下特性，我们认为这些特性对我们迄今所看到的所有图表都是足够的。')


disc("")

data = [
    ["Property", "Meaning"],
    ["dx", """The label's x displacement."""],
    ["dy", """The label's y displacement."""],
    [
        "angle",
        """The angle of rotation (counterclockwise) applied to the label.""",
    ],
    [
        "boxAnchor",
        "The label's box anchor, one of 'n', 'e', 'w', 's', 'ne', 'nw', 'se', 'sw'.",
    ],
    [
        "textAnchor",
        """The place where to anchor the label's text, one of 'start', 'middle', 'end'.""",
    ],
    ["boxFillColor", """The fill color used in the label's box."""],
    ["boxStrokeColor", "The stroke color used in the label's box."],
    ["boxStrokeWidth", """The line width of the label's box."""],
    ["fontName", """The label's font name."""],
    ["fontSize", """The label's font size."""],
    ["leading", """The leading value of the label's text lines."""],
    ["x", """The X-coordinate of the reference point."""],
    ["y", """The Y-coordinate of the reference point."""],
    ["width", """The label's width."""],
    ["height", """The label's height."""],
]
t = Table(data, colWidths=(100, 330))
t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'Times-Bold', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'Times-Roman', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
# getStory().append(t)
# caption("""Table <seq template="%(Chapter)s-%(Table+)s"/> - Label properties""")


cn_data = [
    ["属性", "描述"],
    ["dx", """标签的 X 位移。"""],
    ["dy", """标签的 Y 位移。"""],
    [
        "angle",
        "标签的旋转角度（逆时针）。",
    ],
    [
        "boxAnchor",
        "标签的框锚，'n'、'e'、'w'、's'、'ne'、'nw'、'se'、'sw'中的一种。",
    ],
    [
        "textAnchor",
        '标签文字的固定位置，"start"、"middle"、"end"中的一个。',
    ],
    ["boxFillColor", '标签框中使用的填充颜色。'],
    ["boxStrokeColor", "标签框中使用的笔触颜色。"],
    ["boxStrokeWidth", '标签框的线宽。'],
    ["fontName", '标签的字体名称。'],
    ["fontSize", '标签的字体大小。'],
    ["leading", '标签文字行的前导值。(leading)'],
    ["x", '参考点的X坐标。'],
    ["y", '参考点的Y坐标。'],
    ["width", '标签的宽度。'],
    ["height", '标签的高度。'],
]
cn_t = Table(cn_data, colWidths=(100, 330))
cn_t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'SourceHanSansSC', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'SourceHanSansSC', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
getStory().append(cn_t)
cn_caption('表 <seq template="%(Chapter)s - %(Table+)s"/> - Label 属性')

disc(
    """
To see many more examples of $Label$ objects with different
combinations of properties, please have a look into the
ReportLab test suite in the folder $tests$, run the
script $test_charts_textlabels.py$ and look at the PDF document
it generates!
"""
)
cn_disc('要查看更多的具有不同属性组合的 $Label$ 对象的例子，'
        '请查看文件夹 $tests$ 中的ReportLab测试套件，'
        '运行脚本 $test_charts_textlabels.py$ 并查看它所生成的PDF文档。')


heading2("Axes")

disc(
    """
We identify two basic kinds of axes - <i>Value</i> and <i>Category</i>
ones. Both come in horizontal and vertical flavors.
Both can be subclassed to make very specific kinds of axis.
For example, if you have complex rules for which dates to display
in a time series application, or want irregular scaling, you override
the axis and make a new one.
"""
)
cn_disc('我们确定了两种基本的轴 '
        '--<i>Value</i>和<i>Category</i>。'
        '这两种轴都有水平和垂直的味道。'
        '两者都可以被子类化来制作非常特殊类型的轴。'
        '例如，如果您有复杂的规则，在时间序列应用程序中显示哪些日期，或者想要不规则的缩放，'
        '您可以覆盖该轴并创建一个新的轴。')

disc(
    """
Axes are responsible for determining the mapping from data to image
coordinates; transforming points on request from the chart; drawing
themselves and their tick marks, grid lines and axis labels.
"""
)
cn_disc('轴负责确定从数据到图像坐标的映射；'
        '根据图表的要求变换点；'
        '绘制自己及其刻度线、网格线和轴标签。')

disc(
    """
This drawing shows two axes, one of each kind, which have been created
directly without reference to any chart:
"""
)
cn_disc('这张图显示了两个轴，每一种都有一个，'
        '它们是在没有参考任何图表的情况下直接创建的。')


drawing = Drawing(400, 200)

data = [(10, 20, 30, 40), (15, 22, 37, 42)]

xAxis = XCategoryAxis()
xAxis.setPosition(75, 75, 300)
xAxis.configure(data)
# xAxis.categoryNames = ['Beer', 'Wine', 'Meat', 'Cannelloni']
xAxis.categoryNames = ['啤酒', '葡萄酒', '牛肉', '碎肉卷']
xAxis.labels.boxAnchor = 'n'
xAxis.labels[3].dy = -15
xAxis.labels[3].angle = 30
# xAxis.labels[3].fontName = 'Times-Bold'
xAxis.labels.fontName = 'SourceHanSansSC'

yAxis = YValueAxis()
yAxis.setPosition(50, 50, 125)
yAxis.configure(data)

drawing.add(xAxis)
drawing.add(yAxis)

# draw(drawing, 'Two isolated axes')
cn_draw(drawing, '两个孤立的轴')


disc("Here is the code that created them: ")
cn_disc('下面是创建它们的代码。')


eg(
    """
from reportlab.graphics import shapes
from reportlab.graphics.charts.axes import XCategoryAxis,YValueAxis

drawing = Drawing(400, 200)

data = [(10, 20, 30, 40), (15, 22, 37, 42)]

xAxis = XCategoryAxis()
xAxis.setPosition(75, 75, 300)
xAxis.configure(data)
# xAxis.categoryNames = ['Beer', 'Wine', 'Meat', 'Cannelloni']
xAxis.categoryNames = ['啤酒', '葡萄酒', '牛肉', '碎肉卷']
xAxis.labels.boxAnchor = 'n'
xAxis.labels[3].dy = -15
xAxis.labels[3].angle = 30
# xAxis.labels[3].fontName = 'Times-Bold'
xAxis.labels.fontName = 'SourceHanSansSC'

yAxis = YValueAxis()
yAxis.setPosition(50, 50, 125)
yAxis.configure(data)

drawing.add(xAxis)
drawing.add(yAxis)
"""
)

disc(
    """
Remember that, usually, you won't have to create axes directly;
when using a standard chart, it comes with ready-made axes.
The methods are what the chart uses to configure it and take care
of the geometry. However, we will talk through them in detail below.
The orthogonally dual axes to those we describe have essentially
the same properties, except for those refering to ticks.
"""
)
cn_disc('请记住，通常情况下，你不必直接创建轴；'
        '当使用标准图表时，它自带现成的轴。'
        '这些方法是图表用来配置它和处理几何体的。'
        '不过，下面我们将详细介绍它们。'
        '正交双轴到我们描述的那些轴，除了指的是刻度线外，其他的属性基本相同。')


# heading3("XCategoryAxis class")
cn_heading3('$XCategoryAxis$ 类')

disc(
    """
A Category Axis doesn't really have a scale; it just divides itself
into equal-sized buckets. It is simpler than a value axis.
The chart (or programmer) sets its location with the method
$setPosition(x, y, length)$. The next stage is to show it the data so that it can configure
itself. This is easy for a category axis - it just counts the number of
data points in one of the data series. The $reversed$ attribute (if 1)
indicates that the categories should be reversed.
When the drawing is drawn, the axis can provide some help to the
chart with its $scale()$ method, which tells the chart where
a given category begins and ends on the page. We have not yet seen any need 
to let people override the widths or positions of categories.
"""
)
cn_disc('类别轴并没有真正的刻度，它只是把自己分成大小相等的 $buckets$ 。'
        '它比值轴更简单。图表（或程序员）用方法 $setPosition(x, y, length)$ 设置它的位置。'
        '下一个阶段是向它显示数据，以便它能够自行配置。'
        '对于类别轴来说，这很容易'
        '--它只是计算其中一个数据系列中的数据点数量。'
        '$reversed$ 属性（如果是1）表示类别应该反过来。'
        '绘制时，该轴可以通过其 $scale()$ 方法为图表提供一些帮助，'
        '该方法告诉图表一个给定类别在页面上的开始和结束位置。'
        '我们还没有看到任何让人们覆盖类别的宽度或位置的需求。')


disc("An XCategoryAxis has the following editable properties:")
cn_disc('一个 $XCategoryAxis$ 类有以下可编辑的属性。')


disc("")

data = [
    ["Property", "Meaning"],
    [
        "visible",
        """Should the axis be drawn at all? Sometimes you don't want
to display one or both axes, but they still need to be there as
they manage the scaling of points.""",
    ],
    ["strokeColor", "Color of the axis"],
    [
        "strokeDashArray",
        """Whether to draw axis with a dash and, if so, what kind.
Defaults to None""",
    ],
    ["strokeWidth", "Width of axis in points"],
    [
        "tickUp",
        """How far above the axis should the tick marks protrude?
(Note that making this equal to chart height gives you a gridline)""",
    ],
    ["tickDown", """How far below the axis should the tick mark protrude?"""],
    [
        "categoryNames",
        """Either None, or a list of strings. This should have the
same length as each data series.""",
    ],
    [
        "labels",
        """A collection of labels for the tick marks. By default the 'north'
of each text label (i.e top centre) is positioned 5 points down
from the centre of each category on the axis. You may redefine
any property of the whole label group or of any one label. If
categoryNames=None, no labels are drawn.""",
    ],
    [
        "title",
        """Not Implemented Yet. This needs to be like a label, but also
lets you set the text directly. It would have a default
location below the axis.""",
    ],
]
t = Table(data, colWidths=(100, 330))
t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'Times-Bold', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'Times-Roman', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
# getStory().append(t)
# caption(
#     """Table <seq template="%(Chapter)s-%(Table+)s"/> - XCategoryAxis properties"""
# )

cn_data = [
    ["属性", "描述"],
    [
        "visible",
        '轴是否应该被绘制？有时你不想显示一个或两个轴，\n'
        '但它们仍然需要存在，因为它们管理着点的缩放。',
    ],
    ["strokeColor", "轴的颜色"],
    [
        "strokeDashArray",
        '是否要用破折号画轴，如果要画，画什么样的轴。默认值为"None"。',
    ],
    ["strokeWidth", "轴的宽度，以点为单位（points）"],
    [
        "tickUp",
        '刻度线应突出到轴上方多远？\n'
        '（请注意，使其等于图表高度会给您一条网格线）',
    ],
    ["tickDown", '刻度线应突出到轴下方多远？'],
    [
        "categoryNames",
        '$None$ 或字符串列表。 该长度应与每个数据系列的长度相同。',
    ],
    [
        "labels",
        '刻度线标签的集合。 \n'
        '默认情况下，每个文本标签的“$north$” (北)（即顶部中心）\n'
        '位于轴上每个类别的中心下方5点处。\n'
        '您可以重新定义整个标签组或任何一个标签的任何属性。 \n'
        '如果 $categoryNames=None$，则不会绘制标签。',
    ],
    [
        "title",
        '尚未实现。 这需要像一个标签，但也可以让您直接设置文本。 \n'
        '它在轴下方将具有默认位置。',
    ],
]
cn_t = Table(cn_data, colWidths=(100, 330))
cn_t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'SourceHanSansSC', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'SourceHanSansSC', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
getStory().append(cn_t)
cn_caption('表 <seq template="%(Chapter)s - %(Table+)s"/> - $XCategoryAxis$ 类的属性')


# heading3("YValueAxis")
cn_heading3('$YValueAxis$ 类')

disc(
    """
The left axis in the diagram is a YValueAxis.
A Value Axis differs from a Category Axis in that each point along
its length corresponds to a y value in chart space.
It is the job of the axis to configure itself, and to convert Y values
from chart space to points on demand to assist the parent chart in
plotting.
"""
)
cn_disc('图中的左轴是 $YValueAxis$。 '
        '值轴与类别轴的不同之处在于，沿其长度的每个点都对应于图表空间中的 $y$ 值。 '
        '轴的工作是配置自身，并将 $Y$ 值从图表空间转换为按需点，以辅助父图表进行绘制。')


disc(
    """
$setPosition(x, y, length)$ and $configure(data)$ work exactly as
for a category axis. If you have not fully specified the maximum, minimum and tick
interval, then $configure()$ results in the axis choosing suitable
values. Once configured, the value axis can convert y data values to drawing
space with the $scale()$ method. Thus:
"""
)
cn_disc('$setPosition(x, y, length)$和$configure(data)$的作用与类别轴完全相同。 '
        '如果尚未完全指定最大，最小和刻度间隔，则 $configure()$ 会导致轴选择合适的值。'
        '配置完成后，值轴可以使用 $scale()$ 方法将 y 个数据值转换为绘图空间。 从而：')


eg(
    """
>>> yAxis = YValueAxis()
>>> yAxis.setPosition(50, 50, 125)
>>> data = [(10, 20, 30, 40),(15, 22, 37, 42)]
>>> yAxis.configure(data)
>>> yAxis.scale(10)  # should be bottom of chart
50.0
>>> yAxis.scale(40)  # should be near the top
167.1875
>>>
"""
)

disc(
"""By default, the highest data point is aligned with the top of the
axis, the lowest with the bottom of the axis, and the axis choose
'nice round numbers' for its tickmark points. You may override these
settings with the properties below. """
)

cn_disc("默认情况下，"
     "最高的数据点与轴的顶部对齐，最低的数据点与轴的底部对齐，"
     "轴为其刻度线点选择 $'nice round numbers'$ (漂亮的整数)。"
     "您可以用下面的属性覆盖这些设置。")

data = [
    ["Property", "Meaning"],
    [
        "visible",
        """Should the axis be drawn at all? Sometimes you don't want
to display one or both axes, but they still need to be there as
they manage the scaling of points.""",
    ],
    ["strokeColor", "Color of the axis"],
    [
        "strokeDashArray",
        """Whether to draw axis with a dash and, if so, what kind.
Defaults to None""",
    ],
    ["strokeWidth", "Width of axis in points"],
    [
        "tickLeft",
        """How far to the left of the axis should the tick marks protrude?
(Note that making this equal to chart height gives you a gridline)""",
    ],
    [
        "tickRight",
        """How far to the right of the axis should the tick mark protrude?""",
    ],
    [
        "valueMin",
        """The y value to which the bottom of the axis should correspond.
Default value is None in which case the axis sets it to the lowest
actual data point (e.g. 10 in the example above). It is common to set
this to zero to avoid misleading the eye.""",
    ],
    [
        "valueMax",
        """The y value to which the top of the axis should correspond.
Default value is None in which case the axis sets it to the highest
actual data point (e.g. 42 in the example above). It is common to set
this to a 'round number' so data bars do not quite reach the top.""",
    ],
    [
        "valueStep",
        """The y change between tick intervals. By default this is
None, and the chart tries to pick 'nice round numbers' which are
just wider than the minimumTickSpacing below.""",
    ],
    ["valueSteps", """A list of numbers at which to place ticks."""],
    [
        "minimumTickSpacing",
        """This is used when valueStep is set to None, and ignored
otherwise. The designer specified that tick marks should be no
closer than X points apart (based, presumably, on considerations
of the label font size and angle). The chart tries values of the
type 1,2,5,10,20,50,100... (going down below 1 if necessary) until
it finds an interval which is greater than the desired spacing, and
uses this for the step.""",
    ],
    [
        "labelTextFormat",
        """This determines what goes in the labels. Unlike a category
axis which accepts fixed strings, the labels on a ValueAxis are
supposed to be numbers. You may provide either a 'format string'
like '%0.2f' (show two decimal places), or an arbitrary function
which accepts a number and returns a string. One use for the
latter is to convert a timestamp to a readable year-month-day
format.""",
    ],
    [
        "title",
        """Not Implemented Yet. This needs to be like a label, but also
lets you set the text directly. It would have a default
location below the axis.""",
    ],
]
t = Table(data, colWidths=(100, 330))
t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'Times-Bold', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'Times-Roman', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
# getStory().append(t)
# caption(
#     """Table <seq template="%(Chapter)s-%(Table+)s"/> - YValueAxis properties"""
# )

cn_data = [
    ["属性", "描述"],
    [
        "visible",
        '轴是否应该被绘制？有时你不想显示一个或两个轴，\n'
        '但它们仍然需要存在，因为它们管理着点的缩放。',
    ],
    ["strokeColor", "轴的颜色"],
    [
        "strokeDashArray",
        '是否要用破折号画轴，如果要画，画什么样的轴。默认值为"None"。',
    ],
    ["strokeWidth", "轴的宽度，以点为单位（points）"],
    [
        "tickLeft",
        '刻度线应突出到轴的左侧多远？\n'
        '（请注意，使其等于图表宽度会给您一条网格线）',
    ],
    [
        "tickRight",
        '刻度线应突出到轴的右侧多远？',
    ],
    [
        "valueMin",
        '轴底部应对应的 y 值。 默认值为 None，在这种情况下，\n'
        '轴会将其设置为最低的实际数据点（例如，上例中为10）。 \n'
        '通常将其设置为零以避免误导眼睛。',
    ],
    [
        "valueMax",
        '轴顶部应对应的 y 值。 默认值为 None，在这种情况下，\n'
        '轴会将其设置为最高实际数据点（例如，上例中为42）。\n'
        '通常将其设置为“整数”，这样数据条就不会到达顶部。',
    ],
    [
        "valueStep",
        'y在刻度间隔之间变化。 默认情况下，此值为“None”，\n'
        '图表尝试选择比下面的最小刻度间距更宽的“很好的整数”。',
    ],
    ["valueSteps", '放置刻度的数字列表。'],
    [
        "minimumTickSpacing",
        '当$valueStep$设置为$None$时使用，否则忽略。 \n'
        '设计人员指定刻度线之间的距离不应小于X点（大概是基于标签字体大小和角度的考虑）。 \n'
        '图表尝试使用1,2,5,10,20,50,100 ...（如有必要，请减小到1以下）类型的值，\n'
        '直到找到大于所需间隔的间隔，并将其用于 $step$。',
    ],
    [
        "labelTextFormat",
        '这确定了标签中的内容。 与接受固定字符串的类别轴不同，\n'
        '$ValueAxis$ 上的标签应为数字。 \n'
        '您可以提供“$％0.2f$”之类的“格式字符串”（显示两位小数），\n'
        '也可以提供一个接受数字并返回字符串的任意函数。 \n'
        '后者的一种用法是将时间戳转换为可读的年月日格式。',
    ],
    [
        "title",
        '尚未实现。 这需要像一个标签，但也可以让您直接设置文本。\n'
        '它在轴下方将具有默认位置。',
    ],
]
cn_t = Table(cn_data, colWidths=(100, 330))
cn_t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'SourceHanSansSC', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'SourceHanSansSC', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
getStory().append(cn_t)
cn_caption(
    """表 <seq template="%(Chapter)s - %(Table+)s"/> - $YValueAxis$ 类属性"""
)

disc(
    """
The $valueSteps$ property lets you explicitly specify the
tick mark locations, so you don't have to follow regular intervals.
Hence, you can plot month ends and month end dates with a couple of
helper functions, and without needing special time series chart
classes. The following code show how to create a simple $XValueAxis$ with 
special tick intervals. Make sure to set the $valueSteps$ attribute before 
calling the configure method!
"""
)
cn_disc('$valueSteps$属性让您明确指定刻度线的位置，因此您不必遵循常规的时间间隔。'
        '因此，你可以通过几个辅助函数来绘制月末和月末日期，而且不需要特殊的时间序列图表类。'
        '下面的代码显示了如何创建一个简单的 $XValueAxis$ 与特殊的刻度间隔。'
        '请确保在调用配置方法之前设置 $valueSteps$ 属性!')

eg(
    """
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.axes import XValueAxis

drawing = Drawing(400, 100)

data = [(10, 20, 30, 40)]

xAxis = XValueAxis()
xAxis.setPosition(75, 50, 300)
xAxis.valueSteps = [10, 15, 20, 30, 35, 40]
xAxis.configure(data)
xAxis.labels.boxAnchor = 'n'

drawing.add(xAxis)
"""
)

drawing = Drawing(400, 100)

data = [(10, 20, 30, 40)]

xAxis = XValueAxis()
xAxis.setPosition(75, 50, 300)
xAxis.valueSteps = [10, 15, 20, 30, 35, 40]
xAxis.configure(data)
xAxis.labels.boxAnchor = 'n'

drawing.add(xAxis)

# draw(drawing, 'An axis with non-equidistant tick marks')
cn_draw(drawing, '带非等距刻度线的轴')

disc(
    """
In addition to these properties, all axes classes have three
properties describing how to join two of them to each other.
Again, this is interesting only if you define your own charts
or want to modify the appearance of an existing chart using
such axes.
These properties are listed here only very briefly for now,
but you can find a host of sample functions in the module
$reportlab/graphics/axes.py$ which you can examine...
"""
)
cn_disc('除了这些属性之外，所有的轴类都有三个属性，描述如何将其中的两个轴相互连接。'
        '再次强调，只有当你定义你自己的图表或者想使用这些坐标轴修改现有图表的外观时，这才是有趣的。'
        '这些属性在这里只是非常简单的列出，'
        '但你可以在$reportlab/graphics/axes.py$模块中找到大量的示例函数，'
        '你可以检查......')


disc(
    """
One axis is joined to another, by calling the method
$joinToAxis(otherAxis, mode, pos)$ on the first axis,
with $mode$ and $pos$ being the properties described by
$joinAxisMode$ and $joinAxisPos$, respectively.
$'points'$ means to use an absolute value, and $'value'$
to use a relative value (both indicated by the the
$joinAxisPos$ property) along the axis.
"""
)
cn_disc("通过在第一个轴上调用方法$joinToAxis(otherAxis, mode, pos)$"
        "将一个轴连接到另一个轴，"
        "$mode$和$pos$分别是$joinAxisMode$和$joinAxisPos$描述的属性。"
        "$'points'$表示使用绝对值，$'value'$表示使用沿轴的相对值"
        "（均由$joinAxisPos$属性表示）。")


disc("")

data = [
    ["Property", "Meaning"],
    ["joinAxis", """Join both axes if true."""],
    [
        "joinAxisMode",
        """Mode used for connecting axis ('bottom', 'top', 'left', 'right', 'value', 'points', None).""",
    ],
    ["joinAxisPos", """Position at which to join with other axis."""],
]
t = Table(data, colWidths=(100, 330))
t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'Times-Bold', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'Times-Roman', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
# getStory().append(t)
# caption(
#     """Table <seq template="%(Chapter)s-%(Table+)s"/> - Axes joining properties"""
# )

cn_data = [
    ["属性", "描述"],
    ["joinAxis", """如果为真，则连接两个轴。"""],
    [
        "joinAxisMode",
        "用于连接轴的模式 \n"
        "('bottom', 'top', 'left', 'right', 'value', 'points', None).",
    ],
    ["joinAxisPos", '与其他轴连接的位置。'],
]
cn_t = Table(cn_data, colWidths=(100, 330))
cn_t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'SourceHanSansSC', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'SourceHanSansSC', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
getStory().append(cn_t)
cn_caption(
    """表 <seq template="%(Chapter)s - %(Table+)s"/> - $Axes joining$ 属性列表"""
)

# heading2("Bar Charts")
cn_heading2('柱状图')

disc(
    """
This describes our current $VerticalBarChart$ class, which uses the
axes and labels above. We think it is step in the right direction but is is
far from final. Note that people we speak to are divided about 50/50 on 
whether to call this a 'Vertical' or 'Horizontal' bar chart.
We chose this name because 'Vertical' appears next to 'Bar', so
we take it to mean that the bars rather than the category axis
are vertical.
"""
)
cn_disc("这描述了我们目前的$VerticalBarChart$类，它使用了上面的轴和标签。"
        "我们认为这是正确方向的一步，但还远未到最后的阶段。"
        "请注意，与我们交谈过的人对这是'垂直'还是'水平'条形图的看法不一。"
        "我们选择这个名字是因为'垂直'出现在'条形图'旁边，"
        "所以我们认为它的意思是条形图而不是类别轴是垂直的。")

disc(
    """
As usual, we will start with an example:
"""
)
cn_disc('与往常一样，我们将从一个示例开始：')


drawing = Drawing(400, 200)

data = [(13, 5, 20, 22, 37, 45, 19, 4), (14, 6, 21, 23, 38, 46, 20, 5)]

bc = VerticalBarChart()
bc.x = 50
bc.y = 50
bc.height = 125
bc.width = 300
bc.data = data
bc.strokeColor = colors.black

bc.valueAxis.valueMin = 0
bc.valueAxis.valueMax = 50
bc.valueAxis.valueStep = 10

bc.categoryAxis.labels.boxAnchor = 'ne'
bc.categoryAxis.labels.dx = 8
bc.categoryAxis.labels.dy = -2
bc.categoryAxis.labels.angle = 30
bc.categoryAxis.categoryNames = [
    'Jan-99',
    'Feb-99',
    'Mar-99',
    'Apr-99',
    'May-99',
    'Jun-99',
    'Jul-99',
    'Aug-99',
]

drawing.add(bc)

# draw(drawing, 'Simple bar chart with two data series')
cn_draw(drawing, '具有两个数据系列的简单柱状图')


eg(
    """
    # code to produce the above chart

    from reportlab.graphics.shapes import Drawing
    from reportlab.graphics.charts.barcharts import VerticalBarChart

    drawing = Drawing(400, 200)

    data = [
            (13, 5, 20, 22, 37, 45, 19, 4),
            (14, 6, 21, 23, 38, 46, 20, 5)
            ]

    bc = VerticalBarChart()
    bc.x = 50
    bc.y = 50
    bc.height = 125
    bc.width = 300
    bc.data = data
    bc.strokeColor = colors.black

    bc.valueAxis.valueMin = 0
    bc.valueAxis.valueMax = 50
    bc.valueAxis.valueStep = 10

    bc.categoryAxis.labels.boxAnchor = 'ne'
    bc.categoryAxis.labels.dx = 8
    bc.categoryAxis.labels.dy = -2
    bc.categoryAxis.labels.angle = 30
    bc.categoryAxis.categoryNames = ['Jan-99','Feb-99','Mar-99',
           'Apr-99','May-99','Jun-99','Jul-99','Aug-99']

    drawing.add(bc)
"""
)

disc(
    """
Most of this code is concerned with setting up the axes and
labels, which we have already covered.
Here are the top-level properties of the $VerticalBarChart$ class:
"""
)
cn_disc('这段代码的大部分内容是关于设置坐标轴和标签的，我们已经介绍过了，'
        '下面是$VerticalBarChart$类的顶层属性。')


disc("")

data = [
    ["Property", "Meaning"],
    [
        "data",
        """This should be a "list of lists of numbers" or "list of
tuples of numbers". If you have just one series, write it as
data = [(10,20,30,42),]""",
    ],
    [
        "x, y, width, height",
        """These define the inner 'plot rectangle'. We
highlighted this with a yellow border above. Note that it is
your job to place the chart on the drawing in a way which leaves
room for all the axis labels and tickmarks. We specify this 'inner
rectangle' because it makes it very easy to lay out multiple charts
in a consistent manner.""",
    ],
    [
        "strokeColor",
        """Defaults to None. This will draw a border around the
plot rectangle, which may be useful in debugging. Axes will
overwrite this.""",
    ],
    [
        "fillColor",
        """Defaults to None. This will fill the plot rectangle with
a solid color. (Note that we could implement dashArray etc.
as for any other solid shape)""",
    ],
    [
        "useAbsolute",
        """Defaults to 0. If 1, the three properties below are
absolute values in points (which means you can make a chart
where the bars stick out from the plot rectangle); if 0,
they are relative quantities and indicate the proportional
widths of the elements involved.""",
    ],
    ["barWidth", """As it says. Defaults to 10."""],
    [
        "groupSpacing",
        """Defaults to 5. This is the space between each group of
bars. If you have only one series, use groupSpacing and not
barSpacing to split them up. Half of the groupSpacing is used
before the first bar in the chart, and another half at the end.""",
    ],
    [
        "barSpacing",
        """Defaults to 0. This is the spacing between bars in each
group. If you wanted a little gap between green and red bars in
the example above, you would make this non-zero.""",
    ],
    [
        "barLabelFormat",
        """Defaults to None. As with the YValueAxis, if you supply
a function or format string then labels will be drawn next to each bar
showing the numeric value. They are positioned automatically
above the bar for positive values and below for negative ones.""",
    ],
    [
        "barLabels",
        """A collection of labels used to format all bar labels. Since
this is a two-dimensional array, you may explicitly format the
third label of the second series using this syntax:
  chart.barLabels[(1,2)].fontSize = 12""",
    ],
    [
        "valueAxis",
        """The value axis, which may be formatted as described
previously.""",
    ],
    [
        "categoryAxis",
        """The category axis, which may be formatted as described
previously.""",
    ],
    [
        "title",
        """Not Implemented Yet. This needs to be like a label, but also
lets you set the text directly. It would have a default
location below the axis.""",
    ],
]
t = Table(data, colWidths=(100, 330))
t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'Times-Bold', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'Times-Roman', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
# getStory().append(t)
# caption(
#     """Table <seq template="%(Chapter)s-%(Table+)s"/> - VerticalBarChart properties"""
# )

cn_data = [
    ["属性", "描述"],
    [
        "data",
        '这应该是“数字列表列表”或“数字元组列表”。 \n'
        '如果只有一个系列，则将其写为 data=[(10,20,30,42),]',
    ],
    [
        "x, y, width, height",
        '这些定义了内部的 "绘图矩形"。\n'
        '我们在上面用黄色边框突出显示了这个矩形。\n'
        '请注意，您的工作是将图表放置在图纸上，为所有的轴标签和刻度线留出空间。\n'
        '我们指定这个 "内矩形" 是因为它可以很容易地以一致的方式布置多个图表。',
    ],
    [
        "strokeColor",
        '默认为 None。 这将在绘图矩形周围绘制边框，\n'
        '这可能对调试很有用。 轴将覆盖此位置。',
    ],
    [
        "fillColor",
        '默认为 None。 这将用纯色填充绘图矩形。 \n'
        '（请注意，我们可以像其他任何实心形状一样实现 $dashArray$ 等）',
    ],
    [
        "useAbsolute",
        '默认为0. 如果为1，则下面的三个属性是绝对值，以点为单位 \n'
        '（这意味着你可以制作一个图表，其中的条形图从绘图矩形中伸出来）；\n'
        '如果为0，则是相对量，表示相关元素的比例宽度。',
    ],
    ["barWidth", """柱状宽度. 默认为 10."""],
    [
        "groupSpacing",
        '默认值为5。这是每组条形图之间的间距，\n'
        '如果只有一个系列，请使用$groupSpacing$而不是barSpacing来分割它们。\n'
        '$groupSpacing$的一半用于图表的第一个条形图之前，另一半用于结尾。',
    ],
    [
        "barSpacing",
        '默认值为0。这是每个组中的条之间的间距。 \n'
        '如果在上面的示例中绿色和红色条形之间要有一点间隙，则可以将其设置为非零。',
    ],
    [
        "barLabelFormat",
        '默认为 None。 与$YValueAxis$一样，\n'
        '如果提供函数或格式字符串，则会在每个显示数值的条旁边绘制标签。 \n'
        '对于正值，它们会自动定位在条的上方，\n'
        '对于负值，它们会自动位于下方。',
    ],
    [
        "barLabels",
        '用于格式化所有条形标签的标签集合。\n'
        '由于这是一个二维数组，您可以使用此语法明确格式化第二个系列的第三个标签：\n'
        'chart.barLabels[(1,2)].fontSize = 12。',
    ],
    [
        "valueAxis",
        '值轴，其格式可如前所述。',
    ],
    [
        "categoryAxis",
        '类别轴，其格式可如前所述。',
    ],
    [
        "title",
        '还没有实现。这需要像一个标签一样，\n'
        '但也可以让你直接设置文本。它将有一个默认的位置在轴的下方。',
    ],
]
cn_t = Table(cn_data, colWidths=(100, 330))
cn_t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'SourceHanSansSC', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'SourceHanSansSC', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
getStory().append(cn_t)
cn_caption('表 <seq template="%(Chapter)s - %(Table+)s"/>'
           ' - 柱状图($VerticalBarChart$) 属性列表')


disc(
    """
From this table we deduce that adding the following lines to our code
above should double the spacing between bar groups (the $groupSpacing$
attribute has a default value of five points) and we should also see
some tiny space between bars of the same group ($barSpacing$).
"""
)
cn_disc('从该表中我们可以得出结论，在上面的代码中加入以下几行，'
        '应该会使条形图组之间的间距增加一倍($groupSpacing$属性的默认值为5点)，'
        '我们还应该看到同一组的条形组之间有一些微小的空间($barSpacing$)。')

eg(
    """
    bc.groupSpacing = 10
    bc.barSpacing = 2.5
"""
)

disc(
    """
And, in fact, this is exactly what we can see after adding these
lines to the code above.
Notice how the width of the individual bars has changed as well.
This is because the space added between the bars has to be 'taken'
from somewhere as the total chart width stays unchanged.
"""
)
cn_disc('而且，实际上，这就是在将这些行添加到上面的代码之后所能看到的。 '
        '注意各个条的宽度也如何变化。 '
        '这是因为随着总图表宽度保持不变，必须从某处“占用”条形之间的空格。')

drawing = Drawing(400, 200)

data = [(13, 5, 20, 22, 37, 45, 19, 4), (14, 6, 21, 23, 38, 46, 20, 5)]

bc = VerticalBarChart()
bc.x = 50
bc.y = 50
bc.height = 125
bc.width = 300
bc.data = data
bc.strokeColor = colors.black

bc.groupSpacing = 10
bc.barSpacing = 2.5

bc.valueAxis.valueMin = 0
bc.valueAxis.valueMax = 50
bc.valueAxis.valueStep = 10

bc.categoryAxis.labels.boxAnchor = 'ne'
bc.categoryAxis.labels.dx = 8
bc.categoryAxis.labels.dy = -2
bc.categoryAxis.labels.angle = 30
bc.categoryAxis.categoryNames = [
    'Jan-99',
    'Feb-99',
    'Mar-99',
    'Apr-99',
    'May-99',
    'Jun-99',
    'Jul-99',
    'Aug-99',
]

drawing.add(bc)

# draw(drawing, 'Like before, but with modified spacing')
cn_draw(drawing, '像以前一样，但间距已更改')

disc(
    """
Bars labels are automatically displayed for negative values
<i>below</i> the lower end of the bar for positive values
<i>above</i> the upper end of the other ones.
"""
)
cn_disc('条形图标签将自动显示为条形下限以下的负值，其他条形上限值以上的正值。')



disc(
    """
Stacked bars are also supported for vertical bar graphs.
You enable this layout for your chart by setting the $style$
attribute to $'stacked'$ on the $categoryAxis$.
"""
)
cn_disc("垂直条形图也支持堆叠条形图。"
        "您可以通过在 $categoryAxis$ 上设置 $style$ 属性"
        "为 $'stacked'$ 来为您的图表启用这种布局。")


eg(
    """
    bc.categoryAxis.style = 'stacked'
"""
)

disc(
    """
Here is an example of the previous chart values arranged
in the stacked style.
"""
)
cn_disc('下面是以之前的图表值为例，以叠加的方式排列。')


drawing = Drawing(400, 200)

data = [(13, 5, 20, 22, 37, 45, 19, 4), (14, 6, 21, 23, 38, 46, 20, 5)]

bc = VerticalBarChart()
bc.x = 50
bc.y = 50
bc.height = 125
bc.width = 300
bc.data = data
bc.strokeColor = colors.black

bc.groupSpacing = 10
bc.barSpacing = 2.5

bc.valueAxis.valueMin = 0
bc.valueAxis.valueMax = 100
bc.valueAxis.valueStep = 20

bc.categoryAxis.labels.boxAnchor = 'ne'
bc.categoryAxis.labels.dx = 8
bc.categoryAxis.labels.dy = -2
bc.categoryAxis.labels.angle = 30
bc.categoryAxis.categoryNames = [
    'Jan-99',
    'Feb-99',
    'Mar-99',
    'Apr-99',
    'May-99',
    'Jun-99',
    'Jul-99',
    'Aug-99',
]
bc.categoryAxis.style = 'stacked'

drawing.add(bc)
# draw(drawing, 'Stacking bars on top of each other.')
cn_draw(drawing, '柱状叠加图')


##Property Value
##data This should be a "list of lists of numbers" or "list of tuples of numbers". If you have just one series, write it as
##data = [(10,20,30,42),]
##
##x, y, width, height These define the inner 'plot rectangle'. We highlighted this with a yellow border above. Note that it is your job to place the chart on the drawing in a way which leaves room for all the axis labels and tickmarks. We specify this 'inner rectangle' because it makes it very easy to lay out multiple charts in a consistent manner.
##strokeColor Defaults to None. This will draw a border around the plot rectangle, which may be useful in debugging. Axes will overwrite this.
##fillColor Defaults to None. This will fill the plot rectangle with a solid color. (Note that we could implement dashArray etc. as for any other solid shape)
##barLabelFormat This is a format string or function used for displaying labels above each bar. We're working on ways to position these labels so that they work for positive and negative bars.
##useAbsolute Defaults to 0. If 1, the three properties below are absolute values in points (which means you can make a chart where the bars stick out from the plot rectangle); if 0, they are relative quantities and indicate the proportional widths of the elements involved.
##barWidth As it says. Defaults to 10.
##groupSpacing Defaults to 5. This is the space between each group of bars. If you have only one series, use groupSpacing and not barSpacing to split them up. Half of the groupSpacing is used before the first bar in the chart, and another half at the end.
##barSpacing Defaults to 0. This is the spacing between bars in each group. If you wanted a little gap between green and red bars in the example above, you would make this non-zero.
##barLabelFormat Defaults to None. As with the YValueAxis, if you supply a function or format string then labels will be drawn next to each bar showing the numeric value.
##barLabels A collection of labels used to format all bar labels. Since this is a two-dimensional array, you may explicitly format the third label of the second series using this syntax:
##    chart.barLabels[(1,2)].fontSize = 12
##
##valueAxis The value axis, which may be formatted as described previously
##categoryAxis The categoryAxis, which may be formatted as described previously
##title, subTitle Not implemented yet. These would be label-like objects whose text could be set directly and which would appear in sensible locations. For now, you can just place extra strings on the drawing.


# heading2("Line Charts")
cn_heading2('折线图')

disc(
    """
We consider "Line Charts" to be essentially the same as
"Bar Charts", but with lines instead of bars.
Both share the same pair of Category/Value axes pairs.
This is in contrast to "Line Plots", where both axes are
<i>Value</i> axes.
"""
)
cn_disc('我们认为 "折线图"($Line Charts$)  与 "柱状图"($Bar Charts$) 本质上是一样的，只是用线代替了条。'
        '两者共享同一对类别/数值轴对。这与 "线图"不同，'
        '在"线图"($Line Plots$) 中，两个轴都是<i>值</i>轴。')


disc(
    """
The following code and its output shall serve as a simple
example. More explanation will follow. For the time being you can also study 
the output of running the tool $reportlab/lib/graphdocpy.py$ withough any 
arguments and search the generated PDF document for examples of Line Charts.
"""
)
cn_disc('以下代码及其输出将作为一个简单的例子。'
        '后面会有更多的解释。'
        '目前，您也可以研究运行 $reportlab/lib/graphdocpy.py$ 工具的输出，'
        '并在生成的PDF文档中搜索柱状图($Line Charts$)的例子。')


eg(
    """
from reportlab.graphics.charts.linecharts import HorizontalLineChart

drawing = Drawing(400, 200)

data = [
    (13, 5, 20, 22, 37, 45, 19, 4),
    (5, 20, 46, 38, 23, 21, 6, 14)
]

lc = HorizontalLineChart()
lc.x = 50
lc.y = 50
lc.height = 125
lc.width = 300
lc.data = data
lc.joinedLines = 1
catNames = 'Jan Feb Mar Apr May Jun Jul Aug'.split(' ')
lc.categoryAxis.categoryNames = catNames
lc.categoryAxis.labels.boxAnchor = 'n'
lc.valueAxis.valueMin = 0
lc.valueAxis.valueMax = 60
lc.valueAxis.valueStep = 15
lc.lines[0].strokeWidth = 2
lc.lines[1].strokeWidth = 1.5
drawing.add(lc)
"""
)


drawing = Drawing(400, 200)

data = [(13, 5, 20, 22, 37, 45, 19, 4), (5, 20, 46, 38, 23, 21, 6, 14)]

lc = HorizontalLineChart()
lc.x = 50
lc.y = 50
lc.height = 125
lc.width = 300
lc.data = data
lc.joinedLines = 1
catNames = 'Jan Feb Mar Apr May Jun Jul Aug'.split(' ')
lc.categoryAxis.categoryNames = catNames
lc.categoryAxis.labels.boxAnchor = 'n'
lc.valueAxis.valueMin = 0
lc.valueAxis.valueMax = 60
lc.valueAxis.valueStep = 15
lc.lines[0].strokeWidth = 2
lc.lines[1].strokeWidth = 1.5
drawing.add(lc)

# draw(drawing, 'HorizontalLineChart sample')
cn_draw(drawing, '折线图示例 $HorizontalLineChart$')

disc("")

data = [
    ["Property", "Meaning"],
    ["data", "Data to be plotted, list of (lists of) numbers."],
    [
        "x, y, width, height",
        """Bounding box of the line chart.
Note that x and y do NOT specify the centre but the bottom left corner""",
    ],
    [
        "valueAxis",
        """The value axis, which may be formatted as described previously.""",
    ],
    [
        "categoryAxis",
        """The category axis, which may be formatted as described previously.""",
    ],
    [
        "strokeColor",
        """Defaults to None. This will draw a border around the plot rectangle,
which may be useful in debugging. Axes will overwrite this.""",
    ],
    [
        "fillColor",
        """Defaults to None. This will fill the plot rectangle with a solid color.""",
    ],
    ["lines.strokeColor", """Color of the line."""],
    ["lines.strokeWidth", """Width of the line."""],
    [
        "lineLabels",
        """A collection of labels used to format all line labels. Since
this is a two-dimensional array, you may explicitly format the
third label of the second line using this syntax:
  chart.lineLabels[(1,2)].fontSize = 12""",
    ],
    [
        "lineLabelFormat",
        """Defaults to None. As with the YValueAxis, if you supply
a function or format string then labels will be drawn next
to each line showing the numeric value. You can also set it
to 'values' to display the values explicity defined in lineLabelArray.""",
    ],
    [
        "lineLabelArray",
        """Explicit array of line label values, must match size of data if present.
These labels values will be displayed only if the property
lineLabelFormat above is set to 'values'.""",
    ],
]
t = Table(data, colWidths=(100, 330))
t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'Times-Bold', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'Times-Roman', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
# getStory().append(t)
# caption(
#     """Table <seq template="%(Chapter)s-%(Table+)s"/> - HorizontalLineChart properties"""
# )

cn_data = [
    ["属性", "描述"],
    ["data", "要绘制的数据，（列表）整数清单。"],
    [
        "x, y, width, height",
        '折线图的边界框。 请注意，x和y不指定中心，而是左下角',
    ],
    [
        "valueAxis",
        '值轴，其格式可如前所述。',
    ],
    [
        "categoryAxis",
        '类别轴，其格式可如前所述。',
    ],
    [
        "strokeColor",
        '默认值为 "None"。这将在绘图矩形周围画一个边框，\n'
        '这在调试时可能很有用。轴将覆盖它。',
    ],
    [
        "fillColor",
        """默认为 None。 这将用纯色填充绘图矩形。""",
    ],
    ["lines.strokeColor", '线的颜色'],
    ["lines.strokeWidth", '线的宽度'],
    [
        "lineLabels",
        '用于格式化所有行标签的标签集合。由于这是一个二维数组，\n'
        '您可以使用以下语法明确格式化第二行的第三个标签：\n'
        'chart.lineLabels[(1,2)].fontSize = 12。',
    ],
    [
        "lineLabelFormat",
        '默认值为 "None"。与YValueAxis一样，如果你提供一个函数或格式字符串，\n'
        '那么标签将被绘制在每一行的旁边，显示数值。\n'
        '您也可以将其设置为\'values\'，以显示在lineLabelArray中明确定义的值。',
    ],
    [
        "lineLabelArray",
        "行标签值的显式数组，如果存在，必须与数据的大小相匹配。\n"
        "只有当上面的属性$lineLabelFormat$被设置为'values'时，\n"
        "这些标签值才会被显示。",
    ],
]
cn_t = Table(cn_data, colWidths=(100, 330))
cn_t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'SourceHanSansSC', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'SourceHanSansSC', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
getStory().append(cn_t)
cn_caption('表 <seq template="%(Chapter)s - %(Table+)s"/>'
           ' - 折线图属性列表 $HorizontalLineChart$')

# heading2("Line Plots")
cn_heading2('点线图')

disc(
    """
Below we show a more complex example of a Line Plot that
also uses some experimental features like line markers
placed at each data point.
"""
)
cn_disc('下面我们展示了一个更复杂的线型图的例子，'
        '也使用了一些实验功能，比如在每个数据点放置线型标记。')


eg(
    """
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker

drawing = Drawing(400, 200)

data = [
    ((1,1), (2,2), (2.5,1), (3,3), (4,5)),
    ((1,2), (2,3), (2.5,2), (3.5,5), (4,6))
]

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = data
lp.joinedLines = 1
lp.lines[0].symbol = makeMarker('FilledCircle')
lp.lines[1].symbol = makeMarker('Circle')
lp.lineLabelFormat = '%2.0f'
lp.strokeColor = colors.black
lp.xValueAxis.valueMin = 0
lp.xValueAxis.valueMax = 5
lp.xValueAxis.valueSteps = [1, 2, 2.5, 3, 4, 5]
lp.xValueAxis.labelTextFormat = '%2.1f'
lp.yValueAxis.valueMin = 0
lp.yValueAxis.valueMax = 7
lp.yValueAxis.valueSteps = [1, 2, 3, 5, 6]

drawing.add(lp)
"""
)

drawing = Drawing(400, 200)

data = [
    ((1, 1), (2, 2), (2.5, 1), (3, 3), (4, 5)),
    ((1, 2), (2, 3), (2.5, 2), (3.5, 5), (4, 6)),
]

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = data
lp.joinedLines = 1
lp.lines[0].symbol = makeMarker('FilledCircle')
lp.lines[1].symbol = makeMarker('Circle')
lp.lineLabelFormat = '%2.0f'
lp.strokeColor = colors.black
lp.xValueAxis.valueMin = 0
lp.xValueAxis.valueMax = 5
lp.xValueAxis.valueSteps = [1, 2, 2.5, 3, 4, 5]
lp.xValueAxis.labelTextFormat = '%2.1f'
lp.yValueAxis.valueMin = 0
lp.yValueAxis.valueMax = 7
lp.yValueAxis.valueSteps = [1, 2, 3, 5, 6]

drawing.add(lp)

# draw(drawing, 'LinePlot sample')
cn_draw(drawing, '点线图示例 $LinePlot$')


disc("")

data = [
    ["Property", "Meaning"],
    ["data", "Data to be plotted, list of (lists of) numbers."],
    [
        "x, y, width, height",
        """Bounding box of the line chart.
Note that x and y do NOT specify the centre but the bottom left corner""",
    ],
    [
        "xValueAxis",
        """The vertical value axis, which may be formatted as described previously.""",
    ],
    [
        "yValueAxis",
        """The horizontal value axis, which may be formatted as described previously.""",
    ],
    [
        "strokeColor",
        """Defaults to None. This will draw a border around the plot rectangle,
which may be useful in debugging. Axes will overwrite this.""",
    ],
    [
        "strokeWidth",
        """Defaults to None. Width of the border around the plot rectangle.""",
    ],
    [
        "fillColor",
        """Defaults to None. This will fill the plot rectangle with a solid color.""",
    ],
    ["lines.strokeColor", """Color of the line."""],
    ["lines.strokeWidth", """Width of the line."""],
    [
        "lines.symbol",
        """Marker used for each point.
You can create a new marker using the function makeMarker().
For example to use a circle, the function call would be makeMarker('Circle')""",
    ],
    [
        "lineLabels",
        """A collection of labels used to format all line labels. Since
this is a two-dimensional array, you may explicitly format the
third label of the second line using this syntax:
  chart.lineLabels[(1,2)].fontSize = 12""",
    ],
    [
        "lineLabelFormat",
        """Defaults to None. As with the YValueAxis, if you supply
a function or format string then labels will be drawn next
to each line showing the numeric value. You can also set it
to 'values' to display the values explicity defined in lineLabelArray.""",
    ],
    [
        "lineLabelArray",
        """Explicit array of line label values, must match size of data if present.
These labels values will be displayed only if the property
lineLabelFormat above is set to 'values'.""",
    ],
]
t = Table(data, colWidths=(100, 330))
t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'Times-Bold', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'Times-Roman', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
# getStory().append(t)
# caption(
#     """Table <seq template="%(Chapter)s-%(Table+)s"/> - LinePlot properties"""
# )

cn_data = [
    ["属性", "描述"],
    ["data", "要绘制的数据，（列表）整数清单。"],
    [
        "x, y, width, height",
        '折线图的边界框。 请注意，x和y不指定中心，而是左下角',
    ],
    [
        "xValueAxis",
        '垂直值轴，其格式可以如上所述。',
    ],
    [
        "yValueAxis",
        '水平值轴，其格式可以如上所述。',
    ],
    [
        "strokeColor",
        '默认为None。 这将在绘图矩形周围绘制边框，\n'
        '这可能对调试很有用。 轴将覆盖此位置。',
    ],
    [
        "strokeWidth",
        '默认为None。 绘图矩形周围边框的宽度。',
    ],
    [
        "fillColor",
        '默认为None。 这将用纯色填充绘图矩形。',
    ],
    ["lines.strokeColor", '线的颜色。'],
    ["lines.strokeWidth", '线的宽度'],
    [
        "lines.symbol",
        '每个点使用的标记。您可以使用函数$makeMarker()$创建一个新的标记。\n'
        '例如，要使用一个圆，函数调用是makeMarker(\'Circle\')',
    ],
    [
        "lineLabels",
        '用于格式化所有行标签的标签集合。\n'
        '由于这是一个二维数组，您可以使用以下语法明确格式化第二行的第三个标签：\n'
        'chart.lineLabels[(1,2)].fontSize = 12。',
    ],
    [
        "lineLabelFormat",
        '默认值为 None。与$YValueAxis$一样，如果你提供一个函数或格式字符串，'
        '那么标签将被绘制在每一行的旁边，显示数值。您也可以将其设置为\'values\'，'
        '以显示在$lineLabelArray$中明确定义的值。',
    ],
    [
        "lineLabelArray",
        '行标签值的显式数组，如果存在，必须与数据的大小相匹配。'
        '只有当上面的属性lineLabelFormat被设置为\'values\'时，'
        '这些标签值才会被显示。',
    ],
]
cn_t = Table(cn_data, colWidths=(100, 330))
cn_t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'SourceHanSansSC', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'SourceHanSansSC', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
getStory().append(cn_t)
cn_caption(
    """表 <seq template="%(Chapter)s-%(Table+)s"/> - 点线图属性 $LinePlot$"""
)


# heading2("Pie Charts")
cn_heading2('饼图')

disc(
    """
As usual, we will start with an example:
"""
)
cn_disc('像往常一样，我们将从一个例子开始:')


eg(
    """
from reportlab.graphics.charts.piecharts import Pie
d = Drawing(200, 100)

pc = Pie()
pc.x = 65
pc.y = 15
pc.width = 70
pc.height = 70
pc.data = [10,20,30,40,50,60]
pc.labels = ['a','b','c','d','e','f']

pc.slices.strokeWidth=0.5
pc.slices[3].popout = 10
pc.slices[3].strokeWidth = 2
pc.slices[3].strokeDashArray = [2,2]
pc.slices[3].labelRadius = 1.75
pc.slices[3].fontColor = colors.red
d.add(pc)
"""
)

d = Drawing(400, 200)

pc = Pie()
pc.x = 125
pc.y = 25
pc.width = 150
pc.height = 150
pc.data = [10, 20, 30, 40, 50, 60]
pc.labels = ['a', 'b', 'c', 'd', 'e', 'f']

pc.slices.strokeWidth = 0.5
pc.slices[3].popout = 10
pc.slices[3].strokeWidth = 2
pc.slices[3].strokeDashArray = [2, 2]
pc.slices[3].labelRadius = 1.25
pc.slices[3].fontColor = colors.red

d.add(pc)

draw(d, 'A bare bones pie chart')
cn_draw(d, '凸出的饼图')

disc(
    """
Properties are covered below.
The pie has a 'slices' collection and we document wedge properties
in the same table.
"""
)
cn_disc('属性在下面介绍。 $pie$ 具有 “$slices$” 集合，我们在同一表中记录 $wedge$ 属性。')


disc("")

data = [
    ["Property", "Meaning"],
    ["data", "A list or tuple of numbers"],
    [
        "x, y, width, height",
        """Bounding box of the pie.
Note that x and y do NOT specify the centre but the bottom left
corner, and that width and height do not have to be equal;
pies may be elliptical and slices will be drawn correctly.""",
    ],
    [
        "labels",
        """None, or a list of strings.
Make it None if you don't want labels around the edge of the pie.
Since it is impossible to know the size of slices, we generally
discourage placing labels in or around pies; it is much better 
to put them in a legend alongside.""",
    ],
    [
        "startAngle",
        """Where is the start angle of the first pie slice?
The default is '90' which is twelve o'clock.""",
    ],
    [
        "direction",
        """Which direction do slices progress in?
The default is 'clockwise'.""",
    ],
    [
        "sideLabels",
        """This creates a chart with the labels in two columns,
one on either side.""",
    ],
    [
        "sideLabelsOffset",
        """This is a fraction of the width of the pie that defines the horizontal
distance between the pie and the columns of labels.""",
    ],
    [
        "simpleLabels",
        """Default is 1. Set to 0 to enable the use of customizable labels 
and of properties prefixed by label_ in the collection slices.""",
    ],
    [
        "slices",
        """Collection of slices.
This lets you customise each wedge, or individual ones. See below""",
    ],
    ["slices.strokeWidth", "Border width for wedge"],
    ["slices.strokeColor", "Border color"],
    ["slices.strokeDashArray", "Solid or dashed line configuration"],
    [
        "slices.popout",
        """How far out should the slice(s) stick from the centre of the pie?
Default is zero.""",
    ],
    ["slices.fontName", "Name of the label font"],
    ["slices.fontSize", "Size of the label font"],
    ["slices.fontColor", "Color of the label text"],
    [
        "slices.labelRadius",
        """This controls the anchor point for a text label.
It is a fraction of the radius; 0.7 will place the text inside the
pie, 1.2 will place it slightly outside. (note that if we add labels,
we will keep this to specify their anchor point)""",
    ],
]
t = Table(data, colWidths=(130, 300))
t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'Times-Bold', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'Times-Roman', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
# getStory().append(t)
# caption("""Table <seq template="%(Chapter)s-%(Table+)s"/> - Pie properties""")

cn_data = [
    ["属性", "描述"],
    ["data", "整数合集"],
    [
        "x, y, width, height",
        '饼图的边界框。 请注意，x和y不必指定中心，\n'
        '而是指定左下角，并且宽度和高度不必相等。 \n'
        '饼图可能是椭圆形的，并且会正确绘制切片。',
    ],
    [
        "labels",
        'None, 或者字符串合集. 如果您不希望饼图边缘周围有标签，\n'
        '请将其设为“None”。 \n'
        '由于不可能知道切片的大小，因此我们通常不建议在饼中或饼周围放置标签。 \n'
        '最好将它们放在图例中。\n',
    ],
    [
        "startAngle",
        '第一个饼片的起始角度是什么？默认为"90"，即 12 点钟方向。',
    ],
    [
        "direction",
        '切片的前进方向是什么？默认为 "clockwise"。(顺时针)',
    ],
    [
        "sideLabels",
        '这将创建一个标签在两边各一列的图表。',
    ],
    [
        "sideLabelsOffset",
        '这是饼图宽度的一部分，该宽度定义了饼图和标签列之间的水平距离。',
    ],
    [
        "simpleLabels",
        '默认为 1. 设置为0以启用自定义标签以及在集合切片中使用 label_ 前缀的属性。',
    ],
    [
        "slices",
        """切片的集合。这使您可以自定义每个扇形或单个扇形。 见下文""",
    ],
    ["slices.strokeWidth", "扇形边框宽度"],
    ["slices.strokeColor", "扇形边框颜色"],
    ["slices.strokeDashArray", "实线或虚线配置：['solid', 'dashed']"],
    [
        "slices.popout",
        '切片应从馅饼的中心伸出多远？ 默认值为零。',
    ],
    ["slices.fontName", "标签字体名称"],
    ["slices.fontSize", "标签字体大小"],
    ["slices.fontColor", "标签文字的颜色"],
    [
        "slices.labelRadius",
        '这控制文本标签的锚点。 它是半径的一小部分；\n'
        '0.7将文本放置在饼中，1.2将文本放置在饼外。 \n'
        '（请注意，如果我们添加标签，将保留此标签以指定其锚点）',
    ],
]
cn_t = Table(cn_data, colWidths=(130, 300))
cn_t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'SourceHanSansSC', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'SourceHanSansSC', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
getStory().append(cn_t)
cn_caption('表 <seq template="%(Chapter)s-%(Table+)s"/>'
           ' - 饼图属性 $Pie$')




# heading3("Customizing Labels")
cn_heading3('自定义标签')

disc(
    """
Each slide label can be customized individually by changing
the properties prefixed by $label_$ in the collection $slices$.
For example $pc.slices[2].label_angle = 10$ changes the angle 
of the third label.
"""
)
cn_disc('通过改变集合$slices$中以$label_$为前缀的属性，'
        '可以单独定制每个幻灯片标签。'
        '例如 $pc.slices[2].label_angle = 10$ 改变第三个标签的角度。')


disc(
    """
Before being able to use these customization properties, you need
to disable simple labels with: $pc.simplesLabels = 0$
"""
)
cn_disc('在使用这些自定义属性之前，您需要使用以下命令禁用简单标签：$pc.simplesLabels=0$')


disc("")

data = [
    ["Property", "Meaning"],
    ["label_dx", """X Offset of the label"""],
    ["label_dy", """Y Offset of the label"""],
    [
        "label_angle",
        """Angle of the label, default (0) is horizontal, 90 is vertical,
180 is upside down""",
    ],
    ["label_boxAnchor", """Anchoring point of the label"""],
    ["label_boxStrokeColor", """Border color for the label box"""],
    ["label_boxStrokeWidth", """Border width for the label box"""],
    ["label_boxFillColor", """Filling color of the label box"""],
    ["label_strokeColor", """Border color for the label text"""],
    ["label_strokeWidth", """Border width for the label text"""],
    ["label_text", """Text of the label"""],
    ["label_width", """Width of the label"""],
    ["label_maxWidth", """Maximum width the label can grow to"""],
    ["label_height", """Height of the label"""],
    ["label_textAnchor", """Maximum height the label can grow to"""],
    ["label_visible", """True if the label is to be drawn"""],
    ["label_topPadding", """Padding at top of box"""],
    ["label_leftPadding", """Padding at left of box"""],
    ["label_rightPadding", """Padding at right of box"""],
    ["label_bottomPadding", """Padding at bottom of box"""],
    ["label_simple_pointer", """Set to 1 for simple pointers"""],
    ["label_pointer_strokeColor", """Color of indicator line"""],
    ["label_pointer_strokeWidth", """Width of indicator line"""],
]
t = Table(data, colWidths=(130, 300))
t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'Times-Bold', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'Times-Roman', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
# getStory().append(t)
# caption(
#     """Table <seq template="%(Chapter)s-%(Table+)s"/> - Pie.slices label customization properties"""
# )

cn_data = [
    ["属性", "描述"],
    ["label_dx", 'X轴标签偏移'],
    ["label_dy", 'Y轴标签偏移'],
    [
        "label_angle",
        '标签的角度，默认（0）为水平，90为垂直，180为上下颠倒',
    ],
    ["label_boxAnchor", '标签的固定点'],
    ["label_boxStrokeColor", '标签框的边框颜色'],
    ["label_boxStrokeWidth", '标签框的边框宽度'],
    ["label_boxFillColor", '标签盒的填充颜色'],
    ["label_strokeColor", '标签文字的边框颜色'],
    ["label_strokeWidth", '标签文字的边框宽度'],
    ["label_text", '标签文字'],
    ["label_width", '标签宽度'],
    ["label_maxWidth", '标签可以增加到的最大宽度'],
    ["label_height", '标签高度'],
    ["label_textAnchor", '标签可以增加到的最大高度'],
    ["label_visible", '如果要绘制标签，则为True'],
    ["label_topPadding", '盒子的上边距(Padding at top of box)'],
    ["label_leftPadding", '盒子的左边距(Padding at left of box)'],
    ["label_rightPadding", '盒子的右边距(Padding at right of box)'],
    ["label_bottomPadding", '盒子的下边距(Padding at bottom of box)'],
    ["label_simple_pointer", '为简单指针设置为1(Set to 1 for simple pointers)'],
    ["label_pointer_strokeColor", '指示线颜色'],
    ["label_pointer_strokeWidth", '指示线宽度'],
]
cn_t = Table(cn_data, colWidths=(130, 300))
cn_t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'SourceHanSansSC', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'SourceHanSansSC', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
getStory().append(cn_t)
cn_caption('表 <seq template="%(Chapter)s - %(Table+)s"/>'
           ' - 扇形标签自定义属性 $Pie.slices custom label$')

# heading3("Side Labels")
cn_heading3('侧面标签')

disc(
    """
If the sideLabels attribute is set to true, then the labels of 
the slices are placed in two columns, one on either side of the 
pie and the start angle of the pie will be set automatically.
The anchor of the right hand column is set to 'start' and the 
anchor of the left hand column is set to 'end'.
The distance from the edge of the pie from the edge of either 
column is decided by the sideLabelsOffset attribute, which is 
a fraction of the width of the pie.
If xradius is changed, the pie can overlap the labels, and so 
we advise leaving xradius as None. There is an example below.
"""
)
cn_disc('如果 $sideLabels$ 属性被设置为 $true$，那么切片分为两列，两边各一列。 '
        '饼和饼的起始角度将被自动设置。'
        '右侧栏的锚点设置为 "start"，并设置了左手列的锚点设置为 "end"。'
        '饼的边缘与左手列中任何一个的边缘的距离。'
        '列由 $sideLabelsOffset$ 属性决定，该属性为饼的宽度的一小部分。'
        '如果改变 $xradius$，饼会与标签重叠，这样一来...。'
        '我们建议将 $xradius$ 改为 $None$。下面是一个例子。')

drawing5 = sample5()
# draw(drawing5, 'An example of a piechart with sideLabels =1')
cn_draw(drawing5, '一个 $sideLabels=1$ 的饼图示例')

disc(
    """
If you have sideLabels set to True, then some of the attributes 
become redundant, such as pointerLabelMode. Also sideLabelsOffset only 
changes the piechart if sideLabels is set to true.
"""
)
cn_disc('如果将 $sideLabels$ 设置为 $True$，则某些属性将变得多余，例如 $pointerLabelMode$。 '
        '同样，$sideLabelsOffset$ 仅在将 $sideLabels$ 设置为 $true$ 时更改饼图。')

# heading4("Some issues")
cn_heading4('一些问题')

disc(
    """
The pointers can cross if there are too many slices.
"""
)
cn_disc('如果切片过多，指针可能会交叉。')


drawing7 = sample7()
# draw(drawing7, 'An example of pointers crossing')
cn_draw(drawing7, '指针交叉的例子')

disc(
    """
Also the labels can overlap despite checkLabelOverlap if they 
correspond to slices that are not adjacent.
"""
)
cn_disc('另外，如果标签对应的片子不相邻，尽管有 $checkLabelOverlap$，标签也可以重叠。')


drawing8 = sample8()
# draw(drawing8, 'An example of labels overlapping')
cn_draw(drawing8, '标签重叠的示例')

heading2("Legends")
# cn_heading2('aaa')

disc(
    """
Various preliminary legend classes can be found but need a
cleanup to be consistent with the rest of the charting
model. Legends are the natural place to specify the colors and line
styles of charts; we propose that each chart is created with
a $legend$ attribute which is invisible. One would then do the following to 
specify colors:
"""
)
cn_disc('可以找到各种初步的图例类，但需要进行清理以与图表模型的其他部分保持一致。'
        '图例是指定图表颜色和线条风格的自然场所；'
        '我们建议每个图表都创建一个不可见的$legend$属性。'
        '然后，将执行以下操作以指定颜色：')


eg(
    """
myChart.legend.defaultColors = [red, green, blue]
"""
)

disc(
    """
One could also define a group of charts sharing the same legend:
"""
)
cn_disc('还可以定义一组共享相同图例的图表：')


eg(
    """
myLegend = Legend()
myLegend.defaultColor = [red, green.....] #yuck!
myLegend.columns = 2
# etc.
chart1.legend = myLegend
chart2.legend = myLegend
chart3.legend = myLegend
"""
)

# Hack to force a new paragraph before the todo() :-(
disc("")

todo(
    """Does this work? Is it an acceptable complication over specifying chart
colors directly?"""
)
cn_todo('这样行吗？ 直接指定图表颜色是否可以接受？')


# heading3("Remaining Issues")
cn_heading3('存在的问题')

disc(
    """
There are several issues that are <i>almost</i> solved, but for which
is is a bit too early to start making them really public.
Nevertheless, here is a list of things that are under way:
"""
)
cn_disc('有几个问题已经解决了，但现在开始真正公开这些问题还为时过早。'
        '不过，这里有一个正在进行的事情清单。')


bullet(
    """
Color specification - right now the chart has an undocumented property
$defaultColors$, which provides a list of colors to cycle through,
such that each data series gets its own color.
Right now, if you introduce a legend, you need to make sure it shares
the same list of colors. Most likely, this will be replaced with a scheme to 
specify a kind of legend containing attributes with different values for each data
series. This legend can then also be shared by several charts, but need not
be visible itself.
"""
)

bullet(
    """
Additional chart types - when the current design will have become more 
stable, we expect to add variants of bar charts to deal with percentile bars 
as well as the side-by-side variant seen here.
"""
)

cn_bullet('颜色规范: -- 现在图表有一个没文档化的属性 $defaultColors$, '
          '该属性提供要循环显示的颜色列表，以便每个数据系列都有自己的颜色。'
          '现在，如果你要引入图例，则需要确保它具有相同的颜色列表。'
          '最有可能的是，它将被一种方案取代，该方案指定一种图例，该图例包含每个数据系列具有不同值的属性。 '
          '然后，该图例也可以由多个图表共享，但本身不必可见。')

cn_bullet('额外的图表类型--当目前的设计变得更加稳定时，'
          '我们希望增加条形图的变体，以处理百分位条形图以及这里看到的并排变体。')

# heading3("Outlook")
cn_heading3('展望 ($Outlook$)')

disc(
    """
It will take some time to deal with the full range of chart types.
We expect to finalize bars and pies first and to produce trial
implementations of more general plots, thereafter.
"""
)
cn_disc('处理全部图表类型需要一些时间。我们预计将首先完成柱状图和饼图，然后试行更多的普通图。')


heading3("X-Y Plots")
cn_heading3('aaa')

disc(
    """
Most other plots involve two value axes and directly plotting
x-y data in some form.
The series can be plotted as lines, marker symbols, both, or
custom graphics such as open-high-low-close graphics.
All share the concepts of scaling and axis/title formatting.
At a certain point, a routine will loop over the data series and
'do something' with the data points at given x-y locations.
Given a basic line plot, it should be very easy to derive a
custom chart type just by overriding a single method - say,
$drawSeries()$.
"""
)
cn_disc('大多数其他图都涉及两个值轴，并以某种形式直接绘制x-y数据。 '
        '该系列可以绘制为线条，标记符号，两者兼而有之,'
        '或自定义图形（例如，开-高-低-闭图形）'
        '所有这些都具有缩放和轴/标题格式的概念。 '
        '在某一点上，一个例程将在数据序列上循环，并在给定的x-y位置上对数据点 "做一些事情"。'
        '给定一个基本的折线图，只需覆盖一个方法--比如说，$drawSeries()$，'
        '就可以很容易地推导出一个自定义的图表类型。')



# heading3("Marker customisation and custom shapes")
cn_heading3('自定义标记和自定义形状')

disc(
    """
Well known plotting packages such as excel, Mathematica and Excel
offer ranges of marker types to add to charts.
We can do better - you can write any kind of chart widget you
want and just tell the chart to use it as an example.
"""
)
cn_disc('众所周知的绘图软件包，如 $excel$、$Mathematica$和$Excel$，'
        '都提供了一系列的标记类型来添加到图表中。'
        '我们可以做得更好'
        '--你可以编写任何一种你想要的图表部件，只需告诉图表使用它作为例子。')



# heading4("Combination plots")
cn_heading4('组合图')

disc(
    """
Combining multiple plot types is really easy. You can just draw several 
charts (bar, line or whatever) in the same rectangle, suppressing axes as 
needed. So a chart could correlate a line with Scottish typhoid cases
over a 15 year period on the left axis with a set of bars showing
inflation rates on the right axis. If anyone can remind us where this example came from we'll
attribute it, and happily show the well-known graph as an example.
"""
)
cn_disc('结合多种绘图类型真的很容易。'
        '你只需在同一个矩形中绘制几个图表（条形图、线形图或其他什么图），'
        '根据需要取消显示轴。'
        '因此，一个图表可以将一条线与左轴上15年内的苏格兰伤寒病例相关联，'
        '右轴上有一组显示通货膨胀率的条形图。'
        '如果有谁能提醒我们这个例子的出处，'
        '我们会注明出处，并很高兴地展示这个著名的图表作为例子。')

# heading3("Interactive editors")
cn_heading3('互动式编辑')

disc(
    """
One principle of the Graphics package is to make all 'interesting'
properties of its graphic components accessible and changeable by
setting apropriate values of corresponding public attributes.
This makes it very tempting to build a tool like a GUI editor that
that helps you with doing that interactively.
"""
)
cn_disc('图形包的一个原则是使图形组件的所有 "有趣的" '
        '属性都可以通过设置相应的公共属性的适当值来访问和改变。'
        '这使得我们很想建立一个像GUI编辑器一样的工具，'
        '来帮助你交互式地完成这些工作。')


disc(
    """
ReportLab has built such a tool using the Tkinter toolkit that
loads pure Python code describing a drawing and records your
property editing operations. This "change history" is then used to create 
code for a subclass of that chart, say, that can be saved and used instantly 
just like any other chart or as a new starting point for another interactive 
editing session.
"""
)
cn_disc('ReportLab使用Tkinter工具箱构建了这样的工具，'
        '该工具箱可加载描述图纸的纯Python代码并记录您的属性编辑操作。 '
        '然后，此“更改历史记录”用于为该图表的子类创建代码，'
        '例如，可以像其他任何图表一样立即保存和使用该代码，'
        '或将其用作另一个交互式编辑会话的新起点。')


disc(
    """
This is still work in progress, though, and the conditions for
releasing this need to be further elaborated.
"""
)
cn_disc('不过这还在进行中，发布的条件还需要进一步细化。')



# heading3("Misc.")
cn_heading3('其他')

disc(
    """
This has not been an exhaustive look at all the chart classes.
Those classes are constantly being worked on.
To see exactly what is in the current distribution, use the
$graphdocpy.py$ utility. By default, it will run on reportlab/graphics, 
and produce a full report.
(If you want to run it on other modules or packages,
$graphdocpy.py -h$ prints a help message that will tell you how.)
"""
)
cn_disc('这并不是对所有图表类的详尽介绍。这些类还在不断地改进中。'
        '要查看当前发行版中的确切内容，请使用 $graphdocpy.py$工具。'
        '默认情况下，它将在 $reportlab/graphics$ 上运行，并生成一份完整的报告。'
        '(如果你想在其他模块或软件包上运行它，'
        '$graphdocpy.py -h$ 会打印出一条帮助信息，告诉你如何运行。)')


disc(
    """
This is the tool that was mentioned in the section on 'Documenting
Widgets'.
"""
)
cn_disc('这是“文档小部件” ($Documenting Widgets$) 部分中提到的工具')

