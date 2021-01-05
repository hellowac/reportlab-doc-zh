from reportlab.lib.styles import StyleSheet1, ParagraphStyle, PropertySet, black
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.lib import colors
from reportlab import rl_settings
from reportlab import rl_config

from components import constant


def get_default_style_sheet(font_name=None, font_bold=None):
    _font_name = font_name or rl_config.canvas_basefontname
    _font_bold = font_bold or rl_config.canvas_basefontname

    normal_style = ParagraphStyle(
        name=constant.STYLE_NORMAL,
        fontName=_font_name,
        fontSize=10,
        leading=12,
        spaceBefore=6,
    )
    _body_text = ParagraphStyle(
        name=constant.STYLE_BODY_TEXT,
        parent=normal_style,
        spaceBefore=6,
    )
    comment_style = ParagraphStyle(
        name=constant.STYLE_COMMENT, fontName=_font_name
    )
    indent_0_style = ParagraphStyle(
        name=constant.STYLE_INDENT_0,
        leftIndent=18,
    )
    indent_1_style = ParagraphStyle(
        name=constant.STYLE_INDENT_1,
        leftIndent=36,
        firstLineIndent=0,
        spaceBefore=1,
        spaceAfter=7,
    )
    indent_2_style = ParagraphStyle(
        name=constant.STYLE_INDENT_2,
        leftIndent=50,
        firstLineIndent=0,
        spaceAfter=100,
    )
    italic_style = ParagraphStyle(
        name=constant.STYLE_ITALIC,
        parent=_body_text,
        fontName=_font_name,
    )
    heading_1_style = ParagraphStyle(
        name=constant.STYLE_HEADING_1,
        parent=normal_style,
        fontName=_font_name,
        alignment=TA_CENTER,
        fontSize=18,
        leading=22,
        spaceAfter=6,
    )
    heading_2_style = ParagraphStyle(
        name=constant.STYLE_HEADING_2,
        parent=normal_style,
        fontName=_font_name,
        fontSize=14,
        leading=17,
        spaceBefore=12,
        spaceAfter=6,
    )
    heading_3_style = ParagraphStyle(
        name=constant.STYLE_HEADING_3,
        parent=normal_style,
        fontName=_font_name,
        fontSize=12,
        leading=14,
        spaceBefore=12,
        spaceAfter=6,
    )
    heading_4_style = ParagraphStyle(
        name=constant.STYLE_HEADING_4,
        parent=normal_style,
        fontName=_font_name,
        spaceBefore=10,
        spaceAfter=4,
    )
    title_style = ParagraphStyle(
        name=constant.STYLE_TITLE,
        parent=normal_style,
        fontName=_font_name,
        fontSize=32,
        leading=40,
        spaceAfter=36,
        alignment=TA_CENTER,
    )
    bullet_style = ParagraphStyle(
        name=constant.STYLE_BULLET,
        parent=normal_style,
        firstLineIndent=0,
        leftIndent=32,
        bulletIndent=18,
        spaceBefore=0,
        bulletFontName='Symbol',
    )
    definition_style = ParagraphStyle(
        name=constant.STYLE_DEFINITION,
        parent=normal_style,
        firstLineIndent=0,
        leftIndent=36,
        bulletIndent=0,
        spaceBefore=6,
        bulletFontName='Times-BoldItalic',
    )
    code_style = ParagraphStyle(
        name=constant.STYLE_CODE,
        parent=normal_style,
        fontName=_font_bold,
        fontSize=8,
        leading=8.8,
        leftIndent=36,
        firstLineIndent=0,
        hyphenationLang='',
        wordWrap='CJK',
    )
    link_style = ParagraphStyle(
        name=constant.STYLE_LINK,
        parent=code_style,
        spaceAfter=7,
        spaceBefore=0,
        leftIndent=55,
    )
    function_header_style = ParagraphStyle(
        name=constant.STYLE_FUNCTION_HEADER,
        parent=normal_style,
        fontName=_font_name,
        fontSize=8,
        leading=8.8,
    )
    doc_string_style = ParagraphStyle(
        name=constant.STYLE_DOC_STRING,
        parent=normal_style,
        fontName='Courier',
        fontSize=8,
        leftIndent=18,
        leading=8.8,
    )
    doc_string_indent_style = ParagraphStyle(
        name=constant.STYLE_DOC_STRING_INDENT,
        parent=normal_style,
        fontName=_font_name,
        fontSize=8,
        leftIndent=36,
        leading=8.8,
    )

    url_style = ParagraphStyle(
        name=constant.STYLE_URL,
        parent=normal_style,
        fontName=_font_name,
        textColor=colors.navy,
        alignment=TA_CENTER,
    )
    centred_style = ParagraphStyle(
        name=constant.STYLE_CENTRED,
        parent=normal_style,
        fontName=_font_name,
        alignment=TA_CENTER,
    )
    caption_style = ParagraphStyle(
        name=constant.STYLE_CAPTION,
        parent=centred_style,
        fontName=_font_name,
    )

    stylesheet = StyleSheet1()
    stylesheet.add(normal_style)
    stylesheet.add(comment_style)
    stylesheet.add(indent_0_style)
    stylesheet.add(indent_1_style)
    stylesheet.add(indent_2_style)
    stylesheet.add(_body_text)
    stylesheet.add(italic_style)
    stylesheet.add(
        heading_1_style,
        alias=constant.STYLE_H1,
    )
    stylesheet.add(
        heading_2_style,
        alias=constant.STYLE_H2,
    )
    stylesheet.add(
        heading_3_style,
        alias=constant.STYLE_H3,
    )
    stylesheet.add(
        heading_4_style,
        alias=constant.STYLE_H4,
    )
    stylesheet.add(
        title_style,
        alias=constant.STYLE_T,
    )
    stylesheet.add(
        bullet_style,
        alias=constant.STYLE_BU,
    )
    stylesheet.add(
        definition_style,
        alias=constant.STYLE_DF,
    )
    stylesheet.add(code_style)
    stylesheet.add(link_style)
    stylesheet.add(function_header_style)
    stylesheet.add(doc_string_style)
    stylesheet.add(doc_string_indent_style)
    stylesheet.add(url_style, alias=constant.STYLE_U)
    stylesheet.add(centred_style)
    stylesheet.add(caption_style)

    return stylesheet
