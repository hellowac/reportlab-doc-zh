

from reportlab.platypus.tableofcontents import TableOfContents


class CnTableOfContents(TableOfContents):

    def __int__(self, **kwargs):
        super().__init__(**kwargs)