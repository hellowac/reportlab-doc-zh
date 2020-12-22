# Copyright ReportLab Europe Ltd. 2000-2017
# see license.txt for license details
# history https://hg.reportlab.com/hg-public/reportlab/log/tip/docs/userguide
# /ch5_paragraphs.py
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib import colors
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
    cn_parabox,
    parabox2,
    cn_parabox2,
    bullet,
    getStory,
    pencilnote,
    startKeep,
    endKeep,
    caption,
    cn_caption,
    styleSheet,
    cn_styleSheet,
)
from utils.stylesheet import CnParagraphStyle


# begin chapter oon paragraphs
# heading1("Paragraphs")
cn_heading1("文字段落")

disc(
    """
The $reportlab.platypus.Paragraph$ class is one of the most useful of the 
Platypus $Flowables$;
it can format fairly arbitrary text and provides for inline font style and 
colour changes using
an XML style markup. The overall shape of the formatted text can be 
justified, right or left ragged
or centered. The XML markup can even be used to insert greek characters or to 
do subscripts.
"""
)
cn_disc('$reportlab.platypus.Paragraph$类是Platypus $Flowables$中最有用的一个；'
        '它可以格式化相当任意的文本，并提供了使用XML样式标记的内联字体样式和颜色变化。'
        '格式化后的文本的整体形状可以是公正的，左右粗细的，或者居中的。'
        'XML标记甚至可以用来插入希腊字符或做下标。')

disc("""The following text creates an instance of the $Paragraph$ class:""")
cn_disc('下面的文字创建了一个$Paragraph$类的实例。')

eg("""Paragraph(text, style, bulletText=None)""")
disc(
    """The $text$ argument contains the text of the
paragraph; excess white space is removed from the text at the ends and 
internally after
linefeeds. This allows easy use of indented triple quoted text in 
<b>Python</b> scripts.
The $bulletText$ argument provides the text of a default bullet for the 
paragraph.
The font and other properties for the paragraph text and bullet are set using 
the style argument.
"""
)
cn_disc('参数$text$包含了段落的文本；'
        '在文本的结尾和换行后，多余的空白会被删除。'
        '这允许在<b>Python</b>脚本中轻松使用缩进的三引号文本。'
        '$bulletText$参数提供了段落的默认子弹文本。'
        '段落文本和子弹的字体和其他属性可以使用样式参数来设置。')

disc(
    """
    The $style$ argument should be an instance of class $ParagraphStyle$ 
    obtained typically
    using"""
)
cn_disc('参数 $style$ 应该是一个 $ParagraphStyle$ 类的实例，通常使用')

eg(
    """
from reportlab.lib.styles import ParagraphStyle
"""
)
disc(
    """
this container class provides for the setting of multiple default paragraph 
attributes
in a structured way. The styles are arranged in a dictionary style object 
called a $stylesheet$
which allows for the styles to be accessed as $stylesheet['BodyText']$. A 
sample style
sheet is provided.
"""
)
cn_disc('这个容器类以结构化的方式提供了多个默认段落属性的设置。'
        '这些样式被安排在一个名为$stylesheet$的字典样式对象中，'
        '它允许以$stylesheet[\'BodyText\']$的形式访问这些样式。'
        '我们提供了一个示例样式表。')

eg(
    """
from reportlab.lib.styles import getSampleStyleSheet
stylesheet=getSampleStyleSheet()
normalStyle = stylesheet['Normal']
"""
)
disc(
    """
The options which can be set for a $Paragraph$ can be seen from the 
$ParagraphStyle$ defaults. The values with leading underscore ('_') are 
derived from the defaults in module $reportlab.rl_config$ which are derived from
module $reportlab.rl_settings$.
"""
)
cn_disc('可以为$Paragraph$设置的选项可以从$ParagraphStyle$默认值中看出。'
        '前面带下划线(\'_\')的值来自于 '
        '$reportlab.rl_config$ 模块中的默认值，'
        '这些值来自于$reportlab.rl_settings$模块。')

heading4("$class ParagraphStyle$")
cn_heading4('类 $ParagraphStyle$$')

eg(
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
        'underlineOffset': _baseUnderlineOffset,    #fraction of fontsize to 
        offset underlines
        'underlineGap': _baseUnderlineGap,      #gap for double/triple underline
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

# heading2("Using Paragraph Styles")
cn_heading2('使用文字段落样式')

# this will be used in the ParaBox demos.
sample = """You are hereby charged that on the 28th day of May, 1970, you did
willfully, unlawfully, and with malice of forethought, publish an
alleged English-Hungarian phrase book with intent to cause a breach
of the peace.  How do you plead?"""
cn_sample = ('你在此被指控在1970年5月28日， 你故意，非法，并与恶意的预想， '
             '出版一个所谓的英语 - 匈牙利短语书，意图造成破坏和平。 '
             '你如何辩护？')

disc(
    """The $Paragraph$ and $ParagraphStyle$ classes together
handle most common formatting needs. The following examples
draw paragraphs in various styles, and add a bounding box
so that you can see exactly what space is taken up."""
)
cn_disc('$Paragraph$和$ParagraphStyle$类一起处理大多数常见的格式化需求。'
        '下面的示例以不同的样式绘制段落，并添加了一个边界框，'
        '这样你就可以看到确切的空间被占用了。')

# s1 = ParagraphStyle('Normal')
# parabox(sample, s1, 'The default $ParagraphStyle$')

cn_s1 = CnParagraphStyle('Normal')  # ParagraphStyle('Normal')
cn_parabox(cn_sample, cn_s1, '默认 $ParagraphStyle$')

disc(
    """The two attributes $spaceBefore$ and $spaceAfter$ do what they
say, except at the top or bottom of a frame. At the top of a frame,
$spaceBefore$ is ignored, and at the bottom, $spaceAfter$ is ignored.
This means that you could specify that a 'Heading2' style had two
inches of space before when it occurs in mid-page, but will not
get acres of whitespace at the top of a page.  These two attributes
should be thought of as 'requests' to the Frame and are not part
of the space occupied by the Paragraph itself."""
)
cn_disc('$spaceBefore$和$spaceAfter$这两个属性如它们所说的那样，'
        '除了在一个框架的顶部或底部。'
        '在一个框架的顶部，$spaceBefore$被忽略，而在底部，$spaceAfter$被忽略。'
        '这意味着你可以指定一个\'Heading2\'样式在页面中间出现时，'
        '它之前有两英寸的空间，但不会在页面顶部得到数英亩的空白。 '
        '这两个属性应该被认为是对Frame的 "请求"，'
        '而不是段落本身所占空间的一部分。')

disc(
    """The $fontSize$ and $fontName$ tags are obvious, but it is
important to set the $leading$.  This is the spacing between
adjacent lines of text; a good rule of thumb is to make this
20% larger than the point size.  To get double-spaced text,
use a high $leading$. If you set $autoLeading$(default $"off"$) to $"min"$(
use observed leading even if smaller than specified) or $"max"$(use the 
larger of observed and specified) then an attempt is made to determine the 
leading
on a line by line basis. This may be useful if the lines contain different 
font sizes etc."""
)
cn_disc('$fontSize$和$fontName$标签是显而易见的，'
        '但重要的是设置$leading$。 '
        '这是相邻文本行之间的间距；'
        '一个好的经验法则是让这个间距比点的大小大 20%。 '
        '要获得双倍行距的文本，请使用较高的$leading$。'
        '如果您将$autoLeading$(默认为$"off"$)'
        '设置为$"min"$(使用观察到的前导，即使比指定的小)'
        '或$"max"$(使用观察到的和指定的较大值)'
        '，那么就会尝试逐行确定前导。'
        '如果行中包含不同的字体大小等，'
        '这可能是有用的。')

disc(
    """The figure below shows space before and after and an
increased leading:"""
)
cn_disc('下图为前后空间和增加的引导。')

# parabox(
#     sample,
#     ParagraphStyle('Spaced', spaceBefore=6, spaceAfter=6, leading=16),
#     'Space before and after and increased leading',
# )
cn_parabox(
    cn_sample,
    CnParagraphStyle('Spaced', spaceBefore=6, spaceAfter=6, leading=16),
    '前后空间和增加 leading',
)

disc(
    """The attribute $borderPadding$ adjusts the padding between the 
    paragraph and the border of its background.
This can either be a single value or a tuple containing 2 to 4 values.
These values are applied the same way as in Cascading Style Sheets (CSS).
If a single value is given, that value is applied to all four sides.
If more than one value is given, they are applied in clockwise order to the 
sides starting at the top.
If two or three values are given, the missing values are taken from the 
opposite side(s).
Note that in the following example the yellow box is drawn by the paragraph 
itself."""
)
cn_disc('属性 $borderPadding$ 调整段落与背景边框之间的 $padding$ 。'
        '它可以是一个单一的值，也可以是一个包含2到4个值的元组。'
        '这些值的应用方式与层叠样式表（CSS）相同。'
        '如果给定一个值，该值将应用于所有四条边框。'
        '如果给了一个以上的值，则从顶部开始按顺时针顺序应用到边上。'
        '如果给了两个或三个值，则缺失的值将从相反的边开始应用。'
        '请注意，在下面的例子中，黄色方框是由段落本身绘制的。')

# parabox(
#     sample,
#     ParagraphStyle(
#         'padded',
#         borderPadding=(7, 2, 20),
#         borderColor='#000000',
#         borderWidth=1,
#         backColor='#FFFF00',
#     ),
#     'Variable padding',
# )
cn_parabox(cn_sample, CnParagraphStyle(
    'padded',
    borderPadding=(7, 2, 20),
    borderColor='#000000',
    borderWidth=1,
    backColor='#FFFF00', ),
           '可变 $padding$',
           )

disc(
    """The $leftIndent$ and $rightIndent$ attributes do exactly
what you would expect; $firstLineIndent$ is added to the $leftIndent$ of the
first line. If you want a straight left edge, remember
to set $firstLineIndent$ equal to 0."""
)
cn_disc('$leftIndent$ 和 $rightIndent$ 属性的作用正是你所期望的；'
        '$firstLineIndent$ 被添加到第一行的 $leftIndent$ 中。'
        '如果你想要一个笔直的左边缘，记得将$firstLineIndent$等于0。')

# parabox(
#     sample,
#     ParagraphStyle(
#         'indented', firstLineIndent=+24, leftIndent=24, rightIndent=24
#     ),
#     'one third inch indents at left and right, two thirds on first line',
# )
cn_parabox(
    cn_sample,
    CnParagraphStyle(
        'indented', firstLineIndent=+24, leftIndent=24, rightIndent=24
    ),
    '左右缩进三分一，首行缩进三分二',
)

disc(
    """Setting $firstLineIndent$ equal to a negative number, $leftIndent$
much higher, and using a
different font (we'll show you how later!) can give you a
definition list:."""
)
cn_disc('将$firstLineIndent$设置为负数，'
        '$leftIndent$则高得多，'
        '并使用不同的字体（我们稍后会告诉你怎么做！）'
        '可以给你一个定义列表：')

# parabox(
#     '<b><i>Judge Pickles: </i></b>' + sample,
#     ParagraphStyle('dl', leftIndent=36),
#     'Definition Lists',
# )
cn_parabox(
    '<b><i>皮克尔斯法官: </i></b>' + cn_sample,
    CnParagraphStyle('dl', leftIndent=36),
    '定义列表',
)

disc(
    """There are four possible values of $alignment$, defined as
constants in the module <i>reportlab.lib.enums</i>.  These are
TA_LEFT, TA_CENTER or TA_CENTRE, TA_RIGHT and
TA_JUSTIFY, with values of 0, 1, 2 and 4 respectively.  These
do exactly what you would expect."""
)
cn_disc('在模块<i>reportlab.lib.enums</i>中，'
        '$alignment$有四个可能的值，定义为常量。 '
        '这些值是 $TA_LEFT$, $TA_CENTER$ 或 $TA_CENTRE$, $TA_RIGHT$ 和 $TA_JUSTIFY$ ，'
        '值分别为0, 1, 2和4。 这些都和你所期望的一样。')

disc(
    """Set $wordWrap$ to $'CJK'$ to get Asian language linewrapping. For 
    normal western text you can change the way
the line breaking algorithm handles <i>widows</i> and <i>orphans</i> with the 
$allowWidows$ and $allowOrphans$ values.
Both should normally be set to $0$, but for historical reasons we have 
allowed <i>widows</i>.
The default color of the text can be set with $textColor$ and the paragraph 
background
colour can be set with $backColor$. The paragraph's border properties may be 
changed using
$borderWidth$, $borderPadding$, $borderColor$ and $borderRadius$."""
)
cn_disc('将 $wordWrap$ 设置为 $\'CJK\'$ 来获得亚洲语言的换行。'
        '对于普通的西方文本，'
        '你可以通过$allowWidows$和$allowOrphans$'
        '来改变断行算法处理<i>widows</i>和<i>orphans</i>的方式。'
        '这两个值通常都应该设置为$0$，'
        '但由于历史原因，我们允许<i>widows</i>。'
        '文本的默认颜色可以用$textColor$设置，'
        '段落的背景颜色可以用$backColor$设置。'
        '段落的边框属性可以使用$borderWidth$, '
        '$borderPadding$, $borderColor$和$borderRadius$来改变。')

disc(
    """The $textTransform$ attribute can be <b><i>None</i></b>, 
    <i>'uppercase'</i> or <i>'lowercase'</i> to get the obvious result and 
    <i>'capitalize'</i> to get initial letter capitalization."""
)
cn_disc('$textTransform$属性可以是'
        '<b><i>None</i></b>，'
        '<i>$uppercase$</i>或'
        '<i>$lowercase$</i>'
        '得到明显的结果，'
        '<i>$capitalize$</i>'
        '得到初始字母大写。')

disc(
    """Attribute $endDots$ can be <b><i>None</i></b>, a string, or an object 
    with attributes text and optional fontName, fontSize, textColor,  backColor
and dy(y offset) to specify trailing matter on the last line of left/right 
justified paragraphs."""
)
cn_disc('属性$endDots$可以是'
        '<b><i>None</i></b>，'
        '一个字符串，或者一个对象，'
        '其属性为 $text$ 和可选的 $fontName、fontSize、textColor、backColor$ '
        '和 $dy(y offset)$ ，用于指定左/右对齐段落最后一行的尾部内容。')

disc(
    """The $splitLongWords$ attribute can be set to a false value to avoid 
    splitting very long words."""
)
cn_disc('$splitLongWords$属性可以设置为假值，以避免拆分非常长的单词。')

disc(
    """Attribute $bulletAnchor$ can be <i>'start'</i>, <i>'middle'</i>, 
    <i>'end'</i> or <i>'numeric'</i> to control where the bullet is anchored."""
)
cn_disc("属性 $bulletAnchor$ 可以是"
        "<i>'start'</i>, "
        "<i>'middle'</i>, "
        "<i>'end'</i> 或 "
        "<i>'numeric'</i>"
        "来控制子弹的锚定位置。")

disc(
    """The $justifyBreaks$ attribute controls whether lines deliberately 
    broken with a $&lt;br/&gt;$ tag should be justified"""
)
cn_disc('$justifyBreaks$ 属性'
        '控制了是否应该用 $&lt;br/&gt;$ 标签故意断行。')

disc(
    """Attribute $spaceShrinkage$ is a fractional number specifiying by how 
    much the space of a paragraph
line may be shrunk in order to make it fit; typically it is something like 
0.05"""
)
cn_disc('属性 $spaceShrinkage$ 是一个小数，指定段落行的空间可以缩小多少以使其合适；通常是0.05左右。')

disc(
    """The $underlineWidth$, $underlineOffset$, $underlineGap$ &amp; 
    $underlineColor$ attributes control the underline behaviour when the 
    $&lt;u&gt;$ or
a linking tag is used. Those tags can have override values of these 
attributes. The attribute value  for width &amp; offset
is a $fraction * Letter$ where letter can be one of $P$, $L$, $f$ or $F$ 
representing fontSize proportions. $P$ uses the fontsize at the tag, $F$ is 
the maximum fontSize in the tag, $f$ is the initial fontsize inside the tag.
$L$ means the global (paragrpah style) font size. $strikeWidth$, 
$strikeOffset$, $strikeGap$ &amp; $strikeColor$ attributes do the same for 
strikethrough lines.
"""
)
cn_disc('当使用 $&lt;u&gt;$ 或链接标签时，$underlineWidth$、$underlineOffset$'
        '、$underlineGap$ 和 $underlineColor$属性控制了下划线行为。'
        '这些标签可以有这些属性的覆盖值。'
        '$width$ 和 $offset$ 的属性值是一个 $fraction * Letter$，'
        '其中letter可以是 $P$、$L$、$f$ 或 $F$ 中的一个，代表字体大小比例。'
        '$P$ 使用标签处的字体大小，'
        '$F$ 是标签中的最大字体大小，'
        '$f$ 是标签内的初始字体大小。'
        '$L$ 表示全局（$ParagraphStyle$）字体大小。'
        '$strikeWidth$, $strikeOffset$, '
        '$strikeGap$ 和 $strikeColor$属性对删除线有同样的作用。')

disc(
    """Attribute $linkUnderline$ controls whether link tags are automatically 
    underlined."""
)
cn_disc('属性 $linkUnderline$ 控制链接标签是否自动下划线。')

disc(
    """If the $pyphen$ python module is installed attribute $hyphenationLang$ 
    controls which language will be used to hyphenate words without explicit 
    embedded hyphens."""
)
cn_disc('如果安装了$pyphen$ python模块，'
        '则属性 $hyphenationLang$ 控制'
        '哪种语言将被用于在没有明确嵌入连字符的情况下连字符。')

disc(
    """If $embeddedHyphenation$ is set then attempts will be made to split 
    words with embedded hyphens."""
)
cn_disc('如果设置了 $embeddedHyphenation$，那么就会尝试拆分带有嵌入式连字符的单词。')

disc(
    """Attribute $uriWasteReduce$ controls how we attempt to split long 
    uri's. It is the fraction of a line that we regard as too much waste. The 
    default in module
$reportlab.rl_settings$ is <i>0.5</i> which means that we will try and split 
a word that looks like a uri if we would waste at least half of the line."""
)
cn_disc('属性 $uriWasteReduce$ '
        '控制我们如何尝试分割长的 $uri$。'
        '它是我们认为太过浪费的行的分数，'
        '在模块 $reportlab.rl_settings$ 中的默认值是<i>0.5</i>。'
        '这意味着如果我们将浪费至少一半的行数，我们将尝试拆分一个看起来像uri的单词。')

disc(
    """Currently the hyphenation and uri splitting are turned off by default. 
    You need to modify the default settings by using the file 
    $~/.rl_settings$ or adding a module $reportlab_settings.py$ to the python 
    path. Suitable values are"""
)
cn_disc('目前，连字符 和 $uri$ 分割是默认关闭的。'
        '您需要通过使用 $~/.rl_settings$ 文件'
        '或在 python 路径中添加 $reportlab_settings.py$ 模块'
        '来修改默认设置。合适的值是')

eg(
    """
    hyphenationLanguage='en_GB'
    embeddedHyphenation=1
    uriWasteReduce=0.3
    """
)

# heading2("Paragraph XML Markup Tags")
cn_heading2('文本段落XML标记标签')

disc(
    """XML markup can be used to modify or specify the overall paragraph 
style, and also to specify intra-paragraph markup."""
)
cn_disc('XML标记可以用来修改或指定整体段落样式，也可以指定段落内的标记。')

# heading3("The outermost &lt; para &gt; tag")
cn_heading3('最外层 &lt; para &gt; 标签')

disc(
    """
The paragraph text may optionally be surrounded by
&lt;para attributes....&gt;
&lt;/para&gt;
tags. The attributes if any of the opening &lt;para&gt; tag affect the style 
that is used
with the $Paragraph$ $text$ and/or $bulletText$.
"""
)
cn_disc('段落文本可以选择由 '
        '&lt;para attributes....&gt; &lt;/para&gt; 标签包围。'
        '开头的 &lt;para&gt; 标签的任何属性'
        '都会影响 $Paragraph$ $text$ 和/或 $bulletText$'
        '所使用的样式。')

disc(" ")

from reportlab.platypus.paraparser import (
    _addAttributeNames,
    _paraAttrMap,
    _bulletAttrMap,
)


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
    D = [('Attribute', 'Synonyms')]
    for k in K:
        D.append((k, ", ".join(list(sorted(S[k])))))
    cols = 2 * [None]
    rows = len(D) * [None]
    return D, cols, rows


t = Table(*getAttrs(_paraAttrMap))
t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 1), 'Times-Bold', 10, 12),
            ('FONT', (0, 1), (-1, -1), 'Courier', 8, 8),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)

# getStory().append(t)
# caption(
#     """Table <seq template="%(Chapter)s-%(Table+)s"/> - Synonyms for style
#     attributes"""
# )

def cn_getAttrs(A):
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


cn_t = Table(*cn_getAttrs(_paraAttrMap))
cn_t.setStyle(
    TableStyle(
        [
            ('FONT', (0, 0), (-1, 1), 'STSong-Light', 10, 12),
            ('FONT', (0, 1), (-1, -1), 'Courier', 8, 8),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]
    )
)
getStory().append(cn_t)
cn_caption('表 <seq template="%(Chapter)s-%(Table+)s"/> - 样式属性的同义词')

disc(
    """Some useful synonyms have been provided for our Python attribute
names, including lowercase versions, and the equivalent properties
from the HTML standard where they exist.  These additions make
it much easier to build XML-printing applications, since
much intra-paragraph markup may not need translating. The
table below shows the allowed attributes and synonyms in the
outermost paragraph tag."""
)
cn_disc('我们为我们的 Python 属性名提供了一些有用的同义词，'
        '包括小写版本，以及 HTML 标准中存在的等价属性。 '
        '这些增加的内容使构建 XML 打印应用程序变得更加容易，'
        '因为许多段内标记可能不需要翻译。'
        '下表显示了最外层段落标签中允许的属性和同义词。')

CPage(1)
# heading2("Intra-paragraph markup")
cn_heading2("段内标记")

disc(
    """&lt;![CDATA[Within each paragraph, we use a basic set of XML tags
to provide markup.  The most basic of these are bold (&lt;b&gt;...&lt;/b&gt;),
italic (&lt;i&gt;...&lt;/i&gt;) and underline (&lt;u&gt;...&lt;/u&gt;).
Other tags which are allowed are strong (&lt;strong&gt;...&lt;/strong&gt;), 
and strike through (&lt;strike&gt;...&lt;/strike&gt;). The &lt;link&gt; and 
&lt;a&gt; tags
may be used to refer to URIs, documents or bookmarks in the current document. 
The a variant of the &lt;a&gt; tag can be used to
mark a position in a document. A break (&lt;br/&gt;) tag is also allowed.]]&gt;
"""
)
cn_disc('&lt;！[CDATA[ '
        '在每个段落中，我们使用一组基本的XML标签来提供标记。 '
        '其中最基本的是粗体 (&lt;b&gt;...&lt;/b&gt;)、'
        '斜体 (&lt;i&gt;...&lt;/i&gt;) 和'
        '下划线 (&lt;u&gt;...&lt;/u&gt;)。'
        '其他允許的标签有强调 (&lt;strong&gt;..&lt;/strong&gt;)，'
        '和删除线 (&lt;strike&gt;...&lt;/strike&gt;)。'
        '&lt;link&gt;和&lt;a&gt;标签可用于引用当前文档中的URI、文档或书签。'
        '&lt;a&gt; 标签的 $a$ 变体可用于标记文档中的一个位置。'
        '也允许使用 $break$ (&lt;br/&gt;)标签。]]&gt;。')

# parabox2(
#     """<b>You are hereby charged</b> that on the 28th day of May, 1970,
#     you did
# willfully, unlawfully, and <i>with malice of forethought</i>, publish an
# alleged English-Hungarian phrase book with intent to cause a breach
# of the peace.  <u>How do you plead</u>?""",
#     "Simple bold and italic tags",
# )
cn_parabox2("<b>兹指控</b> 你于1970年5月28日故意、非法和恶意地预谋出版一本所谓的英匈短语书，"
            "意图破坏和平。 <u>你如何辩护</u>？", '简单的黑体和斜体标签')

# parabox2("""This <a href="#MYANCHOR" color="blue">is a link to</a> an anchor
# tag ie <a name="MYANCHOR"/><font color="green">here</font>.
# This <link href="#MYANCHOR" color="blue" fontName="Helvetica">is another link
# to</link> the same anchor tag.""",
#     "anchors and links",
# )

cn_parabox2('这是一个锚标签的<a href="#MYANCHOR" color="blue">链接</a>，'
            '即<a name="MYANCHOR"/><font color="green">这里</font>。'
            '这是另一个指向同一锚标签的'
            '<link href="#MYANCHOR" color="blue" fontName="STSong-Light">'
            '链接</link>。', '锚和链接')

disc(
    """The <b>link</b> tag can be used as a reference, but
not as an anchor. The a and link hyperlink tags have additional attributes 
<i>fontName</i>, <i>fontSize</i>, <i>color</i> &amp; <i>backColor</i> 
attributes. The hyperlink reference can have a scheme of <b>http:</b><i>(
external webpage)</i>, <b>pdf:</b><i>(different pdf document)</i> or 
<b>document:</b><i>(same pdf document)</i>; a missing scheme is treated as 
<b>document</b> as is the case when the reference starts with # (in which 
case the anchor should omit it). Any other scheme is treated as some kind of URI.
"""
)
cn_disc('<b>link</b>标签可以用作参考，但不能用作锚。'
        'a 和 $link$ 超链接标签有附加属性'
        '<i>fontName</i>、<i>fontSize</i>、<i>color</i> '
        '和 <i>backColor</i>属性。'
        '超链接引用可以有<b>http:</b><i>（外部网页）</i>、'
        '<b>pdf:</b>'
        '<i>（不同的pdf文档）</i>或'
        '<b>document:</b>'
        '<i>（相同的pdf文档）</i>等方案；'
        '缺少的方案将被视为<b>document</b>，'
        '就像引用以#开头时的情况一样（在这种情况下，锚应该省略它）。'
        '任何其他方案都会被视为某种URI。')

# parabox2(
#     """<strong>You are hereby charged</strong> that on the 28th day of May,
#     1970, you did
# willfully, unlawfully, <strike>and with malice of forethought</strike>,
# <br/>publish an
# alleged English-Hungarian phrase book with intent to cause a breach
# of the peace. How do you plead?""",
#     "Strong, strike, and break tags",
# )
cn_parabox2(
    '<strong>兹指控你</strong>于1970年5月28日故意、非法和'
    '<strike>恶意地预谋</strike><br/>出版一本所谓的英匈短语书，'
    '你怎么辩解？', "强调, 删除线, 和换行标签")

# heading3("The $&lt;font&gt;$ tag")
cn_heading3('$&lt;font&gt;$ 标签')

disc(
    """The $&lt;font&gt;$ tag can be used to change the font name,
size and text color for any substring within the paragraph.
Legal attributes are $size$, $face$, $name$ (which is the same as $face$),
$color$, and $fg$ (which is the same as $color$). The $name$ is
the font family name, without any 'bold' or 'italic' suffixes.
Colors may be HTML color names or a hex string encoded in a variety of ways; 
see ^reportlab.lib.colors^ for the formats allowed.""")
cn_disc("$&lt;font&gt;$标签可以用来改变段落中任何子串的字体名称、大小和文本颜色。"
        "法定属性有$size$、$face$、$name$（与$face$相同）、$color$和$fg$（与$color$相同）。"
        "$name$是字体家族的名称，没有任何'bold'或'italic'的后缀。"
        "颜色可以是HTML的颜色名称，也可以是以各种方式编码的十六进制字符串；"
        "请参见^reportlab.lib. colors^了解允许的格式。")

# parabox2(
#     """<font face="times" color="red">You are hereby charged</font> that on
# the 28th day of May, 1970, you did willfully, unlawfully, and <font
# size=14>with malice of forethought</font>, publish an alleged
# English-Hungarian phrase book with intent to cause a breach
# of the peace.  How do you plead?""",
#     "The $font$ tag",
# )
cn_parabox2('你在此<font face="STSong-Light" '
            'color="red">被控</font>于1970年5月28日故意、非法和'
            '<font size=16>怀着预谋的恶意</font>出版一本所谓的英匈短语书，意图破坏和平。'
            ' 你如何辩护？', "$font$ 标签")

# heading3("Superscripts and Subscripts")
cn_heading3('上标和下标')

disc(
    """Superscripts and subscripts are supported with the
&lt;![CDATA[&lt;super&gt;/&lt;sup&gt; and &lt;sub&gt; tags, which work exactly
as you might expect. Additionally these three tags have
attributes rise and size to optionally set the rise/descent
and font size for the  superscript/subscript text.
In addition, most greek letters
can be accessed by using the &lt;greek&gt;&lt;/greek&gt;
tag, or with mathML entity names.]]&gt;"""
)
cn_disc('上标和下标是由&lt;![CDATA[&lt;super&gt;/&lt;sup&gt;和&lt;sub&gt;标签支持的，'
        '它们的工作原理和你所期望的完全一样。'
        '另外这三个标签还有属性 rise 和 size，可以选择设置上标/下标文本的上升/下降和字体大小。'
        '此外，大多数希腊字母可以通过使用&lt;greek&gt;&lt;/greek&gt;标签，'
        '或者使用mathML实体名来访问。]]&gt。')

##parabox2("""<greek>epsilon</greek><super><greek>iota</greek>
##<greek>pi</greek></super> = -1""", "Greek letters and subscripts")

parabox2(
    """Equation (&alpha;): <greek>e</greek> <super rise=9 
    size=6><greek>ip</greek></super>  = -1""",
    "Greek letters and superscripts",
)
cn_parabox2('等式（&alpha;）。<greek>e</greek> <super rise=9 size=6><greek>ip</greek></super>=-1。', '希腊字母和上标')

# heading3("Inline Images")
cn_heading3('内联图片')

disc(
    """We can embed images in a paragraph with the 
&lt;img/&gt; tag which has attributes $src$, $width$, $height$ whose meanings 
are obvious. The $valign$ attribute may be set to a css like value from
"baseline", "sub", "super", "top", "text-top", "middle", "bottom", 
"text-bottom"; the value may also be a numeric percentage or an absolute value.
"""
)
cn_disc('我们可以用&lt;img/&gt;标签在段落中嵌入图片，'
        '该标签有$src$、$width$、$height$等属性，其含义很明显。'
        '$valign$属性可以设置为类似css的值，'
        '从 "baseline"、"sub"、"super"、"top"、"text-top"、"middle"、"bottom"、"text-bottom"；'
        '该值也可以是一个数字百分比或绝对值。')

# parabox2(
#     """<para autoLeading="off" fontSize=12>This &lt;img/&gt; <img
#     src="images/testimg.gif" valign="top"/> is aligned <b>top</b>.<br/><br/>
# This &lt;img/&gt; <img src="images/testimg.gif" valign="bottom"/> is aligned
# <b>bottom</b>.<br/><br/>
# This &lt;img/&gt; <img src="images/testimg.gif" valign="middle"/> is aligned
# <b>middle</b>.<br/><br/>
# This &lt;img/&gt; <img src="images/testimg.gif" valign="-4"/> is aligned
# <b>-4</b>.<br/><br/>
# This &lt;img/&gt; <img src="images/testimg.gif" valign="+4"/> is aligned
# <b>+4</b>.<br/><br/>
# This &lt;img/&gt; <img src="images/testimg.gif" width="10"/> has width
# <b>10</b>.<br/><br/>
# </para>""",
#     "Inline images",
# )
cn_parabox2('<para autoLeading="off" fontSize=12>This &lt;img/&gt; '
            '<img src="images/testimg.gif" valign="top"/> is aligned <b>top</b>.'
            '<br/><br/>This &lt;img/&gt; '
            '<img src="images/testimg.gif" valign="bottom"/> is aligned <b>bottom</b>.'
            '<br/><br/> This &lt;img/&gt; '
            '<img src="images/testimg.gif" valign="middle"/> is aligned <b>middle</b>.'
            '<br/><br/>This &lt;img/&gt; '
            '<img src="images/testimg.gif" valign="-4"/> is aligned <b>-4</b>.'
            '<br/><br/>This &lt;img/&gt; '
            '<img src="images/testimg.gif" valign="+4"/> is aligned <b>+4</b>.'
            '<br/><br/>This &lt;img/&gt; '
            '<img src="images/testimg.gif" width="10"/> has width<b>10</b>.'
            '<br/><br/></para>', '内联图片')

disc(
    """The $src$ attribute can refer to a remote location eg 
$src="https://www.reportlab.com/images/logo.gif"$. By default we set 
$rl_config.trustedShemes$ to $['https','http', 'file', 'data', 'ftp']$ and
$rl_config.trustedHosts=None$ the latter meaning no-restriction. You can 
modify these variables using one of the override files eg 
$reportlab_settings.py$ or $~/.reportlab_settings$. Or as comma separated 
strings in the 
environment variables $RL_trustedSchemes$ &amp; $RL_trustedHosts$. Note that 
the $trustedHosts$ values may contain <b>glob</b> wild cars so 
<i>*.reportlab.com</i> will match the obvious domains.
<br/><span color="red"><b>*NB*</b></span> use of <i>trustedHosts</i> and or 
<i>trustedSchemes</i> may not control behaviour &amp; actions when $URI$ 
patterns are detected by the viewer application."""
)
cn_disc("$src$属性可以指向一个远程位置，"
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
        "使用<i>trustedHosts</i>和/或<i>trustedSchemes</i>"
        "可能无法控制行为，以及当$URI$模式被查看器应用程序检测到时的操作。")

# heading3("The $&lt;u&gt;$ &amp; $&lt;strike&gt;$ tags")
cn_heading3('$&lt;u&gt;$ 和 $&lt;strike&gt;$ 标签')

disc(
    """These tags can be used to carry out explicit underlineing or 
strikethroughs. These tags have attributes $width$, $offset$, $color$, 
$gap$ &amp; $kind$. The $kind$ attribute controls how many
lines will be drawn (default $kind=1$) and when $kind>1$ the $gap$ attribute 
controls the disatnce between lines."""
)
cn_disc('这些标签可用于执行明确的下划线或删除线。'
        '这些标签的属性有$width$、$offset$、$color$、$gap$ 和 $kind$。'
        '$kind$属性控制将绘制多少行(默认$kind=1$)，当$kind>1$时，'
        '$gap$属性控制行与行之间的间隔。')

# heading3("The $&lt;nobr&gt;$ tag")
cn_heading3('$&lt;nobr&gt;$ 标签')

disc(
    """If hyphenation is in operation the $&lt;nobr&gt;$ tag suppresses it so 
    $&lt;nobr&gt;averylongwordthatwontbebroken&lt;/nobr&gt;$ won't be broken."""
)
cn_disc('如果使用连字符，$&lt;nobr&gt;$标签会抑制它，'
        '所以$&lt;nobr&gt;一个非常长的单词不会被打断&lt;/nobr&gt;$不会被打断。')

# heading3("Numbering Paragraphs and Lists")
cn_heading3('文字段落和列表的编号')

disc(
    """The $&lt;seq&gt;$ tag provides comprehensive support
for numbering lists, chapter headings and so on.  It acts as
an interface to the $Sequencer$ class in ^reportlab.lib.sequencer^.
These are used to number headings and figures throughout this document.
You may create as many separate 'counters' as you wish, accessed
with the $id$ attribute; these will be incremented by one each
time they are accessed.  The $seqreset$ tag resets a counter.
If you want it to resume from a number other than 1, use
the syntax &lt;seqreset id="mycounter" base="42"&gt;.
Let's have a go:"""
)
cn_disc('$&lt;seq&gt;$标签为编号列表、章节标题等提供了全面的支持，'
        '它作为^reportlab.lib.sequencer^中$Sequencer$类的接口。 '
        '它是^reportlab.lib.sequencer^中$Sequencer$类的接口。'
        '这些都是用来对整个文档中的标题和数字进行编号的。'
        '您可以创建任意多的独立的 "计数器"，并通过$id$属性进行访问；'
        '每次访问时，这些计数器都将以1为单位递增。 '
        '$seqreset$标签可以重置计数器。'
        '如果你想让它从1以外的数字开始恢复，'
        '使用语法&lt;seqreset id="mycounter" base="42"&gt;。'
        '让我们开始吧。')

# parabox2(
#     """<seq id="spam"/>, <seq id="spam"/>, <seq id="spam"/>.
# Reset<seqreset id="spam"/>.  <seq id="spam"/>, <seq id="spam"/>,
# <seq id="spam"/>.""",
#     "Basic sequences",
# )
cn_parabox2('<seq id="spam"/>, '
            '<seq id="spam"/>, '
            '<seq id="spam"/>. 重置'
            '<seqreset id="spam"/>.  '
            '<seq id="spam"/>, '
            '<seq id="spam"/>,'
            '<seq id="spam"/>.', '基本序列')

disc(
    """You can save specifying an ID by designating a counter ID
as the <i>default</i> using the &lt;seqdefault id="Counter"&gt;
tag; it will then be used whenever a counter ID
is not specified.  This saves some typing, especially when
doing multi-level lists; you just change counter ID when
stepping in or out a level."""
)
cn_disc('你可以通过使用&lt;seqdefault id="Counter"&gt; 标签'
        '指定一个计数器ID作为<i>default</i>来节省指定ID的时间；'
        '然后每当没有指定计数器ID时就会使用它。 '
        '这样可以节省一些输入，特别是在做多级列表的时候；'
        '您只需在进入或退出一个级别时更改计数器ID。')

parabox2(
    """<seqdefault id="spam"/>Continued... <seq/>,
<seq/>, <seq/>, <seq/>, <seq/>, <seq/>, <seq/>.""",
    "The default sequence",
)
cn_parabox2('<seqdefault id="spam"/>Continued... <seq/>,'
            '<seq/>, <seq/>, <seq/>, <seq/>, <seq/>, <seq/>.', '默认序列')

disc(
    """Finally, one can access multi-level sequences using
a variation of Python string formatting and the $template$
attribute in a &lt;seq&gt; tags.  This is used to do the
captions in all of the figures, as well as the level two
headings.  The substring $%(counter)s$ extracts the current
value of a counter without incrementing it; appending a
plus sign as in $%(counter)s$ increments the counter.
The figure captions use a pattern like the one below:"""
)
cn_disc('最后，我们可以使用Python字符串格式化的变体'
        '和&lt;seq&gt;标签中的$template$属性来访问多级序列。 '
        '这是用来做所有数字中的标题，以及二级标题。 '
        '子串 $%(counter)s$ 提取了一个计数器的当前值，但不递增；'
        '在 $%(counter)s$ 中添加一个加号，使计数器递增。'
        '数字标题使用了类似下面的模式。')

# parabox2(
#     """Figure <seq template="%(Chapter)s-%(FigureNo+)s"/> - Multi-level
#     templates""",
#     "Multi-level templates",
# )
cn_parabox2('图 <seq template="%(Chapter)s-%(FigureNo+)s"/> - 多级模板', "多级模板",)

disc(
    """We cheated a little - the real document used 'Figure',
but the text above uses 'FigureNo' - otherwise we would have
messed up our numbering!"""
)
cn_disc('我们做了点小手脚--真正的文档用的是 "Figure"，'
        '但上面的文字用的是 "FigureNo" '
        '--否则我们会把编号弄乱的')

# heading2("Bullets and Paragraph Numbering")
cn_heading2('项目符号和段落编号')

disc(
    """In addition to the three indent properties, some other
parameters are needed to correctly handle bulleted and numbered
lists.  We discuss this here because you have now seen how
to handle numbering.  A paragraph may have an optional
^bulletText^ argument passed to its constructor; alternatively,
bullet text may be placed in a $<![CDATA[<bullet>..</bullet>]]>$
tag at its head.  This text will be drawn on the first line of
the paragraph, with its x origin determined by the $bulletIndent$
attribute of the style, and in the font given in the
$bulletFontName$ attribute.   The "bullet" may be a single character
such as (doh!) a bullet, or a fragment of text such as a number in
some numbering sequence, or even a short title as used in a definition
list.   Fonts may offer various bullet
characters but we suggest first trying the Unicode bullet ($&bull;$), which may
be written as $&amp;bull;$,  $&amp;#x2022;$ or (in utf8) $\\xe2\\x80\\xa2$):"""
)
cn_disc('除了三个缩进属性之外，'
        '还需要一些其他参数来正确处理带项目符号和编号的列表。 '
        '我们在这里讨论这个问题，因为你现在已经看到了如何处理编号。 '
        '一个段落可以有一个可选的^bulletText^参数传递给它的构造函数；'
        '或者，项目符号文本可以放在它头部的$<![CDATA[<bullet>...</bullet>]]>$标签中。 '
        '这段文字将被绘制在段落的第一行，其X原点由样式的$bulletIndent$属性决定，字体由$bulletFontName$属性给出。  '
        '"项目符号"可以是一个单一的字符，如（嘟！）一个项目符号，或者是一个文本片段，'
        '如一些编号序列中的数字，甚至是定义列表中使用的简短标题。  '
        '字体可能提供各种项目编号字符，但我们建议首先尝试Unicode项目编号($&bull;$)，'
        '可以写成$&amp;bull;$，和 $#x2022;$ 或(utf8中) $\\xe2\\x80\\xa2$):')

t = Table(*getAttrs(_bulletAttrMap))
t.setStyle(
    [
        ('FONT', (0, 0), (-1, 1), 'Times-Bold', 10, 12),
        ('FONT', (0, 1), (-1, -1), 'Courier', 8, 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ]
)
# getStory().append(t)

cn_t = Table(*cn_getAttrs(_bulletAttrMap))
cn_t.setStyle(
    [
        ('FONT', (0, 0), (-1, 1), 'STSong-Light', 10, 12),
        ('FONT', (0, 1), (-1, -1), 'Courier', 8, 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ]
)
getStory().append(cn_t)

# caption(
#     """Table <seq template="%(Chapter)s-%(Table+)s"/> - &lt;bullet&gt;
#     attributes &amp; synonyms"""
# )
cn_caption('表 <seq template="%(Chapter)s-%(Table+)s"/> &lt;bullet&gt; 属性和同义词')

disc(
    """The &lt;bullet&gt; tag is only allowed once in a given paragraph and 
its use overrides the implied bullet style and ^bulletText^ specified in the  
^Paragraph^ creation.
"""
)
cn_disc('在一个给定的段落中，&lt;bullet&gt;标签只允许使用一次，】它的使用会覆盖在^Paragraph'
        '^创建中指定的隐含的项目符号样式和 ^bulletText^。 (项目符号文本)')

# parabox(
#     """<bullet>&bull;</bullet>this is a bullet point.  Spam
# spam spam spam spam spam spam spam spam spam spam spam
# spam spam spam spam spam spam spam spam spam spam """,
#     styleSheet['Bullet'],
#     'Basic use of bullet points',
# )
cn_parabox('<bullet>&bull;</bullet>这是一个要点。'
           'Spam spam spam spam spam spam spam spam spam spam spam spam'
           'spam spam spam spam spam spam spam spam spam spam',
           cn_styleSheet['Bullet'], '项目点的基本使用')

disc(
    """Exactly the same technique is used for numbers,
except that a sequence tag is used.  It is also possible
to put  a multi-character string in the bullet; with a deep
indent and bold bullet font, you can make a compact
definition list."""
)
cn_disc('除了使用序列标签外，数字也使用了完全相同的技术。 '
        '也可以在项目符号中放入一个多字符的字符串；'
        '用深缩进和粗体子弹字体，'
        '你可以制作一个紧凑的定义列表。')
