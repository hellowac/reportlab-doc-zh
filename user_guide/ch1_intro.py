# Copyright ReportLab Europe Ltd. 2000-2017
# see license.txt for license details
__version__ = '$Id$'

from utils import (
    title,
    cn_title,
    centred,
    cn_centred,
    nextTemplate,
    headingTOC,
    cn_headingTOC,
    getStory,
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
    bullet,
    cn_bullet,
    todo,
    cn_todo,
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import ParagraphStyle
import reportlab
from reportlab.lib.utils import TimeStamp

from utils.table_of_contents import CnTableOfContents


title("ReportLab PDF Library")
cn_title("用户手册")

centred('ReportLab Version ' + reportlab.Version)
cn_centred('版本 ' + reportlab.Version)

centred(
    TimeStamp().datetime.strftime('Document generated on %Y/%m/%d %H:%M:%S %Z')
)
cn_centred(TimeStamp().datetime.strftime('文档生成自 $%Y/%m/%d %H:%M:%S %Z$'))

nextTemplate("TOC")

# headingTOC('Table of contents')
cn_headingTOC('目录')

toc = TableOfContents()
PS = ParagraphStyle
toc.levelStyles = [
    PS(
        name='CnTOCHeading1',
        fontName='Times-Bold',
        fontSize=14,
        leftIndent=20,
        firstLineIndent=-20,
        spaceBefore=5,
        leading=16,
    ),
    PS(
        name='CnTOCHeading2',
        fontName='Times-Bold',
        fontSize=12,
        leftIndent=40,
        firstLineIndent=-20,
        spaceBefore=0,
        leading=12,
    ),
    PS(
        name='CnTOCHeading3',
        fontName='Times-Bold',
        fontSize=10,
        leftIndent=60,
        firstLineIndent=-20,
        spaceBefore=0,
        leading=12,
    ),
    PS(
        name='CnTOCHeading4',
        fontName='Times-Bold',
        fontSize=10,
        leftIndent=100,
        firstLineIndent=-20,
        spaceBefore=0,
        leading=12,
    ),
]
# getStory().append(toc)


cn_toc = CnTableOfContents()
PS = ParagraphStyle
cn_toc.levelStyles= [
    PS(
        fontName='STSong-Light',
        fontSize=14,
        name='TOCHeading1',
        leftIndent=20,
        firstLineIndent=-20,
        spaceBefore=5,
        leading=16,
    ),
    PS(
        fontName='STSong-Light',
        fontSize=12,
        name='TOCHeading2',
        leftIndent=40,
        firstLineIndent=-20,
        spaceBefore=0,
        leading=12,
    ),
    PS(
        fontName='STSong-Light',
        fontSize=10,
        name='TOCHeading3',
        leftIndent=60,
        firstLineIndent=-20,
        spaceBefore=0,
        leading=12,
    ),
    PS(
        fontName='STSong-Light',
        fontSize=10,
        name='TOCHeading4',
        leftIndent=100,
        firstLineIndent=-20,
        spaceBefore=0,
        leading=12,
    ),
]
getStory().append(cn_toc)


nextTemplate("Normal")

########################################################################
#
#               Chapter 1
#
########################################################################


# heading1("Introduction")
cn_heading1("介绍")

# heading2("About this document")
cn_heading2("关于")
disc(
    """This document is an introduction to the ReportLab PDF library.
Some previous programming experience
is presumed and familiarity with the Python Programming language is
recommended.  If you are new to Python, we tell you in the next section
where to go for orientation.
"""
)
cn_disc(
    """本文档是 ReportLab PDF 库的简介。阅读本文档我们已经假定您熟悉Python编程语言是。 
如果您是 Python 编程的新手，我们将在下一小节告诉您该去哪儿学习 Python 编程。
"""
)

disc(
    """
This manual does not cover 100% of the features, but should explain all
the main concepts and help you get started, and point you at other
learning resources.
After working your way through this, you should be ready to begin
writing programs to produce sophisticated reports.
"""
)
cn_disc(
    """本文档并未覆盖百分之百的功能，但应该能解释所有概念和帮助您入门，并指出其他学习资源。
阅读完本文档后，您应该准备好可以开始编程以生成复杂的PDF报告。
"""
)

disc("""In this chapter, we will cover the groundwork:""")
cn_disc("""在本章, 我们将介绍基础:""")
bullet("What is ReportLab all about, and why should I use it?")
cn_bullet("什么是ReportLab, 为什么要使用它？")
bullet("What is Python?")
cn_bullet("什么是Python？")
bullet("How do I get everything set up and running?")
cn_bullet("我该做哪些准备以便开始？")

todo(
    """
We need your help to make sure this manual is complete and helpful.
Please send any feedback to our user mailing list,
which is signposted from <a href="http://www.reportlab.com/">www.reportlab
.com</a>.
"""
)
cn_todo("""
我们需要您的帮助以确保本手册完整且有用。请将任何反馈发送到我们的用户邮件列表，
请参考:<a href="http://www.reportlab.com/">www.reportlab.com</a>。
""")

# heading2("What is the ReportLab PDF Library?")
cn_heading2("什么是 ReportLab PDF Library?")
disc(
    """This is a software library that lets you directly
create documents in Adobe's Portable Document Format (PDF) using
the Python programming language.   It also creates charts and data graphics
in various bitmap and vector formats as well as PDF."""
)
cn_disc(
    """这是一个软件库，可让您直接使用Python编程语言创建Adobe的可移植文档格式(Portable Document Format)（PDF）文档。 
它同样支持创建图表和数据图形各种位图和矢量格式，这就是PDF。"""
)

disc(
    """PDF is the global standard for electronic documents. It
supports high-quality printing yet is totally portable across
platforms, thanks to the freely available Acrobat Reader.  Any
application which previously generated hard copy reports or driving a printer
can benefit from making PDF documents instead; these can be archived,
emailed, placed on the web, or printed out the old-fashioned way.
However, the PDF file format is a complex
indexed binary format which is impossible to type directly.
The PDF format specification is more than 600 pages long and
PDF files must provide precise byte offsets -- a single extra
character placed anywhere in a valid PDF document can render it
invalid.  This makes it harder to generate than HTML."""
)
cn_disc("""PDF是电子文档的全球标准。 它支持高质量打印并且完全跨平台支持，这要归功于免费提供的 Acrobat Reader。 任何
先前生成纸质报告或驱动打印机的应用程序可以从制作PDF文档中受益； 
这些都可以存档通过电子邮件发送，放在网络上或以老式方式打印出来。
但是，PDF文件格式很复杂索引二进制格式，无法直接键入。
PDF格式规范的长度超过600页，PDF文件必须提供精确的字节偏移量-额外增加一个放置在有效PDF文档中任何位置的字符都可以呈现它无效。 
这使得它比HTML难生成。
""")

disc(
    """Most of the world's PDF documents have been produced
by Adobe's Acrobat tools, or rivals such as JAWS PDF Creator, which act
as 'print drivers'.  Anyone wanting to automate PDF production would
typically use a product like Quark, Word or Framemaker running in a loop
with macros or plugins, connected to Acrobat. Pipelines of several
languages and products can be slow and somewhat unwieldy.
"""
)
cn_disc("""世界上大多数PDF文档都是由Adobe的Acrobat工具 或 JAWS PDF Creator等竞争对手产生的，这些工具充当“打印驱动程序”。 
任何想要自动化PDF制作的人通常都会使用Quark，Word或Framemaker之类的产品，该产品与宏或插件循环连接到Acrobat，并在其中循环运行。 
几种语言和产品的管道传输速度可能很慢，而且有些笨拙。
""")

disc(
    """The ReportLab library directly creates PDF based on
your graphics commands.  There are no intervening steps.  Your applications
can generate reports extremely fast - sometimes orders
of magnitude faster than traditional report-writing
tools.   This approach is shared by several other libraries - PDFlib for C,
iText for Java, iTextSharp for .NET and others.  However, The ReportLab library
differs in that it can work at much higher levels, with a full featured engine
for laying out documents complete with tables and charts.  """
)
cn_disc("""ReportLab库根据您的图形命令直接创建PDF。 没有干预步骤。 
您的应用程序可以非常快速地生成报告-有时比传统的报告编写工具快几个数量级。 
此方法由其他几个库共享-C的PDFlib，Java的iText，.NET的iTextSharp等。 
但是，ReportLab库的不同之处在于它可以在更高的层次上运行，并具有一个功能齐全的引擎，用于布局包含表格和图表的文档。
""")


disc(
    """In addition, because you are writing a program
in a powerful general purpose language, there are no
restrictions at all on where you get your data from,
how you transform it, and the kind of output
you can create.  And you can reuse code across
whole families of reports."""
)
cn_disc("""此外，由于您正在使用功能强大的通用语言编写程序，因此从何处获取数据，如何转换数据以及输出的类型都没有任何限制。
您可以创建。 您可以在整个报表系列中重用代码。
""")

disc(
    """The ReportLab library is expected to be useful
in at least the following contexts:"""
)
cn_disc("""预期ReportLab库至少在以下情况下有用：""")
bullet("Dynamic PDF generation on the web")

cn_bullet("网络上动态生成PDF.")
bullet("High-volume corporate reporting and database publishing")
cn_bullet("大批量公司报告和数据库发布.")

bullet(
    """An embeddable print engine for other applications, including
a 'report language' so that users can customize their own reports. <i>
This is particularly relevant to cross-platform apps which cannot
rely on a consistent printing or previewing API on each operating
system</i>."""
)
cn_bullet("""用于其他应用程序的可嵌入打印引擎，包括“报告语言”，以便用户可以自定义自己的报告。 
<i>这尤其适用于跨平台应用程序，这些应用程序不能依赖每个操作系统上一致的打印或预览API。</i>
""")

bullet(
    """A 'build system' for complex documents with charts, tables
and text such as management accounts, statistical reports and
scientific papers """
)
cn_bullet("""具有图表，表格的复杂文档的“构建系统” 和文字，例如管理帐户，统计报告和 科学论文""")

bullet("""Going from XML to PDF in one step""")
cn_bullet("""从XML到PDF的一步""")

heading2("ReportLab's commercial software")
cn_heading2("ReportLab的商业软件")

disc(
    """
The ReportLab library forms the foundation of our commercial solution for
PDF generation, Report Markup Language (RML).  This is available for evaluation
on our web site with full documentation.   We believe that RML is the fastest
and easiest way to develop rich PDF workflows.  You work in a markup language
at a similar level to HTML, using your favorite templating system to populate
an RML document; then call our rml2pdf API function to generate a PDF.  It's
what ReportLab staff use to build all of the solutions you can see on 
reportlab.com.
Key differences:
"""
)
cn_disc("""ReportLab库构成了我们用于生成PDF的商业解决方案（报告标记语言（RML））的基础。 
可以在我们的网站上通过完整的文档进行评估。 我们相信RML是开发丰富的PDF工作流程的最快，最简单的方法。 
您可以使用最喜欢的模板系统来填充RML文档，并使用与HTML类似的标记语言。 
然后调用我们的rml2pdf API函数以生成PDF。 这就是ReportLab员工用来构建您可以在 reportlab.com 上面看到的所有解决方案的东西。
主要区别：
""")

bullet(
    """Fully documented with two manuals, a formal specification (the DTD) 
    and extensive self-documenting tests.  (By contrast, we try to make sure 
    the open source documentation isn't wrong, but we don't always keep up 
    with the code)"""
)
cn_bullet("""完整记录了两本手册，一份正式规范（DTD）和大量的自记录测试。 （通过对比，我们尝试确保开源文档没有错，但是我们并不总是跟上代码）""")

bullet(
    """Work in high-level markup rather than constructing graphs of Python 
    objects """
)
cn_bullet("""在高级标记中工作，而不是构造Python对象图""")

bullet(
    """Requires no Python expertise - your colleagues may thank you after 
    you've left!'"""
)
cn_bullet("""不需要Python专业知识-您离开后，您的同事可能会感谢您！”""")

bullet("""Support for vector graphics and inclusion of other PDF documents""")
cn_bullet("""支持矢量图形并包含其他PDF文档""")

bullet(
    """Many more useful features expressed with a single tag, which would 
    need a lot
of coding in the open source package"""
)
cn_bullet("""用单个标签表示的更多有用功能，这将需要在开源软件包中进行大量编码""")

bullet("""Commercial support is included""")
cn_bullet("""包括商业支持""")


disc(
    """
We ask open source developers to consider trying out RML where it is 
appropriate.
You can register on our site and try out a copy before buying.
The costs are reasonable and linked to the volume of the project, and the 
revenue
helps us spend more time developing this software."""
)
cn_disc("""我们要求开源开发人员考虑在适当的地方尝试RML。 
您可以在我们的网站上注册并尝试购买之前的副本。 
成本是合理的，并且与项目的规模有关，而收入则帮助我们花费更多的时间来开发此软件。
""")

heading2("What is Python?")
cn_heading2("什么是 Python?")

disc(
    """
Python is an <i>interpreted, interactive, object-oriented</i> programming 
language. It is often compared to Tcl, Perl,
Scheme or Java.""")
cn_disc("""Python是一种<i>解释型，交互式，面向对象的</i>编程语言。 通常将它与Tcl，Perl Scheme或Java进行比较。""")

disc(
    """
Python combines remarkable power with very clear syntax. It has modules, 
classes, exceptions, very high level
dynamic data types, and dynamic typing. There are interfaces to many system 
calls and libraries, as well as to
various windowing systems (X11, Motif, Tk, Mac, MFC). New built-in modules 
are easily written in C or C++.
Python is also usable as an extension language for applications that need a 
programmable interface.
"""
)
cn_disc("""Python将非凡的功能与非常清晰的语法结合在一起。 
它具有模块，类，异常，非常高级的动态数据类型和动态类型。 
有许多系统调用和库以及各种窗口系统（X11，Motif，Tk，Mac，MFC）的接口。 
新的内置模块很容易用C或C ++编写。
Python还可用作需要可编程接口的应用程序的扩展语言。""")

disc(
    """
Python is as old as Java and has been growing steadily in popularity for 
years; since our
library first came out it has entered the mainstream.  Many ReportLab library 
users are
already Python devotees, but if you are not, we feel that the language is an 
excellent
choice for document-generation apps because of its expressiveness and ability 
to get
data from anywhere.
"""
)
cn_disc("""Python与Java一样古老，并且多年来一直稳步增长。 
自从我们的ReportLab包首次问世以来，它已经成为主流。 
许多ReportLab库用户已经是Python的忠实拥护者，但如果您不是Python的忠实拥护者，
我们认为该语言是文档生成应用程序的绝佳选择，因为它的表达能力和从任何地方获取数据的能力。""")

disc(
    """
Python is copyrighted but <b>freely usable and distributable, even for 
commercial use</b>.
"""
)
cn_disc("""Python受版权保护，但<b>可自由使用和分发，甚至用于商业用途</ b>。""")

# heading2("Acknowledgements")
cn_heading2("""致谢""")

disc(
    """Many people have contributed to ReportLab.  We would like to thank in 
    particular (in alphabetical order): """)
cn_disc("""许多人为ReportLab做出了贡献。 我们要特别感谢（按字母顺序）：""")

disc("""
<nobr>Albertas Agejevas, 
Alex Buck, 
Andre Reitz, 
Andrew Cutler,
Andrew Mercer, 
Ben Echols,
Benjamin Dumke,
Benn B,
Chad Miller, 
Chris Buergi,
Chris Lee, 
Christian Jacobs, 
Dinu Gherman,
Edward Greve,
Eric Johnson,
Felix Labrecque,  
Fubu @ bitbucket,
Gary Poster, 
Germán M. Bravo,
Guillaume Francois, 
Hans Brand,
Henning Vonbargen,
Hosam Aly,
Ian Stevens, 
James Martin-Collar, 
Jeff Bauer,
Jerome Alet,
Jerry Casiano,
Jorge Godoy,
Keven D Smith,
Kyle MacFarlane,
Magnus Lie Hetland,
Marcel Tromp, 
Marius Gedminas,
Mark de Wit,
Matthew Duggan,
Matthias Kirst,
Matthias Klose,
Max M, 
Michael Egorov,
Michael Spector,
Mike Folwell,
Mirko Dziadzka,
Moshe Wagner,
Nate Silva,
Paul McNett, 
Peter Johnson, 
PJACock,
Publio da Costa Melo,  
Randolph Bentson,
Robert Alsina,
Robert Hölzl,
Robert Kern,
Ron Peleg,
Ruby Yocum,
Simon King,
Stephan Richter,
Steve Halasz, 
Stoneleaf @ bitbucket,
T Blatter,
Tim Roberts,
Tomasz Swiderski,
Ty Sarna,
Volker Haas,
Yoann Roman,</nobr>
and many more."""
)

disc(
    """Special thanks go to Just van Rossum for his valuable assistance with
font technicalities."""
)
cn_disc("""特别感谢Just van Rossum在字体技术方面的宝贵帮助。""")

disc(
    """Moshe Wagner and Hosam Aly deserve a huge thanks for contributing to 
    the RTL patch, which is not yet on the trunk."""
)
cn_disc("""Moshe Wagner和Hosam Aly为RTL补丁做出了巨大的贡献，该补丁尚未发布。""")


disc(
    """Marius Gedminas deserves a big hand for contributing the work on 
    TrueType fonts and we
are glad to include these in the toolkit. Finally we thank Michal Kosmulski 
for the DarkGarden font
for and Bitstream Inc. for the Vera fonts."""
)
cn_disc("""Marius Gedminas在TrueType字体方面的工作值得一臂之力，我们很高兴将其包含在工具包中。 
最后，我们感谢Michal Kosmulski的DarkGarden字体和Bitstream Inc.的Vera字体。""")


# heading2("Installation and Setup")
cn_heading2("安装与设定")

disc(
    """To avoid duplication, the installation instructions are kept in the 
    README file
in our distribution, which can be viewed online at 
^https://hg.reportlab.com/hg-public/reportlab/^"""
)
cn_disc("""为避免重复，安装说明保存在我们发行版的README文件中，可以在以下位置在线查看。
^https://hg.reportlab.com/hg-public/reportlab/^ """)


disc(
    """This release (%s) of ReportLab requires Python versions 2.7, %s.%s+ or 
    higher.  
	If you need to use Python 2.5 or 2.6, please use the latest ReportLab 2.7 
	package.
"""
    % ((reportlab.Version,) + reportlab.__min_python_version__)
)
cn_disc("""此版本（{}）的ReportLab需要Python版本2.7，{}.{} +或更高版本。 
如果您需要使用Python 2.5或2.6，请使用最新的ReportLab 2.7软件包。
""".format(reportlab.Version, *reportlab.__min_python_version__))


# heading2("Getting Involved")
cn_heading2("开始")
disc(
    """ReportLab is an Open Source project.  Although we are
a commercial company we provide the core PDF generation
sources freely, even for commercial purposes, and we make no income directly
from these modules.  We also welcome help from the community
as much as any other Open Source project.  There are many
ways in which you can help:"""
)
cn_disc("""ReportLab是一个开源项目。 
尽管我们是一家商业公司，但我们免费提供核心PDF生成源，即使出于商业目的，我们也不会直接从这些模块中获得收入。 
我们也欢迎社区以及其他任何开源项目的帮助。 您可以通过多种方式提供帮助：
""")


bullet(
    """General feedback on the core API. Does it work for you?
Are there any rough edges?  Does anything feel clunky and awkward?"""
)
cn_bullet("""有关核心API的一般反馈。 对你起作用吗？
有粗糙的边缘吗？ 有什么感觉笨拙而笨拙的吗？""")


bullet(
    """New objects to put in reports, or useful utilities for the library.
We have an open standard for report objects, so if you have written a nice
chart or table class, why not contribute it?"""
)
cn_bullet("""放入报告的新对象，或库的有用工具。
我们有一个针对报表对象的开放标准，因此，如果您编写了不错的图表或表类，为什么不贡献它呢？""")


bullet(
    """Snippets and Case Studies: If you have produced some nice
output, register online on ^http://www.reportlab.com^ and submit a snippet
of your output (with or without scripts).  If ReportLab solved a
problem for you at work, write a little 'case study' and submit it.
And if your web site uses our tools to make reports, let us link to it.
We will be happy to display your work (and credit it with your name
and company) on our site!"""
)
cn_bullet("""片段和案例研究：如果您产生了不错的输出，请在^http://www.reportlab.com^上在线注册并提交输出片段（带或不带脚本）。 
如果ReportLab为您解决了工作中的问题，请编写一些“案例研究”并提交。 
如果您的网站使用我们的工具制作报告，请让我们链接到它。
我们很乐意在我们的网站上显示您的作品（并用您的名字和公司来称赞）！""")


bullet(
    """Working on the core code:  we have a long list of things
to refine or to implement.  If you are missing some features or
just want to help out, let us know!"""
)
cn_bullet("""处理核心代码：我们有一长串需要完善或实现的事情。 如果您缺少某些功能或只是想提供帮助，请告诉我们！""")


disc(
    """The first step for anyone wanting to learn more or
get involved is to join the mailing list.  To Subscribe visit
$http://two.pairlist.net/mailman/listinfo/reportlab-users$.
From there you can also browse through the group's archives
and contributions.  The mailing list is
the place to report bugs and get support. """
)
cn_bullet("""想要了解更多信息或参与其中的任何人的第一步是加入邮件列表。 
要订阅，请访问 $http://two.pairlist.net/mailman/listinfo/reportlab-users$。 
您还可以从那里浏览小组的档案和贡献。 邮件列表是报告错误并获得支持的地方。""")


disc(
    """The code now lives on our website (
    $http://hg.reportlab.com/hg-public/reportlab/$)
in a Mercurial repository, along with an issue tracker and wiki.  Everyone 
should
feel free to contribute, but if you are working actively on some improvements
or want to draw attention to an issue, please use the mailing list to let us 
know."""
)
cn_bullet("""他的代码现在位于Mercurial信息库中的我们网站
（$http://hg.reportlab.com/hg-public/reportlab/$）上，以及问题跟踪器和Wiki。 
每个人都可以随时做出贡献，但是如果您正在积极地进行一些改进，或者想引起人们对问题的关注，请使用邮件列表告知我们。
""")


# heading2("Site Configuration")
cn_heading2("全局配置")

disc(
    """There are a number of options which most likely need to be configured 
    globally for a site.
The python script module $reportlab/rl_config.py$ aggregates the various 
settings files. You may want inspect the file $reportlab/rl_settings.py$ which
contains defaults for the currently used variables. There are several 
overrides for $rl_settings$
modules $reportlab.local_rl_settings$, $reportlab_settings$ (a script file 
anywhere on the python path)
and finally the file $~/.reportlab_settings$ (note no .py). Temporary changes 
can be made using evironment variables which
are the variables from $rl_settings.py$ prefixed with $RL_$ eg $RL_verbose=1$.
"""
)
cn_disc("""有许多选项很可能需要为程序进行全局配置。 
python脚本模块$reportlab/rl_config.py$汇总了各种设置文件。 
您可能需要检查文件$reportlab/rl_settings.py$，其中包含当前使用的变量的默认值。 
$rl_settings$模块$reportlab.local_rl_settings$，
$reportlab_settings$（位于python路径上任何位置的脚本文件）以及文件$~/.reportlab_settings$
（请注意，没有.py）有多个替代项。
可以进行临时更改。 
使用环境变量，这些变量是$rl_settings.py$中以$RL_$开头的变量，例如$RL_verbose=1$。
""")

# heading3("Useful rl_config variables")
cn_heading3("有用的rl_config变量")

bullet("""verbose: set to integer values to control diagnostic output.""")
cn_bullet("""verbose: 设置为整数值以控制诊断输出。""")

bullet(
    """shapeChecking: set this to zero to turn off a lot of error checking in 
    the graphics modules"""
)
cn_bullet("""shapeChecking: 将此设置为零可关闭图形模块中的许多错误检查""")

bullet("""defaultEncoding: set this to WinAnsiEncoding or MacRomanEncoding.""")
cn_bullet("""defaultEncoding: 将此设置为WinAnsiEncoding或MacRomanEncoding。""")

bullet(
    """defaultPageSize: set this to one of the values defined in 
    reportlab/lib/pagesizes.py; as delivered
it is set to pagesizes.A4; other values are pagesizes.letter etc."""
)
cn_bullet("""defaultPageSize：将其设置为reportlab/lib/pagesizes.py中定义的值之一；
 交付时将其设置为pagesizes.A4; 其他值是pagesizes.letter等。""")

bullet(
    """defaultImageCaching: set to zero to inhibit the creation of .a85 files on your hard-drive. The default is to create these preprocessed PDF compatible image files for faster loading"""
)
cn_bullet("""defaultImageCaching：设置为零以禁止在硬盘驱动器上创建.a85文件。 默认设置是创建这些经过预处理的PDF兼容图像文件，以加快加载速度""")

bullet(
    """T1SearchPath: this is a python list of strings representing directories that may be queried for information on Type 1 fonts"""
)
cn_bullet("""T1SearchPath：这是表示目录的字符串的python列表，可以查询有关类型1字体的信息
""")

bullet(
    """TTFSearchPath: this is a python list of strings representing 
    directories that
may be queried for information on TrueType fonts"""
)
cn_bullet("""TTFSearchPath：这是表示目录的字符串的python列表，可以查询该目录以获取有关TrueType字体的信息""")

bullet(
    """CMapSearchPath: this is a python list of strings representing 
    directories that may be queried for information on font code maps."""
)
cn_bullet("""CMapSearchPath：这是表示目录的字符串的python列表，可以查询该目录以获取字体代码映射的信息。""")

bullet("""showBoundary: set to non-zero to get boundary lines drawn.""")
cn_bullet("""showBoundary：设置为非零以绘制边界线。""")

bullet(
    """ZLIB_WARNINGS: set to non-zero to get warnings if the Python 
    compression extension is not found."""
)
cn_bullet("""ZLIB_WARNINGS：如果未找到Python压缩扩展，则设置为非零以获得警告。""")

bullet("""pageCompression: set to non-zero to try and get compressed PDF.""")
cn_bullet("""pageCompression：设置为非零以尝试获取压缩的PDF。
""")

bullet(
    """allowtableBoundsErrors: set to 0 to force an error on very large 
    Platypus table elements"""
)
cn_bullet("""allowtableBoundsErrors：设置为0会在非常大的Platypus表元素上强制执行错误""")

bullet(
    """emptyTableAction: Controls behaviour for empty tables, can be 'error' 
    (default), 'indicate' or 'ignore'."""
)
cn_bullet("""emptyTableAction：控制空表的行为，可以为“error”（默认），“indicate”或“ignore”。
""")

bullet(
    """trustedHosts: if not $None$ a list of glob patterns of trusted hosts; 
    these may be used in places like &lt;img&gt; tags in paragraph texts."""
)
cn_bullet("""TrustedHosts：如果不是$None$，则列出受信任主机的全局模式；
这些可以在＆lt; img＆gt;之类的地方使用。 段落文字中的标签。""")

bullet(
    """trustedSchemes: a list of allowed $URL$ schemes used with 
    $trustedHosts$"""
)
cn_bullet("""trustedSchemes：与$trustedHosts$一起使用的允许的$URL$方案的列表
""")

disc(
    """For the full list of variables see the file $reportlab/rl_settings.py$."""
)
cn_bullet("""有关变量的完整列表，请参见文件$reportlab/rl_settings.py$。""")

# heading3("Other modifications")
cn_heading3("""其他修改""")

disc(
    """More complex modifications to the reportlab toolkit environment may be made using one of the modules $rep[ortlab.local_rl_mods$ (.py script in reportlab folder),
$reportlab_mods$ (.py file on the python path) or $~/.reportlab_mods$ (note no .py)."""
)
cn_disc("""可以使用以下模块之一对reportlab工具箱环境进行更复杂的修改：$rep[ortlab.local_rl_mods$（reportlab文件夹中的.py脚本），
$reportlab_mods$（python路径上的.py文件）或$~/.reportlab_mods$（注意是.py）。
""")


# heading2("Learning More About Python")
cn_heading2("了解有关Python的更多信息")

disc(
    """
If you are a total beginner to Python, you should check out one or more from the
growing number of resources on Python programming. The following are freely 
available on the web:
"""
)
cn_disc("""如果您是Python的初学者，则应该从越来越多的Python编程资源中检出一个或多个。 以下内容可从网上免费获得：""")


bullet(
    """<b>Python Documentation.  </b>
A list of documentation on the Python.org web site.
$http://www.python.org/doc/$
"""
)
cn_bullet("""<b>Python文档</b> 
Python.org网站上的文档列表。$http://www.python.org/doc/$ """)


bullet(
    """<b>Python Tutorial.</b>
The official Python Tutorial , originally written by Guido van Rossum himself.
$http://docs.python.org/tutorial/$
"""
)
cn_bullet("""<b>Python教程</b>
官方的Python教程，最初由Guido van Rossum亲自编写。
$http://docs.python.org/tutorial/$
""")


bullet(
    """<b>Learning to Program.  </b>
A tutorial on programming by Alan Gauld. Has a heavy emphasis on
Python, but also uses other languages.
$http://www.freenetpages.co.uk/hp/alan.gauld/$
"""
)
cn_bullet("""<b>学习编程</b>
Alan Gauld撰写的编程指南。 非常重视Python，但也使用其他语言。
$http://www.freenetpages.co.uk/hp/alan.gauld/$
""")


bullet(
    """<b>Instant Python</b>.
A 6-page minimal crash course by Magnus Lie Hetland.
$http://www.hetland.org/python/instant-python.php$
"""
)
cn_bullet("""<b>即时Python</b>
Magnus Lie Hetland撰写的长达6页的速成课程。
$http://www.hetland.org/python/instant-python.php$
""")


bullet(
    """<b>Dive Into Python</b>.
A free Python tutorial for experienced programmers.
$http://www.diveintopython.net/$
"""
)
cn_bullet("""<b>深入Python</b>
适用于经验丰富的程序员的免费Python教程。
$http://www.diveintopython.net/$
""")


from reportlab.lib.codecharts import SingleByteEncodingChart
from utils.stylesheet import getStyleSheet


styles = getStyleSheet()
indent0_style = styles['Indent0']
indent1_style = styles['Indent1']

# heading2("Goals for the 3.x release series")
cn_heading2("""3.x版本系列的目标""")

disc(
    """ReportLab 3.0 has been produced to help in the migration to Python     3.x.  Python 3.x will be standard in future Ubuntu releases and is gaining popularity, and a good proportion of major Python packages now run on Python 3.  """
)
cn_disc("""已生成ReportLab 3.0，以帮助迁移到Python3.x。 
Python 3.x将在将来的Ubuntu版本中成为标准配置，并且越来越受欢迎，并且现在有很大一部分主要的Python程序包都在Python 3上运行。
""")


bullet(
    """Python 3.x compatibility.  A single line of code should run on 2.7 and 3.6"""
)
cn_bullet("""Python 3.x兼容性。 一行代码应在2.7和3.6上运行""")

bullet(""" __init__.py restricts to 2.7 or >=3.6""")
cn_bullet("""__init__.py限制为2.7或> = 3.6""")

bullet(
    """__init__.py allow the import of on optional reportlab.local_rl_mods to allow monkey patching etc."""
)
cn_bullet("""__init__.py允许导入可选的reportlab.local_rl_mods，以允许猴子打补丁等。""")

bullet(
    """rl_config now imports rl_settings, optionally local_rl_settings, reportlab_settings.py & finally ~/.reportlab_settings"""
)
cn_bullet("""rl_config现在可以导入rl_settings，还可以导入local_rl_settings
，reportlab_settings.py，最后是 ~/.reportlab_settings
""")

bullet(
    """ReportLab C extensions now live inside reportlab; _rl_accel is no longer required. All _rl_accel imports now pass through reportlab.lib.rl_accel"""
)
cn_bullet("""ReportLab C扩展现在位于reportlab中。 不再需要_rl_accel。 现在，所有_rl_accel导入都通过reportlab.lib.rl_accel""")

bullet(
    """xmllib is gone, alongside the paraparser stuff that caused issues in favour of HTMLParser."""
)
cn_bullet("""xmllib以及用于引起HTMLParser问题的paraparser东西一去不复返了。""")

bullet("""some obsolete C extensions (sgmlop and pyHnj) are gone""")
cn_bullet("""一些过时的C扩展名（sgmlop和pyHnj）消失了""")

bullet(
    """Improved support for multi-threaded systems to the _rl_accel C 
    extension module."""
)
cn_bullet("""_rl_accel C扩展模块对多线程系统的改进支持。""")

bullet(
    """Removed reportlab/lib/para.py & pycanvas.py.  These would better belong in third party packages, which can make use of the monkeypatching feature above."""
)
cn_bullet("""删除了reportlab/lib/para.py和pycanvas.py。 这些最好属于第三方程序包，可以利用上面的Monkeypatching功能。""")

bullet(
    """Add ability to output greyscale and 1-bit PIL images without conversion to RGB. (contributed by Matthew Duggan)"""
)
cn_bullet("""增加了无需转换为RGB即可输出灰度和1位PIL图像的功能。 （由Matthew Duggan贡献）""")

bullet("""highlight annotation (contributed by Ben Echols)""")
cn_bullet("""高亮注释（由Ben Echols提供）""")

bullet("""full compliance with pip, easy_install, wheels etc""")
cn_bullet("""完全符合pip，easy_install，wheel等要求""")


disc(
    """Detailed release notes are available at 
$http://www.reportlab.com/software/documentation/relnotes/30/$"""
)
cn_disc("""有关详细的发行说明，请访问：$http://www.reportlab.com/software/documentation/relnotes/30/$
""")

