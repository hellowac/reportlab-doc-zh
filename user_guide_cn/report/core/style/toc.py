"""
目录表格样式，最多只有4级
"""

from reportlab.lib.styles import ParagraphStyle

from report.components import constant

_HEADING_FONT_SIZE_MAP = {
    constant.TOC_STYLE_HEADING_1: 14,
    constant.TOC_STYLE_HEADING_2: 12,
    constant.TOC_STYLE_HEADING_3: 10,
    constant.TOC_STYLE_HEADING_4: 10,
}

_HEADING_SPACE_BEFORE_MAP = {
    constant.TOC_STYLE_HEADING_1: 5,
    constant.TOC_STYLE_HEADING_2: 0,
    constant.TOC_STYLE_HEADING_3: 0,
    constant.TOC_STYLE_HEADING_4: 0,
}

_HEADING_LEFT_INDENT_MAP = {
    constant.TOC_STYLE_HEADING_1: 20,
    constant.TOC_STYLE_HEADING_2: 40,
    constant.TOC_STYLE_HEADING_3: 60,
    constant.TOC_STYLE_HEADING_4: 80,
}

_HEADING_LEADING_MAP = {
    constant.TOC_STYLE_HEADING_1: 16,
    constant.TOC_STYLE_HEADING_2: 12,
    constant.TOC_STYLE_HEADING_3: 12,
    constant.TOC_STYLE_HEADING_4: 12,
}


def get_toc_style(font_name):

    return [
        ParagraphStyle(
            fontName=font_name,
            fontSize=_HEADING_FONT_SIZE_MAP[name],
            name=name,
            leftIndent=_HEADING_LEFT_INDENT_MAP[name],
            firstLineIndent=-20,
            spaceBefore=_HEADING_SPACE_BEFORE_MAP[name],
            leading=_HEADING_LEADING_MAP[name],
        )
        for name in _HEADING_LEFT_INDENT_MAP.keys()
    ]
