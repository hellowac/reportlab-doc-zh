# Copyright ReportLab Europe Ltd. 2000-2017
# see license.txt for license details
# history https://hg.reportlab.com/hg-public/reportlab/log/tip/tools/docco
# /stylesheet.py
# standard stylesheet for our manuals
from reportlab.lib.styles import StyleSheet1, ParagraphStyle, PropertySet, black
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.lib import colors
from reportlab import rl_settings


def getStyleSheet():
    """Returns a stylesheet object"""
    stylesheet = StyleSheet1()

    stylesheet.add(
        ParagraphStyle(
            name='Normal',
            fontName='Times-Roman',
            fontSize=10,
            leading=12,
            spaceBefore=6,
        )
    )

    stylesheet.add(ParagraphStyle(name='Comment', fontName='Times-Italic'))

    stylesheet.add(
        ParagraphStyle(
            name='Indent0',
            leftIndent=18,
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='Indent1',
            leftIndent=36,
            firstLineIndent=0,
            spaceBefore=1,
            spaceAfter=7,
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='Indent2', leftIndent=50, firstLineIndent=0, spaceAfter=100
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='BodyText', parent=stylesheet['Normal'], spaceBefore=6
        )
    )
    stylesheet.add(
        ParagraphStyle(
            name='Italic',
            parent=stylesheet['BodyText'],
            fontName='Times-Italic',
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='Heading1',
            parent=stylesheet['Normal'],
            fontName='Times-Bold',
            alignment=TA_CENTER,
            fontSize=18,
            leading=22,
            spaceAfter=6,
        ),
        alias='h1',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Heading2',
            parent=stylesheet['Normal'],
            fontName='Times-Bold',
            fontSize=14,
            leading=17,
            spaceBefore=12,
            spaceAfter=6,
        ),
        alias='h2',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Heading3',
            parent=stylesheet['Normal'],
            fontName='Times-BoldItalic',
            fontSize=12,
            leading=14,
            spaceBefore=12,
            spaceAfter=6,
        ),
        alias='h3',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Heading4',
            parent=stylesheet['Normal'],
            fontName='Times-BoldItalic',
            spaceBefore=10,
            spaceAfter=4,
        ),
        alias='h4',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Title',
            parent=stylesheet['Normal'],
            fontName='Times-Bold',
            fontSize=32,
            leading=40,
            spaceAfter=36,
            alignment=TA_CENTER,
        ),
        alias='t',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Bullet',
            parent=stylesheet['Normal'],
            firstLineIndent=0,
            leftIndent=54,
            bulletIndent=18,
            spaceBefore=0,
            bulletFontName='Symbol',
        ),
        alias='bu',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Definition',
            parent=stylesheet['Normal'],
            firstLineIndent=0,
            leftIndent=36,
            bulletIndent=0,
            spaceBefore=6,
            bulletFontName='Times-BoldItalic',
        ),
        alias='df',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Code',
            parent=stylesheet['Normal'],
            fontName='Courier-Bold',
            fontSize=8,
            leading=8.8,
            leftIndent=36,
            firstLineIndent=0,
            hyphenationLang='',
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='Link',
            parent=stylesheet['Code'],
            spaceAfter=7,
            spaceBefore=0,
            leftIndent=55,
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='FunctionHeader',
            parent=stylesheet['Normal'],
            fontName='Courier-Bold',
            fontSize=8,
            leading=8.8,
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='DocString',
            parent=stylesheet['Normal'],
            fontName='Courier',
            fontSize=8,
            leftIndent=18,
            leading=8.8,
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='DocStringIndent',
            parent=stylesheet['Normal'],
            fontName='Courier',
            fontSize=8,
            leftIndent=36,
            leading=8.8,
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='URL',
            parent=stylesheet['Normal'],
            fontName='Courier',
            textColor=colors.navy,
            alignment=TA_CENTER,
        ),
        alias='u',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Centred', parent=stylesheet['Normal'], alignment=TA_CENTER
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='Caption',
            parent=stylesheet['Centred'],
            fontName='Times-Italic',
        )
    )

    return stylesheet


# STSong-Light
def getCnStyleSheet():
    stylesheet = StyleSheet1()

    stylesheet.add(
        ParagraphStyle(
            name='Normal',
            fontName='STSong-Light',
            fontSize=10,
            leading=12,
            spaceBefore=6,
        )
    )

    stylesheet.add(ParagraphStyle(name='Comment', fontName='STSong-Light'))

    stylesheet.add(
        ParagraphStyle(
            name='Indent0',
            leftIndent=18,
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='Indent1',
            leftIndent=36,
            firstLineIndent=0,
            spaceBefore=1,
            spaceAfter=7,
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='Indent2', leftIndent=50, firstLineIndent=0, spaceAfter=100
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='BodyText', parent=stylesheet['Normal'], spaceBefore=6
        )
    )
    stylesheet.add(
        ParagraphStyle(
            name='Italic',
            parent=stylesheet['BodyText'],
            fontName='STSong-Light',
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='Heading1',
            parent=stylesheet['Normal'],
            fontName='STSong-Light',
            alignment=TA_CENTER,
            fontSize=18,
            leading=22,
            spaceAfter=6,
        ),
        alias='h1',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Heading2',
            parent=stylesheet['Normal'],
            fontName='STSong-Light',
            fontSize=14,
            leading=17,
            spaceBefore=12,
            spaceAfter=6,
        ),
        alias='h2',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Heading3',
            parent=stylesheet['Normal'],
            fontName='STSong-Light',
            fontSize=12,
            leading=14,
            spaceBefore=12,
            spaceAfter=6,
        ),
        alias='h3',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Heading4',
            parent=stylesheet['Normal'],
            fontName='STSong-Light',
            spaceBefore=10,
            spaceAfter=4,
        ),
        alias='h4',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Title',
            parent=stylesheet['Normal'],
            fontName='STSong-Light',
            fontSize=32,
            leading=40,
            spaceAfter=36,
            alignment=TA_CENTER,
        ),
        alias='t',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Bullet',
            parent=stylesheet['Normal'],
            firstLineIndent=0,
            leftIndent=54,
            bulletIndent=18,
            spaceBefore=0,
            bulletFontName='Symbol',
        ),
        alias='bu',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Definition',
            parent=stylesheet['Normal'],
            firstLineIndent=0,
            leftIndent=36,
            bulletIndent=0,
            spaceBefore=6,
            bulletFontName='Times-BoldItalic',
        ),
        alias='df',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Code',
            parent=stylesheet['Normal'],
            fontName='STSong-Light',
            fontSize=8,
            leading=8.8,
            leftIndent=36,
            firstLineIndent=0,
            hyphenationLang='',
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='Link',
            parent=stylesheet['Code'],
            spaceAfter=7,
            spaceBefore=0,
            leftIndent=55,
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='FunctionHeader',
            parent=stylesheet['Normal'],
            fontName='STSong-Light',
            fontSize=8,
            leading=8.8,
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='DocString',
            parent=stylesheet['Normal'],
            fontName='Courier',
            fontSize=8,
            leftIndent=18,
            leading=8.8,
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='DocStringIndent',
            parent=stylesheet['Normal'],
            fontName='Courier',
            fontSize=8,
            leftIndent=36,
            leading=8.8,
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='URL',
            parent=stylesheet['Normal'],
            fontName='Courier',
            textColor=colors.navy,
            alignment=TA_CENTER,
        ),
        alias='u',
    )

    stylesheet.add(
        ParagraphStyle(
            name='Centred',
            parent=stylesheet['Normal'],
            fontName='STSong-Light',
            alignment=TA_CENTER,
        )
    )

    stylesheet.add(
        ParagraphStyle(
            name='Caption',
            parent=stylesheet['Centred'],
            fontName='STSong-Light',
        )
    )

    return stylesheet


class CnParagraphStyle(PropertySet):
    defaults = {
        'fontName':'STSong-Light',
        'fontSize':10,
        'leading':12,
        'leftIndent':0,
        'rightIndent':0,
        'firstLineIndent':0,
        'alignment':TA_LEFT,
        'spaceBefore':0,
        'spaceAfter':0,
        'bulletFontName':'STSong-Light',
        'bulletFontSize':10,
        'bulletIndent':0,
        #'bulletColor':black,
        'textColor': black,
        'backColor':None,
        'wordWrap':None,        #None means do nothing special
        #CJK use Chinese Line breaking
        #LTR RTL use left to right / right to left
        #with support from pyfribi2 if available
        'borderWidth': 0,
        'borderPadding': 0,
        'borderColor': None,
        'borderRadius': None,
        'allowWidows': 1,
        'allowOrphans': 0,
        'textTransform':None,   #uppercase lowercase (captitalize not yet) or None or absent
        'endDots':None,         #dots on the last line of left/right justified paras
        #string or object with text and optional fontName, fontSize, textColor & backColor
        #dy
        'splitLongWords':1,     #make best efforts to split long words
        'underlineWidth': rl_settings.underlineWidth,  #underline width
        'bulletAnchor': 'start',    #where the bullet is anchored ie start, middle, end or numeric
        'justifyLastLine': 0,   #n allow justification on the last line for more than n words 0 means don't bother
        'justifyBreaks': 0,     #justify lines broken with <br/>
        'spaceShrinkage': rl_settings.spaceShrinkage,  #allow shrinkage of percentage of
        # space to fit
        # on line
        'strikeWidth': rl_settings.strikeWidth,    #stroke width
        #fraction of fontsize to offset underlines
        'underlineOffset': rl_settings.underlineOffset,
        #gap for double/triple underline
        'underlineGap': rl_settings.underlineGap,
        #fraction of fontsize to offset strikethrough
        'strikeOffset': rl_settings.strikeOffset,
        #gap for double/triple strike
        'strikeGap': rl_settings.strikeGap,
        'linkUnderline': rl_settings.platypus_link_underline,
        #'underlineColor':  None,
        #'strikeColor': None,
        'hyphenationLang': rl_settings.hyphenationLang,
        #'hyphenationMinWordLength': _hyphenationMinWordLength,
        'embeddedHyphenation': rl_settings.embeddedHyphenation,
        'uriWasteReduce': rl_settings.uriWasteReduce,
    }