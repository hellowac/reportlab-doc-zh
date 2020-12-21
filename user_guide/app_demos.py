# Copyright ReportLab Europe Ltd. 2000-2017
# see license.txt for license details
# history https://hg.reportlab.com/hg-public/reportlab/log/tip/docs/userguide/app_demos.py
from utils import (
    Appendix1,
    cn_Appendix1,
    disc,
    cn_disc,
    heading2,
    cn_heading2,
    eg,
)

# Appendix1("ReportLab Demos")
cn_Appendix1("ReportLab 示例")

disc(
    """In the subdirectories of $reportlab/demos$ there are a number of working examples showing
almost all aspects of reportlab in use."""
)
cn_disc("在$reportlab/demos$的子目录中，有许多工作实例，几乎展示了reportlab使用的所有方面。")

# heading2("""Odyssey""")
cn_heading2("奥德赛")

disc(
    """
The three scripts odyssey.py, dodyssey.py and fodyssey.py all take the file odyssey.txt
and produce PDF documents. The included odyssey.txt is short; a longer and more testing version
can be found at ftp://ftp.reportlab.com/odyssey.full.zip.
"""
)
cn_disc("odyssey.py、dodyssey.py和fodyssey.py这三个脚本都是取文件oddyssey.txt并生成PDF文档。"
        "包含的 odyssey.txt 很短；"
        "更长和更多的测试版本可以在 ftp://ftp.reportlab.com/odyssey.full.zip 找到。")

eg(
    """
Windows
cd reportlab\\demos\\odyssey
python odyssey.py
start odyssey.pdf

Linux
cd reportlab/demos/odyssey
python odyssey.py
acrord odyssey.pdf
"""
)

disc(
    """Simple formatting is shown by the odyssey.py script. It runs quite fast,
but all it does is gather the text and force it onto the canvas pages. It does no paragraph
manipulation at all so you get to see the XML &lt; &amp; &gt; tags.
"""
)
cn_disc("odyssey.py脚本显示了简单的格式化。"
        "它的运行速度相当快，但它所做的只是收集文本并将其强行放到画布页面上。"
        "它完全不进行段落操作，所以你可以看到XML &lt; &amp; &gt; 标签。")

disc(
    """The scripts fodyssey.py and dodyssey.py handle paragraph formatting so you get
to see colour changes etc. Both scripts
use the document template class and the dodyssey.py script shows the ability to do dual column
layout and uses multiple page templates.
"""
)
cn_disc("脚本fodyssey.py和dodyssey.py处理段落格式，"
        "所以你可以看到颜色变化等。"
        "这两个脚本都使用了文档模板类，dodyssey.py脚本显示了做双列布局的能力，并使用了多个页面模板。")


heading2("""Standard Fonts and Colors""")
cn_heading2("标准字体和颜色")

disc(
    """In $reportlab/demos/stdfonts$ the script stdfonts.py can be used to illustrate
ReportLab's standard fonts. Run the script using"""
)
cn_disc("在$reportlab/demos/stdfonts$中，"
        "脚本stdfonts.py可以用来说明ReportLab的标准字体。"
        "使用以下方法运行该脚本")

eg(
    """
cd reportlab\\demos\\stdfonts
python stdfonts.py
"""
)
disc(
    """
to produce two PDF documents, StandardFonts_MacRoman.pdf &amp;
StandardFonts_WinAnsi.pdf which show the two most common built in
font encodings.
"""
)
cn_disc("生成两个PDF文档，StandardFonts_MacRoman.pdf &amp; StandardFonts_WinAnsi.pdf，"
        "其中显示了两种最常见的内置字体编码。")

disc(
    """The colortest.py script in $reportlab/demos/colors$ demonstrates the different ways in which
reportlab can set up and use colors."""
)
cn_disc("在$reportlab/demos/colors$中的colortest.py脚本展示了reportlab设置和使用颜色的不同方式。")

disc(
    """Try running the script and viewing the output document, colortest.pdf. This shows
different color spaces and a large selection of the colors which are named
in the $reportlab.lib.colors$ module.
"""
)
cn_disc("试着运行该脚本并查看输出文档，colortest.pdf。"
        "这显示了不同的颜色空间和大量在$reportlab.lib.cols$模块中命名的颜色选择。")

# heading2("""Py2pdf""")
cn_heading2("Py2pdf")

disc(
    """Dinu Gherman contributed this useful script
which uses reportlab to produce nicely colorized PDF documents from Python
scripts including bookmarks for classes, methods and functions.
To get a nice version of the main script try"""
)
cn_disc("Dinu Gherman贡献了这个有用的脚本，"
        "它使用reportlab从Python脚本中生成漂亮的彩色PDF文档，包括类、方法和函数的书签。"
        "要得到一个漂亮的主脚本版本，可以尝试一下")


eg(
    """
cd reportlab/demos/py2pdf
python py2pdf.py py2pdf.py
acrord py2pdf.pdf
"""
)
disc(
    """i.e. we used py2pdf to produce a nice version of py2pdf.py in
the document with the same rootname and a .pdf extension.
"""
)
cn_disc("即我们使用py2pdf在文档中生成一个漂亮的py2pdf.py版本，根名相同，扩展名为.pdf。")


disc(
    """
The py2pdf.py script has many options which are beyond the scope of this
simple introduction; consult the comments at the start of the script.
"""
)
cn_disc("py2pdf.py脚本有很多选项，这些选项超出了这个简单介绍的范围，请参考脚本开头的注释。")

heading2("Gadflypaper")
# cn_heading2("Gadflypaper")

disc(
    """
The Python script, gfe.py, in $reportlab/demos/gadflypaper$ uses an inline style of
document preparation. The script almost entirely produced by Aaron Watters produces a document
describing Aaron's $gadfly$ in memory database for Python. To generate the document use
"""
)
cn_disc("$reportlab/demos/gadflypaper$中的Python脚本gfe.py使用了内联式的文档编制方式。"
        "这个脚本几乎完全由Aaron Watters制作，"
        "产生了一个描述Aaron的$gadfly$内存数据库的Python文档。"
        "要生成该文档，请使用")

eg(
    """
cd reportlab\\gadflypaper
python gfe.py
start gfe.pdf
"""
)

disc(
    """
everything in the PDF document was produced by the script which is why this is an inline style
of document production. So, to produce a header followed by some text the script uses functions
$header$ and $p$ which take some text and append to a global story list.
"""
)
cn_disc("PDF文档中的所有内容都是由脚本制作的，这就是为什么这是一种内联式文档制作方式。"
        "所以，为了生成一个标题，后面跟着一些文本，脚本使用了函数$header$和$p$，"
        "这两个函数接收一些文本并附加到一个全局故事列表中。")

eg(
    '''
header("Conclusion")

p("""The revamped query engine design in Gadfly 2 supports
..........
and integration.""")
'''
)
heading2("""Pythonpoint""")
# cn_heading2("""Pythonpoint""")

disc(
    """Andy Robinson has refined the pythonpoint.py script (in $reportlab\\demos\\pythonpoint$)
until it is a really useful script. It takes an input file containing an XML markup
and uses an xmllib style parser to map the tags into PDF slides. When run in its own directory
pythonpoint.py takes as a default input the file pythonpoint.xml and produces pythonpoint.pdf
which is documentation for Pythonpoint! You can also see it in action with an older paper
"""
)
cn_disc("Andy Robinson改进了pythonpoint.py脚本("
        "在$reportlab\\demos\\pythonpoint$中)，直到它成为一个真正有用的脚本。"
        "它接收一个包含XML标记的输入文件，并使用一个xmllib样式分析器将标记映射到PDF幻灯片中。"
        "当在它自己的目录下运行时，pythonpoint.py "
        "将文件 pythonpoint.xml 作为默认输入，并生成 pythonpoint.pdf，"
        "这是 Pythonpoint 的文档。您也可以通过一篇较早的文章看到它的运行情况。")

eg(
    """
cd reportlab\\demos\\pythonpoint
python pythonpoint.py monterey.xml
start monterey.pdf
"""
)

disc(
    """
Not only is pythonpoint self documenting, but it also demonstrates reportlab and PDF. It uses
many features of reportlab (document templates, tables etc).
Exotic features of PDF such as fadeins and bookmarks are also shown to good effect. The use of
an XML document can be contrasted with the <i>inline</i> style of the gadflypaper demo; the
content is completely separate from the formatting
"""
)
cn_disc("pythonpoint不仅是自文档，而且还演示了reportlab和PDF。"
        "它使用了reportlab的许多功能（文档模板、表格等）。"
        "PDF的奇特功能，如淡入和书签也被展示得很好。"
        "XML文档的使用可以与gadflypaper演示中的<i>inline</i>风格形成对比；"
        "内容与格式完全分离。")

