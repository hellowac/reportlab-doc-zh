from reportlab.platypus.flowables import Spacer
from reportlab.lib.units import inch
from reportlab.platypus import Image
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
    cn_npeg,
    EmbeddedCode
)

# heading1("""Programming $Flowables$""")
cn_heading1("编写 $Flowables$")

disc(
    """The following flowables let you conditionally evaluate and execute expressions and statements at wrap time:"""
)
cn_disc('下列$flowable$使您可以在包装文本时有条件地求值并执行表达式和语句：')


heading2("""$DocAssign(self, var, expr, life='forever')$""")
# cn_heading2('aaa')

disc("""Assigns a variable of name $var$ to the expression $expr$. E.g.:""")
cn_disc('为表达式$expr$指定一个名称为$var$的变量。例如：')


eg(
    """
DocAssign('i',3)
"""
)

heading2("""$DocExec(self, stmt, lifetime='forever')$""")
# cn_heading2('aaa')

disc("""Executes the statement $stmt$. E.g.:""")
cn_disc('执行语句$stmt$。例如：')


eg(
    """
DocExec('i-=1')
"""
)

heading2(
    """$DocPara(self, expr, format=None, style=None, klass=None, escape=True)$"""
)
# cn_disc('aaa')


disc(
    """Creates a paragraph with the value of expr as text.
If format is specified it should use %(__expr__)s for string interpolation
of the expression expr (if any). It may also use %(name)s interpolations
for other variables in the namespace. E.g.:"""
)
cn_disc('创建一个以 $expr$ 的值为文本的段落。'
        '如果指定了格式，它应该使用 %($__expr__$)s 对表达式 $expr$ (如果有的话) 进行字符串插值。'
        '它也可以使用%($name$)s对命名空间中的其他变量进行插值。'
        '例如')


eg(
    """
DocPara('i',format='The value of i is %(__expr__)d',style=normal)
"""
)

heading2("""$DocAssert(self, cond, format=None)$""")
# cn_heading2('aaa')

disc(
    """Raises an $AssertionError$ containing the $format$ string if $cond$ evaluates as $False$."""
)
cn_disc('如果$cond$评价为$False$，则引发包含$format$字符串的$AssertionError$。')


eg(
    """
DocAssert(val, 'val is False')
"""
)

heading2("""$DocIf(self, cond, thenBlock, elseBlock=[])$""")
# cn_heading2('aaa')

disc(
    """If $cond$ evaluates as $True$, this flowable is replaced by the $thenBlock$ elsethe $elseBlock$."""
)
cn_disc('如果$cond$的值为$True$，那么这个flowable就会被$thenBlock$ elsethe $elseBlock$取代。')


eg(
    """
DocIf('i>3',Paragraph('The value of i is larger than 3',normal),\\
        Paragraph('The value of i is not larger than 3',normal))
"""
)

heading2("""$DocWhile(self, cond, whileBlock)$""")
# cn_heading2('aaa')

disc("""Runs the $whileBlock$ while $cond$ evaluates to $True$. E.g.:""")
cn_disc('当$cond$值为$True$时，运行$whileBlock$。例如：')


eg(
    """
DocAssign('i',5)
DocWhile('i',[DocPara('i',format='The value of i is %(__expr__)d',style=normal),DocExec('i-=1')])
"""
)

# disc("""This example produces a set of paragraphs of the form:""")
cn_disc('这个例子产生的一组段落的形式是：')


eg(
    """
The value of i is 5
The value of i is 4
The value of i is 3
The value of i is 2
The value of i is 1
"""
)

# heading1("""Other Useful $Flowables$""")
cn_heading1("其他可用的$Flowables$")

heading2(
    """$Preformatted(text, style, bulletText=None, dedent=0, maxLineLength=None, splitChars=None, newLineChars=None)$"""
)

disc(
    """
Creates a preformatted paragraph which does no wrapping, line splitting or other manipulations.
No $XML$ style tags are taken account of in the text.
If dedent is non zero $dedent$ common leading spaces will be removed from the front of each line.
"""
)
cn_disc('创建一个预格式化的段落，不进行任何包装、分行或其他操作。'
        '在文本中不考虑$XML$样式标签。'
        '如果dedent是非零，$dedent$的公共前导空格将从每行前面移除。')

# heading3("Defining a maximum line length")
cn_heading3('定义最大行长')

disc(
    """
You can use the property $maxLineLength$ to define a maximum line length. If a line length exceeds this maximum value, the line will be automatically splitted.
"""
)
cn_disc('您可以使用属性 $maxLineLength$ 来定义最大行长。'
        '如果行长超过这个最大值，行将被自动分割。')

disc(
    """
The line will be split on any single character defined in $splitChars$. If no value is provided for this property, the line will be split on any of the following standard characters: space, colon, full stop, semi-colon, coma, hyphen, forward slash, back slash, left parenthesis, left square bracket and left curly brace
"""
)
cn_disc('行将被分割成$splitChars$中定义的任何一个字符。'
        '如果没有为该属性提供值，'
        '则行将在以下任何标准字符上进行分割：空格、冒号、句号、分号、逗号、连字符、前斜线、后斜线、左括号、左方括号和左大括号。')

disc(
    """
Characters can be automatically inserted at the beginning of each line that has been created. You can set the property $newLineChars$ to the characters you want to use.
"""
)
cn_disc('字符可以自动插入到已创建的每一行的开头。你可以设置属性$newLineChars$为你想使用的字符。')

EmbeddedCode(
    """
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
heading2(
    """$XPreformatted(text, style, bulletText=None, dedent=0, frags=None)$"""
)
# cn_disc('aaa')

disc(
    """
This is a non rearranging form of the $Paragraph$ class; XML tags are allowed in
$text$ and have the same meanings as for the $Paragraph$ class. As for 
$Preformatted$, if dedent is non zero $dedent$ common leading spaces 
will be removed from the front of each line.
"""
)
cn_disc('这是$Paragraph$类的一种非重排形式；'
        '$text$中允许使用XML标签，其含义与$Paragraph$类相同。'
        '至于 $Preformatted$，如果dedent是非零，$dedent$普通的前导空格将从每行的前面移除。')

EmbeddedCode(
    """
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

heading2("""$Image(filename, width=None, height=None)$""")

disc(
    """Create a flowable which will contain the image defined by the data in file $filename$ which can be
filepath, file like object or an instance of a $reportlab.graphics.shapes.Drawing$.
The default <b>PDF</b> image type <i>jpeg</i> is supported and if the <b>PIL</b> extension to <b>Python</b>
is installed the other image types can also be handled. If $width$ and or $height$ are specified
then they determine the dimension of the displayed image in <i>points</i>. If either dimension is
not specified (or specified as $None$) then the corresponding pixel dimension of the image is assumed
to be in <i>points</i> and used.
"""
)
cn_disc('创建一个 $flowable$，它将包含由文件 $filename$ 中的数据定义的图像，'
        '该文件可以是文件路径、类似文件的对象或 $reportlab.graphics.shapes.Drawing$的实例。'
        '默认的 <b>PDF</b> 图像类型<i>jpeg</i>被支持，'
        '如果安装了<b>PIL</b>扩展到<b>Python</b>，其他图像类型也可以被处理。'
        '如果指定了 $width$和$height$，那么它们决定了显示图像的尺寸，单位是<i>points</i>。'
        '如果没有指定任何一个尺寸(或者指定为$None$)，那么图像的相应像素尺寸被假定为<i>points</i>并使用。')

I = "images/lj8100.jpg"
eg(
    """
Image("lj8100.jpg")
""",
    after=0.1,
)

# disc("""will display as""")
cn_disc('将显示为')

try:
    getStory().append(Image(I))
except:
    disc("""An image should have appeared here.""")
    cn_disc("这里应该出现一张图片。")

disc("""whereas""")
cn_disc('然而')

eg(
    """
im = Image("lj8100.jpg", width=2*inch, height=2*inch)
im.hAlign = 'CENTER'
""",
    after=0.1,
)

disc('produces')
cn_disc('产出')

try:
    im = Image(I, width=2 * inch, height=2 * inch)
    im.hAlign = 'CENTER'
    getStory().append(Image(I, width=2 * inch, height=2 * inch))
except:
    disc("""An image should have appeared here.""")
    cn_disc("这里应该出现一张图片。")

heading2("""$Spacer(width, height)$""")

disc(
    """This does exactly as would be expected; it adds a certain amount of space into the story.
At present this only works for vertical space.
"""
)
cn_disc('这与预期的一样，它为故事增加了一定的空间。目前，这只对垂直空间有效。')


CPage(1)
heading2("""$PageBreak()$""")

disc(
    """This $Flowable$ represents a page break. It works by effectively consuming all vertical
space given to it. This is sufficient for a single $Frame$ document, but would only be a
frame break for multiple frames so the $BaseDocTemplate$ mechanism
detects $pageBreaks$ internally and handles them specially.
"""
)
cn_disc('这个 $Flowable$ 代表了一个页面中断。'
        '它的工作原理是有效地消耗所有给它的垂直空间。'
        '这对于单个 $Frame$ 文档来说已经足够了，但对于多个框架来说，'
        '这只是一个框架中断，所以 $BaseDocTemplate$ 机制会在内部检测到 $pageBreaks$ 并进行特殊处理。')

CPage(1)
heading2("""$CondPageBreak(height)$""")

disc(
    """This $Flowable$ attempts to force a $Frame$ break if insufficient vertical space remains
in the current $Frame$. It is thus probably wrongly named and should probably be renamed as
$CondFrameBreak$.
"""
)
cn_disc('如果当前的$Frame$中没有足够的垂直空间，'
        '那么这个$Flowable$试图强制$Frame$断裂。'
        '因此，它的命名可能是错误的，也许应该重新命名为$CondFrameBreak$。')

CPage(1)
heading2("""$KeepTogether(flowables)$""")

disc(
    """
This compound $Flowable$ takes a list of $Flowables$ and attempts to keep them in the same $Frame$.
If the total height of the $Flowables$ in the list $flowables$ exceeds the current frame's available
space then all the space is used and a frame break is forced.
"""
)
cn_disc('这个复合的 $Flowable$ 接收一个 $Flowables$ 的列表，'
        '并试图将它们放在同一个 $Frame$ 中。'
        '如果列表中 $flowables$ 中的 $Flowables$ 的总高度超过了当前框架的可用空间，'
        '那么所有的空间都会被使用，并且会强制中断框架。')

CPage(1)
heading2("""$TableOfContents()$""")

disc(
    """
A table of contents can be generated by using the $TableOfContents$ flowable. The following steps are needed to add a table of contents to your document:
"""
)
cn_disc('通过使用$TableOfContents$ flowable 可以生成一个目录。'
        '下面的步骤是在您的文档中添加一个目录表所需要的。')


disc('Create an instance of $TableOfContents$. '
     'Override the level styles (optional) and add the object to the story:')
cn_disc('创建一个 $TableOfContents$ 的实例。'
        '覆盖关卡样式（可选）并将对象添加到故事中。')

eg(
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

disc(
    """Entries to the table of contents can be done either manually by calling
the $addEntry$ method on the $TableOfContents$ object or automatically by sending
a $'TOCEntry'$ notification in the $afterFlowable$ method of the $DocTemplate$
you are using.

The data to be passed to $notify$ is a list of three or four items countaining
a level number, the entry text, the page number and an optional destination key
which the entry should point to.
This list will usually be created in a document template's method
like afterFlowable(), making notification calls using the notify()
method with appropriate data like this:
"""
)
cn_disc('对目录的输入可以通过调用 '
        '$TableOfContents$ 对象的 $addEntry$ 方法手动完成，'
        '也可以通过在 $DocTemplate$ 的 $afterFlowable$ 方法中自动发送一个 $\'TOCEntry\'$ 通知。'
        '传递给 $notify$ 的数据是一个由三个或四个项目组成的列表，'
        '其中包括一个级别号，条目文本，页码和一个可选的目标键，该条目应该指向。'
        '这个列表通常会在文档模板的方法中创建，'
        '比如afterFlowable()，使用notify()方法调用通知，'
        '并提供适当的数据，比如这样。')


eg(
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

disc(
    """This way, whenever a paragraph of style $'Heading1'$ or $'Heading2'$ is added to the story, it will appear in the table of contents.
$Heading2$ entries will be clickable because a bookmarked key has been supplied.
"""
)
cn_disc("这样，每当一个样式为 $'Heading1'$ 或 $'Heading2'$ 的段落被添加到故事中，它就会出现在目录中。"
        "$Heading2$ 条目将可点击，因为已经提供了一个书签键。")


disc(
    """Finally you need to use the $multiBuild$ method of the DocTemplate because tables of contents need several passes to be generated:"""
)
cn_disc('最后你需要使用 DocTemplate 的 $multiBuild$ 方法，因为内容表需要多次传递才能生成。')


eg(
    """
doc.multiBuild(story)
"""
)

disc(
    """Below is a simple but working example of a document with a table of contents:"""
)
cn_disc('下面是一个简单但可行的带目录的文档例子。')


eg(
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

CPage(1)
heading2("""$SimpleIndex()$""")

disc(
    """
An index can be generated by using the $SimpleIndex$ flowable.
The following steps are needed to add an index to your document:
"""
)
cn_disc('可以通过使用 $SimpleIndex$ flowable生成一个索引。'
        '下面的步骤是为您的文档添加索引所需要的。')


disc("""Use the index tag in paragraphs to index terms:""")
cn_disc('在段落中使用索引标签来索引术语。')


eg(
    '''
story = []

...

story.append('The third <index item="word" />word of this paragraph is indexed.')
'''
)

disc(
    """Create an instance of $SimpleIndex$ and add it to the story where you want it to appear:"""
)
cn_disc('创建一个$SimpleIndex$的实例，并将其添加到你希望它出现的故事中。')


eg(
    '''
index = SimpleIndex(dot=' . ', headers=headers)
story.append(index)
'''
)

disc(
    """The parameters which you can pass into the SimpleIndex constructor are explained in the reportlab reference. Now, build the document by using the canvas maker returned by SimpleIndex.getCanvasMaker():"""
)
cn_disc('你可以传入 $SimpleIndex$ 构造函数的参数在 reportlab 参考资料中解释。'
        '现在，使用SimpleIndex.getCanvasMaker()返回的canvasmaker来构建文档。')

eg(
    """
doc.build(story, canvasmaker=index.getCanvasMaker())
"""
)

disc(
    """To build an index with multiple levels, pass a comma-separated list of items to the item attribute of an index tag:"""
)
cn_disc('要建立一个多级索引，请将一个以逗号分隔的项目列表传递给索引标签的 item 属性。')


eg(
    """
<index item="terma,termb,termc" />
<index item="terma,termd" />
"""
)

disc(
    """terma will respresent the top-most level and termc the most specific term. termd and termb will appear in the same level inside terma."""
)
cn_disc('$terma$ 将表示最顶层的术语，$termc$ 将表示最具体的术语，$terd$ 和 $termb$ 将出现在 $terma$ 的同一层次。')


disc(
    """If you need to index a term containing a comma, you will need to escape it by doubling it. To avoid the ambiguity of three consecutive commas (an escaped comma followed by a list separator or a list separator followed by an escaped comma?) introduce a space in the right position. Spaces at the beginning or end of terms will be removed."""
)
cn_disc('如果您需要为一个包含逗号的术语编制索引，您需要将其加倍转义。'
        '为了避免三个连续逗号的歧义（一个转义逗号后面是一个列表分隔符或一个列表分隔符后面是一个转义逗号？）'
        '在正确的位置引入一个空格。'
        '术语开头或结尾的空格将被删除。')


eg(
    """
<index item="comma(,,), ,, ,...   " />
"""
)

disc(
    """
This indexes the terms "comma (,)", "," and "...".
"""
)
cn_disc('此处索引了 "逗号（，）"、"，"和"...... "等术语。')


heading2("""$ListFlowable(),ListItem()$""")

disc(
    """
Use these classes to make ordered and unordered lists.  Lists can be nested.
"""
)
cn_disc('使用这些类来制作有序和无序的列表。 列表可以被嵌套。')


disc(
    """
$ListFlowable()$ will create an ordered list, which can contain any flowable.  The class has a number of parameters to change font, colour, size, style and position of list numbers, or of bullets in unordered lists.  The type of numbering can also be set to use lower or upper case letters ('A,B,C' etc.) or Roman numerals (capitals or lowercase) using the bulletType property.  To change the list to an unordered type, set bulletType='bullet'.
"""
)
cn_disc('$ListFlowable()$ 将创建一个有序的列表，它可以包含任何可流动的。 '
        '该类有许多参数可以改变列表编号的字体、颜色、大小、样式和位置，或者无序列表中的项目符号。 '
        '还可以使用 $bulletType$ 属性将编号类型设置为使用小写或大写字母（\'A,B,C\'等）或罗马数字（大写或小写）。 '
        '要将列表改为无序类型，请设置 bulletType=\'bullet\'。')


disc(
    """
Items within a $ListFlowable()$ list can be changed from their default appearance by wrapping them in a $ListItem()$ class and setting its properties.
"""
)
cn_disc('在 $ListFlowable()$ 列表中的项目可以通过将它们包装在 $ListItem()$ 类中并设置其属性来改变它们的默认外观。')


disc(
    """
The following will create an ordered list, and set the third item to an unordered sublist.
"""
)
cn_disc('下面将创建一个有序列表，并将第三项设置为无序子列表。')


EmbeddedCode(
    """
from reportlab.platypus import ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()
style = styles["Normal"]
t = ListFlowable(
[
Paragraph("Item no.1", style),
ListItem(Paragraph("Item no. 2", style),bulletColor="green",value=7),
ListFlowable(
                [
                Paragraph("sublist item 1", style),
                ListItem(Paragraph('sublist item 2', style),bulletColor='red',value='square')
                ],
                bulletType='bullet',
                start='square',
                ),
Paragraph("Item no.4", style),
],
bulletType='i'
)
             """
)

disc(
    """To cope with nesting the $start$ parameter can be set to a list of possible starts; for $ul$ acceptable starts are any unicode character or specific names known to flowables.py eg
$bulletchar$, $circle$, $square$, $disc$, $diamond$, $diamondwx$, $rarrowhead$, $sparkle$, $squarelrs$ or  $blackstar$. For $ol$ the $start$ can be any character from $'1iaAI'$ to indicate different number styles.
"""
)
cn_disc('为了应对嵌套，$start$参数可以设置为一个可能的起始列表；'
        '对于$ul$来说，可接受的起始是任何unicode字符或flowables.py已知的特定名称，'
        '例如$bulletchar$、$circle$、$square$、$disc$、$diamond$、$diamondwx$、'
        '$rarrowhead$、$sparkle$、$squarelrs$或$blackstar$。'
        '对于$ol$来说，$start$可以是$\'1iaAI\'$中的任何字符，以表示不同的数字风格。')


heading2("""$BalancedColumns()$""")

disc(
    """Use the $BalancedColumns$ class to make a flowable that splits its content flowables into two or more roughly equal sized columns.
Effectively $n$ frames are synthesized to take the content and the flowable tries to balance the content between them. The created frames
will be split when the total height is too large and the split will maintain the balance. 
"""
)
cn_disc('使用 $BalancedColumns$ 类来制作一个flowable，'
        '将其内容 $flowable$ 分割成两个或更多大小大致相等的列。'
        '实际上，$n$ 框架被合成为内容，而 $flowable$ 试图在它们之间平衡内容。'
        '当创建的框架总高度过大时，会被拆分，拆分后会保持平衡。')

eg(
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
