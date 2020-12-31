from reportlab import rl_config
from reportlab.lib.fonts import tt2ps
from reportlab.lib.units import inch
from reportlab.platypus.figures import Figure as BaseFigure
from reportlab.platypus import Paragraph, Preformatted
from reportlab.lib.styles import ParagraphStyle
from xml.sax.saxutils import escape as xmlEscape


# 示例函数宽高定义
example_function_x_inches = 5.5
example_function_y_inches = 3
example_function_display_sizes = (
    example_function_x_inches * inch,
    example_function_y_inches * inch,
)


class Illustration(BaseFigure):
    def __init__(
        self, operation, caption, width=None, height=None, font_name=None
    ):
        std_width, std_height = example_function_display_sizes

        width = width or std_width
        height = height or std_height

        font_name = font_name or rl_config.canvas_basefontname
        super().__init__(
            width,
            height,
            caption,
            captionFont=tt2ps(font_name, 0, 1),
        )
        self.operation = operation

    def drawFigure(self):
        # shrink it a little...
        # self.canv.scale(0.75, 0.75)
        self.operation(self.canv)


class GraphicsDrawing(Illustration):
    def __init__(self, drawing, caption, font_name=None):
        _font_name = font_name or rl_config.canvas_basefontname
        BaseFigure.__init__(
            self,
            drawing.width,
            drawing.height,
            caption,
            captionFont=tt2ps(_font_name, 0, 1),
        )
        self.drawing = drawing

    def drawFigure(self):
        d = self.drawing
        d.wrap(d.width, d.height)
        d.drawOn(self.canv, 0, 0)


class ParaBox(BaseFigure):
    def __init__(self, text, style, caption, font_name=None):

        _font_name = font_name or rl_config.canvas_basefontname
        super().__init__(0, 0, caption=caption, captionFont=_font_name)
        self.text = text
        self.style = style
        self.para = Paragraph(text, style)

        style_text = self.get_style_text(style)
        desc_style = ParagraphStyle(
            'description', fontName=_font_name, fontSize=8, leading=9.6
        )
        self.pre = Preformatted(style_text, desc_style)

    def wrap(self, availWidth, availHeight):
        """Left 30% is for attributes, right 50% for sample,
        10% gutter each side."""
        self.x0 = availWidth * 0.05  # left of box
        self.x1 = availWidth * 0.1  # left of descriptive text
        self.x2 = availWidth * 0.5  # left of para itself
        self.x3 = availWidth * 0.9  # right of para itself
        self.x4 = availWidth * 0.95  # right of box
        self.width = self.x4 - self.x0
        self.dx = 0.5 * (availWidth - self.width)

        paw, self.pah = self.para.wrap(self.x3 - self.x2, availHeight)
        self.pah = self.pah + self.style.spaceBefore + self.style.spaceAfter
        prw, self.prh = self.pre.wrap(self.x2 - self.x1, availHeight)
        self.figureHeight = max(self.prh, self.pah) * 10.0 / 9.0
        return BaseFigure.wrap(self, availWidth, availHeight)

    def drawFigure(self):

        # now we fill in the bounding box and before/after boxes
        self.canv.saveState()
        self.canv.setFillGray(0.95)
        self.canv.setDash(1, 3)
        self.canv.rect(
            self.x2 - self.x0,
            self.figureHeight * 0.95 - self.pah,
            self.x3 - self.x2,
            self.para.height,
            fill=1,
            stroke=1,
        )

        self.canv.setFillGray(0.90)
        self.canv.rect(
            self.x2 - self.x0,  # spaceBefore
            self.figureHeight * 0.95 - self.pah + self.para.height,
            self.x3 - self.x2,
            self.style.spaceBefore,
            fill=1,
            stroke=1,
        )

        self.canv.rect(
            self.x2 - self.x0,  # spaceBefore
            self.figureHeight * 0.95 - self.pah - self.style.spaceAfter,
            self.x3 - self.x2,
            self.style.spaceAfter,
            fill=1,
            stroke=1,
        )

        self.canv.restoreState()
        # self.canv.setFillColor(colors.yellow)
        self.para.drawOn(
            self.canv, self.x2 - self.x0, self.figureHeight * 0.95 - self.pah
        )
        self.pre.drawOn(
            self.canv, self.x1 - self.x0, self.figureHeight * 0.95 - self.prh
        )

    def get_style_text(self, style):
        """Converts style to preformatted block of text"""
        lines = []
        for key, value in sorted(style.__dict__.items()):
            if key not in ('name', 'parent'):
                lines.append('%s = %s' % (key, value))
        return '\n'.join(lines)


class ParaBox2(BaseFigure):
    def __init__(self, text, caption, style, font_name=None):
        _font_name = font_name or rl_config.canvas_basefontname
        BaseFigure.__init__(self, 0, 0, caption, captionFont=_font_name)
        descr_style = ParagraphStyle(
            'description', fontName=_font_name, fontSize=8, leading=9.6
        )
        self.text = text
        self.left = Paragraph(xmlEscape(text), descr_style)
        self.right = Paragraph(text, style)

    def wrap(self, avail_width, avail_height):
        self.width = avail_width * 0.9
        col_width = 0.4 * self.width
        lw, self.lh = self.left.wrap(col_width, avail_height)
        rw, self.rh = self.right.wrap(col_width, avail_height)
        self.figureHeight = max(self.lh, self.rh) * 10.0 / 9.0
        return BaseFigure.wrap(self, avail_width, avail_height)

    def drawFigure(self):
        self.left.drawOn(
            self.canv, self.width * 0.05, self.figureHeight * 0.95 - self.lh
        )
        self.right.drawOn(
            self.canv, self.width * 0.55, self.figureHeight * 0.95 - self.rh
        )
