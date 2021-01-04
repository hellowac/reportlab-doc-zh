import os
import logging
from datetime import datetime

import reportlab
from components import constant
from core import examples
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


def chapter1(pdf):
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
        "<a href='http://docs.python.org/tutorial/'>http://docs.python.org/tutorial/</a>"
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
        "<a href='http://www.reportlab.com/software/documentation/relnotes/30/'>"
        "^http://www.reportlab.com/software/documentation/relnotes/30/^</a>"
    )


def chapter2(pdf):
    pdf.add_heading("使用 $pdfgen$ 生成图形和文本", level=1)
    pdf.add_heading("基本概念", level=2)
    pdf.add_paragraph(
        "$pdfgen$包是生成PDF文档的最低级别接口。 一个$pdfgen$程序本质上是一个将文档 \"绘制\"到页面序列上的指令序列。 "
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
        "$showPage$方法会使$canvas$停止在当前页上绘制，任何进一步的操作都会在随后的页面上绘制（如果有任何进一步的操作--如果没有的话"
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
        "参数$filename$控制最终PDF文件的名称。 你也可以传入任何开放的二进制流（如$sys.stdout$，python过程中标准的二进制编码输出），PDF文件将被写入该流。 "
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
    pdf.add_code_eg(examples.testhello)
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
    pdf.add_illustration(examples.hello, 'pdfgen 生成 "Hello World"')

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
        """canvas.drawImage(self, image, x,y, width=None,height=None,mask=None) """
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
    pdf.add_code_eg(examples.testcoords)
    pdf.add_paragraph(
        "在默认的用户空间中，\"原点\"^(0,0)^点在左下角。  "
        "在默认的用户空间中执行$coords$函数（针对 \"演示迷你页\"），我们得到以下结果。"
    )
    pdf.add_illustration(examples.coords, '坐标系统')

    pdf.add_heading("移动原点：$translate$方法", level=3)
    pdf.add_paragraph(
        "通常情况下，\"移动原点 \"到左下角的新点是很有用的。 "
        "$canvas.translate(^x,y^)$方法将当前页面的原点移动到当前由^(x,y)^确定的点。"
    )
    pdf.add_paragraph("例如下面的平移函数首先移动原点，然后再绘制如上所示的相同对象。")
    pdf.add_code_eg(examples.testtranslate)
    pdf.add_paragraph("这就产生了以下结果：")
    pdf.add_illustration(examples.translate, "移动原点：$translate$方法")
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
    pdf.add_code_eg(examples.testscale)
    pdf.add_paragraph("这样就会产生一个 \"短小精悍\"的缩小版的之前显示的操作。")
    pdf.add_illustration(examples.scale, "缩放坐标系统")
    pdf.add_pencil_note()
    pdf.add_text_note("缩放也可能会将对象或对象的一部分从页面上移开，或者可能会导致对象 \"缩水为零\"。")
    pdf.add_paragraph("缩放和翻译可以结合起来，但操作的顺序很重要。")
    pdf.add_code_eg(examples.testscaletranslate)
    pdf.add_paragraph(
        "这个示例函数首先保存当前的$canvas$状态，然后进行$scale$和$translate$操作。 "
        "之后，函数恢复了状态（有效地消除了缩放和翻译的影响），"
        "然后以不同的顺序进行<i>相同的</i>操作。"
        "观察下面的效果。"
    )
    pdf.add_illustration(examples.scaletranslate, "缩放和翻译")
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
    pdf.add_code_eg(examples.testmirror)
    pdf.add_paragraph("创建$coord$函数绘制的元素的镜像。")
    pdf.add_illustration(examples.mirror, "镜像")
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
    pdf.add_code_eg(examples.testRGBcolors)
    pdf.add_illustration(examples.colorsRGB, "RGB 颜色模块")
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
    pdf.add_code_eg(examples.testalpha)
    pdf.add_illustration(examples.alpha, "Alpha 例子")
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
    pdf.add_code_eg(examples.testCMYKcolors)
    pdf.add_illustration(examples.colorsCMYK, "CMYK颜色模型")
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
    pdf.add_illustration(examples.overPrint, "OverPrint示例")
    pdf.add_heading("其他对象的打印顺序示例", level=3)
    pdf.add_paragraph('"SPUMONI"字样用白色涂抹在彩色长方形上，有明显的 "去除 "字体内部颜色的效果。')
    pdf.add_code_eg(examples.testspumoni)
    pdf.add_illustration(examples.spumoni, "涂抹颜色")
    pdf.add_paragraph("由于默认的$canvas$背景是白色的，在白色背景上画上白色的字母，单词的最后一个字母不可见。")
    pdf.add_paragraph("这种分层建立复杂绘画的方法可以在$pdfgen$中完成非常多的层数--比起处理物理颜料时的物理限制要少。")
    pdf.add_code_eg(examples.testspumoni2)
    pdf.add_paragraph("Spumoni2$函数在$spumoni$图上叠加一个冰淇淋圆锥。 请注意，圆锥和勺子的不同部分也会互相分层。")
    pdf.add_illustration(examples.spumoni2, "层层叠加")
    pdf.add_heading("标准字体和文本对象", level=2)
    pdf.add_paragraph(
        "在$pdfgen$中可以用许多不同的颜色、字体和大小来绘制文本。"
        "$textsize$函数演示了如何改变文本的颜色、字体和大小，以及如何在页面上放置文本。"
    )
    pdf.add_code_eg(examples.testtextsize)
    pdf.add_paragraph("$textsize$函数生成了以下页面。")
    pdf.add_illustration(examples.textsize, "不同字体和大小的文字")
    pdf.add_paragraph("不同字体和大小的文本在$pdfgen$中总是有许多不同的字体。")
    pdf.add_code_eg(examples.testfonts)
    pdf.add_paragraph(
        "函数$fonts$列出了始终可用的字体。" "这些字体不需要存储在PDF文档中，" "因为它们保证在Acrobat Reader中存在。"
    )
    pdf.add_illustration(examples.fonts, "14种标准字体")
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
    pdf.add_code_eg(examples.testcursormoves1)
    pdf.add_paragraph("函数$cursormoves$依靠文本光标的自动移动来放置原点后的文本。")
    pdf.add_illustration(examples.cursormoves1, "文本光标的移动方式")
    pdf.add_paragraph(
        "也可以通过使用$moveCursor$方法更明确地控制光标的移动"
        "（该方法将光标移动为从当前<i>线</i>开始的偏移量，而不是当前光标，"
        "并且该方法还具有正^y^偏移量移动<i>向下</i>)"
        "与正常几何形状相反，正^y^通常向上移动。"
    )
    pdf.add_code_eg(examples.testcursormoves2)
    pdf.add_paragraph("在这里，$textOut$不会向下移动一行，而$textLine$函数则向下移动。")
    pdf.add_illustration(examples.cursormoves2, "文本光标如何再次移动")
    pdf.add_heading("字符间距", level=3)
    pdf.add_code_eg("""textobject.setCharSpace(charSpace)""")
    pdf.add_paragraph("$setCharSpace$方法调整文本的一个参数--字符间的间距。")
    pdf.add_code_eg(examples.testcharspace)
    pdf.add_paragraph("$charspace$函数行使各种间距设置。它产生以下页面。")
    pdf.add_illustration(examples.charspace, "调整字符间距")
    pdf.add_heading("字距", level=3)
    pdf.add_code_eg("""textobject.setWordSpace(wordSpace)""")
    pdf.add_paragraph("$setWordSpace$方法调整字与字之间的空间。")
    pdf.add_code_eg(examples.testwordspace)
    pdf.add_paragraph("$wordspace$函数显示了下面各种文字空间设置的样子。")
    pdf.add_illustration(examples.wordspace, "调整字距")
    pdf.add_heading("水平缩放", level=3)
    pdf.add_code_eg("""textobject.setHorizScale(horizScale)""")
    pdf.add_paragraph("文本行可以通过$setHorizScale$方法进行水平拉伸或收缩。")
    pdf.add_code_eg(examples.testhorizontalscale)
    pdf.add_paragraph("水平缩放参数^horizScale^是以百分比的形式给出的（默认为100），所以下图所示的80设置看起来很瘦。")
    pdf.add_illustration(examples.horizontalscale, "调整水平文本的比例")
    pdf.add_heading("行间间距(领先)", level=3)
    pdf.add_code_eg("""textobject.setLeading(leading)""")
    pdf.add_paragraph("一条线的起始点和下一条线的起始点之间的垂直偏移称为前导偏移。 " "$setLeading$方法调整前导偏移。")
    pdf.add_code_eg(examples.testleading)
    pdf.add_paragraph("如下图所示，如果一行的前导偏移量设置得太小，我就会把前一行中的字符的底部部分写在上面。")
    pdf.add_illustration(examples.leading, "矫枉过正")
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
    pdf.add_code_eg(examples.teststar)
    pdf.add_paragraph("$star$函数被设计用来说明$pdfgen$支持的各种行式参数。")
    pdf.add_illustration(examples.star, "直线样式参数")
    pdf.add_heading("直线连接设置", level=3)
    pdf.add_paragraph("通过$setLineJoin$方法，可以调整线段在一个点上相接的是方块还是圆角顶点。")
    pdf.add_code_eg(examples.testjoins)
    pdf.add_paragraph("线条连接的设置只有对粗线条才真正有意义，因为对细线条看不清楚。")
    pdf.add_illustration(examples.joins, "不同的直线连接样式")
    pdf.add_heading("直线帽子设置", level=3)
    pdf.add_paragraph(
        "使用$setLineCap$方法调整的线帽设置，" "决定了终止线的终点是在顶点处的正方形、" "顶点上方的正方形还是顶点上方的半圆。"
    )
    pdf.add_code_eg(examples.testcaps)
    pdf.add_paragraph("线帽设置和线条连接设置一样，只有在线条较粗时才会清晰可见。")
    pdf.add_illustration(examples.caps, "直线帽子设置")
    pdf.add_heading("破折号和断线", level=3)
    pdf.add_paragraph("用$setDash$方法可以将线条分成点或破折号。")
    pdf.add_code_eg(examples.testdashes)
    pdf.add_paragraph("虚线或圆点的图案可以是简单的开/关重复图案，也可以指定为复杂的重复图案。")
    pdf.add_illustration(examples.dashes, "破折号")
    pdf.add_heading("用路径对象创建复杂的图形", level=3)
    pdf.add_paragraph(
        "线条、曲线、弧线等图形的组合可以使用路径对象组合成一个图形。"
        "例如下图所示的函数就是利用直线和曲线构造两个路径对象。"
        "这个函数将在后面的铅笔图标构造中使用。"
    )
    pdf.add_code_eg(examples.testpenciltip)
    pdf.add_paragraph(
        "请注意，铅笔头的内部是作为一个对象填充的，即使它是由几条线和曲线构成的。" "然后使用一个新的路径对象在其上绘制铅笔头。"
    )
    pdf.add_illustration(examples.penciltip, "铅笔头")
    pdf.add_heading("矩形、圆形、椭圆形。", level=2)
    pdf.add_paragraph(
        "$pdfgen$模块支持许多一般有用的形状，如矩形、圆角矩形、椭圆和圆。"
        "这些图形中的每一个都可以在路径对象中使用，也可以直接在$canvas$上绘制。 "
        "例如下面的$pencil$函数使用矩形和圆角矩形绘制了一个铅笔图标，"
        "并添加了各种填充颜色和其他一些注释。"
    )
    pdf.add_code_eg(examples.testpencil)
    pdf.add_pencil_note()
    pdf.add_text_note(
        "这个函数是用来创建左边的'边距铅笔'的。"
        "还要注意的是，元素的绘制顺序很重要，因为，"
        "例如，白色矩形'擦掉'了黑色矩形的一部分，"
        "而 '笔尖'则涂抹了黄色矩形的一部分。"
    )
    pdf.add_illustration(examples.pencil, "铅笔")
    pdf.add_heading("贝兹尔曲线", level=2)
    pdf.add_paragraph("想要构造具有弯曲边界的图形的程序，一般使用贝塞尔曲线来形成边界。")
    pdf.add_code_eg(examples.testbezier)
    pdf.add_paragraph(
        "Bezier曲线由四个控制点$(x1,y1)$，$(x2,y2)$，$(x3,y3)$，$(x4,y4)$指定。"
        "曲线起于$(x1,y1)$，止于$(x4,y4)$，从$(x1,y1)$到$(x2,y2)$的线段和从$(x3,y3)$到$(x4,y4)$的线段都与曲线形成切线。 "
        "而且曲线完全包含在凸图形中，顶点在控制点上。"
    )
    pdf.add_illustration(examples.bezier, "基本贝塞尔曲线")
    pdf.add_paragraph("上图($testbezier$的输出)显示了一个bezier曲线、控制点定义的切线和控制点处有顶点的凸图形。")
    pdf.add_heading("平滑地连接贝塞尔曲线序列", level=3)
    pdf.add_paragraph(
        "通常情况下，将几条贝塞尔曲线连接成一条平滑曲线是很有用的。 "
        "要想从几条贝塞尔曲线中构造一条较大的平滑曲线，"
        "请确保相邻贝塞尔曲线在控制点连接的切线位于同一直线上。"
    )
    pdf.add_code_eg(examples.testbezier2)
    pdf.add_paragraph('由$testbezier2$创建的图形描述了一条平滑的复曲线，因为相邻的切线 "排队"，如下图所示。')
    pdf.add_illustration(examples.bezier2, "bezier curves")
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
        '而$arcTo$方法则是将部分椭圆的起始点与当前的形状序列用线连接起来。 '
        '在画部分椭圆之前，先画出部分椭圆的线段。 '
        '点^(x1,y1)^和^(x2,y2)^定义包围椭圆的矩形的相对角点。'
        '$startAng$是一个角度(度数)，指定了部分椭圆的开始位置，其中0角是右边界的中点。'
        '围成的矩形（当^(x1,y1)^为左下角，^(x2,y2)^为右上角）。'
        '$extent$是指与椭圆上的横移。'
    )
    pdf.add_code_eg(examples.testarcs)
    pdf.add_paragraph("上面的$arcs$函数行使了两种局部椭圆方法。它产生了下面的图形。")
    pdf.add_illustration(examples.arcs, "弧线")
    pdf.add_code_eg("""pathobject.rect(x, y, width, height) """)
    pdf.add_paragraph("$rect$方法在^(x,y)^指定的^width^和^height^处画一个左下角的矩形。")
    pdf.add_code_eg("""pathobject.ellipse(x, y, width, height)""")
    pdf.add_paragraph(
        "$ellipse$方法在指定的^width^和^height^的^(x,y)^处绘制一个左下角的矩形包围的椭圆。"
    )
    pdf.add_code_eg("""pathobject.circle(x_cen, y_cen, r) """)
    pdf.add_paragraph("$circle$方法画一个以^(x_cen，y_cen)^为中心，半径^r^的圆。")
    pdf.add_code_eg(examples.testvariousshapes)
    pdf.add_paragraph("上面的$variousshapes$函数显示了一个放置在参考网格中的矩形、圆和椭圆。")
    pdf.add_illustration(examples.variousshapes, "路径对象中的矩形、圆形、椭圆形。")
    pdf.add_code_eg("""pathobject.close() """)
    pdf.add_paragraph(
        "$close$方法通过从图形的最后一点到图形的起始点(最近一次通过$moveTo$或$arc$或其他放置操作将画笔放置在纸上的点)画一条线段来关闭当前图形。"
    )
    pdf.add_code_eg(examples.testclosingfigures)
    pdf.add_paragraph("$closingfigures$函数说明了闭合或不闭合图形的效果，包括一条线段和一个部分椭圆。")
    pdf.add_illustration(examples.closingfigures, "闭合和不闭合的路径对象数字")
    pdf.add_paragraph("关闭或不关闭图形只影响图形的描边轮廓，而不影响图形的填充，如上图所示。")
    pdf.add_paragraph("关于使用路径对象绘图的更广泛的例子，请检查$hand$函数。")
    pdf.add_code_eg(examples.testhand)
    pdf.add_paragraph(
        '在调试模式下(默认)，$hand$函数显示了用于构成图形的贝塞尔曲线的切线段。'
        '请注意，当线段对齐时，曲线平滑地连接在一起，但当线段不对齐时，曲线显示出一个 "尖锐的边缘"。'
    )
    pdf.add_illustration(examples.hand, "手形图")
    pdf.add_paragraph(
        "在非调试模式下，$hand$函数只显示贝塞尔曲线。 如果设置了$fill$参数，则会使用当前的填充颜色填充图形。"
    )
    pdf.add_code_eg(examples.testhand2)
    pdf.add_text_note('边框的 "描边 "画在它们重叠的内部填充物上。')
    pdf.add_illustration(examples.hand2, "妙手回春")
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
        "第11章还详细介绍了ReportLab图表包及其组件（标签、坐标轴、图例和不同类型的图表，如柱状图、线状图和饼状图），"
        "它直接建立在图形库上。"
    )


def chapter3(pdf):
    pass


def chapter4(pdf):
    pass


def chapter5(pdf):
    pass


def chapter6(pdf):
    pass


def chapter7(pdf):
    pass


def chapter8(pdf):
    pass


def chapter9(pdf):
    pass


def chapter10(pdf):
    pass


def chapter11(pdf):
    pass


def main(filename):
    fonts_dir = os.path.join(
        os.path.dirname(os.path.abspath(BASE_DIR)), 'fonts'
    )
    pdf = PDF(filename, fonts_dir=fonts_dir)

    chapter1(pdf)
    chapter2(pdf)
    chapter3(pdf)
    chapter4(pdf)
    chapter5(pdf)
    chapter6(pdf)
    chapter7(pdf)
    chapter8(pdf)
    chapter9(pdf)
    chapter10(pdf)
    chapter11(pdf)
    pdf.build_2_save()


if __name__ == '__main__':

    setup_logging()
    main('test.pdf')
