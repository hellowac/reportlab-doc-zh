"""
Line with markers (serious)
来源: https://www.reportlab.com/chartgallery/line/LineChart01/?iframe=true&width=900&height=500&ajax=true
"""
from reportlab.lib.colors import purple, PCMYKColor, black, pink, green, blue
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.legends import LineLegend
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.lib.validators import Auto
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.pdfbase.pdfmetrics import (
    stringWidth,
    EmbeddedType1Face,
    registerTypeFace,
    Font,
    registerFont,
)
from reportlab.graphics.charts.axes import (
    XValueAxis,
    YValueAxis,
    AdjYValueAxis,
    NormalDateXValueAxis,
)


class SmileyMarkerChart(_DrawingEditorMixin, Drawing):
    """
    Chart Features
    ==============

    This chart is closely related to the 'silly' line chart
    with markers. The key attributes that have changed are:

    - **chart.lines.symbol.kind** was changed from 'FilledCross' to 'Smiley'
    - **chart.lines.symbol.size** was changed from 5 to 15
    - **chart.lines.symbol.angle** was changed from 45 to 0 in order
    to prevent the smiley faces from being rotated
    - **legend.columnMaximum** was changed from 1 to 2, forcing the
    legend into a single stacked column
    - **legend.y** was increased to push the legend up
    - **legend.x** was increased to move it to the right across the chart


    该图表与带有标记的“silly”折线图紧密相关。 更改的关键属性是：

    - **chart.lines.symbol.kind** 从“ FilledCross”更改为“ Smiley”
    - **chart.lines.symbol.size** 从5改为15
    - **chart.lines.symbol.angle** 从45更改为0，以防止笑脸旋转
    - **legend.columnMaximum** 从1更改为2，将图例强制放入单个堆叠列中
    - **legend.y** 增加以推动传奇
    - **legend.x** 增加到将其移到图表的右侧
    """

    def __init__(self, width=258, height=150, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        # font
        fontName = 'Helvetica'
        fontSize = 7
        # chart
        self._add(self, LinePlot(), name='chart', validate=None, desc=None)
        self.chart.y = 16
        self.chart.x = 32
        self.chart.width = 212
        self.chart.height = 90
        # line styles
        self.chart.lines.strokeWidth = 0
        self.chart.lines.symbol = makeMarker('FilledSquare')
        # x axis
        self.chart.xValueAxis = NormalDateXValueAxis()
        self.chart.xValueAxis.labels.fontName = fontName
        self.chart.xValueAxis.labels.fontSize = fontSize - 1
        self.chart.xValueAxis.forceEndDate = 1
        self.chart.xValueAxis.forceFirstDate = 1
        self.chart.xValueAxis.labels.boxAnchor = 'autox'
        self.chart.xValueAxis.xLabelFormat = '{d}-{MMM}'
        self.chart.xValueAxis.maximumTicks = 5
        self.chart.xValueAxis.minimumTickSpacing = 0.5
        self.chart.xValueAxis.niceMonth = 0
        self.chart.xValueAxis.strokeWidth = 1
        self.chart.xValueAxis.loLLen = 5
        self.chart.xValueAxis.hiLLen = 5
        self.chart.xValueAxis.gridEnd = self.width
        self.chart.xValueAxis.gridStart = self.chart.x - 10
        # y axis
        # self.chart.yValueAxis = AdjYValueAxis()
        self.chart.yValueAxis.visibleGrid = 1
        self.chart.yValueAxis.visibleAxis = 0
        self.chart.yValueAxis.labels.fontName = fontName
        self.chart.yValueAxis.labels.fontSize = fontSize - 1
        self.chart.yValueAxis.labelTextFormat = '%0.2f%%'
        self.chart.yValueAxis.strokeWidth = 0.25
        self.chart.yValueAxis.visible = 1
        self.chart.yValueAxis.labels.rightPadding = 5
        # self.chart.yValueAxis.maximumTicks          = 6
        self.chart.yValueAxis.rangeRound = 'both'
        self.chart.yValueAxis.tickLeft = 7.5
        self.chart.yValueAxis.minimumTickSpacing = 0.5
        self.chart.yValueAxis.maximumTicks = 8
        self.chart.yValueAxis.forceZero = 0
        self.chart.yValueAxis.avoidBoundFrac = 0.1
        # legend
        self._add(self, LineLegend(), name='legend', validate=None, desc=None)
        self.legend.fontName = fontName
        self.legend.fontSize = fontSize
        self.legend.alignment = 'right'
        self.legend.dx = 5
        # sample data
        self.chart.data = [
            [
                (19010706, 3.3900000000000001),
                (19010806, 3.29),
                (19010906, 3.2999999999999998),
                (19011006, 3.29),
                (19011106, 3.3399999999999999),
                (19011206, 3.4100000000000001),
                (19020107, 3.3700000000000001),
                (19020207, 3.3700000000000001),
                (19020307, 3.3700000000000001),
                (19020407, 3.5),
                (19020507, 3.6200000000000001),
                (19020607, 3.46),
                (19020707, 3.3900000000000001),
            ],
            [
                (19010706, 3.2000000000000002),
                (19010806, 3.1200000000000001),
                (19010906, 3.1400000000000001),
                (19011006, 3.1400000000000001),
                (19011106, 3.1699999999999999),
                (19011206, 3.23),
                (19020107, 3.1899999999999999),
                (19020207, 3.2000000000000002),
                (19020307, 3.1899999999999999),
                (19020407, 3.3100000000000001),
                (19020507, 3.4300000000000002),
                (19020607, 3.29),
                (19020707, 3.2200000000000002),
            ],
        ]
        self.chart.lines[0].strokeColor = PCMYKColor(0, 100, 100, 40, alpha=100)
        self.chart.lines[1].strokeColor = PCMYKColor(100, 0, 90, 50, alpha=100)
        self.chart.xValueAxis.strokeColor = PCMYKColor(
            100, 60, 0, 50, alpha=100
        )
        self.legend.colorNamePairs = [
            (PCMYKColor(0, 100, 100, 40, alpha=100), 'Bovis Homes'),
            (PCMYKColor(100, 0, 90, 50, alpha=100), 'HSBC Holdings'),
        ]
        self.chart.lines.symbol.x = 0
        self.chart.lines.symbol.strokeWidth = 0
        self.chart.lines.symbol.arrowBarbDx = 5
        self.chart.lines.symbol.strokeColor = PCMYKColor(0, 0, 0, 0, alpha=100)
        self.chart.lines.symbol.fillColor = None
        self.chart.lines.symbol.arrowHeight = 5
        self.legend.dxTextSpace = 7
        self.legend.boxAnchor = 'nw'
        self.legend.subCols.dx = 0
        self.legend.subCols.dy = -2
        self.legend.subCols.rpad = 0
        self.legend.columnMaximum = 1
        self.legend.deltax = 1
        self.legend.deltay = 0
        self.legend.dy = 5
        self.legend.y = 135
        self.legend.x = 120
        self.chart.lines.symbol.kind = 'FilledCross'
        self.chart.lines.symbol.size = 5
        self.chart.lines.symbol.angle = 45


def smiley_marker_chart(
    width=258, height=150, font_name='Helvetica', font_size=7
):

    drawing = Drawing(width, height)
    chart = LinePlot()
    chart.y = 16
    chart.x = 32
    chart.width = 212
    chart.height = 90
    # line styles
    chart.lines.strokeWidth = 0
    chart.lines.symbol = makeMarker('FilledSquare')
    # x axis
    chart.xValueAxis = NormalDateXValueAxis()
    chart.xValueAxis.labels.fontName = font_name
    chart.xValueAxis.labels.fontSize = font_size - 1
    chart.xValueAxis.forceEndDate = 1
    chart.xValueAxis.forceFirstDate = 1
    chart.xValueAxis.labels.boxAnchor = 'autox'
    chart.xValueAxis.xLabelFormat = '{d}-{MMM}'
    chart.xValueAxis.maximumTicks = 5
    chart.xValueAxis.minimumTickSpacing = 0.5
    chart.xValueAxis.niceMonth = 0
    chart.xValueAxis.strokeWidth = 1
    chart.xValueAxis.loLLen = 5
    chart.xValueAxis.hiLLen = 5
    chart.xValueAxis.gridEnd = width
    chart.xValueAxis.gridStart = chart.x - 10
    # y axis
    # chart.yValueAxis = AdjYValueAxis()
    chart.yValueAxis.visibleGrid = 1
    chart.yValueAxis.visibleAxis = 0
    chart.yValueAxis.labels.fontName = font_name
    chart.yValueAxis.labels.fontSize = font_size - 1
    chart.yValueAxis.labelTextFormat = '%0.2f%%'
    chart.yValueAxis.strokeWidth = 0.25
    chart.yValueAxis.visible = 1
    chart.yValueAxis.labels.rightPadding = 5
    # chart.yValueAxis.maximumTicks          = 6
    chart.yValueAxis.rangeRound = 'both'
    chart.yValueAxis.tickLeft = 7.5
    chart.yValueAxis.minimumTickSpacing = 0.5
    chart.yValueAxis.maximumTicks = 8
    chart.yValueAxis.forceZero = 0
    chart.yValueAxis.avoidBoundFrac = 0.1

    legend = LineLegend()
    legend.fontName = font_name
    legend.fontSize = font_size
    legend.alignment = 'right'
    legend.dx = 5
    # sample data
    chart.data = [
        [
            (19010706, 3.3900000000000001),
            (19010806, 3.29),
            (19010906, 3.2999999999999998),
            (19011006, 3.29),
            (19011106, 3.3399999999999999),
            (19011206, 3.4100000000000001),
            (19020107, 3.3700000000000001),
            (19020207, 3.3700000000000001),
            (19020307, 3.3700000000000001),
            (19020407, 3.5),
            (19020507, 3.6200000000000001),
            (19020607, 3.46),
            (19020707, 3.3900000000000001),
        ],
        [
            (19010706, 3.2000000000000002),
            (19010806, 3.1200000000000001),
            (19010906, 3.1400000000000001),
            (19011006, 3.1400000000000001),
            (19011106, 3.1699999999999999),
            (19011206, 3.23),
            (19020107, 3.1899999999999999),
            (19020207, 3.2000000000000002),
            (19020307, 3.1899999999999999),
            (19020407, 3.3100000000000001),
            (19020507, 3.4300000000000002),
            (19020607, 3.29),
            (19020707, 3.2200000000000002),
        ],
    ]
    chart.lines[0].strokeColor = PCMYKColor(0, 100, 100, 40, alpha=100)
    chart.lines[1].strokeColor = PCMYKColor(100, 0, 90, 50, alpha=100)
    chart.xValueAxis.strokeColor = PCMYKColor(100, 60, 0, 50, alpha=100)
    legend.colorNamePairs = [
        (PCMYKColor(0, 100, 100, 40, alpha=100), 'Bovis Homes'),
        (PCMYKColor(100, 0, 90, 50, alpha=100), 'HSBC Holdings'),
    ]
    chart.lines.symbol.x = 0
    chart.lines.symbol.strokeWidth = 0
    chart.lines.symbol.arrowBarbDx = 5
    chart.lines.symbol.strokeColor = PCMYKColor(0, 0, 0, 0, alpha=100)
    chart.lines.symbol.fillColor = None
    chart.lines.symbol.arrowHeight = 5
    legend.dxTextSpace = 7
    legend.boxAnchor = 'nw'
    legend.subCols.dx = 0
    legend.subCols.dy = -2
    legend.subCols.rpad = 0
    legend.columnMaximum = 1
    legend.deltax = 1
    legend.deltay = 0
    legend.dy = 5
    legend.y = 135
    legend.x = 120
    chart.lines.symbol.kind = 'FilledCross'
    chart.lines.symbol.size = 5
    chart.lines.symbol.angle = 45

    drawing.add(chart, 'chart')
    drawing.add(legend, 'legend')

    return drawing


if __name__ == "__main__":  # NORUNTESTS
    # SmileyMarkerChart().save(formats=['pdf'], outDir='.', fnRoot=None)
    draw = smiley_marker_chart()
    draw.save(formats=['pdf'], outDir='.', fnRoot=None)
