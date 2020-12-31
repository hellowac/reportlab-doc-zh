"""
目录内容和样式定义
"""
from reportlab.platypus.tableofcontents import (
    TableOfContents as BaseTableOfContents,
)

from core.style.toc import get_toc_style


class TableOfContents(BaseTableOfContents):
    def __init__(self, font_name, **kwargs):
        super().__init__(**kwargs)
        self.levelStyles = get_toc_style(font_name)
