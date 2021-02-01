"Comparing performances across eight months for 4 categories."
from reportlab.lib.colors import (
    PCMYKColor,
    red,
    Color,
    CMYKColor,
    yellow,
    black,
    blue,
)
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin, String, Line
from reportlab.pdfbase.pdfmetrics import (
    stringWidth,
    EmbeddedType1Face,
    registerTypeFace,
    Font,
    registerFont,
)
from reportlab.graphics.charts.barcharts import (
    VerticalBarChart,
    VerticalBarChart3D,
)
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.widgets.table import TableWidget
from reportlab.lib.validators import Auto
from reportlab.lib.formatters import DecimalFormatter
from reportlab.graphics.charts.barcharts import HorizontalBarChart
from reportlab.graphics.charts.textlabels import RedNegativeChanger, LabelOffset


class FourCategoryEightMonth(_DrawingEditorMixin, Drawing):
    """
    A Comparision Bar Chart
    =======================

    This is a Bar Chart that contains a Legend Widget to compare company
    performances across eight months.

    Chart Features
    --------------

    This chart demonstrates different unique features such as

    - A Legend that can wrap - legend->columnMaximum=3

    - Bar Chart attributes

    - A vertical labels chart->barLabels->angle=90

    - Simple category axis - dates are not necessary here.

    This chart was built with our Diagra_ solution.


    Not the kind of chart you looking for? Do not worry go back for more
    charts, or to see different types of charts click on `ReportLab Charts
    Gallery`_.

    .. _up: ..
    .. _ReportLab Charts Gallery: /chartgallery/
    [Diagra:] (http://www.reportlab.com/software/diagra/)
    """

    def __init__(self, width=298, height=165, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)

        fontName = kw.get('fontName', 'Times-Roman')
        # chart
        self._add(
            self, VerticalBarChart(), name='chart', validate=None, desc=None
        )
        self.chart.width = width - 18  # 280
        self.chart.height = height - 59  # 106
        self.chart.x = 15
        self.chart.y = 50
        # colors
        self._colors = (
            PCMYKColor(100, 67, 0, 23),
            PCMYKColor(60, 40, 0, 13),
            PCMYKColor(100, 0, 46, 46),
            PCMYKColor(70, 0, 36, 36),
        )
        # chart bars
        self.chart.bars.strokeColor = None
        self.chart.bars.strokeWidth = 0
        # we have four series here
        for i, color in enumerate(self._colors):
            self.chart.bars[i].fillColor = color
        self.chart.barSpacing = 4
        self.chart.barWidth = 14
        self.chart.barLabelFormat = '%s'
        self.chart.barLabels.nudge = 5
        self.chart.barLabels.angle = 90
        self.chart.barLabels.fontName = fontName
        self.chart.barLabels.fontSize = 5
        # categoy axis
        self.chart.categoryAxis.categoryNames = [
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'May',
            'Jun',
            'Jul',
            'Aug',
        ]
        self.chart.categoryAxis.labelAxisMode = 'low'
        self.chart.categoryAxis.labels.angle = 0
        self.chart.categoryAxis.labels.boxAnchor = 'n'
        self.chart.categoryAxis.labels.dy = -6
        self.chart.categoryAxis.labels.fillColor = PCMYKColor(0, 0, 0, 100)
        self.chart.categoryAxis.labels.fontName = fontName
        self.chart.categoryAxis.labels.fontSize = 6
        self.chart.categoryAxis.labels.textAnchor = 'middle'
        self.chart.categoryAxis.tickShift = 1
        self.chart.categoryAxis.visibleTicks = 0
        self.chart.categoryAxis.strokeWidth = 0
        self.chart.categoryAxis.strokeColor = None
        # sample data
        self.chart.data = [
            (0.27, 2.17, 3.66, 5.2, -1.33, -3.12, -6.36, 4.4),
            (1.34, 1.11, 3.53, 4.55, -3.36, -6.64, -7.41, -6.22),
            (1.37, 2.17, 3.77, 5.12, -1.22, -3.22, -5.36, 4.14),
            (0.33, 1.21, 3.52, 4.77, -1.36, -6.64, -8.1, -7.52),
        ]
        self.chart.groupSpacing = 15
        # value axis
        self.chart.valueAxis.avoidBoundFrac = None
        self.chart.valueAxis.gridStrokeWidth = 0.25
        self.chart.valueAxis.labels.fontName = fontName
        self.chart.valueAxis.labels.fontSize = 6
        self.chart.valueAxis.rangeRound = 'both'
        self.chart.valueAxis.strokeWidth = 0
        self.chart.valueAxis.visibleGrid = 1
        self.chart.valueAxis.visibleTicks = 0
        self.chart.valueAxis.visibleAxis = 0
        self.chart.valueAxis.gridStrokeColor = PCMYKColor(70, 0, 36, 36)
        self.chart.valueAxis.gridStrokeWidth = 0.25
        self.chart.valueAxis.valueStep = None  # 3
        self.chart.valueAxis.labels.dx = -3
        # legend
        self._add(self, Legend(), name='legend', validate=None, desc=None)
        self.legend.alignment = 'right'
        self.legend.autoXPadding = 6
        self.legend.boxAnchor = 'sw'
        # series
        self._seriesNames = (
            'BP',
            'Shell Transport & Trading',
            'Liberty ' 'International',
            'Royal Bank of Scotland',
        )
        # self.legend.colorNamePairs = [(constants.COLOR_1, 'MSILF Treasury
        # Institutional'), (constants.COLOR_2, 'Lipper Institutional U.S.
        # Treasury Money Market Average')]
        self.legend.columnMaximum = 3
        self.legend.dx = 8
        self.legend.dy = 6
        self.legend.x = 6
        self.legend.y = 1
        self.legend.dxTextSpace = 4
        self.legend.fontSize = 6
        self.legend.fontName = fontName
        self.legend.strokeColor = None
        self.legend.strokeWidth = 0
        self.legend.subCols.minWidth = 55
        self.legend.variColumn = 1
        self.legend.deltay = 10
        # x label
        self._add(
            self,
            Label(),
            name='XLabel',
            validate=None,
            desc="The label on the horizontal axis",
        )
        self.XLabel._text = ""
        self.XLabel.fontSize = 6
        self.XLabel.height = 0
        self.XLabel.maxWidth = 100
        self.XLabel.textAnchor = 'middle'
        self.XLabel.x = 140
        self.XLabel.y = 10
        # y label
        self._add(
            self,
            Label(),
            name='YLabel',
            validate=None,
            desc="The label on the vertical axis",
        )
        self.YLabel._text = ""
        self.YLabel.angle = 90
        self.YLabel.fontSize = 6
        self.YLabel.height = 0
        self.YLabel.maxWidth = 100
        self.YLabel.textAnchor = 'middle'
        self.YLabel.x = 12
        self.YLabel.y = 80
        self.legend.autoXPadding = 65

    def getContents(self):
        self.legend.colorNamePairs = list(zip(self._colors, self._seriesNames))
        return Drawing.getContents(self)


class ComparisonChart(_DrawingEditorMixin, Drawing):
    """
    Chart Features
    --------------

    This is a Bar Chart that contains a Legend Widget to compare several companies performance
    for a period of last 10 years. Features include:

    - A Legend that can wrap: **legend.columnMaximum=3**

    - Labels for the positive bars are above bars, while labels for negative bars are below bars.
    You can control this through the property **chart.barLabels.boxTarget** which can take
    one of ('normal','anti','lo','hi')

    - Simple category axis - dates are not necessary here.

    This chart was built with our [Diagra](http://www.reportlab.com/software/diagra/) solution.

    Not the kind of chart you looking for? Go [up](..) for more charts, or to see different types of charts click on [ReportLab Charts Gallery](/chartgallery/).
    """

    def __init__(self, width=298, height=164, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        # font
        fontName = kw.get('fontName', 'Helvetica')
        # chart
        self._add(
            self, VerticalBarChart(), name='chart', validate=None, desc=None
        )
        self.chart.width = width - 18  # 280
        self.chart.height = height - 68  # 106
        # chart bars
        self.chart.bars.strokeColor = None
        self.chart.bars.strokeWidth = 0
        self.chart.barSpacing = 4
        self.chart.barWidth = 14
        self.chart.barLabelFormat = '%s'
        self.chart.barLabels.nudge = 5
        self.chart.barLabels.fontName = fontName
        self.chart.barLabels.fontSize = 5
        # categoy axis
        self.chart.categoryAxis.labelAxisMode = 'low'
        self.chart.categoryAxis.labels.angle = 0
        self.chart.categoryAxis.labels.boxAnchor = 'n'
        self.chart.categoryAxis.labels.dy = -6
        self.chart.categoryAxis.labels.fillColor = PCMYKColor(0, 0, 0, 100)
        self.chart.categoryAxis.labels.fontName = fontName
        self.chart.categoryAxis.labels.fontSize = 8
        self.chart.categoryAxis.labels.textAnchor = 'middle'
        self.chart.categoryAxis.tickShift = 1
        self.chart.categoryAxis.visibleTicks = 0
        self.chart.categoryAxis.strokeWidth = 0
        self.chart.categoryAxis.strokeColor = None
        self.chart.groupSpacing = 15
        # value axis
        self.chart.valueAxis.avoidBoundFrac = None
        self.chart.valueAxis.labels.fontName = fontName
        self.chart.valueAxis.labels.fontSize = 8
        self.chart.valueAxis.rangeRound = 'both'
        self.chart.valueAxis.strokeWidth = 0
        self.chart.valueAxis.visibleGrid = 1
        self.chart.valueAxis.visibleTicks = 0
        self.chart.valueAxis.visibleAxis = 0
        self.chart.valueAxis.gridStrokeColor = PCMYKColor(100, 0, 46, 46)
        self.chart.valueAxis.gridStrokeWidth = 0.25
        self.chart.valueAxis.valueStep = None  # 3
        self.chart.valueAxis.labels.dx = -3
        # sample data
        self.chart.data = [
            [
                -2.6000000000000001,
                -0.80000000000000004,
                9.8000000000000007,
                None,
                None,
                None,
                None,
            ],
            [
                -1.8999999999999999,
                1.3999999999999999,
                13.1,
                None,
                None,
                None,
                None,
            ],
            [
                -1.8999999999999999,
                1.3,
                12.199999999999999,
                4.9000000000000004,
                2.2000000000000002,
                5.4000000000000004,
                10.6,
            ],
            [
                -1.7,
                2.0,
                13.300000000000001,
                5.9000000000000004,
                3.2000000000000002,
                6.4000000000000004,
                11.6,
            ],
            [
                -1.8999999999999999,
                1.5,
                13.9,
                4.0999999999999996,
                -1.3,
                3.8999999999999999,
                11.1,
            ],
        ]
        self.chart.categoryAxis.categoryNames = [
            'Q3',
            'YTD',
            '1 Year',
            '3 Year',
            '5 Year',
            '7 Year',
            '10 Year',
        ]
        for i in range(len(self.chart.data)):
            self.chart.bars[i].name = (
                'BP',
                'Shell Transport & Trading',
                'Liberty International',
                'Persimmon',
                'Royal Bank of Scotland',
            )[i]
        # self.width = 400
        # self.height = 200
        self.chart.x = 30
        self.chart.y = 65
        self.chart.bars[0].fillColor = PCMYKColor(0, 100, 100, 40, alpha=85)
        self.chart.bars[1].fillColor = PCMYKColor(23, 51, 0, 4, alpha=85)
        self.chart.bars[2].fillColor = PCMYKColor(100, 60, 0, 50, alpha=85)
        self.chart.bars[3].fillColor = PCMYKColor(66, 13, 0, 22, alpha=85)
        self.chart.bars.fillColor = PCMYKColor(100, 0, 90, 50, alpha=85)

        # legend
        self._add(self, Legend(), name='legend', validate=None, desc=None)
        self.legend.alignment = 'right'
        self.legend.boxAnchor = 'sw'
        self.legend.columnMaximum = 3
        self.legend.x = 30
        self.legend.y = 1
        self.legend.deltay = 10
        self.legend.dx = 8
        self.legend.dy = 6
        self.legend.dxTextSpace = 4
        self.legend.fontSize = 8
        self.legend.fontName = fontName
        self.legend.strokeColor = None
        self.legend.strokeWidth = 0
        self.legend.subCols.minWidth = 55
        self.legend.variColumn = 1
        self.legend.colorNamePairs = Auto(obj=self.chart)
        self.legend.autoXPadding = 65

        # x label
        self._add(
            self,
            Label(),
            name='XLabel',
            validate=None,
            desc="The label on the horizontal axis",
        )
        self.XLabel._text = ""
        self.XLabel.fontSize = 6
        self.XLabel.height = 0
        self.XLabel.maxWidth = 100
        self.XLabel.textAnchor = 'middle'
        self.XLabel.x = 140
        self.XLabel.y = 10

        # y label
        self._add(
            self,
            Label(),
            name='YLabel',
            validate=None,
            desc="The label on the vertical axis",
        )
        self.YLabel._text = ""
        self.YLabel.angle = 90
        self.YLabel.fontSize = 6
        self.YLabel.height = 0
        self.YLabel.maxWidth = 100
        self.YLabel.textAnchor = 'middle'
        self.YLabel.x = 12
        self.YLabel.y = 80


class MultiLineXAxisLabels(_DrawingEditorMixin, Drawing):
    """
    Chart Features
    --------------
    This drawing demonstrates the ability to add multi row text to the X Axis in the chart.
    It also features a long ticks which looks more like a table:

    - The ticks are controlled with the property **chart.categoryAxis.tickDown=36**

    This chart was built with our [Diagra](http://www.reportlab.com/software/diagra/) solution.

    Not the kind of chart you looking for? Go [up](..) for more charts, or to see different types of charts click on [ReportLab Charts Gallery](/chartgallery/).
    """

    def __init__(self, width=400, height=200, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        # font
        fontName = kw.get('fontName', 'Helvetica')
        strokeWidth = kw.get('strokeWidth', 0.5)
        strokeDashArray = (0.3, 1)  # , 0.25
        lineCap = kw.get('lineCap', 1)
        gridStickOut = kw.get('gridStickOut', 4)
        tickOut = kw.get('tickOut', 36)

        # self.width = 400
        # self.height = 200

        self._add(
            self, VerticalBarChart(), name='chart', validate=None, desc=None
        )
        self.chart.width = width - 50  # 350
        self.chart.height = height - 75  # 125
        self.chart.bars[0].fillColor = PCMYKColor(100, 60, 0, 50, alpha=100)
        self.chart.bars[1].fillColor = PCMYKColor(100, 0, 90, 50, alpha=100)
        self.chart.barSpacing = 3
        self.chart.barWidth = 9
        self.chart.groupSpacing = 15
        self.chart.x = 24
        self.chart.y = 54
        self.chart.bars.strokeColor = None
        self.chart.bars.strokeWidth = 0
        # colour list can read its colours from the palette
        colorsList = [
            PCMYKColor(100, 60, 0, 50, alpha=100),
            PCMYKColor(100, 0, 90, 50, alpha=100),
        ]
        for i, color in enumerate(colorsList):
            self.chart.bars[i].fillColor = colorsList[i]
        self.chart.categoryAxis.joinAxisMode = 'bottom'
        self.chart.categoryAxis.labelAxisMode = 'low'
        self.chart.categoryAxis.labels.angle = 0
        self.chart.categoryAxis.labels.boxAnchor = 'n'
        self.chart.categoryAxis.labels.dy = -4
        self.chart.categoryAxis.labels.fillColor = black
        self.chart.categoryAxis.labels.fontName = fontName
        self.chart.categoryAxis.labels.fontSize = 6
        self.chart.categoryAxis.labels.textAnchor = 'middle'
        self.chart.categoryAxis.tickShift = 0
        self.chart.categoryAxis.visibleTicks = 1
        self.chart.categoryAxis.tickDown = tickOut
        self.chart.categoryAxis.strokeDashArray = strokeDashArray
        self.chart.categoryAxis.strokeWidth = strokeWidth
        self.chart.categoryAxis.gridStrokeWidth = strokeWidth
        self.chart.categoryAxis.visibleGrid = 0
        self.chart.categoryAxis.gridStrokeDashArray = strokeDashArray
        self.chart.valueAxis.labels.fontName = fontName
        self.chart.valueAxis.labels.fontSize = 6
        self.chart.valueAxis.labels.rightPadding = 3
        self.chart.valueAxis.drawGridLast = 1
        self.chart.valueAxis.rangeRound = 'both'
        # self.chart.valueAxis.valueStep = 5
        self.chart.valueAxis.minimumTickSpacing = 0.5
        self.chart.valueAxis.maximumTicks = 8
        self.chart.valueAxis.forceZero = 1
        self.chart.valueAxis.avoidBoundFrac = None
        self.chart.valueAxis.gridStrokeDashArray = strokeDashArray
        self.chart.valueAxis.visibleGrid = 1
        self.chart.valueAxis.gridStrokeWidth = strokeWidth
        self.chart.valueAxis.strokeDashArray = strokeDashArray
        self.chart.valueAxis.strokeWidth = strokeWidth
        self.chart.valueAxis.gridStart = self.chart.x - gridStickOut
        self.chart.valueAxis.gridEnd = (
            self.chart.x + self.chart.width + gridStickOut
        )
        self.chart.valueAxis.gridStrokeLineCap = lineCap
        self.chart.valueAxis.visibleTicks = False
        self.chart.valueAxis.strokeColor = None
        # self.legend.alignment = 'right'
        # self.legend.autoXPadding = 6
        # self.legend.boxAnchor = 'sw'
        # self.legend.columnMaximum = 1
        # self.legend.dx = 7
        # self.legend.dxTextSpace = 2
        # self.legend.dy = 7
        # self.legend.fontSize = 6
        # self.legend.strokeColor = None
        # self.legend.strokeWidth = 0
        # self.legend.subCols.minWidth = 55
        # self.legend.variColumn = 1
        # self.legend.x = 26
        # self.legend.y = -12
        # self.legend.fontName = fontName

        self._add(
            self,
            Label(),
            name='XLabel',
            validate=None,
            desc="The label on the horizontal axis",
        )
        self.XLabel._text = ""
        self.XLabel.fontSize = 6
        self.XLabel.height = 0
        self.XLabel.maxWidth = 100
        self.XLabel.textAnchor = 'middle'
        self.XLabel.x = 140
        self.XLabel.y = 10

        self._add(
            self,
            Label(),
            name='YLabel',
            validate=None,
            desc="The label on the vertical axis",
        )
        self.YLabel._text = ""
        self.YLabel.angle = 90
        self.YLabel.fontSize = 6
        self.YLabel.height = 0
        self.YLabel.maxWidth = 100
        self.YLabel.textAnchor = 'middle'
        self.YLabel.x = 12
        self.YLabel.y = 80
        # 0 axis
        self.chart.annotations = [
            lambda c, cA, vA: Line(
                c.x,
                vA(0),
                c.x + c.width,
                vA(0),
                strokeColor=black,
                strokeWidth=strokeWidth,
            )
        ]
        # left vertical
        self.chart.annotations.extend(
            [
                lambda c, cA, vA: Line(
                    c.x,
                    c.y - tickOut,
                    c.x,
                    self.chart.y + c.height + gridStickOut,
                    strokeColor=black,
                    strokeWidth=strokeWidth,
                )
            ]
        )
        # right vertical
        self.chart.annotations.extend(
            [
                lambda c, cA, vA: Line(
                    c.x + c.width,
                    c.y - tickOut,
                    c.x + c.width,
                    self.chart.y + c.height + gridStickOut,
                    strokeColor=black,
                    strokeWidth=0.5,
                )
            ]
        )
        self.chart.data = [
            [
                19.260000000000002,
                32.359999999999999,
                1.78,
                -4.3499999999999996,
                2.1000000000000001,
                5.1200000000000001,
                11.0,
            ],
            [
                18.239999999999998,
                14.85,
                -10.619999999999999,
                -7.8700000000000001,
                0.90000000000000002,
                2.5899999999999999,
                10.869999999999999,
            ],
        ]
        self.chart.categoryAxis.categoryNames = [
            u'Quarterly',
            u'YTD',
            u'1 Year',
            u'3 Year',
            u'5 Year',
            u'10 Year',
            u'Since Inception\n(11/05/1984)',
        ]
        colorsList = (
            PCMYKColor(100, 60, 0, 50, alpha=100),
            PCMYKColor(100, 0, 90, 50, alpha=100),
            PCMYKColor(80, 24, 69, 70, spotName='350c', alpha=100),
            PCMYKColor(0, 0, 0, 40, alpha=100),
            PCMYKColor(0, 0, 0, 100, alpha=100),
        )
        y = self.chart.y - 26
        colWidth = self.chart.width * 1.0 / len(self.chart.data[0])
        for i in range(len(self.chart.data)):
            self.chart.bars[i].fillColor = colorsList[i]
        for h, series in enumerate(self.chart.data):
            for (i, value) in enumerate(series):
                if value is None:
                    text = 'N/A'
                else:
                    text = '%0.2f' % value
                x = self.chart.x + (i + 0.5) * colWidth
                s = String(x, y, text, textAnchor='middle')
                s.fontSize = 6
                s.fillColor = self.chart.bars[h].fillColor
                self.add(s)
            y = y - 8


class BarChartWithTable(_DrawingEditorMixin, Drawing):
    """
    Chart Features
    --------------
    We have added an experimental table legend to our open source library. This table legend
    can align its column values with another widget's columns (or bars, etc ...):

    - The bars are filled with one color and stroked with black color.

    - Bar labels are not displayed, you could achieve that through either setting the
    **barLabels.visible** to False, or not providing a formatting function (or any python callable)
    to the barLabelFormat attribute.

    - Simple category axis - dates are not necessary here.

    This chart was built with our [Diagra](http://www.reportlab.com/software/diagra/) solution.

    Not the kind of chart you looking for? Go [up](..) for more charts, or to see different types of charts click on [ReportLab Charts Gallery](/chartgallery/).
    """

    def __init__(self, width=403, height=163, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        fontName = kw.get('fontName', 'Helvetica')
        fontSize = kw.get('fontSize', 5)
        bFontName = kw.get('boldFontName', 'Times-Bold')
        bFontSize = kw.get('boldFontSize', 7)
        colorsList = [
            PCMYKColor(0, 73, 69, 56),
            PCMYKColor(0, 3, 7, 6),
            PCMYKColor(41, 25, 0, 21),
        ]
        table_height = 45
        legend_width = 100

        self._add(
            self, VerticalBarChart(), name='chart', validate=None, desc=None
        )
        self.chart.width = width - 50 - legend_width
        self.chart.height = height - 50 - table_height  # 将表格的空间留出来
        self.chart.x = 140
        self.chart.y = 75
        self.chart.barWidth = 2
        self.chart.groupSpacing = 5
        self.chart.barSpacing = 0.5
        self.chart.fillColor = None
        self.chart.data = [
            [
                7.7199999999999998,
                7.9400000000000004,
                9.1699999999999999,
                7.04,
                7.7199999999999998,
                8.1699999999999999,
            ],
            [4.46, 1.97, 13.220000000000001, 10.49, 8.5800000000000001, 10.74],
            [
                5.1399999999999997,
                9.5999999999999996,
                5.3099999999999996,
                4.4699999999999998,
                3.5099999999999998,
                4.8399999999999999,
            ],
        ]
        # self.chart.bars.fillColor         = color
        self.chart.bars.strokeWidth = 0.5
        self.chart.bars.strokeColor = PCMYKColor(0, 0, 0, 100)
        for i, color in enumerate(colorsList):
            self.chart.bars[i].fillColor = color
        self.chart.valueAxis.labels.fontName = fontName
        self.chart.valueAxis.labels.fontSize = fontSize
        self.chart.valueAxis.strokeDashArray = (5, 0)
        self.chart.valueAxis.visibleGrid = False
        self.chart.valueAxis.visibleTicks = False
        self.chart.valueAxis.tickLeft = 0
        self.chart.valueAxis.tickRight = 11
        # self.chart.valueAxis.gridStrokeDashArray   = (0,1,0)
        # self.chart.valueAxis.valueStep             = 200
        self.chart.valueAxis.strokeWidth = 0.25
        # self.chart.valueAxis.gridStrokeWidth       = 0.25
        # self.chart.valueAxis.gridStrokeDashArray   = (1,1,1)
        self.chart.valueAxis.avoidBoundFrac = 0  # 1#0.5
        self.chart.valueAxis.rangeRound = 'both'
        self.chart.valueAxis.gridStart = 13
        self.chart.valueAxis.gridEnd = 342
        self.chart.valueAxis.labelTextFormat = (
            None  # DecimalFormatter(1, suffix=None, prefix=None)
        )
        self.chart.valueAxis.forceZero = True
        self.chart.valueAxis.labels.boxAnchor = 'e'
        self.chart.valueAxis.labels.dx = -1
        self.chart.categoryAxis.strokeDashArray = (5, 0)
        # self.chart.categoryAxis.gridStrokeDashArray = (1,1,1)
        self.chart.categoryAxis.visibleGrid = False
        self.chart.categoryAxis.visibleTicks = False
        self.chart.categoryAxis.strokeWidth = 0.25
        self.chart.categoryAxis.tickUp = 5
        self.chart.categoryAxis.tickDown = 0
        self.chart.categoryAxis.labelAxisMode = 'low'
        self.chart.categoryAxis.labels.textAnchor = 'end'
        self.chart.categoryAxis.labels.fillColor = black
        self.chart.categoryAxis.labels.angle = 0
        self.chart.categoryAxis.labels.fontName = bFontName
        self.chart.categoryAxis.labels.fontSize = bFontSize
        # self.chart.categoryAxis.tickShift          = 1
        # self.chart.categoryAxis.strokeDashArray     = (0,1,0)
        # self.chart.categoryAxis.labels.boxAnchor    = 'autox'
        self.chart.categoryAxis.labels.boxAnchor = 'e'
        self.chart.categoryAxis.labels.dx = 7  # -10
        self.chart.categoryAxis.labels.dy = -5
        self.chart.categoryAxis.categoryNames = [
            '200%d' % i for i in range(1, 7)
        ]
        self.chart.bars[0].fillColor = PCMYKColor(100, 60, 0, 50, alpha=100)
        self.chart.bars[1].fillColor = PCMYKColor(23, 51, 0, 4, alpha=100)
        self.chart.bars[2].fillColor = PCMYKColor(100, 0, 90, 50, alpha=100)

        self._add(self, Legend(), name='legend', validate=None, desc=None)
        self.legend.x = 24
        self.legend.y = 75
        self.legend.dx = 8
        self.legend.dy = 5
        self.legend.deltay = 8
        self.legend.fontName = fontName
        self.legend.fontSize = fontSize
        self.legend.strokeWidth = 0.5
        self.legend.strokeColor = PCMYKColor(0, 0, 0, 100)
        self.legend.autoXPadding = 0
        self.legend.variColumn = True
        # 175
        self.legend.subCols.minWidth = legend_width  # self.chart.width / 2  #
        self.legend.colorNamePairs = Auto(obj=self.chart)
        self.legend.dxTextSpace = 5
        self.legend.deltax = 0
        self.legend.alignment = 'right'
        self.legend.columnMaximum = 3
        self.legend.boxAnchor = 'sw'

        self._add(self, TableWidget(), name='table', validate=None, desc=None)
        self.table.width = width
        self.table.height = table_height
        self.table.x = 0
        self.table.y = 0
        self.table.borderStrokeColor = PCMYKColor(0, 12, 24, 36)
        self.table.fillColor = PCMYKColor(0, 3, 7, 6)
        self.table.borderStrokeWidth = 0.5
        self.table.horizontalDividerStrokeColor = PCMYKColor(0, 12, 24, 36)
        self.table.verticalDividerStrokeColor = None
        self.table.horizontalDividerStrokeWidth = 0.5
        self.table.verticalDividerStrokeWidth = 0
        self.table.dividerDashArray = None
        self.table.data = [
            ['BP', None, '7.72', '7.94', '9.17', '7.04', '7.72', '8.17'],
            [
                'Shell Transport & Trading',
                None,
                '4.46',
                '1.97',
                '13.22',
                '10.49',
                '8.58',
                '10.74',
            ],
            [
                'Liberty International',
                None,
                '5.14',
                '9.60',
                '5.31',
                '4.47',
                '3.51',
                '4.84',
            ],
        ]
        self.table.boxAnchor = 'sw'
        self.table.fontName = bFontName
        self.table.fontSize = bFontSize
        self.table.fontColor = black
        self.table.alignment = 'left'
        self.table.textAnchor = 'start'
        for i in range(len(self.chart.data)):
            self.chart.bars[i].name = self.table.data[i][0]


class VerticalLabels(_DrawingEditorMixin, Drawing):
    """
    Chart Features
    --------------

    - The bar labels are vertical, this is controlled through the **chart.barLabels.angle** property.

    - Simple category axis: dates are not necessary here.

    This chart was built with our [Diagra](http://www.reportlab.com/software/diagra/) solution.

    Not the kind of chart you looking for? Go [up](..) for more charts, or to see different types of charts click on [ReportLab Charts Gallery](/chartgallery/).
    """

    def __init__(self, width=348, height=146, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        # setting font
        fontName = kw.get('fontName', 'Helvetica')
        # fontSize = 6 for bar labels, 7 for legend, 8 for axis labels
        # adding a vertical bar chart
        self._add(
            self, VerticalBarChart(), name='chart', validate=None, desc=None
        )
        # chart settings
        # self.chart.width = 334  # it takes all the area - below also works
        self.chart.x = 5
        self.chart.y = 35 + 15  # 底部legend高度 + x轴值高度
        self.chart.width = self.width - self.chart.x
        # self.chart.height = 91
        self.height = height - self.chart.y
        self.chart.fillColor = None
        # bar properties
        self.chart.groupSpacing = 20
        self.chart.barSpacing = 1
        self.chart.bars.strokeWidth = 0
        self.chart.bars.strokeColor = None  # self.chart.fillColor
        self.chart.barLabels.angle = 90
        self.chart.barLabelFormat = DecimalFormatter(2)
        self.chart.barLabels.boxAnchor = 'w'
        self.chart.barLabels.boxFillColor = None
        self.chart.barLabels.boxStrokeColor = None
        self.chart.barLabels.fontName = fontName
        self.chart.barLabels.fontSize = 5
        self.chart.barLabels.dy = 3
        self.chart.barLabels.boxTarget = 'hi'
        # value axis properties
        self.chart.valueAxis.labels.fontName = fontName
        self.chart.valueAxis.labels.fontSize = 8
        self.chart.valueAxis.strokeDashArray = (5, 0)
        self.chart.valueAxis.visibleGrid = False
        self.chart.valueAxis.strokeWidth = 0.25
        self.chart.valueAxis.avoidBoundFrac = 0.5
        self.chart.valueAxis.rangeRound = 'both'
        self.chart.valueAxis.gridStart = 13
        self.chart.valueAxis.gridEnd = 342
        self.chart.valueAxis.labelTextFormat = DecimalFormatter(
            0, suffix=None, prefix=None
        )
        self.chart.valueAxis.labels.boxAnchor = 'e'
        self.chart.valueAxis.labels.dx = -1
        self.chart.valueAxis.visibleTicks = 0
        # category axis properties
        self.chart.categoryAxis.strokeDashArray = (5, 0)
        self.chart.categoryAxis.visibleGrid = False
        self.chart.categoryAxis.visibleTicks = True
        self.chart.categoryAxis.strokeWidth = 0.25
        self.chart.categoryAxis.tickUp = 3
        self.chart.categoryAxis.tickDown = 0
        self.chart.categoryAxis.labelAxisMode = 'low'
        self.chart.categoryAxis.labels.textAnchor = 'middle'
        self.chart.categoryAxis.labels.boxAnchor = 'n'
        self.chart.categoryAxis.labels.fillColor = black
        self.chart.categoryAxis.labels.angle = 0
        self.chart.categoryAxis.labels.fontName = fontName
        self.chart.categoryAxis.labels.fontSize = 7  # 8
        self.chart.categoryAxis.labels.dx = 0  # -10
        self.chart.categoryAxis.labels.dy = -2

        # adding a horizontal line to the chart
        self.chart.annotations = [
            lambda c, cA, vA: Line(
                c.x, c.y, c.x + c.width, c.y, strokeColor=black, strokeWidth=0.5
            )
        ]
        # sample data
        colorsList = [
            PCMYKColor(0, 0, 0, 100, spotName='XXX X', alpha=100),
            PCMYKColor(50, 0, 25, 30, spotName='7475C', alpha=100),
            PCMYKColor(50, 0, 25, 30, spotName='7475C', density=40, alpha=100),
            PCMYKColor(0, 0, 0, 50, spotName='XXX X', alpha=100),
            PCMYKColor(0, 0, 0, 25, spotName='XXX X', alpha=100),
            PCMYKColor(0, 0, 0, 40, spotName='XXX X', alpha=100),
            PCMYKColor(50, 0, 25, 30, spotName='7475C', density=25, alpha=100),
            PCMYKColor(0, 0, 0, 25, spotName='XXX X', alpha=100),
        ]
        series = (
            'BP',
            'Shell Transport & Trading',
            'Liberty International',
            'Persimmon',
            'Royal Bank of Scotland',
        )
        for i, s in enumerate(series):
            self.chart.bars[i].name = s
        self.chart.data = [
            [
                -9.0299999999999994,
                -9.0299999999999994,
                -4.5800000000000001,
                7.2699999999999996,
                11.109999999999999,
            ],
            [
                -9.4399999999999995,
                -9.4399999999999995,
                -5.0700000000000003,
                5.8499999999999996,
                0.0,
            ],
            [
                2.1699999999999999,
                2.1699999999999999,
                7.6600000000000001,
                0.0,
                4.5800000000000001,
            ],
            [
                -5.1399999999999997,
                -5.1399999999999997,
                0.0,
                8.1699999999999999,
                11.380000000000001,
            ],
            [
                -4.8799999999999999,
                -4.8799999999999999,
                0.02,
                5.8099999999999996,
                8.6999999999999993,
            ],
        ]
        for i, _ in enumerate(self.chart.data):
            self.chart.bars[i].fillColor = colorsList[i]
        self.chart.categoryAxis.categoryNames = [
            'Quarter',
            'YTD',
            '1-year',
            '3-year',
            '5-year',
        ]
        self.chart.bars[0].fillColor = PCMYKColor(
            23, 51, 0, 4, spotName='XXX X', alpha=100
        )
        self.chart.bars[2].fillColor = PCMYKColor(100, 60, 0, 50, alpha=100)
        self.chart.bars[3].fillColor = PCMYKColor(100, 0, 90, 50, alpha=100)
        self.chart.bars[4].fillColor = PCMYKColor(0, 100, 100, 40, alpha=100)
        self.chart.bars[1].fillColor = PCMYKColor(66, 13, 0, 22, alpha=100)

        # adding legend
        self._add(self, Legend(), name='legend', validate=None, desc=None)
        self.legend.dx = 7
        self.legend.dy = 7
        self.legend.x = 24
        self.legend.y = 35  # 底部 legend 高度
        self.legend.boxAnchor = 'nw'
        self.legend.deltax = 0
        self.legend.deltay = 10
        self.legend.columnMaximum = 3
        self.legend.fontName = fontName
        self.legend.fontSize = 6
        self.legend.alignment = 'right'
        self.legend.strokeWidth = 0
        self.legend.strokeColor = None
        self.legend.autoXPadding = 0
        self.legend.dxTextSpace = 7
        self.legend.variColumn = True
        self.legend.subCols.minWidth = 157  # self.chart.width/2
        self.legend.colorNamePairs = Auto(obj=self.chart)


class DualBarChartsOnOneCanvasBase(HorizontalBarChart):
    def __init__(drawing, _fontName, _fontSize, color):
        HorizontalBarChart.__init__(drawing)
        drawing.x = 45
        drawing.y = 24
        drawing.width = 52
        drawing.height = 154
        drawing.fillColor = None
        drawing.reversePlotOrder = 1

        # chart bars
        drawing.barLabels.fontName = _fontName
        drawing.barLabels.fontSize = _fontSize
        drawing.groupSpacing = 4
        drawing.barWidth = 5
        drawing.barSpacing = 0
        drawing.bars.fillColor = color
        drawing.bars.strokeWidth = 0
        drawing.bars.strokeColor = None
        drawing.barLabels.angle = 0
        drawing.barLabelFormat = DecimalFormatter(2, suffix='%')
        drawing.barLabels.boxAnchor = 'w'
        drawing.barLabels.boxFillColor = None
        drawing.barLabels.boxStrokeColor = None
        drawing.barLabels.dx = 5
        drawing.barLabels.dy = 0
        drawing.barLabels.boxTarget = 'hi'
        # apply colours
        # for i, _ in enumerate(drawing.data ): drawing.bars[i].fillColor = color
        # value axis
        drawing.valueAxis.labels.fontName = _fontName
        drawing.valueAxis.labels.fontSize = _fontSize
        # drawing.valueAxis.strokeDashArray       = (5,0)
        drawing.valueAxis.visibleAxis = False
        drawing.valueAxis.visibleGrid = False
        drawing.valueAxis.visibleTicks = False
        # drawing.valueAxis.gridStrokeDashArray   = (0,1,0)
        # drawing.valueAxis.valueStep             = 200
        # drawing.valueAxis.strokeWidth           = 0.25
        # drawing.valueAxis.gridStrokeWidth       = 0.25
        # drawing.valueAxis.gridStrokeDashArray   = (1,1,1)
        # drawing.valueAxis.avoidBoundFrac        = 0#1#0.5
        # drawing.valueAxis.rangeRound            ='both'
        # drawing.valueAxis.gridStart             = 13
        # drawing.valueAxis.gridEnd               = 342
        # drawing.valueAxis.labelTextFormat        = DecimalFormatter(1, suffix=None, prefix=None)
        # drawing.valueAxis.labels.boxAnchor       = 'autoy'
        drawing.valueAxis.forceZero = True
        # drawing.valueAxis.labels.boxAnchor       = 'e'
        # drawing.valueAxis.labels.dx              = 0
        drawing.valueAxis.visibleLabels = 0
        # category axis
        drawing.categoryAxis.labels.fontName = _fontName
        drawing.categoryAxis.labels.fontSize = _fontSize + 0.5
        drawing.categoryAxis.strokeDashArray = (5, 0)
        # drawing.categoryAxis.gridStrokeDashArray = (1,1,1)
        drawing.categoryAxis.visibleGrid = False
        drawing.categoryAxis.visibleTicks = (
            False  # hidding the ticks remove the label
        )
        drawing.categoryAxis.tickLeft = (
            0  # a workaround is to set the tick length
        )
        drawing.categoryAxis.tickRight = 0  # to zero.
        drawing.categoryAxis.strokeWidth = 0.25
        drawing.categoryAxis.labelAxisMode = 'low'
        drawing.categoryAxis.labels.textAnchor = 'end'
        drawing.categoryAxis.labels.fillColor = black
        drawing.categoryAxis.labels.angle = 0
        # drawing.chart.categoryAxis.tickShift          = 1
        drawing.categoryAxis.labels.dx = -5
        drawing.categoryAxis.labels.dy = 0
        # drawing.categoryAxis.strokeDashArray     = (0,1,0)
        drawing.categoryAxis.labels.boxAnchor = 'e'
        drawing.categoryAxis.labels.leading = 5
        # drawing.categoryAxis.labels.dx           = -10
        # drawing.categoryAxis.labels.dy           = -5
        drawing.categoryAxis.reverseDirection = 1
        drawing.categoryAxis.joinAxisMode = 'left'
        drawing.data = [
            [
                10.9,
                10.84,
                15.99,
                18.75,
                14.75,
                9.1300000000000008,
                9.2100000000000009,
                5.21,
                2.3500000000000001,
                2.8799999999999999,
                0.0,
            ],
            [
                8.9900000000000002,
                11.210000000000001,
                11.859999999999999,
                17.0,
                12.59,
                11.4,
                12.279999999999999,
                4.7199999999999998,
                4.4699999999999998,
                5.4900000000000002,
                0.0,
            ],
        ]
        drawing.categoryAxis.categoryNames = (
            u'Consumer\nStaples',
            u'Consumer\nDiscretionary',
            u'Energy',
            u'Financials',
            u'Health Care',
            u'Industrials',
            u'Information\nTechnology',
            u'Materials',
            u'Telecomm.\nServices',
            u'Utilities',
            u'Other',
        )


class DualBarChartsOnOneCanvas(_DrawingEditorMixin, Drawing):
    """
    Chart Features
    --------------
    Dual Bar charts on one canvas. Bar charts are just another widget in ReportLab's library
    you could add as many of them as you want in your drawing:

    - The two charts share one legend.

    This chart was built with our [Diagra](http://www.reportlab.com/software/diagra/) solution.

    Not the kind of chart you looking for? Go [up](..) for more charts, or to see different types of charts click on [ReportLab Chart Gallery](/chartgallery/).
    """

    def __init__(self, width=264, height=190, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        # font
        self._fontNameBook = 'Helvetica'
        self._fontNameDemi = 'Helvetica'
        self._fontSize = 5
        # colours
        color = PCMYKColor(0, 51, 100, 1)

        legend_y = 18
        chart_y = 18
        y_value_width = 50
        title_height = 20
        chart_interval = 20  # 两个图表垂直间隔
        legend_interval = 20  # 图表和图例间隔
        # chart
        self._add(
            self,
            DualBarChartsOnOneCanvasBase(
                self._fontNameBook, self._fontSize, color
            ),
            name='chart1',
            validate=None,
            desc=None,
        )
        self.chart1.x = y_value_width
        self.chart1.y = chart_y + (legend_interval / 2)
        self.chart1.width = width / 2 - y_value_width - (chart_interval / 2)
        self.chart1.height = (
            height - legend_y - title_height - (legend_interval / 2)
        )
        self.chart1.bars[0].fillColor = PCMYKColor(100, 60, 0, 50, alpha=85)
        self.chart1.bars[1].fillColor = PCMYKColor(66, 13, 0, 22, alpha=85)
        # chart 2
        self._add(
            self,
            DualBarChartsOnOneCanvasBase(
                self._fontNameBook, self._fontSize, color
            ),
            name='chart2',
            validate=None,
            desc=None,
        )
        self.chart2.x = width / 2 + y_value_width + (chart_interval / 2)  # 182
        self.chart2.y = chart_y + (legend_interval / 2)
        self.chart2.width = width / 2 - y_value_width - (chart_interval / 2)
        self.chart2.height = (
            height - legend_y - title_height - (legend_interval / 2)
        )
        self.chart2.data = [
            [
                0.85999999999999999,
                5.2599999999999998,
                2.1899999999999999,
                0.94999999999999996,
                8.4600000000000009,
                11.220000000000001,
                3.25,
                3.2799999999999998,
                8.7400000000000002,
                14.4,
                41.380000000000003,
            ],
            [
                0.050000000000000003,
                3.0299999999999998,
                0.26000000000000001,
                0.01,
                1.3799999999999999,
                3.2599999999999998,
                0.01,
                0.0,
                0.0,
                92.0,
                0.0,
            ],
        ]
        self.chart2.categoryAxis.categoryNames = [
            'Asset Backed\nSecurities',
            'US\nTreasury/Agency',
            'Commercial\nMortgage Backed',
            'High Yield\nCorporate',
            'Investment Grade\nCorporate',
            'Mortgage Backed',
            'Govt Emerging\nMarkets',
            'Non US Currency',
            'TIPS',
            'Cash',
            'Other',
        ]
        self.chart2.bars[0].fillColor = PCMYKColor(100, 60, 0, 50, alpha=85)
        self.chart2.bars[1].fillColor = PCMYKColor(100, 0, 90, 50, alpha=85)

        # legend
        self._add(self, Legend(), name='legend', validate=None, desc=None)
        self.legend.fontName = self._fontNameBook
        self.legend.fontSize = self._fontSize + 0.5
        self.legend.boxAnchor = 'nw'
        self.legend.x = y_value_width  # ３
        self.legend.y = legend_y
        self.legend.deltax = 0
        self.legend.deltay = 10
        self.legend.columnMaximum = 3
        self.legend.alignment = 'right'
        self.legend.strokeWidth = 0
        self.legend.strokeColor = None
        self.legend.autoXPadding = 0
        self.legend.dx = 4
        self.legend.dy = 4
        self.legend.variColumn = True
        self.legend.dxTextSpace = 4
        self.legend.variColumn = True
        # self.legend.subCols.minWidth = self.chart1.width/2
        # self.legend.colorNamePairs   = Auto(obj=self.chart1)
        self.legend.colorNamePairs = [
            (PCMYKColor(100, 60, 0, 50, alpha=85), u'Microsoft'),
            (PCMYKColor(66, 13, 0, 22, alpha=85), u'Russel 2000 Index'),
            (PCMYKColor(100, 0, 90, 50, alpha=85), u'NASDAQ Composite Index'),
        ]
        self.legend.deltay = 5
        self.legend.y = 20
        # self.chart1.categoryAxis.reverseDirection     = 1
        # self.chart1.reversePlotOrder = 1

        # label1
        self._add(self, Label(), name='label1', validate=None, desc=None)
        self.label1.boxAnchor = 'nw'
        self.label1.x = 0  # self.chart1.x
        self.label1.y = self.height
        self.label1.fontName = self._fontNameDemi
        self.label1.fontSize = 8
        self.label1._text = 'Equity Composition'
        # label2
        self._add(self, Label(), name='label2', validate=None, desc=None)
        self.label2.x = self.chart2.x - self.chart1.x
        self.label2.y = self.height
        self.label2.fontName = self._fontNameDemi
        self.label2.fontSize = 8
        self.label2.angle = 0
        # self.label2.boxAnchor = 's'
        self.label2.textAnchor = 'middle'
        self.label2.boxAnchor = 'nw'
        self.label2._text = 'Fixed Income Composition'


class VBCMixedStackedParallel(_DrawingEditorMixin, Drawing):
    """
    Chart Features
    --------------
    This is a simple vertical barchart with mixed stacked & parallel bars

    - The attributes which control the label position in this case are
      **chart.categoryAxis.style='mixed' and .chart.seriesOrder=((0,),(0,1))
      The mixed style uses seriedOrder to determine both sequence and structure,
      each subtuple indicates a stacked bar, the integers indicate
      which series is used. Series may be repeated, missing series are added
      at the end as unstacked bars.

    This chart was built with our
       [Diagra](http://www.reportlab.com/software/diagra/) solution.

    Not the kind of chart you looking for? Go [up](..)
    for more charts, or to see different types of charts click on
       [ReportLab Charts Gallery](/chartgallery/).
    """

    def __init__(self, width=400, height=200, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        self._add(
            self, VerticalBarChart(), name='chart', validate=None, desc=None
        )
        self.chart.x = 30
        self.chart.y = 20
        self.chart.width = self.width - self.chart.x - 10
        self.chart.height = self.height - self.chart.y - 10
        self.chart.reversePlotOrder = 0
        self.chart.valueAxis.forceZero = 1
        self.chart.seriesOrder = ((0,), (0, 1))
        self.chart.categoryAxis.style = 'mixed'
        self.chart.barSpacing = 1
        self.chart.data = [(10.8, 9.6, 9, 7.9), (0.5, 0.7, 0.5, 0.7)]
        self.chart.bars[2].fillColor = blue.clone(alpha=0.8)
        self.chart.data = [(10.8, 9.6, 9, 7.9), (0.5, 0.7, 0.6, 0.9)]
        self.chart.categoryAxis.categoryNames = ['A', 'B', 'C', 'D']
        self._add(self, Label(), name='vaxisl', validate=None, desc=None)
        self.vaxisl.fontName = 'Helvetica'
        self.vaxisl._text = 'Widgets'
        self.vaxisl.boxAnchor = 's'
        self.vaxisl.angle = 90
        self.vaxisl.x = 12
        self.vaxisl.y = self.chart.y + self.chart.height * 0.5


class VBCMixedStackedParallel3D(_DrawingEditorMixin, Drawing):
    """
    Chart Features
    --------------
    This is a simple vertical 3D barchart with mixed stacked & parallel bars

    - The attributes which control the label position in this case are
      **chart.categoryAxis.style='mixed' and .chart.seriesOrder=((0,),(0,1))
      The mixed style uses seriedOrder to determine both sequence and structure,
      each subtuple indicates a stacked bar, the integers indicate
      which series is used. Series may be repeated, missing series are added at
      the end as unstacked bars.

    This chart was built with our
       [Diagra](http://www.reportlab.com/software/diagra/) solution.

    Not the kind of chart you looking for? Go [up](..)
    for more charts, or to see different types of charts click on
       [ReportLab Charts Gallery](/chartgallery/).
    """

    def __init__(self, width=400, height=200, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        self._add(
            self, VerticalBarChart3D(), name='chart', validate=None, desc=None
        )
        self.chart.x = 30
        self.chart.y = 20
        self.chart.width = self.width - self.chart.width - 10
        self.chart.height = self.height - self.chart.y - 20
        self.chart.reversePlotOrder = 0
        self.chart.valueAxis.forceZero = 1
        self.chart.seriesOrder = ((0,), (0, 1))
        self.chart.categoryAxis.style = 'mixed'
        self.chart.barSpacing = 1
        self.chart.data = [(10.8, 9.6, 9, 7.9), (0.5, 0.7, 0.5, 0.7)]
        self.chart.bars[2].fillColor = blue.clone(alpha=0.8)
        self.chart.data = [(10.8, 9.6, 9, 7.9), (0.5, 0.7, 0.6, 0.9)]
        self.chart.categoryAxis.categoryNames = ['A', 'B', 'C', 'D']
        self._add(self, Label(), name='vaxisl', validate=None, desc=None)
        self.vaxisl.fontName = 'Helvetica'
        self.vaxisl._text = 'Widgets'
        self.vaxisl.boxAnchor = 's'
        self.vaxisl.angle = 90
        self.vaxisl.x = 12
        self.vaxisl.y = self.chart.y + self.chart.height * 0.5


class HBarChartWRedXValueAxisNegLabels(_DrawingEditorMixin, Drawing):
    """
    Chart Features
    --------------
    This is a simple horizontal barchart whose XVAlueAxis is modified to make the negative tick labels turn red.

    - The xValueAxis has negative tick labels coloured red. That is accomplished by changing the Label attribute customDrawChanger to be an instance of
    reportlab.graphics.charts.textlabels.RedNegativeChanger.

    This chart was built with our [Diagra](http://www.reportlab.com/software/diagra/) solution.

    Not the kind of chart you looking for? Go [up](..) for more charts, or to see different types of charts click on [ReportLab Charts Gallery](/chartgallery/).
    """

    def __init__(self, width=400, height=200, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        self._add(
            self, HorizontalBarChart(), name='chart', validate=None, desc=None
        )
        self.chart.y = 20
        self.chart.data = [(100, -110, 120, 130), (70, 80, 85, 90)]
        self.chart.width = self.width - 2 * self.chart.x
        self.chart.height = self.height - self.chart.y - 5
        self.chart.valueAxis.labels.customDrawChanger = RedNegativeChanger()
        self.chart.bars[0].fillColor = PCMYKColor(100, 60, 0, 50, alpha=85)
        self.chart.bars[1].fillColor = PCMYKColor(100, 0, 90, 50, alpha=85)


class VBarChartWLineBarLabels(_DrawingEditorMixin, Drawing):
    """
    Chart Features
    --------------
    This is a simple vertical barchart with bar labels connected to the top and bottom of the chart depending on the sign of the data:

    - The bars have labels which are connected to the bars by lines. If the bar is positive the label is at the top else it will be at the chart bottom.

    - The attributes which control the label position in this case are **chart.barLabels.fixedEnd = LabelOffset()**
    - the labels will end at a dynamically controlled offset.
    - **self.chart.barLabels.fixedEnd.posMode='high'**
    - positive bars will be at the top of the chart: **self.chart.barLabels.fixedEnd.pos = 10**
    - negative bars will have labels at the bottom: **chart.barLabels.fixedEnd.negMode='low'**
    - with this y offset: **chart.barLabels.fixedEnd.neg = -10**
    - the normal (positive case) labels will be anchored south: **chart.barLabels.boxAnchor='s'**
    - Negative cases 'do the 'right thing' for boxAnchor and dy: **self.chart.barLabels.dy = -1**

    This chart was built with our [Diagra](http://www.reportlab.com/software/diagra/) solution.

    Not the kind of chart you looking for? Go [up](..) for more charts, or to see different types of charts click on [ReportLab Charts Gallery](/chartgallery/).
    """

    def __init__(self, width=400, height=200, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        self._add(
            self, VerticalBarChart(), name='chart', validate=None, desc=None
        )
        self.chart.barLabelFormat = '%s'
        self.chart.barLabels.lineStrokeColor = blue
        self.chart.barLabels.lineStrokeWidth = 1
        self.chart.y = 20
        self.chart.width = self.width - self.chart.x - 5
        self.chart.height = self.height - 2 * self.chart.y
        self.chart.data = [(100, -110), (25, -30)]
        self.chart.barLabels.fixedEnd = LabelOffset()
        self.chart.barLabels.fixedEnd.posMode = 'high'
        self.chart.barLabels.fixedEnd.negMode = 'low'
        self.chart.barLabels.fixedEnd.pos = 10
        self.chart.barLabels.fixedEnd.neg = -10
        self.chart.barLabels.boxAnchor = 's'
        self.chart.barLabels.dy = -1
        self.chart.bars[0].fillColor = PCMYKColor(100, 60, 0, 50, alpha=85)
        self.chart.bars[1].fillColor = PCMYKColor(100, 0, 90, 50, alpha=85)


class VBarChartWLineIndicatedBarLabels(_DrawingEditorMixin, Drawing):
    """
    This is a simple vertical barchart with bar labels connected to the top and bottom of the chart depending on the sign of the data. Unlike the 01 version this chart connects the axis end of the bar to the label.

    Chart Features
    --------------

    This chart demonstrates different unique features such as

    - The bars have labels which are connected to the bars by lines. If the bar is positive the label is at the top else it will be at the chart bottom.

    - The attributes which control the label position in this case are
        - self.chart.barLabels.fixedEnd = LabelOffset()
          the labels will end at a dynamically controlled offset.

        - self.chart.barLabels.fixedEnd.posMode='low'
          positive bars will be at the bottom of the chart

        - self.chart.barLabels.fixedEnd.pos = -10
          with this offset.

        - self.chart.barLabels.fixedEnd.negMode='high'
          negative bars will have labels at the top

        - self.chart.barLabels.fixedEnd.neg = 10
          with this y offset

        - self.chart.barLabels.boxAnchor='n'
          the normal (positive case) labels will be anchored st their north side.

        - self.chart.barLabels.dy = -1
          with this small adjustment. Negative cases 'do the 'right thing' for boxAnchor and dy.

        - self.chart.barLabels.fixedStart = LabelOffset()
          this object fixes the start of the lines

        - self.chart.barLabels.fixedStart.posMode='axis'
          at the axis for both positive

        - self.chart.barLabels.fixedStart.negMode='axis'
          and negative bars.

    This chart was built with our [Diagra][dialink] solution.

    Not the kind of chart you looking for? Do not worry go [up][up_link] for more charts, or to see different types of charts click on [ReportLab Charts Gallery][gallink].

    [uplink]: ..
    [gallink]: /chartgallery/ "ReportLab Charts Gallery"
    [dialink]: http://www.reportlab.com/software/diagra/
    """

    def __init__(self, width=400, height=200, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        self._add(
            self, VerticalBarChart(), name='chart', validate=None, desc=None
        )
        self.chart.barLabelFormat = '%s'
        self.chart.barLabels.lineStrokeColor = blue
        self.chart.barLabels.lineStrokeWidth = 1
        self.chart.y = 20
        self.chart.width = self.width - self.chart.x - 5
        self.chart.height = self.height - 2 * self.chart.y
        self.chart.data = [(100, -110), (25, -30)]
        self.chart.barLabels.fixedEnd = LabelOffset()
        self.chart.barLabels.fixedEnd.posMode = 'low'
        self.chart.barLabels.fixedEnd.pos = -10
        self.chart.barLabels.fixedEnd.negMode = 'high'
        self.chart.barLabels.fixedEnd.neg = 10
        self.chart.barLabels.boxAnchor = 'n'
        self.chart.barLabels.dy = 1
        self.chart.barLabels.fixedStart = LabelOffset()
        self.chart.barLabels.fixedStart.posMode = 'axis'
        self.chart.barLabels.fixedStart.negMode = 'axis'
