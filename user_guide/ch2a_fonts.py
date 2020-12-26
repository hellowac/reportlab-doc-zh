import os

import reportlab
from reportlab.platypus import Image
from reportlab.lib.codecharts import SingleByteEncodingChart
from reportlab.pdfbase.pdfmetrics import registerFontFamily
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
)
from utils import examples


# heading1("Fonts and encodings")
cn_heading1("字体和编码")

disc(
    """
This chapter covers fonts, encodings and Asian language capabilities.
If you are purely concerned with generating PDFs for Western
European languages, you can just read the "Unicode is the default" section
below and skip the rest on a first reading. We expect this section to grow 
considerably over time. We hope that Open Source will enable us to give 
better support for more of the world's languages than other tools, and we 
welcome feedback and help in this area.
"""
)
cn_disc('本章包括字体、编码和亚洲语言功能。'
        '如果你只关心生成西欧语言的PDF，你可以只读下面的 "Unicode是默认的"部分，并在第一次阅读时跳过其余部分。'
        '我们希望随着时间的推移，这部分内容会有很大的增长。'
        '我们希望开源能让我们比其他工具更好地支持世界上更多的语言，'
        '我们欢迎在这方面的反馈和帮助。')

# heading2("Unicode and UTF8 are the default input encodings")
cn_heading2('Unicode 和 UTF8 是默认编码')

disc(
    """
Starting with reportlab Version 2.0 (May 2006), all text input you
provide to our APIs should be in UTF8 or as Python Unicode objects.
This applies to arguments to canvas.drawString and related APIs,
table cell content, drawing object parameters, and paragraph source
text.  
"""
)
cn_disc('从reportlab 2.0版本(2006年5月)开始，您提供给我们API的所有文本输入都应该是UTF8或Python Unicode对象。'
        '这适用于 canvas.drawString 和相关 API 的参数、表格单元格内容、绘图对象参数和段落源文本。 ')

disc(
    """
We considered making the input encoding configurable or even locale-dependent,
but decided that "explicit is better than implicit"."""
)
cn_disc('我们曾考虑过让输入编码可配置，甚至依赖于本地，但决定 "显式比隐式好"。')


disc(
    """
This simplifies many things we used to do previously regarding greek
letters, symbols and so on.  To display any character, find out its
unicode code point, and make sure the font you are using is able
to display it."""
)
cn_disc('这简化了我们以前做的许多关于希腊字母、符号等的事情。 '
        '要显示任何字符，找出它的unicode码点，并确保你使用的字体能够显示它。')


disc(
    """
If you are adapting a ReportLab 1.x application, or reading data from
another source which contains single-byte data (e.g. latin-1 or WinAnsi),
you need to do a conversion into Unicode.  The Python codecs package now
includes converters for all the common encodings, including Asian ones.
"""
)
cn_disc('如果您正在改编 ReportLab 1.x 应用程序，'
        '或者从其他包含单字节数据的源头读取数据 (例如 latin-1 或 WinAnsi)，'
        '您需要进行 Unicode 转换。 '
        'Python 编解码器包现在包含了所有常用编码的转换器，包括亚洲的编码。')


disc(
    u"""
If your data is not encoded as UTF8, you will get a UnicodeDecodeError as
soon as you feed in a non-ASCII character.  For example, this snippet below is
attempting to read in and print a series of names, including one with a French
accent:  ^Marc-Andr\u00e9 Lemburg^.  The standard error is quite helpful and 
tells you what character it doesn't like:
"""
)
cn_disc('如果你的数据不是UTF8编码，那么一旦你输入一个非ASCII字符，'
        '你就会得到一个UnicodeDecodeError。 '
        '例如，下面这个代码段试图读取并打印一系列名字，包括一个带有法国口音的名字。 '
        '^Marc -Andr/\u00e9 Lemburg^.  标准误差非常有用，它告诉你它不喜欢什么字符。')


eg(
    u"""
>>> from reportlab.pdfgen.canvas import Canvas
>>> c = Canvas('temp.pdf')
>>> y = 700
>>> for line in file('latin_python_gurus.txt','r'):
...     c.drawString(100, y, line.strip())
...
Traceback (most recent call last):
...
UnicodeDecodeError: 'utf8' codec can't decode bytes in position 9-11: invalid 
data
-->\u00e9 L<--emburg
>>> 
"""
)

disc(
    """
The simplest fix is just to convert your data to unicode, saying which encoding
it comes from, like this:"""
)
cn_disc('最简单的解决方法就是将你的数据转换为unicode，并说明它来自哪个编码，就像这样。')


eg(
    """
>>> for line in file('latin_input.txt','r'):
...     uniLine = unicode(line, 'latin-1')
...     c.drawString(100, y, uniLine.strip())
>>>
>>> c.save()
"""
)

# heading2("Automatic output font substitution")
cn_heading2('输出字体自动替换')


disc(
    """
There are still a number of places in the code, including the rl_config
defaultEncoding parameter, and arguments passed to various Font constructors,
which refer to encodings.  These were useful in the past when people needed to
use glyphs in the Symbol and ZapfDingbats fonts which are supported by PDF
viewing devices. By default the standard fonts (Helvetica, Courier, Times Roman)
will offer the glyphs available in Latin-1.  However, if our engine detects
a character not in the font, it will attempt to switch to Symbol or 
ZapfDingbats to display these. For example, if you include the Unicode character for a pair 
of right-facing scissors, \\u2702, in a call to ^drawString^, you should see 
them (there is an example in ^test_pdfgen_general.py/pdf^).  It is not
necessary to switch fonts in your code.

"""
)
cn_disc('在代码中还有很多地方，包括^rl_config.defaultEncoding^参数，'
        '以及传递给各种 $Font$ 构造函数的参数，这些参数都是指编码。 '
        '在过去，当人们需要使用 $PDF$ 浏览设备支持的 $Symbol$ 和 $ZapfDingbats$ 字体的字形时，'
        '这些参数非常有用。'
        '默认情况下，标准字体（$Helvetica$、$Courier$、$Times Roman$）将提供 $Latin-1$ 的字形。 '
        '然而，如果我们的引擎检测到一个字体中没有的字符，它将尝试切换到 $Symbol$ 或 $ZapfDingbats$ 来显示这些字符。'
        '例如，如果你在对^drawString^的调用中包含了一对右面剪刀的 $Unicode$ 字符，\\u2702(\u2702),'
        '你应该会看到它们（在^test_pdfgen_general.py/pdf^中有一个例子）。 '
        '在你的代码中不需要切换字体。')


# heading2("Using non-standard Type 1 fonts")
cn_heading2('使用非标准的 $Type 1$ 字体')


disc(
    """
As discussed in the previous chapter, every copy of Acrobat Reader
comes with 14 standard fonts built in.  Therefore, the ReportLab
PDF Library only needs to refer to these by name.  If you want
to use other fonts, they must be available to your code and
will be embedded in the PDF document."""
)
cn_disc('正如前一章所讨论的那样，每份 $Acrobat Reader$ 都内置了14种标准字体。 '
        '因此，$ReportLab PDF$ 库只需要通过名称来引用这些字体。 '
        '如果您想使用其他字体，它们必须对您的代码可用，并将被嵌入到$PDF$文档中。')


disc(
    """
You can use the mechanism described below to include arbitrary
fonts in your documents. We have an open source font named 
<i>DarkGardenMK</i> which we may use for testing and/or documenting purposes 
(and which you may use as well). It comes bundled with the ReportLab 
distribution in the directory $reportlab/fonts$.
"""
)
cn_disc('您可以使用下面描述的机制在您的文档中包含任意字体。'
        '我们有一个名为<i>DarkGardenMK</i>的开源字体，'
        '我们可以将其用于测试 和或 文档目的（您也可以使用它）。'
        '它与ReportLab发行版捆绑在一起，在$reportlab/fonts$目录下。')


disc(
    """
Right now font-embedding relies on font description files in the Adobe
AFM ('Adobe Font Metrics') and PFB ('Printer Font Binary') format. The
former is an ASCII file and contains information about the characters
('glyphs') in the font such as height, width, bounding box info and
other 'metrics', while the latter is a binary file that describes the
shapes of the font. The $reportlab/fonts$ directory contains the files
$'DarkGardenMK.afm'$ and $'DarkGardenMK.pfb'$ that are used as an example
font.
"""
)
cn_disc('目前，字体嵌入依赖于$Adobe AFM("Adobe Font Metrics")$'
        '和$PFB("Printer Font Binary")$格式的字体描述文件。'
        '前者是一个$ASCII$文件，包含字体中的字符（"字形"）信息，如高度、宽度、边界框信息和其他 "$metrics$"(指标)，'
        '而后者是一个二进制文件，描述字体的形状。'
        '在$reportlab/fonts$目录下，'
        '包含了$"DarkGardenMK.afm"$和$"DarkGardenMK.pfb"$两个文件，'
        '这两个文件被用来作为一个例子字体。')


disc(
    """
In the following example locate the folder containing the test font and
register it for future use with the $pdfmetrics$ module,
after which we can use it like any other standard font.
"""
)
cn_disc('在下面的例子中，找到包含测试字体的文件夹，并用$pdfmetrics$模块注册它，以便将来使用，'
        '之后我们可以像其他标准字体一样使用它。')


eg(
    """
import os
import reportlab
folder = os.path.dirname(reportlab.__file__) + os.sep + 'fonts'
afmFile = os.path.join(folder, 'DarkGardenMK.afm')
pfbFile = os.path.join(folder, 'DarkGardenMK.pfb')

from reportlab.pdfbase import pdfmetrics
justFace = pdfmetrics.EmbeddedType1Face(afmFile, pfbFile)
faceName = 'DarkGardenMK' # pulled from AFM file
pdfmetrics.registerTypeFace(justFace)
justFont = pdfmetrics.Font('DarkGardenMK',
                           faceName,
                           'WinAnsiEncoding')
pdfmetrics.registerFont(justFont)

canvas.setFont('DarkGardenMK', 32)
canvas.drawString(10, 150, 'This should be in')
canvas.drawString(10, 100, 'DarkGardenMK')
"""
)

disc(
    """
Note that the argument "WinAnsiEncoding" has nothing to do with the input;
it's to say which set of characters within the font file will be active
and available.
"""
)
cn_disc('请注意，参数 "$WinAnsiEncoding$"与输入无关，它是说字体文件内的哪一组字符将被激活并可用。')


# illust(examples.customfont1, "Using a very non-standard font")
cn_illust(examples.customfont1, "使用非常不标准的字体")


disc(
    """
The font's facename comes from the AFM file's $FontName$ field.
In the example above we knew the name in advance, but quite
often the names of font description files are pretty cryptic
and then you might want to retrieve the name from an AFM file
automatically. When lacking a more sophisticated method you can use some
code as simple as this:
"""
)
cn_disc('字体的名称来自$AFM$文件的$FontName$字段。'
        '在上面的例子中，我们事先知道了这个名字，但是很多时候字体描述文件的名字是非常神秘的，'
        '那么你可能会想从$AFM$文件中自动检索到这个名字。'
        '当缺乏更复杂的方法时，你可以使用一些像这样简单的代码。')


eg(
    """
class FontNameNotFoundError(Exception):
    pass


def findFontName(path):
    "Extract a font name from an AFM file."

    f = open(path)

    found = 0
    while not found:
        line = f.readline()[:-1]
        if not found and line[:16] == 'StartCharMetrics':
            raise FontNameNotFoundError, path
        if line[:8] == 'FontName':
            fontName = line[9:]
            found = 1

    return fontName
"""
)

disc(
    """
In the <i>DarkGardenMK</i> example we explicitely specified
the place of the font description files to be loaded. In general, you'll 
prefer to store your fonts in some canonic locations and make the embedding 
mechanism aware of them. Using the same configuration mechanism we've already seen at the
beginning of this section we can indicate a default search path for Type-1 
fonts.
"""
)
cn_disc('在<i>DarkGardenMK</i>的例子中，我们明确指定了要加载的字体描述文件的位置。'
        '一般来说，你会更倾向于将你的字体存储在一些规范的位置，并让嵌入机制知道它们。'
        '使用同样的配置机制，我们已经在本节开头看到了，我们可以为Type-1字体指定一个默认的搜索路径。')


disc(
    """
Unfortunately, there is no reliable standard yet for such
locations (not even on the same platform) and, hence, you might
have to edit one of the files $reportlab_settings.py$ or 
$~/.reportlab_settings$ to modify the value of the $T1SearchPath$ identifier 
to contain additional directories.  
Our own recommendation is to use the ^reportlab/fonts^
folder in development; and to have any needed fonts as packaged parts of
your application in any kind of controlled server deployment.  This insulates
you from fonts being installed and uninstalled by other software or system
administrator.
"""
)
cn_disc('不幸的是，目前还没有一个可靠的标准来规定这些位置（甚至在同一个平台上也没有），'
        '因此，你可能需要编辑$reportlab_settings.py$'
        '或者$~/.reportlab_settings$来修改$T1SearchPath$标识符的值，'
        '以包含额外的目录。 '
        '我们自己的建议是在开发中使用^reportlab/fonts^文件夹；并且在任何受控服务器部署中，将任何需要的字体作为应用程序的打包部件。 '
        '这样可以避免字体被其他软件或系统管理员安装和卸载。')


# heading3("Warnings about missing glyphs")
cn_heading3('关于缺失字形的警告')

disc(
    """If you specify an encoding, it is generally assumed that
the font designer has provided all the needed glyphs.  However,
this is not always true.  In the case of our example font,
the letters of the alphabet are present, but many symbols and
accents are missing.  The default behaviour is for the font to
print a 'notdef' character - typically a blob, dot or space -
when passed a character it cannot draw.  However, you can ask
the library to warn you instead; the code below (executed
before loading a font) will cause warnings to be generated
for any glyphs not in the font when you register it."""
)
cn_disc('如果你指定了一个编码，一般会认为字体设计师已经提供了所有需要的字形。 '
        '然而，事实并非总是如此。 '
        '在我们的示例字体中，字母表中的字母都存在，但许多符号和重音都没有。 '
        '默认的行为是，当传递给字体一个它无法绘制的字符时，字体会打印一个 "notdef "字符'
        '--通常是一个blob、点或空格。 '
        '然而，你可以要求库警告你；'
        '下面的代码（在加载字体之前执行）将导致在你注册字体时，对任何不在字体中的字形产生警告。')


eg(
    """
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
"""
)

# heading2("Standard Single-Byte Font Encodings")
cn_heading2('标准的单字节字体编码')

disc(
    """
This section shows you the glyphs available in the common encodings.
"""
)
cn_disc('本节为您展示常用编码中可用的字形。')


disc(
    """The code chart below shows the characters in the $WinAnsiEncoding$.
This is the standard encoding on Windows and many Unix systems in America
and Western Europe.  It is also knows as Code Page 1252, and is practically
identical to ISO-Latin-1 (it contains one or two extra characters). This
is the default encoding used by the Reportlab PDF Library. It was generated from
a standard routine in $reportlab/lib$, $codecharts.py$,
which can be used to display the contents of fonts.  The index numbers
along the edges are in hex."""
)
cn_disc('下面的代码表显示了$WinAnsiEncoding$中的字符，'
        '这是Windows和许多美国和西欧Unix系统的标准编码。'
        '这是在美国和西欧的Windows和许多Unix系统上的标准编码，也被称为Code Page 1252，'
        '实际上与ISO-Latin-1相同（包含一个或两个额外的字符）。 '
        '这是Reportlab PDF库使用的默认编码。'
        '它由$reportlab/lib$中的一个标准例程$codecharts.py$生成，'
        '可用于显示字体的内容。 沿边的索引号是以十六进制表示的。')


cht1 = SingleByteEncodingChart(
    encodingName='WinAnsiEncoding', charsPerRow=32, boxSize=12
)
illust(
    lambda canv: cht1.drawOn(canv, 0, 0),
    "WinAnsi Encoding",
    cht1.width,
    cht1.height,
)

disc(
    """The code chart below shows the characters in the $MacRomanEncoding$.
as it sounds, this is the standard encoding on Macintosh computers in
America and Western Europe.  As usual with non-unicode encodings, the first
128 code points (top 4 rows in this case) are the ASCII standard and agree
with the WinAnsi code chart above; but the bottom 4 rows differ."""
)
cn_disc('下面的代码表显示了$MacRomanEncoding$中的字符，'
        '听起来，这是美国和西欧Macintosh电脑上的标准编码。 '
        '和通常的非unicode编码一样，前128个码点（在本例中，最上面4行）是ASCII标准，'
        '并与上面的WinAnsi代码表一致；但下面4行不同。')

cht2 = SingleByteEncodingChart(
    encodingName='MacRomanEncoding', charsPerRow=32, boxSize=12
)
illust(
    lambda canv: cht2.drawOn(canv, 0, 0),
    "MacRoman Encoding",
    cht2.width,
    cht2.height,
)

disc(
    """These two encodings are available for the standard fonts (Helvetica,
Times-Roman and Courier and their variants) and will be available for most
commercial fonts including those from Adobe.  However, some fonts contain non-
text glyphs and the concept does not really apply.  For example, ZapfDingbats
and Symbol can each be treated as having their own encoding."""
)
cn_disc('这两种编码适用于标准字体（Helvetica、Times-Roman和Courier及其变体），'
        '并将适用于大多数商业字体，包括Adobe的字体。 '
        '然而，有些字体包含非文本字形，这个概念并不真正适用。 '
        '例如，ZapfDingbats和Symbol可以被视为各自拥有自己的编码。')


cht3 = SingleByteEncodingChart(
    faceName='ZapfDingbats',
    encodingName='ZapfDingbatsEncoding',
    charsPerRow=32,
    boxSize=12,
)
# illust(
#     lambda canv: cht3.drawOn(canv, 0, 0),
#     "ZapfDingbats and its one and only encoding",
#     cht3.width,
#     cht3.height,
# )
cn_illust(
    lambda canv: cht3.drawOn(canv, 0, 0),
    "ZapfDingbats和它的唯一编码。",
    cht3.width,
    cht3.height,
)

cht4 = SingleByteEncodingChart(
    faceName='Symbol', encodingName='SymbolEncoding', charsPerRow=32, boxSize=12
)
# illust(
#     lambda canv: cht4.drawOn(canv, 0, 0),
#     "Symbol and its one and only encoding",
#     cht4.width,
#     cht4.height,
# )
cn_illust(
    lambda canv: cht4.drawOn(canv, 0, 0),
    "符号及其唯一的编码",
    cht4.width,
    cht4.height,
)

CPage(5)
# heading2("TrueType Font Support")
cn_heading2('支持TrueType字体')

disc(
    """
Marius Gedminas ($mgedmin@delfi.lt$) with the help of Viktorija Zaksiene (
$vika@pov.lt$) have contributed support for embedded TrueType fonts.  
TrueType fonts work in Unicode/UTF8 and are not limited to 256 characters."""
)
cn_disc('Marius Gedminas ($mgedmin@delfi.lt$)'
        '在Viktorija Zaksiene ($vika@pov.lt$)的帮助下，为嵌入式TrueType字体提供了支持。 '
        'TrueType字体可以在Unicode/UTF8中使用，并且不限于256个字符。')

CPage(3)
disc(
    """We use <b>$reportlab.pdfbase.ttfonts.TTFont$</b> to create a true type
font object and register using <b>$reportlab.pdfbase.pdfmetrics.registerFont$</b>.
In pdfgen drawing directly to the canvas we can do"""
)
cn_disc('我们使用<b>$reportlab.pdfbase.ttfonts.TTFont$</b>来创建一个真正的字体对象，'
        '并使用<b>$reportlab.pdfbase.pdfmetrics.registerFont$</b>进行注册。'
        '在pdfgen直接在画布上绘图时我们可以这样做')

eg(
    """
# we know some glyphs are missing, suppress warnings
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
canvas.setFont('Vera', 32)
canvas.drawString(10, 150, "Some text encoded in UTF-8")
canvas.drawString(10, 100, "In the Vera TT Font!")
"""
)
# illust(examples.ttffont1, "Using a the Vera TrueType Font")
cn_illust(examples.ttffont1, "使用Vera TrueType字体")

disc("""In the above example the True Type font object is created using""")
cn_disc('在上面的例子中，True Type字体对象是使用')

eg(
    """
    TTFont(name,filename)
"""
)
disc(
    """so that the ReportLab internal name is given by the first argument and 
the second argument is a string(or file like object) denoting the font's TTF 
file. In Marius' original patch the filename was supposed to be exactly 
correct, but we have modified things so that if the filename is relative
then a search for the corresponding file is done in the current directory and 
then in directories specified by $reportlab.rl_config.TTFSearchpath$!"""
)
cn_disc('所以ReportLab的内部名称由第一个参数给出，'
        '第二个参数是一个字符串（或类似文件的对象），表示字体的TTF文件。'
        '在Marius最初的补丁中，文件名应该是完全正确的，'
        '但我们已经修改了，如果文件名是相对的，'
        '那么在当前目录下搜索相应的文件，'
        '然后在$reportlab.rl_config.TTFSearchpath$!')


registerFontFamily(
    'Vera', normal='Vera', bold='VeraBd', italic='VeraIt', boldItalic='VeraBI'
)

disc(
    """Before using the TT Fonts in Platypus we should add a mapping from the family name to the individual font names that describe the behaviour under the $&lt;b&gt;$ and 
$&lt;i&gt;$ attributes."""
)
cn_disc('在使用Platypus中的TT字体之前，'
        '我们应该在$&lt;b&gt;$和$&lt;i&gt;$'
        '属性下添加一个从家族名称到描述行为的单个字体名称的映射。')

eg(
    """
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily('Vera',normal='Vera',bold='VeraBd',italic='VeraIt',
boldItalic='VeraBI')
"""
)

disc(
    """If we only have a Vera regular font, no bold or italic then we must 
map all to the same internal fontname.  ^&lt;b&gt;^ and ^&lt;i&gt;^ tags may 
now be used safely, but have no effect. After registering and mapping
the Vera font as above we can use paragraph text like"""
)
cn_disc('如果我们只有一个Vera常规字体，没有粗体或斜体，那么我们必须将所有字体映射到同一个内部字体名。 '
        '^&lt;b&gt;^和^&lt;i&gt;^标签现在可以安全使用，但没有效果。'
        '如上所述注册和映射Vera字体后，我们可以使用段落文本，如')

parabox2(
    """<font name="Times-Roman" size="14">This is in Times-Roman</font>
<font name="Vera" color="magenta" size="14">and this is in magenta 
<b>Vera!</b></font>""",
    "Using TTF fonts in paragraphs",
)

# heading2("Asian Font Support")
cn_heading2('亚洲字体支持')

disc(
    """The Reportlab PDF Library aims to expose full support for Asian fonts.
PDF is the first really portable solution for Asian text handling. There are
two main approaches for this:  Adobe's Asian Language Packs, or TrueType fonts.
"""
)
cn_disc('Reportlab PDF库旨在为亚洲字体提供全面支持。'
        'PDF是第一个真正可移植的亚洲文本处理解决方案。'
        '有两种主要的方法。 Adobe的亚洲语言包，或者TrueType字体。')


# heading3("Asian Language Packs")
cn_heading3('亚洲语言包')

disc(
    """
This approach offers the best performance since nothing needs embedding in the PDF file;
as with the standard fonts, everything is on the reader."""
)
cn_disc('这种方法提供了最好的性能，因为没有任何东西需要嵌入到PDF文件中；与标准字体一样，一切都在阅读器上。')


disc(
    """
Adobe makes available add-ons for each main language.  In Adobe Reader 6.0 
and 7.0, you will be prompted to download and install these as soon as you 
try to open a document using them.  In earlier versions, you would see an 
error message on opening an Asian document and had to know what to do.   
"""
)
cn_disc('Adobe公司为每种主要语言都提供了附加组件。 '
        '在Adobe Reader 6.0和7.0中，当您尝试使用它们打开文档时，您会被提示下载并安装这些插件。 '
        '在早期的版本中，你会在打开亚洲文档时看到一个错误信息，你必须知道该怎么做。')


disc(
    """Japanese, Traditional Chinese (Taiwan/Hong Kong), Simplified Chinese (
mainland China) and Korean are all supported and our software knows about the following fonts:
"""
)
cn_disc('日文、繁体中文(台湾/香港)、简体中文(中国大陆)和韩文都支持，我们的软件知道以下字体。')

bullet(
    """
$chs$ = Chinese Simplified (mainland): '$SourceHanSansSC$'
"""
)

bullet(
    """
$cht$ = Chinese Traditional (Taiwan): '$MSung-Light$', '$MHei-Medium$'
"""
)
bullet(
    """
$kor$ = Korean: '$HYSMyeongJoStd-Medium$','$HYGothic-Medium$'
"""
)
bullet(
    """
$jpn$ = Japanese: '$HeiseiMin-W3$', '$HeiseiKakuGo-W5$'
"""
)

disc(
    """Since many users will not have the font packs installed, we have included
a rather grainy ^bitmap^ of some Japanese characters.  We will discuss below 
what is needed to generate them."""
)
cn_disc('由于许多用户不会安装字体包，我们已经包含了一些日文字符的相当颗粒状的^bitmap^。 下面我们将讨论生成它们所需要的内容。')

# include a bitmap of some Asian text
I = os.path.join('images', 'jpnchars.jpg')
try:
    getStory().append(Image(I))
except:
    disc("""An image should have appeared here.""")
    cn_disc('一个图片应该出现在这儿')


disc(
    """Prior to Version 2.0, you had to specify one of many native encodings
when registering a CID Font. In version 2.0 you should a new UnicodeCIDFont
class."""
)
cn_disc('在2.0版本之前，当你注册一个CID Font时，'
        '你必须指定许多本地编码之一。'
        '在2.0版本中，你应该使用一个新的UnicodeCIDFont类。')

eg(
    """
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
canvas.setFont('HeiseiMin-W3', 16)

# the two unicode characters below are "Tokyo"
msg = u'\\u6771\\u4EAC : Unicode font, unicode input'
canvas.drawString(100, 675, msg)
"""
)
# had to double-escape the slashes above to get escapes into the PDF

disc(
    """The old coding style with explicit encodings should still work, 
but is now only relevant if you need to construct vertical text.  We aim to 
add more readable options for horizontal and vertical text to the 
UnicodeCIDFont constructor in future. The following four test scripts 
generate samples in the corresponding languages:"""
)
cn_disc('旧的编码风格与显式编码应该仍然有效，但现在只有当你需要构建垂直文本时才有意义。 '
        '我们的目标是在未来为UnicodeCIDFont构造函数添加更多可读的水平和垂直文本选项。'
        '以下四个测试脚本会生成相应语言的样本。')

eg(
    """tests/test_multibyte_jpn.py
tests/test_multibyte_kor.py
tests/test_multibyte_chs.py
tests/test_multibyte_cht.py"""
)

## put back in when we have vertical text...
##disc("""The illustration below shows part of the first page
##of the Japanese output sample.  It shows both horizontal and vertical
##writing, and illustrates the ability to mix variable-width Latin
##characters in Asian sentences.  The choice of horizontal and vertical
##writing is determined by the encoding, which ends in 'H' or 'V'.
##Whether an encoding uses fixed-width or variable-width versions
##of Latin characters also depends on the encoding used; see the definitions
##below.""")
##
##Illustration(image("../images/jpn.gif", width=531*0.50,
##height=435*0.50), 'Output from test_multibyte_jpn.py')
##
##caption("""
##Output from test_multibyte_jpn.py
##""")


disc(
    """In previous versions of the ReportLab PDF Library, we had to make
use of Adobe's CMap files (located near Acrobat Reader if the Asian Language
packs were installed).  Now that we only have one encoding to deal with, the
character width data is embedded in the package, and CMap files are not needed
for generation.  The CMap search path in ^rl_config.py^ is now deprecated
and has no effect if you restrict yourself to UnicodeCIDFont.
"""
)
cn_disc('在以前版本的ReportLab PDF库中，'
        '我们不得不使用Adobe的CMap文件（如果安装了亚洲语言包，则位于Acrobat Reader附近）。 '
        '现在我们只需要处理一种编码，字符宽度数据被嵌入到软件包中，生成时不需要CMap文件。 '
        '在^rl_config.py^中的CMap搜索路径现在已经被废弃，'
        '如果你限制自己使用UnicodeCIDFont，则没有效果。')


# heading3("TrueType fonts with Asian characters")
cn_heading3('TrueType字体和亚洲字符')

disc(
    """
This is the easy way to do it.  No special handling at all is needed to
work with Asian TrueType fonts.  Windows users who have installed, for example,
Japanese as an option in Control Panel, will have a font "msmincho.ttf" which
can be used.  However, be aware that it takes time to parse the fonts, and that
quite large subsets may need to be embedded in your PDFs.  We can also now parse
files ending in .ttc, which are a slight variation of .ttf.
"""
)
cn_disc('这就是简单的方法。 '
        '在使用亚洲TrueType字体时，完全不需要特殊的处理。 '
        '例如，在控制面板中安装了日语作为选项的Windows用户，'
        '会有一个可以使用的字体 "msmincho.ttf"。 '
        '然而，请注意，解析字体需要时间，而且相当大的子集可能需要嵌入你的PDF中。 '
        '我们现在也可以解析以.ttc结尾的文件，它们是.ttf的轻微变化。')


heading3("To Do")
# cn_heading3('aaa')

disc(
    """We expect to be developing this area of the package for some time 
.accept2dyear Here is an outline of the main priorities.  We welcome help!"""
)
cn_disc('我们预计将在一段时间内开发这个领域的包.accept2dyear这是一个主要优先事项的大纲。 我们欢迎大家的帮助')


bullet(
    """
Ensure that we have accurate character metrics for all encodings in 
horizontal and vertical writing."""
)
cn_disc('确保我们在横写和竖写中的所有编码都有准确的字符指标。')


bullet(
    """
Add options to ^UnicodeCIDFont^ to allow vertical and proportional variants 
where the font permits it."""
)
cn_bullet('为^UnicodeCIDFont^添加选项，在字体允许的情况下，允许垂直和比例变体。')


bullet(
    """
Improve the word wrapping code in paragraphs and allow vertical writing."""
)
cn_bullet('改进段落中的包字代码，允许竖写。')


CPage(5)
# heading2("RenderPM tests")
cn_heading2('RenderPM 测试')


disc(
    """This may also be the best place to mention the test function of 
$reportlab/graphics/renderPM.py$, which can be considered the cannonical 
place for tests which exercise renderPM (the "PixMap Renderer",
as opposed to renderPDF, renderPS or renderSVG)."""
)
cn_disc('这可能也是提及$reportlab/graphics/renderPM.py$的测试函数的最好地方，'
        '它可以被认为是行使renderPM'
        '("PixMap Renderer"，相对于renderPDF、renderPS或renderSVG)的测试的规范地方。')

disc(
    """If you run this from the command line, you should see lots of output 
    like the following."""
)
cn_disc('如果你从命令行运行这个，你应该会看到很多像下面这样的输出。')


eg(
    """C:\\code\\reportlab\\graphics>renderPM.py
wrote pmout\\renderPM0.gif
wrote pmout\\renderPM0.tif
wrote pmout\\renderPM0.png
wrote pmout\\renderPM0.jpg
wrote pmout\\renderPM0.pct
...
wrote pmout\\renderPM12.gif
wrote pmout\\renderPM12.tif
wrote pmout\\renderPM12.png
wrote pmout\\renderPM12.jpg
wrote pmout\\renderPM12.pct
wrote pmout\\index.html"""
)

disc(
    """This runs a number of tests progressing from a "Hello World" test, 
through various tests of Lines; text strings in a number of sizes, fonts, 
colour and alignments; the basic shapes; translated and rotated groups; 
scaled coordinates; rotated strings; nested groups; anchoring and non-standard fonts."""
)
cn_disc('它运行了许多测试，'
        '从 "Hello World"测试开始，到各种测试，'
        '包括：线条；各种尺寸、字体、颜色和对齐方式的文本字符串；'
        '基本形状；转换和旋转组；缩放坐标；'
        '旋转字符串；嵌套组；锚定和非标准字体。')


disc(
    """It creates a subdirectory called $pmout$, writes the image files into 
it, and writes an $index.html$ page which makes it easy to refer to all the 
results."""
)
cn_disc('它创建了一个名为$pmout$的子目录，将图片文件写入其中，并写了一个$index.html$的页面，便于参考所有结果。')


disc(
    """The font-related tests which you may wish to look at are test #11 (
    'Text strings in a non-standard font')
and test #12 ('Test Various Fonts')."""
)
cn_disc("与字体相关的测试，你可能会想看看#11（'非标准字体中的文本字符串'）和#12（'测试各种字体'）。")



##### FILL THEM IN
