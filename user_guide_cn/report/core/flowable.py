from reportlab.platypus.flowables import Flowable
from reportlab.lib.colors import tan, green


def hand(canvas, debug=1, fill=0):
    """ 手章的绘画数据 """
    (startx, starty) = (0, 0)
    curves = [
        (0, 2),
        (0, 4),
        (0, 8),  # back of hand
        (5, 8),
        (7, 10),
        (7, 14),
        (10, 14),
        (10, 13),
        (7.5, 8),  # thumb
        (13, 8),
        (14, 8),
        (17, 8),
        (19, 8),
        (19, 6),
        (17, 6),
        (15, 6),
        (13, 6),
        (11, 6),  # index, pointing
        (12, 6),
        (13, 6),
        (14, 6),
        (16, 6),
        (16, 4),
        (14, 4),
        (13, 4),
        (12, 4),
        (11, 4),  # middle
        (11.5, 4),
        (12, 4),
        (13, 4),
        (15, 4),
        (15, 2),
        (13, 2),
        (12.5, 2),
        (11.5, 2),
        (11, 2),  # ring
        (11.5, 2),
        (12, 2),
        (12.5, 2),
        (14, 2),
        (14, 0),
        (12.5, 0),
        (10, 0),
        (8, 0),
        (6, 0),  # pinky, then close
    ]
    from reportlab.lib.units import inch

    if debug:
        canvas.setLineWidth(6)
    u = inch * 0.2
    p = canvas.beginPath()
    p.moveTo(startx, starty)
    ccopy = list(curves)
    while ccopy:
        [(x1, y1), (x2, y2), (x3, y3)] = ccopy[:3]
        del ccopy[:3]
        p.curveTo(x1 * u, y1 * u, x2 * u, y2 * u, x3 * u, y3 * u)
    p.close()
    canvas.drawPath(p, fill=fill)
    if debug:
        from reportlab.lib.colors import red, green

        (lastx, lasty) = (startx, starty)
        ccopy = list(curves)
        while ccopy:
            [(x1, y1), (x2, y2), (x3, y3)] = ccopy[:3]
            del ccopy[:3]
            canvas.setStrokeColor(red)
            canvas.line(lastx * u, lasty * u, x1 * u, y1 * u)
            canvas.setStrokeColor(green)
            canvas.line(x2 * u, y2 * u, x3 * u, y3 * u)
            (lastx, lasty) = (x3, y3)


def pencil_tip(canvas, debug=1):
    """ 铅笔提示 """
    from reportlab.lib.colors import tan, black, green
    from reportlab.lib.units import inch

    u = inch / 10.0
    canvas.setLineWidth(4)
    if debug:
        canvas.scale(2.8, 2.8)  # make it big
        canvas.setLineWidth(1)  # small lines
    canvas.setStrokeColor(black)
    canvas.setFillColor(tan)
    p = canvas.beginPath()
    p.moveTo(10 * u, 0)
    p.lineTo(0, 5 * u)
    p.lineTo(10 * u, 10 * u)
    p.curveTo(11.5 * u, 10 * u, 11.5 * u, 7.5 * u, 10 * u, 7.5 * u)
    p.curveTo(12 * u, 7.5 * u, 11 * u, 2.5 * u, 9.7 * u, 2.5 * u)
    p.curveTo(10.5 * u, 2.5 * u, 11 * u, 0, 10 * u, 0)
    canvas.drawPath(p, stroke=1, fill=1)
    canvas.setFillColor(black)
    p = canvas.beginPath()
    p.moveTo(0, 5 * u)
    p.lineTo(4 * u, 3 * u)
    p.lineTo(5 * u, 4.5 * u)
    p.lineTo(3 * u, 6.5 * u)
    canvas.drawPath(p, stroke=1, fill=1)
    if debug:
        canvas.setStrokeColor(green)  # put in a frame of reference
        canvas.grid([0, 5 * u, 10 * u, 15 * u], [0, 5 * u, 10 * u])


def pencil(canvas, text="No.2"):
    """铅笔提示"""
    from reportlab.lib.colors import yellow, red, black, white
    from reportlab.lib.units import inch

    u = inch / 10.0
    canvas.setStrokeColor(black)
    canvas.setLineWidth(4)
    # draw erasor
    canvas.setFillColor(red)
    canvas.circle(30 * u, 5 * u, 5 * u, stroke=1, fill=1)
    # draw all else but the tip (mainly rectangles with different fills)
    canvas.setFillColor(yellow)
    canvas.rect(10 * u, 0, 20 * u, 10 * u, stroke=1, fill=1)
    canvas.setFillColor(black)
    canvas.rect(23 * u, 0, 8 * u, 10 * u, fill=1)
    canvas.roundRect(14 * u, 3.5 * u, 8 * u, 3 * u, 1.5 * u, stroke=1, fill=1)
    canvas.setFillColor(white)
    canvas.rect(25 * u, u, 1.2 * u, 8 * u, fill=1, stroke=0)
    canvas.rect(27.5 * u, u, 1.2 * u, 8 * u, fill=1, stroke=0)
    canvas.setFont("Times-Roman", 3 * u)
    canvas.drawCentredString(18 * u, 4 * u, text)
    # now draw the tip
    pencil_tip(canvas, debug=0)
    # draw broken lines across the body.
    canvas.setDash([10, 5, 16, 10], 0)
    canvas.line(11 * u, 2.5 * u, 22 * u, 2.5 * u)
    canvas.line(22 * u, 7.5 * u, 12 * u, 7.5 * u)


class HandAnnotation(Flowable):
    '''A hand flowable.'''

    def __init__(self, xoffset=0, size=None, fillcolor=tan, strokecolor=green):
        super().__init__()
        from reportlab.lib.units import inch

        if size is None:
            size = 4 * inch
        self.fillcolor, self.strokecolor = fillcolor, strokecolor
        self.xoffset = xoffset
        self.size = size
        # normal size is 4 inches
        self.scale = size / (4.0 * inch)

    def wrap(self, *args):
        return (self.xoffset, self.size)

    def draw(self):
        canvas = self.canv
        canvas.setLineWidth(6)
        canvas.setFillColor(self.fillcolor)
        canvas.setStrokeColor(self.strokecolor)
        canvas.translate(self.xoffset + self.size, 0)
        canvas.rotate(90)
        canvas.scale(self.scale, self.scale)
        hand(canvas, debug=0, fill=1)


class NoteAnnotation(Flowable):
    '''put a pencil in the margin.'''

    def wrap(self, *args):
        return (1, 10)  # I take up very little space! (?)

    def draw(self):
        canvas = self.canv
        canvas.translate(-10, -10)
        canvas.rotate(180)
        canvas.scale(0.2, 0.2)
        pencil(canvas, text="NOTE")
