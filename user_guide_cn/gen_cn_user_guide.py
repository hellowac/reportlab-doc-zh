import os
import logging
from datetime import datetime

import reportlab
from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.codecharts import SingleByteEncodingChart
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.tables import Table, TableStyle
from reportlab.platypus.paraparser import (
    _addAttributeNames,
    _paraAttrMap,
    _bulletAttrMap,
)
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import widgetbase
from reportlab.platypus.flowables import Spacer, Image
from reportlab.lib.units import inch
from reportlab.graphics import testshapes
from reportlab.graphics.shapes import (
    Drawing,
    Line,
    PolyLine,
    String,
    Group,
    mmult,
    translate,
    rotate,
)
from reportlab.graphics.charts.piecharts import sample5, sample7, sample8

from components import constant
from core import doc_examples
from core.pdf import PDF


BASE_DIR = os.path.dirname(__file__)


def setup_logging():
    # Define the log format
    log_format = '%(filename)s %(funcName)s:%(lineno)s %(message)s'

    # Define basic configuration
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[logging.StreamHandler()],
    )


def chapter1_introduction(pdf):
    pdf.add_title('用户手册')
    pdf.add_centred(f'版本 {reportlab.Version}')
    pdf.add_centred(datetime.now().strftime('文档生成自 %Y/%m/%d %H:%M:%S %Z'))
    pdf.next_toc_template()
    pdf.add_toc()
    pdf.next_normal_template()
    pdf.add_heading('介绍', level=1)
    pdf.add_heading('关于', level=2)
    pdf.add_paragraph(
        '本文档是 ReportLab PDF 库的简介。阅读本文档我们已经假定您熟悉Python编程语言是。'
        '如果您是 Python 编程的新手，我们将在下一小节告诉您该去哪儿学习 Python 编程。'
    )
    pdf.add_paragraph(
        '本文档并未覆盖百分之百的功能，但应该能解释所有概念和帮助您入门，并指出其他学习资源。'
        '阅读完本文档后，您应该准备好可以开始编程以生成复杂的PDF报告。'
    )
    pdf.add_paragraph("在本章, 我们将介绍基础功能:")
    pdf.add_bullet("什么是ReportLab, 为什么要使用它？")
    pdf.add_bullet("什么是Python？")
    pdf.add_bullet("我该做哪些准备以便开始？")
    pdf.add_paragraph(
        "我们需要您的帮助以确保本手册完整且有用。请将任何反馈发送到我们的用户邮件列表，请参考:"
        "<a href=\"http://www.reportlab.com/\">www.reportlab.com</a>。"
    )

    pdf.add_heading('什么是 ReportLab PDF Library?', level=2)
    pdf.add_paragraph(
        "这是一个软件库，可让您直接使用Python编程语言创建Adobe的"
        "可移植文档格式(Portable Document Format)（PDF）文档。"
        "它同样支持创建图表和数据图形各种位图和矢量格式，这就是PDF。"
    )
    pdf.add_paragraph(
        "PDF是电子文档的全球标准。 它支持高质量打印并且完全跨平台支持，这要归功于免费提供的 Acrobat Reader。 "
        "任何先前生成纸质报告或驱动打印机的应用程序可以从制作PDF文档中受益；"
        "这些都可以存档通过电子邮件发送，放在网络上或以老式方式打印出来。"
        "但是，PDF文件格式很复杂索引二进制格式，无法直接键入。"
        "PDF格式规范的长度超过600页，PDF文件必须提供精确的字节偏移量"
        "-额外增加一个放置在有效PDF文档中任何位置的字符都可以呈现它无效。"
        "这使得它比HTML难生成。"
    )
    pdf.add_paragraph(
        "世界上大多数PDF文档都是由Adobe的Acrobat工具 或 JAWS PDF Creator等竞争对手产生的，"
        "这些工具充当“打印驱动程序”。任何想要自动化PDF制作的人通常都会使用Quark，Word或Framemaker之类的产品，"
        "该产品与宏或插件循环连接到Acrobat，并在其中循环运行。几种语言和产品的管道传输速度可能很慢，而且有些笨拙。"
    )
    pdf.add_paragraph(
        "ReportLab库根据您的图形命令直接创建PDF。 没有干预步骤。"
        "您的应用程序可以非常快速地生成报告-有时比传统的报告编写工具快几个数量级。"
        "此方法由其他几个库共享-C的PDFlib，Java的iText，.NET的iTextSharp等。"
        "但是，ReportLab库的不同之处在于它可以在更高的层次上运行，并具有一个功能齐全的引擎，用于布局包含表格和图表的文档。"
    )
    pdf.add_paragraph(
        "此外，由于您正在使用功能强大的通用语言编写程序，因此从何处获取数据，如何转换数据以及输出的类型都没有任何限制。"
        "您可以创建。 您可以在整个报表系列中重用代码。"
    )
    pdf.add_paragraph("预期ReportLab库至少在以下情况下有用：")
    pdf.add_bullet("网络上动态生成PDF.")
    pdf.add_bullet("大批量公司报告和数据库发布.")
    pdf.add_bullet(
        "用于其他应用程序的可嵌入打印引擎，包括“报告语言”，以便用户可以自定义自己的报告。"
        "<i>这尤其适用于跨平台应用程序，这些应用程序不能依赖每个操作系统上一致的打印或预览API。</i>"
    )
    pdf.add_bullet('具有图表，表格的复杂文档的“构建系统” 和文字，例如管理帐户，统计报告和科学论文')
    pdf.add_bullet('从XML到PDF的一步')

    pdf.add_heading("ReportLab的商业软件", level=2)
    pdf.add_paragraph(
        "ReportLab库构成了我们用于生成PDF的商业解决方案（报告标记语言（RML））的基础。"
        "可以在我们的网站上通过完整的文档进行评估。 我们相信RML是开发丰富的PDF工作流程的最快，最简单的方法。"
        "您可以使用最喜欢的模板系统来填充RML文档，并使用与HTML类似的标记语言。"
        "然后调用我们的rml2pdf API函数以生成PDF。 "
        "这就是ReportLab员工用来构建您可以在 reportlab.com 上面看到的所有解决方案的东西。"
        "主要区别："
    )
    pdf.add_bullet(
        "完整记录了两本手册，一份正式规范（DTD）和大量的自记录测试。 "
        "（通过对比，我们尝试确保开源文档没有错，但是我们并不总是和代码保持同步）"
    )
    pdf.add_bullet("在高级标记中工作，而不是构造Python对象图")
    pdf.add_bullet("不需要Python专业知识-您离开后，您的同事可能会感谢您！")
    pdf.add_bullet("支持矢量图形并包含其他PDF文档")
    pdf.add_bullet("用单个标签表示的更多有用功能，这将需要在开源软件包中进行大量编码")
    pdf.add_bullet("包括商业支持")
    pdf.add_paragraph(
        "我们要求开源开发人员考虑在适当的地方尝试RML。"
        "您可以在我们的网站上注册并尝试购买之前的副本。"
        "成本是合理的，并且与项目的规模有关，而收入则帮助我们花费更多的时间来开发此软件。"
    )

    pdf.add_heading("什么是 Python?", level=2)
    pdf.add_paragraph(
        "Python是一种<i>解释型，交互式，面向对象的</i>编程语言。 通常将它与Tcl，Perl Scheme或Java进行比较。"
    )
    pdf.add_paragraph(
        "Python将非凡的功能与非常清晰的语法结合在一起。 "
        "它具有模块，类，异常，非常高级的动态数据类型和动态类型。"
        "有许多系统调用和库以及各种窗口系统（X11，Motif，Tk，Mac，MFC）的接口。"
        "新的内置模块很容易用C或C ++编写。"
        "Python还可用作需要可编程接口的应用程序的扩展语言。"
    )
    pdf.add_paragraph(
        "Python与Java一样古老，并且多年来一直稳步增长。"
        "自从我们的ReportLab包首次问世以来，它已经成为主流。"
        "许多ReportLab库用户已经是Python的忠实拥护者，但如果您不是Python的忠实拥护者，"
        "我们认为该语言是文档生成应用程序的绝佳选择，因为它的表达能力和从任何地方获取数据的能力。"
    )

    pdf.add_paragraph("Python受版权保护，但<b>可自由使用和分发，甚至用于商业用途</ b>。")

    pdf.add_heading("致谢", level=2)
    pdf.add_paragraph("许多人为ReportLab做出了贡献。 我们要特别感谢（按字母顺序）：")
    pdf.add_paragraph(
        """
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
    pdf.add_paragraph("特别感谢Just van Rossum在字体技术方面的宝贵帮助。")
    pdf.add_paragraph("Moshe Wagner和Hosam Aly为RTL补丁做出了巨大的贡献，该补丁尚未发布。")
    pdf.add_paragraph(
        "Marius Gedminas在TrueType字体方面的工作值得一臂之力，我们很高兴将其包含在工具包中。"
        "最后，我们感谢Michal Kosmulski的DarkGarden字体和Bitstream Inc.的Vera字体。"
    )

    pdf.add_heading("安装与设定", level=2)
    pdf.add_paragraph(
        "为避免重复，安装说明保存在我们发行版的README文件中，可以在以下位置在线查看。"
        "<a href='https://hg.reportlab.com/hg-public/reportlab/'>"
        "https://hg.reportlab.com/hg-public/reportlab/</a> "
    )
    pdf.add_paragraph(
        "此版本（{}）的ReportLab需要Python版本2.7，{}.{} +或更高版本。 "
        "如果您需要使用Python 2.5或2.6，请使用最新的ReportLab 2.7软件包。".format(
            reportlab.Version, *reportlab.__min_python_version__
        )
    )

    pdf.add_heading("开始", level=2)
    pdf.add_paragraph(
        "ReportLab是一个开源项目。"
        "尽管我们是一家商业公司，但我们免费提供核心PDF生成源，即使出于商业目的，"
        "我们也不会直接从这些模块中获得收入。我们也欢迎社区以及其他任何开源项目的帮助。 "
        "您可以通过多种方式提供帮助："
    )
    pdf.add_bullet("有关核心API的一般反馈。 对你起作用吗？有粗糙的边缘吗？ 有什么感觉笨拙而笨拙的吗？")
    pdf.add_bullet(
        "放入报告的新对象，或库的有用工具。我们有一个针对报表对象的开放标准，因此，如果您编写了不错的图表或表类，为什么不贡献它呢？"
    )
    pdf.add_bullet(
        "片段和案例研究：如果您产生了不错的输出，"
        "请在<a href='http://www.reportlab.com'>http://www.reportlab.com</a>"
        "上在线注册并提交输出片段（带或不带脚本）。"
        "如果ReportLab为您解决了工作中的问题，请编写一些“案例研究”并提交。"
        "如果您的网站使用我们的工具制作报告，请让我们链接到它。"
        "我们很乐意在我们的网站上显示您的作品（并用您的名字和公司来称赞）！"
    )
    pdf.add_bullet("处理核心代码：我们有一长串需要完善或实现的事情。 如果您缺少某些功能或只是想提供帮助，请告诉我们！")

    pdf.add_paragraph(
        "想要了解更多信息或参与其中的任何人的第一步是加入邮件列表。"
        "要订阅，请访问 "
        "<a href='http://two.pairlist.net/mailman/listinfo/reportlab-users'>"
        "http://two.pairlist.net/mailman/listinfo/reportlab-users</a>。"
        "您还可以从那里浏览小组的档案和贡献。 邮件列表是报告错误并获得支持的地方。"
    )
    pdf.add_paragraph(
        "他的代码现在位于Mercurial信息库中的我们网站（"
        "<a href='http://hg.reportlab.com/hg-public/reportlab/'>"
        "http://hg.reportlab.com/hg-public/reportlab/"
        "</a>）上，以及问题跟踪器和Wiki。'"
        "每个人都可以随时做出贡献，但是如果您正在积极地进行一些改进，或者想引起人们对问题的关注，请使用邮件列表告知我们。"
    )

    pdf.add_heading('全局配置', level=2)
    pdf.add_paragraph(
        "有许多选项很可能需要为程序进行全局配置。"
        "python脚本模块$reportlab/rl_config.py$汇总了各种设置文件。"
        "您可能需要检查文件$reportlab/rl_settings.py$，其中包含当前使用的变量的默认值。"
        "$rl_settings$模块$reportlab.local_rl_settings$，"
        "$reportlab_settings$（位于python路径上任何位置的脚本文件）以及文件$~/.reportlab_settings$"
        "（请注意，没有.py）有多个替代项。可以进行临时更改。"
        "使用环境变量，这些变量是 $rl_settings.py$ 中以$RL_$开头的变量，例如$RL_verbose=1$。"
    )

    pdf.add_heading('有用的 $rl_config$ 变量', level=3)
    pdf.add_bullet("^verbose^: 设置为整数值以控制诊断输出。")
    pdf.add_bullet("^shapeChecking^: 将此设置为零可关闭图形模块中的许多错误检查")
    pdf.add_bullet(
        "^defaultEncoding^: 将此设置为 $WinAnsiEncoding$ 或 " "$MacRomanEncoding$ 。"
    )
    pdf.add_bullet(
        "^defaultPageSize^：将其设置为 $reportlab/lib/pagesizes.py$ 中定义的值之一；"
        "交付时将其设置为 $pagesizes.A4$; 其他值是 $pagesizes.letter$ 等。"
    )
    pdf.add_bullet(
        "^defaultImageCaching^：设置为零以禁止在硬盘驱动器上创建.a85文件。 "
        "默认设置是创建这些经过预处理的PDF兼容图像文件，以加快加载速度"
    )
    pdf.add_bullet("^T1SearchPath^：这是表示目录的字符串的python列表，可以查询有关类型1字体的信息")
    pdf.add_bullet(
        "^TTFSearchPath^：这是表示目录的字符串的python列表，可以查询该目录以获取有关$TrueType$字体的信息"
    )
    pdf.add_bullet("^CMapSearchPath^：这是表示目录的字符串的python列表，可以查询该目录以获取字体代码映射的信息。")
    pdf.add_bullet("^showBoundary^：设置为非零以绘制边界线。")
    pdf.add_bullet("^ZLIB_WARNINGS^：如果未找到Python压缩扩展，则设置为非零以获得警告。")
    pdf.add_bullet("^pageCompression^：设置为非零以尝试获取压缩的PDF。")
    pdf.add_bullet("^allowtableBoundsErrors^：设置为0会在非常大的Platypus表元素上强制执行错误")
    pdf.add_bullet(
        "^emptyTableAction^：控制空表的行为，可以为“$error$”（默认），“$indicate$”或“$ignore$"
    )
    pdf.add_bullet(
        "^TrustedHosts^：则列出全局模式下受信任的主机列表；这些模式可用于段落文本中的$&lt;img&gt;$ 标签等地方。"
    )
    pdf.add_bullet("^trustedSchemes^：与 $trustedHosts$ 一起使用的允许的 URL 方案的列表")

    pdf.add_paragraph("有关变量的完整列表，请参见文件 $reportlab/rl_settings.py$。")
    pdf.add_heading("其他修改", level=3)
    pdf.add_paragraph(
        "可以使用以下模块之一对reportlab工具箱环境进行更复杂的修改："
        "rep[ortlab.local_rl_mods（reportlab文件夹中的.py脚本），"
        "$reportlab_mods$（python路径上的.py文件）或$~/.reportlab_mods$（注意是.py）。"
    )

    pdf.add_heading("了解有关Python的更多信息", level=2)
    pdf.add_paragraph(
        "如果您是Python的初学者，则应该从越来越多的Python编程资源中检出一个或多个。 以下内容可从网上免费获得："
    )

    pdf.add_bullet(
        "$Python文档$Python.org网站上的文档列表。"
        "<a href='http://www.python.org/doc/'>http://www.python.org/doc/</a>"
    )
    pdf.add_bullet(
        "$Python教程$"
        "官方的Python教程，最初由Guido van Rossum亲自编写."
        "<a href='http://docs.python.org/tutorial/'>http://docs.python.org"
        "/tutorial/</a>"
    )
    pdf.add_bullet(
        "$学习编程$"
        "Alan Gauld撰写的编程指南。 非常重视Python，但也使用其他语言。"
        "<a href='http://www.freenetpages.co.uk/hp/alan.gauld/'>"
        "http://www.freenetpages.co.uk/hp/alan.gauld/</a>"
    )
    pdf.add_bullet(
        "$即时Python$Magnus Lie Hetland撰写的长达6页的速成课程。"
        "<a href='http://www.hetland.org/python/instant-python.php'>"
        "$http://www.hetland.org/python/instant-python.php$</a>"
    )
    pdf.add_bullet(
        "$深入Python$适用于经验丰富的程序员的免费Python教程。"
        "<a href='http://www.diveintopython.net/'>http://www"
        ".diveintopython.net/</a>"
    )
    pdf.add_heading("3.x版本系列的目标", level=2)
    pdf.add_paragraph(
        "已生成ReportLab 3.0，以帮助迁移到Python3.x。"
        "Python 3.x将在将来的Ubuntu版本中成为标准配置，并且越来越受欢迎，"
        "并且现在有很大一部分主要的Python程序包都在Python 3上运行。"
    )
    pdf.add_bullet("Python 3.x兼容性。 一行代码应在2.7和3.6上运行")
    pdf.add_bullet("__init__.py限制为2.7或> = 3.6")
    pdf.add_bullet("__init__.py允许导入可选的 ^reportlab.local_rl_mods^ ，以允许猴子打补丁等。")
    pdf.add_bullet(
        "rl_config现在可以导入 ^rl_settings^ ，还可以导入 ^local_rl_settings^，"
        "^reportlab_settings.py^，最后是 ^~/.reportlab_settings^"
    )
    pdf.add_bullet(
        "ReportLab C扩展现在位于reportlab中。 不再需要 $_rl_accel$ 。 "
        "现在，所有 $_rl_accel$ 导入都通过 ^reportlab.lib.rl_accel^ "
    )
    pdf.add_bullet("xmllib以及用于引起HTMLParser问题的paraparser东西一去不复返了。")
    pdf.add_bullet("一些过时的C扩展名（sgmlop和pyHnj）消失了")
    pdf.add_bullet("_rl_accel C扩展模块对多线程系统的改进支持。")
    pdf.add_bullet(
        "删除了 $reportlab/lib/para.py$ 和 $pycanvas.py$。 "
        "这些最好属于第三方程序包，可以利用上面的 $Monkeypatching$ 功能。"
    )
    pdf.add_bullet("增加了无需转换为RGB即可输出灰度和1位PIL图像的功能。 （由Matthew Duggan贡献）")
    pdf.add_bullet("高亮注释（由Ben Echols提供）")
    pdf.add_bullet("完全符合 $pip$ ，$easy_install$，$wheel$等要求")

    pdf.add_paragraph(
        "有关详细的发行说明，请访问："
        "<a href='http://www.reportlab.com/software/documentation/relnotes/30"
        "/'>"
        "^http://www.reportlab.com/software/documentation/relnotes/30/^</a>"
    )


def chapter2_overview(pdf):
    pdf.add_heading("使用 $pdfgen$ 生成图形和文本", level=1)
    pdf.add_heading("基本概念", level=2)
    pdf.add_paragraph(
        "$pdfgen$包是生成PDF文档的最低级别接口。 一个$pdfgen引擎$本质上是一个将文档\"绘制\"到页面序列上的指令序列。 "
        "提供绘画操作的接口对象是$pdfgen canvas$。"
    )
    pdf.add_paragraph(
        "他的画布应该被认为是一张白纸，白纸上的点用笛卡尔^(X,Y)^坐标确定，默认情况下，^(0,0)^原点在页面的左下角。 "
        "此外，第一个坐标^x^往右走，第二个坐标^y^往上走，这是默认的。"
    )
    pdf.add_paragraph("下面是一个使用画布的简单示例程序。")
    pdf.add_code_eg(
        """
        from reportlab.pdfgen import canvas
        
        c = canvas.Canvas("hello.pdf")
        c.drawString(100,100,"Hello World")
        c.showPage()
        c.save()
    """
    )
    pdf.add_paragraph(
        "上面的代码创建了一个$canvas$对象，它将在当前工作目录下生成一个名为$hello.pdf$的PDF文件。"
        "然后调用$hello$函数，将$canvas$作为参数。最后，$showPage$方法保存canvas的当前页面。"
    )
    pdf.add_paragraph(
        "$showPage$方法会使$canvas$"
        "停止在当前页上绘制，任何进一步的操作都会在随后的页面上绘制（如果有任何进一步的操作--如果没有的话"
        "新页面被创建）。在文档构建完成后必须调用$save$方法--它将生成PDF文档，这也是$canvas$对象的全部目的。"
    )
    pdf.add_heading("更多关于画布的信息", level=2)
    pdf.add_paragraph(
        "在介绍绘图操作之前，我们先离题万里，介绍一下配置画布可以做的一些事情。 有许多不同的设置可供选择。 "
        "如果你是Python新手，或者迫不及待地想产生一些输出，你可以跳过前面的内容，但以后再来阅读这个内容吧!"
    )
    pdf.add_paragraph("首先，我们来看看画布的构造函数参数:")
    pdf.add_code_eg(
        """    def __init__(self,filename,
                 pagesize=(595.27,841.89),
                 bottomup = 1,
                 pageCompression=0,
                 encoding=rl_config.defaultEncoding,
                 verbosity=0
                 encrypt=None):
                 """
    )
    pdf.add_paragraph(
        "参数$filename$控制最终PDF文件的名称。 "
        "你也可以传入任何开放的二进制流（如$sys.stdout$，python过程中标准的二进制编码输出），PDF文件将被写入该流。 "
        "由于PDF是二进制格式，所以在它之前或之后写其他东西的时候要小心，你不能在HTML页面中间内联传递PDF文档！"
        "你可以在HTML页面中写一个PDF文件，但不能在HTML页面中写一个PDF文件。"
    )
    pdf.add_paragraph(
        "参数$pagesize$是一个以点为单位的两个数字的元组（1/72英寸）。"
        "画布默认为$A4$（国际标准的页面尺寸，与美国标准的$letter$页面尺寸不同），但最好明确指定。 "
        "大多数常见的页面大小都可以在库模块$reportlab.lib.pagesizes$中找到，所以你可以使用类似于"
    )
    pdf.add_code_eg(
        """ from reportlab.lib.pagesizes import letter, A4
            myCanvas = Canvas('myfile.pdf', pagesize=letter)
            width, height = letter  #keep for later
        """
    )
    pdf.add_paragraph("如果您在打印文件时遇到问题，请确保您使用正确的页面尺寸（通常是$A4$或$letter$）。")
    pdf.add_paragraph(
        "很多时候，你会想根据页面大小来计算东西。 "
        "在上面的例子中，我们提取了宽度和高度。 "
        "在以后的程序中，我们可能会使用$width$变量来定义右边距为$width - inch$，而不是使用一个常数。"
        " 通过使用变量，即使页面大小发生变化，页边距也会有意义。"
    )
    pdf.add_paragraph(
        "参数$bottomup$用于切换坐标系。 "
        "一些图形系统(如PDF和PostScript)将(0,0)置于页面的左下角，"
        "其他系统(如许多图形用户界面[GUI's])将原点置于  $bottomup$参数已被废弃，以后可能会被删除。"
    )
    pdf.add_paragraph("需要看看它是否真的对所有任务都有效，如果没有，那就把它扔掉吧。")
    pdf.add_paragraph(
        "$pageCompression$选项决定是否对每一页的PDF操作流进行压缩。"
        " 默认情况下，页面流不被压缩，因为压缩会减慢文件的生成过程。"
        "如果输出大小很重要，则设置$pageCompression=1$，但请记住，压缩后的文件会更小，但生成速度更慢。"
        " 请注意，图像<i>总是</i>压缩的，只有当你在每一页上有非常多的文本和矢量图形时，这个选项才会节省空间。"
    )
    pdf.add_paragraph(
        "在2.0版本中，$encoding$参数基本上已经过时了，可能99%的用户都可以省略。"
        "它的默认值很好，除非你特别需要使用MacRoman中的25个字符之一，而Winansi中没有。"
        "这里是一个有用的参考资料:<font color=\"blue\"><u>"
        "<a href=\"http://www.alanwood.net/demos/charsetdiffs.html\">"
        "http://www.alanwood.net/demos/charsetdiffs.html</a></u></font>."
        "该参数决定了该文件的字体编码。标准Type 1字体；这应该与您系统上的编码相对应。"
        "请注意，这是字体<i>内部使用的编码</i>；"
        "您的文本传递给ReportLab工具包的渲染信息应该总是Python的unicode字符串对象或UTF-8编码的字节字符串(见下一章)! "
    )
    pdf.add_paragraph(
        "字体编码目前有两个值：$'WinAnsiEncoding'$或 $'MacRomanEncoding'$。"
        "上面的变量$rl_config.defaultEncoding$指向的是到前者，"
        "这是$Windows$、$Mac OS X$和许多$Unix$的标准配置(包括$Linux$)。"
        "如果你是Mac用户，并且没有$OS X$，你可能会想要进行全局性的修改："
        "修改在^reportlab/pdfbase/pdfdoc.py^来切换它。"
        "否则，您可以完全无视这个论点，永远不会通过。对于所有$TTF$和常用的CID字体，这里传入的编码会被忽略。"
        "因为reportlab库本身就知道这些情况下的正确编码。"
    )
    pdf.add_paragraph(
        "演示脚本$reportlab/demos/stdfonts.py$将打印出两个测试文档，"
        "显示所有字体的所有代码点，这样你就可以查找字符。"
        "特殊字符可以用通常的Python转义序列插入到字符串命令中，例如 \\101 = 'A'。"
    )
    pdf.add_paragraph(
        "参数$verbosity$决定了打印多少日志信息。 "
        "默认情况下，它是$0$，以帮助应用程序从标准输出中捕获PDF。"
        "如果值为$1$，每次生成文档时，您都会得到一条确认信息。"
        "更高的数字可能会在将来提供更多的输出。"
    )
    pdf.add_paragraph(
        "参数$encrypt$决定了是否以及如何对文档进行加密。"
        "默认情况下，文档没有被加密。如果$encrypt$是一个字符串对象，它被用作pdf的用户密码。"
        "如果$encrypt$是一个$reportlab.lib.pdfencrypt.StandardEncryption$的实例，"
        "那么这个对象就被用来加密pdf。这允许对加密设置进行更精细的控制。加密在第4章有更详细的介绍。"
    )
    pdf.add_cond_page_break()
    pdf.add_todo("$to do$ -- 所有的信息功能和其他非绘图的东西。")
    pdf.add_todo("覆盖所有构造函数参数，以及 ^setAuthor^ 等。")

    pdf.add_heading("绘图操作", level=2)
    pdf.add_paragraph("假设上面提到的$hello$函数实现如下（我们先不详细解释每个操作）。")
    pdf.add_code_eg(doc_examples.testhello)
    pdf.add_paragraph(
        "检查这段代码时注意到，使用画布进行的操作基本上有两种类型。 "
        "第一种类型是在页面上画一些东西，如一个文本字符串或一个矩形或一条线。"
        "第二种类型改变画布的状态，如改变当前的填充或笔触颜色，或改变当前的字体类型和大小。"
    )
    pdf.add_paragraph(
        "如果我们把程序想象成一个在画布上工作的画家，"
        "\"绘制\"操作使用当前的一组工具（颜色、线条样式、字体等）将颜料涂抹到画布上，"
        "而\"状态改变\"操作则改变了当前的一个工具"
        "（例如，将填充颜色从原来的任何颜色改为蓝色，或者将当前的字体改为15点的$Times-Roman$）。"
    )
    pdf.add_paragraph("上面列出的 \"hello world \"程序生成的文档将包含以下图形。")
    pdf.add_illustration(doc_examples.hello, 'pdfgen 生成 "Hello World"')

    pdf.add_heading("关于本文档中的演示", level=3)
    pdf.add_paragraph(
        f"本文档包含了所讨论的代码的演示，如上图矩形所示。 "
        f"这些演示是在嵌入指南真实页面中的 \"小页 \"上绘制的。"
        f"这些小页面的宽度为{constant.EXAMPLE_FUNCTION_X_INCHES}英寸，"
        f"高度为{constant.EXAMPLE_FUNCTION_Y_INCHES}英寸。"
        f"演示显示的是演示代码的实际输出。"
        f"为了方便起见，输出的大小被稍微缩小了。"
    )

    pdf.add_heading("工具：\"$draw$\"的操作", level=2)
    pdf.add_paragraph(
        "本节简要列出了该程序可用来使用画布界面在页面上绘制信息的工具。这些工具将在后面的章节中详细讨论。这里列出这些工具是为了便于参考和总结。"
    )
    pdf.add_heading("绘制直线相关方法", level=3)
    pdf.add_code_eg("""canvas.line(x1,y1,x2,y2)""")
    pdf.add_code_eg("""canvas.lines(linelist)""")

    pdf.add_paragraph("线条方法在画布上绘制直线段。")
    pdf.add_heading("绘制形状相关方法", level=3)

    pdf.add_code_eg("""canvas.grid(xlist, ylist) """)
    pdf.add_code_eg("""canvas.bezier(x1, y1, x2, y2, x3, y3, x4, y4)""")
    pdf.add_code_eg("""canvas.arc(x1,y1,x2,y2) """)
    pdf.add_code_eg("""canvas.rect(x, y, width, height, stroke=1, fill=0) """)
    pdf.add_code_eg("""canvas.ellipse(x1,y1, x2,y2, stroke=1, fill=0)""")
    pdf.add_code_eg(
        """canvas.wedge(x1,y1, x2,y2, startAng, extent, stroke=1, fill=0) """
    )
    pdf.add_code_eg("""canvas.circle(x_cen, y_cen, r, stroke=1, fill=0)""")
    pdf.add_code_eg(
        """canvas.roundRect(x, y, width, height, radius, stroke=1, fill=0) """
    )

    pdf.add_paragraph("形状方法在画布上绘制常见的复杂形状。")

    pdf.add_heading("绘制字符串相关方法", level=3)

    pdf.add_code_eg("""canvas.drawString(x, y, text):""")
    pdf.add_code_eg("""canvas.drawRightString(x, y, text) """)
    pdf.add_code_eg("""canvas.drawCentredString(x, y, text)""")

    pdf.add_paragraph("绘制字符串方法在画布上绘制单行文字。")

    pdf.add_heading("文本对象相关方法", level=3)
    pdf.add_code_eg("""textobject = canvas.beginText(x, y) """)
    pdf.add_code_eg("""canvas.drawText(textobject) """)
    pdf.add_paragraph(
        "文本对象用于以$canvas$界面不直接支持的方式来格式化文本。"
        "程序使用$beginText$从$canvas$创建一个文本对象，"
        "然后通过调用$textobject$方法来格式化文本。"
        "最后使用$drawText$将$textobject$绘制到canvas上。"
    )
    pdf.add_heading("路径对象相关方法", level=3)
    pdf.add_code_eg("""path = canvas.beginPath() """)
    pdf.add_code_eg(
        """canvas.drawPath(path, stroke=1, fill=0, fillMode=None) """
    )
    pdf.add_code_eg(
        """canvas.clipPath(path, stroke=1, fill=0, fillMode=None) """
    )
    pdf.add_paragraph(
        "路径对象类似于文本对象：它们为执行复杂的图形绘制提供了画布界面无法直接提供的专用控件。 "
        "程序使用$beginPath$创建一个路径对象，使用路径对象的方法为路径填充图形，"
        "然后使用$drawPath$在画布上绘制路径。"
    )
    pdf.add_paragraph(
        "也可以使用$clipPath$方法将一个路径作为 \"剪切区域\""
        "--例如，一个圆形的路径可以用来剪切掉一个矩形图像的外部部分，"
        "只留下图像的一个圆形部分在页面上可见。"
    )
    pdf.add_paragraph(
        "如果指定了$fill=1$，那么$fillMode$参数可以用来设置0=$even-odd$或1=$non-zero$填充模式，"
        "这将改变复杂路径的填充方式。"
        "如果使用默认的$None$值，则使用canvas的$_fillMode$属性值（通常为$0$即$even-odd$）。"
    )
    pdf.add_heading("图像相关方法", level=3)
    pdf.add_pencil_note()
    pdf.add_paragraph(
        "你需要Python Imaging Library (PIL)来使用ReportLab包的图像。"
        "通过运行我们的$tests$子目录中的脚本$test_pdfgen_general.py$并查看输出的第7页，"
        "可以找到下面的技术示例。"
    )
    pdf.add_paragraph(
        "有两种听起来差不多的画像方式。 首选的是$drawImage$方法。"
        "它实现了一个缓存系统，所以你可以一次定义一个图像，并多次绘制；"
        "它将只在PDF文件中存储一次。"
        "$drawImage$还公开了一个高级参数，一个透明度掩模，将来还会公开更多。"
        "较老的技术，$drawInlineImage$在页面流中存储位图，"
        "因此，如果你在文档中不止一次使用相同的图像，效率非常低；"
        "但如果图像非常小且不重复，则可以导致PDF更快地渲染。"
        "我们先讨论最老的那个。"
    )
    pdf.add_code_eg(
        """canvas.drawInlineImage(self, image, x,y, width=None,height=None) """
    )
    pdf.add_paragraph(
        "$drawInlineImage$方法在画布上放置一张图片。"
        "参数$image$可以是一个PIL图像对象或图像文件名。"
        "许多常见的文件格式都被接受，包括GIF和JPEG。"
        "它以(宽，高)元组的形式返回实际图像的像素大小。"
    )
    pdf.add_code_eg(
        """canvas.drawImage(self, image, x,y, width=None,height=None,
        mask=None) """
    )
    pdf.add_paragraph(
        "参数和返回值和$drawInlineImage$一样。 "
        "然而，我们使用了一个缓存系统；"
        "一个给定的图像将只在第一次使用时被存储，而只是在后续使用时被引用。 "
        "如果您提供一个文件名，它假设相同的文件名意味着相同的图像。 "
        "如果你提供了一个PIL图片，它在重新嵌入之前会测试内容是否有实际变化。"
    )
    pdf.add_paragraph(
        "参数$mask$可以让你创建透明图像。 "
        "它需要6个数字，并定义RGB值的范围，这些值将被屏蔽掉或被视为透明。"
        "例如，使用 [0,2,40,42,136,139]，它将遮蔽任何"
        "红色值为 0 或 1 的像素，"
        "绿色值为 40 或 41 的像素，"
        "蓝色值为 136、137 或 138 的像素（在 0-255 的范围内）。"
        "目前你的工作是知道哪种颜色是 \"透明 \"的或背景的。"
    )
    pdf.add_paragraph(
        "PDF允许许多图像功能，我们将在一段时间内暴露更多的图像功能，可能会用额外的关键字参数来表示$drawImage$。"
    )
    pdf.add_heading("结束一个页面", level=3)
    pdf.add_code_eg("""canvas.showPage()""")
    pdf.add_paragraph("$showPage$方法完成了当前页面。 所有额外的绘图将在另一个页面上完成。")
    pdf.add_pencil_note()
    pdf.add_paragraph(
        "警告! "
        "当你在$pdfgen$中前进到一个新的页面时，"
        "所有的状态改变（字体改变，颜色设置，几何变换，等等）都会被忘记。"
        "任何您希望保留的状态设置必须在程序继续绘制之前重新设置!"
    )
    pdf.add_heading("工具箱：'状态变化'(state change) 操作", level=2)
    pdf.add_paragraph("本节简要列举了程序使用$canvas$界面将信息绘制到页面上的工具的切换方法。这些也将在后面的章节中详细讨论。")
    pdf.add_heading("改变颜色", level=3)

    pdf.add_code_eg("""canvas.setFillColorCMYK(c, m, y, k) """)
    pdf.add_code_eg("""canvas.setStrikeColorCMYK(c, m, y, k) """)
    pdf.add_code_eg("""canvas.setFillColorRGB(r, g, b) """)
    pdf.add_code_eg("""canvas.setStrokeColorRGB(r, g, b) """)
    pdf.add_code_eg("""canvas.setFillColor(acolor) """)
    pdf.add_code_eg("""canvas.setStrokeColor(acolor) """)
    pdf.add_code_eg("""canvas.setFillGray(gray) """)
    pdf.add_code_eg("""canvas.setStrokeGray(gray) """)

    pdf.add_paragraph(
        "PDF支持三种不同的颜色模型：灰度级、外加剂(red/green/blue或RGB)、 "
        "和 减去暗度参数（青色/红褐色/黄色/暗度或CMYK）。"
        "ReportLab包还提供了命名颜色，如$lawngreen$。 "
        "这里是图形状态下的两个基本颜色参数：$Fill$的为图形的填充色和$Stroke$为图形的边框色。 "
        "上述两种方法支持使用四种颜色中的任何一种来设置填充或描边颜色。"
    )
    pdf.add_heading("更改字体", level=3)
    pdf.add_code_eg("""canvas.setFont(psfontname, size, leading = None) """)
    pdf.add_paragraph(
        "$setFont$方法将当前的文本字体改为给定的类型和大小。$leading$参数指定了从一行文字前进到下一行时向下移动的距离。"
    )
    pdf.add_heading("更改图形线条样式", level=3)
    pdf.add_code_eg("""canvas.setLineWidth(width) """)
    pdf.add_code_eg("""canvas.setLineCap(mode) """)
    pdf.add_code_eg("""canvas.setLineJoin(mode) """)
    pdf.add_code_eg("""canvas.setMiterLimit(limit) """)
    pdf.add_code_eg("""canvas.setDash(self, array=[], phase=0) """)
    pdf.add_paragraph(
        "在PDF中绘制的线条可以以多种图形样式呈现。"
        "线条可以有不同的宽度，它们可以以不同的盖子样式结束，"
        "它们可以以不同的连接样式相接，它们可以是连续的，也可以是点线或虚线。 "
        "上述方法可以调整这些不同的参数。"
    )
    pdf.add_heading("改变几何形状", level=3)
    pdf.add_code_eg("""canvas.setPageSize(pair) """)
    pdf.add_code_eg("""canvas.transform(a,b,c,d,e,f): """)
    pdf.add_code_eg("""canvas.translate(dx, dy) """)
    pdf.add_code_eg("""canvas.scale(x, y) """)
    pdf.add_code_eg("""canvas.rotate(theta) """)
    pdf.add_code_eg("""canvas.skew(alpha, beta) """)
    pdf.add_paragraph(
        "所有的PDF图纸都适合指定的页面大小。 "
        "在指定的页面尺寸之外绘制的元素是不可见的。"
        "此外，所有绘制的元素都会通过一个可能调整其位置和/或扭曲其外观的仿射变换。 "
        "$setPageSize$方法可以调整当前的页面大小。 "
        "$transform$, $translate$, $scale$, $rotate$, "
        "和 $skew$ 方法会给当前的变换添加额外的变换。"
        "重要的是要记住，这些转换是<i>递增的</i>。 "
        "-- 新的变换会修改当前的变换(但不会取代它)；"
    )

    pdf.add_heading("状态控制", level=3)
    pdf.add_code_eg("""canvas.saveState() """)
    pdf.add_code_eg("""canvas.restoreState() """)
    pdf.add_paragraph(
        "很多时候，保存当前的字体、图形变换、线条样式和其他图形状态是很重要的，以便以后恢复它们。"
        "$saveState$方法标记了当前的图形状态，以便以后通过匹配的$restoreState$进行恢复。 "
        "请注意，保存和还原方法的调用必须匹配--还原调用会将状态还原到最近保存的状态，而最近的状态还没有被还原。"
        "但是，你不能在一个页面上保存状态，然后在下一个页面上还原它 -- 页面之间不会保存状态。"
    )

    pdf.add_heading("其他$canvas$的方法", level=2)
    pdf.add_paragraph(
        "并非所有$canvas$对象的方法都适合\"tool\"或\"toolbox\"类别。 "
        "以下是一些不合群的方法，为了完整起见，在此收录。"
    )
    pdf.add_code_eg(
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

    pdf.add_heading("坐标（默认用户空间)", level=2)
    pdf.add_paragraph(
        "默认情况下，页面上的位置是由一对数字来标识的，"
        "例如，一对$(4.5*inch, 1*inch)$标识的是页面上的位置。"
        "例如，一对$(4.5*inch, 1*inch)$从左下角开始，向右移动4.5英寸，"
        "再向上移动一英寸，来标识页面上的位置。"
    )
    pdf.add_paragraph("例如，下面的函数在$canvas$上绘制一些元素。")
    pdf.add_code_eg(doc_examples.testcoords)
    pdf.add_paragraph(
        "在默认的用户空间中，\"原点\"^(0,0)^点在左下角。  "
        "在默认的用户空间中执行$coords$函数（针对 \"演示迷你页\"），我们得到以下结果。"
    )
    pdf.add_illustration(doc_examples.coords, '坐标系统')

    pdf.add_heading("移动原点：$translate$方法", level=3)
    pdf.add_paragraph(
        "通常情况下，\"移动原点 \"到左下角的新点是很有用的。 "
        "$canvas.translate(^x,y^)$方法将当前页面的原点移动到当前由^(x,y)^确定的点。"
    )
    pdf.add_paragraph("例如下面的平移函数首先移动原点，然后再绘制如上所示的相同对象。")
    pdf.add_code_eg(doc_examples.testtranslate)
    pdf.add_paragraph("这就产生了以下结果：")
    pdf.add_illustration(doc_examples.translate, "移动原点：$translate$方法")
    pdf.add_pencil_note()
    pdf.add_text_note(
        "如示例中所示，完全可以将对象或对象的一部分绘制到\"页面之外\"。"
        "特别是一个常见的令人困惑的错误是将整个绘图从页面的可见区域翻译出来的翻译操作。 "
        "如果一个程序产生了一个空白页，那么所有绘制的对象都有可能不在页面上。"
    )
    pdf.add_heading("缩小与增长：scale操作", level=3)
    pdf.add_paragraph(
        "另一个重要的操作是缩放操作。 "
        "缩放操作$canvas.scale(^dx,dy^)$分别以^dx^, ^dy^系数来拉伸或缩小^x^和^y^的尺寸。 "
        "通常情况下，^dx^和^dy^是相同的 -- 例如，"
        "要在所有维度上将图形缩小一半，使用$dx = dy = 0.5$。 "
        "然而为了说明问题，我们举一个例子，其中$dx$和$dy$是不同的。"
    )
    pdf.add_code_eg(doc_examples.testscale)
    pdf.add_paragraph("这样就会产生一个 \"短小精悍\"的缩小版的之前显示的操作。")
    pdf.add_illustration(doc_examples.scale, "缩放坐标系统")
    pdf.add_pencil_note()
    pdf.add_text_note("缩放也可能会将对象或对象的一部分从页面上移开，或者可能会导致对象 \"缩水为零\"。")
    pdf.add_paragraph("缩放和翻译可以结合起来，但操作的顺序很重要。")
    pdf.add_code_eg(doc_examples.testscaletranslate)
    pdf.add_paragraph(
        "这个示例函数首先保存当前的$canvas$状态，然后进行$scale$和$translate$操作。 "
        "之后，函数恢复了状态（有效地消除了缩放和翻译的影响），"
        "然后以不同的顺序进行<i>相同的</i>操作。"
        "观察下面的效果。"
    )
    pdf.add_illustration(doc_examples.scaletranslate, "缩放和翻译")
    pdf.add_pencil_note()
    pdf.add_text_note(
        "缩放会收缩或增长所有的东西，包括线宽，"
        "因此使用canvas.scale方法以缩放的微观单位来渲染微观图形可能会产生一个blob（因为所有的线宽都会被大量扩展）。"
        "此外，以米为单位渲染飞机机翼，缩放为厘米，可能会导致线条收缩到消失的程度。 "
        "对于工程或科学目的，如这些比例和翻译。"
        "在使用画布渲染之前，从外部对单元进行渲染。"
    )
    pdf.add_heading("保存和恢复$canvas$状态：$saveState$和$restoreState$。", level=3)
    pdf.add_paragraph(
        "$scaletranslate$函数使用了$canvas$对象的一个重要特性：能够保存和恢复$canvas$的当前参数。"
        "通过在一对匹配的$canvas.saveState()$和$canvas.restoreState()$操作中包含一个操作序列，"
        "所有字体、颜色、线条样式、缩放、翻译或$canvas$图形状态的其他方面的变化都可以恢复到$saveState()$点的状态。"
        "请记住，保存/还原调用必须匹配：一个杂乱的保存或还原操作可能会导致意外和不理想的行为。"
        "另外，请记住，<i>没有</i> $canvas$状态会在页面中断时被保存，保存/还原机制不会不能跨越分页符工作。"
    )
    pdf.add_heading("镜像", level=3)
    pdf.add_paragraph("有趣的是，虽然可能不是非常有用，但注意到比例因子可以是负的。 例如下面的函数")
    pdf.add_code_eg(doc_examples.testmirror)
    pdf.add_paragraph("创建$coord$函数绘制的元素的镜像。")
    pdf.add_illustration(doc_examples.mirror, "镜像")
    pdf.add_paragraph("注意，文字串是倒着画的。")
    pdf.add_heading("颜色", level=2)
    pdf.add_paragraph(
        "PDF中使用的颜色一般有两种类型，这取决于PDF将被使用的媒体。"
        "最常见的屏幕颜色模型RGB可以在PDF中使用，然而在专业印刷中主要使用另一种颜色模型CMYK，"
        "它可以对油墨如何应用于纸张进行更多的控制。以下是关于这些颜色模型的更多信息。"
    )
    pdf.add_heading("RGB颜色", level=3)
    pdf.add_paragraph(
        "$RGB$或称加色表示法，遵循电脑屏幕添加不同层次的红、绿、蓝光的方式，使其间的任何颜色，" "其中白色是通过将三盏灯全开形成的。"
    )
    pdf.add_paragraph(
        "在$pdfgen$中，有三种方法可以指定RGB颜色："
        "通过名称（使用$color$模块），"
        "通过红/绿/蓝（加法，$RGB$）值，"
        "或者通过灰度级别。"
        "下面的$colors$函数对这四种方法分别进行了练习。"
    )
    pdf.add_code_eg(doc_examples.testRGBcolors)
    pdf.add_illustration(doc_examples.colorsRGB, "RGB 颜色模块")
    pdf.add_heading("RGB颜色透明度", level=4)
    pdf.add_paragraph(
        "在$pdfgen$中，可以将对象涂在其他对象上，以达到良好的效果。 "
        "一般来说，有两种模式可以处理空间中重叠的对象，顶层的默认对象会隐藏掉它下面的其他对象的任何部分。"
        "如果你需要透明度，你有两个选择:"
    )
    pdf.add_paragraph(
        "1. 如果您的文档打算以专业的方式打印，并且您在CMYK色彩空间中工作，那么您可以使用overPrint。"
        "在overPrinting中，颜色会在打印机中物理混合，从而获得一种新的颜色。"
        "默认情况下，将应用一个淘汰，只有顶部对象出现。"
        "如果您打算使用CMYK，请阅读CMYK部分。"
    )
    pdf.add_paragraph(
        "2. 如果您的文档打算用于屏幕输出，并且您使用的是RGB颜色，"
        "那么您可以设置一个alpha值，其中alpha是颜色的不透明度值。"
        "默认的alpha值是 $1$（完全不透明），你可以使用任何实数。"
    )
    pdf.add_paragraph(
        "Alpha透明度($alpha$)类似于overprint，"
        "但在RGB色彩空间中工作，下面这个例子演示了alpha功能。"
        "请参考我们的网站 http://www.reportlab.com/snippets/，"
        "并查找overPrint和alpha的片段，以查看生成下面图表的代码。"
    )
    pdf.add_code_eg(doc_examples.testalpha)
    pdf.add_illustration(doc_examples.alpha, "Alpha 例子")
    pdf.add_heading("CMYK 颜色", level=3)
    pdf.add_paragraph(
        "$CMYK$或减法是按照打印机混合三种颜料（青色、品红色和黄色）形成颜色的方式进行的。"
        "因为混合化学品比结合光照更难 还有第四个参数是暗度。 "
        "例如，$CMY$颜料的化学组合通常不会产生完美的黑色"
        "--而是产生混浊的颜色--因此，为了得到黑色，打印机不使用$CMY$颜料，而是直接使用黑色墨水。 "
        "因为$CMYK$更直接地映射到打印机硬件的工作方式，"
        "所以在打印时，$CMYK$指定的颜色可能会提供更好的保真度和更好的控制。"
    )
    pdf.add_paragraph(
        "CMYK颜色有两种表示方法："
        "每一种颜色都可以用以下方法来表示可以是0到1之间的实值，"
        "也可以是0到100之间的整数值。"
        "根据您的喜好，您可以使用CMYKColor（对于实值）或 PCMYKColor（对于整数值）。"
        "0表示 \"没有墨水\"，所以在白纸上打印会得到白色。"
        "1表示 \"最大墨水量\"(如果使用PCMYKColor，则为100)。"
        "例如：CMYKColor(0,0,0,1)是黑色，CMYKColor(0,0,0,0)表示 \"没有墨水\"。"
        "而CMYKColor(0.5,0,0,0)表示50%的青色。"
    )
    pdf.add_code_eg(doc_examples.testCMYKcolors)
    pdf.add_illustration(doc_examples.colorsCMYK, "CMYK颜色模型")
    pdf.add_heading("色彩空间检查", level=2)
    pdf.add_paragraph(
        "画布的$enforceColorSpace$参数用于强制执行文档中使用的颜色模型的一致性。"
        "它接受这些值。$CMYK$, $RGB$, $SEP$, $SEP_BLACK$, $SEP_CMYK$."
        "\"SEP\"指的是命名的分色，如$Pantone$专色--根据使用的参数，这些颜色可以与$CMYK$或$RGB$混合。"
        "默认值是'$MIXED$'，允许你使用任何颜色空间的颜色。"
        "如果使用的任何颜色不能转换为指定的模型，例如^rgb^和^cmyk^，"
        "就会产生一个异常（更多信息请参见$test_pdfgen_general$）。"
        "这种方法不检查文档中包含的外部图像。"
    )
    pdf.add_heading("彩色套印", level=2)
    pdf.add_paragraph(
        "当两个CMYK颜色的对象在打印时重叠，"
        "那么 \"上面\"的对象会把下面的对象的颜色打掉，或者两个对象的颜色会在重叠的区域混合。"
        "这种行为可以使用属性$overPrint$来设置。"
    )
    pdf.add_paragraph(
        "$overPrint$"
        "函数将导致色彩的椭圆区域混合。"
        "在下面的例子中，左边矩形的颜色应该在它们重叠的地方出现混合"
        "--如果你看不到这个效果，那么你可能需要在你的PDF浏览软件中启用\"叠印预览\"选项。 "
        "一些PDF浏览器，如$evince$不支持叠印，但是Adobe Acrobat Reader支持。"
    )
    pdf.add_illustration(doc_examples.overPrint, "OverPrint示例")
    pdf.add_heading("其他对象的打印顺序示例", level=3)
    pdf.add_paragraph('"SPUMONI"字样用白色涂抹在彩色长方形上，有明显的 "去除 "字体内部颜色的效果。')
    pdf.add_code_eg(doc_examples.testspumoni)
    pdf.add_illustration(doc_examples.spumoni, "涂抹颜色")
    pdf.add_paragraph("由于默认的$canvas$背景是白色的，在白色背景上画上白色的字母，单词的最后一个字母不可见。")
    pdf.add_paragraph("这种分层建立复杂绘画的方法可以在$pdfgen$中完成非常多的层数--比起处理物理颜料时的物理限制要少。")
    pdf.add_code_eg(doc_examples.testspumoni2)
    pdf.add_paragraph("Spumoni2$函数在$spumoni$图上叠加一个冰淇淋圆锥。 请注意，圆锥和勺子的不同部分也会互相分层。")
    pdf.add_illustration(doc_examples.spumoni2, "层层叠加")
    pdf.add_heading("标准字体和文本对象", level=2)
    pdf.add_paragraph(
        "在$pdfgen$中可以用许多不同的颜色、字体和大小来绘制文本。"
        "$textsize$函数演示了如何改变文本的颜色、字体和大小，以及如何在页面上放置文本。"
    )
    pdf.add_code_eg(doc_examples.testtextsize)
    pdf.add_paragraph("$textsize$函数生成了以下页面。")
    pdf.add_illustration(doc_examples.textsize, "不同字体和大小的文字")
    pdf.add_paragraph("不同字体和大小的文本在$pdfgen$中总是有许多不同的字体。")
    pdf.add_code_eg(doc_examples.testfonts)
    pdf.add_paragraph(
        "函数$fonts$列出了始终可用的字体。" "这些字体不需要存储在PDF文档中，" "因为它们保证在Acrobat Reader中存在。"
    )
    pdf.add_illustration(doc_examples.fonts, "14种标准字体")
    pdf.add_paragraph("Symbol和ZapfDingbats字体无法正确显示，因为这些字体中不存在所需的字形。")
    pdf.add_paragraph("有关如何使用任意字体的信息，请参阅下一章。")
    pdf.add_heading("文本对象方法", level=2)
    pdf.add_paragraph(
        "对于PDF文档中文本的专用展示，可以使用文本对象。"
        "文本对象接口提供了对文本布局参数的详细控制，而这些参数在$canvas$级别是无法直接获得的。 "
        "此外，它还可以生成更小的PDF，其渲染速度比许多单独调用$drawString$方法要快。"
    )
    pdf.add_code_eg("""textobject.setTextOrigin(x,y)""")
    pdf.add_code_eg("""textobject.setTextTransform(a,b,c,d,e,f)""")
    pdf.add_code_eg(
        """textobject.moveCursor(dx, dy) # from start of current LINE"""
    )
    pdf.add_code_eg("""(x,y) = textobject.getCursor()""")
    pdf.add_code_eg("""x = textobject.getX(); y = textobject.getY()""")
    pdf.add_code_eg("""textobject.setFont(psfontname, size, leading = None)""")
    pdf.add_code_eg("""textobject.textOut(text)""")
    pdf.add_code_eg("""textobject.textLine(text='')""")
    pdf.add_code_eg("""textobject.textLines(stuff, trim=1)""")
    pdf.add_paragraph("上面显示的文本对象方法与基本的文本几何体有关。")
    pdf.add_paragraph(
        "文本对象维护一个文本光标，当文本被绘制时，这个光标会在页面上移动。 "
        "例如，$setTextOrigin$将光标放置在一个已知的位置，"
        "而$textLine$和$textLines$方法则将文本光标向下移动，经过缺失的线条。"
    )
    pdf.add_code_eg(doc_examples.testcursormoves1)
    pdf.add_paragraph("函数$cursormoves$依靠文本光标的自动移动来放置原点后的文本。")
    pdf.add_illustration(doc_examples.cursormoves1, "文本光标的移动方式")
    pdf.add_paragraph(
        "也可以通过使用$moveCursor$方法更明确地控制光标的移动"
        "（该方法将光标移动为从当前<i>线</i>开始的偏移量，而不是当前光标，"
        "并且该方法还具有正^y^偏移量移动<i>向下</i>)"
        "与正常几何形状相反，正^y^通常向上移动。"
    )
    pdf.add_code_eg(doc_examples.testcursormoves2)
    pdf.add_paragraph("在这里，$textOut$不会向下移动一行，而$textLine$函数则向下移动。")
    pdf.add_illustration(doc_examples.cursormoves2, "文本光标如何再次移动")
    pdf.add_heading("字符间距", level=3)
    pdf.add_code_eg("""textobject.setCharSpace(charSpace)""")
    pdf.add_paragraph("$setCharSpace$方法调整文本的一个参数--字符间的间距。")
    pdf.add_code_eg(doc_examples.testcharspace)
    pdf.add_paragraph("$charspace$函数行使各种间距设置。它产生以下页面。")
    pdf.add_illustration(doc_examples.charspace, "调整字符间距")
    pdf.add_heading("字距", level=3)
    pdf.add_code_eg("""textobject.setWordSpace(wordSpace)""")
    pdf.add_paragraph("$setWordSpace$方法调整字与字之间的空间。")
    pdf.add_code_eg(doc_examples.testwordspace)
    pdf.add_paragraph("$wordspace$函数显示了下面各种文字空间设置的样子。")
    pdf.add_illustration(doc_examples.wordspace, "调整字距")
    pdf.add_heading("水平缩放", level=3)
    pdf.add_code_eg("""textobject.setHorizScale(horizScale)""")
    pdf.add_paragraph("文本行可以通过$setHorizScale$方法进行水平拉伸或收缩。")
    pdf.add_code_eg(doc_examples.testhorizontalscale)
    pdf.add_paragraph("水平缩放参数^horizScale^是以百分比的形式给出的（默认为100），所以下图所示的80设置看起来很瘦。")
    pdf.add_illustration(doc_examples.horizontalscale, "调整水平文本的比例")
    pdf.add_heading("行间间距(领先)", level=3)
    pdf.add_code_eg("""textobject.setLeading(leading)""")
    pdf.add_paragraph("一条线的起始点和下一条线的起始点之间的垂直偏移称为前导偏移。 " "$setLeading$方法调整前导偏移。")
    pdf.add_code_eg(doc_examples.testleading)
    pdf.add_paragraph("如下图所示，如果一行的前导偏移量设置得太小，我就会把前一行中的字符的底部部分写在上面。")
    pdf.add_illustration(doc_examples.leading, "矫枉过正")
    pdf.add_heading("其他文本对象方法", level=3)
    pdf.add_code_eg("""textobject.setTextRenderMode(mode)""")
    pdf.add_paragraph("例如，$setTextRenderMode$方法允许将文本作为剪裁背景图的前景。")
    pdf.add_code_eg("""textobject.setRise(rise)""")
    pdf.add_paragraph(
        "$setRise$方法<super>提高</super>或<sub>降低</sub>行上的文本（例如，用于创建上标或下标）。"
    )
    pdf.add_code_eg(
        """textobject.setFillColor(aColor);
        textobject.setStrokeColor(self, aColor)
        # and similar"""
    )
    pdf.add_paragraph(
        "这些颜色变化操作会改变文本的<font color=darkviolet>颜色</font>，"
        "其他方面与$canvas$对象的颜色方法类似。"
    )
    pdf.add_heading("路径和直线", level=2)
    pdf.add_paragraph(
        "正如文本对象被设计成专门用于展示文本一样，路径对象被设计成专门用于构建图形。 "
        "当路径对象被绘制到$canvas$上时，它们被绘制成一个图形（就像一个矩形），"
        "整个图形的绘制模式可以调整：图形的线条可以绘制（笔画），也可以不绘制；"
        "图形的内部可以填充，也可以不填充；等等。"
    )
    pdf.add_paragraph("例如，$star$函数使用一个路径对象来绘制一个星体")
    pdf.add_code_eg(doc_examples.teststar)
    pdf.add_paragraph("$star$函数被设计用来说明$pdfgen$支持的各种行式参数。")
    pdf.add_illustration(doc_examples.star, "直线样式参数")
    pdf.add_heading("直线连接设置", level=3)
    pdf.add_paragraph("通过$setLineJoin$方法，可以调整线段在一个点上相接的是方块还是圆角顶点。")
    pdf.add_code_eg(doc_examples.testjoins)
    pdf.add_paragraph("线条连接的设置只有对粗线条才真正有意义，因为对细线条看不清楚。")
    pdf.add_illustration(doc_examples.joins, "不同的直线连接样式")
    pdf.add_heading("直线帽子设置", level=3)
    pdf.add_paragraph(
        "使用$setLineCap$方法调整的线帽设置，" "决定了终止线的终点是在顶点处的正方形、" "顶点上方的正方形还是顶点上方的半圆。"
    )
    pdf.add_code_eg(doc_examples.testcaps)
    pdf.add_paragraph("线帽设置和线条连接设置一样，只有在线条较粗时才会清晰可见。")
    pdf.add_illustration(doc_examples.caps, "直线帽子设置")
    pdf.add_heading("破折号和断线", level=3)
    pdf.add_paragraph("用$setDash$方法可以将线条分成点或破折号。")
    pdf.add_code_eg(doc_examples.testdashes)
    pdf.add_paragraph("虚线或圆点的图案可以是简单的开/关重复图案，也可以指定为复杂的重复图案。")
    pdf.add_illustration(doc_examples.dashes, "破折号")
    pdf.add_heading("用路径对象创建复杂的图形", level=3)
    pdf.add_paragraph(
        "线条、曲线、弧线等图形的组合可以使用路径对象组合成一个图形。"
        "例如下图所示的函数就是利用直线和曲线构造两个路径对象。"
        "这个函数将在后面的铅笔图标构造中使用。"
    )
    pdf.add_code_eg(doc_examples.testpenciltip)
    pdf.add_paragraph(
        "请注意，铅笔头的内部是作为一个对象填充的，即使它是由几条线和曲线构成的。" "然后使用一个新的路径对象在其上绘制铅笔头。"
    )
    pdf.add_illustration(doc_examples.penciltip, "铅笔头")
    pdf.add_heading("矩形、圆形、椭圆形。", level=2)
    pdf.add_paragraph(
        "$pdfgen$模块支持许多一般有用的形状，如矩形、圆角矩形、椭圆和圆。"
        "这些图形中的每一个都可以在路径对象中使用，也可以直接在$canvas$上绘制。 "
        "例如下面的$pencil$函数使用矩形和圆角矩形绘制了一个铅笔图标，"
        "并添加了各种填充颜色和其他一些注释。"
    )
    pdf.add_code_eg(doc_examples.testpencil)
    pdf.add_pencil_note()
    pdf.add_text_note(
        "这个函数是用来创建左边的'边距铅笔'的。"
        "还要注意的是，元素的绘制顺序很重要，因为，"
        "例如，白色矩形'擦掉'了黑色矩形的一部分，"
        "而 '笔尖'则涂抹了黄色矩形的一部分。"
    )
    pdf.add_illustration(doc_examples.pencil, "铅笔")
    pdf.add_heading("贝兹尔曲线", level=2)
    pdf.add_paragraph("想要构造具有弯曲边界的图形的程序，一般使用贝塞尔曲线来形成边界。")
    pdf.add_code_eg(doc_examples.testbezier)
    pdf.add_paragraph(
        "Bezier曲线由四个控制点$(x1,y1)$，$(x2,y2)$，$(x3,y3)$，$(x4,y4)$指定。"
        "曲线起于$(x1,y1)$，止于$(x4,y4)$，从$(x1,y1)$到$(x2,y2)$的线段和从$(x3,y3)$到$(x4,"
        "y4)$的线段都与曲线形成切线。 "
        "而且曲线完全包含在凸图形中，顶点在控制点上。"
    )
    pdf.add_illustration(doc_examples.bezier, "基本贝塞尔曲线")
    pdf.add_paragraph("上图($testbezier$的输出)显示了一个bezier曲线、控制点定义的切线和控制点处有顶点的凸图形。")
    pdf.add_heading("平滑地连接贝塞尔曲线序列", level=3)
    pdf.add_paragraph(
        "通常情况下，将几条贝塞尔曲线连接成一条平滑曲线是很有用的。 "
        "要想从几条贝塞尔曲线中构造一条较大的平滑曲线，"
        "请确保相邻贝塞尔曲线在控制点连接的切线位于同一直线上。"
    )
    pdf.add_code_eg(doc_examples.testbezier2)
    pdf.add_paragraph('由$testbezier2$创建的图形描述了一条平滑的复曲线，因为相邻的切线 "排队"，如下图所示。')
    pdf.add_illustration(doc_examples.bezier2, "bezier curves")
    pdf.add_heading("路径对象方法", level=2)
    pdf.add_paragraph(
        '路径对象通过在画布上的起始点设置 "笔"或"画笔"，'
        '并在画布上的附加点上绘制线条或曲线，从而建立复杂的图形。'
        '大多数操作都是从上一次操作的终点开始在画布上涂抹颜料，并在新的终点留下画笔。'
    )
    pdf.add_code_eg("""pathobject.moveTo(x,y)""")
    pdf.add_paragraph(
        "$moveTo$方法抬起画笔(结束任何当前的线条或曲线序列(如果有的话))，"
        "并在画布上新的^(x,y)^位置替换画笔，开始一个新的路径序列。"
    )
    pdf.add_code_eg("""pathobject.lineTo(x,y)""")
    pdf.add_paragraph("$lineTo$方法从当前笔刷位置到新的^(x,y)^位置绘制直线段。")
    pdf.add_code_eg("""pathobject.curveTo(x1, y1, x2, y2, x3, y3) """)
    pdf.add_paragraph(
        "$curveTo$方法从当前画笔位置开始绘制一条贝塞尔曲线，"
        "使用^(x1,y1)^、^(x2,y2)^和^(x3,y3)^作为其他三个控制点，"
        "将画笔留在^(x3,y3)^上。"
    )
    pdf.add_code_eg("""pathobject.arc(x1,y1, x2,y2, startAng=0, extent=90) """)
    pdf.add_code_eg(
        """pathobject.arcTo(x1,y1, x2,y2, startAng=0, extent=90) """
    )
    pdf.add_paragraph(
        '$arc$和$arcTo$方法可以绘制部分椭圆。'
        '$arc$方法首先 "提起画笔 "并开始一个新的形状序列。'
        '而$arcTo$方法则是将部分椭圆的起始点与当前的形状序列用线连接起来 。'
        '在画部分椭圆之前，先画出部分椭圆的线段 。'
        '点^(x1,y1)^和^(x2,y2)^定义包围椭圆的矩形的相对角点。'
        '$startAng$是一个角度(度数)，指定了部分椭圆的开始位置，其中0角是右边界的中点。'
        '围成的矩形（当^(x1,y1)^为左下角，^(x2,y2)^为右上角）。'
        '$extent$是指与椭圆上的横移。'
    )
    pdf.add_code_eg(doc_examples.testarcs)
    pdf.add_paragraph("上面的$arcs$函数行使了两种局部椭圆方法。它产生了下面的图形。")
    pdf.add_illustration(doc_examples.arcs, "弧线")
    pdf.add_code_eg("""pathobject.rect(x, y, width, height) """)
    pdf.add_paragraph("$rect$方法在^(x,y)^指定的^width^和^height^处画一个左下角的矩形。")
    pdf.add_code_eg("""pathobject.ellipse(x, y, width, height)""")
    pdf.add_paragraph(
        "$ellipse$方法在指定的^width^和^height^的^(x,y)^处绘制一个左下角的矩形包围的椭圆。"
    )
    pdf.add_code_eg("""pathobject.circle(x_cen, y_cen, r) """)
    pdf.add_paragraph("$circle$方法画一个以^(x_cen，y_cen)^为中心，半径^r^的圆。")
    pdf.add_code_eg(doc_examples.testvariousshapes)
    pdf.add_paragraph("上面的$variousshapes$函数显示了一个放置在参考网格中的矩形、圆和椭圆。")
    pdf.add_illustration(doc_examples.variousshapes, "路径对象中的矩形、圆形、椭圆形。")
    pdf.add_code_eg("""pathobject.close() """)
    pdf.add_paragraph(
        "$close$方法通过从图形的最后一点到图形的起始点("
        "最近一次通过$moveTo$或$arc$或其他放置操作将画笔放置在纸上的点)画一条线段来关闭当前图形。"
    )
    pdf.add_code_eg(doc_examples.testclosingfigures)
    pdf.add_paragraph("$closingfigures$函数说明了闭合或不闭合图形的效果，包括一条线段和一个部分椭圆。")
    pdf.add_illustration(doc_examples.closingfigures, "闭合和不闭合的路径对象数字")
    pdf.add_paragraph("关闭或不关闭图形只影响图形的描边轮廓，而不影响图形的填充，如上图所示。")
    pdf.add_paragraph("关于使用路径对象绘图的更广泛的例子，请检查$hand$函数。")
    pdf.add_code_eg(doc_examples.testhand)
    pdf.add_paragraph(
        '在调试模式下(默认)，$hand$函数显示了用于构成图形的贝塞尔曲线的切线段。'
        '请注意，当线段对齐时，曲线平滑地连接在一起，但当线段不对齐时，曲线显示出一个 "尖锐的边缘"。'
    )
    pdf.add_illustration(doc_examples.hand, "手形图")
    pdf.add_paragraph(
        "在非调试模式下，$hand$函数只显示贝塞尔曲线。 如果设置了$fill$参数，则会使用当前的填充颜色填充图形。"
    )
    pdf.add_code_eg(doc_examples.testhand2)
    pdf.add_text_note('边框的 "描边 "画在它们重叠的内部填充物上。')
    pdf.add_illustration(doc_examples.hand2, "妙手回春")
    pdf.add_heading("进一步阅读: ReportLab图形库", level=2)
    pdf.add_paragraph(
        "到目前为止，我们所看到的图形是在相当低的水平上创建的。"
        "但应该注意的是，还有一种方法可以使用专用的高级<i>ReportLab图形库</i>创建更复杂的图形。"
    )
    pdf.add_paragraph(
        "它可以用来为不同的输出格式（矢量图和位图）如PDF、EPS、SVG、JPG和PNG等制作高质量的、独立于平台的、可重复使用的图形。"
    )
    pdf.add_paragraph(
        "本文档第11章<i>绘图</i>对其理念和功能进行了更详尽的描述，其中包含了现有组件的信息以及如何创建自定义组件。"
    )
    pdf.add_paragraph(
        "第11章还详细介绍了ReportLab图表包及其组件（标签、坐标轴、图例和不同类型的图表，如柱状图、折线图和饼状图），"
        "它直接建立在图形库上。"
    )


def chapter3_font(pdf):
    pdf.add_heading("字体和编码", level=1)
    pdf.add_paragraph(
        '本章包括字体、编码和亚洲语言功能。'
        '如果你只关心生成西欧语言的PDF，你可以只读下面的 "Unicode是默认的"部分，并在第一次阅读时跳过其余部分。'
        '我们希望随着时间的推移，这部分内容会有很大的增长。'
        '我们希望开源能让我们比其他工具更好地支持世界上更多的语言，'
        '我们欢迎在这方面的反馈和帮助。'
    )

    pdf.add_heading('Unicode 和 UTF8 作为默认编码', level=2)
    pdf.add_paragraph(
        '从$reportlab 2.0$版本('
        '2006年5月)开始，您提供给我们API的所有文本输入都应该是UTF8或$Python Unicode$对象。'
        '这适用于^canvas.drawString^和相关$API$的参数、表格单元格内容、绘图对象参数和段落源文本。'
    )
    pdf.add_paragraph('我们曾考虑过让输入编码可配置，甚至依赖于本地，但决定"显式比隐式好"。')
    pdf.add_paragraph(
        '这简化了我们以前做的许多关于希腊字母、符号等的事情。' '要显示任何字符，找出它的unicode码点，并确保你使用的字体能够显示它。'
    )
    pdf.add_paragraph(
        '如果您正在改编$ReportLab 1.x$应用程序，'
        '或者从其他包含单字节数据的源头读取数据 (例如 latin-1 或 WinAnsi)，'
        '您需要进行$Unicode$转换。Python编解码器包现在包含了所有常用编码的转换器，包括亚洲的编码。'
    )
    pdf.add_paragraph(
        '如果你的数据不是UTF8编码，那么一旦你输入一个非ASCII字符，'
        '你就会得到一个UnicodeDecodeError 。'
        '例如，下面这个代码段试图读取并打印一系列名字，包括一个带有法国口音的名字。'
        '^Marc -Andr/\u00e9 Lemburg^.  标准误差非常有用，它告诉你它不喜欢什么字符。'
    )
    pdf.add_code_eg(
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
    pdf.add_paragraph('最简单的解决方法就是将你的数据转换为unicode，并说明它来自哪个编码，就像这样。')
    pdf.add_code_eg(
        """
>>> for line in file('latin_input.txt','r'):
...     uniLine = unicode(line, 'latin-1')
...     c.drawString(100, y, uniLine.strip())
>>>
>>> c.save()
"""
    )
    pdf.add_heading("输出字体自动替换", level=2)
    pdf.add_paragraph(
        '在代码中还有很多地方，包括^rl_config.defaultEncoding^参数，'
        '以及传递给各种 $Font$ 构造函数的参数，这些参数都是指编码。'
        '在过去，当人们需要使用 $PDF$ 浏览设备支持的$Symbol$和$ZapfDingbats$字体的字形时，'
        '这些参数非常有用。'
        '默认情况下，标准字体（$Helvetica$、$Courier$、$Times Roman$）将提供$Latin-1$的字形。'
        '然而，如果我们的引擎检测到一个字体中没有的字符，它将尝试切换到$Symbol$或$ZapfDingbats$来显示这些字符。'
        '例如，如果你在对^drawString^的调用中包含了一对右面剪刀的$Unicode$字符，\\u2702(\u2702),'
        '你应该会看到它们(在^test_pdfgen_general.py/pdf^中有一个例子)。'
        '在你的代码中不需要切换字体。'
    )
    pdf.add_heading("使用非标准的 $Type 1$ 字体", level=2)
    pdf.add_paragraph(
        '正如前一章所讨论的那样，每份 $Acrobat Reader$ 都内置了14种标准字体。'
        '因此，$ReportLab PDF$ 库只需要通过名称来引用这些字体。'
        '如果您想使用其他字体，它们必须对您的代码可用，并将被嵌入到$PDF$文档中。'
    )
    pdf.add_paragraph(
        '您可以使用下面描述的机制在您的文档中包含任意字体。'
        '我们有一个名为^DarkGardenMK^的开源字体，'
        '我们可以将其用于测试和或文档目的(您也可以使用它)。'
        '它与ReportLab发行版捆绑在一起，在$reportlab/fonts$目录下。'
    )
    pdf.add_paragraph(
        '目前，字体嵌入依赖于$Adobe AFM("Adobe Font Metrics")$'
        '和$PFB("Printer Font Binary")$格式的字体描述文件。'
        '前者是一个$ASCII$文件，包含字体中的字符（"字形"）信息，如高度、宽度、边界框信息和其他 "$metrics$"(指标)，'
        '而后者是一个二进制文件，描述字体的形状。'
        '在$reportlab/fonts$目录下，'
        '包含了$"DarkGardenMK.afm"$和$"DarkGardenMK.pfb"$两个文件，'
        '这两个文件被用来作为一个例子字体。'
    )
    pdf.add_paragraph(
        '在下面的例子中，找到包含测试字体的文件夹，并用$pdfmetrics$模块注册它，以便将来使用，' '之后我们可以像其他标准字体一样使用它。'
    )
    pdf.add_code_eg(
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
    pdf.add_paragraph('请注意，参数 "$WinAnsiEncoding$"与输入无关，它是说字体文件内的哪一组字符将被激活并可用。')
    pdf.add_illustration(doc_examples.customfont1, "使用非常不标准的字体")
    pdf.add_paragraph(
        '字体的名称来自$AFM$文件的$FontName$字段。'
        '在上面的例子中，我们事先知道了这个名字，但是很多时候字体描述文件的名字是非常神秘的，'
        '那么你可能会想从$AFM$文件中自动检索到这个名字。'
        '当缺乏更复杂的方法时，你可以使用一些像这样简单的代码。'
    )
    pdf.add_code_eg(
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
    pdf.add_paragraph(
        '在<i>DarkGardenMK</i>的例子中，我们明确指定了要加载的字体描述文件的位置。'
        '一般来说，你会更倾向于将你的字体存储在一些规范的位置，并让嵌入机制知道它们。'
        '使用同样的配置机制，我们已经在本节开头看到了，我们可以为Type-1字体指定一个默认的搜索路径。'
    )
    pdf.add_paragraph(
        '不幸的是，目前还没有一个可靠的标准来规定这些位置（甚至在同一个平台上也没有），'
        '因此，你可能需要编辑$reportlab_settings.py$'
        '或者$~/.reportlab_settings$来修改$T1SearchPath$标识符的值，'
        '以包含额外的目录。'
        '我们自己的建议是在开发中使用^reportlab/fonts^文件夹；并且在任何受控服务器部署中，将任何需要的字体作为应用程序的打包部件。'
        '这样可以避免字体被其他软件或系统管理员安装和卸载。'
    )
    pdf.add_heading("关于缺失字形的警告", level=3)
    pdf.add_paragraph(
        '如果你指定了一个编码，一般会认为字体设计师已经提供了所有需要的字形。'
        '然而，事实并非总是如此。'
        '在我们的示例字体中，字母表中的字母都存在，但许多符号和重音都没有。'
        '默认的行为是，当传递给字体一个它无法绘制的字符时，字体会打印一个 "notdef "字符'
        '--通常是一个blob、点或空格。'
        '然而，你可以要求库警告你；'
        '下面的代码（在加载字体之前执行）将导致在你注册字体时，对任何不在字体中的字形产生警告。'
    )
    pdf.add_code_eg(
        """
    import reportlab.rl_config
    reportlab.rl_config.warnOnMissingFontGlyphs = 0
    """
    )
    pdf.add_heading("标准的单字节字体编码", level=2)
    pdf.add_paragraph('本节为您展示常用编码中可用的字形。')
    pdf.add_paragraph(
        '下面的代码表显示了$WinAnsiEncoding$中的字符，'
        '这是Windows和许多美国和西欧Unix系统的标准编码。'
        '这是在美国和西欧的Windows和许多Unix系统上的标准编码，也被称为$Code Page 1252$，'
        '实际上与$ISO-Latin-1$相同（包含一个或两个额外的字符）。'
        '这是$Reportlab PDF$库使用的默认编码。'
        '它由$reportlab/lib$中的一个标准例程$codecharts.py$生成，'
        '可用于显示字体的内容。 沿边的索引号是以十六进制表示的。'
    )
    cht1 = SingleByteEncodingChart(
        encodingName='WinAnsiEncoding', charsPerRow=32, boxSize=12
    )
    pdf.add_illustration(
        lambda canv: cht1.drawOn(canv, 0, 0),
        "WinAnsi Encoding",
        cht1.width,
        cht1.height,
    )
    pdf.add_paragraph(
        '下面的代码表显示了$MacRomanEncoding$中的字符，'
        '听起来，这是美国和西欧Macintosh电脑上的标准编码。'
        '和通常的非unicode编码一样，前128个码点（在本例中，最上面4行）是ASCII标准，'
        '并与上面的WinAnsi代码表一致；但下面4行不同。'
    )
    cht2 = SingleByteEncodingChart(
        encodingName='MacRomanEncoding', charsPerRow=32, boxSize=12
    )
    pdf.add_illustration(
        lambda canv: cht2.drawOn(canv, 0, 0),
        "MacRoman Encoding",
        cht2.width,
        cht2.height,
    )
    pdf.add_paragraph(
        '这两种编码适用于标准字体（Helvetica、Times-Roman和Courier及其变体），'
        '并将适用于大多数商业字体，包括Adobe的字体。'
        '然而，有些字体包含非文本字形，这个概念并不真正适用。'
        '例如，ZapfDingbats和Symbol可以被视为各自拥有自己的编码。'
    )

    cht3 = SingleByteEncodingChart(
        faceName='ZapfDingbats',
        encodingName='ZapfDingbatsEncoding',
        charsPerRow=32,
        boxSize=12,
    )
    pdf.add_illustration(
        lambda canv: cht3.drawOn(canv, 0, 0),
        "ZapfDingbats和它的唯一编码。",
        cht3.width,
        cht3.height,
    )
    cht4 = SingleByteEncodingChart(
        faceName='Symbol',
        encodingName='SymbolEncoding',
        charsPerRow=32,
        boxSize=12,
    )
    pdf.add_illustration(
        lambda canv: cht4.drawOn(canv, 0, 0),
        "$Symbol$及其唯一的编码",
        cht4.width,
        cht4.height,
    )
    pdf.add_cond_page_break(5)

    pdf.add_heading("支持TrueType字体", level=2)
    pdf.add_paragraph(
        'Marius Gedminas ($mgedmin@delfi.lt$)'
        '在$Viktorija Zaksiene$($vika@pov.lt$)的帮助下，为嵌入式TrueType字体提供了支持。'
        'TrueType字体可以在Unicode/UTF8中使用，并且不限于256个字符。'
    )
    pdf.add_cond_page_break(3)
    pdf.add_paragraph(
        '我们使用<b>$reportlab.pdfbase.ttfonts.TTFont$</b>来创建一个真正的字体对象，'
        '并使用<b>$reportlab.pdfbase.pdfmetrics.registerFont$</b>进行注册。'
        '在pdfgen直接在画布上绘图时我们可以这样做'
    )
    pdf.add_code_eg(
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
    pdf.add_illustration(doc_examples.ttffont1, "使用$Vera TrueType$字体")
    pdf.add_paragraph('在上面的例子中，$True Type$字体对象是使用')
    pdf.add_code_eg(
        """
        TTFont(name,filename)
    """
    )
    pdf.add_paragraph(
        '所以ReportLab的内部名称由第一个参数给出，'
        '第二个参数是一个字符串（或类似文件的对象），表示字体的TTF文件。'
        '在Marius最初的补丁中，文件名应该是完全正确的，'
        '但我们已经修改了，如果文件名是相对的，'
        '那么在当前目录下搜索相应的文件，'
        '然后在$reportlab.rl_config.TTFSearchpath$!'
    )

    pdf.add_paragraph(
        '在使用Platypus中的TT字体之前，'
        '我们应该在$&lt;b&gt;$和$&lt;i&gt;$'
        '属性下添加一个从家族名称到描述行为的单个字体名称的映射。'
    )
    pdf.add_code_eg(
        """
    from reportlab.pdfbase.pdfmetrics import registerFontFamily
    registerFontFamily('Vera',normal='Vera',bold='VeraBd',italic='VeraIt',
    boldItalic='VeraBI')
    """
    )
    pdf.add_paragraph(
        '如果我们只有一个Vera常规字体，没有粗体或斜体，那么我们必须将所有字体映射到同一个内部字体名。'
        '^&lt;b&gt;^和^&lt;i&gt;^标签现在可以安全使用，但没有效果。'
        '如上所述注册和映射Vera字体后，我们可以使用段落文本，如'
    )
    # 注册一下字体，后面会用到，这个字体是Reportlab包自带的
    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
    pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
    registerFontFamily(
        'Vera',
        normal='Vera',
        bold='VeraBd',
        italic='VeraIt',
        boldItalic='VeraBI',
    )
    pdf.add_para_box2(
        """<font name="Times-Roman" size="14">This is in Times-Roman</font>
<font name="Vera" color="magenta" size="14">and this is in magenta 
<b>Vera!</b></font>""",
        "Using TTF fonts in paragraphs",
    )
    pdf.add_heading("亚洲字体支持", level=2)
    pdf.add_paragraph(
        'Reportlab PDF库旨在为亚洲字体提供全面支持。'
        'PDF是第一个真正可移植的亚洲文本处理解决方案。'
        '有两种主要的方法。 Adobe的亚洲语言包，或者TrueType字体。'
    )
    pdf.add_heading("亚洲语言包", level=3)
    pdf.add_paragraph('这种方法提供了最好的性能，因为没有任何东西需要嵌入到PDF文件中；与标准字体一样，一切都在阅读器上。')
    pdf.add_paragraph(
        'Adobe公司为每种主要语言都提供了附加组件。'
        '在$Adobe Reader 6.0$和7.0中，当您尝试使用它们打开文档时，您会被提示下载并安装这些插件。'
        '在早期的版本中，你会在打开亚洲文档时看到一个错误信息，你必须知道该怎么做。'
    )
    pdf.add_paragraph('日文、繁体中文(台湾/香港)、简体中文(中国大陆)和韩文都支持，我们的软件知道以下字体。')
    pdf.add_bullet("$chs$ = Chinese Simplified (mainland): '$SourceHanSansSC$'")
    pdf.add_bullet(
        "$cht$ = Chinese Traditional (Taiwan): '$MSung-Light$', '$MHei-Medium$'"
    )
    pdf.add_bullet(
        "$kor$ = Korean: '$HYSMyeongJoStd-Medium$','$HYGothic-Medium$'"
    )
    pdf.add_bullet("$jpn$ = Japanese: '$HeiseiMin-W3$', '$HeiseiKakuGo-W5$'")
    pdf.add_paragraph(
        '由于许多用户不会安装字体包，我们已经包含了一些日文字符的相当颗粒状的^bitmap^。 下面我们将讨论生成它们所需要的内容。'
    )

    pdf.add_image(os.path.join(BASE_DIR, "images", 'jpnchars.jpg'))
    pdf.add_paragraph(
        '在2.0版本之前，当你注册一个$CIDFont$时，'
        '你必须指定许多本地编码之一。在2.0版本中，你应该使用一个新的^UnicodeCIDFont^类。'
    )
    pdf.add_code_eg(
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
    pdf.add_paragraph(
        '旧的编码风格与显式编码应该仍然有效，但现在只有当你需要构建垂直文本时才有意义。'
        '我们的目标是在未来为UnicodeCIDFont构造函数添加更多可读的水平和垂直文本选项。'
        '以下四个测试脚本会生成相应语言的样本。'
    )

    pdf.add_code_eg(
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

    pdf.add_paragraph(
        '在以前版本的$ReportLab PDF$库中，'
        '我们不得不使用Adobe的CMap文件（如果安装了亚洲语言包，则位于$Acrobat Reader$附近）。'
        '现在我们只需要处理一种编码，字符宽度数据被嵌入到软件包中，生成时不需要CMap文件。'
        '在^rl_config.py^中的CMap搜索路径现在已经被废弃，'
        '如果你限制自己使用$UnicodeCIDFont$，则没有效果。'
    )
    pdf.add_heading("TrueType字体和亚洲字符", level=3)
    pdf.add_paragraph(
        '这就是简单的方法。'
        '在使用亚洲$TrueType$字体时，完全不需要特殊的处理。'
        '例如，在控制面板中安装了日语作为选项的Windows用户，'
        '会有一个可以使用的字体 "$msmincho.ttf$"。'
        '然而，请注意，解析字体需要时间，而且相当大的子集可能需要嵌入你的PDF中。'
        '我们现在也可以解析以$.ttc$结尾的文件，它们是$.ttf$的轻微变化。'
    )
    pdf.add_heading("To Do", level=3)

    pdf.add_paragraph(
        '我们预计将在一段时间内开发这个领域的包.accept2dyear这是一个主要优先事项的大纲。 我们欢迎大家的帮助'
    )
    pdf.add_bullet('确保我们在横写和竖写中的所有编码都有准确的字符指标。')
    pdf.add_bullet('为^UnicodeCIDFont^添加选项，在字体允许的情况下，允许垂直和比例变体。')
    pdf.add_bullet('改进段落中的包字代码，允许竖写。')
    pdf.add_cond_page_break(5)
    pdf.add_heading("RenderPM 测试", level=2)
    pdf.add_paragraph(
        '这可能也是提及$reportlab/graphics/renderPM.py$的测试函数的最好地方，'
        '它可以被认为是行使renderPM'
        '("$PixMap Renderer$"，相对于renderPDF、renderPS或renderSVG)的测试的规范地方。'
    )
    pdf.add_paragraph('如果你从命令行运行这个，你应该会看到很多像下面这样的输出。')
    pdf.add_code_eg(
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
    pdf.add_paragraph(
        '它运行了许多测试，'
        '从 "Hello World"测试开始，到各种测试，'
        '包括：线条；各种尺寸、字体、颜色和对齐方式的文本字符串；'
        '基本形状；转换和旋转组；缩放坐标；'
        '旋转字符串；嵌套组；锚定和非标准字体。'
    )
    pdf.add_paragraph(
        '它创建了一个名为$pmout$的子目录，将图片文件写入其中，并写了一个$index.html$的页面，便于参考所有结果。'
    )
    pdf.add_paragraph("与字体相关的测试，你可能会想看看#11（'非标准字体中的文本字符串'）和#12（'测试各种字体'）。")


def chapter4_special_features(pdf):
    pdf.add_heading("PDF的特殊功能", level=1)
    pdf.add_paragraph("PDF提供了许多功能，使电子文档的浏览更加高效和舒适，我们的类库就公开了其中的一些功能。")

    pdf.add_heading("表单", level=2)
    pdf.add_paragraph(
        "表单功能使您可以在PDF文件开头附近创建一个图形和文本块，然后在后续页面中简单地引用它。 "
        "如果要处理5000种重复的业务表单（例如一页发票或工资单），"
        "则只需将背景存储一次，并在每页上简单地绘制变化的文本即可。 "
        "正确使用表格可以极大地减少文件大小和生产时间，"
        "并且显然甚至可以加快打印机上的处理速度。"
    )
    pdf.add_paragraph('表单不需要引用整个页面； 任何可能经常重复的内容都应以表格的形式放置。')
    pdf.add_paragraph('下面的示例显示了使用的基本顺序。 真正的程序可能会预先定义表单，然后从另一个位置引用它们。')
    pdf.add_code_eg(doc_examples.testforms)
    pdf.add_heading("链接和目的地(书签)", level=2)
    pdf.add_paragraph(
        "PDF支持内部超链接。 单击可以触发多种链接类型，目标类型和事件。"
        "目前，我们仅支持从文档的一个部分跳转到另一部分并在跳转后控制窗口的缩放级别的基本功能。"
        "^bookmarkPage^方法定义一个目标，该目标是跳转的终点。"
    )
    pdf.add_code_eg(
        """
        canvas.bookmarkPage(name, fit="Fit", left=None,
            top=None, bottom=None, right=None, zoom=None
        )
    """
    )
    pdf.add_paragraph(
        "默认情况下，$ bookmarkPage $方法将页面本身定义为目标。"
        "跳转到由^bookmarkPage^定义的端点之后，PDF浏览器将显示整个页面，并将其缩放以适合屏幕大小："
    )
    pdf.add_code_eg("""canvas.bookmarkPage(name)""")
    pdf.add_paragraph("通过提供一个$fit$参数，$bookmarkPage$方法可以用多种不同的方式显示页面。")

    table = Table(
        [
            ['fit', '必传参数', '描述'],
            [
                'Fit',
                None,
                '自适应窗口 (默认)\nEntire page fits in window (the default)',
            ],
            [
                'FitH',
                'top',
                '坐标在窗口上方, 自适应宽度\n'
                'Top coord at top of window, width scaled to fit',
            ],
            [
                'FitV',
                'left',
                '坐标在窗口左边, 自适应高度\n'
                'Left coord at left of window, height scaled to fit',
            ],
            [
                'FitR',
                'left bottom right top',
                '缩放窗口以适应指定的矩形\n' 'Scale window to fit the specified rectangle',
            ],
            [
                'XYZ',
                'left top zoom',
                '细致的控制。如果您省略了一个参数，PDF浏览器会将其解释为 "保持原样"。\n'
                'Fine grained control. If you omit a parameter\n'
                'the PDF browser interprets it as "leave as is"',
            ],
        ]
    )
    table.setStyle(
        TableStyle(
            [
                ('FONT', (0, 0), (-1, -6), 'SourceHanSans-Normal', 10, 12),
                ('FONT', (0, 1), (-1, -1), 'SourceHanSans-ExtraLight', 10, 12),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            ]
        )
    )
    pdf.add_paragraph("")  # 增加一个空行
    pdf.add_flowable(table)
    pdf.add_caption('配合不同类型所需的属性', category=constant.CAPTION_TABLE)
    pdf.add_pencil_note()
    pdf.add_text_note("$fit$的设置是区分大小写的，所以$fit=\"FIT\"$是无效的。")
    pdf.add_paragraph(
        '有时你希望跳转的目标是一个页面的某个部分。$fit="FitR"$允许你确定一个特定的矩形，缩放区域以适合整个页面。'
    )
    pdf.add_paragraph('要将显示设置为页面的特定x和y坐标，并直接使用fit="XYZ"控制缩放。')
    pdf.add_code_eg(
        "canvas.bookmarkPage('my_bookmark',fit=\"XYZ\",left=0,top=200)"
    )
    pdf.add_paragraph(
        '这个目标位于页面的最左边，屏幕顶部的位置是200。因为没有设置$zoom$，所以无论用户设置成什么样子，缩放都会保持在这个位置。'
    )
    pdf.add_code_eg(
        "canvas.bookmarkPage('my_bookmark',fit=\"XYZ\",left=0,top=200,zoom=2)"
    )
    pdf.add_paragraph('这次的缩放设置为将页面扩大2倍其正常大小。')
    pdf.add_pencil_note()
    pdf.add_text_note(
        '$XYZ$和$FitR$的拟合类型都需要用默认的用户空间来指定它们的位置参数($top, bottom, left, right$)。'
        '它们会忽略画布图形状态下的任何几何变换。'
    )
    pdf.add_paragraph(
        '之前有两个书签方法是支持的，但由于^bookmarkPage^的通用性，现在已经废弃了。'
        '这两个方法是$bookmarkHorizontalAbsolute$和$bookmarkHorizontal$。'
    )

    pdf.add_heading("定义内部链接", level=3)
    pdf.add_code_eg(
        """
    canvas.linkAbsolute(contents, destinationname, Rect=None, addtopage=1, 
        name=None, thickness=0, color=None, dashArray=None, **kw)
     """
    )

    pdf.add_paragraph(
        '$linkAbsolute$方法定义了一个跳跃的起点。'
        '当用户使用动态查看器(如Acrobat Reader)浏览生成的文档时，当鼠标在$Rect$指定的矩形内点击时，'
        '查看器将跳转到与$destinationname$相关联的端点。'
        '如同$bookmarkHorizontalAbsolute$一样，矩形$Rect$必须用默认的用户空间来指定。'
        '参数$contents$指定了当用户左键点击该区域时在查看器中显示的文本块。'
    )
    pdf.add_paragraph('矩形$Rect$必须用元组^(x1,y1,x2,y2)^来指定，以确定在默认用户空间中矩形的左下角和右上角。')
    pdf.add_paragraph("示例代码")
    pdf.add_code_eg('canvas.bookmarkPage("Meaning_of_life")')
    pdf.add_paragraph(
        '定义了一个位置，作为当前页面的整个标识符$Meaning_of_life$ 。'
        '为了在绘制一个可能不同的页面时创建一个矩形链接到它，我们将使用以下代码。'
    )
    pdf.add_code_eg(
        """
 canvas.linkAbsolute("Find the Meaning of Life", "Meaning_of_life",
                     (inch, inch, 6*inch, 2*inch))
"""
    )
    pdf.add_paragraph(
        "默认情况下，在交互式浏览时，链接周围会出现一个矩形。"
        "使用关键字参数$Border='[0 0 0]'$来抑制查看链接时周围可见的矩形。"
        "例如"
    )
    pdf.add_code_eg(
        """
     canvas.linkAbsolute("Meaning of Life", "Meaning_of_life",
                         (inch, inch, 6*inch, 2*inch), Border='[0 0 0]')
    """
    )
    pdf.add_paragraph(
        '如果没有指定Border参数，$thickness$、$color$和$dashArray$参数可以交替使用来指定边框。'
        '如果指定了Border参数，它必须是一个PDF数组的字符串表示，'
        '或者是一个$PDFArray$(参见pdfdoc模块)。'
        '$color$参数(应该是一个$Color$实例)相当于一个关键字参数$C$，'
        '它应该解析为一个PDF颜色定义(通常是一个三条PDF数组)。'
    )
    pdf.add_paragraph(
        '$canvas.linkRect$方法的意图与$linkAbsolute$方法类似，'
        '但多了一个参数$relative=1$，所以打算服从本地用户空间转换。'
    )

    pdf.add_heading("大纲", level=2)
    pdf.add_paragraph(
        '$Acrobat Reader$有一个导航页，它可以容纳一个文档大纲；'
        '当您打开本指南时，它通常应该是可见的。'
        '我们提供一些简单的方法来添加大纲条目。'
        '通常情况下，一个制作文档的程序（如本用户指南）在到达文档中的每个标题时，'
        '会调用方法'
        '$canvas.addOutlineEntry(^self, title, key, level=0, closed=None^)$。'
    )
    pdf.add_paragraph(
        '^title^是将显示在左侧窗格的标题。'
        '^key^必须是一个字符串，它在文档中是唯一的，并且和超链接一样，可以命名一个书签。'
        '除非另有说明，否则^level^是0'
        '--最上层，而且一次下行超过一层是错误的(例如，在0层标题后加上2层标题)。'
        '最后，^closed^参数指定大纲窗格中的节点是默认关闭还是打开。'
    )
    pdf.add_paragraph(
        '下面的片段来自于格式化本用户指南的文档模板 。'
        '中央处理器依次查看每个段落，当出现新的章节时，'
        '就会做出一个新的大纲条目，将章节标题文本作为标题文本 。'
        '键是从章节号中获得的（这里没有显示），所以第2章的键为 "ch2" 。'
        '大纲入口指向的书签是针对整页的，但它也可以很容易地成为一个单独的段落。'
    )
    pdf.add_code_eg(
        """
    #abridged code from our document template
    if paragraph.style == 'Heading1':
        self.chapter = paragraph.getPlainText()
        key = 'ch%d' % self.chapterNo
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(paragraph.getPlainText(),
                                                key, 0, 0)
        """
    )
    pdf.add_heading("页面过渡效果", level=2)
    pdf.add_code_eg(
        """
     canvas.setPageTransition(self, effectname=None, duration=1,
                            direction=0,dimension='H',motion='I')
                            """
    )
    pdf.add_paragraph(
        '$setPageTransition$方法指定了一个页面如何被下一个页面替换 。'
        '例如，通过将页面转换效果设置为 "溶解"，当当前页面在交互式浏览过程中被下一个页面所取代时，它将显示为融化 。'
        '这些效果在美化幻灯片演示等地方很有用。关于如何使用此方法，请参阅参考手册。'
    )
    pdf.add_heading("内部文件注释", level=2)
    pdf.add_code_eg(
        """
     canvas.setAuthor(name)
     canvas.setTitle(title)
     canvas.setSubject(subj)
     """
    )
    pdf.add_paragraph(
        '这些方法对文档没有自动可见的效果。'
        '它们向文件添加内部注释 。'
        '这些注释可以使用浏览器的 "文档信息 "菜单项来查看，'
        '它们也可以作为一种简单的标准方式，向不需要解析整个文件的归档软件提供有关文件的基本信息 。'
        '要找到注释，请使用标准文本编辑器'
        '（如MS/Windows上的$notepad$或unix上的$vi$或$emacs$）'
        '查看$*.pdf$输出文件，'
        '并在文件内容中查找字符串$/Author$。'
    )
    pdf.add_code_eg(doc_examples.testannotations)
    pdf.add_paragraph('如果您想让主题、标题和作者在查看和打印时自动显示在文档中，您必须像其他文本一样将它们绘制到文档中。')
    pdf.add_illustration(doc_examples.annotations, "设置文档内部注释")
    pdf.add_heading("加密", level=2)
    pdf.add_heading("关于加密PDF文件", level=3)
    pdf.add_paragraph('Adobe的PDF标准允许你在对一个PDF文件进行加密时做三件相关的事情。')
    pdf.add_bullet('对其进行密码保护，所以用户必须提供有效的密码才能够读取它。')
    pdf.add_bullet('对文件的内容进行加密，使其在解密前毫无用处，并对文件进行加密。')
    pdf.add_bullet('控制用户在查看文档时是否可以打印、复制、粘贴或修改文档。')
    pdf.add_paragraph('PDF安全处理程序允许为一个文档指定两个不同的密码。')
    pdf.add_bullet('所有者 "密码"（也就是 "安全密码 "或 "主密码"）。')
    pdf.add_bullet('用户 "密码"（也就是 "打开密码"）。')
    pdf.add_paragraph('当用户提供其中一个密码时，PDF文件将被打开、解密并显示在屏幕上。')
    pdf.add_paragraph(
        '如果提供了所有者密码，那么文件的打开就有了完全的控制权' '--你可以对它做任何事情，包括改变安全设置和密码，或者用新密码重新加密。'
    )
    pdf.add_paragraph(
        '如果用户密码是提供的密码，你就在一个更受限制的模式下打开它。' '这些限制是在文件加密时设置的，将允许或拒绝用户进行以下操作的权限。'
    )
    pdf.add_bullet('修改文件的内容')
    pdf.add_bullet('从文档中复制文本和图形')
    pdf.add_bullet('添加或修改文本注释和交互式表格字段。')
    pdf.add_bullet('打印文件')
    pdf.add_paragraph(
        '请注意，所有受密码保护的PDF文件都是加密的，但并不是所有加密的PDF都受密码保护。'
        '如果一个文件的用户密码是一个空字符串，当打开文件时将不会有密码提示。'
        '如果只用所有者密码来保护文档，那么打开文件时也不会有密码提示。'
        '如果在对PDF文件进行加密时，将所有者和用户密码设置为同一字符串，则该文件将始终以用户访问权限打开。'
        '这就意味着，可以创建一个文件，比如说，任何人都不可能打印出来，即使是创建该文件的人。'
    )
    table = Table(
        [
            ['所有者密码\n已设置?', '用户密码\n已设置?', '结果'],
            [
                '是',
                '-',
                '打开文件时无需密码。适用于所有人。\n'
                'No password required when opening file.\n'
                'Restrictions apply to everyone.',
            ],
            [
                '-',
                '是',
                '打开文件时需要用户密码。适用于所有人。\n'
                'User password required when opening file. \n'
                'Restrictions apply to everyone.',
            ],
            [
                '是',
                '是',
                '打开文件时需要一个密码。\n只有在提供用户密码的情况下才有限制。\n'
                'A password required when opening file. \n'
                'Restrictions apply only if user password supplied.',
            ],
        ],
        [90, 90, 260],
    )
    table.setStyle(
        TableStyle(
            [
                ('FONT', (0, 0), (-1, -4), 'SourceHanSans-Normal', 10, 12),
                ('FONT', (0, 1), (-1, -1), 'SourceHanSans-ExtraLight', 10, 12),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            ]
        )
    )
    pdf.add_paragraph("")
    pdf.add_flowable(table)
    pdf.add_caption("PDF加密方式", category=constant.CAPTION_TABLE)
    pdf.add_paragraph(
        '当一个PDF文件被加密时，加密将应用于文件中的所有字符串和流。'
        '这可以防止没有密码的人简单地从PDF文件中删除密码以获得访问权'
        ' - 它使文件无用，除非你真的有密码。'
    )
    pdf.add_paragraph(
        'PDF 的标准加密方法使用 MD5 消息摘要算法'
        '（如 RFC 1321，MD5 消息摘要算法中所述）和一种称为 RC4 的加密算法。'
        'RC4是一种对称流加密算法'
        '--加密和解密都使用相同的算法，而且该算法不会改变数据的长度。'
    )
    pdf.add_heading("如何使用加密技术", level=3)
    pdf.add_paragraph('文档可以通过向画布对象传递一个参数来加密。')
    pdf.add_paragraph('如果参数是一个字符串对象，它被用作PDF的用户密码。')
    pdf.add_paragraph(
        '参数也可以是$reportlab.lib.pdfencrypt.StandardEncryption$类的实例，'
        '它允许对加密设置进行更精细的控制。'
    )
    pdf.add_paragraph('$StandardEncryption$构造函数接受以下参数。')
    pdf.add_code_eg(
        """
    def __init__(self, userPassword,
        ownerPassword=None,
        canPrint=1,
        canModify=1,
        canCopy=1,
        canAnnotate=1,
        strength=40):
    """
    )
    pdf.add_paragraph('$userPassword$和$ownerPassword$参数在加密的PDF上设置了相关密码。')
    pdf.add_paragraph(
        '布尔标志$canPrint$,$canModify$,$canCopy$,$canAnnotate$决定了'
        '当只有用户密码被提供时，用户是否可以在PDF上执行相应的操作。'
    )
    pdf.add_paragraph('如果用户在打开PDF时提供了所有者密码，则无论标志如何，所有的操作都可以执行。')

    pdf.add_heading("示例", level=3)
    pdf.add_paragraph("要创建一个名为hello.pdf的文档，用户密码为'rptlab'，不允许打印，可以用以下代码。")
    pdf.add_code_eg(
        """
    from reportlab.pdfgen import canvas
    from reportlab.lib import pdfencrypt
    
    enc=pdfencrypt.StandardEncryption("rptlab",canPrint=0)
    
    def hello(c):
        c.drawString(100,100,"Hello World")
    c = canvas.Canvas("hello.pdf",encrypt=enc)
    hello(c)
    c.showPage()
    c.save()
    
    """
    )
    pdf.add_heading("交互式表单", level=2)
    pdf.add_heading("交互式表格概述", level=3)
    pdf.add_paragraph(
        'PDF标准允许各种交互式元素，'
        'ReportLab工具包目前只支持一小部分的可能性，应该被认为是一项正在进行中的工作。'
        '目前我们允许使用^checkbox^、^radio^、^choice^和^listbox^部件进行选择；'
        '文本值可以使用^textfield^部件进行输入。'
        '所有的widget都是通过调用^canvas.acroform^属性上的方法创建的。'
    )
    pdf.add_heading("示例", level=3)
    pdf.add_paragraph('这显示了在当前页面上创建交互式元素的基本机制。')
    pdf.add_code_eg(
        """
    canvas.acroform.checkbox(
            name='CB0',
            tooltip='Field CB0',
            checked=True,
            x=72,y=72+4*36,
            buttonStyle='diamond',
            borderStyle='bevelled',
            borderWidth=2,
            borderColor=red,
            fillColor=green,
            textColor=blue,
            forceBorder=True)
    """
    )
    al_style = TableStyle(
        [
            ('SPAN', (0, 0), (-1, 0)),
            ('FONT', (0, 0), (-1, 0), 'SourceHanSans-Normal', 10, 12),
            ('FONT', (0, 1), (-1, 1), 'SourceHanSans-Normal', 9, 9.6),
            ('FONT', (0, 2), (0, -1), 'Courier', 8, 8.4),  # 参数列
            ('FONT', (1, 2), (1, -1), 'SourceHanSans-ExtraLight', 8, 8.4),
            ('FONT', (2, 2), (2, -1), 'SourceHanSans-ExtraLight', 8, 8.4),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('ALIGN', (1, 1), (1, 1), 'CENTER'),
            ('VALIGN', (0, 2), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
    pdf.add_text_note("^acroform^画布属性是根据需求自动创建的，而且一个文档中只允许有一个表单。")
    pdf.add_heading("复选框用法", level=3)
    pdf.add_paragraph(
        '^canvas.acroform.checkbox^方法在当前页面上创建了一个^checkbox^小部件。'
        '复选框的值是$YES$或$OFF$。参数为:'
    )
    table = Table(
        [
            ['canvas.acroform.checkbox 参数列表', '', ''],
            ['参数名', '描述', '默认值'],
            ["name", "表单参数名\nthe parameter's name", "None"],
            [
                "x",
                "在页面上的水平位置(绝对坐标)\n"
                "the horizontal position on the page (absolute coordinates)",
                "0",
            ],
            [
                "y",
                "在页面上的垂直位置(绝对坐标)\n"
                "the vertical position on the page (absolute coordinates)",
                "0",
            ],
            [
                "size",
                "轮廓尺寸：size x size\n" "The outline dimensions size x size",
                "20",
            ],
            [
                "checked",
                "如果为真，则该复选框被初始选中\n" "if True the checkbox is initially checked",
                "False",
            ],
            [
                "buttonStyle",
                "如果为真，则该复选框最初被选中，复选框样式（见下文）。\n"
                "the checkbox style (see below)",
                "'check'",
            ],
            [
                "shape",
                "小组件的轮廓（见下文）。\n" "The outline of the widget (see below)",
                "'square'",
            ],
            [
                "fillColor",
                "填充颜色\n" "colour to be used to fill the widget",
                "None",
            ],
            ["textColor", "符号的颜色\n" "the colour of the symbol or text", "None"],
            ["borderWidth", "边框宽度\nas it says", "1"],
            ["borderColor", "边框颜色\nthe widget's border colour", "None"],
            ["borderStyle", "边框样式\nThe border style name", "'solid'"],
            [
                "tooltip",
                "悬停在小组件上时要显示的文本。\n"
                "The text to display when hovering over the widget",
                "None",
            ],
            [
                "annotationFlags",
                "空白分隔的注解标志字符串\n" "blank separated string of annotation flags",
                "'print'",
            ],
            [
                "fieldFlags",
                "空白分隔的字段标志（见下文）。\n" "Blank separated field flags (see below)",
                "'required'",
            ],
            [
                "forceBorder",
                "为 True 的时候会强行画边框\n"
                "when true a border force a border to be drawn",
                "False",
            ],
            [
                "relative",
                "如果为 Tru，服从当前画布的变换\n"
                "if true obey the current canvas transform",
                "False",
            ],
            [
                "dashLen ",
                "如果 borderStyle=='dashed' ，要使用的折线。\n"
                "the dashline to be used if the borderStyle=='dashed'",
                "3",
            ],
        ],
        [90, 260, 90],
        style=al_style,
        repeatRows=2,
    )
    pdf.add_paragraph("")
    pdf.add_flowable(table)
    pdf.add_heading("单选框使用方法", level=3)
    pdf.add_paragraph(
        '^canvas.acroform.radio^方法在当前页面上创建一个radio小组件。'
        'radio的值是radio组选择的值，如果没有选择，则是$OFF$。参数是'
    )
    table = Table(
        [
            ['canvas.acroform.radio 参数列表', '', ''],
            ['参数名', '描述', '默认值'],
            [
                "name",
                "单选框组的名称(该参数)\nthe radio's group (ie parameter) name",
                "None",
            ],
            ["value", "单选框组的名称\nthe radio's group name", "None"],
            [
                "x",
                "在页面上的水平位置(绝对坐标)\n"
                "the horizontal position on the page (absolute coordinates)",
                "0",
            ],
            [
                "y",
                "在页面上的垂直位置(绝对坐标)\n"
                "the vertical position on the page (absolute coordinates)",
                "0",
            ],
            [
                "size",
                "轮廓尺寸，size x size\n" "The outline dimensions size x size",
                "20",
            ],
            [
                "selected",
                "如果为 'true'，则该单选机在其组中被选中。\n"
                "if True this radio is the selected "
                "one in its group",
                "False",
            ],
            [
                "buttonStyle",
                "按钮样式\nthe checkbox style (see below)",
                "'check'",
            ],
            [
                "shape",
                "小组件的轮廓（见下文）。\n" "The outline of the widget (see below)",
                "'square'",
            ],
            [
                "fillColor",
                "用来填充小组件的颜色\n" "colour to be used to fill the widget",
                "None",
            ],
            ["textColor", "符号的颜色\n" "the colour of the symbol or text", "None"],
            ["borderWidth", "边框宽度\n" "as it says", "1"],
            ["borderColor", "边框颜色\nthe widget's border colour", "None"],
            ["borderStyle", "边框样式\nThe border style name", "'solid'"],
            [
                "tooltip",
                "悬停在小组件上时要显示的文本。\n"
                "The text to display when hovering over the widget",
                "None",
            ],
            [
                "annotationFlags",
                "空白分隔的注解标志字符串\n" "blank separated string of annotation flags",
                "'print'",
            ],
            [
                "fieldFlags",
                "空白分隔的字段标志（见下文）。\n" "Blank separated field flags (see below)",
                "'noToggleToOff required radio'",
            ],
            [
                "forceBorder",
                "当真的时候会强行画边框\n" "when true a border force a border to be drawn",
                "False",
            ],
            [
                "relative",
                "如果为true，则遵循当前的画布转换\n"
                "if true obey the current canvas transform",
                "False",
            ],
            [
                "dashLen ",
                "如果borderStyle=='dashed'，要使用的折线。\n"
                "the dashline to be used if the borderStyle=='dashed'",
                "3",
            ],
        ],
        [90, 240, 110],
        style=al_style,
        repeatRows=2,
    )
    pdf.add_paragraph("")
    pdf.add_flowable(table)

    pdf.add_heading("列表框用法", level=3)
    pdf.add_paragraph(
        '^canvas.acroform.listbox^方法在当前页面上创建了一个^listbox^小组件。'
        'listbox包含一个选项列表，其中一个或多个选项（取决于$fieldFlags$）可以被选中。'
    )
    table = Table(
        [
            ['canvas.acroform.listbox 参数列表', '', ''],
            ['参数', '描述', '默认值'],
            ["name", "组名\nthe radio's group (ie parameter) name", "None"],
            [
                "options",
                "可用选项的列表或元组\nList or tuple of avaiable options",
                "[]",
            ],
            [
                "value",
                "单个或选定选项的字符串列表。\n"
                "Singleton or list of strings of selected options",
                "[]",
            ],
            [
                "x",
                "在页面上的水平位置(绝对坐标)\n"
                "the horizontal position on the page (absolute coordinates)",
                "0",
            ],
            [
                "y",
                "在页面上的垂直位置(绝对坐标)\n"
                "the vertical position on the page (absolute coordinates)",
                "0",
            ],
            ["width", "小组件宽度\nThe widget width", "120"],
            ["height", "小组件高度\nThe widget height", "36"],
            [
                "fontName",
                "要使用的第1种字体的名称。\nThe name of the type 1 font to be used",
                "'Helvetica'",
            ],
            ["fontSize", "要使用的字体大小\nThe size of font to be used", "12"],
            [
                "fillColor",
                "用来填充小组件的颜色\ncolour to be used to fill the widget",
                "None",
            ],
            ["textColor", "符号或文本的颜色\nthe colour of the symbol or text", "None"],
            ["borderWidth", "边框宽度\nas it says", "1"],
            ["borderColor", "边框颜色\nthe widget's border colour", "None"],
            ["borderStyle", "边框样式\nThe border style name", "'solid'"],
            [
                "tooltip",
                "悬停在小组件上时要显示的文本。\n"
                "The text to display when hovering over the widget",
                "None",
            ],
            [
                "annotationFlags",
                "空白分隔的注解标志字符串\nblank separated string of annotation flags",
                "'print'",
            ],
            [
                "fieldFlags",
                "空白分隔的字段标志（见下文）。\nBlank separated field flags (see below)",
                "''",
            ],
            [
                "forceBorder",
                "当真的时候会强行画边框\nwhen true a border force a border to be drawn",
                "False",
            ],
            [
                "relative",
                "如果为真，服从当前画布的变换\nif true obey the current canvas transform",
                "False",
            ],
            [
                "dashLen ",
                "如果borderStyle=='dashed'，要使用的折线。\n"
                "the dashline to be used if the borderStyle=='dashed'",
                "3",
            ],
        ],
        [90, 260, 90],
        style=al_style,
        repeatRows=2,
    )
    pdf.add_paragraph("")
    pdf.add_flowable(table)

    pdf.add_heading("下拉菜单的使用", level=3)
    pdf.add_paragraph(
        '^canvas.acroform.choice^方法在当前页面上创建了一个^dropdown^小部件。'
        '下拉菜单包含一个选项列表，其中一个或多个选项（取决于fieldFlags）可以被选中。'
        '如果您在^fieldFlags^中添加^edit^，那么结果可以被编辑。'
    )
    table = Table(
        [
            ['canvas.acroform.choice 参数列表', '', ''],
            ['参数', '描述', '默认值'],
            ["name", "组名\nthe radio's group (ie parameter) name", "None"],
            ["options", "可用选项的列表或元组\nList or tuple of available options", "[]"],
            [
                "value",
                "单个或选定选项的字符串列表。\n"
                "Singleton or list of strings of selected options",
                "[]",
            ],
            [
                "x",
                "在页面上的水平位置(绝对坐标)\n"
                "the horizontal position on the page (absolute coordinates)",
                "0",
            ],
            [
                "y",
                "在页面上的垂直位置(绝对坐标)\n"
                "the vertical position on the page (absolute coordinates)",
                "0",
            ],
            ["width", "小组件宽度\nThe widget width", "120"],
            ["height", "小组件高度\nThe widget height", "36"],
            [
                "fontName",
                "要使用的第1种字体的名称。\n" "The name of the type 1 font to be used",
                "'Helvetica'",
            ],
            ["fontSize", "要使用的字体大小\nThe size of font to be used", "12"],
            [
                "fillColor",
                "用来填充小组件的颜色\ncolour to be used to fill the widget",
                "None",
            ],
            ["textColor", "符号的颜色\nthe colour of the symbol or text", "None"],
            ["borderWidth", "边框宽度\nas it says", "1"],
            ["borderColor", "边框颜色\nthe widget's border colour", "None"],
            ["borderStyle", "边框样式\nThe border style name", "'solid'"],
            [
                "tooltip",
                "悬停在小组件上时要显示的文本。\n"
                "The text to display when hovering over the widget",
                "None",
            ],
            [
                "annotationFlags",
                "空白分隔的注解标志字符串\nblank separated string of annotation flags",
                "'print'",
            ],
            [
                "fieldFlags",
                "空白分隔的字段标志（见下文）。\nBlank separated field flags (see below)",
                "'combo'",
            ],
            [
                "forceBorder",
                "当真的时候会强行画边框\nwhen true a border force a border to be drawn",
                "False",
            ],
            [
                "relative",
                "如果为真，服从当前画布的变换\nif true obey the current canvas transform",
                "False",
            ],
            [
                "dashLen ",
                "如果borderStyle=='dashed'，要使用的破折号。\n"
                "the dashline to be used if the borderStyle=='dashed'",
                "3",
            ],
            [
                "maxlen ",
                "无或小组件值的最大长度\nNone or maximum length of the widget value",
                "None",
            ],
        ],
        [90, 260, 90],
        style=al_style,
        repeatRows=2,
    )
    pdf.add_paragraph("")
    pdf.add_flowable(table)

    pdf.add_heading("文本字段用法", level=3)
    pdf.add_paragraph(
        '^canvas.acroform.textfield^方法在当前页面上创建了一个^textfield^条目部件。'
        '文本字段可以被编辑，以改变小组件的值。'
    )
    table = Table(
        [
            ['canvas.acroform.textfield 参数列表', '', ''],
            ['参数', '描述', '默认值'],
            ["name", "组名\nthe radio's group (ie parameter) name", "None"],
            ["value", "文本字段的值\nValue of the text field", "''"],
            [
                "maxlen ",
                "无或小组件值的最大长度\nNone or maximum length of the widget value",
                "100",
            ],
            [
                "x",
                "在页面上的水平位置(绝对坐标)\n"
                "the horizontal position on the page (absolute coordinates)",
                "0",
            ],
            [
                "y",
                "在页面上的垂直位置(绝对坐标)\n"
                "the vertical position on the page (absolute coordinates)",
                "0",
            ],
            ["width", "小组件宽度\nThe widget width", "120"],
            ["height", "小组件高度\nThe widget height", "36"],
            [
                "fontName",
                "要使用的第1种字体的名称。\nThe name of the type 1 font to be used",
                "'Helvetica'",
            ],
            ["fontSize", "要使用的字体大小\nThe size of font to be used", "12"],
            [
                "fillColor",
                "用来填充小组件的颜色\ncolour to be used to fill the widget",
                "None",
            ],
            ["textColor", "符号或文本的颜色\nthe colour of the symbol or text", "None"],
            ["borderWidth", "边框宽度\nas it says", "1"],
            ["borderColor", "边框颜色\nthe widget's border colour", "None"],
            ["borderStyle", "边框样式\nThe border style name", "'solid'"],
            [
                "tooltip",
                "悬停在小组件上时要显示的文本。"
                "\nThe text to display when hovering over the widget",
                "None",
            ],
            [
                "annotationFlags",
                "空白分隔的注解标志字符串" "\nblank separated string of annotation flags",
                "'print'",
            ],
            [
                "fieldFlags",
                "空白分隔的字段标志（见下文）。\n" "Blank separated field flags (see below)",
                "''",
            ],
            [
                "forceBorder",
                "当真的时候会强行画边框\n" "when true a border force a border to be drawn",
                "False",
            ],
            [
                "relative",
                "如果为真，服从当前画布的变换\n" "if true obey the current canvas transform",
                "False",
            ],
            [
                "dashLen ",
                "如果borderStyle=='dashed'，要使用破折号。\n"
                "the dashline to be used if the borderStyle=='dashed'",
                "3",
            ],
        ],
        [90, 260, 90],
        style=al_style,
        repeatRows=2,
    )
    pdf.add_paragraph("")
    pdf.add_flowable(table)
    pdf.add_heading("按钮样式", level=3)

    pdf.add_paragraph(
        '按钮样式参数表示当按钮被选中时，应该在按钮中出现什么样式的符号。'
        '有几种选择: $check$、$cross$、$circle$、$star$、$diamond$。'
    )
    pdf.add_paragraph(
        '请注意，文档渲染器可能会使这些符号中的某些符号在其预期应用中出现错误 。'
        'Acrobat阅读器更喜欢在规范规定应该显示的内容上使用自己的渲染（特别是在使用表格高亮功能的时候'
    )
    pdf.add_heading("小工具形状", level=3)
    pdf.add_paragraph('形状参数描述了复选框或单选部件的轮廓应该如何显示，你可以使用:$circle$、$square$。')
    pdf.add_paragraph('渲染器可能会自行决定小组件的外观，所以Acrobat Reader更喜欢圆形轮廓的收音机。')

    pdf.add_heading("边框样式", level=3)
    pdf.add_paragraph(
        '^borderStyle^参数会改变页面上小组件的3D外观，'
        '你可以使用: $solid$、$dashed$、$inset$、$bevelled$、$underlined$。'
    )
    pdf.add_heading("^fieldFlags^ 参数", level=3)
    pdf.add_paragraph(
        'fieldFlags参数可以是一个整数或一个包含空白的独立标记的字符串，其值如下表所示。更多信息请参考PDF规范。'
    )
    table = Table(
        [
            ['字段标志 Tokens 和 values', '', ''],
            ['Token', '描述', '值'],
            ["readOnly", "小部件只读\nThe widget is read only", "1<<0"],
            ["required", "小部件是必需的\nthe widget is required", "1<<1"],
            ["noExport", "不要导出小组件的值\ndon't export the widget value", "1<<2"],
            [
                "noToggleToOff",
                "单选框组必选选择一个\nradios one only must be on",
                "1<<14",
            ],
            ["radio", "单选法\nadded by the radio method", "1<<15"],
            [
                "pushButton",
                "当按钮为公共按钮时\nif the button is a push button",
                "1<<16",
            ],
            [
                "radiosInUnison",
                "单选框拥有一样的值时一起切换\nradios with the same value toggle together",
                "1<<25",
            ],
            ["multiline", "用于多行文本小组件\nfor multiline text widget", "1<<12"],
            ["password", "密码文本域\npassword textfield", "1<<13"],
            ["fileSelect", "文件选择小组件\nfile selection widget", "1<<20"],  # 1.4
            ["doNotSpellCheck", "不拼写检查\nas it says", "1<<22"],  # 1.4
            [
                "doNotScroll",
                "文本框不滚动\ntext fields do not scroll",
                "1<<23",
            ],  # 1.4
            [
                "comb",
                "根据最大长度值制作 comb 样式的文字\nmake a comb style text based on the "
                "maxlen value",
                "1<<24",
            ],  # 1.5
            ["richText", "如果使用富文本\nif rich text is used", "1<<25"],  # 1.5
            ["combo", "针对下拉框\nfor choice fields", "1<<17"],
            ["edit", "如果选择是可编辑的\nif the choice is editable", "1<<18"],
            ["sort", "是否要对数值进行排序\nif the values should be sorted", "1<<19"],
            [
                "multiSelect",
                "如果选择允许多选\nif the choice allows multi-select",
                "1<<21",
            ],  # 1.4
            [
                "commitOnSelChange",
                "reportlab 没有使用\nnot used by reportlab",
                "1<<26",
            ],  # 1.5
        ],
        [90, 260, 90],
        style=al_style,
        repeatRows=2,
    )
    pdf.add_paragraph("")
    pdf.add_flowable(table)

    pdf.add_heading("^annotationFlags^ 参数", level=3)
    pdf.add_paragraph('PDF小组件是注释，并具有注释属性，这些属性显示在下面的表格中。')
    Table(
        [
            ['注释标志 Tokens 和 values', '', ''],
            ['Token', '描述', '值'],
            ["invisible", "小组件不显示\nThe widget is not shown", "1<<0"],
            ["hidden", "小组件隐藏\nThe widget is hidden", "1<<1"],
            ["print", "小组件打印\nThe widget will print", "1<<2"],
            [
                "nozoom",
                "注释不会随渲染页面的大小而缩放。\nThe annotation will notscale with the "
                "rendered page",
                "1<<3",
            ],
            [
                "norotate",
                "小组件不会随着页面旋转。\nThe widget won't rotate with the page",
                "1<<4",
            ],
            ["noview", "不要渲染小组件\nDon't render the widget", "1<<5"],
            ["readonly", "小组件只读，不交互\nWidget cannot be interacted with", "1<<6"],
            ["locked", "小组件无法更改\nThe widget cannot be changed", "1<<7"],  # 1.4
            [
                "togglenoview",
                "在某些事件发生后，可以展示该小部件。\nTeh widget may be viewed after some "
                "events",
                "1<<8",
            ],  # 1.9
            [
                "lockedcontents",
                "小部件的内容是固定的\nThe contents of the widget are fixed",
                "1<<9",
            ],  # 1.7
        ],
        [90, 260, 90],
        style=al_style,
    )
    pdf.add_paragraph("")
    pdf.add_flowable(table)


def chapter5_platypus(pdf):
    pdf.add_heading("PLATYPUS - 页面布局和排版", level=1)
    pdf.add_heading("设计目标", level=2)
    pdf.add_paragraph(
        '$Platypus$是$"Page Layout and Typography Using Scripts"$的缩写。'
        '它是一个高水平的页面布局库，让你可以用最少的努力以编程方式创建复杂的文档。'
    )
    pdf.add_paragraph(
        'Platypus的设计力求将 "高层次 "的布局决定与文档内容尽可能分开 。'
        '例如，段落使用段落样式，页面使用页面模板，目的是让数百个有数千页的文件可以按照不同的样式规格重新格式化，'
        '只需在一个包含段落样式和页面布局规格的共享文件中修改几行即可。'
    )
    pdf.add_paragraph('$Platypus$的整体设计可以认为有几个层次，自上而下，这些是:')
    pdf.add_paragraph("")
    pdf.add_bullet('$DocTemplates$作为文档的最外层容器。')
    pdf.add_bullet('$PageTemplates$作为各种页面布局的规格。')
    pdf.add_bullet('$Frames$页面中可包含流动文本或图形的区域规格。')
    pdf.add_bullet(
        '$Flowables$对应$"flowed into the document"$流入文档的文本或图形元素'
        '（即图像、段落和表格等内容，但不包括$页脚$或$固定页面图形$等内容）。'
    )
    pdf.add_paragraph('$pdfgen.Canvas$为最终从其他图层接收文档绘画的最低层。')
    pdf.add_illustration(
        doc_examples.doctemplateillustration, 'DocTemplate 结构说明'
    )
    pdf.add_paragraph(
        '上面的插图形象地说明了$DocTemplate$、$PageTemplate$和$Flowables$的概念 。'
        '然而，它具有欺骗性，因为每一个$PageTemplate$实际上可以指定任何数量的页面的格式'
        '（而不是像从图中推断的那样只指定一个）。'
    )
    pdf.add_paragraph(
        '$DocTemplate$包含一个或多个$PageTemplate$，'
        '每个$PageTemplate$包含一个或多个$Frame$。'
        '$Flowables$ 是指可以^flowed^(流入)$Frame$的东西，'
        '例如$Paragraph$或$Table$。'
    )
    pdf.add_paragraph(
        '要使用$platypus$，你需要从$DocTemplate$类中创建一个文档，'
        '并向其$build$方法传递一个$Flowable$s列表。'
        '$document$的$build$方法知道如何将$flowable列表$处理成合理的东西。'
    )
    pdf.add_paragraph(
        '在内部，$DocTemplate$类使用各种事件来实现页面布局和格式化。'
        '每个事件都有一个对应的处理方法，称为$handle_XXX$ ，'
        '其中$XXX$是事件名称。'
        '一个典型的事件是$frameBegin$，'
        '它发生在机械开始第一次使用一个框架的时候。'
    )
    pdf.add_paragraph(
        '$Platypus$故事由一系列基本元素组成，这些元素被称为$Flowables$，'
        '它们驱动着数据驱动的$Platypus$格式化引擎。'
        '为了修改引擎的行为，一种特殊的可流式元素$ActionFlowables$告诉布局引擎，'
        '例如，跳到下一列或者换成另一个$PageTemplate$。'
    )
    pdf.add_heading("开始", level=2)
    pdf.add_paragraph('考虑以下代码序列，它为$Platypus$提供了一个非常简单的 "hello world "例子。')
    pdf.add_code_eg(doc_examples.platypussetup)
    pdf.add_paragraph('首先，我们从其他模块中导入一些构造函数、一些段落样式和其他方便。')
    pdf.add_code_eg(doc_examples.platypusfirstpage)
    pdf.add_paragraph('我们用上面的函数定义文档首页的固定特征。')
    pdf.add_code_eg(doc_examples.platypusnextpage)
    pdf.add_paragraph(
        '由于我们希望第一个页面之后的页面看起来与第一个页面不同，'
        '我们为其他页面的固定特征定义了一个备用布局。'
        '请注意，上面的两个函数使用 $pdfgen$ 级别的画布操作来为页面绘制注释。'
    )
    pdf.add_code_eg(doc_examples.platypusgo)
    pdf.add_paragraph(
        '最后，我们创建一个$"store"$并构建文档。'
        '请注意，我们在这里使用的是$"canned"$(罐头)文档模板，'
        '它是预建的页面模板。我们还使用了预建的段落样式 。'
        '我们在这里只使用了两种类型的$"flowables"$ --$Spacers$和$Paragraphs$ 。'
        '第一个$Spacer$确保段落跳过标题字符串。'
    )
    pdf.add_paragraph(
        '要查看这个示例程序的输出，'
        '请以"顶层脚本"的形式运行模块$docs/userguide/doc_examples.py$'
        '（来自$ReportLab docs$发行版）。'
        '脚本解释$python doc_examples.py$将生成$Platypus$输出$phello.pdf$。'
    )

    pdf.add_heading("$Flowables$", level=2)
    pdf.add_paragraph(
        '$Flowables$是可以被绘制的东西，'
        '它有$wrap$, $draw$和可能的$split$方法。'
        '$Flowable$是一个抽象的基类，用于绘制事物，一个实例知道它的大小，'
        '并在它自己的坐标系中绘制(这需要基API在调用$Flowable.draw$方法时提供一个绝对坐标系)。'
        '要获得一个实例，使用 $f=Flowable()$。'
    )
    pdf.add_text_note('$Flowable$类是一个抽象类，通常只作为基类使用。')
    keep_flag = pdf.start_keep_together()
    pdf.add_paragraph(
        '为了说明使用$Flowables$的一般方式，'
        '我们将展示如何在画布上使用和绘制衍生类$Paragraph$。'
        '$Paragraph$是如此重要，它们将有一整章的篇幅来介绍。'
    )
    pdf.add_code_eg(
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
    pdf.end_keep_together(keep_flag)

    pdf.add_heading("$Flowable$ 方法", level=3)
    pdf.add_code_eg('Flowable.draw()')
    pdf.add_paragraph(
        '这将被调用来要求 $flowable$ 实际渲染自己。'
        '$Flowable$类没有实现$draw$。'
        '调用代码应该确保 $flowable$ 有一个属性$canv$，'
        '它是$pdfgen.Canvas$，它应该被绘制到$Canvas$上，'
        '并且$Canvas$处于一个适当的状态(就翻译、旋转等而言)。'
        '通常这个方法只在内部被$drawOn$方法调用，派生类必须实现这个方法。'
        '派生类必须实现这个方法。'
    )

    pdf.add_code_eg('Flowable.drawOn(canvas,x,y)')
    pdf.add_paragraph(
        '这是控制引擎用来将$flowable$渲染到特定画布的方法。'
        '它处理转换为画布坐标(^x^,^y^)，并确保$flowable$有一个$canv$属性，'
        '这样$draw$方法(在基类中没有实现)就可以在一个绝对坐标框架中渲染。'
    )

    pdf.add_code_eg("Flowable.wrap(availWidth, availHeight)")
    pdf.add_paragraph('在询问对象的大小、绘制或其他什么之前，这个函数将被包围的框架调用。它返回实际使用的尺寸。')

    pdf.add_code_eg("Flowable.split(self, availWidth, availheight)")
    pdf.add_paragraph(
        '当wrap失败时，更复杂的框架会调用这个函数。'
        '愚蠢的$flowables$应该返回$[]$,这意味着它们无法拆分。'
        '聪明的$flowables$应该自己拆分并返回一个$flowables$列表。'
        '客户端代码要确保避免重复尝试拆分。'
        '如果空间足够，拆分方法应该返回[self]。'
        '否则，$flowable$应该重新排列，并返回一个按顺序考虑的$flowable$列表$[f0,...]$。'
        '实现的拆分方法应该避免改变$self$，因为这将允许复杂的布局机制在一个可流动的列表上进行多次传递。'
    )
    pdf.add_heading("流动定位的准则", level=2)
    pdf.add_paragraph('有两种方法，默认情况下返回零，为可流动物的垂直间距提供指导。')
    pdf.add_code_eg(
        """
        Flowable.getSpaceAfter(self):
        Flowable.getSpaceBefore(self):
    """
    )
    pdf.add_paragraph(
        '这些方法会返回$flowable$后面或前面应该有多少空间。'
        '这些空间不属于$flowable$本身，'
        '也就是说，$flowable$的$draw$方法在渲染时不应该考虑它。'
        '控制程序将使用返回的值来确定上下文中特定$flowable$需要多少空间。'
    )
    pdf.add_paragraph(
        "所有的$flowables$都有一个$hAlign$属性："
        "$('LEFT','RIGHT','CENTER'或'CENTRE')$。"
        "对于占满整个框架宽度的段落，这个属性没有影响。"
        "对于小于框架宽度的表格、图像或其他对象，这决定了它们的水平位置。"
    )
    pdf.add_paragraph('下面的章节将涵盖最重要的特定类型的可流动文件，段落和表格。')

    pdf.add_heading("Frames", level=2)
    pdf.add_paragraph(
        '$Frames$是活动的容器，'
        '它本身就包含在$PageTemplate$中，'
        '$Frames$有一个位置和大小，并保持一个剩余可绘制空间的概念。如：'
    )
    pdf.add_code_eg(
        """
        Frame(x1, y1, width,height, leftPadding=6, bottomPadding=6,
                rightPadding=6, topPadding=6, id=None, showBoundary=0)
    """
    )
    pdf.add_paragraph(
        '创建一个左下角坐标为$(x1,y1)$的$Frame$实例(在使用时相对于画布)，'
        '尺寸为 $width$ x $height$。'
        '$Padding$参数是用于减少绘画空间的正量。'
        '参数$id$是运行时使用的标识符，例如$"LeftColumn"$或$"RightColumn"$等。'
        '如果$showBoundary$参数是非零，那么框架的边界将在运行时被绘制出来（这有时很有用）。'
    )

    pdf.add_heading("$Frame$ 方法", level=3)

    pdf.add_code_eg("Frame.addFromList(drawlist, canvas)")
    pdf.add_paragraph('消耗$drawlist$前面的$Flowables$，直到帧满为止。如果不能容纳一个对象，则引发一个异常。')

    pdf.add_code_eg("Frame.split(flowable,canv)")
    pdf.add_paragraph('要求flowable使用可用空间进行分割，并返回flowable的列表。')

    pdf.add_code_eg("Frame.drawBoundary(canvas)")
    pdf.add_paragraph('将框架边界画成一个矩形（主要用于调试）。')

    pdf.add_heading("使用 $Frames$", level=3)
    pdf.add_paragraph(
        '$Frames$可以直接与$canvases$和$flowables$一起使用来创建文档。'
        '$Frame.addFromList$方法为你处理$wrap$ 和 $drawOn$调用。'
        '你不需要所有的$Platypus引擎$来获得有用的东西到$PDF$中。'
    )
    pdf.add_code_eg(
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

    pdf.add_heading("文档和模板", level=2)
    pdf.add_paragraph(
        '$BaseDocTemplate$类实现了文档格式化的基本机制。'
        '该类的一个实例包含了一个或多个$PageTemplate$的列表，'
        '这些$PageTemplate$可用于描述单页信息的布局。'
        '$build$方法可用于处理$Flowables列表$，以生成一个$PDF$文档。'
    )
    pdf.add_cond_page_break(3.0)
    pdf.add_heading("$BaseDocTemplate$", level=3)
    pdf.add_code_eg(
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
    pdf.add_paragraph(
        '创建一个适合创建基本文档的文档模板。'
        '它带有相当多的内部机制，但没有默认的页面模板。'
        '所需的$filename$可以是一个字符串，一个用于接收创建的<b>PDF</b>文档的文件名；'
        '也可以是一个有$write$方法的对象，如 $BytesIO$ 或 $file$ 或 $socket$。'
    )
    pdf.add_paragraph(
        '允许的参数应该是不言自明的，但是$showBoundary$控制是否绘制$Frame$的边界，这对于调试来说是很有用的。'
        '$allowSplitting$参数决定了内置方法是否应该尝试<i>split</i>单个$Flowables$跨越$Frame$。'
        '$_pageBreakQuick$参数决定了在结束页面之前，是否应该尝试结束页面上的所有框架。'
        '$encrypt$ 参数决定了是否对文档进行加密，以及如何加密。'
        '默认情况下，文档是不加密的。'
        '如果$encrypt$是一个字符串对象，那么它将作为pdf的用户密码。'
        '如果$encrypt$是一个$reportlab.lib.pdfencrypt.StandardEncryption$的实例，'
        '那么这个对象就被用来加密pdf。'
        '这允许对加密设置进行更精细的控制。'
    )
    pdf.add_heading("$BaseDocTemplate$ 方法", level=4)
    pdf.add_paragraph('这些都是客户程序员直接关心的问题，因为他们通常会被使用。')
    pdf.add_code_eg(
        """
        BaseDocTemplate.addPageTemplates(self,pageTemplates)
    """
    )
    pdf.add_paragraph('此方法用于在现有文档中添加一个或一系列$PageTemplate$。')
    pdf.add_code_eg(
        """
        BaseDocTemplate.build(self, flowables, filename=None, 
        canvasmaker=canvas.Canvas)
    """
    )
    pdf.add_paragraph(
        '这是应用程序程序员感兴趣的主要方法。假设文档实例被正确设置，'
        '$build$方法将^story^以$flowables列表$的形式接收（$flowables参数$），'
        '并在列表中循环，将$flowables列表$一次一个地强制通过格式化机制。'
        '实际上，这使得$BaseDocTemplate$实例发出对实例$handle_XXX$方法的调用来处理各种事件。'
    )

    pdf.add_heading("$BaseDocTemplate$ 抽象方法", level=4)
    pdf.add_paragraph(
        '这些在基类中根本没有语义。它们的目的是作为布局机制的纯虚拟钩子。紧接派生类的创建者可以覆盖这些，而不用担心影响布局引擎的属性。'
    )

    pdf.add_code_eg("BaseDocTemplate.afterInit(self)")
    pdf.add_paragraph('这个方法在基类初始化后被调用；派生类可以覆盖该方法来添加默认的$PageTemplates$。')

    pdf.add_code_eg("BaseDocTemplate.afterPage(self)")
    pdf.add_paragraph(
        '这是在页面处理后，紧接着当前页面模板的$afterDrawPage$方法被调用。'
        '一个派生类可以使用这个方法来做一些依赖于页面信息的事情，比如字典页面上的首字和尾字。'
    )

    pdf.add_code_eg("BaseDocTemplate.beforeDocument(self)")
    pdf.add_paragraph(
        '在对文档进行任何处理之前，但在处理机制准备好之后，'
        '就会调用这个函数，因此它可以用来对实例的$pdfgen.canvas$等进行处理。'
        '因此，它可以用来对实例的$pdfgen.canvas$等进行操作。'
    )

    pdf.add_code_eg("BaseDocTemplate.beforePage(self)")
    pdf.add_paragraph(
        '这是在页面处理开始时，在当前页面模板的$beforeDrawPage$方法之前调用的。它可以用来重置页面特定的信息持有者。'
    )

    pdf.add_code_eg("BaseDocTemplate.filterFlowables(self,flowables)")
    pdf.add_paragraph(
        '在主 $handle_flowable$ 方法开始时，'
        '调用这个函数来过滤$flowables$。'
        '在返回时，如果$flowables[0]$被设置为^None^，'
        '则会被丢弃，主方法立即返回。'
    )

    pdf.add_code_eg("BaseDocTemplate.afterFlowable(self, flowable)")
    pdf.add_paragraph('在$flowable$被渲染后调用。有兴趣的类可以使用这个钩子来收集特定页面或框架上存在的信息。')

    pdf.add_heading("$BaseDocTemplate$ 事件处理", level=4)
    pdf.add_paragraph(
        '这些方法构成了布局引擎的主要部分。'
        '程序员不应该直接调用或覆盖这些方法，除非他们试图修改布局引擎。'
        '当然，有经验的程序员如果想在某个特定的事件，即$XXX$处进行干预，'
        '而这个事件并不对应于其中的一个虚拟方法，那么总是可以覆盖并调用$drived$类版本中的基方法。'
        '我们为每个处理方法提供了一个基类同义词，名称相同，前缀为下划线$"_"$，这样就很容易了。'
    )

    pdf.add_code_eg(
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
    pdf.add_paragraph('在这里我们列出这些方法只是为了说明正在处理的事件。有兴趣的程序员可以看一下源码。')

    pdf.add_code_eg(
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
    pdf.add_paragraph(
        '使用文档模板可以非常简单，$SimpleDoctemplate$'
        '是由$BaseDocTemplate$派生出来的一个类，'
        '它提供了自己的$PageTemplate$和$Frame$设置。'
    )

    pdf.add_code_eg(
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

    pdf.add_heading("$PageTemplates$", level=3)
    pdf.add_paragraph(
        '$PageTemplate$类是一个语义相当简单的容器类。'
        '每个实例都包含一个$Frames$的列表，'
        '并且有一些方法应该在每个页面的开始和结束时被调用。'
    )

    pdf.add_code_eg(
        "PageTemplate(id=None,frames=[],onPage=_doNothing,onPageEnd=_doNothing)"
    )
    pdf.add_paragraph(
        '用于初始化一个实例，$frames$参数应该是一个$Frames$的列表，'
        '而可选的$onPage$和$onPageEnd$参数是可调用的，'
        '它们的签名应该是 $def XXX(canvas,document)$，'
        '其中$canvas$和$document$是正在绘制的画布和文档。'
        '这些例程的目的是用来绘制页面的非流动（即标准）部分。'
        '这些属性函数与纯虚拟方法 $PageTemplate.beforPage$ 和 $PageTemplate.afterPage$'
        '完全平行，这两个方法的签名是 $beforPage(self,canvas,document)$。'
        '这些方法允许使用类派生来定义标准行为，而属性则允许改变实例。'
        '在运行时，$id$ 参数用于执行 $PageTemplate$ 的切换，'
        '所以 $id=\'FirstPage\'$ 或 $id=\'TwoColumns\'$ 是典型的。'
    )


def chapter6_paragraph(pdf):
    pdf.add_heading("Paragraphs - 文本段落", level=1)
    pdf.add_paragraph(
        '$reportlab.platypus.Paragraph$类是$Platypus Flowables$中最有用的一个；'
        '它可以格式化相当任意的文本，并提供了使用$XML样式标记$的内联字体样式和颜色变化。'
        '格式化后的文本的整体形状可以是公正的，左右粗细的，或者居中的。'
        '$XML标记$甚至可以用来插入希腊字符或做下标。'
    )
    pdf.add_paragraph('下面的文字创建了一个$Paragraph$类的实例。')
    pdf.add_code_eg("""Paragraph(text, style, bulletText=None)""")
    pdf.add_paragraph(
        '参数$text$包含了段落的文本；'
        '在文本的结尾和换行后，多余的空白会被删除。'
        '这允许在<b>Python</b>脚本中轻松使用缩进的三引号文本。'
        '$bulletText$参数提供了段落的默认子弹文本。'
        '段落文本和子弹的字体和其他属性可以使用样式参数来设置。'
    )
    pdf.add_paragraph('参数 $style$ 应该是一个 $ParagraphStyle$ 类的实例，通常使用')
    pdf.add_code_eg("from reportlab.lib.styles import ParagraphStyle")

    pdf.add_paragraph(
        '这个容器类以结构化的方式提供了多个默认段落属性的设置。'
        '这些样式被安排在一个名为$stylesheet$的字典样式对象中，'
        '它允许以$stylesheet[\'BodyText\']$的形式访问这些样式。'
        '我们提供了一个示例样式表。'
    )
    pdf.add_code_eg(
        """
    from reportlab.lib.styles import getSampleStyleSheet
    stylesheet=getSampleStyleSheet()
    normalStyle = stylesheet['Normal']
    """
    )
    pdf.add_paragraph(
        '可以为$Paragraph$设置的选项可以从$ParagraphStyle$默认值中看出。'
        '前面带下划线(\'_\')的值来自于 '
        '$reportlab.rl_config$ 模块中的默认值，'
        '这些值来自于$reportlab.rl_settings$模块。'
    )
    pdf.add_heading("$ParagraphStyle$", level=2)
    pdf.add_code_eg(
        """
    class ParagraphStyle(PropertySet):
        defaults = {
            'fontName':_baseFontName,
            'fontSize':10,
            'leading':12,
            'leftIndent':0,
            'rightIndent':0,
            'firstLineIndent':0,
            'alignment':TA_LEFT,
            'spaceBefore':0,
            'spaceAfter':0,
            'bulletFontName':_baseFontName,
            'bulletFontSize':10,
            'bulletIndent':0,
            'textColor': black,
            'backColor':None,
            'wordWrap':None,
            'borderWidth': 0,
            'borderPadding': 0,
            'borderColor': None,
            'borderRadius': None,
            'allowWidows': 1,
            'allowOrphans': 0,
            'textTransform':None,
            'endDots':None,
            'splitLongWords':1,
            'underlineWidth': _baseUnderlineWidth,
            'bulletAnchor': 'start',
            'justifyLastLine': 0,
            'justifyBreaks': 0,
            'spaceShrinkage': _spaceShrinkage,
            'strikeWidth': _baseStrikeWidth,    #stroke width
            'underlineOffset': _baseUnderlineOffset,    #fraction of fontsize 
            to 
            offset underlines
            'underlineGap': _baseUnderlineGap,      #gap for double/triple 
            underline
            'strikeOffset': _baseStrikeOffset,  #fraction of fontsize to offset 
            strikethrough
            'strikeGap': _baseStrikeGap,        #gap for double/triple strike
            'linkUnderline': _platypus_link_underline,
            #'underlineColor':  None,
            #'strikeColor': None,
            'hyphenationLang': _hyphenationLang,
            'uriWasteReduce': _uriWasteReduce,
            'embeddedHyphenation': _embeddedHyphenation,
            }
    """
    )
    pdf.add_paragraph("使用文字段落样式: $ParagraphStyle$")
    paragraph_sample = (
        '你在此被指控在1970年5月28日， 你故意，非法，并与恶意的预想， '
        '出版一个所谓的英语 - 匈牙利短语书，意图造成破坏和平。 '
        '你如何辩护？'
    )
    pdf.add_paragraph(
        '$Paragraph$和$ParagraphStyle$类一起处理大多数常见的格式化需求。'
        '下面的示例以不同的样式绘制段落，并添加了一个边界框，'
        '这样你就可以看到确切的空间被占用了。'
    )
    pdf.add_para_box(
        paragraph_sample,
        pdf.stylesheet[constant.STYLE_NORMAL],
        '默认 $ParagraphStyle$',
    )
    pdf.add_paragraph(
        '$spaceBefore$和$spaceAfter$这两个属性如它们所说的那样，'
        '除了在一个框架的顶部或底部。'
        '在一个框架的顶部，$spaceBefore$被忽略，而在底部，$spaceAfter$被忽略。'
        '这意味着你可以指定一个\'Heading2\'样式在页面中间出现时，'
        '它之前有两英寸的空间，但不会在页面顶部得到数英亩的空白。 '
        '这两个属性应该被认为是对Frame的 "请求"，'
        '而不是段落本身所占空间的一部分。'
    )
    pdf.add_paragraph(
        '$fontSize$和$fontName$标签是显而易见的，'
        '但重要的是设置$leading$。 '
        '这是相邻文本行之间的间距；'
        '一个好的经验法则是让这个间距比点的大小大 20%。 '
        '要获得双倍行距的文本，请使用较高的$leading$。'
        '如果您将$autoLeading$(默认为$"off"$)'
        '设置为$"min"$(使用观察到的前导，即使比指定的小)'
        '或$"max"$(使用观察到的和指定的较大值)'
        '，那么就会尝试逐行确定前导。'
        '如果行中包含不同的字体大小等，'
        '这可能是有用的。'
    )
    pdf.add_paragraph('下图为前后空间和增加的引导。')
    _style = ParagraphStyle(
        'Spaced',
        spaceBefore=6,
        spaceAfter=6,
        leading=16,
        fontName=pdf.font_regular,
    )
    pdf.add_para_box(
        paragraph_sample,
        _style,
        '前后空间和增加 leading',
    )
    pdf.add_paragraph(
        '属性 $borderPadding$ 调整段落与背景边框之间的 $padding$ 。'
        '它可以是一个单一的值，也可以是一个包含2到4个值的元组。'
        '这些值的应用方式与层叠样式表（CSS）相同。'
        '如果给定一个值，该值将应用于所有四条边框。'
        '如果给了一个以上的值，则从顶部开始按顺时针顺序应用到边上。'
        '如果给了两个或三个值，则缺失的值将从相反的边开始应用。'
        '请注意，在下面的例子中，黄色方框是由段落本身绘制的。'
    )
    _style = ParagraphStyle(
        'padded',
        borderPadding=(7, 2, 20),
        borderColor='#000000',
        borderWidth=1,
        backColor='#FFFF00',
        fontName=pdf.font_regular,
    )
    pdf.add_para_box(
        paragraph_sample,
        _style,
        '可变 $padding$',
    )
    pdf.add_paragraph(
        '$leftIndent$ 和 $rightIndent$ 属性的作用正是你所期望的；'
        '$firstLineIndent$ 被添加到第一行的 $leftIndent$ 中。'
        '如果你想要一个笔直的左边缘，记得将$firstLineIndent$等于0。'
    )

    _style = ParagraphStyle(
        'indented',
        firstLineIndent=+24,
        leftIndent=24,
        rightIndent=24,
        fontName=pdf.font_regular,
    )
    pdf.add_para_box(
        paragraph_sample,
        _style,
        '左右缩进三分一，首行缩进三分二',
    )
    pdf.add_paragraph(
        '将$firstLineIndent$设置为负数，'
        '$leftIndent$则高得多，'
        '并使用不同的字体（我们稍后会告诉你怎么做！）'
        '可以给你一个定义列表：'
    )

    _style = ParagraphStyle(
        'dl',
        leftIndent=36,
        fontName=pdf.font_regular,
    )
    pdf.add_para_box(
        f"$皮克尔斯法官$: {paragraph_sample}",
        _style,
        '左右缩进三分一，首行缩进三分二',
    )
    pdf.add_paragraph(
        '在模块<i>reportlab.lib.enums</i>中，'
        '$alignment$有四个可能的值，定义为常量。 '
        '这些值是 $TA_LEFT$, $TA_CENTER$ 或 $TA_CENTRE$, $TA_RIGHT$ 和 $TA_JUSTIFY$ ，'
        '值分别为0, 1, 2和4。 这些都和你所期望的一样。'
    )
    pdf.add_paragraph(
        '将$wordWrap$设置为$\'CJK\'$来获得亚洲语言的换行。'
        '对于普通的西方文本，'
        '你可以通过$allowWidows$和$allowOrphans$'
        '来改变断行算法处理^widows^和^orphans^的方式。'
        '这两个值通常都应该设置为$0$，'
        '但由于历史原因，我们允许^widows^。'
        '文本的默认颜色可以用$textColor$设置，'
        '段落的背景颜色可以用$backColor$设置。'
        '段落的边框属性可以使用$borderWidth$, '
        '$borderPadding$, $borderColor$和$borderRadius$来改变。'
    )
    pdf.add_paragraph(
        '$textTransform$属性可以是'
        '^None^，'
        '$uppercase$或'
        '$lowercase$'
        '得到明显的结果，'
        '$capitalize$'
        '得到初始字母大写。'
    )
    pdf.add_paragraph(
        '属性$endDots$可以是'
        '^None^，'
        '一个字符串，或者一个对象，'
        '其属性为 $text$ 和可选的 $fontName、fontSize、textColor、backColor$'
        '和 $dy(y offset)$ ，用于指定左/右对齐段落最后一行的尾部内容。'
    )
    pdf.add_paragraph('$splitLongWords$属性可以设置为假值，以避免拆分非常长的单词。')
    pdf.add_paragraph(
        "属性$bulletAnchor$可以是"
        "^'start'^,"
        "^'middle'^,"
        "^'end'^或"
        "^'numeric'^"
        "来控制子弹的锚定位置。"
    )
    pdf.add_paragraph('$justifyBreaks$ 属性' '控制了是否应该用 $&lt;br/&gt;$ 标签故意断行。')
    pdf.add_paragraph('属性$spaceShrinkage$是一个小数，指定段落行的空间可以缩小多少以使其合适；通常是0.05左右。')
    pdf.add_paragraph(
        '当使用 $&lt;u&gt;$ 或链接标签时，$underlineWidth$、$underlineOffset$'
        '、$underlineGap$ 和 $underlineColor$属性控制了下划线行为。'
        '这些标签可以有这些属性的覆盖值。'
        '$width$ 和 $offset$ 的属性值是一个$fraction * Letter$，'
        '其中letter可以是 $P$、$L$、$f$ 或 $F$ 中的一个，代表字体大小比例。'
        '$P$ 使用标签处的字体大小，'
        '$F$ 是标签中的最大字体大小，'
        '$f$ 是标签内的初始字体大小。'
        '$L$ 表示全局（$ParagraphStyle$）字体大小。'
        '$strikeWidth$, $strikeOffset$, '
        '$strikeGap$ 和 $strikeColor$属性对删除线有同样的作用。'
    )
    pdf.add_paragraph('属性 $linkUnderline$ 控制链接标签是否自动下划线。')
    pdf.add_paragraph(
        '如果安装了$pyphen$ python模块，'
        '则属性 $hyphenationLang$ 控制'
        '哪种语言将被用于在没有明确嵌入连字符的情况下连字符。'
    )
    pdf.add_paragraph('如果设置了 $embeddedHyphenation$，那么就会尝试拆分带有嵌入式连字符的单词。')
    pdf.add_paragraph(
        '属性 $uriWasteReduce$ '
        '控制我们如何尝试分割长的 $uri$。'
        '它是我们认为太过浪费的行的分数，'
        '在模块 $reportlab.rl_settings$ 中的默认值是<i>0.5</i>。'
        '这意味着如果我们将浪费至少一半的行数，我们将尝试拆分一个看起来像uri的单词。'
    )
    pdf.add_paragraph(
        '目前，连字符 和 $uri$ 分割是默认关闭的。'
        '您需要通过使用 $~/.rl_settings$ 文件'
        '或在 python 路径中添加 $reportlab_settings.py$ 模块'
        '来修改默认设置。合适的值是'
    )
    pdf.add_code_eg(
        """
    hyphenationLanguage='en_GB'
    embeddedHyphenation=1
    uriWasteReduce=0.3
    """
    )

    pdf.add_heading("文本段落XML标记标签", level=2)
    pdf.add_paragraph('XML标记可以用来修改或指定整体段落样式，也可以指定段落内的标记。')

    pdf.add_heading('最外层 &lt; para &gt; 标签', level=3)
    pdf.add_paragraph(
        '段落文本可以选择由 '
        '&lt;para attributes....&gt; &lt;/para&gt; 标签包围。'
        '开头的 &lt;para&gt; 标签的任何属性'
        '都会影响 $Paragraph$ $text$ 和/或 $bulletText$'
        '所使用的样式。'
    )
    pdf.add_paragraph("")

    def getAttrs(A):
        _addAttributeNames(A)
        S = {}
        for k, v in A.items():
            a = v[0]
            if a not in S:
                S[a] = [k]
            else:
                S[a].append(k)

        K = list(sorted(S.keys()))
        K.sort()
        D = [('属性', '同义词')]
        for k in K:
            D.append((k, ", ".join(list(sorted(S[k])))))
        cols = 2 * [None]
        rows = len(D) * [None]
        return D, cols, rows

    table = Table(*getAttrs(_paraAttrMap))
    table.setStyle(
        TableStyle(
            [
                ('FONT', (0, 0), (-1, 1), 'SourceHanSans-ExtraLight', 10, 12),
                ('FONT', (0, 1), (-1, -1), 'Courier', 8, 8),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            ]
        )
    )
    pdf.add_flowable(table)
    pdf.add_caption('样式属性的同义词', category=constant.CAPTION_TABLE)
    pdf.add_paragraph(
        '我们为我们的 Python 属性名提供了一些有用的同义词，'
        '包括小写版本，以及 HTML 标准中存在的等价属性。 '
        '这些增加的内容使构建 XML 打印应用程序变得更加容易，'
        '因为许多段内标记可能不需要翻译。'
        '下表显示了最外层段落标签中允许的属性和同义词。'
    )
    pdf.add_cond_page_break(1)

    pdf.add_heading("段内标记", level=2)
    pdf.add_paragraph(
        '&lt;！[CDATA[ '
        '在每个段落中，我们使用一组基本的XML标签来提供标记。 '
        '其中最基本的是粗体 (&lt;b&gt;...&lt;/b&gt;)、'
        '斜体 (&lt;i&gt;...&lt;/i&gt;) 和'
        '下划线 (&lt;u&gt;...&lt;/u&gt;)。'
        '其他允許的标签有强调 (&lt;strong&gt;..&lt;/strong&gt;)，'
        '和删除线(&lt;strike&gt;...&lt;/strike&gt;)。'
        '&lt;link&gt;和&lt;a&gt;标签可用于引用当前文档中的URI、文档或书签。'
        '&lt;a&gt; 标签的 $a$ 变体可用于标记文档中的一个位置。'
        '也允许使用 $break$ (&lt;br/&gt;)标签。]]&gt;。'
    )
    pdf.add_para_box2(
        "$兹指控$你于1970年5月28日故意、非法和恶意地预谋出版一本所谓的英匈短语书，" "意图破坏和平。 <u>你如何辩护</u>？",
        '简单的黑体和斜体标签',
    )
    pdf.add_para_box2(
        '这是一个锚标签的<a href="#MYANCHOR" color="blue">链接</a>，'
        '即<a name="MYANCHOR"/><font color="green">这里</font>。'
        '这是另一个指向同一锚标签的'
        '<link href="#MYANCHOR" color="blue" '
        'fontName="SourceHanSans-ExtraLight">'
        '链接</link>。',
        '锚和链接',
    )

    pdf.add_paragraph(
        '$link$标签可以用作参考，但不能用作锚。'
        '$a$和$link$超链接标签有附加属性'
        '^fontName^、^fontSize^、^color^'
        '和 ^backColor^属性。'
        '超链接引用可以有$http:$<i>（外部网页）</i>、'
        '$pdf:$'
        '<i>（不同的pdf文档）</i>或'
        '<b>document:</b>'
        '<i>（相同的pdf文档）</i>等方案；'
        '缺少的方案将被视为<b>document</b>，'
        '就像引用以#开头时的情况一样（在这种情况下，锚应该省略它）。'
        '任何其他方案都会被视为某种URI。'
    )
    pdf.add_para_box2(
        '<strong>兹指控你</strong>于1970年5月28日故意、非法和'
        '<strike>恶意地预谋</strike><br/>出版一本所谓的英匈短语书，'
        '你怎么辩解？',
        "强调, 删除线, 和换行标签",
    )

    pdf.add_heading("$&lt;font&gt;$ 标签", level=3)
    pdf.add_paragraph(
        "$&lt;font&gt;$标签可以用来改变段落中任何子串的字体名称、大小和文本颜色。"
        "法定属性有$size$、$face$、$name$（与$face$相同）、$color$和$fg$（与$color$相同）。"
        "$name$是字体家族的名称，没有任何'bold'或'italic'的后缀。"
        "颜色可以是HTML的颜色名称，也可以是以各种方式编码的十六进制字符串；"
        "请参见^reportlab.lib. colors^了解允许的格式。"
    )
    pdf.add_para_box2(
        '你在此<font face="SourceHanSans-ExtraLight"'
        'color="red">被控</font>于1970年5月28日故意、非法和'
        '<font size=16>怀着预谋的恶意</font>出版一本所谓的英匈短语书，意图破坏和平。'
        ' 你如何辩护？',
        "$font$ 标签",
    )

    pdf.add_heading("上标和下标", level=3)
    pdf.add_paragraph(
        '上标和下标是由&lt;![CDATA[&lt;super&gt;/&lt;sup&gt;和&lt;sub&gt;标签支持的，'
        '它们的工作原理和你所期望的完全一样。'
        '另外这三个标签还有属性 rise 和 size，可以选择设置上标/下标文本的上升/下降和字体大小。'
        '此外，大多数希腊字母可以通过使用&lt;greek&gt;&lt;/greek&gt;标签，'
        '或者使用mathML实体名来访问。]]&gt。'
    )

    pdf.add_para_box2(
        '等式（&alpha;）。<greek>e</greek> <super rise=9 '
        'size=6><greek>ip</greek></super>=-1。',
        '希腊字母和上标',
    )

    pdf.add_heading('内联图片', level=3)

    pdf.add_paragraph(
        '我们可以用&lt;img/&gt;标签在段落中嵌入图片，'
        '该标签有$src$、$width$、$height$等属性，其含义很明显。'
        '$valign$属性可以设置为类似css的值，'
        '从 "baseline"、"sub"、"super"、"top"、"text-top"、"middle"、"bottom"、"text'
        '-bottom"；'
        '该值也可以是一个数字百分比或绝对值。'
    )

    pdf.add_para_box2(
        '<para autoLeading="off" fontSize=12>This &lt;img/&gt; '
        '<img src="images/testimg.gif" valign="top"/> is aligned <b>top</b>.'
        '<br/><br/>This &lt;img/&gt; '
        '<img src="images/testimg.gif" valign="bottom"/> is aligned '
        '<b>bottom</b>.'
        '<br/><br/> This &lt;img/&gt; '
        '<img src="images/testimg.gif" valign="middle"/> is aligned '
        '<b>middle</b>.'
        '<br/><br/>This &lt;img/&gt; '
        '<img src="images/testimg.gif" valign="-4"/> is aligned <b>-4</b>.'
        '<br/><br/>This &lt;img/&gt; '
        '<img src="images/testimg.gif" valign="+4"/> is aligned <b>+4</b>.'
        '<br/><br/>This &lt;img/&gt; '
        '<img src="images/testimg.gif" width="10"/> has width<b>10</b>.'
        '<br/><br/></para>',
        '内联图片',
    )
    pdf.add_paragraph(
        "$src$属性可以指向一个远程位置，"
        "例如$src=\"https://www.reportlab.com/images/logo.gif\"$。"
        "默认情况下，我们将$rl_config.trustedShemes$ "
        "设置为$['https','http','file','data','ftp']$"
        "和$rl_config.trustedHosts=None$，后者意味着没有限制。"
        "你可以使用覆盖文件来修改这些变量，"
        "例如$reportlab_settings.py$或$~/.reportlab_settings$。"
        "或者在环境变量$RL_trustedSchemes$ &amp; "
        "$RL_trustedHosts$中以逗号分隔。"
        "请注意，$trustedHosts$值可能包含<b>glob</b>野车，"
        "因此<i>*.reportlab.com</i>将匹配明显的域。"
        "<br/><span color=\"red\"><b>*NB*</b></span>"
        "使用^trustedHosts^和/或^trustedSchemes^"
        "可能无法控制行为，以及当$URI$模式被查看器应用程序检测到时的操作。"
    )

    pdf.add_heading("$&lt;u&gt;$ 和 $&lt;strike&gt;$ 标签", level=3)

    pdf.add_paragraph(
        '这些标签可用于执行明确的下划线或删除线。'
        '这些标签的属性有$width$、$offset$、$color$、$gap$ 和 $kind$。'
        '$kind$属性控制将绘制多少行(默认$kind=1$)，当$kind>1$时，'
        '$gap$属性控制行与行之间的间隔。'
    )

    pdf.add_heading("$&lt;nobr&gt;$ 标签", level=3)
    pdf.add_paragraph(
        '如果使用连字符，$&lt;nobr&gt;$标签会抑制它，'
        '所以$&lt;nobr&gt;一个非常长的单词不会被打断&lt;/nobr&gt;$不会被打断。'
    )

    pdf.add_heading('文字段落和列表的编号', level=3)
    pdf.add_paragraph(
        '$&lt;seq&gt;$标签为编号列表、章节标题等提供了全面的支持，'
        '它作为^reportlab.lib.sequencer^中$Sequencer$类的接口。 '
        '它是^reportlab.lib.sequencer^中$Sequencer$类的接口。'
        '这些都是用来对整个文档中的标题和数字进行编号的。'
        '您可以创建任意多的独立的 "计数器"，并通过$id$属性进行访问；'
        '每次访问时，这些计数器都将以1为单位递增。 '
        '$seqreset$标签可以重置计数器。'
        '如果你想让它从1以外的数字开始恢复，'
        '使用语法&lt;seqreset id="mycounter" base="42"&gt;。'
        '让我们开始吧。'
    )
    pdf.add_para_box2(
        '<seq id="spam"/>, '
        '<seq id="spam"/>, '
        '<seq id="spam"/>. 重置'
        '<seqreset id="spam"/>.  '
        '<seq id="spam"/>, '
        '<seq id="spam"/>,'
        '<seq id="spam"/>.',
        '基本序列',
    )
    pdf.add_paragraph(
        '你可以通过使用&lt;seqdefault id="Counter"&gt; 标签'
        '指定一个计数器ID作为<i>default</i>来节省指定ID的时间；'
        '然后每当没有指定计数器ID时就会使用它。 '
        '这样可以节省一些输入，特别是在做多级列表的时候；'
        '您只需在进入或退出一个级别时更改计数器ID。'
    )

    pdf.add_para_box2(
        '<seqdefault id="spam"/>Continued... <seq/>,'
        '<seq/>, <seq/>, <seq/>, <seq/>, <seq/>, <seq/>.',
        '默认序列',
    )
    pdf.add_paragraph(
        '最后，我们可以使用Python字符串格式化的变体'
        '和&lt;seq&gt;标签中的$template$属性来访问多级序列。 '
        '这是用来做所有数字中的标题，以及二级标题。 '
        '子串 $%(counter)s$ 提取了一个计数器的当前值，但不递增；'
        '在 $%(counter)s$ 中添加一个加号，使计数器递增。'
        '数字标题使用了类似下面的模式。'
    )

    pdf.add_para_box2(
        '图 <seq template="%(Chapter)s-%(FigureNo+)s"/> - 多级模板', "多级模板"
    )
    pdf.add_paragraph(
        '我们做了点小手脚--真正的文档用的是 "Figure"，' '但上面的文字用的是 "FigureNo" ' '--否则我们会把编号弄乱的'
    )

    pdf.add_heading("项目符号和段落编号", level=2)
    pdf.add_paragraph(
        '除了三个缩进属性之外，'
        '还需要一些其他参数来正确处理带项目符号和编号的列表。 '
        '我们在这里讨论这个问题，因为你现在已经看到了如何处理编号。 '
        '一个段落可以有一个可选的^bulletText^参数传递给它的构造函数；'
        '或者，项目符号文本可以放在它头部的$<![CDATA[<bullet>...</bullet>]]>$标签中。 '
        '这段文字将被绘制在段落的第一行，其X原点由样式的$bulletIndent$属性决定，字体由$bulletFontName$属性给出。  '
        '"项目符号"可以是一个单一的字符，如（嘟！）一个项目符号，或者是一个文本片段，'
        '如一些编号序列中的数字，甚至是定义列表中使用的简短标题。  '
        '字体可能提供各种项目编号字符，但我们建议首先尝试Unicode项目编号($&bull;$)，'
        '可以写成$&amp;bull;$，和 $#x2022;$ 或(utf8中) $\\xe2\\x80\\xa2$):'
    )

    table = Table(*getAttrs(_bulletAttrMap))
    table.setStyle(
        [
            ('FONT', (0, 0), (-1, 1), 'SourceHanSans-ExtraLight', 10, 12),
            ('FONT', (0, 1), (-1, -1), 'Courier', 8, 8),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
    pdf.add_flowable(table)

    pdf.add_caption('&lt;bullet&gt; 属性和同义词', category=constant.CAPTION_TABLE)
    pdf.add_paragraph(
        '在一个给定的段落中，&lt;bullet&gt;标签只允许使用一次，】它的使用会覆盖在^Paragraph'
        '^创建中指定的隐含的项目符号样式和 ^bulletText^。 (项目符号文本)'
    )
    pdf.add_para_box(
        '<bullet>&bull;</bullet>这是一个要点。'
        'Spam spam spam spam spam spam spam spam spam spam spam spam'
        'spam spam spam spam spam spam spam spam spam spam',
        pdf.stylesheet[constant.STYLE_BULLET],
        '项目点的基本使用',
    )

    pdf.add_paragraph(
        '除了使用序列标签外，数字也使用了完全相同的技术。 '
        '也可以在项目符号中放入一个多字符的字符串；'
        '用深缩进和粗体子弹字体，'
        '你可以制作一个紧凑的定义列表。'
    )


def chapter7_table(pdf):
    pdf.add_heading("表格和表格样式", level=1)

    pdf.add_paragraph(
        '$Table$和$LongTable$类来源于$Flowable$类，是一个简单的文本网格机制。'
        '当计算列宽时，$longTable$类使用了一种贪婪的算法，它是为速度至上的长表设计的。'
        '$Table$单元格可以容纳任何可以转换为<b>Python</b> $string$或$Flowables$ '
        '(或$Flowables$列表)的内容。'
    )
    pdf.add_paragraph(
        '我们现在的表格是在高效绘图和规范与功能之间的权衡。 ' '我们假设读者对HTML表格有一定的熟悉。' '简而言之，它们具有以下特点。'
    )
    pdf.add_paragraph("")
    pdf.add_bullet('它们可以包含任何可转换为字符串的东西；可流动的对象，如其他表格；或整个子集。')
    pdf.add_bullet(
        '如果你不提供行高，他们可以计算出行高来适应数据。 ' '(他们也可以计算出宽度，但一般来说，设计师最好手动设置宽度，这样画得更快)。'
    )
    pdf.add_bullet(
        '如果需要的话，它们可以在不同的页面上进行分割（参见canSplit属性）。'
        '你可以指定在分割后，顶部和底部的若干行应该重复显示'
        '（例如，在第2,3,4页再次显示页眉...）。'
    )
    pdf.add_bullet(
        '他们有一个简单而强大的符号来指定阴影和网格线，'
        '这对于财务或数据库表来说非常适用，因为你不知道前面有多少行。 '
        '你可以很容易的说 '
        '"把最后一行加粗，并在上面加一条线"。'
    )
    pdf.add_bullet(
        '样式和数据是分开的，所以你可以声明少量的表格样式，' '并将它们用于一个报表系列。 ' '样式也可以 "继承"，就像段落一样。'
    )
    pdf.add_paragraph(
        '然而，与HTML表格相比，有一个主要的限制。'
        '它们定义了一个简单的矩形网格。 '
        '没有简单的行或列跨度；'
        '如果你需要跨度单元格，'
        '你必须将表格嵌套在表格单元格内，或者使用更复杂的方案，'
        '其中跨度的前导单元格包含实际内容。'
    )
    pdf.add_paragraph(
        '通过向构造函数传递列宽的可选序列、行高的可选序列以及行序的数据来创建$Tables$。'
        '表的绘制可以通过使用TableStyle$实例来控制。'
        '这允许控制行的颜色和权重（如果有的话），以及文本的字体、对齐和填充。'
        '提供了一个原始的自动行高和列宽计算机制。'
    )
    pdf.add_heading('$Table$', level=2)
    pdf.add_paragraph('这些是客户端程序员感兴趣的主要方法。')

    pdf.add_heading("$Table$ 初始化", level=4)

    pdf.add_code_eg(
        """
    Table(
        data,
        colWidths=None,
        rowHeights=None,
        style=None,
        splitByRow=1,
        repeatRows=0,
        repeatCols=0,
        rowSplitRange=None,
        spaceBefore=None,
        spaceAfter=None,
    )
    """
    )
    pdf.add_paragraph(
        '参数$data$是单元格值的序列，'
        '每个单元格值都应该使用$str$函数转换为字符串值，'
        '或者应该是一个 $Flowable$ 实例(如$Paragraph$)或此类实例的列表(或元组)。'
        '如果一个单元格值是一个 $Flowable$ 或 $Flowable$ 的列表，'
        '这些单元格必须有一个确定的宽度，或者包含的列必须有一个固定的宽度。'
        '单元格值的第一行在 $data[0]$ 中，也就是说，单元格值是按行顺序排列的。'
        '$i$, $j$<sup>th.</sup>单元格值在$data[i][j]$中。'
        '单元格值中的新行字符$\'\\n\'$被视为行分割字符，'
        '并在<i>draw</i>时用于将单元格格式化为行。'
    )
    pdf.add_paragraph(
        '其他参数是相当明显的，'
        '$colWidths$ 参数是一个数字序列，也可能是$None$，代表列的宽度。'
        '在 $colWidths$ 中的元素数决定了表中的列数。值为$None$意味着相应的列宽应该自动计算。'
    )
    pdf.add_paragraph(
        '参数 $rowHeights$ 是一个数字序列，也可能是$None$，代表行的高度。'
        '$rowHeights$ 中的元素数决定了表中的行数。'
        '值为$None$意味着相应的行高应该自动计算。'
    )
    pdf.add_paragraph('参数 $style$ 可以是表的初始样式。')
    pdf.add_paragraph(
        '$splitByRow$ 参数只适用于太高和太宽而无法适应当前上下文的表格。 '
        '在这种情况下，你必须决定是向下和横向 "平铺"，还是横向然后向下。 '
        '这个参数是一个布尔值，表示当当前绘图区域可用空间太小，而调用者希望$Table$进行分割时，'
        '$Table$应该先按行进行分割，再按列进行分割。'
        '目前还没有实现按列分割$Table$，'
        '所以将$splitByRow$设置为$False$'
        '将导致$NotImplementedError$。'
    )
    pdf.add_paragraph(
        '参数$repeatRows$指定了当$Table$被要求拆分时应该重复的前导行的数量或元组。'
        '如果它是一个元组，它应该指定哪些前导行应该被重复；'
        '这允许表的第一次出现比后来的分割部分有更多的前导行。'
        '目前，$repeatCols$参数被忽略，因为$Table$不能按列进行拆分。'
    )
    pdf.add_paragraph(
        '当在$platypus$故事中重新编排时，'
        '$spaceBefore$ 和 $spaceAfter$ 参数 可以用来在表格之前或之后放置额外的空间。'
    )
    pdf.add_paragraph(
        '$rowSplitRange$参数可以用来控制表的分割，将表分割成它的行的子集；这可以防止分割太接近表的开始或结束。'
    )
    pdf.add_heading("$Table.setStyle(tblStyle)$", level=4)
    pdf.add_paragraph(
        '这个方法将类$TableStyle$(下面讨论)的一个特定实例应用到$Table$实例中。'
        '这是让$tables$以一种很好的格式化方式出现的唯一方法。'
    )
    pdf.add_paragraph('对$setStyle$方法的连续使用以加法的方式应用这些样式。' '也就是说，后面的应用会覆盖前面重叠的应用。')

    pdf.add_heading("$TableStyle$", level=2)
    pdf.add_paragraph(
        '这个类是通过传递给它一个<i>commands</i>序列来创建的，'
        '每个 $command$ 是一个元组，由它的第一个元素识别，它是一个字符串；'
        '$command$ 元组的其余元素代表命令的起始和停止单元格坐标，可能还有厚度和颜色等。'
    )
    pdf.add_heading('$TableStyle$  方法', level=2)
    pdf.add_heading("$TableStyle(commandSequence)$", level=3)
    pdf.add_paragraph('创建方法以参数命令序列为例初始化$TableStyle$。')
    pdf.add_code_eg(
        """
        LIST_STYLE = TableStyle(
            [('LINEABOVE', (0,0), (-1,0), 2, colors.green),
            ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
            ('LINEBELOW', (0,-1), (-1,-1), 2, colors.green),
            ('ALIGN', (1,1), (-1,-1), 'RIGHT')]
            )
    """
    )
    pdf.add_heading("$TableStyle.add(commandSequence)$", level=3)
    pdf.add_paragraph('此方法允许你向现有的$TableStyle$添加命令，即你可以在多个语句中建立$TableStyles$。')
    pdf.add_code_eg(
        """
        LIST_STYLE.add('BACKGROUND', (0,0), (-1,0), colors.Color(0,0.7,0.7))
    """
    )
    pdf.add_heading("$TableStyle.getCommands()$", level=3)
    pdf.add_paragraph('此方法返回实例的命令序列。')
    pdf.add_code_eg(
        """
        cmds = LIST_STYLE.getCommands()
    """
    )
    pdf.add_heading("$TableStyle$ Commands", level=2)
    pdf.add_paragraph('传递给$TableStyles$的命令主要有三组，分别影响表格背景、绘制线条或设置单元格样式。')
    pdf.add_paragraph(
        '每个命令的第一个元素是它的标识符，'
        '第二个和第三个参数决定了受影响的单元格的单元格坐标，'
        '负坐标从极限值向后数，就像<b>Python</b>索引一样。'
        '坐标是以(列，行)的形式给出的，它遵循电子表格的 "A1 "模型，'
        '但不是更自然的(对数学家来说) "RC "排序。'
        '左上角的单元格是（0，0），右下角的单元格是（-1，-1）。'
        '根据命令的不同，各种额外的(???)发生在3开始的指数上。'
    )
    pdf.add_pencil_note()
    pdf.add_text_note(
        '对表格坐标系理解不够透彻的参考: '
        '<a href="https://blog.csdn.net/weixin_39021016/article/details/109044955">'
        '<font color="green">这里</font></a>',
        prefix='<font color="red">译者注</font>: ',
    )

    pdf.add_heading("$TableStyle$ Cell Formatting Commands", level=3)
    pdf.add_paragraph('单元格格式化命令都以一个标识符开头，后面是单元格定义的开始和结束，也许还有其他参数。')
    table = Table(
        [
            ('Command', '同义词', '描述'),
            ('FONT', None, '字体名称, 可选字体大小和字符间距(leading).'),
            ('FONTNAME', "FACE", '字体名称.'),
            ('FONTSIZE', "SIZE", '以点为单位的字体大小; 字符间距(leading)可能会不同步.'),
            ('LEADING', None, '以点为单位的字符间距(leading).'),
            ('TEXTCOLOR', None, '颜色名称或 (R,G,B) 元组.'),
            (
                'ALIGNMENT',
                "ALIGN",
                'LEFT, RIGHT 和 CENTRE (或 CENTER) 或 DECIMAL 中的一个.',
            ),
            ('LEFTPADDING', None, '整数左边距，默认为6.'),
            ('RIGHTPADDING', None, '整数右边距，默认为6.'),
            ('BOTTOMPADDING', None, '整数下边距，默认为3.'),
            ('TOPPADDING', None, '整数上边距，默认为3.'),
            (
                'BACKGROUND',
                None,
                '取一个由对象、字符串名称或数字元组/列表定义的颜色，\n'
                '或者取一个描述所需渐变填充的列表/元组，\n'
                '该列表/元组应包含[DIRECTION, startColor, endColor]三个元素，\n'
                '其中 DIRECTION 是 VERTICAL 或 HORIZONTAL。\n',
            ),
            ('ROWBACKGROUNDS', None, '一个要循环使用的颜色列表。'),
            ('COLBACKGROUNDS', None, '一个要循环使用的颜色列表。'),
            ('VALIGN', None, '取 TOP, MIDDLE 或默认的 BOTTOM 中的一个。'),
        ]
    )
    table.setStyle(
        [
            ('FONT', (0, 0), (-1, 1), 'SourceHanSans-Normal', 10, 12),
            ('FONT', (0, 1), (-1, -1), 'SourceHanSans-ExtraLight', 8, 8),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
    pdf.add_paragraph("")
    pdf.add_flowable(table)
    pdf.add_paragraph(
        '这将设置相关单元格的背景颜色。' '下面的例子显示了 $BACKGROUND$ 和 $TEXTCOLOR$ 命令的作用。'
    )
    pdf.add_embedded_code(
        """
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib import colors

data=  [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]
t=Table(data)
t.setStyle(TableStyle([('BACKGROUND',(1,1),(-2,-2),colors.green),
                        ('TEXTCOLOR',(0,0),(1,-1),colors.red)]))
"""
    )
    pdf.add_paragraph('为了看到对齐样式的效果，我们需要一些宽度和网格，但应该很容易看到样式的来源。')
    pdf.add_embedded_code(
        """
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

data =  [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]
t = Table(data,5*[0.4*inch], 4*[0.4*inch])
t.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                        ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                        ('VALIGN',(0,0),(0,-1),'TOP'),
                        ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                        ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                        ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                        ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                        ]))
"""
    )

    pdf.add_heading('$TableStyle$ Line Commands', level=3)
    pdf.add_paragraph(
        '线条命令以标识符、起始和终止单元格坐标开始，'
        '并始终以所需线条的厚度（以点为单位）和颜色跟随。'
        '颜色可以是名称，也可以指定为$(R, G, B)$元组，'
        '其中$R,G和B$是浮动数，(0, 0, 0)是黑色。行命令名称为 '
        '$GRID, BOX, OUTLINE, INNERGRID, LINEBELOW, '
        'LINEABOVE, LINEBEFORE 和 LINEAFTER$。'
        '$BOX和OUTLINE$相等，'
        '$GRID$相当于同时应用 $BOX 和 INNERGRID$。'
    )
    pdf.add_cond_page_break(4.0)
    pdf.add_paragraph('我们可以通过下面的例子看到一些行命令的作用。')

    pdf.add_embedded_code(
        """
from reportlab.platypus.tables import Table
from reportlab.lib import colors

data=  [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]

t=Table(data,style=[('GRID',(1,1),(-2,-2),1,colors.green),
                    ('BOX',(0,0),(1,-1),2,colors.red),
                    ('LINEABOVE',(1,2),(-2,2),1,colors.blue),
                    ('LINEBEFORE',(2,1),(2,-2),1,colors.pink),
                    ])
"""
    )
    pdf.add_paragraph('行命令在拆分表格时，会给表格带来问题；下面的例子显示了一个表格在不同位置被拆分的情况')

    pdf.add_embedded_code(
        """
from reportlab.platypus.tables import Table
from reportlab.lib import colors

data=  [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]
t=Table(data,style=[
                ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                ('GRID',(1,1),(-2,-2),1,colors.green),
                ('BOX',(0,0),(1,-1),2,colors.red),
                ('BOX',(0,0),(-1,-1),2,colors.black),
                ('LINEABOVE',(1,2),(-2,2),1,colors.blue),
                ('LINEBEFORE',(2,1),(2,-2),1,colors.pink),
                ('BACKGROUND', (0, 0), (0, 1), colors.pink),
                ('BACKGROUND', (1, 1), (1, 2), colors.lavender),
                ('BACKGROUND', (2, 2), (2, 3), colors.orange),
                ])
    """
    )
    table = pdf.store[-1]
    pdf.add_flowable(Spacer(0, 6))
    for s in table.split(4 * inch, 30):
        pdf.add_flowable(s)
        pdf.add_flowable(Spacer(0, 6))
    pdf.add_flowable(Spacer(0, 6))

    for s in table.split(4 * inch, 36):
        pdf.add_flowable(s)
        pdf.add_flowable(Spacer(0, 6))

    pdf.add_paragraph('当在第一行或第二行进行拆分和分割时。')
    pdf.add_cond_page_break(4.0)
    pdf.add_heading('复杂的单元格值', level=3)
    pdf.add_paragraph(
        '如上所述，我们可以有复杂的单元格值，'
        '包括$Paragraphs$，$Images$和其他$Flowables$或相同的列表。'
        '要看到这个操作，请考虑下面的代码和它产生的表格。'
        '请注意，$Image$的背景是白色的，这将会遮挡住您为单元格选择的任何背景。'
        '为了得到更好的效果，你应该使用透明的背景。'
    )
    img = 'images/replogo.gif'
    pdf.add_embedded_code(
        """
from reportlab.platypus.flowables import Image
from reportlab.platypus import Paragraph
from reportlab.platypus.tables import Table
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle

I = Image('{}')
I.drawHeight = 1.25*inch*I.drawHeight / I.drawWidth
I.drawWidth = 1.25*inch

normal_style = ParagraphStyle(
    name='Normal',
    fontName='SourceHanSans-Light',
    fontSize=10,
    leading=12,
    spaceBefore=6,
)
_body_text = ParagraphStyle(
    name='BodyText',
    parent=normal_style,
    spaceBefore=6,
)

P0 = Paragraph('''
               <b>A pa<font color=red>r</font>a<i>graph</i></b>
               <super><font color=yellow>1</font></super>''',
               _body_text)
P = Paragraph('''
       <para align=center spaceb=3>The <b>ReportLab Left
       <font color=red>Logo</font></b>
       Image</para>''',
       _body_text)
data=  [['A',   'B', 'C',     P0, 'D'],
        ['00', '01', '02', [I,P], '04'],
        ['10', '11', '12', [P,I], '14'],
        ['20', '21', '22',  '23', '24'],
        ['30', '31', '32',  '33', '34']]

t=Table(data,style=[('GRID',(1,1),(-2,-2),1,colors.green),
                    ('BOX',(0,0),(1,-1),2,colors.red),
                    ('LINEABOVE',(1,2),(-2,2),1,colors.blue),
                    ('LINEBEFORE',(2,1),(2,-2),1,colors.pink),
                    ('BACKGROUND', (0, 0), (0, 1), colors.pink),
                    ('BACKGROUND', (1, 1), (1, 2), colors.lavender),
                    ('BACKGROUND', (2, 2), (2, 3), colors.orange),
                    ('BOX',(0,0),(-1,-1),2,colors.black),
                    ('GRID',(0,0),(-1,-1),0.5,colors.black),
                    ('VALIGN',(3,0),(3,0),'BOTTOM'),
                    ('BACKGROUND',(3,0),(3,0),colors.limegreen),
                    ('BACKGROUND',(3,1),(3,1),colors.khaki),
                    ('ALIGN',(3,1),(3,1),'CENTER'),
                    ('BACKGROUND',(3,2),(3,2),colors.beige),
                    ('ALIGN',(3,2),(3,2),'LEFT'),
                    ])

t._argW[3]=1.5*inch
    """.format(
            img
        )
    )
    pdf.add_heading('$TableStyle$ 跨单元格命令', level=3)

    pdf.add_paragraph('我们的$Table$类支持跨度的概念，但它的指定方式与html不同。样式规范')
    pdf.add_code_eg(
        """
    SPAN, (sc,sr), (ec,er)
    """
    )
    pdf.add_paragraph(
        '表示列 $sc$ - $ec$ 和行 $sr$ - $er$ 中的单元格应该合并成一个超级单元格，'
        '其内容由单元格 $(sc, sr)$ 决定。'
        '其他单元格应该存在，但应该包含空字符串，否则可能会得到意想不到的结果。'
    )
    pdf.add_embedded_code(
        """
from reportlab.platypus.tables import Table
from reportlab.lib import colors

data=  [['Top\\nLeft', '', '02', '03', '04'],
        ['', '', '12', '13', '14'],
        ['20', '21', '22', 'Bottom\\nRight', ''],
        ['30', '31', '32', '', '']]
t=Table(data,style=[
                ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                ('BACKGROUND',(0,0),(1,1),colors.palegreen),
                ('SPAN',(0,0),(1,1)),
                ('BACKGROUND',(-2,-2),(-1,-1), colors.pink),
                ('SPAN',(-2,-2),(-1,-1)),
                ])
    """
    )
    pdf.add_paragraph('注意到我们的$GRID$命令不需要太保守。跨越的单元格不会被画穿。')

    pdf.add_heading('$TableStyle$ 其他命令', level=3)
    pdf.add_paragraph('要控制 $Table$ 的拆分，可以使用 $NOSPLIT$ 命令。')
    pdf.add_code_eg(
        """
    NOSPLIT, (sc,sr), (ec,er)
    """
    )
    pdf.add_paragraph('要求列 $sc$-$ec$ 和行 $sr$-$er$ 中的单元格不能被拆分。')

    pdf.add_heading('$TableStyle$ 特殊的指标', level=3)
    pdf.add_paragraph(
        "在任何样式命令中，第一行索引可以设置为特殊字符串^splitlast^或^splitfirst^中的一个，"
        "以表明该样式只用于拆分表的最后一行或延续表的第一行。"
        "这样可以使拆分表在拆分后有更好的效果。"
    )


def chapter8_flowables(pdf):
    pdf.add_heading("$Flowables$", level=1)
    pdf.add_paragraph('下列$flowable$使您可以在包装文本时有条件地求值并执行表达式和语句：')

    pdf.add_heading("DocAssign", level=2)
    pdf.add_paragraph("定义: ")
    pdf.add_code_eg("DocAssign(self, var, expr, life='forever')")
    pdf.add_paragraph('为表达式$expr$指定一个名称为$var$的变量。例如：')
    pdf.add_code_eg("DocAssign('i',3)")

    pdf.add_heading("DocExec", level=2)
    pdf.add_paragraph("定义:")
    pdf.add_code_eg("DocExec(self, stmt, lifetime='forever')")
    pdf.add_paragraph('执行语句$stmt$。例如：')
    pdf.add_code_eg("DocExec('i-=1')")

    pdf.add_heading("$DocPara$", level=2)
    pdf.add_paragraph("定义:")
    pdf.add_code_eg(
        "DocPara(self, expr, format=None, style=None, klass=None, escape=True)"
    )
    pdf.add_paragraph(
        '创建一个以 $expr$ 的值为文本的段落。'
        '如果指定了格式，它应该使用 %($__expr__$)s 对表达式 $expr$ (如果有的话) 进行字符串插值。'
        '它也可以使用%($name$)s对命名空间中的其他变量进行插值。'
        '例如'
    )
    pdf.add_code_eg(
        "DocPara('i',format='The value of i is %(__expr__)d',style=normal)"
    )
    pdf.add_heading("DocAssert", level=2)
    pdf.add_paragraph("定义:")
    pdf.add_code_eg("DocAssert(self, cond, format=None)")
    pdf.add_paragraph("如果$cond$评价为$False$，则引发包含$format$字符串的$AssertionError$。")
    pdf.add_code_eg("DocAssert(val, 'val is False')")

    pdf.add_heading("DocIf", level=2)
    pdf.add_paragraph("定义:")
    pdf.add_code_eg("DocIf(self, cond, thenBlock, elseBlock=[])")
    pdf.add_paragraph(
        '如果$cond$的值为$True$，那么这个flowable就会被$thenBlock$ elsethe $elseBlock$取代。'
    )
    pdf.add_code_eg(
        """
DocIf('i>3',Paragraph('The value of i is larger than 3',normal),\\
        Paragraph('The value of i is not larger than 3',normal))
"""
    )

    pdf.add_heading("DocWhile", level=2)
    pdf.add_paragraph("定义:")
    pdf.add_code_eg("DocWhile(self, cond, whileBlock)")
    pdf.add_paragraph("当$cond$值为$True$时，运行$whileBlock$。例如：")
    pdf.add_code_eg(
        """
    DocAssign('i',5)
    DocWhile('i',[DocPara('i',format='The value of i is %(__expr__)d',style=normal),DocExec('i-=1')])
    """
    )
    pdf.add_paragraph('这个例子产生的一组段落的形式是：')
    pdf.add_code_eg(
        """
    The value of i is 5
    The value of i is 4
    The value of i is 3
    The value of i is 2
    The value of i is 1
    """
    )

    pdf.add_heading("其他有用的$Flowables$", level=1)
    pdf.add_heading("Preformatted", level=2)
    pdf.add_paragraph("定义:")
    pdf.add_code_eg(
        "Preformatted(text, style, bulletText=None, dedent=0, maxLineLength=None, splitChars=None, newLineChars=None)"
    )
    pdf.add_paragraph(
        '创建一个预格式化的段落，不进行任何包装、分行或其他操作。'
        '在文本中不考虑$XML$样式标签。'
        '如果dedent是非零，$dedent$的公共前导空格将从每行前面移除。'
    )

    pdf.add_heading("定义最大行长", level=3)
    pdf.add_paragraph('您可以使用属性 $maxLineLength$ 来定义最大行长。' '如果行长超过这个最大值，行将被自动分割。')
    pdf.add_paragraph(
        '行将被分割成$splitChars$中定义的任何一个字符。'
        '如果没有为该属性提供值，'
        '则行将在以下任何标准字符上进行分割：空格、冒号、句号、分号、逗号、连字符、前斜线、后斜线、左括号、左方括号和左大括号。'
    )
    pdf.add_paragraph('字符可以自动插入到已创建的每一行的开头。你可以设置属性$newLineChars$为你想使用的字符。')
    pdf.add_embedded_code(
        """
from reportlab.platypus.flowables import Preformatted
from reportlab.lib.styles import getSampleStyleSheet

stylesheet=getSampleStyleSheet()
normalStyle = stylesheet['Code']
text='''
class XPreformatted(Paragraph):
    def __init__(self, text, style, bulletText = None, frags=None, caseSensitive=1):
        self.caseSensitive = caseSensitive
        if maximumLineLength and text:
            text = self.stopLine(text, maximumLineLength, splitCharacters)
        cleaner = lambda text, dedent=dedent: ''.join(_dedenter(text or '',dedent))
        self._setup(text, style, bulletText, frags, cleaner)
'''
t=Preformatted(text,normalStyle,maxLineLength=60, newLineChars='> ')
    """
    )

    pdf.add_heading("XPreformatted", level=2)
    pdf.add_paragraph("定义:")
    pdf.add_code_eg(
        "$XPreformatted(text, style, bulletText=None, dedent=0, frags=None)"
    )
    pdf.add_paragraph(
        '这是$Paragraph$类的一种非重排形式；'
        '$text$中允许使用XML标签，其含义与$Paragraph$类相同。'
        '至于 $Preformatted$，如果dedent是非零，$dedent$普通的前导空格将从每行的前面移除。'
    )

    pdf.add_embedded_code(
        """
from reportlab.platypus import XPreformatted
from reportlab.lib.styles import getSampleStyleSheet

stylesheet=getSampleStyleSheet()
normalStyle = stylesheet['Code']
text='''

   This is a non rearranging form of the <b>Paragraph</b> class;
   <b><font color=red>XML</font></b> tags are allowed in <i>text</i> and have the same

      meanings as for the <b>Paragraph</b> class.
   As for <b>Preformatted</b>, if dedent is non zero <font color="red" size="+1">dedent</font>
       common leading spaces will be removed from the
   front of each line.
   You can have &amp;amp; style entities as well for &amp; &lt; &gt; and &quot;.

'''
t=XPreformatted(text,normalStyle,dedent=3)
"""
    )

    pdf.add_heading("$Image$", level=2)
    pdf.add_paragraph("定义:")
    pdf.add_code_eg("Image(filename, width=None, height=None)")
    pdf.add_paragraph(
        '创建一个 $flowable$，它将包含由文件 $filename$ 中的数据定义的图像，'
        '该文件可以是文件路径、类似文件的对象或 $reportlab.graphics.shapes.Drawing$的实例。'
        '默认的 <b>PDF</b> 图像类型<i>jpeg</i>被支持，'
        '如果安装了<b>PIL</b>扩展到<b>Python</b>，其他图像类型也可以被处理。'
        '如果指定了 $width$和$height$，那么它们决定了显示图像的尺寸，单位是<i>points</i>。'
        '如果没有指定任何一个尺寸(或者指定为$None$)，那么图像的相应像素尺寸被假定为<i>points</i>并使用。'
    )
    img = "images/lj8100.jpg"
    pdf.add_code_eg(
        """
    Image("{}")
    """.format(
            img
        ),
        after=0.1,
    )
    pdf.add_paragraph('将显示为')
    pdf.add_flowable(Image(img))
    pdf.add_paragraph("然而")

    pdf.add_code_eg(
        """
im = Image("{}", width=2*inch, height=2*inch)
im.hAlign = 'CENTER'
""".format(
            img
        ),
        after=0.1,
    )
    pdf.add_paragraph("产出")
    im = Image(img, width=2 * inch, height=2 * inch)
    im.hAlign = 'CENTER'
    pdf.add_flowable(im)

    pdf.add_heading("$Spacer$", level=2)
    pdf.add_paragraph("定义:")
    pdf.add_code_eg("Spacer(width, height)")
    pdf.add_paragraph('这与预期的一样，它为$story$增加了一定的空间。目前，这只对垂直空间有效。')
    pdf.add_cond_page_break(1)

    pdf.add_heading("PageBreak", level=2)
    pdf.add_paragraph(
        '这个 $Flowable$ 代表了一个页面中断。'
        '它的工作原理是有效地消耗所有给它的垂直空间。'
        '这对于单个 $Frame$ 文档来说已经足够了，但对于多个框架来说，'
        '这只是一个框架中断，所以 $BaseDocTemplate$ 机制会在内部检测到 $pageBreaks$ 并进行特殊处理。'
    )
    pdf.add_cond_page_break(1)

    pdf.add_heading("CondPageBreak", level=2)
    pdf.add_paragraph("定义:")
    pdf.add_code_eg("CondPageBreak(height)")
    pdf.add_paragraph(
        '如果当前的$Frame$中没有足够的垂直空间，'
        '那么这个$Flowable$试图强制$Frame$断裂。'
        '因此，它的命名可能是错误的，也许应该重新命名为$CondFrameBreak$。'
    )
    pdf.add_cond_page_break(1)

    pdf.add_heading("KeepTogether", level=2)
    pdf.add_paragraph("定义:")
    pdf.add_code_eg("KeepTogether(flowables)")
    pdf.add_paragraph(
        '这个复合的 $Flowable$ 接收一个 $Flowables$ 的列表，'
        '并试图将它们放在同一个 $Frame$ 中。'
        '如果列表中 $flowables$ 中的 $Flowables$ 的总高度超过了当前框架的可用空间，'
        '那么所有的空间都会被使用，并且会强制中断框架。'
    )
    pdf.add_cond_page_break(1)

    pdf.add_heading("TableOfContents", level=2)
    pdf.add_paragraph("定义:")
    pdf.add_code_eg("TableOfContents()")
    pdf.add_paragraph(
        '通过使用$TableOfContents$ flowable 可以生成一个目录。下面的步骤是在您的文档中添加一个目录表所需要的。'
    )
    pdf.add_paragraph('创建一个 $TableOfContents$ 的实例。覆盖关卡样式（可选）并将对象添加到$story$中。')

    pdf.add_code_eg(
        """
    toc = TableOfContents()
    PS = ParagraphStyle
    toc.levelStyles = [
        PS(fontName='Times-Bold', fontSize=14, name='TOCHeading1',
                leftIndent=20, firstLineIndent=-20, spaceBefore=5, leading=16),
        PS(fontSize=12, name='TOCHeading2',
                leftIndent=40, firstLineIndent=-20, spaceBefore=0, leading=12),
        PS(fontSize=10, name='TOCHeading3',
                leftIndent=60, firstLineIndent=-20, spaceBefore=0, leading=12),
        PS(fontSize=10, name='TOCHeading4',
                leftIndent=100, firstLineIndent=-20, spaceBefore=0, leading=12),
    ]
    story.append(toc)
    """
    )
    pdf.add_paragraph(
        '对目录的输入可以通过调用 '
        '$TableOfContents$ 对象的 $addEntry$ 方法手动完成，'
        '也可以通过在 $DocTemplate$ 的 $afterFlowable$ 方法中自动发送一个 $\'TOCEntry\'$ 通知。'
        '传递给 $notify$ 的数据是一个由三个或四个项目组成的列表，'
        '其中包括一个级别号，条目文本，页码和一个可选的目标键，该条目应该指向。'
        '这个列表通常会在文档模板的方法中创建，'
        '比如afterFlowable()，使用notify()方法调用通知，'
        '并提供适当的数据，比如这样。'
    )

    pdf.add_code_eg(
        '''
    def afterFlowable(self, flowable):
        """Detect Level 1 and 2 headings, build outline,
        and track chapter title."""
        if isinstance(flowable, Paragraph):
            txt = flowable.getPlainText()
            if style == 'Heading1':
                # ...
                self.notify('TOCEntry', (0, txt, self.page))
            elif style == 'Heading2':
                # ...
                key = 'h2-%s' % self.seq.nextf('heading2')
                self.canv.bookmarkPage(key)
                self.notify('TOCEntry', (1, txt, self.page, key))
            # ...
    '''
    )
    pdf.add_paragraph(
        "这样，每当一个样式为 $'Heading1'$ 或 $'Heading2'$ 的段落被添加到故事中，它就会出现在目录中。"
        "$Heading2$ 条目将可点击，因为已经提供了一个书签键。"
    )
    pdf.add_paragraph(
        '最后你需要使用 $DocTemplate$ 的 $multiBuild$ 方法，因为内容表需要多次传递才能生成。'
    )
    pdf.add_code_eg("doc.multiBuild(story)")

    pdf.add_paragraph('下面是一个简单但可行的带目录的文档例子。')
    pdf.add_code_eg(
        '''
    from reportlab.lib.styles import ParagraphStyle as PS
    from reportlab.platypus import PageBreak
    from reportlab.platypus.paragraph import Paragraph
    from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
    from reportlab.platypus.tableofcontents import TableOfContents
    from reportlab.platypus.frames import Frame
    from reportlab.lib.units import cm
    
    class MyDocTemplate(BaseDocTemplate):
    
        def __init__(self, filename, **kw):
            self.allowSplitting = 0
            BaseDocTemplate.__init__(self, filename, **kw)
            template = PageTemplate('normal', [Frame(2.5*cm, 2.5*cm, 15*cm, 25*cm, id='F1')])
            self.addPageTemplates(template)
    
        def afterFlowable(self, flowable):
            "Registers TOC entries."
            if flowable.__class__.__name__ == 'Paragraph':
                text = flowable.getPlainText()
                style = flowable.style.name
                if style == 'Heading1':
                    self.notify('TOCEntry', (0, text, self.page))
                if style == 'Heading2':
                    self.notify('TOCEntry', (1, text, self.page))
    
    h1 = PS(name = 'Heading1',
           fontSize = 14,
           leading = 16)
    
    h2 = PS(name = 'Heading2',
           fontSize = 12,
           leading = 14,
           leftIndent = delta)
    
    # Build story.
    story = []
    toc = TableOfContents()
    # For conciseness we use the same styles for headings and TOC entries
    toc.levelStyles = [h1, h2]
    story.append(toc)
    story.append(PageBreak())
    story.append(Paragraph('First heading', h1))
    story.append(Paragraph('Text in first heading', PS('body')))
    story.append(Paragraph('First sub heading', h2))
    story.append(Paragraph('Text in first sub heading', PS('body')))
    story.append(PageBreak())
    story.append(Paragraph('Second sub heading', h2))
    story.append(Paragraph('Text in second sub heading', PS('body')))
    story.append(Paragraph('Last heading', h1))
    
    doc = MyDocTemplate('mintoc.pdf')
    doc.multiBuild(story)
    '''
    )
    pdf.add_cond_page_break(1)
    pdf.add_heading("$SimpleIndex$", level=2)
    pdf.add_paragraph("定义:")
    pdf.add_code_eg("SimpleIndex()")
    pdf.add_paragraph(
        '可以通过使用 $SimpleIndex$ flowable生成一个索引。' '下面的步骤是为您的文档添加索引所需要的。'
    )
    pdf.add_paragraph('在段落中使用索引标签来索引术语。')
    pdf.add_code_eg(
        '''
    story = []
    
    ...
    
    story.append('The third <index item="word" />word of this paragraph is indexed.')
    '''
    )
    pdf.add_paragraph('创建一个$SimpleIndex$的实例，并将其添加到你希望它出现的故事中。')
    pdf.add_code_eg(
        '''
    index = SimpleIndex(dot=' . ', headers=headers)
    story.append(index)
    '''
    )

    pdf.add_paragraph(
        '你可以传入 $SimpleIndex$ 构造函数的参数在 $reportlab$ 参考资料中解释。'
        '现在，使用^SimpleIndex.getCanvasMaker()^返回的$canvasmaker$来构建文档。'
    )
    pdf.add_code_eg(
        """
    doc.build(story, canvasmaker=index.getCanvasMaker())
    """
    )
    pdf.add_paragraph('要建立一个多级索引，请将一个以逗号分隔的项目列表传递给索引标签的 item 属性。')
    pdf.add_code_eg(
        """
    <index item="terma,termb,termc" />
    <index item="terma,termd" />
    """
    )
    pdf.add_paragraph(
        '$terma$ 将表示最顶层的术语，$termc$ 将表示最具体的术语，$terd$ 和 $termb$ 将出现在 $terma$ 的同一层次。'
    )
    pdf.add_paragraph(
        '如果您需要为一个包含逗号的术语编制索引，您需要将其加倍转义。'
        '为了避免三个连续逗号的歧义（一个转义逗号后面是一个列表分隔符或一个列表分隔符后面是一个转义逗号？）'
        '在正确的位置引入一个空格。'
        '术语开头或结尾的空格将被删除。'
    )
    pdf.add_code_eg(
        """
    <index item="comma(,,), ,, ,...   " />
    """
    )
    pdf.add_paragraph('此处索引了 "逗号（，）"、"，"和"...... "等术语。')

    pdf.add_heading("ListFlowable, ListItem", level=2)
    pdf.add_paragraph('使用这些类来制作有序和无序的列表。 列表可以被嵌套。')
    pdf.add_paragraph(
        '$ListFlowable()$ 将创建一个有序的列表，它可以包含任何可流动的。 '
        '该类有许多参数可以改变列表编号的字体、颜色、大小、样式和位置，或者无序列表中的项目符号。 '
        '还可以使用 $bulletType$ 属性将编号类型设置为使用小写或大写字母（\'A,B,C\'等）或罗马数字（大写或小写）。 '
        '要将列表改为无序类型，请设置 bulletType=\'bullet\'。'
    )
    pdf.add_paragraph(
        "在 $ListFlowable()$ 列表中的项目可以通过将它们包装在 $ListItem()$ 类中并设置其属性来改变它们的默认外观。"
    )
    pdf.add_paragraph('下面将创建一个有序列表，并将第三项设置为无序子列表。')

    pdf.add_embedded_code(
        """
from reportlab.platypus import ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.paragraph import Paragraph

styles = getSampleStyleSheet()
style = styles["Normal"]

t = ListFlowable(
    [
        Paragraph("Item no.1", style),
        ListItem(
            Paragraph("Item no. 2", style), bulletColor="green", value=7
        ),
        ListFlowable(
            [
                Paragraph("sublist item 1", style),
                ListItem(
                    Paragraph('sublist item 2', style),
                    bulletColor='red',
                    value='square',
                ),
            ],
            bulletType='bullet',
            start='square',
        ),
        Paragraph("Item no.4", style),
    ],
    bulletType='i',
)
"""
    )
    pdf.add_paragraph(
        '为了应对嵌套，$start$参数可以设置为一个可能的起始列表；'
        '对于$ul$来说，可接受的起始是任何$unicode字符$或$flowables.py$已知的特定名称，'
        '例如$bulletchar$、$circle$、$square$、$disc$、$diamond$、$diamondwx$、'
        '$rarrowhead$、$sparkle$、$squarelrs$或$blackstar$。'
        '对于$ol$来说，$start$可以是$\'1iaAI\'$中的任何字符，以表示不同的数字风格。'
    )

    pdf.add_heading("$BalancedColumns$", level=2)
    pdf.add_paragraph(
        '使用 $BalancedColumns$ 类来制作一个flowable，'
        '将其内容 $flowable$ 分割成两个或更多大小大致相等的列。'
        '实际上，$n$ 框架被合成为内容，而 $flowable$ 试图在它们之间平衡内容。'
        '当创建的框架总高度过大时，会被拆分，拆分后会保持平衡。'
    )
    pdf.add_code_eg(
        """
    from reportlab.platypus.flowables import BalancedColumns
    from reportlab.platypus.frames import ShowBoundaryValue
    F = [
        list of flowables........
        ]
    story.append(
        Balanced(
            F,          #the flowables we are balancing
            nCols = 2,  #the number of columns
            needed = 72,#the minimum space needed by the flowable
            spacBefore = 0,
            spaceAfter = 0,
            showBoundary = None,    #optional boundary showing
            leftPadding=None,       #these override the created frame
            rightPadding=None,      #paddings if specified else the
            topPadding=None,        #default frame paddings
            bottomPadding=None,     #are used
            innerPadding=None,      #the gap between frames if specified else
                                    #use max(leftPadding,rightPadding)
            name='',                #for identification purposes when stuff goes awry
            endSlack=0.1,           #height disparity allowance ie 10% of available height
            )
        )   
    """
    )


def chapter9_useful_flowables(pdf):
    pdf.add_heading("编写 $Flowable$ ")
    pdf.add_paragraph(
        '$Flowables$旨在成为创建可重复使用的报表内容的开放标准，您可以轻松创建自己的对象。 '
        '我们希望随着时间的推移，我们将建立一个贡献库，为 $reportlab$ 用户提供丰富的图表、图形和其他 "report widgets"选择，'
        '他们可以在自己的报表中使用。本节将向您展示如何创建您自己的 $flowables$。'
    )
    pdf.add_paragraph('我们应该把Figure类放在标准库中，因为它是一个非常有用的基础。')

    pdf.add_heading("一个非常简单的 $Flowable$", level=2)
    pdf.add_paragraph(
        '回想一下本用户指南中 $pdfgen$ 一节中的 $hand$ 函数，' '它生成了一个由贝塞尔曲线构成的闭合图形的手图。'
    )
    pdf.add_illustration(doc_examples.hand, "一只手")
    pdf.add_paragraph(
        '为了在 $Platypus flowable$ 中嵌入这个或其他绘图，'
        '我们必须定义一个 $Flowable$ 的子类，'
        '至少有一个$wrap$方法和一个$draw$方法。'
    )
    pdf.add_code_eg(doc_examples.testhandannotation)
    pdf.add_paragraph(
        '$wrap$方法必须提供绘图的大小'
        '-- $Platypus$ 主循环用它来决定这个元素是否适合当前框架的剩余空间。 '
        '在 $Platypus$ 主循环将 $(0,0)$ 原点转换到适当的框架中的适当位置后，'
        '$draw$方法将执行对象的绘制。'
    )
    pdf.add_paragraph('以下是 $HandAnnotation flowable$ 的一些使用示例。')
    pdf.add_hand_note()
    pdf.add_paragraph("默认情况下")
    pdf.add_hand_note(size=inch)
    pdf.add_paragraph('只是一寸高。')
    pdf.add_hand_note(
        xoffset=3 * inch,
        size=inch,
        strokecolor=colors.blue,
        fillcolor=colors.cyan,
    )
    pdf.add_paragraph('高1英寸，向左偏蓝和青色。')

    pdf.add_heading('修改内置的 $Flowable$', level=2)
    pdf.add_paragraph("要修改现有的可流动对象，您应该创建一个派生类并覆盖需要更改以获得所需行为的方法。")
    pdf.add_paragraph('作为创建旋转图像的示例，您需要覆盖现有 $Image$ 类的 $wrap$ 和 $draw$ 方法')

    img = 'images/replogo.gif'
    pdf.add_embedded_code(
        """
from reportlab.platypus.flowables import Image
class RotatedImage(Image):
    def wrap(self,availWidth,availHeight):
        h, w = Image.wrap(self,availHeight,availWidth)
        return w, h
    def draw(self):
        self.canv.rotate(90)
        Image.draw(self)
I = RotatedImage('{}')
I.hAlign = 'CENTER'
""".format(
            img
        ),
        name='I',
    )


def chapter10_graph(pdf):
    pdf.add_heading("绘制", level=1)
    pdf.add_heading("简介", level=2)
    pdf.add_paragraph(
        "$ReportLab Graphics$是$ReportLab$库的一个子包。"
        "它最初是作为一个独立的程序集，但现在是$ReportLab$工具包的一个完整的集成部分，"
        "它允许您使用其强大的图表和图形功能来改进您的PDF表格和报表。"
    )

    pdf.add_heading("一般概念", level=2)
    pdf.add_paragraph('在本节中，我们将介绍图形库的一些比较基本的原理，这些原理会在后面的各个地方出现。')

    pdf.add_heading("图纸和渲染器", level=3)
    pdf.add_paragraph(
        '^Drawing^是一个独立于平台的形状集合的描述。'
        '它不直接与$PDF, Postscript$或任何其他输出格式相关联。'
        '幸运的是，大多数矢量图形系统都遵循$Postscript$模型，'
        '因此可以毫不含糊地描述形状。'
    )
    pdf.add_paragraph(
        '一张图中包含了许多原始的^Shape^ (形状)。'
        '普通形状是那些广为人知的矩形、圆形、线条等。'
        '一个特殊的（逻辑）形状是 (组)，'
        '它可以容纳其他形状并对它们进行变换。'
        ' $Group$ 代表了 $Shape$ 的组合，并允许将 $Group$ '
        '合当作一个单一的 $Shape$ 来处理。'
        '几乎所有的东西都可以从少量的基本 $Shape$ (形状)建立起来。'
    )
    pdf.add_paragraph(
        '该包提供了几个^Renderers^ (渲染器)，它们知道如何将图纸绘制成不同的格式。'
        '其中包括 $PDF (renderPDF)$、$Postscript (renderPS)$ 和位图输出 $(renderPM)$。'
        '位图渲染器使用 $Raph Levien$ 的 ^libart^ 栅格化器'
        '和 $Fredrik Lundh$ 的 ^Python Imaging Library^ (PIL)。'
        '$SVG$ 渲染器使用了 $Python$ 的标准库 $XML$ 模块，'
        '所以你不需要安装 $XML-SIG$ 的附加包 $PyXML$。'
        '如果你安装了正确的扩展，你可以为网络生成位图形式的图画，'
        '也可以为 $PDF$ 文档生成矢量形式的图画，并得到 "相同的输出"。'
    )
    pdf.add_paragraph(
        '$PDF$ 渲染器具有特殊的 "特权" '
        '-- 一个 $Drawing$ 对象也是一个<i>Flowable</i>，'
        '因此，可以直接放在任何 $Platypus$ 文档的故事中，或者直接用一行代码在^Canvas^上绘制。'
        '此外，$PDF$ 渲染器还有一个实用功能，可以快速制作一页$PDF$文档。'
    )
    pdf.add_paragraph(
        '$SVG$ 渲染器很特别，因为它仍然是相当的实验性的。'
        '它所生成的 $SVG$ 代码并没有经过任何优化，'
        '只是将 $ReportLab Graphics (RLG)$ 中可用的功能映射到 $SVG$ 中。'
        '这意味着不支持 $SVG$ 动画、交互性、脚本或更复杂的剪切、遮罩或渐变形状。'
        '因此，请小心，并请报告您发现的任何错误。'
    )

    pdf.add_heading("坐标系统", level=3)
    pdf.add_paragraph(
        '在我们的$X-Y$坐标系中，$Y$ 方向从底部<i>向上</i>。'
        '这与 $PDF$、$Postscript$ 和数学符号一致。'
        '对人们来说，这似乎也更自然，尤其是在处理图表时。'
        '请注意，在其他图形模型中（如$SVG$），$Y$ 坐标点<i>向下</i>。'
        '对于 $SVG$ 渲染器来说，这实际上是没有问题的，'
        '因为它将根据需要对您的图纸进行翻转，'
        '因此您的 $SVG$ 输出看起来和预期的一样。'
    )
    pdf.add_paragraph(
        '$X$坐标一如既往地从左到右。'
        '到目前为止，似乎没有任何模型主张反方向'
        ' -- 至少目前还没有（似乎有一些有趣的例外，阿拉伯人在看时间序列图时...）。'
    )

    pdf.add_heading("开始", level=3)
    pdf.add_paragraph(
        '让我们创建一个简单的图形，包含字符串 "Hello World "和一些特殊的字符，'
        '显示在一个彩色的矩形之上。'
        '创建完成后，我们将把图画保存到一个独立的PDF文件中。'
    )
    pdf.add_code_eg(
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
    pdf.add_paragraph('这将产生一个包含以下图形的PDF文件。')
    pdf.add_draw(testshapes.getDrawing01(), "'Hello World'")
    pdf.add_paragraph(
        '每个渲染器都可以做任何适合其格式的事情，并且可以有任何需要的API。'
        '如果它指的是一种文件格式，它通常有一个 $drawToFile$ 函数，'
        '这就是你需要知道的关于渲染器的所有信息。'
        '让我们以 $Encapsulated Postscript$ 格式保存同一张图。'
    )
    pdf.add_code_eg(
        """
        from reportlab.graphics import renderPS
        renderPS.drawToFile(d, 'example1.eps')
    """
    )
    pdf.add_paragraph(
        '这将生成一个具有相同图形的EPS文件，'
        '可以导入到Quark Express等出版工具中。'
        '如果我们想生成同样的图形作为网站的位图文件，'
        '比如说，我们需要做的就是写这样的代码。'
    )
    pdf.add_code_eg(
        """
        from reportlab.graphics import renderPM
        renderPM.drawToFile(d, 'example1.png', 'PNG')
    """
    )
    pdf.add_paragraph(
        '许多其他的位图格式，如GIF、JPG、TIFF、BMP和PPN都是真正可用的，'
        '这使得你不太可能需要添加外部的后处理步骤来转换为你需要的最终格式。'
    )
    pdf.add_paragraph(
        '要生成一个包含相同图形的SVG文件，并将其导入到 $Illustrator$ 等图形编辑工具中，' '我们需要做的就是编写这样的代码。'
    )
    pdf.add_code_eg(
        """
        from reportlab.graphics import renderSVG
        renderSVG.drawToFile(d, 'example1.svg')
    """
    )

    pdf.add_heading("属性验证", level=3)
    pdf.add_paragraph(
        'Python是非常动态的，让我们在运行时执行的语句很容易成为意外行为的来源。'
        '一个微妙的 "错误 "是当分配到一个框架不知道的属性时，因为使用的属性的名字包含了一个错别字。'
        'Python 让你可以逃过一劫(比如说，给一个对象添加一个新的属性)，'
        '但图形框架在不采取特殊对策的情况下，是不会检测到这个"错别字"的。'
    )
    pdf.add_paragraph(
        '有两种验证技术可以避免这种情况。'
        '默认情况下，每个对象在运行时都会检查每一次赋值，这样你就只能赋值给 "合法"的属性。'
        '这就是默认情况。由'
        '于这样做会带来很小的性能损失，所以在你需要的时候可以关闭这种行为。'
    )
    pdf.add_code_eg(
        """
    >>> r = Rect(10,10,200,100, fillColor=colors.red)
    >>>
    >>> r.fullColor = colors.green # note the typo
    >>> r.x = 'not a number'       # illegal argument type
    >>> del r.width                # that should confuse it
    """
    )
    pdf.add_paragraph(
        '这些语句在静态类型的语言中会被编译器捕获，'
        '但是 Python 让你摆脱了它。'
        '第一个错误可能会让你盯着图片想弄清楚为什么颜色是错的。'
        '第二个错误可能只有在以后，当一些后端试图绘制矩形时才会变得清晰。'
        '第三种错误，虽然可能性较小，但会导致一个不知道如何绘制的无效对象。'
    )
    pdf.add_code_eg(
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
    pdf.add_paragraph(
        '这将带来性能上的惩罚，所以当你需要这种行为时，可以将其关闭。'
        '要做到这一点，您应该在第一次导入 ^reportlab.graphics.shapes^ 之前使用以下代码行。'
    )
    pdf.add_code_eg(
        """
    >>> import reportlab.rl_config
    >>> reportlab.rl_config.shapeChecking = 0
    >>> from reportlab.graphics import shapes
    >>>
    """
    )

    pdf.add_paragraph(
        '一旦你关闭了 ^reportlab.rl_config.shapeChecking^，'
        '类实际上是在没有验证钩子的情况下构建的；'
        '那么，代码应该会变得更快。'
        '目前，对成批图表的惩罚似乎是25%，所以几乎不值得禁用。'
        '然而，如果我们将来把渲染器转移到C语言上（这是很有可能的），'
        '剩下的75%就会缩减到几乎没有，而且从验证中节省的成本也会很可观。'
    )
    pdf.add_paragraph(
        '每个对象，包括绘图本身，都有一个$verify()$方法。'
        '这个方法要么成功，要么引发一个异常。'
        '如果你关闭了自动验证，那么你应该在开发代码时，'
        '在测试中明确地调用 $verify()$，'
        '或者在一个批处理中调用一次。'
    )

    pdf.add_heading("属性编辑", level=3)
    pdf.add_paragraph(
        '我们将在下面介绍的 $reportlab/graphics$ 的一个基石是，'
        '你可以自动记录 $widget$ 。'
        '这意味着你可以掌握它们所有的可编辑属性，包括它们的子组件。'
    )
    pdf.add_paragraph(
        '另一个目标是能够为图纸创建GUI和配置文件。'
        '可以建立一个通用的GUI来显示图纸的所有可编辑的属性，'
        '并让你修改这些属性并查看结果。'
        '$Visual Basic$ 或 $Delphi$ 开发环境是这类东西的好例子。'
        '在批处理图表应用程序中，一个文件可以列出图表中所有组件的所有属性，'
        '并与数据库查询合并，以制作一批图表。'
        '另一个目标是能够为图纸创建GUI和配置文件。'
        '可以建立一个通用的GUI来显示图纸的所有可编辑的属性，'
        '并让你修改这些属性并查看结果。'
        '$Visual Basic$ 或 $Delphi$ 开发环境是这类东西的好例子。'
        '在批处理图表应用程序中，一个文件可以列出图表中所有组件的所有属性，'
        '并与数据库查询合并，以制作一批图表。'
    )
    pdf.add_paragraph(
        '为了支持这些应用，我们有两个接口，'
        '$getProperties$ 和 $setProperties$，'
        '以及一个方便的方法$dumpProperties$。'
        '第一个方法返回一个对象的可编辑属性的字典；'
        '第二个方法则集体设置这些属性。'
        '如果一个对象有公开的 "子对象"，那么我们也可以递归地设置和获取它们的属性。'
        '当我们稍后看^Widgets^时，这将更有意义，但我们需要将支持放到框架的基础上。'
    )
    pdf.add_code_eg(
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
    pdf.add_pencil_note()
    pdf.add_text_note(
        '$pprint$ 是标准的Python库模块，它允许您在多行上 "漂亮地打印" 输出，而不是只有一行很长的内容。'
    )
    pdf.add_paragraph(
        '这三种方法在这里似乎并没有什么作用，' '但正如我们将看到的那样，' '它们使我们的 $widgets$ 框架在处理非原始对象时更加强大。'
    )
    pdf.add_heading("Children 命名", level=3)
    pdf.add_paragraph(
        '您可以将对象添加到$Drawing$和$Group$对象中。'
        '这些对象通常会进入一个内容列表中。'
        '然而，你也可以在添加对象时给它们一个名字。'
        '这允许您在构造一个绘图后引用并可能改变它的任何元素。'
    )
    pdf.add_code_eg(
        """
    >>> d = shapes.Drawing(400, 200)
    >>> s = shapes.String(10, 10, 'Hello World')
    >>> d.add(s, 'caption')
    >>> s.caption.text
    'Hello World'
    >>>
    """
    )
    pdf.add_paragraph(
        '请注意，您可以在绘图中的多个上下文中使用相同的形状实例；'
        '如果您选择在许多位置（如散点图【scatter plot】）使用相同的$Circle$对象，'
        '并使用不同的名称来访问它，它仍然是一个共享对象，'
        '并且更改将是全局的。'
    )
    pdf.add_paragraph('这为创建和修改交互式图纸提供了一种范式。')

    pdf.add_heading("图表", level=2)
    pdf.add_paragraph(
        '其中大部分的动机是为了创建一个灵活的图表包。' '本节将介绍我们的图表模型背后的想法，' '设计目标是什么，以及图表包的哪些组件已经存在。'
    )
    pdf.add_heading("设计目标", level=3)
    pdf.add_paragraph('以下是一些设计目标。')
    pdf.add_paragraph('让简单的顶层使用变得真正简单')
    pdf.add_paragraph(
        '<para lindent="+36">应该可以用最少的代码行来创建一个简单的图表，'
        '并通过合理的自动设置让它 "做正确的事情"。'
        '上面的饼图片段就是这样做的。'
        '如果一个真正的图表有许多子组件，'
        '您仍然不需要与它们交互，除非您想自定义它们的功能。</para>'
    )
    pdf.add_paragraph('允许精确定位')
    pdf.add_paragraph(
        '<para lindent="+36">在出版和平面设计中，一个绝对的要求是控制每个元素的位置和风格。'
        '我们会尽量让属性以固定的尺寸和绘图比例来指定事物，'
        '而不是有自动调整大小的功能。'
        '因此，当你把y标签的字体大小变大时，"内图矩形" 不会神奇地改变，'
        '即使这意味着你的标签可以溢出图表矩形的左边缘。'
        '你的工作是预览图表，并选择能用的大小和空间。</para>'
    )
    pdf.add_paragraph(
        '<para lindent="+36">有些事情确实需要自动完成。'
        '例如，如果你想在一个200点的空间里放进N个条形图，而事先又不知道N，'
        '我们就把条形图的分隔指定为条形图宽度的百分比，而不是一个点的大小，让图表来计算。'
        '这样做还是具有确定性和可控性的。</para>'
    )
    pdf.add_paragraph("单独或分组控制子元素")
    pdf.add_paragraph(
        '<para lindent="+36">我们使用智能集合类，让你自定义一组东西，或者只是其中的一个。'
        '例如你可以在我们的实验饼图中这样做。</para>'
    )
    pdf.add_embedded_code(
        """
from reportlab.graphics.shapes import Drawing, Circle
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.textlabels import Label
from reportlab.lib import colors

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
    """,
        name='d',
    )
    pdf.add_paragraph(
        '<para lindent="+36"> $pc.slices[3]$ 实际上是懒惰地创建了一个小对象，'
        '它保存了有关片子的信息；'
        '如果有第四个片子的话，这个对象将在绘制时被用来格式化。</para>'
    )
    pdf.add_paragraph("只揭露你应该改变的事情")
    pdf.add_paragraph(
        '<para lindent="+36">从统计学的角度来看，让你直接调整上面例子中的一个饼片的角度是错误的，因为这是由数据决定的。'
        '所以并不是所有的东西都会通过公共属性暴露出来。'
        '可能会有 "后门 "让你在真正需要的时候违反这一点，'
        '或者提供高级功能的方法，但一般来说，属性会是正交的。</para>'
    )
    pdf.add_paragraph("组成和成分")
    pdf.add_paragraph(
        '<para lindent="+36">图表是由可重复使用的儿童部件构建的。'
        '图例是一个易于掌握的例子。'
        '如果你需要一个特殊类型的图例（例如圆形色板），'
        '你应该将标准的图例部件子类化。然后你可以做一些像...</para>'
    )
    pdf.add_code_eg(
        """
    c = MyChartWithLegend()
    c.legend = MyNewLegendClass()    # just change it
    c.legend.swatchRadius = 5    # set a property only relevant to the new one
    c.data = [10,20,30]   #   and then configure as usual...
    """
    )
    pdf.add_paragraph(
        '<para lindent="+36">...或者创建/修改你自己的图表或绘图类，默认创建其中一个。'
        '这对于时间序列图来说也是非常重要的，因为在时间序列图中，X轴可以有很多样式。</para>'
    )
    pdf.add_paragraph(
        '<para lindent="+36">'
        '顶层图表类会创建一些这样的组件，然后调用方法或设置私有属性来告诉它们的高度和位置'
        '--所有这些东西都应该为你做，而你无法定制。'
        '我们正在努力模拟这些组件应该是什么，'
        '并将在达成共识后在这里发布它们的API。</para>'
    )
    pdf.add_paragraph("倍数")
    pdf.add_paragraph(
        '<para lindent="+36">组件方法的一个必然结果是，'
        '你可以用多个图表或自定义数据图形来创建图表。'
        '我们最喜欢的例子是我们图库中由用户贡献的天气报告；'
        '我们希望能够轻松创建这样的图，将构件与它们的图例挂钩，'
        '并以一致的方式提供这些数据。</para>'
    )
    pdf.add_paragraph(
        '<para lindent="+36">(如果你想看图片，可以在我们的网站上找到。'
        '<font color="blue">'
        '<a href="https://www.reportlab.com/media/imadj/'
        'data/RLIMG_e5e5cb85cc0a555f5433528ac38c5884.PDF">'
        '这儿</a></font>)</para>'
    )

    pdf.add_heading("概述", level=3)
    pdf.add_paragraph(
        '图表或图是一个放置在图纸上的对象，' '它本身不是一个图纸。因此，你可以控制它的位置，在同一张图上放几个，或者添加注释。'
    )
    pdf.add_paragraph(
        '图表有两个轴，轴可以是 $Value$ 轴或 $Category$ 轴。'
        '轴又有一个 Labels 属性，可以让你配置所有的文本标签或单独配置每个标签。'
        '不同图表的大多数配置细节都与轴属性或轴标签有关。'
    )
    pdf.add_paragraph(
        '对象通过上一节中讨论的接口暴露出属性；'
        '这些都是可选的，是为了让最终用户配置外观。'
        '为了使图表工作而必须设置的东西，'
        '以及图表和它的组件之间的基本通信，都是通过方法来处理的。'
    )
    pdf.add_paragraph('你可以对任何图表组件进行子类化，' '并使用你的替代品来代替原来的组件，只要你实现了基本的方法和属性。')

    pdf.add_heading("$Labels$ 属性", level=3)
    pdf.add_paragraph(
        '标签是附加在某些图表元素上的一串文本。'
        '它们用于坐标轴、标题或坐标轴旁，或附加到单个数据点上。'
        '标签可以包含换行符，但只能用一种字体。'
    )
    pdf.add_paragraph(
        '标签的文本和 "origin" 通常由其父对象设置。'
        '它们是通过方法而不是属性来访问的。'
        '因此，X轴决定了每个刻度线标签的 "reference point" （参考点）'
        '和每个标签的数字或日期文本。'
        '然而，最终用户可以直接设置标签（或标签集合）的属性，'
        '以影响其相对于该原点的位置及其所有格式化。'
    )
    pdf.add_embedded_code(
        """
from reportlab.graphics.shapes import Drawing, Circle
from reportlab.graphics.charts.textlabels import Label
from reportlab.lib import colors

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
lab.setText('Some\\nMulti-Line\\nLabel')

d.add(lab)
    """,
        name='d',
    )
    pdf.add_paragraph('在上图中，标签是相对于绿色小球定义的。文本框的东北角应在原点向下10点，并围绕该角旋转45度。')
    pdf.add_paragraph('目前，标签具有以下特性，我们认为这些特性对我们迄今所看到的所有图表都是足够的。')

    attr_style = TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'SourceHanSans-Normal', 10, 12),
            ('FONT', (0, 1), (0, -1), 'Courier', 8, 8),
            ('FONT', (1, 1), (1, -1), 'SourceHanSans-ExtraLight', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )

    attributes = [
        ["属性", "描述"],
        ["dx", "标签的 X 位移。\nThe label's x displacement."],
        ["dy", "标签的 Y 位移。\nThe label's y displacement."],
        [
            "angle",
            "标签的旋转角度（逆时针）。\n"
            "The angle of rotation (counterclockwise) applied to the label.",
        ],
        [
            "boxAnchor",
            "标签的框锚，'n'、'e'、'w'、's'、'ne'、'nw'、'se'、'sw'中的一种。\n"
            "The label's box anchor, one of 'n', 'e', 'w', 's', 'ne', 'nw', 'se', 'sw'.",
        ],
        [
            "textAnchor",
            "标签文字的固定位置，'start'、'middle'、'end'中的一个。\n"
            "The place where to anchor the label's text, one of 'start', 'middle', 'end'.",
        ],
        [
            "boxFillColor",
            '标签框中使用的填充颜色。\n' 'The fill color used in the label\'s box.',
        ],
        [
            "boxStrokeColor",
            "标签框中使用的笔触颜色。\n" "The stroke color used in the label's box.",
        ],
        ["boxStrokeWidth", '标签框的线宽。\nThe line width of the label\'s box.'],
        ["fontName", '标签的字体名称。\nThe label\'s font name.'],
        ["fontSize", '标签的字体大小。\nThe label\'s font size.'],
        [
            "leading",
            '标签文字行的前导值。(leading)\n'
            'The leading value of the label\'s text lines.',
        ],
        ["x", '参考点的X坐标。\nThe X-coordinate of the reference point.'],
        ["y", '参考点的Y坐标。\nThe Y-coordinate of the reference point.'],
        ["width", '标签的宽度。\nThe label\'s width.'],
        ["height", '标签的高度。\nThe label\'s height.'],
    ]
    table = Table(attributes, style=attr_style, colWidths=(100, 330))
    pdf.add_space()
    pdf.add_flowable(table)
    pdf.add_caption("Label 属性", category=constant.CAPTION_TABLE)
    pdf.add_paragraph(
        '要查看更多的具有不同属性组合的 $Label$ 对象的例子，'
        '请查看文件夹 $tests$ 中的ReportLab测试套件，'
        '运行脚本 $test_charts_textlabels.py$ 并查看它所生成的PDF文档。'
    )

    pdf.add_heading("Axes", level=2)
    pdf.add_paragraph(
        '我们确定了两种基本的轴 '
        '--^Value^和^Category^。'
        '这两种轴都有水平和垂直的味道。'
        '两者都可以被子类化来制作非常特殊类型的轴。'
        '例如，如果您有复杂的规则，在时间序列应用程序中显示哪些日期，或者想要不规则的缩放，'
        '您可以覆盖该轴并创建一个新的轴。'
    )
    pdf.add_paragraph('轴负责确定从数据到图像坐标的映射；' '根据图表的要求变换点；' '绘制自己及其刻度线、网格线和轴标签。')
    pdf.add_paragraph('这张图显示了两个轴，每一种都有一个，' '它们是在没有参考任何图表的情况下直接创建的。')

    pdf.add_embedded_code(
        """
from reportlab.graphics.shapes import Drawing, Circle
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.axes import XCategoryAxis, YValueAxis, XValueAxis
from reportlab.lib import colors

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
xAxis.labels.fontName = 'SourceHanSans-ExtraLight'

yAxis = YValueAxis()
yAxis.setPosition(50, 50, 125)
yAxis.configure(data)

drawing.add(xAxis)
drawing.add(yAxis)
    """,
        name='drawing',
    )
    pdf.add_caption('两个孤立的轴', category=constant.CAPTION_IMAGE)
    pdf.add_paragraph(
        '请记住，通常情况下，你不必直接创建轴；'
        '当使用标准图表时，它自带现成的轴。'
        '这些方法是图表用来配置它和处理几何体的。'
        '不过，下面我们将详细介绍它们。'
        '正交双轴到我们描述的那些轴，除了指的是刻度线外，其他的属性基本相同。'
    )

    pdf.add_heading("$XCategoryAxis$", level=3)
    pdf.add_paragraph(
        '类别轴并没有真正的刻度，它只是把自己分成大小相等的 $buckets$。'
        '它比值轴更简单。图表（或程序员）用方法 $setPosition(x, y, length)$ 设置它的位置。'
        '下一个阶段是向它显示数据，以便它能够自行配置。'
        '对于类别轴来说，这很容易'
        '--它只是计算其中一个数据系列中的数据点数量。'
        '$reversed$ 属性（如果是1）表示类别应该反过来。'
        '绘制时，该轴可以通过其$scale()$方法为图表提供一些帮助，'
        '该方法告诉图表一个给定类别在页面上的开始和结束位置。'
        '我们还没有看到任何让人们覆盖类别的宽度或位置的需求。'
    )
    pdf.add_paragraph("一个 $XCategoryAxis$ 类有以下可编辑的属性。")
    pdf.add_space()

    attributes = [
        ["属性", "描述"],
        [
            "visible",
            '轴是否应该被绘制？有时你不想显示一个或两个轴，\n'
            '但它们仍然需要存在，因为它们管理着点的缩放。\n'
            'Should the axis be drawn at all? \n'
            'Sometimes you don\'t want to display one or both axes, \n'
            'but they still need to be there as they manage the scaling of '
            'points.',
        ],
        ["strokeColor", "轴的颜色\nColor of the axis"],
        [
            "strokeDashArray",
            '是否要用破折号画轴，如果要画，画什么样的轴。默认值为"None"。\n'
            'Whether to draw axis with a dash and, if so, what kind.'
            'Defaults to None',
        ],
        ["strokeWidth", "轴的宽度，以点为单位（points）\n" "Width of axis in points"],
        [
            "tickUp",
            '刻度线应突出到轴上方多远？\n'
            '（请注意，使其等于图表高度会给您一条网格线）\n'
            'How far above the axis should the tick marks protrude? \n'
            '(Note that making this equal to chart height gives you a gridline)',
        ],
        [
            "tickDown",
            '刻度线应突出到轴下方多远？\n'
            'How far below the axis should the tick mark protrude?',
        ],
        [
            "categoryNames",
            '$None$ 或字符串列表。 该长度应与每个数据系列的长度相同。\n'
            'Either None, or a list of strings.\n'
            'This should have the same length as each data series.',
        ],
        [
            "labels",
            '刻度线标签的集合。 \n'
            '默认情况下，每个文本标签的“north” (北方)（例如:顶部中心）\n'
            '位于轴上每个类别的中心下方5点处。\n'
            '您可以重新定义整个标签组或任何一个标签的任何属性。 \n'
            '如果 categoryNames=None，则不会绘制标签。\n'
            'A collection of labels for the tick marks.\n'
            'By default the \'north\' of each text label (i.e top centre) \n'
            'is positioned 5 points down from the centre of each category on '
            'the axis. \n'
            'You may redefine any property of the whole label group or of \n'
            'any one label. If categoryNames=None, no labels are drawn.',
        ],
        [
            "title",
            '尚未实现。 这需要像一个标签，但也可以让您直接设置文本。 \n'
            '它在轴下方将具有默认位置。\n'
            'Not Implemented Yet. This needs to be like a label, \n'
            'but also lets you set the text directly. \n'
            'It would have a default location below the axis.',
        ],
    ]
    table = Table(attributes, style=attr_style, colWidths=(100, 330))
    pdf.add_space()
    pdf.add_flowable(table)
    pdf.add_caption("XCategoryAxis 属性", category=constant.CAPTION_TABLE)

    pdf.add_heading("YValueAxis", level=3)
    pdf.add_paragraph(
        '图中的左轴是 $YValueAxis$。 '
        '值轴与类别轴的不同之处在于，沿其长度的每个点都对应于图表空间中的 $y$ 值。 '
        '轴的工作是配置自身，并将 $Y$ 值从图表空间转换为按需点，以辅助父图表进行绘制。'
    )
    pdf.add_paragraph(
        '$setPosition(x, y, length)$和$configure(data)$的作用与类别轴完全相同。 '
        '如果尚未完全指定最大，最小和刻度间隔，则 $configure()$ 会导致轴选择合适的值。'
        '配置完成后，值轴可以使用 $scale()$ 方法将 y 个数据值转换为绘图空间。 从而：'
    )
    pdf.add_code_eg(
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
    pdf.add_paragraph(
        "默认情况下，"
        "最高的数据点与轴的顶部对齐，最低的数据点与轴的底部对齐，"
        "轴为其刻度线点选择 $'nice round numbers'$ (漂亮的整数)。"
        "您可以用下面的属性覆盖这些设置。"
    )
    attribute = [
        ["属性", "描述"],
        [
            "visible",
            '轴是否应该被绘制？有时你不想显示一个或两个轴，\n'
            '但它们仍然需要存在，因为它们管理着点的缩放。\n'
            'Should the axis be drawn at all? \n'
            'Sometimes you don\'t want to display one or both axes, \n'
            'but they still need to be there as manage the scaling of points.',
        ],
        ["strokeColor", "轴的颜色\nColor of the axis"],
        [
            "strokeDashArray",
            '是否要用破折号画轴，如果要画，画什么样的轴。默认值为"None"。\n'
            'Whether to draw axis with a dash and, if so, what kind.\n'
            'Defaults to None',
        ],
        ["strokeWidth", "轴的宽度，以点为单位（points）\nWidth of axis in points"],
        [
            "tickLeft",
            '刻度线应突出到轴的左侧多远？\n'
            '（请注意，使其等于图表宽度会给您一条网格线）\n'
            'How far to the left of the axis should the tick marks protrude?\n'
            '(Note that making this equal to chart height gives you a gridline)',
        ],
        [
            "tickRight",
            '刻度线应突出到轴的右侧多远？\n'
            'How far to the right of the axis should the tick mark protrude?',
        ],
        [
            "valueMin",
            '轴底部应对应的 y 值。 默认值为 None，在这种情况下，\n'
            '轴会将其设置为最低的实际数据点（例如，上例中为10）。 \n'
            '通常将其设置为零以避免误导眼睛。\n'
            'The y value to which the bottom of the axis should correspond.\n'
            'Default value is None in which case the axis sets it to the '
            'lowest\n'
            'actual data point (e.g. 10 in the example above).\n'
            ' It is common to set this to zero to avoid misleading the eye.',
        ],
        [
            "valueMax",
            '轴顶部应对应的 y 值。 默认值为 None，在这种情况下，\n'
            '轴会将其设置为最高实际数据点（例如，上例中为42）。\n'
            '通常将其设置为“整数”，这样数据条就不会到达顶部。\n'
            'The y value to which the top of the axis should correspond.\n'
            'Default value is None in which case the axis sets it to the '
            'highest\n'
            'actual data point (e.g. 42 in the example above).\n'
            'It is common to set this to a \'round number \n'
            'so data bars do not quite reach the top.',
        ],
        [
            "valueStep",
            'y在刻度间隔之间变化。 默认情况下，此值为“None”，\n'
            '图表尝试选择比下面的最小刻度间距更宽的“很好的整数”。\n'
            'The y change between tick intervals. By default this is None, \n'
            'and the chart tries to pick \'nice round numbers\' which are\n'
            'just wider than the minimumTickSpacing below.',
        ],
        [
            "valueSteps",
            '放置刻度的数字列表。\n' 'A list of numbers at which to place ticks.',
        ],
        [
            "minimumTickSpacing",
            '当$valueStep$设置为$None$时使用，否则忽略。 \n'
            '设计人员指定刻度线之间的距离不应小于X点（大概是基于标签字体大小和角度的考虑）。 \n'
            '图表尝试使用1,2,5,10,20,50,100 ...（如有必要，请减小到1以下）类型的值，\n'
            '直到找到大于所需间隔的间隔，并将其用于 $step$。\n'
            'This is used when valueStep is set to None, and ignored '
            'otherwise. \n'
            'The designer specified that tick marks should be \n'
            'no closer than X points apart \n'
            '(based, presumably, on considerations of the label font size and angle). \n'
            'The chart tries values of the type 1,2,5,10,20,50,100... \n'
            '(going down below 1 if necessary) until it finds an interval \n'
            'which is greater than the desired spacing, and uses this for the step.',
        ],
        [
            "labelTextFormat",
            '这确定了标签中的内容。 与接受固定字符串的类别轴不同，\n'
            '$ValueAxis$ 上的标签应为数字。 \n'
            '您可以提供“$％0.2f$”之类的“格式字符串”（显示两位小数），\n'
            '也可以提供一个接受数字并返回字符串的任意函数。 \n'
            '后者的一种用法是将时间戳转换为可读的年月日格式。\n'
            'This determines what goes in the labels. \n'
            'Unlike a category axis which accepts fixed strings, \n'
            'the labels on a ValueAxis are supposed to be numbers. \n'
            'You may provide either a \'format string\' like \'%0.2f\'\n'
            '(show two decimal places), or an arbitrary function \n'
            'which accepts a number and returns a string.\n'
            'One use for the latter is to convert a timestamp \n'
            'to a readable year-month-day format.',
        ],
        [
            "title",
            '尚未实现。 这需要像一个标签，但也可以让您直接设置文本。\n'
            '它在轴下方将具有默认位置。\n'
            'Not Implemented Yet. This needs to be like a label,\n'
            'but also lets you set the text directly. \n'
            'It would have a default location below the axis.',
        ],
    ]
    table = Table(attribute, style=attr_style, colWidths=(100, 330))
    pdf.add_space()
    pdf.add_flowable(table)
    pdf.add_caption("YValueAxis 属性", category=constant.CAPTION_TABLE)
    pdf.add_paragraph(
        '$valueSteps$属性让您明确指定刻度线的位置，因此您不必遵循常规的时间间隔。'
        '因此，你可以通过几个辅助函数来绘制月末和月末日期，而且不需要特殊的时间序列图表类。'
        '下面的代码显示了如何创建一个简单的 $XValueAxis$ 与特殊的刻度间隔。'
        '请确保在调用配置方法之前设置 $valueSteps$ 属性!'
    )
    pdf.add_embedded_code(
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
""",
        name='drawing',
    )
    pdf.add_caption("带非等距刻度线的轴", category=constant.CAPTION_IMAGE)
    pdf.add_paragraph(
        '除了这些属性之外，所有的轴类都有三个属性，描述如何将其中的两个轴相互连接。'
        '再次强调，只有当你定义你自己的图表或者想使用这些坐标轴修改现有图表的外观时，这才是有趣的。'
        '这些属性在这里只是非常简单的列出，'
        '但你可以在$reportlab/graphics/axes.py$模块中找到大量的示例函数，'
        '你可以检查......'
    )
    pdf.add_paragraph(
        "通过在第一个轴上调用方法$joinToAxis(otherAxis, mode, pos)$"
        "将一个轴连接到另一个轴，"
        "$mode$和$pos$分别是$joinAxisMode$和$joinAxisPos$描述的属性。"
        "$'points'$表示使用绝对值，$'value'$表示使用沿轴的相对值"
        "（均由$joinAxisPos$属性表示）。"
    )
    pdf.add_space()
    attributes = [
        ["属性", "描述"],
        ["joinAxis", "如果为真，则连接两个轴。\nJoin both axes if true."],
        [
            "joinAxisMode",
            "用于连接轴的模式 \n"
            "('bottom', 'top', 'left', 'right', 'value', 'points', None).\n"
            "Mode used for connecting axis \n"
            "('bottom', 'top', 'left', 'right', 'value', 'points', None).",
        ],
        [
            "joinAxisPos",
            '与其他轴连接的位置。\nPosition at which to join with other axis.',
        ],
    ]
    table = Table(attributes, style=attr_style, colWidths=(100, 330))
    pdf.add_flowable(table)
    pdf.add_caption("Axes joining 属性", category=constant.CAPTION_TABLE)

    pdf.add_heading("柱状图", level=2)
    pdf.add_paragraph(
        "这描述了我们目前的$VerticalBarChart$类，它使用了上面的轴和标签。"
        "我们认为这是正确方向的一步，但还远未到最后的阶段。"
        "请注意，与我们交谈过的人对这是'垂直'还是'水平'条形图的看法不一。"
        "我们选择这个名字是因为'垂直'出现在'条形图'旁边，"
        "所以我们认为它的意思是条形图而不是类别轴是垂直的。"
    )
    pdf.add_paragraph('与往常一样，我们将从一个示例开始：')
    pdf.add_embedded_code(
        """
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib import colors

drawing = Drawing(400, 200)

data = [(13, 5, 20, 22, 37, 45, 19, 4), 
        (14, 6, 21, 23, 38, 46, 20, 5)]

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
    """,
        name='drawing',
    )
    pdf.add_caption("具有两个数据系列的简单柱状图", category=constant.CAPTION_IMAGE)
    pdf.add_paragraph(
        '这段代码的大部分内容是关于设置坐标轴和标签的，我们已经介绍过了，' '下面是$VerticalBarChart$类的顶层属性。'
    )
    pdf.add_space()

    attributes = [
        ["属性", "描述"],
        [
            "data",
            '这应该是“数字列表列表”或“数字元组列表”。 \n'
            '如果只有一个系列，则将其写为 data=[(10,20,30,42),]\n'
            'This should be a "list of lists of numbers" or "list of tuples '
            'of numbers".\n'
            'If you have just one series, write it as data = [(10,20,30,42),]',
        ],
        [
            "x, y, width, height",
            '这些定义了内部的 "绘图矩形"。\n'
            '我们在上面用黄色边框突出显示了这个矩形。\n'
            '请注意，您的工作是将图表放置在图纸上，为所有的轴标签和刻度线留出空间。\n'
            '我们指定这个 "内矩形" 是因为它可以很容易地以一致的方式布置多个图表。\n'
            'These define the inner \'plot rectangle\'. \n'
            'We highlighted this with a yellow border above. \n'
            'Note that it is your job to place the chart on the drawing \n'
            'in a way which leaves room for all the axis labels and \n'
            'tickmarks. We specify this \'inner rectangle\' \n'
            'because it makes it very easy to lay out multiple charts \n'
            'in a consistent manner.',
        ],
        [
            "strokeColor",
            '默认为 None。 这将在绘图矩形周围绘制边框，\n'
            '这可能对调试很有用。 轴将覆盖此位置。\n'
            'Defaults to None. This will draw a border around the plot '
            'rectangle,\n'
            'which may be useful in debugging. Axes will overwrite this.',
        ],
        [
            "fillColor",
            '默认为 None。 这将用纯色填充绘图矩形。 \n'
            '（请注意，我们可以像其他任何实心形状一样实现 $dashArray$ 等）\n'
            'Defaults to None. This will fill the plot rectangle with \n'
            'a solid color. (Note that we could implement dashArray etc.\n'
            'as for any other solid shape)',
        ],
        [
            "useAbsolute",
            '默认为0. 如果为1，则下面的三个属性是绝对值，以点为单位 \n'
            '（这意味着你可以制作一个图表，其中的条形图从绘图矩形中伸出来）；\n'
            '如果为0，则是相对量，表示相关元素的比例宽度。\n'
            'Defaults to 0. If 1, the three properties below are \n'
            'absolute values in points (which means you can make a chart \n'
            'where the bars stick out from the plot rectangle); if 0, \n'
            'they are relative quantities and indicate the proportional \n'
            'widths of the elements involved.',
        ],
        ["barWidth", "柱状宽度. 默认为 10. \nAs it says. Defaults to 10."],
        [
            "groupSpacing",
            '默认值为5。这是每组条形图之间的间距，\n'
            '如果只有一个系列，请使用$groupSpacing$而不是barSpacing来分割它们。\n'
            '$groupSpacing$的一半用于图表的第一个条形图之前，另一半用于结尾。\n'
            'Defaults to 5. This is the space between each group of ars.\n'
            'If you have only one series, use groupSpacing and not barSpacing\n'
            'to split them up. Half of the groupSpacing is used before \n'
            'the first bar in the chart, and another half at the end.',
        ],
        [
            "barSpacing",
            '默认值为0。这是每个组中的条之间的间距。 \n'
            '如果在上面的示例中绿色和红色条形之间要有一点间隙，则可以将其设置为非零。\n'
            'Defaults to 0. This is the spacing between bars in each \n'
            'group. If you wanted a little gap between green and red bars in\n'
            'the example above, you would make this non-zero.',
        ],
        [
            "barLabelFormat",
            '默认为 None。 与$YValueAxis$一样，\n'
            '如果提供函数或格式字符串，则会在每个显示数值的条旁边绘制标签。 \n'
            '对于正值，它们会自动定位在条的上方，\n'
            '对于负值，它们会自动位于下方。\n'
            'Defaults to None. As with the YValueAxis, if you supply\n'
            'a function or format string then labels will be drawn next to '
            'each bar\n'
            'showing the numeric value. They are positioned automatically\n'
            'above the bar for positive values and below for negative ones.',
        ],
        [
            "barLabels",
            '用于格式化所有条形标签的标签集合。\n'
            '由于这是一个二维数组，您可以使用此语法明确格式化第二个系列的第三个标签：\n'
            'chart.barLabels[(1,2)].fontSize = 12。\n'
            'A collection of labels used to format all bar labels.\n'
            ' Since this is a two-dimensional array, \n'
            'you may explicitly format the third label of \n'
            'the second series using this syntax:\n'
            'chart.barLabels[(1,2)].fontSize = 12',
        ],
        [
            "valueAxis",
            '值轴，其格式可如前所述。\n'
            'The value axis, which may be formatted as described previously.',
        ],
        [
            "categoryAxis",
            '类别轴，其格式可如前所述。\n'
            'The category axis, which may be formatted as described '
            'previously.',
        ],
        [
            "title",
            '还没有实现。这需要像一个标签一样，\n'
            '但也可以让你直接设置文本。它将有一个默认的位置在轴的下方。\n'
            'Not Implemented Yet. This needs to be like a label, \n'
            'but also lets you set the text directly. \n'
            'It would have a default location below the axis.',
        ],
    ]
    table = Table(attributes, style=attr_style, colWidths=(100, 330))
    pdf.add_flowable(table)
    pdf.add_caption("VerticalBarChart 属性", category=constant.CAPTION_TABLE)
    pdf.add_paragraph(
        '从该表中我们可以得出结论，在上面的代码中加入以下几行，'
        '应该会使条形图组之间的间距增加一倍($groupSpacing$属性的默认值为5点)，'
        '我们还应该看到同一组的条形组之间有一些微小的空间($barSpacing$)。'
    )
    pdf.add_code_eg(
        """
        bc.groupSpacing = 10
        bc.barSpacing = 2.5
    """
    )
    pdf.add_paragraph(
        '而且，实际上，这就是在将这些行添加到上面的代码之后所能看到的。 '
        '注意各个条的宽度也如何变化。 '
        '这是因为随着总图表宽度保持不变，必须从某处“占用”条形之间的空格。'
    )

    pdf.add_embedded_code(
        """
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib import colors

drawing = Drawing(400, 200)

data = [(13, 5, 20, 22, 37, 45, 19, 4), 
        (14, 6, 21, 23, 38, 46, 20, 5)]

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
""",
        name='drawing',
    )
    pdf.add_caption('像以前一样，但间距已更改', category=constant.CAPTION_IMAGE)
    pdf.add_paragraph('条形图标签将自动显示为条形下限以下的负值，其他条形上限值以上的正值。')
    pdf.add_paragraph(
        "垂直条形图也支持堆叠条形图。"
        "您可以通过在 $categoryAxis$ 上设置 $style$ 属性"
        "为 $'stacked'$ 来为您的图表启用这种布局。"
    )
    pdf.add_code_eg("bc.categoryAxis.style = 'stacked'")
    pdf.add_paragraph('下面是以之前的图表值为例，以叠加的方式排列。')

    pdf.add_embedded_code(
        """
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib import colors

drawing = Drawing(400, 200)

data = [(13, 5, 20, 22, 37, 45, 19, 4), 
        (14, 6, 21, 23, 38, 46, 20, 5)]

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
""",
        name='drawing',
    )
    pdf.add_caption("柱状叠加图", category=constant.CAPTION_IMAGE)
    pdf.add_heading("折线图", level=2)
    pdf.add_paragraph(
        '我们认为 "折线图"($Line Charts$)  与 "柱状图"($Bar Charts$) 本质上是一样的，只是用线代替了条。'
        '两者共享同一对类别/数值轴对。这与 "线图"不同，'
        '在"线图"($Line Plots$) 中，两个轴都是<i>值</i>轴。'
    )
    pdf.add_paragraph(
        '以下代码及其输出将作为一个简单的例子。'
        '后面会有更多的解释。'
        '目前，您也可以研究运行 $reportlab/lib/graphdocpy.py$ 工具的输出，'
        '并在生成的PDF文档中搜索柱状图($Line Charts$)的例子。'
    )

    pdf.add_embedded_code(
        """
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.lib import colors

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
    """,
        name="drawing",
    )
    pdf.add_caption(
        'HorizontalLineChart - 折线图', category=constant.CAPTION_IMAGE
    )
    pdf.add_space()

    attribute = [
        ["属性", "描述"],
        [
            "data",
            "要绘制的数据，（列表）整数清单。\n"
            "Data to be plotted, list of (lists of) numbers.",
        ],
        [
            "x, y, width, height",
            '折线图的边界框。 请注意，x和y不指定中心，而是左下角\n'
            'Bounding box of the line chart.\n'
            'Note that x and y do NOT specify the centre but the bottom left corner',
        ],
        [
            "valueAxis",
            '值轴，其格式可如前所述。\n'
            'The value axis, which may be formatted as described previously.',
        ],
        [
            "categoryAxis",
            '类别轴，其格式可如前所述。\n'
            'The category axis, which may be formatted as described previously.',
        ],
        [
            "strokeColor",
            '默认值为 "None"。这将在绘图矩形周围画一个边框，\n'
            '这在调试时可能很有用。轴将覆盖它。\n'
            'Defaults to None. This will draw a border around the plot '
            'rectangle,\n'
            'which may be useful in debugging. Axes will overwrite this.',
        ],
        [
            "fillColor",
            "默认为 None。 这将用纯色填充绘图矩形。\n"
            "Defaults to None. This will fill the plot rectangle with a solid color.",
        ],
        ["lines.strokeColor", '线的颜色\nColor of the line.'],
        ["lines.strokeWidth", '线的宽度\nWidth of the line.'],
        [
            "lineLabels",
            '用于格式化所有行标签的标签集合。由于这是一个二维数组，\n'
            '您可以使用以下语法明确格式化第二行的第三个标签：\n'
            'chart.lineLabels[(1,2)].fontSize = 12。\n'
            'A collection of labels used to format all line labels.\n'
            'Since this is a two-dimensional array, you may explicitly format the third \n'
            'label of the second line using this syntax:\n'
            'chart.lineLabels[(1,2)].fontSize = 12',
        ],
        [
            "lineLabelFormat",
            '默认值为 "None"。与YValueAxis一样，如果你提供一个函数或格式字符串，\n'
            '那么标签将被绘制在每一行的旁边，显示数值。\n'
            '您也可以将其设置为\'values\'，以显示在lineLabelArray中明确定义的值。\n'
            'Defaults to None. As with the YValueAxis, if you supply \n'
            'a function or format string then labels will be drawn next\n'
            'to each line showing the numeric value. You can also set it\n'
            'to \'values\' to display the values explicity defined in lineLabelArray.',
        ],
        [
            "lineLabelArray",
            "行标签值的显式数组，如果存在，必须与数据的大小相匹配。\n"
            "只有当上面的属性$lineLabelFormat$被设置为'values'时，\n"
            "这些标签值才会被显示。\n"
            "Explicit array of line label values, must match size of data if "
            "present.\n"
            "These labels values will be displayed only if the property\n"
            "lineLabelFormat above is set to 'values'.",
        ],
    ]
    table = Table(attribute, style=attr_style, colWidths=(100, 330))
    pdf.add_flowable(table)
    pdf.add_caption("HorizontalLineChart 属性", category=constant.CAPTION_TABLE)

    pdf.add_heading("点线图", level=2)
    pdf.add_paragraph('下面我们展示了一个更复杂的线型图的例子，' '也使用了一些实验功能，比如在每个数据点放置线型标记。')

    pdf.add_embedded_code(
        """
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.lib import colors

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
    """,
        name="drawing",
    )
    pdf.add_caption("LinePlot 示例图", category=constant.CAPTION_IMAGE)
    pdf.add_space()

    attribute = [
        ["属性", "描述"],
        [
            "data",
            "要绘制的数据，（列表）整数清单。\n"
            "Data to be plotted, list of (lists of) numbers.",
        ],
        [
            "x, y, width, height",
            '折线图的边界框。 请注意，x和y不指定中心，而是左下角\n'
            'Bounding box of the line chart.\n'
            'Note that x and y do NOT specify the centre but the bottom left corner',
        ],
        [
            "xValueAxis",
            '垂直值轴，其格式可以如上所述。\n'
            'The vertical value axis, which may be formatted as described previously.',
        ],
        [
            "yValueAxis",
            '水平值轴，其格式可以如上所述。\n'
            'The horizontal value axis, which may be formatted as described previously.',
        ],
        [
            "strokeColor",
            '默认为None。 这将在绘图矩形周围绘制边框，\n'
            '这可能对调试很有用。 轴将覆盖此位置。\n'
            'Defaults to None. This will draw a border around the plot '
            'rectangle,\n'
            'which may be useful in debugging. Axes will overwrite this.',
        ],
        [
            "strokeWidth",
            '默认为None。 绘图矩形周围边框的宽度。\n'
            'Defaults to None. Width of the border around the plot rectangle.',
        ],
        [
            "fillColor",
            '默认为None。 这将用纯色填充绘图矩形。\n'
            'Defaults to None. This will fill the plot rectangle with a solid color.',
        ],
        ["lines.strokeColor", '线的颜色。\n' 'Color of the line.'],
        ["lines.strokeWidth", '线的宽度\n' 'Width of the line.'],
        [
            "lines.symbol",
            '每个点使用的标记。您可以使用函数$makeMarker()$创建一个新的标记。\n'
            '例如，要使用一个圆，函数调用是makeMarker(\'Circle\')\n'
            'Marker used for each point.\n'
            'You can create a new marker using the function makeMarker().\n'
            'For example to use a circle, the function call would be '
            'makeMarker(\'Circle\')',
        ],
        [
            "lineLabels",
            '用于格式化所有行标签的标签集合。\n'
            '由于这是一个二维数组，您可以使用以下语法明确格式化第二行的第三个标签：\n'
            'chart.lineLabels[(1,2)].fontSize = 12。\n'
            'A collection of labels used to format all line labels. \n'
            'Since this is a two-dimensional array, you may explicitly format the \n'
            'third label of the second line using this syntax: \n'
            'chart.lineLabels[(1,2)].fontSize = 12',
        ],
        [
            "lineLabelFormat",
            '默认值为 None。与$YValueAxis$一样，如果你提供一个函数或格式字符串，'
            '那么标签将被绘制在每一行的旁边，显示数值。您也可以将其设置为\'values\'，'
            '以显示在$lineLabelArray$中明确定义的值。\n'
            'Defaults to None. As with the YValueAxis, if you supply\n'
            'a function or format string then labels will be drawn next\n'
            'to each line showing the numeric value. You can also set it\n'
            'to \'values\' to display the values explicity defined in lineLabelArray.',
        ],
        [
            "lineLabelArray",
            '行标签值的显式数组，如果存在，必须与数据的大小相匹配。'
            '只有当上面的属性lineLabelFormat被设置为\'values\'时，'
            '这些标签值才会被显示。\n'
            'Explicit array of line label values, must match size of data if '
            'present.\n'
            'These labels values will be displayed only if the property\n'
            'lineLabelFormat above is set to \'values\'.',
        ],
    ]
    table = Table(attribute, style=attr_style, colWidths=(100, 330))
    pdf.add_flowable(table)
    pdf.add_caption("LinePlot 属性")

    pdf.add_heading("饼图", level=2)
    pdf.add_paragraph('像往常一样，我们将从一个例子开始:')
    pdf.add_embedded_code(
        """
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib import colors

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
        """,
        name='d',
    )
    pdf.add_caption("凸出的饼图", category=constant.CAPTION_IMAGE)
    pdf.add_paragraph('属性在下面介绍。 $pie$ 具有 “$slices$” 集合，我们在同一表中记录 $wedge$ 属性。')
    pdf.add_space()

    attribute = [
        ["属性", "描述"],
        ["data", "整数合集"],
        [
            "x, y, width, height",
            '饼图的边界框。 请注意，x和y不必指定中心，\n'
            '而是指定左下角，并且宽度和高度不必相等。 \n'
            '饼图可能是椭圆形的，并且会正确绘制切片。\n'
            'A list or tuple of numbers\n'
            'Note that x and y do NOT specify the centre but the bottom left\n'
            'corner, and that width and height do not have to be equal;\n'
            'pies may be elliptical and slices will be drawn correctly.',
        ],
        [
            "labels",
            'None, 或者字符串合集. 如果您不希望饼图边缘周围有标签，\n'
            '请将其设为“None”。 \n'
            '由于不可能知道切片的大小，因此我们通常不建议在饼中或饼周围放置标签。 \n'
            '最好将它们放在图例中。\n'
            'None, or a list of strings.\n'
            'Make it None if you don\'t want labels around the edge of the '
            'pie.\n'
            'Since it is impossible to know the size of slices, we generally\n'
            'discourage placing labels in or around pies; it is much better \n'
            'to put them in a legend alongside.',
        ],
        [
            "startAngle",
            '第一个饼片的起始角度是什么？默认为"90"，即 12 点钟方向。\n'
            'Where is the start angle of the first pie slice?\n'
            'The default is \'90\' which is twelve o\'clock.',
        ],
        [
            "direction",
            '切片的前进方向是什么？默认为 "clockwise"。(顺时针)\n'
            'Which direction do slices progress in?\n'
            'The default is \'clockwise\'.',
        ],
        [
            "sideLabels",
            '这将创建一个标签在两边各一列的图表。\n'
            'This creates a chart with the labels in two columns, one on either side.',
        ],
        [
            "sideLabelsOffset",
            '这是饼图宽度的一部分，该宽度定义了饼图和标签列之间的水平距离。\n'
            'This is a fraction of the width of the pie that defines the '
            'horizontal\n'
            'distance between the pie and the columns of labels.',
        ],
        [
            "simpleLabels",
            '默认为 1. 设置为0以启用自定义标签以及在集合切片中使用 label_ 前缀的属性。\n'
            'Default is 1. Set to 0 to enable the use of customizable labels '
            '\nand of properties prefixed by label_ in the collection slices.',
        ],
        [
            "slices",
            "切片的集合。这使您可以自定义每个扇形或单个扇形。 见下文\n"
            "Collection of slices. This lets you customise each wedge, or individual ones. See below",
        ],
        ["slices.strokeWidth", "扇形边框宽度\nBorder width for wedge"],
        ["slices.strokeColor", "扇形边框颜色\nBorder color"],
        [
            "slices.strokeDashArray",
            "实线或虚线配置：['solid', 'dashed']\nSolid or dashed line configuration",
        ],
        [
            "slices.popout",
            '切片应从馅饼的中心伸出多远？ 默认值为零。\n'
            'How far out should the slice(s) stick from the centre of the '
            'pie? \nDefault is zero.',
        ],
        ["slices.fontName", "标签字体名称\nName of the label font"],
        ["slices.fontSize", "标签字体大小\nSize of the label font"],
        ["slices.fontColor", "标签文字的颜色\nColor of the label text"],
        [
            "slices.labelRadius",
            '这控制文本标签的锚点。 它是半径的一小部分；\n'
            '0.7将文本放置在饼中，1.2将文本放置在饼外。 \n'
            '（请注意，如果我们添加标签，将保留此标签以指定其锚点）\n'
            'This controls the anchor point for a text label.\n'
            'It is a fraction of the radius; 0.7 will place the text inside '
            'the pie, \n'
            '1.2 will place it slightly outside. (note that if we add labels,'
            '\n'
            'we will keep this to specify their anchor point)',
        ],
    ]
    table = Table(attribute, style=attr_style, colWidths=(130, 300))
    pdf.add_flowable(table)
    pdf.add_heading("自定义 Label", level=3)

    pdf.add_paragraph(
        '通过改变集合$slices$中以$label_$为前缀的属性，'
        '可以单独定制每个幻灯片标签。'
        '例如 $pc.slices[2].label_angle = 10$ 改变第三个标签的角度。'
    )
    pdf.add_paragraph('在使用这些自定义属性之前，您需要使用以下命令禁用简单标签：$pc.simplesLabels=0$')
    pdf.add_space()

    attribute = [
        ["属性", "描述"],
        ["label_dx", 'X轴标签偏移\nX Offset of the label'],
        ["label_dy", 'Y轴标签偏移\nY Offset of the label'],
        [
            "label_angle",
            '标签的角度，默认（0）为水平，90为垂直，180为上下颠倒\n'
            'Angle of the label, default (0) is horizontal, 90 is vertical,180 is upside down',
        ],
        ["label_boxAnchor", '标签的固定点\nAnchoring point of the label'],
        ["label_boxStrokeColor", '标签框的边框颜色\nBorder color for the label box'],
        ["label_boxStrokeWidth", '标签框的边框宽度\nBorder width for the label box'],
        ["label_boxFillColor", '标签盒的填充颜色\nFilling color of the label box'],
        ["label_strokeColor", '标签文字的边框颜色\nBorder color for the label text'],
        ["label_strokeWidth", '标签文字的边框宽度\nBorder width for the label text'],
        ["label_text", '标签文字\nText of the label'],
        ["label_width", '标签宽度\nWidth of the label'],
        ["label_maxWidth", '标签可以增加到的最大宽度\nMaximum width the label can grow to'],
        ["label_height", '标签高度\nHeight of the label'],
        [
            "label_textAnchor",
            '标签可以增加到的最大高度\nMaximum height the label can grow to',
        ],
        ["label_visible", '如果要绘制标签，则为True\nTrue if the label is to be drawn'],
        ["label_topPadding", '盒子的上边距(Padding at top of box)'],
        ["label_leftPadding", '盒子的左边距(Padding at left of box)'],
        ["label_rightPadding", '盒子的右边距(Padding at right of box)'],
        ["label_bottomPadding", '盒子的下边距(Padding at bottom of box)'],
        ["label_simple_pointer", '为简单指针设置为1(Set to 1 for simple pointers)'],
        ["label_pointer_strokeColor", '指示线颜色\nColor of indicator line'],
        ["label_pointer_strokeWidth", '指示线宽度\nWidth of indicator line'],
    ]
    table = Table(attribute, style=attr_style, colWidths=(130, 300))
    pdf.add_flowable(table)
    pdf.add_caption("Pie.slices 自定义 label", category=constant.CAPTION_TABLE)

    pdf.add_heading("Side Labels 侧面标签", level=3)

    pdf.add_paragraph(
        '如果 $sideLabels$ 属性被设置为 $true$，那么切片分为两列，两边各一列。 '
        '饼和饼的起始角度将被自动设置。'
        '右侧栏的锚点设置为 "start"，并设置了左手列的锚点设置为 "end"。'
        '饼的边缘与左手列中任何一个的边缘的距离。'
        '列由 $sideLabelsOffset$ 属性决定，该属性为饼的宽度的一小部分。'
        '如果改变 $xradius$，饼会与标签重叠，这样一来...。'
        '我们建议将 $xradius$ 改为 $None$。下面是一个例子。'
    )
    pdf.add_draw(sample5(), '一个 $sideLabels=1$ 的饼图示例')
    pdf.add_paragraph(
        '如果将 $sideLabels$ 设置为 $True$，则某些属性将变得多余，例如 $pointerLabelMode$。 '
        '同样，$sideLabelsOffset$ 仅在将 $sideLabels$ 设置为 $true$ 时更改饼图。'
    )

    pdf.add_heading("一些问题", level=4)
    pdf.add_paragraph('如果切片过多，指针可能会交叉。')
    pdf.add_draw(sample7(), '指针交叉的例子')
    pdf.add_paragraph('另外，如果标签对应的片子不相邻，尽管有 $checkLabelOverlap$，标签也可以重叠。')

    pdf.add_draw(sample8(), '标签重叠的示例')

    pdf.add_heading("Legends", level=2)
    pdf.add_paragraph(
        '可以找到各种初步的图例类，但需要进行清理以与图表模型的其他部分保持一致。'
        '图例是指定图表颜色和线条风格的自然场所；'
        '我们建议每个图表都创建一个不可见的$legend$属性。'
        '然后，将执行以下操作以指定颜色：'
    )

    pdf.add_code_eg("myChart.legend.defaultColors = [red, green, blue]")
    pdf.add_paragraph("还可以定义一组共享相同图例的图表：")
    pdf.add_code_eg(
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
    pdf.add_space()

    pdf.add_todo('这样行吗？ 直接指定图表颜色是否可以接受？')

    pdf.add_heading("存在的问题", level=3)
    pdf.add_paragraph('有几个问题已经解决了，但现在开始真正公开这些问题还为时过早。' '不过，这里有一个正在进行的事情清单。')
    pdf.add_bullet(
        '颜色规范: -- 现在图表有一个没文档化的属性 $defaultColors$, '
        '该属性提供要循环显示的颜色列表，以便每个数据系列都有自己的颜色。'
        '现在，如果你要引入图例，则需要确保它具有相同的颜色列表。'
        '最有可能的是，它将被一种方案取代，该方案指定一种图例，该图例包含每个数据系列具有不同值的属性。 '
        '然后，该图例也可以由多个图表共享，但本身不必可见。'
    )
    pdf.add_bullet(
        '额外的图表类型--当目前的设计变得更加稳定时，' '我们希望增加条形图的变体，以处理百分位条形图以及这里看到的并排变体。'
    )

    pdf.add_heading("展望 ($Outlook$)", level=3)
    pdf.add_paragraph('处理全部图表类型需要一些时间。我们预计将首先完成柱状图和饼图，然后试行更多的普通图。')

    pdf.add_heading("X-Y Plots", level=3)
    pdf.add_paragraph(
        '大多数其他图都涉及两个值轴，并以某种形式直接绘制x-y数据。 '
        '该系列可以绘制为线条，标记符号，两者兼而有之,'
        '或自定义图形（例如，开-高-低-闭图形）'
        '所有这些都具有缩放和轴/标题格式的概念。 '
        '在某一点上，一个例程将在数据序列上循环，并在给定的x-y位置上对数据点 "做一些事情"。'
        '给定一个基本的折线图，只需覆盖一个方法--比如说，$drawSeries()$，'
        '就可以很容易地推导出一个自定义的图表类型。'
    )

    pdf.add_heading("自定义标记和自定义形状", level=3)
    pdf.add_paragraph(
        '众所周知的绘图软件包，如 $excel$、$Mathematica$和$Excel$，'
        '都提供了一系列的标记类型来添加到图表中。'
        '我们可以做得更好'
        '--你可以编写任何一种你想要的图表部件，只需告诉图表使用它作为例子。'
    )

    pdf.add_heading("组合图", level=4)
    pdf.add_paragraph(
        '结合多种绘图类型真的很容易。'
        '你只需在同一个矩形中绘制几个图表（条形图、线形图或其他什么图），'
        '根据需要取消显示轴。'
        '因此，一个图表可以将一条线与左轴上15年内的苏格兰伤寒病例相关联，'
        '右轴上有一组显示通货膨胀率的条形图。'
        '如果有谁能提醒我们这个例子的出处，'
        '我们会注明出处，并很高兴地展示这个著名的图表作为例子。'
    )

    pdf.add_heading("互动式编辑", level=3)
    pdf.add_paragraph(
        '图形包的一个原则是使图形组件的所有 "有趣的" '
        '属性都可以通过设置相应的公共属性的适当值来访问和改变。'
        '这使得我们很想建立一个像GUI编辑器一样的工具，'
        '来帮助你交互式地完成这些工作。'
    )
    pdf.add_paragraph(
        'ReportLab使用Tkinter工具箱构建了这样的工具，'
        '该工具箱可加载描述图纸的纯Python代码并记录您的属性编辑操作。 '
        '然后，此“更改历史记录”用于为该图表的子类创建代码，'
        '例如，可以像其他任何图表一样立即保存和使用该代码，'
        '或将其用作另一个交互式编辑会话的新起点。'
    )
    pdf.add_paragraph('不过这还在进行中，发布的条件还需要进一步细化。')

    pdf.add_heading("其他", level=3)
    pdf.add_paragraph(
        '这并不是对所有图表类的详尽介绍。这些类还在不断地改进中。'
        '要查看当前发行版中的确切内容，请使用 $graphdocpy.py$工具。'
        '默认情况下，它将在 $reportlab/graphics$ 上运行，并生成一份完整的报告。'
        '(如果你想在其他模块或软件包上运行它，'
        '$graphdocpy.py -h$ 会打印出一条帮助信息，告诉你如何运行。)'
    )
    pdf.add_paragraph('这是“文档小部件” ($Documenting Widgets$) 部分中提到的工具')

    pdf.add_heading("Shapes 多边形", level=2)

    pdf.add_paragraph(
        '本节介绍形状的概念及其作为图形库生成的所有输出的构建块的重要性。 '
        '介绍了现有形状的一些属性及其与图表的关系，'
        '并简要介绍了针对不同输出格式使用不同渲染器的概念。'
    )

    pdf.add_heading("可用形状", level=3)
    pdf.add_paragraph(
        '绘画是由形状组成的。任何东西都可以通过组合相同的原始图形集来构建。'
        '模块$shapes.py$提供了一些可以添加到图形中的基本形状和构造。它们是'
    )

    pdf.add_bullet('Rect - 矩形')
    pdf.add_bullet('Circle - 圆')
    pdf.add_bullet('Ellipse - 椭圆')
    pdf.add_bullet('Wedge (a pie slice) - 扇形')
    pdf.add_bullet('Polygon - 多边形')
    pdf.add_bullet('Line - 线')
    pdf.add_bullet('PolyLine - 折线')
    pdf.add_bullet('String - 字符串')
    pdf.add_bullet('Group - 组')
    pdf.add_bullet('$Path$ (<i>还没有完全实现，但将来会加入</i>) - 路径')

    pdf.add_paragraph(
        '下面的图画来自于我们的测试套件，显示了大部分的基本形状（除了组）。那些有绿色填充面的图形也被称为<i>实体图形</i>。'
        '(这些是$Rect$、$Circle$、$Ellipse$、$Wedge$和$Polygon$)。'
    )

    pdf.add_draw(testshapes.getDrawing06(), '基本的图形')

    pdf.add_heading("形状属性", level=3)
    pdf.add_paragraph(
        '形状有两种属性 --有的用来定义其几何形状，' '有的用来定义其样式。让我们创建一个红色的矩形，有3点粗的绿色边框。'
    )

    pdf.add_embedded_code(
        """
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.shapes import Rect
from reportlab.lib.colors import red, green

d = Drawing(220,120)
r = Rect(5, 5, 200, 100)
r.fillColor = red
r.strokeColor = green
r.strokeWidth = 3
d.add(r)
    """,
        name='d',
    )
    pdf.add_caption('红色矩形和绿色边框', category=constant.CAPTION_IMAGE)

    pdf.add_pencil_note()
    pdf.add_text_note("在未来的例子中，我们将省略导入语句。")
    pdf.add_paragraph(
        '所有的形状都有一些可以设置的属性。'
        '在交互式提示下，我们可以使用它们的^dumpProperties()^方法来列出这些属性。'
        '下面是你可以用来配置一个^Rect.Rex^的方法。'
    )

    pdf.add_code_eg(
        """
    >>> r.dumpProperties()
    fillColor = Color(1.00,0.00,0.00)
    height = 100
    rx = 0
    ry = 0
    strokeColor = Color(0.00,0.50,0.00)
    strokeDashArray = None
    strokeLineCap = 0
    strokeLineJoin = 0
    strokeMiterLimit = 0
    strokeWidth = 3
    width = 200
    x = 5
    y = 5
    >>>
    """
    )
    pdf.add_paragraph(
        '形状一般有<i>style属性</i>和<i>geometry属性</i>。'
        '$x$, $y$, $width$ 和 $height$ 是几何属性的一部分，'
        '在创建矩形时必须提供，因为没有这些属性就没有什么意义。'
        '其他的属性是可选的，并且有合理的默认值。'
    )
    pdf.add_paragraph(
        '你可以在随后的行中设置其他属性，或者将它们作为可选参数传递给构造函数。' '我们也可以用这种方式来创建我们的矩形。'
    )
    pdf.add_code_eg(
        """
    >>> r = Rect(5, 5, 200, 100,
                 fillColor=red,
                 strokeColor=green,
                 strokeWidth=3)
    """
    )
    pdf.add_paragraph(
        '我们来看看样式属性。'
        '$fillColor$是显而易见的。'
        '$stroke$ 是形状边缘的发布术语；$stroke$有一个颜色、宽度，'
        '可能还有一个破折号图案，以及一些（很少使用的）功能，'
        '用于当一条线转角时发生的情况。'
        '$rx$ 和 $ry$ 是可选的几何属性，用于定义圆角矩形的角半径。'
    )
    pdf.add_paragraph('其他所有的实体形状都具有相同的样式属性。')

    pdf.add_heading("Lines - 线", level=3)

    pdf.add_paragraph(
        '我们提供单条直线、多条直线和曲线。'
        '线条具有所有的$stroke*$属性，但没有$fillColor$。'
        '下面是一些直线和多线的例子以及相应的图形输出。'
    )

    pdf.add_embedded_code(
        """
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.graphics.shapes import (
    Drawing, Line, PolyLine
)

d = Drawing(400, 200)
d.add(Line(50,50, 300,100,
     strokeColor=colors.blue, strokeWidth=5))
d.add(Line(50,100, 300,50,
     strokeColor=colors.red,
     strokeWidth=10,
     strokeDashArray=[10, 20]))
d.add(PolyLine([120,110, 130,150, 140,110, 150,150, 160,110,
          170,150, 180,110, 190,150, 200,110],
         strokeWidth=2,
         strokeColor=colors.purple))
    """,
        name='d',
    )
    pdf.add_caption("线和折线示例", category=constant.CAPTION_IMAGE)

    pdf.add_heading("字符串", level=3)
    pdf.add_paragraph(
        '$ReportLab$ 图形包并不是为花哨的文本布局而设计的，'
        '但它可以将字符串放置在所需的位置上，'
        '并进行 $left/right/center$ 对齐。'
        '让我们指定一个$String$对象，看看它的属性。'
    )
    pdf.add_code_eg(
        """
    >>> s = String(10, 50, 'Hello World')
    >>> s.dumpProperties()
    fillColor = Color(0.00,0.00,0.00)
    fontName = Times-Roman
    fontSize = 10
    text = Hello World
    textAnchor = start
    x = 10
    y = 50
    >>>
    """
    )
    pdf.add_paragraph(
        "字符串有一个 $textAnchor$ 属性，它的值可以是 $'start'$、$'middle'$、$'end'$之一。"
        "如果设置为$'start'$，则$x$和$y$与字符串的开始相关，以此类推。"
        "这提供了一个简单的方法来对齐文本。"
    )
    pdf.add_paragraph(
        '字符串使用一个通用的字体标准：$Acrobat Reader$ 中存在的 $Type 1 Postscript$ 字体。'
        '因此，我们可以在 $ReportLab$ 中使用基本的14种字体，并获得准确的指标。'
        '我们最近还增加了对额外的$Type 1$字体的支持，'
        '渲染器都知道如何渲染$Type 1$字体。'
    )
    pdf.add_paragraph(
        "下面是一个使用下面代码片段的更漂亮的例子。"
        "请查阅 $ReportLab$ 用户指南，了解像 $'DarkGardenMK'$ 这样的非标准字体是如何被注册的。"
    )
    pdf.add_code_eg(
        """
        d = Drawing(400, 200)
        for size in range(12, 36, 4):
            d.add(String(10+size*2, 10+size*2, 'Hello World',
                         fontName='Times-Roman',
                         fontSize=size))
    
        d.add(String(130, 120, 'Hello World',
                     fontName='Courier',
                     fontSize=36))
    
        d.add(String(150, 160, 'Hello World',
                     fontName='DarkGardenMK',
                     fontSize=36))
    """
    )
    rl_config.warnOnMissingFontGlyphs = 0
    flolder = folder = os.path.dirname(reportlab.__file__) + os.sep + 'fonts'
    afmFile = os.path.join(folder, 'DarkGardenMK.afm')
    pfbFile = os.path.join(folder, 'DarkGardenMK.pfb')
    T1face = pdfmetrics.EmbeddedType1Face(afmFile, pfbFile)
    T1faceName = 'DarkGardenMK'
    pdfmetrics.registerTypeFace(T1face)
    T1font = pdfmetrics.Font(T1faceName, T1faceName, 'WinAnsiEncoding')
    pdfmetrics.registerFont(T1font)

    d = Drawing(400, 200)
    for size in range(12, 36, 4):
        d.add(
            String(
                10 + size * 2,
                10 + size * 2,
                'Hello World',
                fontName='Times-Roman',
                fontSize=size,
            )
        )

    d.add(String(130, 120, 'Hello World', fontName='Courier', fontSize=36))

    d.add(String(150, 160, 'Hello World', fontName='DarkGardenMK', fontSize=36))

    pdf.add_draw(d, '花式字体样例')

    pdf.add_heading("Paths", level=3)
    pdf.add_paragraph(
        '$Postscript paths$ 是图形学中一个广为人知的概念。'
        '它们在$reportlab/graphics$中还没有实现，但很快就会实现。'
    )

    pdf.add_heading("Groups", level=3)
    pdf.add_paragraph(
        '最后，我们有 $Group$ 对象。'
        '一个组有一个内容列表，就是其他节点。'
        '它还可以应用变换 -- 它的内容可以被旋转、缩放或移动。'
        '如果你懂数学，你可以直接设置变换。'
        '否则它提供了旋转、缩放等方法。'
        '在这里，我们做一个旋转和转换的组。'
    )
    pdf.add_code_eg(
        """
    >>> g =Group(shape1, shape2, shape3)
    >>> g.rotate(30)
    >>> g.translate(50, 200)
    """
    )
    pdf.add_paragraph(
        '组提供了一个重复使用的工具。'
        '你可以做一堆形状来表示某个组件 '
        '--比如说，一个坐标系--并把它们放在一个叫做 "Axis" (轴) 的组里。'
        '然后你可以把这个组放到其他组中，每个组都有不同的平移和旋转，'
        '你就会得到一堆轴。它仍然是同一个组，被画在不同的地方。'
    )
    pdf.add_paragraph('让我们用一些只稍微多一点的代码来做这件事。')
    pdf.add_code_eg(
        """
        d = Drawing(400, 200)
    
        Axis = Group(
            Line(0,0,100,0),  # x axis
            Line(0,0,0,50),   # y axis
            Line(0,10,10,10), # ticks on y axis
            Line(0,20,10,20),
            Line(0,30,10,30),
            Line(0,40,10,40),
            Line(10,0,10,10), # ticks on x axis
            Line(20,0,20,10),
            Line(30,0,30,10),
            Line(40,0,40,10),
            Line(50,0,50,10),
            Line(60,0,60,10),
            Line(70,0,70,10),
            Line(80,0,80,10),
            Line(90,0,90,10),
            String(20, 35, 'Axes', fill=colors.black)
            )
    
        firstAxisGroup = Group(Axis)
        firstAxisGroup.translate(10,10)
        d.add(firstAxisGroup)
    
        secondAxisGroup = Group(Axis)
        secondAxisGroup.translate(150,10)
        secondAxisGroup.rotate(15)
    
        d.add(secondAxisGroup)
    
        thirdAxisGroup = Group(Axis,
                               transform=mmult(translate(300,10),
                                               rotate(30)))
        d.add(thirdAxisGroup)
    """
    )

    d = Drawing(400, 200)
    Axis = Group(
        Line(0, 0, 100, 0),  # x axis
        Line(0, 0, 0, 50),  # y axis
        Line(0, 10, 10, 10),  # ticks on y axis
        Line(0, 20, 10, 20),
        Line(0, 30, 10, 30),
        Line(0, 40, 10, 40),
        Line(10, 0, 10, 10),  # ticks on x axis
        Line(20, 0, 20, 10),
        Line(30, 0, 30, 10),
        Line(40, 0, 40, 10),
        Line(50, 0, 50, 10),
        Line(60, 0, 60, 10),
        Line(70, 0, 70, 10),
        Line(80, 0, 80, 10),
        Line(90, 0, 90, 10),
        String(20, 35, 'Axes', fill=colors.black),
    )
    firstAxisGroup = Group(Axis)
    firstAxisGroup.translate(10, 10)
    d.add(firstAxisGroup)
    secondAxisGroup = Group(Axis)
    secondAxisGroup.translate(150, 10)
    secondAxisGroup.rotate(15)
    d.add(secondAxisGroup)
    thirdAxisGroup = Group(
        Axis, transform=mmult(translate(300, 10), rotate(30))
    )
    d.add(thirdAxisGroup)
    # draw(d, "Groups doc_examples")
    pdf.add_draw(d, "$Groups$ 示例")

    pdf.add_heading("小部件", level=2)
    pdf.add_paragraph('现在，我们描述小部件及其与形状的关系。 ' '通过许多示例，展示了小部件如何使可重用图形组件成为现实。')

    pdf.add_heading("Shapes vs. Widgets", level=3)
    pdf.add_paragraph(
        '到目前为止，图纸一直是 "$pure data$"(纯数据)。'
        '除了协助程序员检查和检验图纸外，它们中没有任何代码可以真正做任何事情。'
        '事实上，这是整个概念的基石，也是让我们实现可移植性的原因'
        '--渲染器只需要实现原始形状。'
    )
    pdf.add_paragraph(
        '我们希望构建可重复使用的图形对象，包括一个强大的图表库。'
        '要做到这一点，我们需要重用比矩形和圆形更有形的东西。'
        '我们应该能够编写对象供其他人重用 '
        '--箭头、齿轮、文本框、UML图节点，甚至是完全成熟的图表。'
    )
    pdf.add_paragraph(
        '小部件标准是建立在shapes模块之上的标准，'
        '任何人都可以编写新的小部件，我们可以建立它们的库。'
        '$Widget$ 支持 $getProperties()$ 和 $setProperties()$ 方法，'
        '所以你可以检查和修改，也可以用统一的方式记录它们。'
    )
    pdf.add_bullet('小部件是一个可重复使用的形状')
    pdf.add_bullet('当调用 $draw()$ 方法时，它可以在没有参数的情况下进行初始化，' '它创建了一个原始形状或一个组来表示自己。')
    pdf.add_bullet('它可以有任何你想要的参数，它们可以驱动它的绘制方式。')
    pdf.add_bullet(
        '它有一个$demo()$方法，该方法应以200x100矩形返回一个精美的绘制示例。 '
        '这是自动文档编制工具的基础。 $demo()$方法也应该有一个写得很好的文档字符串，因为它也可以打印！'
    )
    pdf.add_paragraph(
        '小部件与图形只是一捆形状的想法背道而驰。 他们肯定有自己的代码吗？ '
        '它们的工作方式是，小部件可以将自身转换为一组原始形状。 '
        '如果其某些组件本身就是小部件，它们也将被转换。 '
        '这在渲染过程中自动发生。 '
        '渲染器将看不到图表小部件，而只会看到矩形，直线和字符串的集合。 '
        '您还可以显式 “$flatten out$” (扁平化) 工程图，从而将所有小部件都转换为基元。'
    )

    pdf.add_heading("使用一个小部件", level=3)
    pdf.add_paragraph('让我们想象一个简单的新部件。' '我们将使用一个小部件来绘制一张脸，然后展示它是如何实现的。')
    pdf.add_code_eg(
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
    pdf.add_draw(d, '小部件示例')

    pdf.add_paragraph('让我们看看它有哪些可用的属性，使用我们前面看到的 $setProperties()$ 方法。')
    pdf.add_code_eg(
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

    pdf.add_paragraph(
        '上面的代码似乎奇怪的一件事是，当我们制作面孔时，我们没有设置大小或位置。 '
        '这是必要的折衷方案，以允许使用一个统一的界面来构造小部件并对其进行记录'
        '-它们不能在其 $__init__()$ 方法中要求参数。 '
        '取而代之的是，通常将它们设计为适合200 x 100的窗口，'
        '然后在创建后通过设置诸如 $x, y, width$ 等属性来移动或调整它们的大小。'
    )
    pdf.add_paragraph(
        '此外，一个小部件总是提供一个$demo()$方法。'
        '像这样简单的总是在设置属性之前做一些合理的事情，但更复杂的像图表这样的就没有任何数据可供绘制。'
        '文档工具会调用$demo()$，'
        '这样你的花哨的新图表类就可以创建一张图来展示它的能力。'
    )
    pdf.add_paragraph('以下是一些简单的小部件，可在模块 <i>$signsandsymbols.py$</i> 中使用。')

    pdf.add_embedded_code(
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
    """,
        name='d',
    )
    pdf.add_caption(
        '一些来自 $signandsymbols.py$ 的例子。', category=constant.CAPTION_IMAGE
    )
    pdf.add_paragraph('而这是生成它们所需要的代码，如上图所示。')

    pdf.add_heading("复合小部件", level=3)
    pdf.add_paragraph(
        '让我们想象一下，一个复合小组件可以并排绘制两个面孔。' '当你有了 $Face widget$ 时，就可以很容易地构建这个小部件。'
    )
    pdf.add_code_eg(
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
    pdf.add_paragraph(
        "故意暴露了'$faceOne$'和'$faceTwo$'这两个属性，这样你就可以直接获取它们。也可以有顶层属性，但本例中没有。"
    )
    pdf.add_heading("校验小部件", level=3)
    pdf.add_paragraph(
        '小组件设计者决定验证的策略，但默认情况下，' '如果设计者提供了检查信息，它们就会像形状一样工作--检查每一个任务。'
    )
    pdf.add_heading("实现小部件", level=3)
    pdf.add_paragraph('我们试图让它尽可能容易地实现小部件。下面是一个不做任何类型检查的 $Face$ 小组件的代码。')
    pdf.add_code_eg(
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
    pdf.add_paragraph('我们在这个文档中省略了所有绘制形状的代码，但你可以在 $widgetbase.py$ 中找到它。')
    pdf.add_paragraph(
        '默认情况下，任何没有前导下划线的属性都会被 $setProperties$ 返回。这是为了鼓励一致的编码惯例而特意制定的政策。'
    )
    pdf.add_paragraph(
        '一旦你的 $widget$ 工作了，你可能想要添加对验证的支持。'
        '这涉及到在类中添加一个名为 $_verifyMap$ 的字典，它从属性名映射到 "检查函数"。'
        '$widgetbase.py$ 模块定义了一堆检查函数，比如 $isNumber$, $isListOfShapes$ 等等。'
        '你也可以简单地使用 $None$，这意味着属性必须存在，但可以有任何类型。'
        '而且你可以也应该写你自己的检查函数。'
        '我们想将 "$mood$" 自定义属性限制为 "$happy$"、"$sad$"或 "$ok$" 等值。'
        '所以我们这样做:'
    )
    pdf.add_code_eg(
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
    pdf.add_paragraph(
        '这个检查将在每次属性分配时执行；'
        '或者，如果$config.shapeChecking$是关闭的，'
        '每当你调用$myFace.verify()$时，这个检查就会被执行。'
    )
    pdf.add_heading("记录小部件", level=3)
    pdf.add_paragraph(
        '我们正在开发一个通用工具来记录任何Python包或模块；'
        '它已经记录到到 $ReportLab$ 中，并将用于为 $ReportLab$包生成一个引用。'
        '当它遇到小部件时，它会在手册中添加额外的章节，包括：'
    )
    pdf.add_bullet('您的小组件类的文档字符串')
    pdf.add_bullet('从您的^demo()^方法中提取的代码片段，以便人们可以看到如何使用它')
    pdf.add_bullet('由^demo()^方法产生的图画。')
    pdf.add_bullet('绘图中小组件的属性转储。')
    pdf.add_paragraph(
        '这个工具意味着我们可以保证在网站和印刷品上的小部件和图表上都有最新的文档； ' '而且您也可以为自己的小部件做同样的事情！'
    )
    pdf.add_heading("小工具设计策略", level=3)
    pdf.add_paragraph(
        '我们无法提出一个一致的架构来设计 $widget$，所以我们把这个问题留给了作者！'
        '如果你不喜欢默认的验证策略，或者是 $setProperties/getProperties$ 的工作方式，'
        '你可以自己覆盖它们。'
    )
    pdf.add_paragraph(
        '对于简单的 $widgets$ ，建议你做我们上面所做的：'
        '选择非重叠的属性，在 $__init__$ 上初始化每个属性，'
        '然后在调用 $draw()$ 时构造一切。你可以使用 $__setattr__$ 钩子，'
        '当某些属性被设置时，就会更新所有的东西。'
        '考虑一个饼图。如果你想暴露各个切片，你可以写这样的代码。'
    )
    pdf.add_code_eg(
        """
    from reportlab.graphics.charts import piecharts
    pc = piecharts.Pie()
    pc.defaultColors = [navy, blue, skyblue] #used in rotation
    pc.data = [10,30,50,25]
    pc.slices[7].strokeWidth = 5
    """
    )
    pdf.add_paragraph(
        '最后一行是有问题的，因为我们只创建了四个切片'
        '--事实上，我们可能还没有创建它们。'
        '$pc.slices[7]$是否会引起错误？'
        '如果定义了第七个楔形图，用来覆盖默认设置，这是不是一个解决方案？'
        '我们现在把这个问题直接丢给 $widget$ 作者，并建议您在暴露 "子对象" 之前先做一个简单的工作，'
        '因为子对象的存在取决于其他属性的值 :-)'
    )
    pdf.add_paragraph(
        '我们还讨论了父级小部件可以将属性传递给其子级的规则。 '
        '人们似乎普遍希望以一种全局的方式来表示“所有切片均从其父级的 $lineWidth$ 获得其 $lineWidth$ ”，'
        '而无需进行大量重复编码。 '
        '我们没有通用的解决方案，因此请再次将其留给小部件作者。 '
        '我们希望人们将尝试下推，下拉和模式匹配方法，并提出一些不错的东西。'
        ' 同时，我们当然可以编写整体式的图表小部件，'
        '这些小部件的工作方式类似于Visual Basic和Delphi。'
    )
    pdf.add_paragraph('现在看看下面的示例代码，使用一个早期版本的饼图小组件和它产生的输出。')

    pdf.add_embedded_code(
        """
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing, String
from reportlab.lib import colors

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
""",
        name='d',
    )
    pdf.add_caption('一些饼图示例', category=constant.CAPTION_IMAGE)


def chapter11(pdf):
    pass


def chapter12_appendix_1(pdf):
    pdf.add_appendix("$ReportLab$ 示例")
    pdf.add_paragraph(
        "在$reportlab/demos$的子目录中，有许多工作实例，几乎展示了 $reportlab$ 使用的所有方面。"
    )

    pdf.add_heading("奥德赛", level=2)
    pdf.add_paragraph(
        "$odyssey.py$、$dodyssey.py$和$fodyssey.py$"
        "这三个脚本都是取文件$oddyssey.txt$并生成PDF文档。"
        "包含的 $odyssey.txt$ 很短；"
        "更长和更多的测试版本可以在 <a href=\"ftp://ftp.reportlab.com/odyssey.full.zip\">"
        "$ftp://ftp.reportlab.com/odyssey.full.zip$</a> 找到。"
    )
    pdf.add_code_eg(
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
    pdf.add_paragraph(
        "$odyssey.py$ 脚本显示了简单的格式化。"
        "它的运行速度相当快，但它所做的只是收集文本并将其强行放到画布页面上。"
        "它完全不进行段落操作，所以你可以看到 $XML$ &lt; 和 &gt; 标签。"
    )
    pdf.add_paragraph(
        "脚本 $fodyssey.py$ 和 $dodyssey.py$ 处理段落格式，"
        "所以你可以看到颜色变化等。"
        "这两个脚本都使用了文档模板类， $dodyssey.py$ 脚本显示了做双列布局的能力，并使用了多个页面模板。"
    )
    pdf.add_heading("标准字体和颜色", level=2)
    pdf.add_paragraph(
        "在$reportlab/demos/stdfonts$中，"
        "脚本 $stdfonts.py$ 可以用来说明 $ReportLab$ 的标准字体。"
        "使用以下方法运行该脚本"
    )
    pdf.add_code_eg(
        """
    cd reportlab\\demos\\stdfonts
    python stdfonts.py
    """
    )
    pdf.add_paragraph(
        "生成两个PDF文档，$StandardFonts_MacRoman.pdf$ 和 $StandardFonts_WinAnsi.pdf$，"
        "其中显示了两种最常见的内置字体编码。"
    )
    pdf.add_paragraph(
        "在$reportlab/demos/colors$中的 $colortest.py$ 脚本展示了 "
        " $reportlab$ 设置和使用颜色的不同方式。"
    )
    pdf.add_paragraph(
        "试着运行该脚本并查看输出文档，$colortest.pdf$。"
        "这显示了不同的颜色空间和大量在$reportlab.lib.cols$模块中命名的颜色选择。"
    )
    pdf.add_paragraph(
        "$Dinu Gherman$ 贡献了这个有用的脚本，"
        "它使用 $reportlab$ 从 $Python$ 脚本中生成漂亮的彩色$PDF$文档，包括类、方法和函数的书签。"
        "要得到一个漂亮的主脚本版本，可以尝试一下"
    )
    pdf.add_code_eg(
        """
    cd reportlab/demos/py2pdf
    python py2pdf.py py2pdf.py
    acrord py2pdf.pdf
    """
    )
    pdf.add_paragraph("即我们使用$py2pdf$在文档中生成一个漂亮的$py2pdf.py$版本，根名相同，扩展名为$.pdf$。")
    pdf.add_paragraph("$py2pdf.py$脚本有很多选项，这些选项超出了这个简单介绍的范围，请参考脚本开头的注释。")
    pdf.add_heading("Gadflypaper", level=2)
    pdf.add_paragraph(
        "$reportlab/demos/gadflypaper$中的$Python$脚本$gfe.py$使用了内联式的文档编制方式。"
        "这个脚本几乎完全由$Aaron Watters$制作，"
        "产生了一个描述$Aaron$的$gadfly$内存数据库的Python文档。"
        "要生成该文档，请使用"
    )
    pdf.add_code_eg(
        """
    cd reportlab\\gadflypaper
    python gfe.py
    start gfe.pdf
    """
    )
    pdf.add_paragraph(
        "PDF文档中的所有内容都是由脚本制作的，这就是为什么这是一种内联式文档制作方式。"
        "所以，为了生成一个标题，后面跟着一些文本，脚本使用了函数$header$和$p$，"
        "这两个函数接收一些文本并附加到一个全局故事列表中。"
    )
    pdf.add_code_eg(
        '''
    header("Conclusion")
    
    p("""The revamped query engine design in Gadfly 2 supports
    ..........
    and integration.""")
    '''
    )
    pdf.add_heading("Pythonpoint", level=2)
    pdf.add_paragraph(
        "$Andy Robinson$改进了$pythonpoint.py$脚本("
        "在$reportlab\\demos\\pythonpoint$中)，直到它成为一个真正有用的脚本。"
        "它接收一个包含XML标记的输入文件，并使用一个 $xmllib$样式 分析器将标记映射到$PDF$幻灯片中。"
        "当在它自己的目录下运行时，$pythonpoint.py$ "
        "将文件 $pythonpoint.xml$ 作为默认输入，并生成 $pythonpoint.pdf$，"
        "这是 $Pythonpoint$ 的文档。您也可以通过一篇较早的文章看到它的运行情况。"
    )
    pdf.add_code_eg(
        """
    cd reportlab\\demos\\pythonpoint
    python pythonpoint.py monterey.xml
    start monterey.pdf
    """
    )
    pdf.add_paragraph(
        "$pythonpoint$ 不仅是自文档，而且还演示了 $reportlab$ 和 $PDF$ 。"
        "它使用了 $reportlab$ 的许多功能（文档模板、表格等）。"
        "$PDF$ 的奇特功能，如淡入和书签也被展示得很好。"
        "$XML$ 文档的使用可以与 $gadflypaper$ 演示中的<i>$inline$</i>风格形成对比；"
        "内容与格式完全分离。"
    )


def chapter13_appendix_2(pdf):
    pdf.add_appendix("译者备注")

    pdf.add_paragraph("后面的信息为译者在翻译本手册时，学习，查询资料做的备注，或者说总结，没有对应的英文版...")
    pdf.add_heading("$Win Ansi$ 编码 和 $Mac Roman$ 编码", level=2)
    pdf.add_paragraph(
        '参考: <font color="blue"><u>'
        '<a href="https://www.ziti163.com/Item/2054.aspx">'
        '$ANSI$，$ISO-8859-1$和$MacRoman$字符集之间的差异'
        '</a></u></font>'
    )
    pdf.add_paragraph('以下为原文和译文:')
    pdf.add_paragraph(
        'Of the three main 8-bit character sets, '
        'only ISO-8859-1 is produced by a standards organization.  '
        'The three sets are identical for the 95 characters from 32 to 126, '
        'the ASCII character set.  '
        'The ANSI character set, also known as Windows-1252, '
        'has become a Microsoft proprietary character set; '
        'it is a superset of ISO-8859-1 with the addition of 27 characters '
        'in locations that ISO designates for control codes.  '
        'Apple’s proprietary MacRoman character set '
        'contains a similar variety of characters from 128 to 255, '
        'but with very few of them assigned the same numbers, '
        'and also assigns characters to the control-code positions.'
    )
    pdf.add_paragraph(
        'The characters that appear in the first column '
        'of the following tables are generated '
        'from Unicode numeric character references, '
        'and so they should appear correctly in any Web browser '
        'that supports Unicode and that has suitable fonts available, '
        'regardless of the operating system.'
    )

    pdf.add_bullet('ANSI characters not present in ISO-8859-1')
    pdf.add_bullet('ANSI characters not present in MacRoman')
    pdf.add_bullet('ISO-8859-1 characters not present in ANSI')
    pdf.add_bullet('ISO-8859-1 characters not present in MacRoman')
    pdf.add_bullet('MacRoman characters not present in ANSI')
    pdf.add_bullet('MacRoman characters not present in ISO-8859-1')
    pdf.add_paragraph("译文:")
    pdf.add_paragraph(
        '在三种主要的8位字符集中，只有$ISO-8859-1$是由标准组织制作的。 '
        '这三个字符集对于32到126这95个字符，即$ASCII$字符集是相同的。 '
        '$ANSI$字符集，也就是$Windows-1252$，已经成为微软的专有字符集；'
        '它是$ISO-8859-1$的超集，在ISO指定控制代码的位置增加了27个字符。 '
        '苹果公司专有的$MacRoman$字符集包含从128到255个类似的各种字符，'
        '但其中很少有相同的数字，而且还将字符分配到控制码的位置。'
    )
    pdf.add_paragraph(
        '下表第一栏中显示的字符是从$Unicode$数字字符引用生成的，'
        '因此，无论使用什么操作系统，'
        '它们都应该在支持$Unicode$并具有合适的可用字体的任何$Web$浏览器中正确显示。'
    )
    pdf.add_bullet('$ISO-8859-1$ 中不存在 $ANSI$ 字符')
    pdf.add_bullet('$MacRoman$ 中不存在 $ANSI$ 字符')
    pdf.add_bullet('$ANSI$ 中不存在 $ISO-8859-1$ 字符')
    pdf.add_bullet('$MacRoman$ 中不存在 $ISO-8859-1$ 字符')
    pdf.add_bullet('$ANSI$ 中不存在 $MacRoman$ 字符')
    pdf.add_bullet('$ISO-8859-1$ 中不存在 $MacRoman$ 字符')
    pdf.add_heading('其他参考:', level=3)
    pdf.add_paragraph(
        '$Win Ansi$ 编码总体来说就是, '
        '微软公司根据$windows$系统的本地化和国际化地区，'
        '默认采取的某种编码.'
        '参考:<font color="blue"><u>'
        '<a href="https://www.cnblogs.com/malecrab/p/5300486.html">'
        '$ANSI$是什么编码？</a></u></font>'
    )

    pdf.add_heading('生成pdf文件，推荐开源字体：思源黑体', level=2)

    pdf.add_paragraph(
        'True Type 字体介绍: <font color="blue"><u>'
        '<a href="https://blog.csdn.net/gaojinshan/article/details/80319856">'
        'https://blog.csdn.net/gaojinshan/article/details/80319856'
        '</a></u></font>'
    )

    pdf.add_paragraph(
        '思源黑体、思源宋体TTF介绍: <font color="blue"><u>'
        '<a href="https://www.v2ex.com/t/399030">'
        'https://www.v2ex.com/t/399030'
        '</a></u></font>'
    )

    pdf.add_paragraph("$GitHub 资源: $")

    pdf.add_bullet(
        '1. <font color="blue"><u>'
        '<a href="https://github.com/be5invis/source-han-sans-ttf/releases">'
        'https://github.com/be5invis/source-han-sans-ttf/releases'
        '</a></u></font>'
    )
    pdf.add_bullet(
        '2. <font color="blue"><u>'
        '<a href="https://github.com/junmer/source-han-serif-ttf">'
        'https://github.com/junmer/source-han-serif-ttf'
        '</a></u></font>'
    )
    pdf.add_bullet(
        '3. <font color="blue"><u>'
        '<a href="https://github.com/Pal3love/Source-Han-TrueType">'
        'https://github.com/Pal3love/Source-Han-TrueType'
        '</a></u></font>'
    )


def main(filename):
    fonts_dir = os.path.join(
        os.path.dirname(os.path.abspath(BASE_DIR)), 'fonts'
    )
    pdf = PDF(filename, fonts_dir=fonts_dir)

    chapter1_introduction(pdf)
    chapter2_overview(pdf)
    chapter3_font(pdf)
    chapter4_special_features(pdf)
    chapter5_platypus(pdf)
    chapter6_paragraph(pdf)
    chapter7_table(pdf)
    chapter8_flowables(pdf)
    chapter9_useful_flowables(pdf)
    chapter10_graph(pdf)
    chapter11(pdf)
    chapter12_appendix_1(pdf)
    chapter13_appendix_2(pdf)
    pdf.build_2_save()


if __name__ == '__main__':

    setup_logging()
    main('test.pdf')
