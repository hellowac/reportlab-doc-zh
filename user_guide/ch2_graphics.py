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
    pencilnote,
    todo,
    cn_todo,
    illust,
    cn_illust,
    examplefunctionxinches,
    examplefunctionyinches,

)
from utils import examples
from reportlab.lib.codecharts import SingleByteEncodingChart


# heading1("Graphics and Text with $pdfgen$")
cn_heading1("使用 $pdfgen$ 生成图形和文本")

# heading2("Basic Concepts")
cn_heading2("基本概念")

disc(
    """
The $pdfgen$ package is the lowest level interface for
generating PDF documents.  A $pdfgen$ program is essentially
a sequence of instructions for "painting" a document onto
a sequence of pages.  The interface object which provides the
painting operations is the $pdfgen canvas$.
"""
)
cn_disc("$pdfgen$包是生成PDF文档的最低级别接口。 一个$pdfgen$程序本质上是一个将文档 \"绘制 \"到页面序列上的指令序列。 "
        "提供绘画操作的接口对象是$pdfgen canvas$。")

disc(
    """
The canvas should be thought of as a sheet of white paper
with points on the sheet identified using Cartesian ^(X,Y)^ coordinates
which by default have the ^(0,0)^ origin point at the lower
left corner of the page.  Furthermore the first coordinate ^x^
goes to the right and the second coordinate ^y^ goes up, by
default."""
)
cn_disc("他的画布应该被认为是一张白纸，白纸上的点用笛卡尔^(X,Y)^坐标确定，默认情况下，^(0,0)^原点在页面的左下角。 "
        "此外，第一个坐标^x^往右走，第二个坐标^y^往上走，这是默认的。")

disc(
    """ A simple example program that uses a canvas follows. """
)
cn_disc("下面是一个使用画布的简单示例程序。")

eg(
    """
    from reportlab.pdfgen import canvas
    def hello(c):
        c.drawString(100,100,"Hello World")
    c = canvas.Canvas("hello.pdf")
    hello(c)
    c.showPage()
    c.save()
"""
)

disc(
    """
The above code creates a $canvas$ object which will generate
a PDF file named $hello.pdf$ in the current working directory.
It then calls the $hello$ function passing the $canvas$ as an argument.
Finally the $showPage$ method saves the current page of the canvas
and the $save$ method stores the file and closes the canvas."""
)
cn_disc("上面的代码创建了一个$canvas$对象，它将在当前工作目录下生成一个名为$hello.pdf$的PDF文件。"
        "然后调用$hello$函数，将$canvas$作为参数。最后，$showPage$方法保存canvas的当前页面。")

disc(
    """
The $showPage$ method causes the $canvas$ to stop drawing on the
current page and any further operations will draw on a subsequent
page (if there are any further operations -- if not no
new page is created).  The $save$ method must be called after the
construction of the document is complete -- it generates the PDF
document, which is the whole purpose of the $canvas$ object.
"""
)
cn_disc("$showPage$方法会使$canvas$停止在当前页上绘制，任何进一步的操作都会在随后的页面上绘制（如果有任何进一步的操作--如果没有的话"
        "新页面被创建）。在文档构建完成后必须调用$save$方法--它将生成PDF文档，这也是$canvas$对象的全部目的。")

# heading2("More about the Canvas")
cn_heading2("更多关于画布的信息")

disc(
    """
Before describing the drawing operations, we will digress to cover
some of the things which can be done to configure a canvas.  There
are many different settings available.  If you are new to Python
or can't wait to produce some output, you can skip ahead, but
come back later and read this!"""
)
cn_disc("在介绍绘图操作之前，我们先离题万里，介绍一下配置画布可以做的一些事情。 有许多不同的设置可供选择。 "
        "如果你是Python新手，或者迫不及待地想产生一些输出，你可以跳过前面的内容，但以后再来阅读这个内容吧!")

disc(
    """First of all, we will look at the constructor arguments for the 
    canvas:"""
)
cn_disc("首先，我们来看看画布的构造函数参数:")

eg(
    """    def __init__(self,filename,
                 pagesize=(595.27,841.89),
                 bottomup = 1,
                 pageCompression=0,
                 encoding=rl_config.defaultEncoding,
                 verbosity=0
                 encrypt=None):
                 """
)

disc(
    """The $filename$ argument controls the
name of the final PDF file.  You
may also pass in any open binary stream (such as $sys.stdout$, the python 
process standard output with a binary encoding)
and the PDF document will be written to that.  Since PDF
is a binary format, you should take care when writing other
stuff before or after it; you can't deliver PDF documents
inline in the middle of an HTML page!"""
)
cn_disc("参数$filename$控制最终PDF文件的名称。 你也可以传入任何开放的二进制流（如$sys.stdout$，python过程中标准的二进制编码输出），PDF文件将被写入该流。 "
        "由于PDF是二进制格式，所以在它之前或之后写其他东西的时候要小心，你不能在HTML页面中间内联传递PDF文档！"
        "你可以在HTML页面中写一个PDF文件，但不能在HTML页面中写一个PDF文件。")

disc(
    """The $pagesize$ argument is a tuple of two numbers
in points (1/72 of an inch). The canvas defaults to $A4$ (an international 
standard page size which differs from the American standard page size of 
$letter$), but it is better to explicitly specify it.  Most common page
sizes are found in the library module $reportlab.lib.pagesizes$,
so you can use expressions like"""
)
cn_disc("参数$pagesize$是一个以点为单位的两个数字的元组（1/72英寸）。"
        "画布默认为$A4$（国际标准的页面尺寸，与美国标准的$letter$页面尺寸不同），但最好明确指定。 "
        "大多数常见的页面大小都可以在库模块$reportlab.lib.pagesizes$中找到，所以你可以使用类似于")

eg(
    """from reportlab.lib.pagesizes import letter, A4
myCanvas = Canvas('myfile.pdf', pagesize=letter)
width, height = letter  #keep for later
"""
)

pencilnote()

disc(
    """If you have problems printing your document make sure you
are using the right page size (usually either $A4$ or $letter$).
Some printers do not work well with pages that are too large or too small."""
)
cn_disc("如果您在打印文件时遇到问题，请确保您使用正确的页面尺寸（通常是$A4$或$letter$）。")

disc(
    """Very often, you will want to calculate things based on
the page size.  In the example above we extracted the width and
height.  Later in the program we may use the $width$ variable to
define a right margin as $width - inch$ rather than using
a constant.  By using variables the margin will still make sense even
if the page size changes."""
)
cn_disc("很多时候，你会想根据页面大小来计算东西。 "
        "在上面的例子中，我们提取了宽度和高度。 "
        "在以后的程序中，我们可能会使用$width$变量来定义右边距为$width - inch$，而不是使用一个常数。"
        " 通过使用变量，即使页面大小发生变化，页边距也会有意义。")

disc(
    """The $bottomup$ argument switches coordinate systems.  Some graphics systems (like PDF and PostScript) place (0,0) at the bottom left of the page
others (like many graphical user interfaces [GUI's]) place the origin at the 
top left.  The $bottomup$ argument is deprecated and may be dropped in future"""
)
cn_disc("参数$bottomup$用于切换坐标系。 "
        "一些图形系统(如PDF和PostScript)将(0,0)置于页面的左下角，"
        "其他系统(如许多图形用户界面[GUI's])将原点置于  $bottomup$参数已被废弃，以后可能会被删除。")

todo(
    """Need to see if it really works for all tasks, and if not then get rid of it"""
)
cn_disc("需要看看它是否真的对所有任务都有效，如果没有，那就把它扔掉吧。")

disc(
    """The $pageCompression$ option determines whether the stream
of PDF operations for each page is compressed.  By default
page streams are not compressed, because the compression slows the file 
generation process.
If output size is important set $pageCompression=1$, but remember that, 
compressed documents will be smaller, but slower to generate.  Note that 
images are <i>always</i> compressed, and this option will only save space if 
you have a very large amount of text and vector graphics on each page."""
)
cn_disc("$pageCompression$选项决定是否对每一页的PDF操作流进行压缩。"
        " 默认情况下，页面流不被压缩，因为压缩会减慢文件的生成过程。"
        "如果输出大小很重要，则设置$pageCompression=1$，但请记住，压缩后的文件会更小，但生成速度更慢。"
        " 请注意，图像<i>总是</i>压缩的，只有当你在每一页上有非常多的文本和矢量图形时，这个选项才会节省空间。")

disc(
    """The $encoding$ argument is largely obsolete in version 2.0 and can
probably be omitted by 99% of users.  Its default value is fine unless you
very specifically need to use one of the 25 or so characters which are present
in MacRoman and not in Winansi.  A useful reference to these is here:
<font color="blue"><u><a href="http://www.alanwood.net/demos/charsetdiffs
.html">http://www.alanwood.net/demos/charsetdiffs.html</a></u></font>.

The parameter determines which font encoding is used for the
standard Type 1 fonts; this should correspond to the encoding on your system.
Note that this is the encoding used <i>internally by the font</i>; text you
pass to the ReportLab toolkit for rendering should always either be a Python
unicode string object or a UTF-8 encoded byte string (see the next chapter)!
The font encoding has two values at present: $'WinAnsiEncoding'$ or
$'MacRomanEncoding'$.  The variable $rl_config.defaultEncoding$ above points
to the former, which is standard on Windows, Mac OS X and many Unices
(including Linux). If you are Mac user and don't have OS X, you may want to
make a global change: modify the line at the top of
<i>reportlab/pdfbase/pdfdoc.py</i> to switch it over.  Otherwise, you can
probably just ignore this argument completely and never pass it.  For all TTF
and the commonly-used CID fonts, the encoding you pass in here is ignored,
since the reportlab library itself knows the right encodings in those cases."""
)
cn_disc("在2.0版本中，$encoding$参数基本上已经过时了，可能99%的用户都可以省略。 "
        "它的默认值很好，除非你特别需要使用MacRoman中的25个字符之一，而Winansi中没有。 "
        "这里是一个有用的参考资料:"
        "<font color=\"blue\"><u>"
        "<a href=\"http://www.alanwood.net/demos/charsetdiffs.html\">"
        "http://www.alanwood.net/demos/charsetdiffs.html</a></u></font>."
        "该参数决定了该文件的字体编码。标准Type 1字体；这应该与您系统上的编码相对应。"
        "请注意，这是字体<i>内部使用的编码</i>；"
        "您的文本 传递给ReportLab工具包的渲染信息应该总是Python的 "
        "unicode字符串对象或UTF-8编码的字节字符串(见下一章)! "
        "字体编码目前有两个值：$'WinAnsiEncoding'$或 $'MacRomanEncoding'$。 "
        "上面的变量$rl_config.defaultEncoding$指向的是 到前者，"
        "这是Windows、Mac OS X和许多Unices的标准配置(包括Linux)。"
        "如果你是Mac用户，并且没有OS X，你可能会想要 进行全局性的修改："
        "修改在 <i>reportlab/pdfbase/pdfdoc.py</i>来切换它。"
        "否则，您可以 可能就完全无视这个论点，永远不会通过。 "
        "对于所有TTF 和常用的CID字体，这里传入的编码会被忽略。"
        "因为reportlab库本身就知道这些情况下的正确编码。")

disc(
    """The demo script $reportlab/demos/stdfonts.py$
will print out two test documents showing all code points
in all fonts, so you can look up characters.  Special
characters can be inserted into string commands with
the usual Python escape sequences; for example \\101 = 'A'."""
)
cn_disc("演示脚本$reportlab/demos/stdfonts.py$将打印出两个测试文档，"
        "显示所有字体的所有代码点，这样你就可以查找字符。"
        "特殊字符可以用通常的Python转义序列插入到字符串命令中，例如 \\101 = 'A'。")

disc(
    """The $verbosity$ argument determines how much log
information is printed.  By default, it is zero to assist
applications which want to capture PDF from standard output.
With a value of 1, you will get a confirmation message
each time a document is generated.  Higher numbers may
give more output in future."""
)
cn_disc("参数$verbosity$决定了打印多少日志信息。 "
        "默认情况下，它是零，以帮助应用程序从标准输出中捕获PDF。"
        "如果值为1，每次生成文档时，您都会得到一条确认信息。 "
        "更高的数字可能会在将来提供更多的输出。")

disc(
    """The $encrypt$ argument determines if and how the document is encrypted.
By default, the document is not encrypted. If $encrypt$ is a string object, 
it is used as the user password for the pdf. If $encrypt$ is an instance of 
$reportlab.lib.pdfencrypt.StandardEncryption$,  this object is used to 
encrypt the pdf. This allows more finegrained control over the  encryption 
settings. Encryption is covered in more detail in Chapter 4."""
)
cn_disc("参数$encrypt$决定了是否以及如何对文档进行加密。"
        "默认情况下，文档没有被加密。如果$encrypt$是一个字符串对象，它被用作pdf的用户密码。"
        "如果$encrypt$是一个$reportlab.lib.pdfencrypt.StandardEncryption$的实例，"
        "那么这个对象就被用来加密pdf。这允许对加密设置进行更精细的控制。加密在第4章有更详细的介绍。")

todo("to do - all the info functions and other non-drawing stuff")
cn_todo("要做的事 -- 所有的信息功能和其他非绘图的东西。")
todo("""Cover all constructor arguments, and setAuthor etc.""")
cn_todo("覆盖所有构造函数参数，以及setAuthor等。")

# heading2("Drawing Operations")
cn_heading2("绘图操作")

disc(
    """
Suppose the $hello$ function referenced above is implemented as
follows (we will not explain each of the operations in detail yet).
"""
)
cn_disc("假设上面提到的$hello$函数实现如下（我们先不详细解释每个操作）。")

eg(examples.testhello)

disc(
    """
Examining this code notice that there are essentially two types
of operations performed using a canvas.  The first type draws something
on the page such as a text string or a rectangle or a line.  The second
type changes the state of the canvas such as changing the current fill or 
stroke color or changing the current font type and size.
"""
)
cn_disc("检查这段代码时注意到，使用画布进行的操作基本上有两种类型。 "
        "第一种类型是在页面上画一些东西，如一个文本字符串或一个矩形或一条线。"
        "第二种类型改变画布的状态，如改变当前的填充或笔触颜色，或改变当前的字体类型和大小。")

disc(
    """
If we imagine the program as a painter working on
the canvas the "draw" operations apply paint to the canvas using
the current set of tools (colors, line styles, fonts, etcetera)
and the "state change" operations change one of the current tools
(changing the fill color from whatever it was to blue, or changing
the current font to $Times-Roman$ in 15 points, for example).
"""
)
cn_disc("如果我们把程序想象成一个在画布上工作的画家，"
        "\"绘制\"操作使用当前的一组工具（颜色、线条样式、字体等）将颜料涂抹到画布上，"
        "而\"状态改变\"操作则改变了当前的一个工具"
        "（例如，将填充颜色从原来的任何颜色改为蓝色，或者将当前的字体改为15点的$Times-Roman$）。")

disc(
    """
The document generated by the "hello world" program listed above would contain
the following graphics.
"""
)
cn_disc("上面列出的 \"hello world \"程序生成的文档将包含以下图形。")

# illust(examples.hello, '"Hello World" in pdfgen')
cn_illust(examples.hello, 'pdfgen 生成 "Hello World"')

# heading3("About the demos in this document")
cn_heading3("关于本文档中的演示")

disc(
    """
This document contains demonstrations of the code discussed like the one shown
in the rectangle above.  These demos are drawn on a "tiny page" embedded
within the real pages of the guide.  The tiny pages are %s inches wide
and %s inches tall. The demo displays show the actual output of the demo code.
For convenience the size of the output has been reduced slightly.
"""
    % (examplefunctionxinches, examplefunctionyinches)
)
cn_disc(f"本文档包含了所讨论的代码的演示，如上图矩形所示。 "
        f"这些演示是在嵌入指南真实页面中的 \"小页 \"上绘制的。" 
        f"这些小页面的宽度为{examplefunctionxinches}英寸，高度为{examplefunctionyinches}英寸。"
        f"演示显示的是演示代码的实际输出。"
        f"为了方便起见，输出的大小被稍微缩小了。")

# heading2('The tools: the "draw" operations')
cn_heading2("工具：\"draw\"的操作")

disc(
    """
This section briefly lists the tools available to the program for painting 
information onto a page using the canvas interface. These will be discussed 
in detail in later sections.  They are listed here for easy reference and 
for summary purposes.
"""
)
cn_disc("本节简要列出了该程序可用来使用画布界面在页面上绘制信息的工具。"
        "这些工具将在后面的章节中详细讨论。 "
        "这里列出这些工具是为了便于参考和总结。")

# heading3("Line methods")
cn_heading3("绘制直线相关方法")

eg("""canvas.line(x1,y1,x2,y2)""")
eg("""canvas.lines(linelist)""")

disc(
    """The line methods draw straight line segments on the canvas."""
)
cn_disc("线条方法在画布上绘制直线段。")

# heading3("Shape methods")
cn_heading3("绘制形状相关方法")

eg("""canvas.grid(xlist, ylist) """)
eg("""canvas.bezier(x1, y1, x2, y2, x3, y3, x4, y4)""")
eg("""canvas.arc(x1,y1,x2,y2) """)
eg("""canvas.rect(x, y, width, height, stroke=1, fill=0) """)
eg("""canvas.ellipse(x1,y1, x2,y2, stroke=1, fill=0)""")
eg("""canvas.wedge(x1,y1, x2,y2, startAng, extent, stroke=1, fill=0) """)
eg("""canvas.circle(x_cen, y_cen, r, stroke=1, fill=0)""")
eg("""canvas.roundRect(x, y, width, height, radius, stroke=1, fill=0) """)

disc(
    """The shape methods draw common complex shapes on the canvas."""
)
cn_disc("形状方法在画布上绘制常见的复杂形状。")

# heading3("String drawing methods")
cn_heading3("绘制字符串相关方法")

eg("""canvas.drawString(x, y, text):""")
eg("""canvas.drawRightString(x, y, text) """)
eg("""canvas.drawCentredString(x, y, text)""")

disc(
    """The draw string methods draw single lines of text on the canvas."""
)
cn_disc("绘制字符串方法在画布上绘制单行文字。")

# heading3("The text object methods")
cn_heading3("文本对象相关方法")

eg("""textobject = canvas.beginText(x, y) """)
eg("""canvas.drawText(textobject) """)

disc(
    """
Text objects are used to format text in ways that
are not supported directly by the $canvas$ interface.
A program creates a text object from the $canvas$ using $beginText$
and then formats text by invoking $textobject$ methods.
Finally the $textobject$ is drawn onto the canvas using
$drawText$.
"""
)
cn_disc("文本对象用于以$canvas$界面不直接支持的方式来格式化文本。"
        "程序使用$beginText$从$canvas$创建一个文本对象，"
        "然后通过调用$textobject$方法来格式化文本。"
        "最后使用$drawText$将$textobject$绘制到canvas上。")

# heading3("The path object methods")
cn_heading3("路径对象相关方法")

eg("""path = canvas.beginPath() """)
eg("""canvas.drawPath(path, stroke=1, fill=0, fillMode=None) """)
eg("""canvas.clipPath(path, stroke=1, fill=0, fillMode=None) """)

disc(
    """
Path objects are similar to text objects: they provide dedicated control
for performing complex graphical drawing not directly provided by the
canvas interface.  A program creates a path object using $beginPath$
populates the path with graphics using the methods of the path object
and then draws the path on the canvas using $drawPath$."""
)
cn_disc("路径对象类似于文本对象：它们为执行复杂的图形绘制提供了画布界面无法直接提供的专用控件。 "
        "程序使用$beginPath$创建一个路径对象，使用路径对象的方法为路径填充图形，"
        "然后使用$drawPath$在画布上绘制路径。")

disc(
    """It is also possible to use a path as a "clipping region" using the 
    $clipPath$ method -- for example a circular path can be used to clip away 
    the outer parts of a rectangular image leaving only a circular part of the 
    image visible on the page.
"""
)
cn_disc("也可以使用$clipPath$方法将一个路径作为 \"剪切区域\""
        "--例如，一个圆形的路径可以用来剪切掉一个矩形图像的外部部分，"
        "只留下图像的一个圆形部分在页面上可见。")

disc(
    """If $fill=1$ is specified then the $fillMode$ argument may be used to 
    set either 0=$even-odd$ or 1=$non-zero$ filling mode.
which will alter the way that complex paths are filled. If the default $None$ 
values is used then the canvas
$_fillMode$ attribute value is used (normally $0$ ie $even-odd$)."""
)
cn_disc("如果指定了$fill=1$，那么$fillMode$参数可以用来设置0=$even-odd$或1=$non-zero$填充模式，"
        "这将改变复杂路径的填充方式。"
        "如果使用默认的$None$值，则使用canvas的$_fillMode$属性值（通常为$0$即$even-odd$）。")

# heading3("Image methods")
cn_heading3("图像相关方法")

pencilnote()

disc(
    """
You need the Python Imaging Library (PIL) to use images with the ReportLab package.
Examples of the techniques below can be found by running the script $test_pdfgen_general.py$
in our $tests$ subdirectory and looking at page 7 of the output.
"""
)
cn_disc("你需要Python Imaging Library (PIL)来使用ReportLab包的图像。"
        "通过运行我们的$tests$子目录中的脚本$test_pdfgen_general.py$并查看输出的第7页，"
        "可以找到下面的技术示例。")

disc(
    """
There are two similar-sounding ways to draw images.  The preferred one is
the $drawImage$ method.  This implements a caching system so you can
define an image once and draw it many times; it will only be
stored once in the PDF file.  $drawImage$ also exposes one advanced parameter,
a transparency mask, and will expose more in future.  The older technique,
$drawInlineImage$ stores bitmaps within the page stream and is thus very
inefficient if you use the same image more than once in a document; but can 
result in PDFs which render faster if the images are very small and not 
repeated. We'll discuss the oldest one first:
"""
)
cn_disc("有两种听起来差不多的画像方式。 首选的是$drawImage$方法。 "
        "它实现了一个缓存系统，所以你可以一次定义一个图像，并多次绘制；"
        "它将只在PDF文件中存储一次。 "
        "$drawImage$还公开了一个高级参数，一个透明度掩模，将来还会公开更多。 "
        "较老的技术，$drawInlineImage$在页面流中存储位图，"
        "因此，如果你在文档中不止一次使用相同的图像，效率非常低；"
        "但如果图像非常小且不重复，则可以导致PDF更快地渲染。"
        "我们先讨论最老的那个。")

eg("""canvas.drawInlineImage(self, image, x,y, width=None,height=None) """)

disc(
    """
The $drawInlineImage$ method places an image on the canvas.  The $image$
parameter may be either a PIL Image object or an image filename.  Many common
file formats are accepted including GIF and JPEG.  It returns the size of the 
actual image in pixels as a (width, height) tuple.
"""
)
cn_disc("$drawInlineImage$方法在画布上放置一张图片。 "
        "参数$image$可以是一个PIL图像对象或图像文件名。 "
        "许多常见的文件格式都被接受，包括GIF和JPEG。 "
        "它以(宽，高)元组的形式返回实际图像的像素大小。")

eg("""canvas.drawImage(self, image, x,y, width=None,height=None,mask=None) """)
disc(
    """
The arguments and return value work as for $drawInlineImage$.  However, 
we use a caching system; a given image will only be stored the first time it 
is used, and just referenced on subsequent use.  If you supply a filename, 
it assumes that the same filename means the same image.  If you supply a PIL 
image, it tests if the content has actually changed before re-embedding."""
)
cn_disc("参数和返回值和$drawInlineImage$一样。 "
        "然而，我们使用了一个缓存系统；"
        "一个给定的图像将只在第一次使用时被存储，而只是在后续使用时被引用。 "
        "如果您提供一个文件名，它假设相同的文件名意味着相同的图像。 "
        "如果你提供了一个PIL图片，它在重新嵌入之前会测试内容是否有实际变化。")

disc(
    """
The $mask$ parameter lets you create transparent images.  It takes 6 numbers
and defines the range of RGB values which will be masked out or treated as
transparent. For example with [0,2,40,42,136,139], it will mask out any pixels
with a Red value from 0 or 1, Green from 40 or 41 and Blue of  136, 137 or 138
(on a scale of 0-255). It's currently your job to know which color is the
'transparent' or background one."""
)
cn_disc("参数$mask$可以让你创建透明图像。 "
        "它需要6个数字，并定义RGB值的范围，这些值将被屏蔽掉或被视为透明。"
        "例如，使用 [0,2,40,42,136,139]，它将遮蔽任何"
        "红色值为 0 或 1 的像素，"
        "绿色值为 40 或 41 的像素，"
        "蓝色值为 136、137 或 138 的像素（在 0-255 的范围内）。"
        "目前你的工作是知道哪种颜色是 \"透明 \"的或背景的。")

disc(
    """PDF allows for many image features and we will expose more of the over
time, probably with extra keyword arguments to $drawImage$."""
)
cn_disc("PDF允许许多图像功能，我们将在一段时间内暴露更多的图像功能，"
        "可能会用额外的关键字参数来表示$drawImage$。")

# heading3("Ending a page")
cn_heading3("结束一个页面")

eg("""canvas.showPage()""")

disc(
    """The $showPage$ method finishes the current page.  All additional 
drawing will be done on another page."""
)
cn_disc("$showPage$方法完成了当前页面。 所有额外的绘图将在另一个页面上完成。")

pencilnote()

disc(
    """Warning!  All state changes (font changes, color settings, geometry 
transforms, etcetera) are FORGOTTEN when you advance to a new page in 
$pdfgen$.  Any state settings you wish to preserve must be set up again 
before the program proceeds with drawing!"""
)
cn_disc("警告!  "
        "当你在$pdfgen$中前进到一个新的页面时，"
        "所有的状态改变（字体改变，颜色设置，几何变换，等等）都会被忘记。"
        "任何您希望保留的状态设置必须在程序继续绘制之前重新设置!")

# heading2('The toolbox: the "state change" operations')
cn_heading2("工具箱：'状态变化'(state change) 操作")

disc(
    """
This section briefly lists the ways to switch the tools used by the program
for painting information onto a page using the $canvas$ interface.
These too will be discussed in detail in later sections.
"""
)
cn_disc("本节简要列举了程序使用$canvas$界面将信息绘制到页面上的工具的切换方法。"
        "这些也将在后面的章节中详细讨论。")

# heading3("Changing Colors")
cn_heading3("改变颜色")

eg("""canvas.setFillColorCMYK(c, m, y, k) """)
eg("""canvas.setStrikeColorCMYK(c, m, y, k) """)
eg("""canvas.setFillColorRGB(r, g, b) """)
eg("""canvas.setStrokeColorRGB(r, g, b) """)
eg("""canvas.setFillColor(acolor) """)
eg("""canvas.setStrokeColor(acolor) """)
eg("""canvas.setFillGray(gray) """)
eg("""canvas.setStrokeGray(gray) """)

disc(
    """
PDF supports three different color models: gray level, additive (
red/green/blue or RGB), and
subtractive with darkness parameter (cyan/magenta/yellow/darkness or CMYK).
The ReportLab packages also provide named colors such as $lawngreen$.  There 
are two
basic color parameters in the graphics state: the $Fill$ color for the 
interior of graphic
figures and the $Stroke$ color for the boundary of graphic figures.  The 
above methods
support setting the fill or stroke color using any of the four color 
specifications.
"""
)
cn_disc("PDF支持三种不同的颜色模型：灰度级、外加剂(red/green/blue或RGB)、 "
        "和 减去暗度参数（青色/红褐色/黄色/暗度或CMYK）。"
        "ReportLab包还提供了命名颜色，如$lawngreen$。 "
        "这里是图形状态下的两个基本颜色参数：$Fill$的为图形的填充色和$Stroke$为图形的边框色。 "
        "上述两种方法支持使用四种颜色中的任何一种来设置填充或描边颜色。")

# heading3("Changing Fonts")
cn_heading3("更改字体")
eg("""canvas.setFont(psfontname, size, leading = None) """)

disc(
    """
The $setFont$ method changes the current text font to a given type and size.
The $leading$ parameter specifies the distance down to move when advancing from
one text line to the next.
"""
)
cn_disc("$setFont$方法将当前的文本字体改为给定的类型和大小。"
        "$leading$参数指定了从一行文字前进到下一行时向下移动的距离。")

# heading3("Changing Graphical Line Styles")
cn_heading3("更改图形线条样式")

eg("""canvas.setLineWidth(width) """)
eg("""canvas.setLineCap(mode) """)
eg("""canvas.setLineJoin(mode) """)
eg("""canvas.setMiterLimit(limit) """)
eg("""canvas.setDash(self, array=[], phase=0) """)

disc(
    """
Lines drawn in PDF can be presented in a number of graphical styles.
Lines can have different widths, they can end in differing cap styles,
they can meet in different join styles, and they can be continuous or
they can be dotted or dashed.  The above methods adjust these various 
parameters."""
)
cn_disc("在PDF中绘制的线条可以以多种图形样式呈现。"
        "线条可以有不同的宽度，它们可以以不同的盖子样式结束，"
        "它们可以以不同的连接样式相接，它们可以是连续的，也可以是点线或虚线。 "
        "上述方法可以调整这些不同的参数。")

# heading3("Changing Geometry")
cn_heading3("改变几何形状")

eg("""canvas.setPageSize(pair) """)
eg("""canvas.transform(a,b,c,d,e,f): """)
eg("""canvas.translate(dx, dy) """)
eg("""canvas.scale(x, y) """)
eg("""canvas.rotate(theta) """)
eg("""canvas.skew(alpha, beta) """)

disc(
    """
All PDF drawings fit into a specified page size.  Elements drawn outside of 
the specified page size are not visible.  Furthermore all drawn elements are 
passed through an affine transformation which may adjust their location 
and/or distort their appearence.  The $setPageSize$ method adjusts the 
current page size.  The $transform$, $translate$, $scale$, $rotate$, 
and $skew$ methods add additional transformations to the current transformation.
It is important to remember that these transformations are <i>incremental</i> 
-- a new transform modifies the current transform (but does not replace it).
"""
)
cn_disc("所有的PDF图纸都适合指定的页面大小。 "
        "在指定的页面尺寸之外绘制的元素是不可见的。"
        "此外，所有绘制的元素都会通过一个可能调整其位置和/或扭曲其外观的仿射变换。 "
        "$setPageSize$方法可以调整当前的页面大小。 "
        "$transform$, $translate$, $scale$, $rotate$, "
        "和 $skew$ 方法会给当前的变换添加额外的变换。"
        "重要的是要记住，这些转换是<i>递增的</i>。 "
        "-- 新的变换会修改当前的变换(但不会取代它)；")

# heading3("State control")
cn_heading3("状态控制")

eg("""canvas.saveState() """)
eg("""canvas.restoreState() """)

disc(
    """
Very often it is important to save the current font, graphics transform, 
line styles and other graphics state in order to restore them later. The 
$saveState$ method marks the current graphics state for later restoration by 
a matching $restoreState$.  Note that the save and restore method invocation 
must match -- a restore call restores the state to the most recently saved 
state which hasn't been restored yet. You cannot save the state on one page 
and restore it on the next, however -- no state is preserved between pages."""
)
cn_disc("很多时候，保存当前的字体、图形变换、线条样式和其他图形状态是很重要的，以便以后恢复它们。"
        "$saveState$方法标记了当前的图形状态，以便以后通过匹配的$restoreState$进行恢复。 "
        "请注意，保存和还原方法的调用必须匹配--还原调用会将状态还原到最近保存的状态，而最近的状态还没有被还原。"
        "但是，你不能在一个页面上保存状态，然后在下一个页面上还原它 -- 页面之间不会保存状态。")

# heading2("Other $canvas$ methods.")
cn_heading2("其他$canvas$的方法。")

disc(
    """
Not all methods of the $canvas$ object fit into the "tool" or "toolbox"
categories.  Below are some of the misfits, included here for completeness.
"""
)
cn_disc("并非所有$canvas$对象的方法都适合\"tool\"或\"toolbox\"类别。 "
        "以下是一些不合群的方法，为了完整起见，在此收录。")

eg(
    """
 canvas.setAuthor()
 canvas.addOutlineEntry(title, key, level=0, closed=None)
 canvas.setTitle(title)
 canvas.setSubject(subj)
 canvas.pageHasData()
 canvas.showOutline()
 canvas.bookmarkPage(name)
 canvas.bookmarkHorizontalAbsolute(name, yhorizontal)
 canvas.doForm()
 canvas.beginForm(name, lowerx=0, lowery=0, upperx=None, uppery=None)
 canvas.endForm()
 canvas.linkAbsolute(contents, destinationname, Rect=None, addtopage=1, 
 name=None, **kw)
 canvas.linkRect(contents, destinationname, Rect=None, addtopage=1, 
 relative=1, name=None, **kw)
 canvas.getPageNumber()
 canvas.addLiteral()
 canvas.getAvailableFonts()
 canvas.stringWidth(self, text, fontName, fontSize, encoding=None)
 canvas.setPageCompression(onoff=1)
 canvas.setPageTransition(self, effectname=None, duration=1,
                        direction=0,dimension='H',motion='I')
"""
)

# heading2('Coordinates (default user space)')
cn_heading2("坐标（默认用户空间)")

disc(
    """
By default locations on a page are identified by a pair of numbers.
For example the pair $(4.5*inch, 1*inch)$ identifies the location
found on the page by starting at the lower left corner and moving to
the right 4.5 inches and up one inch.
"""
)
cn_disc("默认情况下，页面上的位置是由一对数字来标识的，"
        "例如，一对$(4.5*inch, 1*inch)$标识的是页面上的位置。"
        "例如，一对$(4.5*inch, 1*inch)$从左下角开始，向右移动4.5英寸，"
        "再向上移动一英寸，来标识页面上的位置。")

disc("For example, the following function draws a number "
     "of elements on a $canvas$.")

cn_disc("例如，下面的函数在$canvas$上绘制一些元素。")

eg(examples.testcoords)

disc(
    """In the default user space the "origin" ^(0,0)^ point is at the lower
left corner.  Executing the $coords$ function in the default user space
(for the "demo minipage") we obtain the following."""
)
cn_disc("在默认的用户空间中，\"原点\"^(0,0)^点在左下角。  "
        "在默认的用户空间中执行$coords$函数（针对 \"演示迷你页\"），我们得到以下结果。")

# illust(examples.coords, 'The Coordinate System')
cn_illust(examples.coords, '坐标系统')

# heading3("Moving the origin: the $translate$ method")
cn_heading3("移动原点：$translate$方法")

disc(
    """Often it is useful to "move the origin" to a new point off
the lower left corner.  The $canvas.translate(^x,y^)$ method moves the origin
for the current page to the point currently identified by ^(x,y)^."""
)
cn_disc("通常情况下，\"移动原点 \"到左下角的新点是很有用的。 "
        "$canvas.translate(^x,y^)$方法将当前页面的原点移动到当前由^(x,y)^确定的点。")

disc(
    """For example the following translate function first moves
the origin before drawing the same objects as shown above."""
)
cn_disc("例如下面的平移函数首先移动原点，然后再绘制如上所示的相同对象。")

eg(examples.testtranslate)

disc("""This produces the following.""")
cn_disc("这就产生了以下结果：")

# illust(examples.translate, "Moving the origin: the $translate$ method")
cn_illust(examples.translate, "移动原点：$translate$方法")

# illust(NOP) # execute some code

pencilnote()

disc(
    """
<i>Note:</i> As illustrated in the example it is perfectly possible to draw 
objects or parts of objects "off the page". In particular a common confusing 
bug is a translation operation that  translates the entire drawing off the 
visible area of the page.  If a program produces a blank page it is possible 
that all the drawn objects are off the page.
"""
)
cn_disc("<i>注意：</i>如示例中所示，完全可以将对象或对象的一部分绘制到\"页面之外\"。"
        "特别是一个常见的令人困惑的错误是将整个绘图从页面的可见区域翻译出来的翻译操作。 "
        "如果一个程序产生了一个空白页，那么所有绘制的对象都有可能不在页面上。")

# heading3("Shrinking and growing: the scale operation")
cn_heading3("缩小与增长：scale操作")

disc(
    """Another important operation is scaling.  The scaling operation $canvas.scale(^dx,dy^)$
stretches or shrinks the ^x^ and ^y^ dimensions by the ^dx^, ^dy^ factors 
respectively.  Often ^dx^ and ^dy^ are the same -- for example to reduce a 
drawing by half in all dimensions use $dx = dy = 0.5$.  However for the 
purposes of illustration we show an example where $dx$ and $dy$ are different.
"""
)
cn_disc("另一个重要的操作是缩放操作。 "
        "缩放操作$canvas.scale(^dx,dy^)$分别以^dx^, ^dy^系数来拉伸或缩小^x^和^y^的尺寸。 "
        "通常情况下，^dx^和^dy^是相同的 -- 例如，"
        "要在所有维度上将图形缩小一半，使用$dx = dy = 0.5$。 "
        "然而为了说明问题，我们举一个例子，其中$dx$和$dy$是不同的。")

eg(examples.testscale)

disc(
    """This produces a "short and fat" reduced version of the previously 
    displayed operations."""
)
cn_disc("这样就会产生一个 \"短小精悍\"的缩小版的之前显示的操作。")

# illust(examples.scale, "Scaling the coordinate system")
cn_illust(examples.scale, "缩放坐标系统")

# illust(NOP) # execute some code

pencilnote()

disc(
    """<i>Note:</i> scaling may also move objects or parts of objects off the page,
or may cause objects to "shrink to nothing." """
)
cn_disc("<i>注意：</i>缩放也可能会将对象或对象的一部分从页面上移开，或者可能会导致对象 \"缩水为零\"。")

disc(
    """Scaling and translation can be combined, but the order of the
operations are important."""
)
cn_disc("缩放和翻译可以结合起来，但操作的顺序很重要。")

eg(examples.testscaletranslate)

disc(
    """This example function first saves the current $canvas$ state
and then does a $scale$ followed by a $translate$.  Afterward the function
restores the state (effectively removing the effects of the scaling and
translation) and then does the <i>same</i> operations in a different order.
Observe the effect below."""
)
cn_disc("这个示例函数首先保存当前的$canvas$状态，然后进行$scale$和$translate$操作。 "
        "之后，函数恢复了状态（有效地消除了缩放和翻译的影响），"
        "然后以不同的顺序进行<i>相同的</i>操作。"
        "观察下面的效果。")

# illust(examples.scaletranslate, "Scaling and Translating")
cn_illust(examples.scaletranslate, "缩放和翻译")

# illust(NOP) # execute some code

pencilnote()

disc(
    """<em>Note:</em> scaling shrinks or grows everything including line widths
so using the canvas.scale method to render a microscopic drawing in
scaled microscopic units may produce a blob (because all line widths will get expanded a huge amount).
Also rendering an aircraft wing in meters scaled to centimeters may cause the lines to shrink to the point where they disappear.  For engineering or scientific purposes such as these scale and translate
the units externally before rendering them using the canvas."""
)
cn_disc("<em>注意：</em>缩放会收缩或增长所有的东西，包括线宽，"
        "因此使用canvas.scale方法以缩放的微观单位来渲染微观图形可能会产生一个blob（因为所有的线宽都会被大量扩展）。"
        "此外，以米为单位渲染飞机机翼，缩放为厘米，可能会导致线条收缩到消失的程度。 "
        "对于工程或科学目的，如这些比例和翻译。"
        "在使用画布渲染之前，从外部对单元进行渲染。")

# heading3("Saving and restoring the $canvas$ state: "
#          "$saveState$ and $restoreState$")
cn_heading3("保存和恢复$canvas$状态：$saveState$和$restoreState$。")

disc(
    """
The $scaletranslate$ function used an important feature of the $canvas$ object:
the ability to save and restore the current parameters of the $canvas$.
By enclosing a sequence of operations in a matching pair of $canvas.saveState()$
an $canvas.restoreState()$ operations all changes of font, color, line style,
scaling, translation, or other aspects of the $canvas$ graphics state can be
restored to the state at the point of the $saveState()$.  Remember that the 
save/restore calls must match: a stray save or restore operation may cause 
unexpected and undesirable behavior.  Also, remember that <i>no</i> $canvas$ 
state is preserved across page breaks, and the save/restore mechanism does 
not work across page breaks.
"""
)
cn_disc("$scaletranslate$函数使用了$canvas$对象的一个重要特性：能够保存和恢复$canvas$的当前参数。"
        "通过在一对匹配的$canvas.saveState()$和$canvas.restoreState()$操作中包含一个操作序列，"
        "所有字体、颜色、线条样式、缩放、翻译或$canvas$图形状态的其他方面的变化都可以恢复到$saveState()$点的状态。"
        "请记住，保存/还原调用必须匹配：一个杂乱的保存或还原操作可能会导致意外和不理想的行为。"
        "另外，请记住，<i>没有</i> $canvas$状态会在页面中断时被保存，保存/还原机制不会不能跨越分页符工作。")

# heading3("Mirror image")
cn_heading3("镜像")

disc(
    """
It is interesting although perhaps not terribly useful to note that
scale factors can be negative.  For example the following function
"""
)
cn_disc("有趣的是，虽然可能不是非常有用，但注意到比例因子可以是负的。 例如下面的函数")

eg(examples.testmirror)

disc(
    """
creates a mirror image of the elements drawn by the $coord$ function.
"""
)
cn_disc("创建$coord$函数绘制的元素的镜像。")

# illust(examples.mirror, "Mirror Images")
cn_illust(examples.mirror, "镜像")

disc(
    """
Notice that the text strings are painted backwards.
"""
)
cn_disc("注意，文字串是倒着画的。")

# heading2("Colors")
cn_heading2("颜色")

disc(
    """
There are generally two types of colors used in PDF depending on the media where
the PDF will be used. The most commonly known screen colors model RGB can be used
in PDF, however in professional printing another color model CMYK is mainly used 
which gives more control over how inks are applied to paper. More on these color
models below.
"""
)
cn_disc("PDF中使用的颜色一般有两种类型，这取决于PDF将被使用的媒体。"
        "最常见的屏幕颜色模型RGB可以在PDF中使用，然而在专业印刷中主要使用另一种颜色模型CMYK，"
        "它可以对油墨如何应用于纸张进行更多的控制。以下是关于这些颜色模型的更多信息。")

# heading3("RGB Colors")
cn_heading3("RGB颜色")

disc(
    """
The $RGB$ or additive color representation follows the way a computer
screen adds different levels of the red, green, and blue light to make
any color in between, where white is formed by turning all three lights on full
($1,1,1$).
"""
)
cn_disc("$RGB$或称加色表示法，遵循电脑屏幕添加不同层次的红、绿、蓝光的方式，使其间的任何颜色，"
        "其中白色是通过将三盏灯全开形成的。")

disc(
    """
There are three ways to specify RGB colors in $pdfgen$: by name (using the 
$color$ module, by red/green/blue (additive, $RGB$) value, or by gray level.
The $colors$ function below exercises each of the four methods.
"""
)
cn_disc("在$pdfgen$中，有三种方法可以指定RGB颜色："
        "通过名称（使用$color$模块），"
        "通过红/绿/蓝（加法，$RGB$）值，"
        "或者通过灰度级别。"
        "下面的$colors$函数对这四种方法分别进行了练习。")

eg(examples.testRGBcolors)
# illust(examples.colorsRGB, "RGB Color Models")
cn_illust(examples.colorsRGB, "RGB 颜色模块")

# heading4("RGB Color Transparency")
cn_heading4("RGB颜色透明度")

disc(
    """
Objects may be painted over other objects to good effect in $pdfgen$.  Generally
There are two modes of handling objects that overlap in space, the default 
objects in the top layer will hide any part of other objects that falls 
underneath it. If you need transparency you got two choices:
"""
)
cn_disc("在$pdfgen$中，可以将对象涂在其他对象上，以达到良好的效果。 "
        "一般来说，有两种模式可以处理空间中重叠的对象，顶层的默认对象会隐藏掉它下面的其他对象的任何部分。"
        "如果你需要透明度，你有两个选择:")

disc(
    """
1. If your document is intended to be printed in a professional way and you are 
working in CMYK color space then you can use overPrint. In overPrinting the 
colors physically mix in the printer and thus a new color is obtained. By 
default a knockout will be applied and only top object appears. Read the CMYK section
if this is what you intend to use.
"""
)
cn_disc("1. 如果您的文档打算以专业的方式打印，并且您在CMYK色彩空间中工作，那么您可以使用overPrint。"
        "在overPrinting中，颜色会在打印机中物理混合，从而获得一种新的颜色。"
        "默认情况下，将应用一个淘汰，只有顶部对象出现。"
        "如果您打算使用CMYK，请阅读CMYK部分。")

disc(
    """
2. If your document is intended for screen output and you are using RGB colors 
then you can set an alpha value, where alpha is the opacity value of the color.
The default alpha value is $1$ (fully opaque) and you can use any real number
value in the range 0-1.
"""
)
cn_disc("2. 如果您的文档打算用于屏幕输出，并且您使用的是RGB颜色，"
        "那么您可以设置一个alpha值，其中alpha是颜色的不透明度值。"
        "默认的alpha值是 $1$（完全不透明），你可以使用任何实数。")

disc(
    """
Alpha transparency ($alpha$) is similar to overprint but works in RGB color 
space this example below demonstrates the alpha functionality. Refer to our 
website http://www.reportlab.com/snippets/ and look for snippets of overPrint and alpha
to see the code that generates the graph below.
"""
)
cn_disc("Alpha透明度($alpha$)类似于overprint，"
        "但在RGB色彩空间中工作，下面这个例子演示了alpha功能。"
        "请参考我们的网站 http://www.reportlab.com/snippets/，"
        "并查找overPrint和alpha的片段，以查看生成下面图表的代码。")

eg(examples.testalpha)
# illust(examples.alpha, "Alpha example")
cn_illust(examples.alpha, "Alpha 例子")

# heading3("CMYK Colors")
cn_heading3("CMYK 颜色")

disc(
    """
The $CMYK$ or subtractive method follows the way a printer
mixes three pigments (cyan, magenta, and yellow) to form colors.
Because mixing chemicals is more difficult than combining light there
is a fourth parameter for darkness.  For example a chemical
combination of the $CMY$ pigments generally never makes a perfect
black -- instead producing a muddy color -- so, to get black printers
don not use the $CMY$ pigments but use a direct black ink.  Because
$CMYK$ maps more directly to the way printer hardware works it may
be the case that colors specified in $CMYK$ will provide better fidelity
and better control when printed.
"""
)
cn_disc("$CMYK$或减法是按照打印机混合三种颜料（青色、品红色和黄色）形成颜色的方式进行的。"
        "因为混合化学品比结合光照更难 还有第四个参数是暗度。 "
        "例如，$CMY$颜料的化学组合通常不会产生完美的黑色"
        "--而是产生混浊的颜色--因此，为了得到黑色，打印机不使用$CMY$颜料，而是直接使用黑色墨水。 "
        "因为$CMYK$更直接地映射到打印机硬件的工作方式，"
        "所以在打印时，$CMYK$指定的颜色可能会提供更好的保真度和更好的控制。")

disc(
    """
There are two ways of representing CMYK Color: each color can be represented 
either by a real value between 0 and 1, or integer value between 0 and 100. 
Depending on your preference you can either use CMYKColor (for real values) or 
PCMYKColor ( for integer values). 0 means 'no ink', so printing on white papers gives you 
white. 1 (or 100 if you use PCMYKColor) means 'the maximum amount of ink'. 
e.g. CMYKColor(0,0,0,1) is black, CMYKColor(0,0,0,0) means 'no ink', 
and CMYKColor(0.5,0,0,0) means 50 percent cyan color.
"""
)
cn_disc("CMYK颜色有两种表示方法："
        "每一种颜色都可以用以下方法来表示可以是0到1之间的实值，"
        "也可以是0到100之间的整数值。"
        "根据您的喜好，您可以使用CMYKColor（对于实值）或 PCMYKColor（对于整数值）。"
        "0表示 \"没有墨水\"，所以在白纸上打印会得到白色。"
        "1表示 \"最大墨水量\"(如果使用PCMYKColor，则为100)。"
        "例如：CMYKColor(0,0,0,1)是黑色，CMYKColor(0,0,0,0)表示 \"没有墨水\"。"
        "而CMYKColor(0.5,0,0,0)表示50%的青色。")

eg(examples.testCMYKcolors)
# illust(examples.colorsCMYK, "CMYK Color Models")
cn_illust(examples.colorsCMYK, "CMYK颜色模型")

# heading2("Color space checking")
cn_heading2("色彩空间检查")

disc(
    """The $enforceColorSpace$ argument of the canvas is used to enforce the 
consistency of the colour model used in a document. It accepts these values: 
CMYK, RGB, SEP, SEP_BLACK, SEP_CMYK. 'SEP' refers to named color separations 
such as Pantone spot colors - these can be mixed with CMYK or RGB according 
to the parameter used.  The default is 'MIXED' which allows you to use colors from any color space.  An exception is raised if any 
colors used are not convertible to the specified model, e.g. rgb and cmyk (more 
information in test_pdfgen_general). This approach doesn't check external 
images included in document.
"""
)
cn_disc("画布的$enforceColorSpace$参数用于强制执行文档中使用的颜色模型的一致性。"
        "它接受这些值。CMYK, RGB, SEP, SEP_BLACK, SEP_CMYK. "
        "\"SEP\"指的是命名的分色，如Pantone专色--根据使用的参数，这些颜色可以与CMYK或RGB混合。 "
        "默认值是'MIXED'，允许你使用任何颜色空间的颜色。"
        "如果使用的任何颜色不能转换为指定的模型，例如rgb和cmyk，"
        "就会产生一个异常（更多信息请参见$test_pdfgen_general$）。"
        "这种方法不检查文档中包含的外部图像。")

# heading2("Color Overprinting")
cn_heading2("彩色套印")

disc(
    """
When two CMYK colored objects overlap in printing, then either the object 'on top'
will knock out the color of the the one underneath it, or the colors of the two
objects will mix in the overlapped area.
This behaviour can be set using the property $overPrint$.
"""
)
cn_disc("当两个CMYK颜色的对象在打印时重叠，"
        "那么 \"上面\"的对象会把下面的对象的颜色打掉，或者两个对象的颜色会在重叠的区域混合。"
        "这种行为可以使用属性$overPrint$来设置。")

disc(
    """
The $overPrint$ function will cause ovelapping areas of color to mix. In the 
example below, the colors of the rectangles on the left should appear mixed 
where they overlap - If you can't see this effect then you may need to enable 
the 'overprint preview' option in your PDF viewing software.  
Some PDF viewers such as $evince$ do not support overPrint; 
however Adobe Acrobat Reader does support it.
"""
)
cn_disc("$overPrint$"
        "函数将导致色彩的椭圆区域混合。"
        "在下面的例子中，左边矩形的颜色应该在它们重叠的地方出现混合"
        "--如果你看不到这个效果，那么你可能需要在你的PDF浏览软件中启用\"叠印预览\"选项。 "
        "一些PDF浏览器，如$evince$不支持叠印，但是Adobe Acrobat Reader支持。")

# illust(examples.overPrint, "overPrint example")
cn_illust(examples.overPrint, "OverPrint示例")

# heading3("Other Object Order of Printing Examples")
cn_heading3("其他对象的打印顺序示例")

disc(
    """
The word "SPUMONI" is painted in white over the colored rectangles,
with the apparent effect of "removing" the color inside the body of
the word.
"""
)
cn_disc('"SPUMONI"字样用白色涂抹在彩色长方形上，有明显的 "去除 "字体内部颜色的效果。')

eg(examples.testspumoni)
# illust(examples.spumoni, "Painting over colors")
cn_illust(examples.spumoni, "涂抹颜色")

disc(
    """
The last letters of the word are not visible because the default $canvas$
background is white and painting white letters over a white background
leaves no visible effect.
"""
)
cn_disc("由于默认的$canvas$背景是白色的，在白色背景上画上白色的字母，单词的最后一个字母不可见。")

disc(
    """
This method of building up complex paintings in layers can be done
in very many layers in $pdfgen$ -- there are fewer physical limitations
than there are when dealing with physical paints.
"""
)
cn_disc("这种分层建立复杂绘画的方法可以在$pdfgen$中完成非常多的层数"
        "--比起处理物理颜料时的物理限制要少。")

eg(examples.testspumoni2)

disc(
    """
The $spumoni2$ function layers an ice cream cone over the
$spumoni$ drawing.  Note that different parts of the cone
and scoops layer over eachother as well.
"""
)
cn_disc("Spumoni2$函数在$spumoni$图上叠加一个冰淇淋圆锥。 请注意，圆锥和勺子的不同部分也会互相分层。")

# illust(examples.spumoni2, "building up a drawing in layers")
cn_illust(examples.spumoni2, "层层叠加")

# heading2('Standard fonts and text objects')
cn_heading2("标准字体和文本对象")
disc(
    """
Text may be drawn in many different colors, fonts, and sizes in $pdfgen$.
The $textsize$ function demonstrates how to change the color and font and
size of text and how to place text on the page.
"""
)
cn_disc("在$pdfgen$中可以用许多不同的颜色、字体和大小来绘制文本。"
        "$textsize$函数演示了如何改变文本的颜色、字体和大小，以及如何在页面上放置文本。")

eg(examples.testtextsize)

disc('The $textsize$ function generates the following page.')
cn_disc("$textsize$函数生成了以下页面。")

# illust(examples.textsize, "text in different fonts and sizes")
cn_illust(examples.textsize, "不同字体和大小的文字")

disc(
    """
A number of different fonts are always available in $pdfgen$.
"""
)
cn_disc("不同字体和大小的文本在$pdfgen$中总是有许多不同的字体。")

eg(examples.testfonts)

disc(
    """
The $fonts$ function lists the fonts that are always available.
These don't need to be stored in a PDF document, since they
are guaranteed to be present in Acrobat Reader.
"""
)
cn_disc("函数$fonts$列出了始终可用的字体。"
        "这些字体不需要存储在PDF文档中，"
        "因为它们保证在Acrobat Reader中存在。")

# illust(examples.fonts, "the 14 standard fonts")
cn_illust(examples.fonts, "14种标准字体")

disc(
    """The Symbol and ZapfDingbats fonts cannot display properly because the 
required glyphs are not present in those fonts."""
)
cn_disc("Symbol和ZapfDingbats字体无法正确显示，因为这些字体中不存在所需的字形。")

disc(
    """
For information on how to use arbitrary fonts, see the next chapter.
"""
)
cn_disc("有关如何使用任意字体的信息，请参阅下一章。")

# heading2("Text object methods")
cn_heading2('文本对象方法')

disc(
    """
For the dedicated presentation of text in a PDF document, use a text object.
The text object interface provides detailed control of text layout parameters
not available directly at the $canvas$ level.  In addition, it results in 
smaller PDF that will render faster than many separate calls to the 
$drawString$ methods.
"""
)
cn_disc("对于PDF文档中文本的专用展示，可以使用文本对象。"
        "文本对象接口提供了对文本布局参数的详细控制，而这些参数在$canvas$级别是无法直接获得的。 "
        "此外，它还可以生成更小的PDF，其渲染速度比许多单独调用$drawString$方法要快。")

eg("""textobject.setTextOrigin(x,y)""")
eg("""textobject.setTextTransform(a,b,c,d,e,f)""")
eg("""textobject.moveCursor(dx, dy) # from start of current LINE""")
eg("""(x,y) = textobject.getCursor()""")
eg("""x = textobject.getX(); y = textobject.getY()""")
eg("""textobject.setFont(psfontname, size, leading = None)""")
eg("""textobject.textOut(text)""")
eg("""textobject.textLine(text='')""")
eg("""textobject.textLines(stuff, trim=1)""")

disc(
    """
The text object methods shown above relate to basic text geometry.
"""
)
cn_disc("上面显示的文本对象方法与基本的文本几何体有关。")

disc(
    """
A text object maintains a text cursor which moves about the page when
text is drawn.  For example the $setTextOrigin$ places the cursor
in a known position and the $textLine$ and $textLines$ methods move
the text cursor down past the lines that have been missing.
"""
)
cn_disc("文本对象维护一个文本光标，当文本被绘制时，这个光标会在页面上移动。 "
        "例如，$setTextOrigin$将光标放置在一个已知的位置，"
        "而$textLine$和$textLines$方法则将文本光标向下移动，经过缺失的线条。")

eg(examples.testcursormoves1)

disc(
    """
The $cursormoves$ function relies on the automatic movement of the text 
cursor for placing text after the origin has been set.
"""
)
cn_disc("函数$cursormoves$依靠文本光标的自动移动来放置原点后的文本。")

# illust(examples.cursormoves1, "How the text cursor moves")
cn_illust(examples.cursormoves1, "文本光标的移动方式")

disc(
    """
It is also possible to control the movement of the cursor
more explicitly by using the $moveCursor$ method (which moves
the cursor as an offset from the start of the current <i>line</i>
NOT the current cursor, and which also has positive ^y^ offsets
move <i>down</i> )in contrast to the normal geometry where
positive ^y^ usually moves up.
"""
)
cn_disc("也可以通过使用$moveCursor$方法更明确地控制光标的移动"
        "（该方法将光标移动为从当前<i>线</i>开始的偏移量，而不是当前光标，"
        "并且该方法还具有正^y^偏移量移动<i>向下</i>)"
        "与正常几何形状相反，正^y^通常向上移动。")

eg(examples.testcursormoves2)

disc(
    """
Here the $textOut$ does not move the down a line in contrast
to the $textLine$ function which does move down.
"""
)
cn_disc("在这里，$textOut$不会向下移动一行，而$textLine$函数则向下移动。")

# illust(examples.cursormoves2, "How the text cursor moves again")
cn_illust(examples.cursormoves2, "文本光标如何再次移动")

# heading3("Character Spacing")
cn_heading3("字符间距")

eg("""textobject.setCharSpace(charSpace)""")

disc(
    """The $setCharSpace$ method adjusts one of the parameters of text 
-- the inter-character spacing."""
)
cn_disc("$setCharSpace$方法调整文本的一个参数--字符间的间距。")

eg(examples.testcharspace)

disc(
    """The
$charspace$ function exercises various spacing settings.
It produces the following page."""
)
cn_disc("$charspace$函数行使各种间距设置。它产生以下页面。")

# illust(examples.charspace, "Adjusting inter-character spacing")
cn_illust(examples.charspace, "调整字符间距")

# heading3("Word Spacing")
cn_heading3("字距")

eg("""textobject.setWordSpace(wordSpace)""")

disc("The $setWordSpace$ method adjusts the space between words.")
cn_disc("$setWordSpace$方法调整字与字之间的空间。")

eg(examples.testwordspace)

disc(
    """The $wordspace$ function shows what various word space settings
look like below."""
)
cn_disc("$wordspace$函数显示了下面各种文字空间设置的样子。")

# illust(examples.wordspace, "Adjusting word spacing")
cn_illust(examples.wordspace, "调整字距")

# heading3("Horizontal Scaling")
cn_heading3("水平缩放")

eg("""textobject.setHorizScale(horizScale)""")

disc(
    """Lines of text can be stretched or shrunken horizontally by the
$setHorizScale$ method."""
)
cn_disc("文本行可以通过$setHorizScale$方法进行水平拉伸或收缩。")

eg(examples.testhorizontalscale)

disc(
    """The horizontal scaling parameter ^horizScale^
is given in percentages (with 100 as the default), so the 80 setting
shown below looks skinny.
"""
)
cn_disc("水平缩放参数^horizScale^是以百分比的形式给出的（默认为100），"
        "所以下图所示的80设置看起来很瘦。")

# illust(examples.horizontalscale, "adjusting horizontal text scaling")
cn_illust(examples.horizontalscale, "调整水平文本的比例")

# heading3("Interline spacing (Leading)")
cn_heading3("行间间距(领先)")

eg("""textobject.setLeading(leading)""")

disc(
    """The vertical offset between the point at which one
line starts and where the next starts is called the leading
offset.  The $setLeading$ method adjusts the leading offset.
"""
)
cn_disc("一条线的起始点和下一条线的起始点之间的垂直偏移称为前导偏移。 "
        "$setLeading$方法调整前导偏移。")

eg(examples.testleading)

disc(
    """As shown below if the leading offset is set too small
characters of one line my write over the bottom parts of characters
in the previous line."""
)
cn_disc("如下图所示，如果一行的前导偏移量设置得太小，我就会把前一行中的字符的底部部分写在上面。")

# illust(examples.leading, "adjusting the leading")
cn_illust(examples.leading, "矫枉过正")

# heading3("Other text object methods")
cn_heading3("其他文本对象方法")

eg("""textobject.setTextRenderMode(mode)""")

disc(
    """The $setTextRenderMode$ method allows text to be used
as a foreground for clipping background drawings, for example."""
)
cn_disc("例如，$setTextRenderMode$方法允许将文本作为剪裁背景图的前景。")

eg("""textobject.setRise(rise)""")

disc(
    """
The $setRise$ method <super>raises</super> or <sub>lowers</sub> text on the line
(for creating superscripts or subscripts, for example).
"""
)
cn_disc("$setRise$方法<super>提高</super>或<sub>降低</sub>行上的文本（例如，用于创建上标或下标）。")

eg(
    """textobject.setFillColor(aColor);
textobject.setStrokeColor(self, aColor)
# and similar"""
)

disc(
    """
These color change operations change the <font color=darkviolet>color</font> 
of the text and are otherwise
similar to the color methods for the $canvas$ object."""
)
cn_disc("这些颜色变化操作会改变文本的<font color=darkviolet>颜色</font>，"
        "其他方面与$canvas$对象的颜色方法类似。")

# heading2('Paths and Lines')
cn_heading2("路径和直线")

disc(
    """Just as textobjects are designed for the dedicated presentation
of text, path objects are designed for the dedicated construction of
graphical figures.  When path objects are drawn onto a $canvas$ they
are drawn as one figure (like a rectangle) and the mode of drawing
for the entire figure can be adjusted: the lines of the figure can
be drawn (stroked) or not; the interior of the figure can be filled or
not; and so forth."""
)
cn_disc("正如文本对象被设计成专门用于展示文本一样，路径对象被设计成专门用于构建图形。 "
        "当路径对象被绘制到$canvas$上时，它们被绘制成一个图形（就像一个矩形），"
        "整个图形的绘制模式可以调整：图形的线条可以绘制（笔画），也可以不绘制；"
        "图形的内部可以填充，也可以不填充；等等。")

disc(
    """
For example the $star$ function uses a path object to draw a star
"""
)
cn_disc("例如，$star$函数使用一个路径对象来绘制一个星体")

eg(examples.teststar)

disc(
    """
The $star$ function has been designed to be useful in illustrating
various line style parameters supported by $pdfgen$.
"""
)
cn_disc("$star$函数被设计用来说明$pdfgen$支持的各种行式参数。")

# illust(examples.star, "line style parameters")
cn_illust(examples.star, "直线样式参数")

# heading3("Line join settings")
cn_heading3("直线连接设置")

disc(
    """
The $setLineJoin$ method can adjust whether line segments meet in a point
a square or a rounded vertex.
"""
)
cn_disc("通过$setLineJoin$方法，可以调整线段在一个点上相接的是方块还是圆角顶点。")

eg(examples.testjoins)

disc(
    """
The line join setting is only really of interest for thick lines because
it cannot be seen clearly for thin lines.
"""
)
cn_disc("线条连接的设置只有对粗线条才真正有意义，因为对细线条看不清楚。")

# illust(examples.joins, "different line join styles")
cn_illust(examples.joins, "不同的直线连接样式")

# heading3("Line cap settings")
cn_heading3("直线帽子设置")
disc(
    """The line cap setting, adjusted using the $setLineCap$ method,
determines whether a terminating line ends in a square exactly at the vertex, a square over the vertex
or a half circle over the vertex.
"""
)
cn_disc("使用$setLineCap$方法调整的线帽设置，"
        "决定了终止线的终点是在顶点处的正方形、"
        "顶点上方的正方形还是顶点上方的半圆。")

eg(examples.testcaps)

disc(
    """The line cap setting, like the line join setting, is only clearly
visible when the lines are thick."""
)
cn_disc("线帽设置和线条连接设置一样，只有在线条较粗时才会清晰可见。")

# illust(examples.caps, "line cap settings")
cn_illust(examples.caps, "直线帽子设置")

# heading3("Dashes and broken lines")
cn_heading3("破折号和断线")

disc(
    """
The $setDash$ method allows lines to be broken into dots or dashes.
"""
)
cn_disc("用$setDash$方法可以将线条分成点或破折号。")

eg(examples.testdashes)

disc(
    """
The patterns for the dashes or dots can be in a simple on/off repeating pattern
or they can be specified in a complex repeating pattern.
"""
)
cn_disc("虚线或圆点的图案可以是简单的开/关重复图案，也可以指定为复杂的重复图案。")

# illust(examples.dashes, "some dash patterns")
cn_illust(examples.dashes, "破折号")

# heading3("Creating complex figures with path objects")
cn_heading3("用路径对象创建复杂的图形")

disc(
    """
Combinations of lines, curves, arcs and other figures can be combined into a 
single figure using path objects. For example the function shown below 
constructs two path objects using lines and curves. This function will be 
used later on as part of a pencil icon construction.
"""
)
cn_disc("线条、曲线、弧线等图形的组合可以使用路径对象组合成一个图形。"
        "例如下图所示的函数就是利用直线和曲线构造两个路径对象。"
        "这个函数将在后面的铅笔图标构造中使用。")

eg(examples.testpenciltip)

disc(
    """
Note that the interior of the pencil tip is filled as one object even though 
it is constructed from several lines and curves.  The pencil lead is then
drawn over it using a new path object.
"""
)
cn_disc("请注意，铅笔头的内部是作为一个对象填充的，即使它是由几条线和曲线构成的。"
        "然后使用一个新的路径对象在其上绘制铅笔头。")

# illust(examples.penciltip, "a pencil tip")
cn_illust(examples.penciltip, "铅笔头")

# heading2('Rectangles, circles, ellipses')
cn_heading2("矩形、圆形、椭圆形。")

disc(
    """
The $pdfgen$ module supports a number of generally useful shapes
such as rectangles, rounded rectangles, ellipses, and circles.
Each of these figures can be used in path objects or can be drawn
directly on a $canvas$.  For example the $pencil$ function below
draws a pencil icon using rectangles and rounded rectangles with
various fill colors and a few other annotations.
"""
)
cn_disc("$pdfgen$模块支持许多一般有用的形状，如矩形、圆角矩形、椭圆和圆。"
        "这些图形中的每一个都可以在路径对象中使用，也可以直接在$canvas$上绘制。 "
        "例如下面的$pencil$函数使用矩形和圆角矩形绘制了一个铅笔图标，"
        "并添加了各种填充颜色和其他一些注释。")

eg(examples.testpencil)

pencilnote()

disc(
    """
Note that this function is used to create the "margin pencil" to the left.
Also note that the order in which the elements are drawn are important
because, for example, the white rectangles "erase" parts of a black rectangle
and the "tip" paints over part of the yellow rectangle.
"""
)
cn_disc("注意，这个函数是用来创建左边的'边距铅笔'的。"
        "还要注意的是，元素的绘制顺序很重要，因为，"
        "例如，白色矩形'擦掉'了黑色矩形的一部分，"
        "而 '笔尖'则涂抹了黄色矩形的一部分。")

# illust(examples.pencil, "a whole pencil")
cn_illust(examples.pencil, "铅笔")

# heading2('Bezier curves')
cn_heading2("贝兹尔曲线")

disc(
    """
Programs that wish to construct figures with curving borders
generally use Bezier curves to form the borders.
"""
)
cn_disc("想要构造具有弯曲边界的图形的程序，一般使用贝塞尔曲线来形成边界。")

eg(examples.testbezier)

disc(
    """
A Bezier curve is specified by four control points $(x1,y1)$, $(x2,y2)$, 
$(x3,y3)$, $(x4,y4)$. The curve starts at $(x1,y1)$ and ends at $(x4,y4)$ 
and the line segment from $(x1,y1)$ to $(x2,y2)$ 
and the line segment from $(x3,y3)$ to $(x4,y4)$ 
both form tangents to the curve.  
Furthermore the curve is entirely contained in the convex figure with vertices at the control points.
"""
)
cn_disc("Bezier曲线由四个控制点$(x1,y1)$，$(x2,y2)$，$(x3,y3)$，$(x4,y4)$指定。"
        "曲线起于$(x1,y1)$，止于$(x4,y4)$，从$(x1,y1)$到$(x2,y2)$的线段和从$(x3,y3)$到$(x4,y4)$的线段都与曲线形成切线。 "
        "而且曲线完全包含在凸图形中，顶点在控制点上。")

# illust(examples.bezier, "basic bezier curves")
cn_illust(examples.bezier, "基本贝塞尔曲线")

disc(
    """
The drawing above (the output of $testbezier$) shows a bezier curves, 
the tangent lines defined by the control points and the convex figure with 
vertices at the control points.
"""
)
cn_disc("上图($testbezier$的输出)显示了一个bezier曲线、控制点定义的切线和控制点处有顶点的凸图形。")

# heading3("Smoothly joining bezier curve sequences")
cn_heading3("平滑地连接贝塞尔曲线序列")

disc(
    """
It is often useful to join several bezier curves to form a
single smooth curve.  To construct a larger smooth curve from
several bezier curves make sure that the tangent lines to adjacent
bezier curves that join at a control point lie on the same line.
"""
)
cn_disc("通常情况下，将几条贝塞尔曲线连接成一条平滑曲线是很有用的。 "
        "要想从几条贝塞尔曲线中构造一条较大的平滑曲线，"
        "请确保相邻贝塞尔曲线在控制点连接的切线位于同一直线上。")

eg(examples.testbezier2)

disc(
    """
The figure created by $testbezier2$ describes a smooth complex curve because 
adjacent tangent lines "line up" as illustrated below.
"""
)
cn_disc('由$testbezier2$创建的图形描述了一条平滑的复曲线，因为相邻的切线 "排队"，如下图所示。')

# illust(examples.bezier2, "bezier curves")
cn_illust(examples.bezier2, "bezier curves")

# heading2("Path object methods")
cn_heading2('路径对象方法')

disc(
    """
Path objects build complex graphical figures by setting
the "pen" or "brush" at a start point on the canvas and drawing
lines or curves to additional points on the canvas.  Most operations
apply paint on the canvas starting at the end point of the last
operation and leave the brush at a new end point.
"""
)
cn_disc('路径对象通过在画布上的起始点设置 "笔 "或 "画笔"，'
        '并在画布上的附加点上绘制线条或曲线，从而建立复杂的图形。 '
        '大多数操作都是从上一次操作的终点开始在画布上涂抹颜料，并在新的终点留下画笔。')

eg("""pathobject.moveTo(x,y)""")

disc(
    """
The $moveTo$ method lifts the brush (ending any current sequence
of lines or curves if there is one) and replaces the brush at the
new ^(x,y)^ location on the canvas to start a new path sequence.
"""
)
cn_disc("$moveTo$方法抬起画笔(结束任何当前的线条或曲线序列(如果有的话))，"
        "并在画布上新的^(x,y)^位置替换画笔，开始一个新的路径序列。")

eg("""pathobject.lineTo(x,y)""")

disc(
    """
The $lineTo$ method paints straight line segment from the current brush
location to the new ^(x,y)^ location.
"""
)
cn_disc("$lineTo$方法从当前笔刷位置到新的^(x,y)^位置绘制直线段。")

eg("""pathobject.curveTo(x1, y1, x2, y2, x3, y3) """)

disc(
    """
The $curveTo$ method starts painting a Bezier curve beginning at
the current brush location, using ^(x1,y1)^, ^(x2,y2)^, and ^(x3,y3)^
as the other three control points, leaving the brush on ^(x3,y3)^.
"""
)
cn_disc("$curveTo$方法从当前画笔位置开始绘制一条贝塞尔曲线，"
        "使用^(x1,y1)^、^(x2,y2)^和^(x3,y3)^作为其他三个控制点，"
        "将画笔留在^(x3,y3)^上。")

eg("""pathobject.arc(x1,y1, x2,y2, startAng=0, extent=90) """)

eg("""pathobject.arcTo(x1,y1, x2,y2, startAng=0, extent=90) """)

disc(
    """
The $arc$ and $arcTo$ methods paint partial ellipses.  The $arc$ method first 
"lifts the brush" and starts a new shape sequence.  The $arcTo$ method joins 
the start of the partial ellipse to the current shape sequence by line 
segment before drawing the partial ellipse.  The points ^(x1,y1)^ and ^(x2,
y2)^ define opposite corner points of a rectangle enclosing the ellipse.  
The $startAng$ is an angle (in degrees) specifying where to begin the partial ellipse where the 0 angle is the midpoint of the right border of 
the enclosing rectangle (when ^(x1,y1)^ is the lower left corner and ^(x2,
y2)^ is the upper right corner).  The $extent$ is the angle in degrees to 
traverse on the ellipse.
"""
)
cn_disc('$arc$和$arcTo$方法可以绘制部分椭圆。 '
        '$arc$方法首先 "提起画笔 "并开始一个新的形状序列。 '
        '而$arcTo$方法则是将部分椭圆的起始点与当前的形状序列用线连接起来。 '
        '在画部分椭圆之前，先画出部分椭圆的线段。 '
        '点^（x1，y1）^和^（x2, y2)^定义包围椭圆的矩形的相对角点。 '
        'startAng$是一个角度(度数)，指定了部分椭圆的开始位置，其中0角是右边界的中点。 '
        '围成的矩形（当^(x1,y1)^为左下角，^(x2, y2）^为右上角）.'
        '$extent$是指与椭圆上的横移。')

eg(examples.testarcs)

disc(
    """The $arcs$ function above exercises the two partial ellipse methods.
It produces the following drawing."""
)
cn_disc("上面的$arcs$函数行使了两种局部椭圆方法。它产生了下面的图形。")

# illust(examples.arcs, "arcs in path objects")
cn_illust(examples.arcs, "弧线")

eg("""pathobject.rect(x, y, width, height) """)

disc(
    """The $rect$ method draws a rectangle with lower left corner
at ^(x,y)^ of the specified ^width^ and ^height^."""
)
cn_disc("$rect$方法在^(x,y)^指定的^width^和^height^处画一个左下角的矩形。")

eg("""pathobject.ellipse(x, y, width, height)""")

disc(
    """The $ellipse$ method
draws an ellipse enclosed in the rectange with lower left corner
at ^(x,y)^ of the specified ^width^ and ^height^.
"""
)
cn_disc("$ellipse$方法在指定的^width^和^height^的^(x,y)^处绘制一个左下角的矩形包围的椭圆。")

eg("""pathobject.circle(x_cen, y_cen, r) """)

disc(
    """The $circle$ method
draws a circle centered at ^(x_cen, y_cen)^ with radius ^r^.
"""
)
cn_disc("circle$方法画一个以^(x_cen，y_cen)^为中心，半径^r^的圆。")

eg(examples.testvariousshapes)

disc(
    """
The $variousshapes$ function above shows a rectangle, circle and ellipse
placed in a frame of reference grid.
"""
)
cn_disc("上面的$variousshapes$函数显示了一个放置在参考网格中的矩形、圆和椭圆。")

# illust(examples.variousshapes, "rectangles, circles, ellipses in path objects")
cn_illust(examples.variousshapes, "路径对象中的矩形、圆形、椭圆形。")

eg("""pathobject.close() """)

disc(
    """
The $close$ method closes the current graphical figure
by painting a line segment from the last point of the figure
to the starting point of the figure (the the most
recent point where the brush was placed on the paper by $moveTo$
or $arc$ or other placement operations).
"""
)
cn_disc("$close$方法通过从图形的最后一点到图形的起始点(最近一次通过$moveTo$或$arc$或其他放置操作将画笔放置在纸上的点)画一条线段来关闭当前图形。")

eg(examples.testclosingfigures)

disc(
    """
The $closingfigures$ function illustrates the
effect of closing or not closing figures including a line
segment and a partial ellipse.
"""
)
cn_disc("$closingfigures$函数说明了闭合或不闭合图形的效果，包括一条线段和一个部分椭圆。")

# illust(examples.closingfigures, "closing and not closing patho bject figures")
cn_illust(examples.closingfigures, "闭合和不闭合的路径对象数字")

disc(
    """
Closing or not closing graphical figures effects only the stroked outline
of a figure, not the filling of the figure as illustrated above.
"""
)
cn_disc("关闭或不关闭图形只影响图形的描边轮廓，而不影响图形的填充，如上图所示。")

disc(
    """
For a more extensive example of drawing using a path object examine the 
$hand$ function.
"""
)
cn_disc("关于使用路径对象绘图的更广泛的例子，请检查$hand$函数。")

eg(examples.testhand)

disc(
    """
In debug mode (the default) the $hand$ function shows the tangent line segments
to the bezier curves used to compose the figure.  Note that where the segments
line up the curves join smoothly, but where they do not line up the curves show
a "sharp edge".
"""
)
cn_disc('在调试模式下(默认)，$hand$函数显示了用于构成图形的贝塞尔曲线的切线段。'
        '请注意，当线段对齐时，曲线平滑地连接在一起，但当线段不对齐时，曲线显示出一个 "尖锐的边缘"。')

# illust(examples.hand, "an outline of a hand using bezier curves")
cn_illust(examples.hand, "手形图")

disc(
    """
Used in non-debug mode the $hand$ function only shows the
Bezier curves.  With the $fill$ parameter set the figure is
filled using the current fill color.
"""
)
cn_disc("在非调试模式下，$hand$函数只显示贝塞尔曲线。 "
        "如果设置了$fill$参数，则会使用当前的填充颜色填充图形。")

eg(examples.testhand2)

disc(
    """
Note that the "stroking" of the border draws over the interior fill where
they overlap.
"""
)
cn_disc('注意，边框的 "描边 "画在它们重叠的内部填充物上。')

# illust(examples.hand2, "the finished hand, filled")
cn_illust(examples.hand2, "妙手回春")

# heading2("Further Reading: The ReportLab Graphics Library")
cn_heading2("进一步阅读: ReportLab图形库")

disc(
    """
So far the graphics we have seen were created on a fairly low level.
It should be noted, though, that there is another way of creating
much more sophisticated graphics using the dedicated
high-level <i>ReportLab Graphics Library</i>.
"""
)
cn_disc("到目前为止，我们所看到的图形是在相当低的水平上创建的。"
        "但应该注意的是，还有一种方法可以使用专用的高级<i>ReportLab图形库</i>创建更复杂的图形。")

disc(
    """
It can be used to produce high-quality, platform-independant,
reusable graphics for different output formats (vector and bitmap)
like PDF, EPS, SVG, JPG and PNG.
"""
)
cn_disc("它可以用来为不同的输出格式（矢量图和位图）如PDF、EPS、SVG、JPG和PNG等制作高质量的、独立于平台的、可重复使用的图形。")

disc(
    """
A more thorough description of its philosophy and features is
now covered in Chapter 11 of this document, <i>Graphics</i>, which 
contains information about the existing components and
how to create customized ones.
"""
)
cn_disc("本文档第11章<i>绘图</i>对其理念和功能进行了更详尽的描述，其中包含了现有组件的信息以及如何创建自定义组件。")

disc(
    """
Chapter 11 also contains details of the ReportLab 
charting package and its components (labels, axes, legends and
different types of charts like bar, line and pie charts) that
builds directly on the graphics library.
"""
)
cn_disc("第11章还详细介绍了ReportLab图表包及其组件（标签、坐标轴、图例和不同类型的图表，如柱状图、线状图和饼状图），"
        "它直接建立在图形库上。")



##### FILL THEM IN
