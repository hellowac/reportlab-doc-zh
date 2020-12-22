# Copyright ReportLab Europe Ltd. 2000-2017
# see license.txt for license details
# history https://hg.reportlab.com/hg-public/reportlab/log/tip/docs/userguide
# /ch3_pdffeatures.py
from reportlab.lib import colors
from reportlab.platypus.tables import Table, TableStyle
from utils import (
    heading1,
    cn_heading1,
    heading2,
    cn_heading2,
    heading3,
    caption,
    cn_caption,
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
)
from utils import examples


# heading1("Exposing PDF Special Capabilities")
cn_heading1("揭示PDF的特殊能力")

disc(
    """PDF provides a number of features to make electronic
    document viewing more efficient and comfortable, and
    our library exposes a number of these."""
)
cn_disc("PDF提供了许多功能，使电子文档的浏览更加高效和舒适，我们的类库就公开了其中的一些功能。")

# heading2("Forms")
cn_heading2("表单")

disc(
    """The Form feature lets you create a block of graphics and text
once near the start of a PDF file, and then simply refer to it on
subsequent pages.  If you are dealing with a run of 5000 repetitive
business forms - for example, one-page invoices or payslips - you
only need to store the backdrop once and simply draw the changing
text on each page.  Used correctly, forms can dramatically cut
file size and production time, and apparently even speed things
up on the printer.
    """
)
cn_disc('表单功能让您可以在PDF文件的开头附近创建一个图形和文本块，'
        '然后在随后的页面上简单地引用它。 '
        '如果您要处理5000个重复的商业表格'
        '--例如，一页的发票或工资单--您只需要存储一次背景，并简单地在每一页上绘制变化的文本。 '
        '正确使用表格，可以大大减少文件大小和生产时间，甚至可以加快打印机的速度。')

disc(
    """Forms do not need to refer to a whole page; anything which might be 
repeated often should be placed in a form."""
)
cn_disc('表格不需要引用整页的内容，凡是可能经常重复的内容都应该放在表格中。')

disc(
    """The example below shows the basic sequence used.  A real
program would probably define the forms up front and refer to
them from another location."""
)
cn_disc('下面的例子显示了使用的基本序列。 一个真正的程序可能会在前面定义表格，并从另一个位置引用它们。')

eg(examples.testforms)

# heading2("Links and Destinations")
cn_heading2("链接和目的地")

disc(
    """PDF supports internal hyperlinks.  There is a very wide
range of link types, destination types and events which
can be triggered by a click.  At the moment we just
support the basic ability to jump from one part of a document
to another, and to control the zoom level of the window after
the jump.  The ^bookmarkPage^ method defines a destination that
is the endpoint of a jump."""
)
cn_disc('PDF支持内部超链接。 '
        '有一个非常广泛的链接类型，目标类型和事件可以通过点击来触发。 '
        '目前，我们只支持从文档的一个部分跳转到另一个部分的基本功能，以及控制跳转后窗口的缩放级别。 '
        '^bookmarkPage^方法定义了一个目标，它是跳转的终点。')

# todo("code example here...")

eg(
    """
    canvas.bookmarkPage(name,
                        fit="Fit",
                        left=None,
                        top=None,
                        bottom=None,
                        right=None,
                        zoom=None
                        )
"""
)
disc(
    """
By default the $bookmarkPage$ method defines the page itself as the
destination. After jumping to an endpoint defined by bookmarkPage,
the PDF browser will display the whole page, scaling it to fit the
screen:"""
)
cn_disc('默认情况下，$bookmarkPage$方法将页面本身定义为目标。'
        '在跳转到由^bookmarkPage^定义的端点后，PDF浏览器将显示整个页面，并将其缩放以适应屏幕。')

eg("""canvas.bookmarkPage(name)""")

disc(
    """The $bookmarkPage$ method can be instructed to display the
page in a number of different ways by providing a $fit$
parameter."""
)
cn_disc('通过提供一个$fit$参数，$bookmarkPage$方法可以被指示以多种不同的方式显示页面。')

eg("")

t = Table(
    [
        ['fit', 'Parameters Required', 'Meaning'],
        ['Fit', None, 'Entire page fits in window (the default)'],
        ['FitH', 'top', 'Top coord at top of window, width scaled to fit'],
        ['FitV', 'left', 'Left coord at left of window, height scaled to fit'],
        [
            'FitR',
            'left bottom right top',
            'Scale window to fit the specified rectangle',
        ],
        [
            'XYZ',
            'left top zoom',
            'Fine grained control. If you omit a parameter\nthe PDF browser '
            'interprets it as "leave as is"',
        ],
    ]
)
t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 1), 'Times-Bold', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
# getStory().append(t)

cn_t = Table([
    ['fit', '必传参数', '描述'],
    ['Fit', None, '自适应窗口 (默认)'],
    ['FitH', 'top', '坐标在窗口上方, 自适应宽度'],
    ['FitV', 'left', '坐标在窗口左边, 自适应高度'],
    [
        'FitR',
        'left bottom right top',
        '缩放窗口以适应指定的矩形',
    ],
    [
        'XYZ',
        'left top zoom',
        '细致的控制。如果您省略了一个参数，PDF浏览器会将其解释为 "保持原样"。',
    ],
])
cn_t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, -1), 'STSong-Light', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
getStory().append(cn_t)

# caption(
#     """Table <seq template="%(Chapter)s-%(Table+)s"/> - Required attributes
#     for different fit types"""
# )
cn_caption('表 <seq template="%(Chapter)s-%(Table+)s"/> - 配合不同类型所需的属性')

disc(
    """
Note : $fit$ settings are case-sensitive so $fit="FIT"$ is invalid
"""
)
cn_disc('注意：$fit$的设置是区分大小写的，所以$fit="FIT"$是无效的。')

disc(
    """
Sometimes you want the destination of a jump to be some part of a page.
The $FitR$ fit allows you to identify a particular rectangle, scaling
the area to fit the entire page.
"""
)
cn_disc('有时你希望跳转的目标是一个页面的某个部分。'
        '$FitR$ fit允许你确定一个特定的矩形，缩放区域以适合整个页面。')

disc(
    """
To set the display to a particular x and y coordinate of the page and to
control the zoom directly use fit="XYZ".
"""
)
cn_disc('要将显示设置为页面的特定x和y坐标，并直接使用fit="XYZ "控制缩放。')

eg(
    """
canvas.bookmarkPage('my_bookmark',fit="XYZ",left=0,top=200)
"""
)

disc(
    """
This destination is at the leftmost of the page with the top of the screen
at position 200. Because $zoom$ was not set the zoom remains at whatever the
user had it set to.
"""
)
cn_disc('这个目标位于页面的最左边，屏幕顶部的位置是200。'
        '因为没有设置$zoom$，所以无论用户设置成什么样子，缩放都会保持在这个位置。')

eg(
    """
canvas.bookmarkPage('my_bookmark',fit="XYZ",left=0,top=200,zoom=2)
"""
)

disc("""This time zoom is set to expand the page 2X its normal size.""")
cn_disc('这次的缩放设置为将页面扩大2倍其正常大小。')

disc(
    """
Note  : Both $XYZ$ and $FitR$ fit types require that their positional parameters
($top, bottom, left, right$) be specified in terms of the default user space.
They ignore any geometric transform in effect in the canvas graphic state.
"""
)
cn_disc('注意：$XYZ$和$FitR$的拟合类型都需要用默认的用户空间来指定它们的位置参数($top, bottom, left, right$)。'
        '它们会忽略画布图形状态下的任何几何变换。')

pencilnote()

disc(
    """
<i>Note:</i> Two previous bookmark methods are supported but deprecated now
that bookmarkPage is so general.  These are $bookmarkHorizontalAbsolute$
and $bookmarkHorizontal$.
"""
)
cn_disc('<i>注意：</i>之前有两个书签方法是支持的，但由于bookmarkPage的通用性，现在已经废弃了。 '
        '这两个方法是$bookmarkHorizontalAbsolute$和$bookmarkHorizontal$。')

# heading3("Defining internal links")
cn_heading3("定义内部链接")

eg(
    """
 canvas.linkAbsolute(contents, destinationname, Rect=None, addtopage=1, 
 name=None, 
 thickness=0, color=None, dashArray=None, **kw)
 """
)

disc(
    """
The $linkAbsolute$ method defines a starting point for a jump.  When the 
user is browsing the generated document using a dynamic viewer (such as 
Acrobat Reader) when the mouse is clicked when the pointer is within the 
rectangle specified by $Rect$ the viewer will jump to the endpoint associated 
with 
$destinationname$. As in the case with $bookmarkHorizontalAbsolute$ the 
rectangle $Rect$ must be specified in terms of the default user space.  The 
$contents$ parameter specifies a chunk of text which displays in the viewer 
if the user left-clicks on the region.
"""
)
cn_disc('$linkAbsolute$方法定义了一个跳跃的起点。 '
        '当用户使用动态查看器(如Acrobat Reader)浏览生成的文档时，当鼠标在$Rect$指定的矩形内点击时，'
        '查看器将跳转到与$destinationname$相关联的端点。'
        '如同$bookmarkHorizontalAbsolute$一样，矩形$Rect$必须用默认的用户空间来指定。 '
        '参数$contents$指定了当用户左键点击该区域时在查看器中显示的文本块。')

disc(
    """
The rectangle $Rect$ must be specified in terms of a tuple ^(x1,y1,x2, 
y2)^ identifying the lower left and upper right points of the rectangle in 
default user space.
"""
)
cn_disc('矩形$Rect$必须用元组^(x1,y1,x2,y2)^来指定，以确定在默认用户空间中矩形的左下角和右上角。')

disc('For example the code')
cn_disc('示例代码')

eg(
    """
    canvas.bookmarkPage("Meaning_of_life")
"""
)

disc(
    """
defines a location as the whole of the current page with the identifier
$Meaning_of_life$.  To create a rectangular link to it while drawing a possibly
different page, we would use this code:
"""
)
cn_disc('定义了一个位置，作为当前页面的整个标识符$Meaning_of_life$。 '
        '为了在绘制一个可能不同的页面时创建一个矩形链接到它，我们将使用以下代码。')

eg(
    """
 canvas.linkAbsolute("Find the Meaning of Life", "Meaning_of_life",
                     (inch, inch, 6*inch, 2*inch))
"""
)

disc(
    """
By default during interactive viewing a rectangle appears around the
link. Use the keyword argument $Border='[0 0 0]'$ to suppress the visible 
rectangle around the during viewing link. For example
"""
)
cn_disc("默认情况下，在交互式浏览时，链接周围会出现一个矩形。"
        "使用关键字参数$Border='[0 0 0]'$来抑制查看链接时周围可见的矩形。"
        "例如")

eg(
    """
 canvas.linkAbsolute("Meaning of Life", "Meaning_of_life",
                     (inch, inch, 6*inch, 2*inch), Border='[0 0 0]')
"""
)

disc(
    """The $thickness$, $color$ and $dashArray$ arguments may be used 
    alternately
to specify a border if no Border argument is specified.
If Border is specified it must be either a string representation of a PDF
array or a $PDFArray$ (see the pdfdoc module). The $color$ argument (which 
should be a $Color$ instance) is equivalent to a keyword argument $C$ which 
should resolve to a PDF color definition (Normally a three entry PDF array).
"""
)
cn_disc('如果没有指定Border参数，$thickness$、$color$和$dashArray$参数可以交替使用来指定边框。'
        '如果指定了Border参数，它必须是一个PDF数组的字符串表示，'
        '或者是一个$PDFArray$(参见pdfdoc模块)。'
        '$color$参数(应该是一个$Color$实例)相当于一个关键字参数$C$，'
        '它应该解析为一个PDF颜色定义(通常是一个三条PDF数组)。')

disc(
    """The $canvas.linkRect$ method is similar in intent to the 
$linkAbsolute$ method, but has an extra argument $relative=1$ so is 
intended to obey the local user space transformation."""
)
cn_disc('$canvas.linkRect$方法的意图与$linkAbsolute$方法类似，'
        '但多了一个参数$relative=1$，所以打算服从本地用户空间转换。')

# heading2("Outline Trees")
cn_heading2("大纲")

disc(
    """Acrobat Reader has a navigation page which can hold a
document outline; it should normally be visible when you
open this guide.  We provide some simple methods to add
outline entries.  Typically, a program to make a document
(such as this user guide) will call the method
$canvas.addOutlineEntry(^self, title, key, level=0,
closed=None^)$ as it reaches each heading in the document.
    """
)
cn_disc('Acrobat Reader有一个导航页，它可以容纳一个文档大纲；'
        '当您打开本指南时，它通常应该是可见的。 '
        '我们提供一些简单的方法来添加大纲条目。 '
        '通常情况下，一个制作文档的程序（如本用户指南）在到达文档中的每个标题时，'
        '会调用方法$canvas.addOutlineEntry(^self, title, key, level=0, '
        'closed=None^)$。')

disc(
    """^title^ is the caption which will be displayed in
the left pane.  The ^key^ must be a string which is unique within the 
document and which names a bookmark, as with the hyperlinks.  The ^level^ is 
zero - the uppermost level - unless otherwise specified, and it is an error 
to go down more than one level at a time (for example to follow a level 0 
heading by a level 2 heading).  Finally, the ^closed^ argument specifies
whether the node in the outline pane is closed or opened by default."""
)
cn_disc('^title^是将显示在左侧窗格的标题。 '
        '^key^必须是一个字符串，它在文档中是唯一的，并且和超链接一样，可以命名一个书签。 '
        '除非另有说明，否则^level^是0'
        '--最上层，而且一次下行超过一层是错误的(例如，在0层标题后加上2层标题)。 '
        '最后，^closed^参数指定大纲窗格中的节点是默认关闭还是打开。')

disc(
    """The snippet below is taken from the document template
that formats this user guide.  A central processor looks
at each paragraph in turn, and makes a new outline entry
when a new chapter occurs, taking the chapter heading text
as the caption text.  The key is obtained from the
chapter number (not shown here), so Chapter 2 has the
key 'ch2'.  The bookmark to which the
outline entry points aims at the whole page, but it could
as easily have been an individual paragraph.
    """
)
cn_disc('下面的片段来自于格式化本用户指南的文档模板。 '
        '中央处理器依次查看每个段落，当出现新的章节时，'
        '就会做出一个新的大纲条目，将章节标题文本作为标题文本。 '
        '键是从章节号中获得的（这里没有显示），所以第2章的键为 "ch2"。 '
        '大纲入口指向的书签是针对整页的，但它也可以很容易地成为一个单独的段落。')

eg(
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

# heading2("Page Transition Effects")
cn_heading2("页面过渡效果")

eg(
    """
 canvas.setPageTransition(self, effectname=None, duration=1,
                        direction=0,dimension='H',motion='I')
                        """
)

disc(
    """
The $setPageTransition$ method specifies how one page will be replaced with
the next.  By setting the page transition effect to "dissolve" for example
the current page will appear to melt away when it is replaced by the next
page during interactive viewing.  These effects are useful in spicing up
slide presentations, among other places. Please see the reference manual for 
more detail on how to use this method.
"""
)
cn_disc('$setPageTransition$方法指定了一个页面如何被下一个页面替换。 '
        '例如，通过将页面转换效果设置为 "溶解"，当当前页面在交互式浏览过程中被下一个页面所取代时，它将显示为融化。 '
        '这些效果在美化幻灯片演示等地方很有用。关于如何使用此方法，请参阅参考手册。')

# heading2("Internal File Annotations")
cn_heading2("内部文件注释")

eg(
    """
 canvas.setAuthor(name)
 canvas.setTitle(title)
 canvas.setSubject(subj)
 """
)

disc(
    """
These methods have no automatically seen visible effect on the document.
They add internal annotations to the document.  These annotations can be
viewed using the "Document Info" menu item of the browser and they also can
be used as a simple standard way of providing basic information about the
document to archiving software which need not parse the entire
file.  To find the annotations view the $*.pdf$ output file using a standard
text editor (such as $notepad$ on MS/Windows or $vi$ or $emacs$ on unix) and 
look for the string $/Author$ in the file contents.
"""
)
cn_disc('这些方法对文档没有自动可见的效果。'
        '它们向文件添加内部注释。 '
        '这些注释可以使用浏览器的 "文档信息 "菜单项来查看，'
        '它们也可以作为一种简单的标准方式，向不需要解析整个文件的归档软件提供有关文件的基本信息。 '
        '要找到注释，请使用标准文本编辑器'
        '（如MS/Windows上的$notepad$或unix上的$vi$或$emacs$）'
        '查看$*.pdf$输出文件，'
        '并在文件内容中查找字符串$/Author$。')

eg(examples.testannotations)

disc(
    """
If you want the subject, title, and author to automatically display
in the document when viewed and printed you must paint them onto the
document like any other text.
"""
)
cn_disc('如果您想让主题、标题和作者在查看和打印时自动显示在文档中，您必须像其他文本一样将它们绘制到文档中。')

# illust(examples.annotations, "Setting document internal annotations")
cn_illust(examples.annotations, "设置文档内部注释")

# heading2("Encryption")
cn_heading2("加密")

# heading3("About encrypting PDF files")
cn_heading3("关于加密PDF文件")

disc(
    """
Adobe's PDF standard allows you to do three related things to a PDF file when 
you encrypt it:
"""
)
cn_disc('Adobe的PDF标准允许你在对一个PDF文件进行加密时做三件相关的事情。')

bullet(
    """Apply password protection to it, so a user must supply a valid 
    password before being able to read it,
"""
)
cn_bullet('对其进行密码保护，所以用户必须提供有效的密码才能够读取它。')

bullet(
    """Encrypt the contents of the file to make it useless until it is 
    decrypted, and
"""
)
cn_bullet('对文件的内容进行加密，使其在解密前毫无用处，并对文件进行加密。')

bullet(
    """Control whether the user can print, copy and paste or modify the 
    document while viewing it.
"""
)
cn_bullet('控制用户在查看文档时是否可以打印、复制、粘贴或修改文档。')

disc(
    """
The PDF security handler allows two different passwords to be specified for a 
document:
"""
)
cn_disc('PDF安全处理程序允许为一个文档指定两个不同的密码。')

bullet(
    """The 'owner' password (aka the 'security password' or 'master password')
"""
)
cn_bullet('所有者 "密码"（也就是 "安全密码 "或 "主密码"）。')

bullet(
    """The 'user' password (aka the 'open password')
"""
)
cn_bullet('用户 "密码"（也就是 "打开密码"）。')

disc(
    """
When a user supplies either one of these passwords, the PDF file will be 
opened, decrypted and displayed on screen.
"""
)
cn_disc('当用户提供其中一个密码时，PDF文件将被打开、解密并显示在屏幕上。')

disc(
    """
If the owner password is supplied, then the file is opened with full control 
- you can do anything to it, including changing the security settings and 
passwords, or re-encrypting it with a new password.
"""
)
cn_disc('如果提供了所有者密码，那么文件的打开就有了完全的控制权'
        '--你可以对它做任何事情，包括改变安全设置和密码，或者用新密码重新加密。')

disc(
    """
If the user password was the one that was supplied, you open it up in a more 
restricted mode. The restrictions were put in
place when the file was encrypted, and will either allow or deny the user 
permission to do the following:
"""
)
cn_disc('如果用户密码是提供的密码，你就在一个更受限制的模式下打开它。'
        '这些限制是在文件加密时设置的，将允许或拒绝用户进行以下操作的权限。')

bullet("Modifying the document's contents")
bullet("Copying text and graphics from the document")
bullet("Adding or modifying text annotations and interactive form fields")
bullet("Printing the document")

cn_bullet('修改文件的内容')
cn_bullet('从文档中复制文本和图形')
cn_bullet('添加或修改文本注释和交互式表格字段。')
cn_bullet('打印文件')

disc(
    """
Note that all password protected PDF files are encrypted, but not all 
encrypted PDFs are password protected. If a document's user password is an 
empty string, there will be no prompt for the password when the file is
opened. If you only secure a document with the owner password, there will 
also not be a prompt for the password when you open the file. If the owner 
and user passwords are set to the same string when encrypting
the PDF file, the document will always open with the user access privileges. 
This means that it is possible to create a file which, for example, 
is impossible for anyone to print out, even the person who created it.
"""
)
cn_disc('请注意，所有受密码保护的PDF文件都是加密的，但并不是所有加密的PDF都受密码保护。'
        '如果一个文件的用户密码是一个空字符串，当打开文件时将不会有密码提示。'
        '如果只用所有者密码来保护文档，那么打开文件时也不会有密码提示。'
        '如果在对PDF文件进行加密时，将所有者和用户密码设置为同一字符串，则该文件将始终以用户访问权限打开。'
        '这就意味着，可以创建一个文件，比如说，任何人都不可能打印出来，即使是创建该文件的人。')

t = Table(
    [
        ['Owner Password \nset?', 'User Password \nset?', 'Result'],
        [
            'Y',
            '-',
            'No password required when opening file. \nRestrictions apply to '
            'everyone.',
        ],
        [
            '-',
            'Y',
            'User password required when opening file. \nRestrictions apply '
            'to everyone.',
        ],
        [
            'Y',
            'Y',
            'A password required when opening file. \nRestrictions apply only '
            'if user password supplied.',
        ],
    ],
    [90, 90, 260],
)
t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 0), 'Times-Bold', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
# getStory().append(t)

cn_t = Table(
    [
        ['所有者密码\n已设置?', '用户密码\n已设置?', '结果'],
        [
            '是',
            '-',
            '打开文件时无需密码。适用于所有人。',
        ],
        [
            '-',
            '是',
            '打开文件时需要用户密码。适用于所有人。',
        ],
        [
            '是',
            '是',
            '打开文件时需要一个密码。\n只有在提供用户密码的情况下才有限制。',
        ],
    ],
    [90, 90, 260],
)
cn_t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, -1), 'STSong-Light', 10, 12),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
getStory().append(cn_t)

disc(
    """
When a PDF file is encrypted, encryption is applied to all the strings and 
streams in the file. This prevents people who don't have the password from 
simply removing the password from the PDF file to gain access to it - it 
renders the file useless unless you actually have the password.
"""
)
cn_disc('当一个PDF文件被加密时，加密将应用于文件中的所有字符串和流。'
        '这可以防止没有密码的人简单地从PDF文件中删除密码以获得访问权'
        ' - 它使文件无用，除非你真的有密码。')

disc(
    """
PDF's standard encryption methods use the
MD5 message digest algorithm (as described in RFC 1321, The MD5 
Message-Digest Algorithm) and an
encryption algorithm known as RC4. RC4 is a symmetric stream cipher - the 
same algorithm is used both for
encryption and decryption, and the algorithm does not change the length of 
the data.
"""
)
cn_disc('PDF 的标准加密方法使用 MD5 消息摘要算法'
        '（如 RFC 1321，MD5 消息摘要算法中所述）和一种称为 RC4 的加密算法。'
        'RC4是一种对称流加密算法'
        '--加密和解密都使用相同的算法，而且该算法不会改变数据的长度。')

heading3("How To Use Encryption")
cn_heading3("如何使用加密技术")

disc('Documents can be encrypted by passing an argument to the canvas object.')
cn_disc('文档可以通过向画布对象传递一个参数来加密。')

disc(
    'If the argument is a string object, it is used as the User password to '
    'the PDF.')
cn_disc('如果参数是一个字符串对象，它被用作PDF的用户密码。')

disc("""
The argument can also be an instance of the class 
$reportlab.lib.pdfencrypt.StandardEncryption$,
which allows more finegrained control over encryption settings.
""")
cn_disc('参数也可以是$reportlab.lib.pdfencrypt.StandardEncryption$类的实例，'
        '它允许对加密设置进行更精细的控制。')

disc('The $StandardEncryption$ constructor takes the following arguments:')
cn_disc('$StandardEncryption$构造函数接受以下参数。')

eg("""
def __init__(self, userPassword,
    ownerPassword=None,
    canPrint=1,
    canModify=1,
    canCopy=1,
    canAnnotate=1,
    strength=40):
""")

disc(
"""
The $userPassword$ and $ownerPassword$ parameters set the relevant 
password on the encrypted PDF.
"""
)
cn_disc('$userPassword$和$ownerPassword$参数在加密的PDF上设置了相关密码。')

disc(
"""
The boolean flags $canPrint$, $canModify$, $canCopy$, $canAnnotate$ 
determine wether a user can perform the corresponding actions on the PDF when only a user password has been supplied.
"""
)
cn_disc('布尔标志$canPrint$, $canModify$, $canCopy$, $canAnnotate$决定了'
        '当只有用户密码被提供时，用户是否可以在PDF上执行相应的操作。')

disc('If the user supplies the owner password while opening the PDF, '
     'all actions can be performed regardless of the flags.')
cn_disc('如果用户在打开PDF时提供了所有者密码，则无论标志如何，所有的操作都可以执行。')

# heading3("Example")
cn_heading3("示例")

disc(
"""
To create a document named hello.pdf with a user password of 'rptlab' on 
which printing is not allowed,
use the following code:
"""
)
cn_disc("要创建一个名为hello.pdf的文档，用户密码为'rptlab'，不允许打印，可以用以下代码。")

eg(
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

# heading2("Interactive Forms")
cn_heading2("交互式表单")

# heading3("Overview of Interactive Forms")
cn_heading3("交互式表格概述")

disc(
    """The PDF standard allows for various kinds of interactive elements,
the ReportLab toolkit currently supports only a fraction of the possibilities 
and should be considered a work in progress.At present we allow choices with
<i>checkbox</i>, <i>radio</i>, <i>choice</i> &amp; <i>listbox</i> widgets; 
text values can be entered with a <i>textfield</i> widget. All the widgets 
are created by calling methods on the <i>canvas.acroform</i> property."""
)
cn_disc('PDF标准允许各种交互式元素，'
        'ReportLab工具包目前只支持一小部分的可能性，应该被认为是一项正在进行中的工作。'
        '目前我们允许使用<i>checkbox</i>, <i>radio</i>, '
        '<i>choice</i> &amp; <i>listbox</i> widget进行选择；'
        '文本值可以使用<i>textfield</i> widget进行输入。'
        '所有的widget都是通过调用<i>canvas.acroform</i>属性上的方法创建的。')

# heading3("Example")
cn_heading3("示例")

disc(
    "This shows the basic mechanism of creating an interactive element on the current page."
)
cn_disc('这显示了在当前页面上创建交互式元素的基本机制。')

eg(
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
alStyle = TableStyle(
    [
        ('SPAN', (0, 0), (-1, 0)),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 10, 12),
        ('FONT', (0, 1), (-1, 1), 'Helvetica-BoldOblique', 8, 9.6),
        ('FONT', (0, 2), (0, -1), 'Helvetica-Bold', 7, 8.4),
        ('FONT', (1, 2), (1, -1), 'Helvetica', 7, 8.4),
        ('FONT', (2, 2), (2, -1), 'Helvetica-Oblique', 7, 8.4),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('ALIGN', (1, 1), (1, 1), 'CENTER'),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ]
)
cn_alStyle = TableStyle(
    [
        ('SPAN', (0, 0), (-1, 0)),
        ('FONT', (0, 0), (-1, 0), 'STSong-Light', 10, 12),
        ('FONT', (0, 1), (-1, 1), 'STSong-Light', 8, 9.6),
        ('FONT', (0, 2), (0, -1), 'STSong-Light', 7, 8.4),
        ('FONT', (1, 2), (1, -1), 'STSong-Light', 7, 8.4),
        ('FONT', (2, 2), (2, -1), 'STSong-Light', 7, 8.4),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('ALIGN', (1, 1), (1, 1), 'CENTER'),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ]
)

disc(
    """<b>NB</b> note that the <i>acroform</i> canvas property is created 
automatically on demand and that there is only one form allowd in a document."""
)
cn_disc('<b>NB</b>请注意，<i>acroform</i>画布属性是根据需求自动创建的，而且一个文档中只允许有一个表单。')

# heading3("Checkbox Usage")
cn_heading3("复选框用法")

disc(
    """The <i>canvas.acroform.checkbox</i> method creates a <i>checkbox</i> 
widget on the current page. The value of the checkbox is either 
<b>YES</b> or <b>OFF</b>. The arguments are"""
)
cn_disc('<i>canvas.acroform.checkbox</i>方法在当前页面上创建了一个<i>checkbox</i>小部件。'
        '复选框的值是<b>YES</b>或<b>OFF</b>。参数为')

t = Table(
    [
        ['canvas.acroform.checkbox parameters', '', ''],
        ['Parameter', 'Meaning', 'Default'],
        ["name", "the parameter's name", "None"],
        [
            "x",
            "the horizontal position on the page (absolute coordinates)",
            "0",
        ],
        ["y", "the vertical position on the page (absolute coordinates)", "0"],
        ["size", "The outline dimensions size x size", "20"],
        ["checked", "if True the checkbox is initially checked", "False"],
        ["buttonStyle", "the checkbox style (see below)", "'check'"],
        ["shape", "The outline of the widget (see below)", "'square'"],
        ["fillColor", "colour to be used to fill the widget", "None"],
        ["textColor", "the colour of the symbol or text", "None"],
        ["borderWidth", "as it says", "1"],
        ["borderColor", "the widget's border colour", "None"],
        ["borderStyle", "The border style name", "'solid'"],
        [
            "tooltip",
            "The text to display when hovering over the widget",
            "None",
        ],
        [
            "annotationFlags",
            "blank separated string of annotation flags",
            "'print'",
        ],
        ["fieldFlags", "Blank separated field flags (see below)", "'required'"],
        [
            "forceBorder",
            "when true a border force a border to be drawn",
            "False",
        ],
        ["relative", "if true obey the current canvas transform", "False"],
        [
            "dashLen ",
            "the dashline to be used if the borderStyle=='dashed'",
            "3",
        ],
    ],
    [90, 260, 90],
    style=alStyle,
    repeatRows=2,
)
# getStory().append(t)

cn_t = Table(
    [
        ['canvas.acroform.checkbox 参数列表', '', ''],
        ['参数名', '描述', '默认值'],
        ["name", "表单参数名", "None"],
        [
            "x",
            "在页面上的水平位置(绝对坐标)",
            "0",
        ],
        ["y", "在页面上的垂直位置(绝对坐标)", "0"],
        ["size", "轮廓尺寸：size x size", "20"],
        ["checked", "如果为真，则该复选框被初始选中", "False"],
        ["buttonStyle", "如果为真，则该复选框最初被选中，复选框样式（见下文）。", "'check'"],
        ["shape", "小组件的轮廓（见下文）。", "'square'"],
        ["fillColor", "用来填充小组件的颜色", "None"],
        ["textColor", "符号的颜色", "None"],
        ["borderWidth", "边框宽度", "1"],
        ["borderColor", "小组件的边框颜色", "None"],
        ["borderStyle", "边框样式名称", "'solid'"],
        [
            "tooltip",
            "悬停在小组件上时要显示的文本。",
            "None",
        ],
        [
            "annotationFlags",
            "空白分隔的注解标志字符串",
            "'print'",
        ],
        ["fieldFlags", "空白分隔的字段标志（见下文）。", "'required'"],
        [
            "forceBorder",
            "当真的时候会强行画边框",
            "False",
        ],
        ["relative", "如果为真，服从当前画布的变换", "False"],
        [
            "dashLen ",
            "如果 borderStyle=='dashed' ，要使用的折线。",
            "3",
        ],
    ],
    [90, 260, 90],
    style=cn_alStyle,
    repeatRows=2,
)
getStory().append(cn_t)

heading3("Radio Usage")
cn_heading3("单选框使用方法")

disc(
"""The <i>canvas.acroform.radio</i> method creates a <i>radio</i> widget 
on the current page. The value of the radio is the value of the radio 
group's selected value or <b>OFF</b> if none are selected. The arguments are"""
)
cn_disc('<i>canvas.acroform.radio</i>方法在当前页面上创建一个<i>radio</i>小组件。'
        'radio的值是radio组选择的值，如果没有选择，则是<b>OFF</b>。参数是')

t = Table(
    [
        ['canvas.acroform.radio parameters', '', ''],
        ['Parameter', 'Meaning', 'Default'],
        ["name", "the radio's group (ie parameter) name", "None"],
        ["value", "the radio's group name", "None"],
        [
            "x",
            "the horizontal position on the page (absolute coordinates)",
            "0",
        ],
        ["y", "the vertical position on the page (absolute coordinates)", "0"],
        ["size", "The outline dimensions size x size", "20"],
        [
            "selected",
            "if True this radio is the selected one in its group",
            "False",
        ],
        ["buttonStyle", "the checkbox style (see below)", "'check'"],
        ["shape", "The outline of the widget (see below)", "'square'"],
        ["fillColor", "colour to be used to fill the widget", "None"],
        ["textColor", "the colour of the symbol or text", "None"],
        ["borderWidth", "as it says", "1"],
        ["borderColor", "the widget's border colour", "None"],
        ["borderStyle", "The border style name", "'solid'"],
        [
            "tooltip",
            "The text to display when hovering over the widget",
            "None",
        ],
        [
            "annotationFlags",
            "blank separated string of annotation flags",
            "'print'",
        ],
        [
            "fieldFlags",
            "Blank separated field flags (see below)",
            "'noToggleToOff required radio'",
        ],
        [
            "forceBorder",
            "when true a border force a border to be drawn",
            "False",
        ],
        ["relative", "if true obey the current canvas transform", "False"],
        [
            "dashLen ",
            "the dashline to be used if the borderStyle=='dashed'",
            "3",
        ],
    ],
    [90, 260, 90],
    style=alStyle,
    repeatRows=2,
)
# getStory().append(t)
cn_t = Table(
    [
        ['canvas.acroform.radio 参数列表', '', ''],
        ['参数名', '描述', '默认值'],
        ["name", "单选框组的名称(该参数)", "None"],
        ["value", "单选框组的名称", "None"],
        [
            "x",
            "在页面上的水平位置(绝对坐标)",
            "0",
        ],
        ["y", "在页面上的垂直位置(绝对坐标)", "0"],
        ["size", "轮廓尺寸，size x size", "20"],
        [
            "selected",
            "if True this radio is the selected one in its group",
            "False",
        ],
        ["buttonStyle", "如果为 'true'，则该单选机在其组中被选中。", "'check'"],
        ["shape", "小组件的轮廓（见下文）。", "'square'"],
        ["fillColor", "用来填充小组件的颜色", "None"],
        ["textColor", "符号的颜色", "None"],
        ["borderWidth", "边框宽度", "1"],
        ["borderColor", "边框颜色", "None"],
        ["borderStyle", "边框样式名称", "'solid'"],
        [
            "tooltip",
            "悬停在小组件上时要显示的文本。",
            "None",
        ],
        [
            "annotationFlags",
            "空白分隔的注解标志字符串",
            "'print'",
        ],
        [
            "fieldFlags",
            "空白分隔的字段标志（见下文）。",
            "'noToggleToOff required radio'",
        ],
        [
            "forceBorder",
            "当真的时候会强行画边框",
            "False",
        ],
        ["relative", "if true obey the current canvas transform", "False"],
        [
            "dashLen ",
            "如果borderStyle=='dashed'，要使用的折线。",
            "3",
        ],
    ],
    [90, 260, 90],
    style=cn_alStyle,
    repeatRows=2,
)
getStory().append(cn_t)

# heading3("Listbox Usage")
cn_heading3("列表框用法")

disc(
    """The <i>canvas.acroform.listbox</i> method creates a <i>listbox</i> 
widget on the current page. The listbox contains a list of options one or 
more of which (depending on fieldFlags) may be selected.
"""
)
cn_disc('<i>canvas.acroform.listbox</i>方法在当前页面上创建了一个<i>listbox</i>小组件。'
        'listbox包含一个选项列表，其中一个或多个选项（取决于fieldFlags）可以被选中。')

t = Table(
    [
        ['canvas.acroform.listbox parameters', '', ''],
        ['Parameter', 'Meaning', 'Default'],
        ["name", "the radio's group (ie parameter) name", "None"],
        ["options", "List or tuple of avaiable options", "[]"],
        ["value", "Singleton or list of strings of selected options", "[]"],
        [
            "x",
            "the horizontal position on the page (absolute coordinates)",
            "0",
        ],
        ["y", "the vertical position on the page (absolute coordinates)", "0"],
        ["width", "The widget width", "120"],
        ["height", "The widget height", "36"],
        ["fontName", "The name of the type 1 font to be used", "'Helvetica'"],
        ["fontSize", "The size of font to be used", "12"],
        ["fillColor", "colour to be used to fill the widget", "None"],
        ["textColor", "the colour of the symbol or text", "None"],
        ["borderWidth", "as it says", "1"],
        ["borderColor", "the widget's border colour", "None"],
        ["borderStyle", "The border style name", "'solid'"],
        [
            "tooltip",
            "The text to display when hovering over the widget",
            "None",
        ],
        [
            "annotationFlags",
            "blank separated string of annotation flags",
            "'print'",
        ],
        ["fieldFlags", "Blank separated field flags (see below)", "''"],
        [
            "forceBorder",
            "when true a border force a border to be drawn",
            "False",
        ],
        ["relative", "if true obey the current canvas transform", "False"],
        [
            "dashLen ",
            "the dashline to be used if the borderStyle=='dashed'",
            "3",
        ],
    ],
    [90, 260, 90],
    style=alStyle,
    repeatRows=2,
)
# getStory().append(t)
cn_t = Table(
    [
        ['canvas.acroform.listbox 参数列表', '', ''],
        ['参数', '描述', '默认值'],
        ["name", "组名", "None"],
        ["options", "可用选项的列表或元组", "[]"],
        ["value", "单个或选定选项的字符串列表。", "[]"],
        [
            "x",
            "在页面上的水平位置(绝对坐标)",
            "0",
        ],
        ["y", "在页面上的垂直位置(绝对坐标)", "0"],
        ["width", "小组件宽度", "120"],
        ["height", "小组件高度", "36"],
        ["fontName", "要使用的第1种字体的名称。", "'Helvetica'"],
        ["fontSize", "要使用的字体大小", "12"],
        ["fillColor", "用来填充小组件的颜色", "None"],
        ["textColor", "符号的颜色", "None"],
        ["borderWidth", "边框宽度", "1"],
        ["borderColor", "边框颜色", "None"],
        ["borderStyle", "边框样式", "'solid'"],
        [
            "tooltip",
            "悬停在小组件上时要显示的文本。",
            "None",
        ],
        [
            "annotationFlags",
            "空白分隔的注解标志字符串",
            "'print'",
        ],
        ["fieldFlags", "空白分隔的字段标志（见下文）。", "''"],
        [
            "forceBorder",
            "当真的时候会强行画边框",
            "False",
        ],
        ["relative", "如果为真，服从当前画布的变换", "False"],
        [
            "dashLen ",
            "如果borderStyle=='dashed'，要使用的折线。",
            "3",
        ],
    ],
    [90, 260, 90],
    style=cn_alStyle,
    repeatRows=2,
)
getStory().append(cn_t)

# heading3("Choice Usage")
cn_heading3("下拉菜单的使用")

disc(
    """The <i>canvas.acroform.choice</i> method creates a <i>dropdown</i> 
    widget on the current page. The dropdown contains a
list of options one or more of which (depending on fieldFlags) may be 
selected. If you add <i>edit</i> to the <i>fieldFlags</i>
then the result may be edited.
"""
)
cn_disc('<i>canvas.acroform.choice</i>方法在当前页面上创建了一个<i>dropdown</i>小部件。'
        '下拉菜单包含一个选项列表，其中一个或多个选项（取决于fieldFlags）可以被选中。'
        '如果您在<i>fieldFlags</i>中添加<i>edit</i>，那么结果可以被编辑。')

t = Table(
    [
        ['canvas.acroform.choice parameters', '', ''],
        ['Parameter', 'Meaning', 'Default'],
        ["name", "the radio's group (ie parameter) name", "None"],
        ["options", "List or tuple of available options", "[]"],
        ["value", "Singleton or list of strings of selected options", "[]"],
        [
            "x",
            "the horizontal position on the page (absolute coordinates)",
            "0",
        ],
        ["y", "the vertical position on the page (absolute coordinates)", "0"],
        ["width", "The widget width", "120"],
        ["height", "The widget height", "36"],
        ["fontName", "The name of the type 1 font to be used", "'Helvetica'"],
        ["fontSize", "The size of font to be used", "12"],
        ["fillColor", "colour to be used to fill the widget", "None"],
        ["textColor", "the colour of the symbol or text", "None"],
        ["borderWidth", "as it says", "1"],
        ["borderColor", "the widget's border colour", "None"],
        ["borderStyle", "The border style name", "'solid'"],
        [
            "tooltip",
            "The text to display when hovering over the widget",
            "None",
        ],
        [
            "annotationFlags",
            "blank separated string of annotation flags",
            "'print'",
        ],
        ["fieldFlags", "Blank separated field flags (see below)", "'combo'"],
        [
            "forceBorder",
            "when true a border force a border to be drawn",
            "False",
        ],
        ["relative", "if true obey the current canvas transform", "False"],
        [
            "dashLen ",
            "the dashline to be used if the borderStyle=='dashed'",
            "3",
        ],
        ["maxlen ", "None or maximum length of the widget value", "None"],
    ],
    [90, 260, 90],
    style=alStyle,
    repeatRows=2,
)
# getStory().append(t)
cn_t = Table(
    [
        ['canvas.acroform.choice 参数列表', '', ''],
        ['参数', '描述', '默认值'],
        ["name", "组名", "None"],
        ["options", "可用选项的列表或元组", "[]"],
        ["value", "单个或选定选项的字符串列表。", "[]"],
        [
            "x",
            "在页面上的水平位置(绝对坐标)",
            "0",
        ],
        ["y", "在页面上的垂直位置(绝对坐标)", "0"],
        ["width", "小组件宽度", "120"],
        ["height", "小组件高度", "36"],
        ["fontName", "要使用的第1种字体的名称。", "'Helvetica'"],
        ["fontSize", "要使用的字体大小", "12"],
        ["fillColor", "用来填充小组件的颜色", "None"],
        ["textColor", "符号的颜色", "None"],
        ["borderWidth", "边框宽度", "1"],
        ["borderColor", "边框颜色", "None"],
        ["borderStyle", "边框样式", "'solid'"],
        [
            "tooltip",
            "悬停在小组件上时要显示的文本。",
            "None",
        ],
        [
            "annotationFlags",
            "空白分隔的注解标志字符串",
            "'print'",
        ],
        ["fieldFlags", "空白分隔的字段标志（见下文）。", "'combo'"],
        [
            "forceBorder",
            "当真的时候会强行画边框",
            "False",
        ],
        ["relative", "如果为真，服从当前画布的变换", "False"],
        [
            "dashLen ",
            "如果borderStyle=='dashed'，要使用的破折号。",
            "3",
        ],
        ["maxlen ", "无或小组件值的最大长度", "None"],
    ],
    [90, 260, 90],
    style=cn_alStyle,
    repeatRows=2,
)
getStory().append(cn_t)

# heading3("Textfield Usage")
cn_heading3("文本字段用法")

disc(
    """The <i>canvas.acroform.textfield</i> method creates a <i>textfield</i> 
entry widget on the current page. The textfield may be edited
to change tha value of the widget
"""
)
cn_disc('<i>canvas.acroform.textfield</i>方法在当前页面上创建了一个<i>textfield</i>条目部件。'
        '文本字段可以被编辑，以改变小组件的值。')

t = Table(
    [
        ['canvas.acroform.textfield parameters', '', ''],
        ['Parameter', 'Meaning', 'Default'],
        ["name", "the radio's group (ie parameter) name", "None"],
        ["value", "Value of the text field", "''"],
        ["maxlen ", "None or maximum length of the widget value", "100"],
        [
            "x",
            "the horizontal position on the page (absolute coordinates)",
            "0",
        ],
        ["y", "the vertical position on the page (absolute coordinates)", "0"],
        ["width", "The widget width", "120"],
        ["height", "The widget height", "36"],
        ["fontName", "The name of the type 1 font to be used", "'Helvetica'"],
        ["fontSize", "The size of font to be used", "12"],
        ["fillColor", "colour to be used to fill the widget", "None"],
        ["textColor", "the colour of the symbol or text", "None"],
        ["borderWidth", "as it says", "1"],
        ["borderColor", "the widget's border colour", "None"],
        ["borderStyle", "The border style name", "'solid'"],
        [
            "tooltip",
            "The text to display when hovering over the widget",
            "None",
        ],
        [
            "annotationFlags",
            "blank separated string of annotation flags",
            "'print'",
        ],
        ["fieldFlags", "Blank separated field flags (see below)", "''"],
        [
            "forceBorder",
            "when true a border force a border to be drawn",
            "False",
        ],
        ["relative", "if true obey the current canvas transform", "False"],
        [
            "dashLen ",
            "the dashline to be used if the borderStyle=='dashed'",
            "3",
        ],
    ],
    [90, 260, 90],
    style=alStyle,
    repeatRows=2,
)
# getStory().append(t)
cn_t = Table(
    [
        ['canvas.acroform.textfield 参数列表', '', ''],
        ['参数', '描述', '默认值'],
        ["name", "组名", "None"],
        ["value", "文本字段的值", "''"],
        ["maxlen ", "无或小组件值的最大长度", "100"],
        [
            "x",
            "在页面上的水平位置(绝对坐标)",
            "0",
        ],
        ["y", "在页面上的垂直位置(绝对坐标)", "0"],
        ["width", "小组件宽度", "120"],
        ["height", "小组件高度", "36"],
        ["fontName", "要使用的第1种字体的名称。", "'Helvetica'"],
        ["fontSize", "要使用的字体大小", "12"],
        ["fillColor", "用来填充小组件的颜色", "None"],
        ["textColor", "符号或文本的颜色", "None"],
        ["borderWidth", "边框宽度", "1"],
        ["borderColor", "边框颜色", "None"],
        ["borderStyle", "边框样式", "'solid'"],
        [
            "tooltip",
            "悬停在小组件上时要显示的文本。",
            "None",
        ],
        [
            "annotationFlags",
            "空白分隔的注解标志字符串",
            "'print'",
        ],
        ["fieldFlags", "空白分隔的字段标志（见下文）。", "''"],
        [
            "forceBorder",
            "当真的时候会强行画边框",
            "False",
        ],
        ["relative", "如果为真，服从当前画布的变换", "False"],
        [
            "dashLen ",
            "如果borderStyle=='dashed'，要使用破折号。",
            "3",
        ],
    ],
    [90, 260, 90],
    style=cn_alStyle,
    repeatRows=2,
)
getStory().append(cn_t)

# heading3("Button styles")
cn_heading3("按钮样式")

disc(
    """The button style argument indicates what style of symbol should appear 
in the button when it is selected. There are several choices"""
)
cn_disc('按钮样式参数表示当按钮被选中时，应该在按钮中出现什么样式的符号。有几种选择')

eg("""check
cross
circle
star
diamond
""")

disc(
    """note that the document renderer can make some of these symbols wrong 
for their intended application.  Acrobat reader
prefers to use its own rendering on top of what the specification says should 
be shown (especially when the forms hihlighting features are used"""
)
cn_disc('请注意，文档渲染器可能会使这些符号中的某些符号在其预期应用中出现错误。 '
        'Acrobat阅读器更喜欢在规范规定应该显示的内容上使用自己的渲染（特别是在使用表格高亮功能的时候')

# heading3("Widget shape")
cn_heading3("小工具形状")

disc(
    """The shape argument describes how the outline of the checkbox or radio 
widget should appear you can use"""
)
cn_disc('形状参数描述了复选框或单选部件的轮廓应该如何显示，你可以使用')

eg("""circle
square
""")

disc("""The renderer may make its own decisions about how the widget should look; 
so Acrobat Reader prefers circular outlines for radios.""")
cn_disc('渲染器可能会自行决定小组件的外观，所以Acrobat Reader更喜欢圆形轮廓的收音机。')

# heading3("Border style")
cn_heading3("边框样式")

disc(
    """The borderStyle argument changes the 3D appearance of the widget on 
the page alternatives are"""
)
cn_disc('borderStyle参数会改变页面上小组件的3D外观，你可以使用')

eg("""  solid
  dashed
  inset
  bevelled
  underlined
"""
)
# heading3("fieldFlags Argument")
cn_heading3("^fieldFlags^ 参数")

disc(
    """The fieldFlags arguments can be an integer or a string containing 
blank separate tokens the values are shown in the table below. For
more information consult the PDF specification."""
)
cn_disc('fieldFlags参数可以是一个整数或一个包含空白的独立标记的字符串，其值如下表所示。更多信息请参考PDF规范。')

t = Table(
    [
        ['Field Flag Tokens and values', '', ''],
        ['Token', 'Meaning', 'Value'],
        ["readOnly", "The widget is read only", "1<<0"],
        ["required", "the widget is required", "1<<1"],
        ["noExport", "don't export the widget value", "1<<2"],
        ["noToggleToOff", "radios one only must be on", "1<<14"],
        ["radio", "added by the radio method", "1<<15"],
        ["pushButton", "if the button is a push button", "1<<16"],
        [
            "radiosInUnison",
            "radios with the same value toggle together",
            "1<<25",
        ],
        ["multiline", "for multiline text widget", "1<<12"],
        ["password", "password textfield", "1<<13"],
        ["fileSelect", "file selection widget", "1<<20"],  # 1.4
        ["doNotSpellCheck", "as it says", "1<<22"],  # 1.4
        ["doNotScroll", "text fields do not scroll", "1<<23"],  # 1.4
        [
            "comb",
            "make a comb style text based on the maxlen value",
            "1<<24",
        ],  # 1.5
        ["richText", "if rich text is used", "1<<25"],  # 1.5
        ["combo", "for choice fields", "1<<17"],
        ["edit", "if the choice is editable", "1<<18"],
        ["sort", "if the values should be sorted", "1<<19"],
        ["multiSelect", "if the choice allows multi-select", "1<<21"],  # 1.4
        ["commitOnSelChange", "not used by reportlab", "1<<26"],  # 1.5
    ],
    [90, 260, 90],
    style=alStyle,
    repeatRows=2,
)
# getStory().append(t)
cn_t = Table(
    [
        ['字段标志 Tokens 和 values', '', ''],
        ['Token', '描述', '值'],
        ["readOnly", "小部件只读", "1<<0"],
        ["required", "小部件是必需的", "1<<1"],
        ["noExport", "不要导出小组件的值", "1<<2"],
        ["noToggleToOff", "单选框组必选选择一个", "1<<14"],
        ["radio", "单选法", "1<<15"],
        ["pushButton", "当按钮为公共按钮时", "1<<16"],
        [
            "radiosInUnison",
            "单选框拥有一样的值时一起切换",
            "1<<25",
        ],
        ["multiline", "用于多行文本小组件", "1<<12"],
        ["password", "密码文本域", "1<<13"],
        ["fileSelect", "文件选择小组件", "1<<20"],  # 1.4
        ["doNotSpellCheck", "不拼写检查", "1<<22"],  # 1.4
        ["doNotScroll", "文本框不滚动", "1<<23"],  # 1.4
        [
            "comb",
            "根据最大长度值制作 comb 样式的文字",
            "1<<24",
        ],  # 1.5
        ["richText", "如果使用富文本", "1<<25"],  # 1.5
        ["combo", "针对下拉框", "1<<17"],
        ["edit", "如果选择是可编辑的", "1<<18"],
        ["sort", "是否要对数值进行排序", "1<<19"],
        ["multiSelect", "如果选择允许多选", "1<<21"],  # 1.4
        ["commitOnSelChange", "reportlab 没有使用", "1<<26"],  # 1.5
    ],
    [90, 260, 90],
    style=cn_alStyle,
    repeatRows=2,
)
getStory().append(cn_t)

# heading3("annotationFlags Argument")
cn_heading3("^annotationFlags^ 参数")

disc(
    """PDF widgets are annotations and have annotation properties these are 
shown in the table below"""
)
cn_disc('PDF小组件是注释，并具有注释属性，这些属性显示在下面的表格中。')

t = Table(
    [
        ['Annotation Flag Tokens and values', '', ''],
        ['Token', 'Meaning', 'Value'],
        ["invisible", "The widget is not shown", "1<<0"],
        ["hidden", "The widget is hidden", "1<<1"],
        ["print", "The widget will print", "1<<2"],
        [
            "nozoom",
            "The annotation will notscale with the rendered page",
            "1<<3",
        ],
        ["norotate", "The widget won't rotate with the page", "1<<4"],
        ["noview", "Don't render the widget", "1<<5"],
        ["readonly", "Widget cannot be interacted with", "1<<6"],
        ["locked", "The widget cannot be changed", "1<<7"],  # 1.4
        [
            "togglenoview",
            "Teh widget may be viewed after some events",
            "1<<8",
        ],  # 1.9
        [
            "lockedcontents",
            "The contents of the widget are fixed",
            "1<<9",
        ],  # 1.7
    ],
    [90, 260, 90],
    style=alStyle,
)
# getStory().append(t)
cn_t = Table(
    [
        ['注释标志 Tokens 和 values', '', ''],
        ['Token', '描述', '值'],
        ["invisible", "小组件不显示", "1<<0"],
        ["hidden", "小组件隐藏", "1<<1"],
        ["print", "小组件打印", "1<<2"],
        [
            "nozoom",
            "注释不会随渲染页面的大小而缩放。",
            "1<<3",
        ],
        ["norotate", "小组件不会随着页面旋转。", "1<<4"],
        ["noview", "不要渲染小组件", "1<<5"],
        ["readonly", "小组件只读，不交互", "1<<6"],
        ["locked", "小组件无法更改", "1<<7"],  # 1.4
        [
            "togglenoview",
            "在某些事件发生后，可以展示该小部件。",
            "1<<8",
        ],  # 1.9
        [
            "lockedcontents",
            "小部件的内容是固定的",
            "1<<9",
        ],  # 1.7
    ],
    [90, 260, 90],
    style=cn_alStyle,
)
getStory().append(cn_t)
