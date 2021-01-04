import os
import logging
from datetime import datetime

import reportlab
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
        "使用环境变量，这些变量是$rl_settings.py$中以$RL_$开头的变量，例如$RL_verbose=1$。"
    )

    pdf.add_heading('有用的rl_config变量', level=3)
    pdf.add_bullet("verbose: 设置为整数值以控制诊断输出。")
    pdf.add_bullet("shapeChecking: 将此设置为零可关闭图形模块中的许多错误检查")
    pdf.add_bullet("defaultEncoding: 将此设置为WinAnsiEncoding或MacRomanEncoding。")
    pdf.add_bullet(
        "defaultPageSize：将其设置为reportlab/lib/pagesizes.py中定义的值之一；"
        "交付时将其设置为pagesizes.A4; 其他值是pagesizes.letter等。"
    )
    pdf.add_bullet(
        "defaultImageCaching：设置为零以禁止在硬盘驱动器上创建.a85文件。 "
        "默认设置是创建这些经过预处理的PDF兼容图像文件，以加快加载速度"
    )
    pdf.add_bullet("T1SearchPath：这是表示目录的字符串的python列表，可以查询有关类型1字体的信息")
    pdf.add_bullet(
        "TTFSearchPath：这是表示目录的字符串的python列表，可以查询该目录以获取有关TrueType字体的信息"
    )
    pdf.add_bullet("CMapSearchPath：这是表示目录的字符串的python列表，可以查询该目录以获取字体代码映射的信息。")
    pdf.add_bullet("showBoundary：设置为非零以绘制边界线。")
    pdf.add_bullet("ZLIB_WARNINGS：如果未找到Python压缩扩展，则设置为非零以获得警告。")
    pdf.add_bullet("pageCompression：设置为非零以尝试获取压缩的PDF。")
    pdf.add_bullet("allowtableBoundsErrors：设置为0会在非常大的Platypus表元素上强制执行错误")
    pdf.add_bullet("emptyTableAction：控制空表的行为，可以为“error”（默认），“indicate”或“ignore")
    pdf.add_bullet(
        "TrustedHosts：如果不是$None$，则列出受信任主机的全局模式；"
        "这些可以在＆lt; img＆gt;之类的地方使用。 段落文字中的标签。"
    )
    pdf.add_bullet("trustedSchemes：与 trustedHosts 一起使用的允许的 URL 方案的列表")

    pdf.add_paragraph("有关变量的完整列表，请参见文件$reportlab/rl_settings.py$。")
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
        "<b>Python文档</b>Python.org网站上的文档列表。"
        "<a href='http://www.python.org/doc/'>http://www.python.org/doc/</a>"
    )
    pdf.add_bullet(
        "<b>Python教程</b>"
        "官方的Python教程，最初由Guido van Rossum亲自编写."
        "<a href='http://docs.python.org/tutorial/'>http://docs.python.org/tutorial/</a>"
    )
    pdf.add_bullet(
        "<b>学习编程</b>"
        "Alan Gauld撰写的编程指南。 非常重视Python，但也使用其他语言。"
        "<a href='http://www.freenetpages.co.uk/hp/alan.gauld/'>http://www"
        ".freenetpages.co.uk/hp/alan.gauld/</a>"
    )
    pdf.add_bullet(
        "<b>即时Python</b>Magnus Lie Hetland撰写的长达6页的速成课程。"
        "<a href='http://www.hetland.org/python/instant-python.php$'>"
        "http://www.hetland.org/python/instant-python.php$</a>"
    )
    pdf.add_bullet(
        "<b>深入Python</b>适用于经验丰富的程序员的免费Python教程。"
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
    pdf.add_bullet("__init__.py允许导入可选的reportlab.local_rl_mods，以允许猴子打补丁等。")
    pdf.add_bullet(
        "rl_config现在可以导入rl_settings，还可以导入local_rl_settings，"
        "reportlab_settings.py，最后是 ~/.reportlab_settings"
    )
    pdf.add_bullet(
        "ReportLab C扩展现在位于reportlab中。 不再需要_rl_accel。 "
        "现在，所有_rl_accel导入都通过reportlab.lib.rl_accel"
    )
    pdf.add_bullet("xmllib以及用于引起HTMLParser问题的paraparser东西一去不复返了。")
    pdf.add_bullet("一些过时的C扩展名（sgmlop和pyHnj）消失了")
    pdf.add_bullet("_rl_accel C扩展模块对多线程系统的改进支持。")
    pdf.add_bullet(
        "删除了reportlab/lib/para.py和pycanvas.py。 这些最好属于第三方程序包，可以利用上面的Monkeypatching功能。"
    )
    pdf.add_bullet("增加了无需转换为RGB即可输出灰度和1位PIL图像的功能。 （由Matthew Duggan贡献）")
    pdf.add_bullet("高亮注释（由Ben Echols提供）")
    pdf.add_bullet("完全符合pip，easy_install，wheel等要求")

    pdf.add_paragraph(
        "有关详细的发行说明，请访问："
        "<a href='http://www.reportlab.com/software/documentation/relnotes/30/'>"
        "http://www.reportlab.com/software/documentation/relnotes/30/</a>"
    )


def main(filename):
    fonts_dir = os.path.join(
        os.path.dirname(os.path.abspath(BASE_DIR)), 'fonts'
    )
    pdf = PDF(filename, fonts_dir=fonts_dir)

    chapter1(pdf)
    pdf.build_2_save()


if __name__ == '__main__':

    setup_logging()
    main('test.pdf')
