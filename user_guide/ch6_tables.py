# Copyright ReportLab Europe Ltd. 2000-2017
# see license.txt for license details
# history https://hg.reportlab.com/hg-public/reportlab/log/tip/docs/userguide/ch6_tables.py
from reportlab.platypus.flowables import Spacer
from reportlab.lib.units import inch
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

from reportlab.platypus import Image

# heading1("Tables and TableStyles")
cn_heading1('表格和表格样式')

disc(
    """
The $Table$  and $LongTable$ classes derive from the $Flowable$ class and are intended
as a simple textual gridding mechanisms. The $longTable$ class uses a greedy algorithm
when calculating column widths and is intended for long tables where speed counts.
$Table$ cells can hold anything which can be converted to
a <b>Python</b> $string$ or $Flowables$ (or lists of $Flowables$).
"""
)
cn_disc('$Table$和$LongTable$类来源于$Flowable$类，是一个简单的文本网格机制。'
        '当计算列宽时，$longTable$类使用了一种贪婪的算法，它是为速度至上的长表设计的。'
        '$Table$单元格可以容纳任何可以转换为<b>Python</b> $string$或$Flowables$ '
        '(或$Flowables$列表)的内容。')

disc(
    """
Our present tables are a trade-off between efficient drawing and specification
and functionality.  We assume the reader has some familiarity with HTML tables.
In brief, they have the following characteristics:
"""
)
cn_disc('我们现在的表格是在高效绘图和规范与功能之间的权衡。 '
        '我们假设读者对HTML表格有一定的熟悉。'
        '简而言之，它们具有以下特点。')


bullet(
    """They can contain anything convertible to a string; flowable
objects such as other tables; or entire sub-stories"""
)

bullet(
    """They can work out the row heights to fit the data if you don't supply
the row height.  (They can also work out the widths, but generally it is better
for a designer to set the width manually, and it draws faster)."""
)

bullet(
    """They can split across pages if needed (see the canSplit attribute).
You can specify that a number of rows at the top and bottom should be
repeated after the split (e.g. show the headers again on page 2,3,4...)"""
)

bullet(
    """They have a simple and powerful notation for specifying shading and
gridlines which works well with financial or database tables, where you
don't know the number of rows up front.  You can easily say 'make the last row
bold and put a line above it'"""
)

bullet(
    """The style and data are separated, so you can declare a handful of table
styles and use them for a family of reports.  Styes can also 'inherit', as with
paragraphs."""
)
cn_bullet('它们可以包含任何可转换为字符串的东西；可流动的对象，如其他表格；或整个子集。')
cn_bullet('如果你不提供行高，他们可以计算出行高来适应数据。 '
          '(他们也可以计算出宽度，但一般来说，设计师最好手动设置宽度，这样画得更快)。')

cn_bullet('如果需要的话，它们可以在不同的页面上进行分割（参见canSplit属性）。'
          '你可以指定在分割后，顶部和底部的若干行应该重复显示'
          '（例如，在第2,3,4页再次显示页眉...）。')

cn_bullet('他们有一个简单而强大的符号来指定阴影和网格线，'
          '这对于财务或数据库表来说非常适用，因为你不知道前面有多少行。 '
          '你可以很容易的说 '
          '"把最后一行加粗，并在上面加一条线"。')

cn_bullet('样式和数据是分开的，所以你可以声明少量的表格样式，'
          '并将它们用于一个报表系列。 '
          '样式也可以 "继承"，就像段落一样。')

disc(
    """There is however one main limitation compared to an HTML table.
They define a simple rectangular grid.  There is no simple row or column
spanning; if you need to span cells, you must nest tables inside table cells instead or use a more
complex scheme in which the lead cell of a span contains the actual contents."""
)
cn_disc('然而，与HTML表格相比，有一个主要的限制。'
        '它们定义了一个简单的矩形网格。 '
        '没有简单的行或列跨度；'
        '如果你需要跨度单元格，'
        '你必须将表格嵌套在表格单元格内，或者使用更复杂的方案，'
        '其中跨度的前导单元格包含实际内容。')


disc(
    """
$Tables$ are created by passing the constructor an optional sequence of column widths,
an optional sequence of row heights, and the data in row order.
Drawing of the table can be controlled by using a $TableStyle$ instance. This allows control of the
color and weight of the lines (if any), and the font, alignment and padding of the text.
A primitive automatic row height and or column width calculation mechanism is provided for.
"""
)
cn_disc('通过向构造函数传递列宽的可选序列、行高的可选序列以及行序的数据来创建$Tables$。'
        '表的绘制可以通过使用TableStyle$实例来控制。'
        '这允许控制行的颜色和权重（如果有的话），以及文本的字体、对齐和填充。'
        '提供了一个原始的自动行高和列宽计算机制。')


# heading2('$Table$ User Methods')
cn_heading2('$Table$ 用户方法')

disc(
    """These are the main methods which are of interest to the client programmer."""
)
cn_disc('这些是客户端程序员感兴趣的主要方法。')


heading4(
    """$Table(data, colWidths=None, rowHeights=None, style=None, splitByRow=1,
repeatRows=0, repeatCols=0, rowSplitRange=None, spaceBefore=None, spaceAfter=None)$"""
)
# cn_heading4('aaa')

disc(
    """The $data$ argument is a sequence of sequences of cell values each of which
should be convertible to a string value using the $str$ function or should be a Flowable instance (such as a $Paragraph$) or a list (or tuple) of such instances.
If a cell value is a $Flowable$ or list of $Flowables$ these must either have a determined width
or the containing column must have a fixed width.
The first row of cell values
is in $data[0]$ i.e. the values are in row order. The $i$, $j$<sup>th.</sup> cell value is in
$data[i][j]$. Newline characters $'\\n'$ in cell values are treated as line split characters and
are used at <i>draw</i> time to format the cell into lines.
"""
)
cn_disc('参数$data$是单元格值的序列，'
        '每个单元格值都应该使用$str$函数转换为字符串值，'
        '或者应该是一个 $Flowable$ 实例(如$Paragraph$)或此类实例的列表(或元组)。'
        '如果一个单元格值是一个 $Flowable$ 或 $Flowable$ 的列表，'
        '这些单元格必须有一个确定的宽度，或者包含的列必须有一个固定的宽度。'
        '单元格值的第一行在 $data[0]$ 中，也就是说，单元格值是按行顺序排列的。'
        '$i$, $j$<sup>th.</sup>单元格值在$data[i][j]$中。'
        '单元格值中的新行字符$\'\\n\'$被视为行分割字符，'
        '并在<i>draw</i>时用于将单元格格式化为行。')

disc(
    """The other arguments are fairly obvious, the $colWidths$ argument is a sequence
of numbers or possibly $None$, representing the widths of the columns. The number of elements
in $colWidths$ determines the number of columns in the table.
A value of $None$ means that the corresponding column width should be calculated automatically."""
)
cn_disc('其他参数是相当明显的，'
        '$colWidths$ 参数是一个数字序列，也可能是$None$，代表列的宽度。'
        '在 $colWidths$ 中的元素数决定了表中的列数。值为$None$意味着相应的列宽应该自动计算。')


disc(
    """The $rowHeights$ argument is a sequence
of numbers or possibly $None$, representing the heights of the rows. The number of elements
in $rowHeights$ determines the number of rows in the table.
A value of $None$ means that the corresponding row height should be calculated automatically."""
)
cn_disc('参数 $rowHeights$ 是一个数字序列，也可能是$None$，代表行的高度。'
        '$rowHeights$ 中的元素数决定了表中的行数。'
        '值为$None$意味着相应的行高应该自动计算。')


disc("""The $style$ argument can be an initial style for the table.""")
cn_disc('参数 $style$ 可以是表的初始样式。')

disc(
    """The $splitByRow$ argument is only needed for tables both too tall and too wide
to fit in the current context.  In this case you must decide whether to 'tile'
down and across, or across and then down.  This parameter is a Boolean indicating that the
$Table$ should split itself by row before attempting to split itself by 
column when too little space is available in the current drawing area and the caller wants the $Table$ to split.
Splitting a $Table$ by column is currently not implemented, so setting $splitByRow$ to $False$ will result in a $NotImplementedError$."""
)
cn_disc('$splitByRow$ 参数只适用于太高和太宽而无法适应当前上下文的表格。 '
        '在这种情况下，你必须决定是向下和横向 "平铺"，还是横向然后向下。 '
        '这个参数是一个布尔值，表示当当前绘图区域可用空间太小，而调用者希望$Table$进行分割时，'
        '$Table$应该先按行进行分割，再按列进行分割。'
        '目前还没有实现按列分割$Table$，'
        '所以将$splitByRow$设置为$False$'
        '将导致$NotImplementedError$。')


disc(
    """The $repeatRows$ argument specifies the number or a tuple of leading rows
that should be repeated when the $Table$ is asked to split itself. If it is a tuple it should specify which of the leading rows should be repeated; this allows
for cases where the first appearance of the table hsa more leading rows than later split parts.
The $repeatCols$ argument is currently ignored as a $Table$ cannot be split by column."""
)
cn_disc('参数$repeatRows$指定了当$Table$被要求拆分时应该重复的前导行的数量或元组。'
        '如果它是一个元组，它应该指定哪些前导行应该被重复；'
        '这允许表的第一次出现比后来的分割部分有更多的前导行。'
        '目前，$repeatCols$参数被忽略，因为$Table$不能按列进行拆分。')

disc(
    """The $spaceBefore$ &amp; $spaceAfter$ arguments may be used to put extra space before or after the table when renedered in a $platypus$ story."""
)
cn_disc('当在$platypus$故事中重新编排时，'
        '$spaceBefore$ 和 $spaceAfter$ 参数 可以用来在表格之前或之后放置额外的空间。')

disc(
    """The $rowSplitRange$ argument may be used to control the splitting of the table to a subset of its rows; that can be to prevent splitting too close to the beginning or end of the table."""
)
cn_disc('$rowSplitRange$参数可以用来控制表的分割，将表分割成它的行的子集；这可以防止分割太接近表的开始或结束。')

heading4('$Table.setStyle(tblStyle)$')
# cn_heading4('aaa')

disc(
    """
This method applies a particular instance of class $TableStyle$ (discussed below)
to the $Table$ instance. This is the only way to get $tables$ to appear
in a nicely formatted way.
"""
)
cn_disc('这个方法将类$TableStyle$(下面讨论)的一个特定实例应用到$Table$实例中。'
        '这是让$tables$以一种很好的格式化方式出现的唯一方法。')

disc(
    """
Successive uses of the $setStyle$ method apply the styles in an additive fashion.
That is, later applications override earlier ones where they overlap.
"""
)
cn_disc('对$setStyle$方法的连续使用以加法的方式应用这些样式。'
        '也就是说，后面的应用会覆盖前面重叠的应用。')


# heading2('$TableStyle$')
cn_heading2('$TableStyle$')

disc(
    """
This class is created by passing it a sequence of <i>commands</i>, each command
is a tuple identified by its first element which is a string; the remaining
elements of the command tuple represent the start and stop cell coordinates
of the command and possibly thickness and colors, etc.
"""
)
cn_disc('这个类是通过传递给它一个<i>commands</i>序列来创建的，'
        '每个 $command$ 是一个元组，由它的第一个元素识别，它是一个字符串；'
        '$command$ 元组的其余元素代表命令的起始和停止单元格坐标，可能还有厚度和颜色等。')

# heading2("$TableStyle$ User Methods")
cn_heading2('$TableStyle$  用户方法')

heading3("$TableStyle(commandSequence)$")
# cn_heading3('aaa')

disc(
    """The creation method initializes the $TableStyle$ with the argument
command sequence as an example:"""
)
cn_disc('创建方法以参数命令序列为例初始化$TableStyle$。')

eg(
    """
    LIST_STYLE = TableStyle(
        [('LINEABOVE', (0,0), (-1,0), 2, colors.green),
        ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 2, colors.green),
        ('ALIGN', (1,1), (-1,-1), 'RIGHT')]
        )
"""
)

heading3("$TableStyle.add(commandSequence)$")
# cn_heading3('aaa')

disc(
    """This method allows you to add commands to an existing
$TableStyle$, i.e. you can build up $TableStyles$ in multiple statements.
"""
)
cn_disc('此方法允许你向现有的$TableStyle$添加命令，即你可以在多个语句中建立$TableStyles$。')

eg(
    """
    LIST_STYLE.add('BACKGROUND', (0,0), (-1,0), colors.Color(0,0.7,0.7))
"""
)

heading3("$TableStyle.getCommands()$")
# cn_heading3('aaa')

disc("""This method returns the sequence of commands of the instance.""")
cn_disc('此方法返回实例的命令序列。')

eg(
    """
    cmds = LIST_STYLE.getCommands()
"""
)

heading2("$TableStyle$ Commands")
# cn_heading2('aaa')

disc(
    """The commands passed to $TableStyles$ come in three main groups
which affect the table background, draw lines, or set cell styles.
"""
)
cn_disc('传递给$TableStyles$的命令主要有三组，分别影响表格背景、绘制线条或设置单元格样式。')

disc(
    """The first element of each command is its identifier,
the second and third arguments determine the cell coordinates of
the box of cells which are affected with negative coordinates
counting backwards from the limit values as in <b>Python</b>
indexing. The coordinates are given as
(column, row) which follows the spreadsheet 'A1' model, but not
the more natural (for mathematicians) 'RC' ordering.
The top left cell is (0, 0) the bottom right is (-1, -1). Depending on
the command various extra (???) occur at indices beginning at 3 on.
"""
)
cn_disc('每个命令的第一个元素是它的标识符，'
        '第二个和第三个参数决定了受影响的单元格的单元格坐标，'
        '负坐标从极限值向后数，就像<b>Python</b>索引一样。'
        '坐标是以(列，行)的形式给出的，它遵循电子表格的 "A1 "模型，'
        '但不是更自然的(对数学家来说) "RC "排序。'
        '左上角的单元格是（0，0），右下角的单元格是（-1，-1）。'
        '根据命令的不同，各种额外的(???)发生在3开始的指数上。')

pencilnote()

cn_disc('<font color="red">译者注</font>: 对表格坐标系理解不够透彻的参考: '
        '<a href="https://blog.csdn.net/weixin_39021016/article/details/109044955">'
        '<font color="green">这里</font>'
        '</a>')

heading3("""$TableStyle$ Cell Formatting Commands""")
# cn_heading3('aaa')

disc(
    """The cell formatting commands all begin with an identifier, followed by
the start and stop cell definitions and the perhaps other arguments.
the cell formatting commands are:"""
)
cn_disc('单元格格式化命令都以一个标识符开头，后面是单元格定义的开始和结束，也许还有其他参数。')

# npeg(
#     """
# FONT                    - takes fontname, optional fontsize and optional leading.
# FONTNAME (or FACE)      - takes fontname.
# FONTSIZE (or SIZE)      - takes fontsize in points; leading may get out of sync.
# LEADING                 - takes leading in points.
# TEXTCOLOR               - takes a color name or (R,G,B) tuple.
# ALIGNMENT (or ALIGN)    - takes one of LEFT, RIGHT and CENTRE (or CENTER) or DECIMAL.
# LEFTPADDING             - takes an integer, defaults to 6.
# RIGHTPADDING            - takes an integer, defaults to 6.
# BOTTOMPADDING           - takes an integer, defaults to 3.
# TOPPADDING              - takes an integer, defaults to 3.
# BACKGROUND              - takes a color defined by an object, string name or numeric tuple/list,
#                           or takes a list/tuple describing a desired gradient fill which should
#                           contain three elements of the form [DIRECTION, startColor, endColor]
#                           where DIRECTION is either VERTICAL or HORIZONTAL.
# ROWBACKGROUNDS          - takes a list of colors to be used cyclically.
# COLBACKGROUNDS          - takes a list of colors to be used cyclically.
# VALIGN                  - takes one of TOP, MIDDLE or the default BOTTOM
# """
# )
cn_npeg("""
FONT                    - 字体名称, 可选字体大小和字符间距(leading).
FONTNAME (or FACE)      - 字体名称.
FONTSIZE (or SIZE)      - 以点为单位的字体大小; 字符间距(leading)可能会不同步.
LEADING                 - 以点为单位的字符间距(leading).
TEXTCOLOR               - 颜色名称或 (R,G,B) 元组.
ALIGNMENT (or ALIGN)    - LEFT, RIGHT 和 CENTRE (或 CENTER) 或 DECIMAL 中的一个.
LEFTPADDING             - 整数左边距，默认为6.
RIGHTPADDING            - 整数右边距，默认为6.
BOTTOMPADDING           - 整数下边距，默认为3.
TOPPADDING              - 整数上边距，默认为3.
BACKGROUND              - 取一个由对象、字符串名称或数字元组/列表定义的颜色，
                          或者取一个描述所需渐变填充的列表/元组，
                          该列表/元组应包含[DIRECTION, startColor, endColor]三个元素，
                          其中 $DIRECTION$ 是 $VERTICAL$ 或 $HORIZONTAL$。
ROWBACKGROUNDS          - 一个要循环使用的颜色列表。
COLBACKGROUNDS          - 一个要循环使用的颜色列表。
VALIGN                  - 取 $TOP, MIDDLE$ 或默认的 $BOTTOM$ 中的一个。
""")

disc(
    """This sets the background cell color in the relevant cells.
The following example shows the $BACKGROUND$, and $TEXTCOLOR$ commands in action:"""
)
cn_disc('这将设置相关单元格的背景颜色。'
        '下面的例子显示了 $BACKGROUND$ 和 $TEXTCOLOR$ 命令的作用。')

EmbeddedCode(
    """
data=  [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]
t=Table(data)
t.setStyle(TableStyle([('BACKGROUND',(1,1),(-2,-2),colors.green),
                        ('TEXTCOLOR',(0,0),(1,-1),colors.red)]))
"""
)
disc(
    """To see the effects of the alignment styles we need  some widths
and a grid, but it should be easy to see where the styles come from."""
)
cn_disc('为了看到对齐样式的效果，我们需要一些宽度和网格，但应该很容易看到样式的来源。')

EmbeddedCode(
    """
data=  [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]
t=Table(data,5*[0.4*inch], 4*[0.4*inch])
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

# heading3("""$TableStyle$ Line Commands""")
cn_heading3('$TableStyle$ 行的命令集')

disc(
    """
Line commands begin with the identifier, the start and stop cell coordinates
and always follow this with the thickness (in points) and color of the desired lines. Colors can be names,
or they can be specified as a (R, G, B) tuple, where R, G and B are floats and (0, 0, 0) is black. The line
command names are: GRID, BOX, OUTLINE, INNERGRID, LINEBELOW, LINEABOVE, LINEBEFORE
and LINEAFTER. BOX and OUTLINE are equivalent, and GRID is the equivalent of applying both BOX and
INNERGRID.
"""
)
cn_disc('线条命令以标识符、起始和终止单元格坐标开始，'
        '并始终以所需线条的厚度（以点为单位）和颜色跟随。'
        '颜色可以是名称，也可以指定为(R, G, B)元组，'
        '其中R, G和B是浮动数，(0, 0, 0)是黑色。'
        '行命令名称为 GRID, BOX, OUTLINE, INNERGRID, LINEBELOW, LINEABOVE, '
        'LINEBEFORE 和 LINEAFTER。'
        'BOX和OUTLINE相等，'
        'GRID相当于同时应用 BOX 和 INNERGRID。')

CPage(4.0)

disc('We can see some line commands in action with the following example.')
cn_disc('我们可以通过下面的例子看到一些行命令的作用。')

EmbeddedCode(
    """
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

disc(
    """Line commands cause problems for tables when they split; the following example
shows a table being split in various positions"""
)
cn_disc('行命令在拆分表格时，会给表格带来问题；下面的例子显示了一个表格在不同位置被拆分的情况')

EmbeddedCode(
    """
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
t = getStory()[-1]
getStory().append(Spacer(0, 6))
for s in t.split(4 * inch, 30):
    getStory().append(s)
    getStory().append(Spacer(0, 6))
getStory().append(Spacer(0, 6))
for s in t.split(4 * inch, 36):
    getStory().append(s)
    getStory().append(Spacer(0, 6))

disc("""When unsplit and split at the first or second row.""")
cn_disc('当在第一行或第二行进行拆分和分割时。')


CPage(4.0)

# heading3("""Complex Cell Values""")
cn_heading3('复杂的单元格值')

disc(
    """
As mentioned above we can have complicated cell values including $Paragraphs$, $Images$ and other $Flowables$
or lists of the same. To see this in operation consider the following code and the table it produces.
Note that the $Image$ has a white background which will obscure any background you choose for the cell.
To get better results you should use a transparent background.
"""
)
cn_disc('aaa')

import os, reportlab.platypus

I = 'images/replogo.gif'
EmbeddedCode(
    """
I = Image('%s')
I.drawHeight = 1.25*inch*I.drawHeight / I.drawWidth
I.drawWidth = 1.25*inch
P0 = Paragraph('''
               <b>A pa<font color=red>r</font>a<i>graph</i></b>
               <super><font color=yellow>1</font></super>''',
               styleSheet["BodyText"])
P = Paragraph('''
       <para align=center spaceb=3>The <b>ReportLab Left
       <font color=red>Logo</font></b>
       Image</para>''',
       styleSheet["BodyText"])
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
"""
    % I
)

heading3("""$TableStyle$ Span Commands""")
cn_disc('aaa')

disc(
    """Our $Table$ classes support the concept of spanning, but it isn't specified in the same way
as html. The style specification
"""
)
cn_disc('aaa')

eg(
    """
SPAN, (sc,sr), (ec,er)
"""
)

disc(
    """indicates that the cells in columns $sc$ - $ec$ and rows $sr$ - $er$ should be combined into a super cell
with contents determined by the cell $(sc, sr)$. The other cells should be present, but should contain empty strings
or you may get unexpected results.
"""
)
cn_disc('aaa')

EmbeddedCode(
    """
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

disc(
    """notice that we don't need to be conservative with our $GRID$ command. The spanned cells are not drawn through.
"""
)
cn_disc('aaa')

heading3("""$TableStyle$ Miscellaneous Commands""")
cn_heading3('aaa')

disc(
    """To control $Table$ splitting the $NOSPLIT$ command may be used
The style specification
"""
)
cn_disc('aaa')

eg(
    """
NOSPLIT, (sc,sr), (ec,er)
"""
)
disc(
    """demands that the cells in columns $sc$ - $ec$ and rows $sr$ - $er$ may not be split."""
)
cn_disc('aaa')


heading3("""Special $TableStyle$ Indeces""")
cn_heading3('aaa')

disc(
    """In any style command the first row index may be set to one of the special strings
$'splitlast'$ or $'splitfirst'$ to indicate that the style should be used only for the last row of
a split table, or the first row of a continuation. This allows splitting tables with nicer effects around the split."""
)
cn_disc('aaa')


# heading1("""Programming $Flowables$""")
cn_heading1("编写 $Flowables$")

disc(
    """The following flowables let you conditionally evaluate and execute expressions and statements at wrap time:"""
)
cn_disc('aaa')


heading2("""$DocAssign(self, var, expr, life='forever')$""")
cn_heading2('aaa')

disc("""Assigns a variable of name $var$ to the expression $expr$. E.g.:""")
cn_disc('aaa')


eg(
    """
DocAssign('i',3)
"""
)

heading2("""$DocExec(self, stmt, lifetime='forever')$""")
cn_heading2('aaa')

disc("""Executes the statement $stmt$. E.g.:""")
cn_disc('aaa')


eg(
    """
DocExec('i-=1')
"""
)

heading2(
    """$DocPara(self, expr, format=None, style=None, klass=None, escape=True)$"""
)
cn_disc('aaa')


disc(
    """Creates a paragraph with the value of expr as text.
If format is specified it should use %(__expr__)s for string interpolation
of the expression expr (if any). It may also use %(name)s interpolations
for other variables in the namespace. E.g.:"""
)
cn_disc('aaa')


eg(
    """
DocPara('i',format='The value of i is %(__expr__)d',style=normal)
"""
)

heading2("""$DocAssert(self, cond, format=None)$""")
cn_heading2('aaa')

disc(
    """Raises an $AssertionError$ containing the $format$ string if $cond$ evaluates as $False$."""
)
cn_disc('aaa')


eg(
    """
DocAssert(val, 'val is False')
"""
)

heading2("""$DocIf(self, cond, thenBlock, elseBlock=[])$""")
cn_heading2('aaa')

disc(
    """If $cond$ evaluates as $True$, this flowable is replaced by the $thenBlock$ elsethe $elseBlock$."""
)
cn_disc('aaa')


eg(
    """
DocIf('i>3',Paragraph('The value of i is larger than 3',normal),\\
        Paragraph('The value of i is not larger than 3',normal))
"""
)

heading2("""$DocWhile(self, cond, whileBlock)$""")
cn_heading2('aaa')

disc("""Runs the $whileBlock$ while $cond$ evaluates to $True$. E.g.:""")
cn_disc('aaa')


eg(
    """
DocAssign('i',5)
DocWhile('i',[DocPara('i',format='The value of i is %(__expr__)d',style=normal),DocExec('i-=1')])
"""
)

disc("""This example produces a set of paragraphs of the form:""")
cn_disc('aaa')


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
cn_heading2("其他可用的$Flowables$")
cn_heading2('aaa')

heading2(
    """$Preformatted(text, style, bulletText=None, dedent=0, maxLineLength=None, splitChars=None, newLineChars=None)$"""
)
cn_heading2('aaa')

disc(
    """
Creates a preformatted paragraph which does no wrapping, line splitting or other manipulations.
No $XML$ style tags are taken account of in the text.
If dedent is non zero $dedent$ common leading
spaces will be removed from the front of each line.
"""
)
cn_disc('aaa')

heading3("Defining a maximum line length")
cn_heading3('aaa')

disc(
    """
You can use the property $maxLineLength$ to define a maximum line length. If a line length exceeds this maximum value, the line will be automatically splitted.
"""
)
cn_disc('aaa')

disc(
    """
The line will be split on any single character defined in $splitChars$. If no value is provided for this property, the line will be split on any of the following standard characters: space, colon, full stop, semi-colon, coma, hyphen, forward slash, back slash, left parenthesis, left square bracket and left curly brace
"""
)
cn_disc('aaa')

disc(
    """
Characters can be automatically inserted at the beginning of each line that has been created. You can set the property $newLineChars$ to the characters you want to use.
"""
)
cn_disc('aaa')

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
cn_disc('aaa')

disc(
    """
This is a non rearranging form of the $Paragraph$ class; XML tags are allowed in
$text$ and have the same meanings as for the $Paragraph$ class.
As for $Preformatted$, if dedent is non zero $dedent$ common leading
spaces will be removed from the front of each line.
"""
)
cn_disc('aaa')

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
cn_heading2('aaa')

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
cn_disc('aaa')

I = "../images/lj8100.jpg"
eg(
    """
Image("lj8100.jpg")
""",
    after=0.1,
)

disc("""will display as""")
cn_disc('aaa')

try:
    getStory().append(Image(I))
except:
    disc("""An image should have appeared here.""")

disc("""whereas""")
cn_disc('aaa')

eg(
    """
im = Image("lj8100.jpg", width=2*inch, height=2*inch)
im.hAlign = 'CENTER'
""",
    after=0.1,
)

disc('produces')
cn_disc('aaa')

try:
    im = Image(I, width=2 * inch, height=2 * inch)
    im.hAlign = 'CENTER'
    getStory().append(Image(I, width=2 * inch, height=2 * inch))
except:
    disc("""An image should have appeared here.""")
    cn_disc('aaa')

heading2("""$Spacer(width, height)$""")
cn_heading2('aaa')

disc(
    """This does exactly as would be expected; it adds a certain amount of space into the story.
At present this only works for vertical space.
"""
)
cn_disc('aaa')


CPage(1)
heading2("""$PageBreak()$""")
cn_heading2('aaa')

disc(
    """This $Flowable$ represents a page break. It works by effectively consuming all vertical
space given to it. This is sufficient for a single $Frame$ document, but would only be a
frame break for multiple frames so the $BaseDocTemplate$ mechanism
detects $pageBreaks$ internally and handles them specially.
"""
)
cn_disc('aaa')

CPage(1)
heading2("""$CondPageBreak(height)$""")
cn_heading2('aaa')

disc(
    """This $Flowable$ attempts to force a $Frame$ break if insufficient vertical space remains
in the current $Frame$. It is thus probably wrongly named and should probably be renamed as
$CondFrameBreak$.
"""
)
cn_disc('aaa')

CPage(1)
heading2("""$KeepTogether(flowables)$""")
cn_heading2('aaa')

disc(
    """
This compound $Flowable$ takes a list of $Flowables$ and attempts to keep them in the same $Frame$.
If the total height of the $Flowables$ in the list $flowables$ exceeds the current frame's available
space then all the space is used and a frame break is forced.
"""
)
cn_disc('aaa')

CPage(1)
heading2("""$TableOfContents()$""")
cn_heading2('aaa')

disc(
    """
A table of contents can be generated by using the $TableOfContents$ flowable.

The following steps are needed to add a table of contents to your document:
"""
)
cn_disc('aaa')


disc(
    """Create an instance of $TableOfContents$. Override the level styles (optional) and add the object to the story:"""
)
cn_disc('aaa')


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
cn_disc('aaa')


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
cn_disc('aaa')


disc(
    """Finally you need to use the $multiBuild$ method of the DocTemplate because tables of contents need several passes to be generated:"""
)
cn_disc('aaa')


eg(
    """
doc.multiBuild(story)
"""
)

disc(
    """Below is a simple but working example of a document with a table of contents:"""
)
cn_disc('aaa')


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
cn_heading2('aaa')

disc(
    """
An index can be generated by using the $SimpleIndex$ flowable.

The following steps are needed to add an index to your document:
"""
)
cn_disc('aaa')


disc("""Use the index tag in paragraphs to index terms:""")
cn_disc('aaa')


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
cn_disc('aaa')


eg(
    '''
index = SimpleIndex(dot=' . ', headers=headers)
story.append(index)
'''
)

disc(
    """The parameters which you can pass into the SimpleIndex constructor are explained in the reportlab reference. Now, build the document by using the canvas maker returned by SimpleIndex.getCanvasMaker():"""
)
cn_disc('aaa')


eg(
    """
doc.build(story, canvasmaker=index.getCanvasMaker())
"""
)

disc(
    """To build an index with multiple levels, pass a comma-separated list of items to the item attribute of an index tag:"""
)
cn_disc('aaa')


eg(
    """
<index item="terma,termb,termc" />
<index item="terma,termd" />
"""
)

disc(
    """terma will respresent the top-most level and termc the most specific term. termd and termb will appear in the same level inside terma."""
)
cn_disc('aaa')


disc(
    """If you need to index a term containing a comma, you will need to escape it by doubling it. To avoid the ambiguity of three consecutive commas (an escaped comma followed by a list separator or a list separator followed by an escaped comma?) introduce a space in the right position. Spaces at the beginning or end of terms will be removed."""
)
cn_disc('aaa')


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
cn_disc('aaa')


heading2("""$ListFlowable(),ListItem()$""")
cn_heading2('aaa')

disc(
    """
Use these classes to make ordered and unordered lists.  Lists can be nested.
"""
)
cn_disc('aaa')


disc(
    """
$ListFlowable()$ will create an ordered list, which can contain any flowable.  The class has a number of parameters to change font, colour, size, style and position of list numbers, or of bullets in unordered lists.  The type of numbering can also be set to use lower or upper case letters ('A,B,C' etc.) or Roman numerals (capitals or lowercase) using the bulletType property.  To change the list to an unordered type, set bulletType='bullet'.
"""
)
cn_disc('aaa')


disc(
    """
Items within a $ListFlowable()$ list can be changed from their default appearance by wrapping them in a $ListItem()$ class and setting its properties.
"""
)
cn_disc('aaa')


disc(
    """
The following will create an ordered list, and set the third item to an unordered sublist.
"""
)
cn_disc('aaa')


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
cn_disc('aaa')


heading2("""$BalancedColumns()$""")
cn_heading2('aaa')

disc(
    """Use the $BalancedColumns$ class to make a flowable that splits its content flowables into two or more roughly equal sized columns.
Effectively $n$ frames are synthesized to take the content and the flowable tries to balance the content between them. The created frames
will be split when the total height is too large and the split will maintain the balance. 
"""
)
cn_disc('aaa')

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
