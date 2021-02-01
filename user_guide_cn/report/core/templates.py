import os
from reportlab.platypus import PageTemplate, BaseDocTemplate, Frame, Paragraph
from reportlab.lib.units import inch, cm
from reportlab.lib.sequencer import Sequencer
from reportlab.rl_config import defaultPageSize

from report.components import constant

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class RLFrontCoverTemplate(PageTemplate):
    """ 封面 """

    def __init__(
        self,
        _id,
        unicode_font,
        cover_image=None,
        after_page_strings=None,
        page_size=defaultPageSize,
    ):
        self.unicode_font = unicode_font
        self.pageWidth = page_size[0]
        self.pageHeight = page_size[1]
        self.cover_image = cover_image
        self.after_page_strings = after_page_strings or []
        frame1 = Frame(
            inch,
            3 * inch,
            self.pageWidth - 2 * inch,
            self.pageHeight - 518,
            id='cover',
        )
        PageTemplate.__init__(self, _id, [frame1])  # note lack of onPage

    def afterDrawPage(self, canvas, doc):
        canvas.saveState()

        # 如果有封面图片
        if self.cover_image:
            canvas.drawImage(self.cover_image, 2 * inch, 8 * inch)

        # 封面左下角文本（版权信息）
        x = inch
        font_size = 12
        canvas.setFont(self.unicode_font, font_size - 2)
        canvas.line(inch, 120, self.pageWidth - inch, 120)

        for index, text in enumerate(self.after_page_strings):
            y = 100 - font_size * index
            canvas.drawString(x, y, text)
        # canvas.drawString(inch, 100, 'ReportLab')
        # canvas.drawString(inch, 88, 'Wimbletech')
        # canvas.drawString(inch, 76, '35 Wimbledon Hill Road')
        # canvas.drawString(inch, 64, 'London SW19 7NB, UK')
        # from reportlab.pdfgen import canvas
        canvas.restoreState()


class OneColumnTemplate(PageTemplate):
    """ 页眉/页脚 """

    def __init__(self, _id, unicode_font, page_size=defaultPageSize):
        self.unicode_font = unicode_font
        self.pageWidth = page_size[0]
        self.pageHeight = page_size[1]
        frame1 = Frame(
            inch,
            inch,
            self.pageWidth - 2 * inch,
            self.pageHeight - 2 * inch,
            id='normal',
        )
        PageTemplate.__init__(self, _id, [frame1])  # note lack of onPage

    def afterDrawPage(self, canvas, doc):
        y = self.pageHeight - 50
        canvas.saveState()
        canvas.setFont(self.unicode_font, 10)
        canvas.drawString(inch, y + 8, doc.title)
        canvas.drawRightString(self.pageWidth - inch, y + 8, doc.chapter)
        canvas.line(inch, y, self.pageWidth - inch, y)
        canvas.drawCentredString(
            doc.pagesize[0] / 2, 0.75 * inch, f'第 {canvas.getPageNumber()} 页'
        )
        canvas.restoreState()


class TOCTemplate(PageTemplate):
    """ 目录 """

    def __init__(self, _id, unicode_font, page_size=defaultPageSize):
        self.unicode_font = unicode_font
        self.pageWidth = page_size[0]
        self.pageHeight = page_size[1]
        frame1 = Frame(
            inch,
            inch,
            self.pageWidth - 2 * inch,
            self.pageHeight - 2 * inch,
            id='normal',
        )
        PageTemplate.__init__(self, _id, [frame1])  # note lack of onPage

    def afterDrawPage(self, canvas, doc):
        y = self.pageHeight - 50
        canvas.saveState()
        canvas.setFont(self.unicode_font, 10)
        canvas.drawString(inch, y + 8, doc.title)
        canvas.drawRightString(self.pageWidth - inch, y + 8, '目录')
        canvas.line(inch, y, self.pageWidth - inch, y)
        canvas.drawCentredString(
            doc.pagesize[0] / 2, 0.75 * inch, f'第 {canvas.getPageNumber()} 页'
        )
        canvas.restoreState()


class TwoColumnTemplate(PageTemplate):
    """ 页眉 """

    def __init__(self, _id, unicode_font, page_size=defaultPageSize):
        self.unicode_font = unicode_font
        self.pageWidth = page_size[0]
        self.pageHeight = page_size[1]
        colWidth = 0.5 * (self.pageWidth - 2.25 * inch)
        frame1 = Frame(
            inch, inch, colWidth, self.pageHeight - 2 * inch, id='leftCol'
        )
        frame2 = Frame(
            0.5 * self.pageWidth + 0.125,
            inch,
            colWidth,
            self.pageHeight - 2 * inch,
            id='rightCol',
        )
        PageTemplate.__init__(
            self, _id, [frame1, frame2]
        )  # note lack of onPage

    def afterDrawPage(self, canvas, doc):
        y = self.pageHeight - 50
        canvas.saveState()
        canvas.setFont(self.unicode_font, 10)
        canvas.drawString(inch, y + 8, doc.title)
        canvas.drawRightString(self.pageWidth - inch, y + 8, doc.chapter)
        canvas.line(inch, y, self.pageWidth - inch, y * inch)

        canvas.drawCentredString(
            doc.pagesize[0] / 2, 0.75 * inch, f'第 {canvas.getPageNumber()} 页'
        )
        canvas.restoreState()


class RLDocTemplate(BaseDocTemplate):
    """ Reportlab文档模板 """

    def __init__(
        self,
        filename,
        unicode_font,
        cover_image=None,
        copyrights=None,
        **kwargs,
    ):
        super().__init__(filename=filename, **kwargs)

        self.addPageTemplates(
            RLFrontCoverTemplate(
                constant.PAGE_TEMPLATE_COVER,
                unicode_font,
                cover_image=cover_image,
                after_page_strings=copyrights,
                page_size=self.pagesize,
            )
        )
        self.addPageTemplates(
            TOCTemplate(
                constant.PAGE_TEMPLATE_TOC,
                unicode_font,
                page_size=self.pagesize,
            )
        )
        self.addPageTemplates(
            OneColumnTemplate(
                constant.PAGE_TEMPLATE_NORMAL,
                unicode_font,
                page_size=self.pagesize,
            )
        )
        self.addPageTemplates(
            TwoColumnTemplate(
                constant.PAGE_TEMPLATE_TWO_COLUMN,
                unicode_font,
                page_size=self.pagesize,
            )
        )
        self.seq = Sequencer()  # 计数器

        # 初始化标题和章节
        self.title = "(这儿是文档标题)"
        self.chapter = "(这儿是章节标题)"
        self.seq.reset('section')
        self.seq.reset('chapter')

    def beforeDocument(self):
        self.canv.showOutline()
        self.title = "(这儿是文档标题)"
        self.chapter = "(这儿是章节标题)"
        self.seq.reset('section')
        self.seq.reset('chapter')

    def afterFlowable(self, flowable):
        """Detect Level 1 and 2 headings, build outline,
        and track chapter title."""

        if isinstance(flowable, Paragraph):
            style = flowable.style.name
            txt = flowable.getPlainText()

            if style == constant.STYLE_TITLE:
                self.title = txt
            elif style == constant.STYLE_HEADING_1:
                self.chapter = txt
                key = 'ch%s' % self.seq.nextf('chapter')
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(txt, key, 0, 0)
                self.seq.reset("section")
                self.notify('TOCEntry', (0, txt, self.page, key))
            elif style == constant.STYLE_HEADING_2:
                self.section = flowable.text
                key = 'ch%ss%s' % (
                    self.seq.thisf("chapter"),
                    self.seq.nextf("section"),
                )
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(txt, key, 1, 0)
                self.notify('TOCEntry', (1, txt, self.page, key))
