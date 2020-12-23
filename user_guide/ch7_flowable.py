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
