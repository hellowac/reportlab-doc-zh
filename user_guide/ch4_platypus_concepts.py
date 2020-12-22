# Copyright ReportLab Europe Ltd. 2000-2017
# see license.txt for license details
# history https://hg.reportlab.com/hg-public/reportlab/log/tip/docs/userguide/ch4_platypus_concepts.py
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
)
from utils import examples

# heading1("PLATYPUS - Page Layout and Typography Using Scripts")
cn_heading1("PLATYPUS - 使用脚本进行页面布局和排版。")

# heading2("Design Goals")
cn_heading2("全局设计")

disc(
    """
Platypus stands for &quot;Page Layout and Typography Using Scripts&quot;.  It is a high
level page layout library which lets you programmatically create complex
documents with a minimum of effort.
"""
)
cn_disc('Platypus是&quot;Page Layout and Typography Using Scripts&quot;的缩写。 '
        '它是一个高水平的页面布局库，让你可以用最少的努力以编程方式创建复杂的文档。')


disc(
    """
The design of Platypus seeks to separate "high level" layout decisions
from the document content as much as possible.  Thus, for example, paragraphs
are constructed using paragraph styles and pages are constructed
using page templates with the intention that hundreds of
documents with thousands of pages can be reformatted to different
style specifications with the modifications of a few lines in a single
shared file which contains the paragraph styles and page layout specifications.
"""
)
cn_disc('Platypus的设计力求将 "高层次 "的布局决定与文档内容尽可能分开。 '
        '例如，段落使用段落样式，页面使用页面模板，目的是让数百个有数千页的文件可以按照不同的样式规格重新格式化，'
        '只需在一个包含段落样式和页面布局规格的共享文件中修改几行即可。')

disc(
    """
The overall design of Platypus can be thought of has having
several layers, top down, these are"""
)
cn_disc('Platypus的整体设计可以认为有几个层次，自上而下，这些是')


disc("<b>$DocTemplates$</b> the outermost container for the document;")
cn_disc('<b>$DocTemplates$</b>文档的最外层容器。')


disc(
    "<b>$PageTemplates$</b> specifications for layouts of pages of various kinds;"
)
cn_disc('<b>$PageTemplates$</b>各种页面布局的规格。')


disc(
    "<b>$Frames$</b> specifications of regions in pages that can contain flowing text or graphics."
)
cn_disc('<b>$Frames$</b>页面中可包含流动文本或图形的区域规格。')


disc(
"""<b>$Flowables$</b> text or graphic elements that should be "flowed
into the document (i.e. things like images, paragraphs and tables, but not things
like page footers or fixed page graphics)."""
)
cn_disc('<b>$Flowables$</b>对应 "流入文档"的文本或图形元素'
        '（即图像、段落和表格等内容，但不包括页脚或固定页面图形等内容）。')


disc(
"""<b>$pdfgen.Canvas$</b> the lowest level which ultimately receives the painting of the
document from the other layers."""
)
cn_disc('<b>$pdfgen.Canvas$</b>为最终从其他图层接收文档绘画的最低层。')


# illust(
#     examples.doctemplateillustration, "Illustration of DocTemplate structure"
# )
cn_illust(examples.doctemplateillustration, 'DocTemplate 结构说明')

disc(
    """
The illustration above graphically illustrates the concepts of $DocTemplates$,
$PageTemplates$ and $Flowables$.  It is deceptive, however, because each
of the $PageTemplates$ actually may specify the format for any number of pages
(not just one as might be inferred from the diagram).
"""
)
cn_disc('上面的插图形象地说明了$DocTemplate$、$PageTemplate$和$Flowables$的概念。 '
        '然而，它具有欺骗性，因为每一个$PageTemplate$实际上可以指定任何数量的页面的格式'
        '（而不是像从图中推断的那样只指定一个）。')


disc(
    """
$DocTemplates$ contain one or more $PageTemplates$ each of which contain one or more
$Frames$. $Flowables$ are things which can be <i>flowed</i> into a $Frame$ e.g.
a $Paragraph$ or a $Table$.
"""
)
cn_disc('$DocTemplate$ 包含一个或多个 $PageTemplate$，'
        '每个 $PageTemplate$ 包含一个或多个$Frame$。'
        '$Flowables$ 是指可以<i>流入</i> $Frame$的东西，'
        '例如$Paragraph$或$Table$。')


disc(
    """
To use platypus you create a document from a $DocTemplate$ class and pass
a list of $Flowable$s to its $build$ method. The document
$build$ method knows how to process the list of flowables
into something reasonable.
"""
)
cn_disc('要使用platypus，你需要从$DocTemplate$类中创建一个文档，'
        '并向其$build$方法传递一个$Flowable$s列表。'
        'document的$build$方法知道如何将flowable列表处理成合理的东西。')


disc(
    """
Internally the $DocTemplate$ class implements page layout and formatting
using various events. Each of the events has a corresponding handler method
called $handle_XXX$ where $XXX$ is the event name. A typical event is
$frameBegin$ which occurs when the machinery begins to use a frame for the
first time.
"""
)
cn_disc('在内部，$DocTemplate$类使用各种事件来实现页面布局和格式化。'
        '每个事件都有一个对应的处理方法，称为 $handle_XXX$ ，'
        '其中 $XXX$ 是事件名称。'
        '一个典型的事件是$frameBegin$，'
        '它发生在机械开始第一次使用一个框架的时候。')


disc(
    """
A Platypus story consists of a sequence of basic elements called $Flowables$
and these elements drive the data driven Platypus formatting engine.
To modify the behavior of the engine a special kind of flowable, 
$ActionFlowables$, tell the layout engine to, for example, skip to the next
column or change to another $PageTemplate$.
"""
)
cn_disc('Platypus故事由一系列基本元素组成，这些元素被称为 "可流动元素"，'
        '它们驱动着数据驱动的Platypus格式化引擎。'
        '为了修改引擎的行为，一种特殊的可流式元素$ActionFlowables$告诉布局引擎，'
        '例如，跳到下一列或者换成另一个$PageTemplate$。')

# heading2("""Getting started""")
cn_heading2("开始")


disc(
    """Consider the following code sequence which provides
a very simple "hello world" example for Platypus."""
)
cn_disc('考虑以下代码序列，它为Platypus提供了一个非常简单的 "hello world "例子。')


eg(examples.platypussetup)

disc(
    """First we import some constructors, some paragraph styles
and other conveniences from other modules."""
)
cn_disc('首先，我们从其他模块中导入一些构造函数、一些段落样式和其他方便。')


eg(examples.platypusfirstpage)

disc(
    """We define the fixed features of the first page of the document
with the function above."""
)
cn_disc('我们用上面的函数定义文档首页的固定特征。')


eg(examples.platypusnextpage)

disc(
    """Since we want pages after the first to look different from the
first we define an alternate layout for the fixed features
of the other pages.  Note that the two functions above use
the $pdfgen$ level canvas operations to paint the annotations for
the pages.
"""
)
cn_disc('由于我们希望第一个页面之后的页面看起来与第一个页面不同，'
        '我们为其他页面的固定特征定义了一个备用布局。 '
        '请注意，上面的两个函数使用 $pdfgen$ 级别的画布操作来为页面绘制注释。')

eg(examples.platypusgo)

disc(
    """
Finally, we create a story and build the document.
Note that we are using a "canned" document template here which
comes pre-built with page templates.  We are also using a pre-built
paragraph style.  We are only using two types of flowables here
-- $Spacers$ and $Paragraphs$.  The first $Spacer$ ensures that the
Paragraphs skip past the title string.
"""
)
cn_disc('最后，我们创建一个故事并构建文档。'
        '请注意，我们在这里使用的是 "罐头 "文档模板，'
        '它是预建的页面模板。 我们还使用了预建的段落样式。 '
        '我们在这里只使用了两种类型的flowables--$Spacers$和$Paragraphs$。 '
        '第一个$Spacer$确保段落跳过标题字符串。')

disc(
    """
To see the output of this example program run the module
$docs/userguide/examples.py$ (from the ReportLab $docs$ distribution)
as a "top level script".  The script interpretation $python examples.py$ will
generate the Platypus output $phello.pdf$.
"""
)
cn_disc('要查看这个示例程序的输出，'
        '请以 "顶层脚本 "的形式运行模块 $docs/userguide/examples.py$'
        '（来自ReportLab $docs$发行版）。 '
        '脚本解释 $python examples.py$ 将生成 Platypus输出 $phello.pdf$。')

heading2("$Flowables$")
# cn_heading2("aaa")

disc(
    """
$Flowables$ are things which can be drawn and which have $wrap$, $draw$ and perhaps $split$ methods.
$Flowable$ is an abstract base class for things to be drawn and an instance knows its size
and draws in its own coordinate system (this requires the base API to provide an absolute coordinate
system when the $Flowable.draw$ method is called). To get an instance use $f=Flowable()$.
"""
)
cn_disc('$Flowables$是可以被绘制的东西，'
        '它有$wrap$, $draw$和可能的$split$方法。'
        '$Flowable$是一个抽象的基类，用于绘制事物，一个实例知道它的大小，'
        '并在它自己的坐标系中绘制(这需要基API在调用$Flowable.draw$方法时提供一个绝对坐标系)。'
        '要获得一个实例，使用 $f=Flowable()$。')

disc(
    """
It should be noted that the $Flowable$ class is an <i>abstract</i> class and is normally
only used as a base class.
"""
)
cn_disc('需要注意的是，$Flowable$类是一个<i>抽象</i>类，通常只作为基类使用。')

k = startKeep()
disc(
    """
To illustrate the general way in which $Flowables$ are used we show how a derived class $Paragraph$
is used and drawn on a canvas. $Paragraphs$ are so important they will get a whole chapter
to themselves.
"""
)
cn_disc('为了说明使用$Flowables$的一般方式，'
        '我们将展示如何在画布上使用和绘制衍生类$Paragraph$。'
        '$Paragraph$是如此重要，它们将有一整章的篇幅来介绍。')

eg(
    """
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph
    from reportlab.pdfgen.canvas import Canvas
    styleSheet = getSampleStyleSheet()
    style = styleSheet['BodyText']
    P=Paragraph('This is a very silly example',style)
    canv = Canvas('doc.pdf')
    aW = 460    # available width and height
    aH = 800
    w,h = P.wrap(aW, aH)    # find required space
    if w<=aW and h<=aH:
        P.drawOn(canv,0,aH)
        aH = aH - h         # reduce the available height
        canv.save()
    else:
        raise ValueError, "Not enough room"
"""
)
endKeep(k)

# heading3("$Flowable$ User Methods")
cn_heading3("$Flowable$ 用户方法")

eg('Flowable.draw()')
disc(
    """This will be called to ask the flowable to actually render itself.
The $Flowable$ class does not implement $draw$.
The calling code should ensure that the flowable has an attribute $canv$
which is the $pdfgen.Canvas$ which should be drawn to an that the $Canvas$
is in an appropriate state (as regards translations rotations, etc). Normally
this method will only be called internally by the $drawOn$ method. Derived classes
must implement this method.
"""
)
cn_disc('这将被调用来要求 $flowable$ 实际渲染自己。'
        '$Flowable$类没有实现$draw$。'
        '调用代码应该确保 $flowable$ 有一个属性$canv$，'
        '它是$pdfgen.Canvas$，它应该被绘制到$Canvas$上，'
        '并且$Canvas$处于一个适当的状态(就翻译、旋转等而言)。'
        '通常这个方法只在内部被$drawOn$方法调用，派生类必须实现这个方法。'
        '派生类必须实现这个方法。')

eg('Flowable.drawOn(canvas,x,y)')

disc(
    """
This is the method which controlling programs use to render the flowable to a particular
canvas. It handles the translation to the canvas coordinate (<i>x</i>,<i>y</i>) and ensuring that
the flowable has a $canv$ attribute so that the
$draw$ method (which is not implemented in the base class) can render in an
absolute coordinate frame.
"""
)
cn_disc('这是控制程序用来将 $flowable$ 渲染到特定画布的方法。'
        '它处理转换为画布坐标(<i>x</i>,<i>y</i>)，并确保 $flowable$ 有一个$canv$属性，'
        '这样$draw$方法(在基类中没有实现)就可以在一个绝对坐标框架中渲染。')

eg("Flowable.wrap(availWidth, availHeight)")

disc(
    """This will be called by the enclosing frame before objects
are asked their size, drawn or whatever.  It returns the
size actually used."""
)
cn_disc('在询问对象的大小、绘制或其他什么之前，这个函数将被包围的框架调用。 它返回实际使用的尺寸。')

eg(
    """
    Flowable.split(self, availWidth, availheight):
"""
)
disc(
    """This will be called by more sophisticated frames when
wrap fails. Stupid flowables should return [] meaning that they are unable to split.
Clever flowables should split themselves and return a list of flowables. It is up to
the client code to ensure that repeated attempts to split are avoided.
If the space is sufficient the split method should return [self].
Otherwise the flowable should rearrange itself and return a list $[f0,
...]$ of flowables which will be considered in order. The implemented split 
method should avoid changing $self$ as this will allow sophisticated layout 
mechanisms to do multiple passes over a list of flowables.
"""
)
cn_disc('当wrap失败时，更复杂的框架会调用这个函数。'
        '愚蠢的 $flowables$ 应该返回[]，'
        '这意味着它们无法拆分。'
        '聪明的 $flowables$ 应该自己拆分并返回一个 $flowables$ 列表。'
        '客户端代码要确保避免重复尝试拆分。'
        '如果空间足够，拆分方法应该返回[self]。'
        '否则，$flowable$ 应该重新排列，并返回一个按顺序考虑的 $flowable$ 列表$[f0,...]$。'
        '实现的拆分方法应该避免改变 $self$，因为这将允许复杂的布局机制在一个可流动的列表上进行多次传递。')

# heading2("Guidelines for flowable positioning")
cn_heading2("流动定位的准则")


disc(
    """Two methods, which by default return zero, provide guidance on vertical
spacing of flowables:
"""
)
cn_disc('有两种方法，默认情况下返回零，为可流动物的垂直间距提供指导。')


eg(
    """
    Flowable.getSpaceAfter(self):
    Flowable.getSpaceBefore(self):
"""
)
disc(
    """These methods return how much space should follow or precede
the flowable. The space doesn't belong to the flowable itself i.e. the flowable's
$draw$ method shouldn't consider it when rendering. Controlling programs
will use the values returned in determining how much space is required by
a particular flowable in context.
"""
)
cn_disc('这些方法会返回 flowable 后面或前面应该有多少空间。'
        '这些空间不属于flowable本身，'
        '也就是说，flowable 的$draw$方法在渲染时不应该考虑它。'
        '控制程序将使用返回的值来确定上下文中特定 flowable 需要多少空间。')


disc(
    """All flowables have an $hAlign$ property: $('LEFT', 'RIGHT', 'CENTER' or 'CENTRE')$.
For paragraphs, which fill the full width of the frame, this has no effect.  For tables,
images or other objects which are less than the width of the frame, this determines their
horizontal placement.
"""
)
cn_disc("所有的flowables都有一个$hAlign$属性："
        "$('LEFT', 'RIGHT', 'CENTER'$ 或 $'CENTRE')$。"
        "对于占满整个框架宽度的段落，这个属性没有影响。 "
        "对于小于框架宽度的表格、图像或其他对象，这决定了它们的水平位置。")

disc(
    """The chapters which follow will cover the most important
specific types of flowables: Paragraphs and Tables."""
)
cn_disc('下面的章节将涵盖最重要的特定类型的可流动文件。段落和表格。')


heading2("Frames")
# cn_heading2("Frames")

disc(
    """
$Frames$ are active containers which are themselves contained in $PageTemplates$.
$Frames$ have a location and size and maintain a concept of remaining drawable
space. The command
"""
)
cn_disc('$Frames$是活动的容器，'
        '它本身就包含在$PageTemplate$中，'
        '$Frames$有一个位置和大小，并保持一个剩余可绘制空间的概念。如：')

eg(
    """
    Frame(x1, y1, width,height, leftPadding=6, bottomPadding=6,
            rightPadding=6, topPadding=6, id=None, showBoundary=0)
"""
)
disc(
    """creates a $Frame$ instance with lower left hand corner at coordinate $(x1,y1)$
(relative to the canvas at use time) and with dimensions $width$ x $height$. The $Padding$
arguments are positive quantities used to reduce the space available for drawing.
The $id$ argument is an identifier for use at runtime e.g. 'LeftColumn' or 'RightColumn' etc.
If the $showBoundary$ argument is non-zero then the boundary of the frame will get drawn
at run time (this is useful sometimes).
"""
)
cn_disc('创建一个左下角坐标为$(x1,y1)$的$Frame$实例(在使用时相对于画布)，'
        '尺寸为 $width$ x $height$。'
        '$Padding$参数是用于减少绘画空间的正量。'
        '参数$id$是运行时使用的标识符，例如 "LeftColumn "或 "RightColumn "等。'
        '如果$showBoundary$参数是非零，那么框架的边界将在运行时被绘制出来（这有时很有用）。')


# heading3("$Frame$ User Methods")
cn_heading3("$Frame$ 用户方法")

eg(
    """
    Frame.addFromList(drawlist, canvas)
"""
)
disc(
    """consumes $Flowables$ from the front of $drawlist$ until the
frame is full.  If it cannot fit one object, raises
an exception."""
)
cn_disc('消耗$drawlist$前面的$Flowables$，直到帧满为止。 如果不能容纳一个对象，则引发一个异常。')


eg(
    """
    Frame.split(flowable,canv)
"""
)
disc(
    '''Asks the flowable to split using up the available space and return
the list of flowables.
'''
)
cn_disc('要求flowable使用可用空间进行分割，并返回flowable的列表。')


eg(
    """
    Frame.drawBoundary(canvas)
"""
)
disc("draws the frame boundary as a rectangle (primarily for debugging).")
cn_disc('将框架边界画成一个矩形（主要用于调试）。')


# heading3("Using $Frames$")
cn_heading3("使用 $Frames$")

disc(
    """
$Frames$ can be used directly with canvases and flowables to create documents.
The $Frame.addFromList$ method handles the $wrap$ &amp; $drawOn$ calls for you.
You don't need all of the Platypus machinery to get something useful into
PDF.
"""
)
cn_disc('$Frames$可以直接与canvases和flowables一起使用来创建文档。'
        '$Frame.addFromList$方法为你处理$wrap$ 和 $drawOn$调用。'
        '你不需要所有的Platypus机器来获得有用的东西到PDF中。')

eg(
    """
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']
story = []

#add some flowables
story.append(Paragraph("This is a Heading",styleH))
story.append(Paragraph("This is a paragraph in <i>Normal</i> style.",
    styleN))
c  = Canvas('mydoc.pdf')
f = Frame(inch, inch, 6*inch, 9*inch, showBoundary=1)
f.addFromList(story,c)
c.save()
"""
)

# heading2("Documents and Templates")
cn_heading2("文档和模板")


disc(
    """
The $BaseDocTemplate$ class implements the basic machinery for document
formatting. An instance of the class contains a list of one or more
$PageTemplates$ that can be used to describe the layout of information
on a single page. The $build$ method can be used to process
a list of $Flowables$ to produce a <b>PDF</b> document.
"""
)
cn_disc('$BaseDocTemplate$ 类实现了文档格式化的基本机制。'
        '该类的一个实例包含了一个或多个$PageTemplate$的列表，'
        '这些 $PageTemplate$可用于描述单页信息的布局。'
        '$build$方法可用于处理 $Flowables$ 列表，以生成一个<b>PDF</b>文档。')


CPage(3.0)
# heading3("The $BaseDocTemplate$ class")
cn_heading3("$BaseDocTemplate$ 类。")


eg(
    """
    BaseDocTemplate(self, filename,
                    pagesize=defaultPageSize,
                    pageTemplates=[],
                    showBoundary=0,
                    leftMargin=inch,
                    rightMargin=inch,
                    topMargin=inch,
                    bottomMargin=inch,
                    allowSplitting=1,
                    title=None,
                    author=None,
                    _pageBreakQuick=1,
                    encrypt=None)
"""
)

disc(
    """
creates a document template suitable for creating a basic document. It comes with quite a lot
of internal machinery, but no default page templates. The required $filename$ can be a string,
the name of a file to  receive the created <b>PDF</b> document; alternatively it
can be an object which has a $write$ method such as a $BytesIO$ or $file$ or $socket$.
"""
)
cn_disc('创建一个适合创建基本文档的文档模板。'
        '它带有相当多的内部机制，但没有默认的页面模板。'
        '所需的$filename$可以是一个字符串，一个用于接收创建的<b>PDF</b>文档的文件名；'
        '也可以是一个有$write$方法的对象，如 $BytesIO$ 或 $file$ 或 $socket$。')

disc(
    """
The allowed arguments should be self explanatory, but $showBoundary$ controls whether or
not $Frame$ boundaries are drawn which can be useful for debugging purposes. The
$allowSplitting$ argument determines whether the builtin methods should try to <i>split</i>
individual $Flowables$ across $Frames$. The $_pageBreakQuick$ argument determines whether
an attempt to do a page break should try to end all the frames on the page or not, before ending
the page. The encrypt argument determines wether or not and how the document is encrypted.
By default, the document is not encrypted.
If $encrypt$ is a string object, it is used as the user password for the pdf.
If $encrypt$ is an instance of $reportlab.lib.pdfencrypt.StandardEncryption$, this object is
used to encrypt the pdf. This allows more finegrained control over the encryption settings.
"""
)
cn_disc('允许的参数应该是不言自明的，但是$showBoundary$控制是否绘制$Frame$的边界，这对于调试来说是很有用的。'
        '$allowSplitting$参数决定了内置方法是否应该尝试<i>split</i>单个$Flowables$跨越$Frame$。'
        '$_pageBreakQuick$参数决定了在结束页面之前，是否应该尝试结束页面上的所有框架。'
        '$encrypt$ 参数决定了是否对文档进行加密，以及如何加密。'
        '默认情况下，文档是不加密的。'
        '如果$encrypt$是一个字符串对象，那么它将作为pdf的用户密码。'
        '如果$encrypt$是一个$reportlab.lib.pdfencrypt.StandardEncryption$的实例，'
        '那么这个对象就被用来加密pdf。'
        '这允许对加密设置进行更精细的控制。')


# heading4("User $BaseDocTemplate$ Methods")
cn_heading4("$BaseDocTemplate$ 用户方法")


disc(
    """These are of direct interest to client programmers
in that they are normally expected to be used.
"""
)
cn_disc('这些都是客户程序员直接关心的问题，因为他们通常会被使用。')

eg(
    """
    BaseDocTemplate.addPageTemplates(self,pageTemplates)
"""
)
disc(
    """
This method is used to add one or a list of $PageTemplates$ to an existing documents.
"""
)
cn_disc('此方法用于在现有文档中添加一个或一系列$PageTemplate$。')

eg(
    """
    BaseDocTemplate.build(self, flowables, filename=None, canvasmaker=canvas.Canvas)
"""
)
disc(
    """
This is the main method which is of interest to the application
programmer. Assuming that the document instance is correctly set up the
$build$ method takes the <i>story</i> in the shape of the list of flowables
(the $flowables$ argument) and loops through the list forcing the flowables
one at a time through the formatting machinery. Effectively this causes
the $BaseDocTemplate$ instance to issue calls to the instance $handle_XXX$ methods
to process the various events.
"""
)
cn_disc('这是应用程序程序员感兴趣的主要方法。假设文档实例被正确设置，'
        '$build$ 方法将<i>story</i>以flowables列表的形式接收（$flowables$参数），'
        '并在列表中循环，将 $flowables$ 一次一个地强制通过格式化机制。'
        '实际上，这使得$BaseDocTemplate$实例发出对实例 $handle_XXX$ 方法的调用来处理各种事件。')

# heading4("User Virtual $BaseDocTemplate$ Methods")
cn_heading4("$BaseDocTemplate$ 用户虚拟方法")

disc(
    """
These have no semantics at all in the base class. They are intended as pure virtual hooks
into the layout machinery. Creators of immediately derived classes can override these
without worrying about affecting the properties of the layout engine.
"""
)
cn_disc('这些在基类中根本没有语义。它们的目的是作为布局机制的纯虚拟钩子。'
        '紧接派生类的创建者可以覆盖这些，而不用担心影响布局引擎的属性。')

eg(
    """
    BaseDocTemplate.afterInit(self)
"""
)
disc(
    """
This is called after initialisation of the base class; a derived class could overide
the method to add default $PageTemplates$.
"""
)
cn_disc('这个方法在基类初始化后被调用；派生类可以覆盖该方法来添加默认的$PageTemplates$。')


eg(
    """
    BaseDocTemplate.afterPage(self)
"""
)
disc(
    """This is called after page processing, and immediately after the 
afterDrawPage method of the current page template. A derived class could
use this to do things which are dependent on information in the page
such as the first and last word on the page of a dictionary.
"""
)
cn_disc('这是在页面处理后，紧接着当前页面模板的 $afterDrawPage$ 方法被调用。'
        '一个派生类可以使用这个方法来做一些依赖于页面信息的事情，比如字典页面上的首字和尾字。')

eg(
    """
    BaseDocTemplate.beforeDocument(self)
"""
)

disc(
    """This is called before any processing is
done on the document, but after the processing machinery
is ready. It can therefore be used to do things to the instance's
$pdfgen.canvas$ and the like.
"""
)
cn_disc('在对文档进行任何处理之前，但在处理机制准备好之后，'
        '就会调用这个函数，因此它可以用来对实例的$pdfgen.canvas$等进行处理。'
        '因此，它可以用来对实例的$pdfgen.canvas$等进行操作。')

eg(
    """
    BaseDocTemplate.beforePage(self)
"""
)

disc(
    """This is called at the beginning of page
processing, and immediately before the
beforeDrawPage method of the current page
template. It could be used to reset page specific
information holders."""
)
cn_disc('这是在页面处理开始时，'
        '在当前页面模板的 $beforeDrawPage$ 方法之前调用的。'
        '它可以用来重置页面特定的信息持有者。')

eg(
    """
    BaseDocTemplate.filterFlowables(self,flowables)
"""
)

disc("""This is called to filter flowables at the start of the main handle_flowable method.
Upon return if flowables[0] has been set to None it is discarded and the main
method returns immediately.""")
cn_disc('在主 $handle_flowable$ 方法开始时，'
        '调用这个函数来过滤flowables。'
        '在返回时，如果flowables[0]被设置为None，'
        '则会被丢弃，主方法立即返回。')

eg(
    """
    BaseDocTemplate.afterFlowable(self, flowable)
"""
)

disc(
    """
Called after a flowable has been rendered. An interested class could use this
hook to gather information about what information is present on a particular page or frame."""
)
cn_disc('在flowable被渲染后调用。'
        '有兴趣的类可以使用这个钩子来收集特定页面或框架上存在的信息。')


# heading4("$BaseDocTemplate$ Event handler Methods")
cn_heading4("$BaseDocTemplate$ 事件处理方法")

disc(
    """
These methods constitute the greater part of the layout engine. Programmers shouldn't
have to call or override these methods directly unless they are trying to modify the layout engine.
Of course, the experienced programmer who wants to intervene at a particular event, $XXX$,
which does not correspond to one of the virtual methods can always override and
call the base method from the drived class version. We make this easy by providing
a base class synonym for each of the handler methods with the same name prefixed by an underscore '_'.
"""
)
cn_disc('这些方法构成了布局引擎的主要部分。'
        '程序员不应该直接调用或覆盖这些方法，除非他们试图修改布局引擎。'
        '当然，有经验的程序员如果想在某个特定的事件，即$XXX$处进行干预，'
        '而这个事件并不对应于其中的一个虚拟方法，那么总是可以覆盖并调用drived类版本中的基方法。'
        '我们为每个处理方法提供了一个基类同义词，名称相同，前缀为下划线"_"，这样就很容易了。')


eg(
    """
    def handle_pageBegin(self):
        doStuff()
        BaseDocTemplate.handle_pageBegin(self)
        doMoreStuff()

    #using the synonym
    def handle_pageEnd(self):
        doStuff()
        self._handle_pageEnd()
        doMoreStuff()
"""
)
disc(
    """
Here we list the methods only as an indication of the events that are being
handled. Interested programmers can take a look at the source.
"""
)
cn_disc('在这里我们列出这些方法只是为了说明正在处理的事件。'
        '有兴趣的程序员可以看一下源码。')

eg(
    """
    handle_currentFrame(self,fx)
    handle_documentBegin(self)
    handle_flowable(self,flowables)
    handle_frameBegin(self,*args)
    handle_frameEnd(self)
    handle_nextFrame(self,fx)
    handle_nextPageTemplate(self,pt)
    handle_pageBegin(self)
    handle_pageBreak(self)
    handle_pageEnd(self)
"""
)


disc(
    """
Using document templates can be very easy; $SimpleDoctemplate$ is a class derived from
$BaseDocTemplate$ which provides its own $PageTemplate$ and $Frame$ setup.
"""
)
cn_disc('使用文档模板可以非常简单，$SimpleDoctemplate$ '
        '是由$BaseDocTemplate$派生出来的一个类，'
        '它提供了自己的 $PageTemplate$ 和 $Frame$ 设置。')


eg(
    """
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate
styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']
story = []

#add some flowables
story.append(Paragraph("This is a Heading",styleH))
story.append(Paragraph("This is a paragraph in <i>Normal</i> style.",
    styleN))
doc = SimpleDocTemplate('mydoc.pdf',pagesize = letter)
doc.build(story)
"""
)
heading3("$PageTemplates$")

disc(
    """
The $PageTemplate$ class is a container class with fairly minimal semantics. Each instance
contains a list of $Frames$ and has methods which should be called at the start and end
of each page.
"""
)
cn_disc('$PageTemplate$类是一个语义相当简单的容器类。'
        '每个实例都包含一个$Frames$的列表，'
        '并且有一些方法应该在每个页面的开始和结束时被调用。')

eg("PageTemplate(id=None,frames=[],onPage=_doNothing,onPageEnd=_doNothing)")

disc(
    """
is used to initialize an instance, the $frames$ argument should be a list of $Frames$
whilst the optional $onPage$ and $onPageEnd$ arguments are callables which should have signature
$def XXX(canvas,document)$ where $canvas$ and $document$
are the canvas and document being drawn. These routines are intended to be used to paint non-flowing (i.e. standard)
parts of pages. These attribute functions are exactly parallel to the pure virtual methods
$PageTemplate.beforPage$ and $PageTemplate.afterPage$ which have signature
$beforPage(self,canvas,document)$. The methods allow class derivation to be used to define
standard behaviour, whilst the attributes allow instance changes. The $id$ argument is used at
run time to perform $PageTemplate$ switching so $id='FirstPage'$ or $id='TwoColumns'$ are typical.
"""
)
cn_disc('用于初始化一个实例，$frames$ 参数应该是一个 $Frames$ 的列表，'
        '而可选的 $onPage$ 和 $onPageEnd$ 参数是可调用的，'
        '它们的签名应该是 $def XXX(canvas,document)$，'
        '其中 $canvas$ 和 $document$ 是正在绘制的画布和文档。'
        '这些例程的目的是用来绘制页面的非流动（即标准）部分。'
        '这些属性函数与纯虚拟方法 $PageTemplate.beforPage$ 和 $PageTemplate.afterPage$'
        '完全平行，这两个方法的签名是 $beforPage(self,canvas,document)$。'
        '这些方法允许使用类派生来定义标准行为，而属性则允许改变实例。'
        '在运行时，$id$ 参数用于执行 $PageTemplate$ 的切换，'
        '所以 $id=\'FirstPage\'$ 或 $id=\'TwoColumns\'$ 是典型的。')

