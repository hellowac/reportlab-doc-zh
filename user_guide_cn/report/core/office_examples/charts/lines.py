"""
Line with markers (serious)
来源: https://www.reportlab.com/chartgallery/line/LineChart01/?iframe=true
&width=900&height=500&ajax=true
"""
from reportlab.lib.colors import purple, PCMYKColor, black, pink, green, blue
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.legends import LineLegend
from reportlab.graphics.charts.lineplots import SimpleTimeSeriesPlot
from reportlab.graphics.shapes import Drawing, Rect, Line, String
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


def line_with_smiley_marker_serious(
    width=258, height=150, font_name='Helvetica', font_size=7
):
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

    chart = LinePlot()
    chart.width = width - 46  # 留出一部分给容器(坐标轴)
    chart.height = height - 60  # 留出一部分给title(坐标轴)
    chart.y = 16
    chart.x = 32
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
    chart.lines.symbol.x = 0
    chart.lines.symbol.strokeWidth = 0
    chart.lines.symbol.arrowBarbDx = 5
    chart.lines.symbol.strokeColor = PCMYKColor(0, 0, 0, 0, alpha=100)
    chart.lines.symbol.fillColor = None
    chart.lines.symbol.arrowHeight = 5
    chart.lines.symbol.kind = 'FilledCross'
    chart.lines.symbol.size = 5
    chart.lines.symbol.angle = 45

    legend = LineLegend()
    legend.fontName = font_name
    legend.fontSize = font_size
    legend.alignment = 'right'
    legend.dx = 5
    legend.colorNamePairs = [
        (PCMYKColor(0, 100, 100, 40, alpha=100), 'Bovis Homes'),
        (PCMYKColor(100, 0, 90, 50, alpha=100), 'HSBC Holdings'),
    ]
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

    drawing = Drawing(width, height)
    drawing.add(chart, 'chart')
    drawing.add(legend, 'legend')

    return drawing


def line_with_smiley_marker_silly(
    width=258, height=150, font_name='Helvetica', font_size=7
):
    """
    Chart Features
    ==============

    This chart is closely related to the 'serious' line chart
    with markers. The key attributes that have changed are:

    - **chart.lines.symbol.kind** was changed from 'Smiley' to 'FilledCross'
    - **chart.lines.symbol.size** was changed from 15 to 5
    - **chart.lines.symbol.angle** was changed from 0 to 45 in order
    to rotate the crosses
    - **legend.columnMaximum** was changed from 2 to 1, forcing the
    legend to fall into a single row with two columns
    - **legend.y** was reduced to bring the row down
    - **legend.x** was reduced to move it to the left across the chart

     该图表与带有标记的“silly”折线图紧密相关。 更改的关键属性是：

    - **chart.lines.symbol.kind** 从“ Smiley”更改为“ FilledCross”
    - **chart.lines.symbol.size** 从15改为5
    - **chart.lines.symbol.angle** 从0更改为45以旋转十字
    - **legend.columnMaximum** 从2更改为1，迫使图例分成两列的单行
    - **legend.y** 被减少以减少行数
    - **legend.x** 减少到将其移到图表的左侧
    """

    chart = LinePlot()
    chart.y = 16
    chart.x = 32
    chart.width = width - 46  # 留出一部分给容器(坐标轴)
    chart.height = height - 60  # 留出一部分给title(坐标轴)
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

    # legend
    legend = LineLegend()
    legend.y = 145
    legend.fontName = font_name
    legend.fontSize = font_size
    legend.alignment = 'right'
    legend.deltax = 1
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
    chart.lines.symbol.kind = 'Smiley'
    chart.lines.symbol.size = 15
    chart.lines.symbol.strokeColor = PCMYKColor(0, 0, 0, 0, alpha=100)
    chart.lines.symbol.fillColor = None
    chart.lines.symbol.arrowHeight = 5
    legend.x = 175
    legend.dxTextSpace = 7
    legend.deltay = 0
    legend.boxAnchor = 'nw'
    legend.subCols.dx = 0
    legend.dy = 5
    legend.subCols.dy = -2
    legend.subCols.rpad = 0
    legend.columnMaximum = 2

    drawing = Drawing(width, height)
    drawing.add(chart, 'chart')
    drawing.add(legend, 'legend')
    return drawing


def line_with_background_color(
    width=400, height=200, font_name='Helvetica', font_size=7
):
    """
    Chart Features
    ============

    There is a canvas background which is a light blue rectangle with same size and dimension of the drawing:

    - **background.fillColor** sets the CMYK fill color
    - **background.height**, **background.width**, **background.x**, and **background.y** define the size and position of the fill.
    - **background.strokeColor** sets the color of the dotted border.
    - **background.strokeDashArray** sets the type of dash. (3,2) gives the relative lengths of the filled and empty space.
    - **background.strokeWidth** gives the weight of the border
    - Note also that **legend.colorNamePairs** is set automatically based on the colors and names of the lines. This makes a lot of sense compared to other examples in which these are defined separately and may differ from the lines they are associated with.
    """
    chart = LinePlot()
    chart.width = width - 46  # 留出一部分给容器(坐标轴)
    chart.height = height - 60  # 留出一部分给title(坐标轴)
    chart.y = 55
    chart.x = 23
    chart.xValueAxis = NormalDateXValueAxis()
    chart.yValueAxis.visibleGrid = 1
    chart.yValueAxis.visibleAxis = 0
    chart.yValueAxis.visibleTicks = 0
    chart.yValueAxis.labels.fontName = font_name
    chart.yValueAxis.labels.fontSize = 8
    chart.yValueAxis.labelTextFormat = '%0.0f'
    chart.yValueAxis.strokeWidth = 0
    chart.yValueAxis.gridStrokeWidth = 0.25
    chart.yValueAxis.labels.rightPadding = 5
    chart.yValueAxis.maximumTicks = 15
    chart.yValueAxis.rangeRound = 'both'
    chart.yValueAxis.avoidBoundFrac = 0.1
    chart.yValueAxis.labels.dx = 3
    chart.yValueAxis.forceZero = 1
    chart.xValueAxis.labels.boxAnchor = 'autox'
    chart.xValueAxis.xLabelFormat = '{yy}'
    chart.xValueAxis.labels.fontName = font_name
    chart.xValueAxis.labels.fontSize = 8
    chart.xValueAxis.strokeWidth = 0
    chart.xValueAxis.visibleAxis = 0
    chart.xValueAxis.visibleTicks = 0
    chart.xValueAxis.labels.rightPadding = 2
    chart.xValueAxis.maximumTicks = 30
    chart.xValueAxis.forceFirstDate = 1
    # sample data
    chart.data = [
        [
            (19910301, 94.260000000000005),
            (19910301, 102.25),
            (19920301, 101.47),
            (19930301, 134.84999999999999),
            (19940301, 121.52),
            (19950301, 145.87),
            (19960301, 166.0),
            (19970301, 172.91),
            (19980301, 212.83000000000001),
            (19990301, 391.86000000000001),
            (20000301, 267.38999999999999),
            (20010301, 218.22),
            (20020301, 161.50999999999999),
            (20030301, 211.46000000000001),
            (20040301, 245.16),
            (20050301, 278.97000000000003),
            (20060301, 337.45999999999998),
            (20070301, 392.66000000000003),
            (20080301, 357.25),
        ],
        [
            (19910301, 94.319999999999993),
            (19910301, 100.36),
            (19920301, 87.530000000000001),
            (19930301, 109.78),
            (19940301, 114.98999999999999),
            (19950301, 128.38999999999999),
            (19960301, 133.13999999999999),
            (19970301, 136.24000000000001),
            (19980301, 166.84999999999999),
            (19990301, 216.41),
            (20000301, 163.62),
            (20010301, 123.68000000000001),
            (20020301, 104.19),
            (20030301, 138.03),
            (20040301, 160.78),
            (20050301, 182.69999999999999),
            (20060301, 215.40000000000001),
            (20070301, 250.84),
            (20080301, 230.37),
        ],
    ]
    sNames = 'Shell Transport & Trading', 'Liberty International'
    for i in range(len(chart.data)):
        chart.lines[i].name = sNames[i]
    chart.lines[0].strokeColor = PCMYKColor(100, 0, 90, 50, alpha=100)
    chart.lines[1].strokeColor = PCMYKColor(0, 100, 100, 40, alpha=100)
    chart.xValueAxis.subGridStrokeColor = black
    chart.yValueAxis.gridStrokeColor = PCMYKColor(100, 100, 100, 100, alpha=100)
    chart.strokeWidth = 1
    chart.yValueAxis.visible = 1
    chart.yValueAxis.strokeColor = black
    chart.yValueAxis.labelTextScale = 1
    chart.yValueAxis.labels.fillColor = black
    # chart.width = 265
    # chart.height = 95
    chart.lines.strokeWidth = 2
    # legend
    legend = LineLegend()
    legend.colorNamePairs = Auto(obj=chart)
    legend.x = 6
    legend.y = 30
    legend.dx = 6
    legend.dy = 10
    legend.fontName = font_name
    legend.fontSize = 8
    legend.alignment = 'right'
    legend.columnMaximum = 3
    legend.dxTextSpace = 4
    legend.variColumn = 1
    legend.boxAnchor = 'nw'
    legend.deltay = 10
    legend.autoXPadding = 65
    background = Rect(
        0,
        0,
        width,
        height,
        strokeWidth=0,
        fillColor=PCMYKColor(0, 0, 10, 0),
    )
    background.strokeColor = black
    background.fillOpacity = 0.5
    background.strokeWidth = 3
    background.strokeDashArray = (3, 2)
    background.fillColor = PCMYKColor(66, 13, 0, 22, alpha=30)
    background.x = 0

    drawing = Drawing(width, height)
    drawing.add(background, 'background')
    drawing.add(chart, 'chart')
    drawing.add(legend, 'legend')

    return drawing


def dashed_line_and_number_format(
    width=400,
    height=200,
    font_name='Helvetica',
    font_size=7,
    stroke_with=0.5,
    dash_array=None,
    line_cap=1,
    over_shoot=0,
):
    """
    Chart features
    ============

    - **chart.yValueAxis.labelTextScale = 1000:** Multiplies y-values in the data by a scaling factor of 1000
    - **chart.xValueAxis.xLabelFormat = '{mm}/{dd}/{yy}':** Sets the date format to display on the x-axis. The x-axis accepts data values as integers in the format yyyymmdd
    - **chart.xValueAxis.labels.angle = 90:** Rotates the x-axis labels such that they are vertical
    - **chart.yValueAxis.labelTextFormat = '$%0.2f':** Describes the formatting of the y-axis; note the addition of the '$' sign
    - **chart.lines[0].strokeDashArray = (1, 1):** Gives the dash pattern of the line, lengths in points, alternating between filled and empty space
    - **chart.lines[1].strokeDashArray = (6, 2):** Gives the dash pattern of the line, lengths in points, alternating between filled and empty space
    - **chart.lines[2].strokeDashArray = (2, 2, 2, 2, 10):** Gives the dash pattern of the line, lengths in points, alternating between filled and empty space

    """

    dash_array = dash_array or (0.3, 1)
    # chart
    chart = LinePlot()
    chart.width = width - 46  # 留出一部分给容器(坐标轴)
    chart.height = height - 100  # 留出一部分给title(坐标轴)
    chart.x = 50
    chart.y = 50
    # colours
    colorsList = [
        PCMYKColor(65.1, 72.16, 33.33, 14.51),
        PCMYKColor(50.98, 28.63, 41.18, 1.18),
        PCMYKColor(0, 0, 0, 100),
        PCMYKColor(0, 0, 0, 0),
        PCMYKColor(0, 0, 0, 0),
        PCMYKColor(0, 0, 0, 0),
    ]
    for i, color in enumerate(colorsList[:3]):
        chart.lines[i].strokeColor = color
    # x axis
    chart.xValueAxis = NormalDateXValueAxis()
    chart.xValueAxis.labels.fontName = font_name
    chart.xValueAxis.labels.fontSize = 6
    chart.xValueAxis.labels.boxAnchor = 'autox'
    chart.xValueAxis.labels.angle = 90
    chart.xValueAxis.labels.rightPadding = 2
    chart.xValueAxis.xLabelFormat = '{mm}/{dd}/{yy}'
    chart.xValueAxis.strokeDashArray = dash_array
    chart.xValueAxis.strokeLineCap = line_cap
    chart.xValueAxis.maximumTicks = 20
    chart.xValueAxis.forceFirstDate = 1
    chart.xValueAxis.dailyFreq = 0
    chart.xValueAxis.forceEndDate = 1
    chart.xValueAxis.minimumTickSpacing = 15
    # chart.xValueAxis.niceMonth=0
    # y axis
    # chart.yValueAxis = AdjYValueAxis()
    chart.yValueAxis.labels.fontName = font_name
    chart.yValueAxis.labels.fontSize = 6
    chart.yValueAxis.labelTextFormat = '$%0.2f'
    chart.yValueAxis.labels.rightPadding = 7
    chart.yValueAxis.strokeWidth = 0.5
    chart.yValueAxis.strokeDashArray = dash_array
    chart.yValueAxis.strokeLineCap = line_cap
    # self.chart.yValueAxis.origShiftIPC         = 1
    chart.yValueAxis.maximumTicks = 15
    chart.yValueAxis.rangeRound = 'both'
    chart.yValueAxis.avoidBoundFrac = 0.1
    chart.yValueAxis.gridStrokeWidth = stroke_with
    chart.yValueAxis.gridStrokeDashArray = dash_array
    chart.yValueAxis.gridStrokeLineCap = line_cap
    chart.yValueAxis.visibleAxis = 0
    chart.yValueAxis.visibleGrid = 1
    # sample data
    chart.data = [
        [
            (20070201, 1.0),
            (20070228, 1.0089999999999999),
            (20070331, 1.0264),
            (20070430, 1.0430999999999999),
            (20070531, 1.0649),
            (20070630, 1.0720000000000001),
            (20070731, 1.0742),
            (20070831, 1.0553999999999999),
            (20070930, 1.0713999999999999),
            (20071031, 1.1031),
            (20071130, 1.093),
            (20071231, 1.1005),
            (20080131, 1.0740000000000001),
        ],
        [
            (20070201, 1.0),
            (20070228, 1.0154000000000001),
            (20070331, 1.0155000000000001),
            (20070430, 1.0208999999999999),
            (20070531, 1.0132000000000001),
            (20070630, 1.0101),
            (20070731, 1.0185),
            (20070831, 1.0309999999999999),
            (20070930, 1.0388999999999999),
            (20071031, 1.0482),
            (20071130, 1.0670999999999999),
            (20071231, 1.0701000000000001),
            (20080131, 1.0880000000000001),
        ],
        [
            (20070201, 1.0),
            (20070228, 1.0089999999999999),
            (20070331, 1.0182),
            (20070430, 1.0311999999999999),
            (20070531, 1.0471999999999999),
            (20070630, 1.0518000000000001),
            (20070731, 1.0532999999999999),
            (20070831, 1.0344),
            (20070930, 1.0470999999999999),
            (20071031, 1.0699000000000001),
            (20071130, 1.0613999999999999),
            (20071231, 1.0621),
            (20080131, 1.0455000000000001),
        ],
    ]
    _colorsList = [
        PCMYKColor(65.1, 72.16, 33.33, 14.51, alpha=100),
        PCMYKColor(50.98, 28.63, 41.18, 1.18, alpha=100),
        PCMYKColor(0, 0, 0, 100, alpha=100),
        PCMYKColor(0, 0, 0, 0, alpha=100),
        PCMYKColor(0, 0, 0, 0, alpha=100),
        PCMYKColor(0, 0, 0, 0, alpha=100),
    ]
    sNames = (
        'Liberty International',
        'Persimmon',
        'Royal Bank of Scotland',
    )
    for i in range(len(chart.data)):
        chart.lines[i].name = sNames[i]
    for i in range(len(chart.data)):
        chart.lines[i].strokeColor = _colorsList[i]
    chart.lines[0].strokeColor = PCMYKColor(23, 51, 0, 4, alpha=100)
    chart.lines[2].strokeColor = PCMYKColor(100, 60, 0, 50, alpha=100)
    chart.lines[1].strokeColor = PCMYKColor(66, 13, 0, 22, alpha=100)
    chart.lines.strokeWidth = 2
    chart.lines[1].strokeDashArray = (6, 2)
    chart.lines[2].strokeDashArray = (2, 2, 2, 2, 10)
    chart.lines[0].strokeDashArray = (1, 1)
    chart.yValueAxis.labelTextScale = 1000
    chart.xValueAxis.visible = 1
    chart.xValueAxis.visibleGrid = 0
    chart.xValueAxis.visibleTicks = 1
    chart.xValueAxis.subGridStrokeWidth = 0.25
    chart.xValueAxis.strokeWidth = 0.5
    chart.xValueAxis.gridStrokeWidth = 0.25
    chart.yValueAxis.tickLeft = 0
    # legend
    legend = LineLegend()
    legend.colorNamePairs = Auto(obj=chart)
    legend.fontName = font_name
    legend.fontSize = 7
    legend.alignment = 'right'
    legend.columnMaximum = 1
    legend.dxTextSpace = 5
    legend.variColumn = 1
    legend.autoXPadding = 15
    legend.y = 175
    legend.x = 100

    # L0
    left_line = Line(
        chart.x,
        chart.y,
        chart.x,
        chart.y + chart.height,
        strokeWidth=stroke_with,
        strokeDashArray=dash_array,
        strokeLineCap=line_cap,
    )
    # left_line.x1 = 50
    # left_line.x2 = 50
    # left_line.y1 = 50
    # left_line.y2 = 150
    left_line.strokeWidth = 1

    # L1
    right_line = Line(
        chart.x + chart.width,
        chart.y,
        chart.x + chart.width,
        chart.y + chart.height,
        strokeWidth=stroke_with,
        strokeDashArray=dash_array,
        strokeLineCap=line_cap,
    )
    # right_line.x1 = 350
    # right_line.x2 = 350
    # right_line.y1 = 50
    # right_line.y2 = 150
    right_line.strokeWidth = 1

    # L2
    bottom_line = Line(
        chart.x - over_shoot,
        chart.y,
        chart.x + chart.width + over_shoot,
        chart.y,
        strokeWidth=stroke_with,
    )
    # bottom_line.x1 = 50
    # bottom_line.x2 = 350
    # bottom_line.y1 = 50
    # bottom_line.y2 = 50
    bottom_line.strokeWidth = 0.75

    drawing = Drawing(width, height)
    drawing.add(chart, 'chart')
    drawing.add(legend, 'legend')
    drawing.add(left_line, 'left_line')
    drawing.add(right_line, 'right_line')
    drawing.add(bottom_line, 'bottom_line')

    return drawing


def line_with_time_series_plot(
    width=400,
    height=200,
    font_name='Helvetica',
    font_size=7,
):
    """
    Chart features
    ==============

    This chart has a simple time series axis, which accepts (x,y) pairs in which the x value is an integer of the format yyymmdd:

    A title is added:

    - **self._add(self,String(10,10,'text'),name='title',validate=None,desc=None):** Adds a text string
    - **self.title.text = 'Simple Time Series Plot':** Defines the text of the string
    - **self.title.fontSize = 16:** Determines the font size
    - **self.title.y = 160:** Positions the y value of the lower left corner of the title
    - **self.title.x = 115:** Positions the x value of the lower left corner of the title

    """

    chart = SimpleTimeSeriesPlot()
    chart.x = 30
    chart.y = 30
    chart.width = width - 46  # 留出一部分给容器(坐标轴)
    chart.height = height - 60  # 留出一部分给title(坐标轴)
    # chart.width = 335
    # chart.height = 90
    chart.yValueAxis.forceZero = 0
    chart.lines[0].strokeColor = PCMYKColor(100, 0, 90, 50, alpha=100)
    chart.lines.strokeWidth = 2
    chart.lines[1].strokeColor = PCMYKColor(0, 100, 100, 40, alpha=100)
    chart.xValueAxis.xLabelFormat = '{mm}/{YY}'
    chart.data = [
        [
            ('20120101', 100),
            ('20120102', 100),
            ('20120103', 101),
            ('20120104', 101),
            ('20120105', 102),
            ('20120106', 101),
            ('20120107', 101),
            ('20120108', 101),
            ('20120109', 102),
            ('20120110', 103),
            ('20120111', 103),
            ('20120112', 104),
            ('20120113', 103),
            ('20120114', 103),
            ('20120115', 103),
            ('20120116', 103),
            ('20120117', 103),
            ('20120118', 105),
            ('20120119', 106),
            ('20120120', 106),
            ('20120121', 106),
            ('20120122', 106),
            ('20120123', 106),
            ('20120124', 107),
            ('20120125', 108),
            ('20120126', 107),
            ('20120127', 107),
            ('20120128', 107),
            ('20120129', 107),
            ('20120130', 107),
            ('20120131', 107),
            ('20120201', 109),
            ('20120202', 109),
            ('20120203', 111),
            ('20120204', 111),
            ('20120205', 111),
            ('20120206', 111),
            ('20120207', 111),
            ('20120208', 111),
            ('20120209', 110),
            ('20120210', 109),
            ('20120211', 109),
            ('20120212', 109),
            ('20120213', 110),
            ('20120214', 110),
            ('20120215', 109),
            ('20120216', 111),
            ('20120217', 111),
            ('20120218', 111),
            ('20120219', 111),
            ('20120220', 111),
            ('20120221', 111),
            ('20120222', 111),
            ('20120223', 112),
            ('20120224', 111),
            ('20120225', 111),
            ('20120226', 111),
            ('20120227', 111),
            ('20120228', 111),
            ('20120229', 110),
            ('20120301', 111),
            ('20120302', 109),
            ('20120303', 109),
            ('20120304', 109),
            ('20120305', 109),
            ('20120306', 106),
            ('20120307', 108),
            ('20120308', 109),
            ('20120309', 111),
            ('20120310', 111),
            ('20120311', 111),
            ('20120312', 110),
            ('20120313', 113),
            ('20120314', 112),
            ('20120315', 113),
            ('20120316', 112),
            ('20120317', 112),
            ('20120318', 112),
            ('20120319', 113),
            ('20120320', 112),
            ('20120321', 112),
            ('20120322', 110),
            ('20120323', 111),
            ('20120324', 111),
            ('20120325', 111),
            ('20120326', 113),
            ('20120327', 113),
            ('20120328', 112),
            ('20120329', 112),
            ('20120330', 112),
            ('20120331', 112),
            ('20120401', 112),
            ('20120402', 113),
            ('20120403', 112),
            ('20120404', 110),
            ('20120405', 110),
            ('20120406', 110),
            ('20120407', 110),
            ('20120408', 110),
            ('20120409', 108),
            ('20120410', 106),
            ('20120411', 107),
            ('20120412', 109),
            ('20120413', 107),
            ('20120414', 107),
            ('20120415', 107),
            ('20120416', 107),
            ('20120417', 109),
            ('20120418', 108),
            ('20120419', 108),
            ('20120420', 108),
            ('20120421', 108),
            ('20120422', 108),
            ('20120423', 106),
            ('20120424', 107),
            ('20120425', 109),
            ('20120426', 110),
            ('20120427', 111),
            ('20120428', 111),
            ('20120429', 111),
            ('20120430', 110),
            ('20120501', 110),
            ('20120502', 110),
            ('20120503', 108),
            ('20120504', 106),
            ('20120505', 106),
            ('20120506', 106),
            ('20120507', 106),
            ('20120508', 106),
            ('20120509', 105),
            ('20120510', 106),
            ('20120511', 105),
            ('20120512', 105),
            ('20120513', 105),
            ('20120514', 104),
            ('20120515', 103),
            ('20120516', 103),
            ('20120517', 101),
            ('20120518', 100),
            ('20120519', 100),
            ('20120520', 100),
            ('20120521', 102),
            ('20120522', 102),
            ('20120523', 102),
            ('20120524', 102),
            ('20120525', 102),
            ('20120526', 102),
            ('20120527', 102),
            ('20120528', 102),
            ('20120529', 104),
            ('20120530', 102),
            ('20120531', 101),
            ('20120601', 98),
            ('20120602', 98),
            ('20120603', 98),
            ('20120604', 98),
            ('20120605', 99),
            ('20120606', 102),
            ('20120607', 101),
            ('20120608', 102),
            ('20120609', 102),
            ('20120610', 102),
            ('20120611', 100),
            ('20120612', 101),
            ('20120613', 99),
            ('20120614', 100),
            ('20120615', 101),
            ('20120616', 101),
            ('20120617', 101),
            ('20120618', 102),
            ('20120619', 103),
            ('20120620', 103),
            ('20120621', 100),
            ('20120622', 101),
            ('20120623', 101),
            ('20120624', 101),
            ('20120625', 99),
            ('20120626', 99),
            ('20120627', 100),
            ('20120628', 100),
            ('20120629', 103),
            ('20120630', 103),
            ('20120701', 103),
            ('20120702', 104),
            ('20120703', 106),
            ('20120704', 106),
            ('20120705', 106),
            ('20120706', 104),
            ('20120707', 104),
            ('20120708', 104),
            ('20120709', 104),
            ('20120710', 102),
            ('20120711', 102),
            ('20120712', 102),
            ('20120713', 103),
            ('20120714', 103),
            ('20120715', 103),
            ('20120716', 102),
            ('20120717', 103),
            ('20120718', 104),
            ('20120719', 104),
            ('20120720', 102),
            ('20120721', 102),
            ('20120722', 102),
            ('20120723', 101),
            ('20120724', 99),
            ('20120725', 100),
            ('20120726', 101),
            ('20120727', 104),
            ('20120728', 104),
            ('20120729', 104),
            ('20120730', 103),
            ('20120731', 103),
            ('20120801', 101),
            ('20120802', 101),
            ('20120803', 103),
            ('20120804', 103),
            ('20120805', 103),
            ('20120806', 104),
            ('20120807', 105),
            ('20120808', 105),
            ('20120809', 106),
            ('20120810', 106),
            ('20120811', 106),
            ('20120812', 106),
            ('20120813', 105),
            ('20120814', 105),
            ('20120815', 106),
            ('20120816', 107),
            ('20120817', 108),
            ('20120818', 108),
            ('20120819', 108),
            ('20120820', 107),
            ('20120821', 107),
            ('20120822', 107),
            ('20120823', 106),
            ('20120824', 106),
            ('20120825', 106),
            ('20120826', 106),
            ('20120827', 106),
            ('20120828', 107),
            ('20120829', 107),
            ('20120830', 106),
            ('20120831', 106),
            ('20120901', 106),
            ('20120902', 106),
            ('20120903', 106),
            ('20120904', 107),
            ('20120905', 107),
            ('20120906', 110),
            ('20120907', 110),
            ('20120908', 110),
            ('20120909', 110),
            ('20120910', 110),
            ('20120911', 110),
            ('20120912', 111),
            ('20120913', 112),
            ('20120914', 114),
            ('20120915', 114),
            ('20120916', 114),
            ('20120917', 113),
            ('20120918', 112),
            ('20120919', 112),
            ('20120920', 111),
            ('20120921', 111),
            ('20120922', 111),
            ('20120923', 111),
            ('20120924', 111),
            ('20120925', 109),
            ('20120926', 108),
            ('20120927', 110),
            ('20120928', 109),
            ('20120929', 109),
            ('20120930', 109),
            ('20121001', 109),
            ('20121002', 109),
            ('20121003', 109),
            ('20121004', 110),
            ('20121005', 110),
            ('20121006', 110),
            ('20121007', 110),
            ('20121008', 109),
            ('20121009', 108),
            ('20121010', 108),
            ('20121011', 108),
            ('20121012', 107),
            ('20121013', 107),
            ('20121014', 107),
            ('20121015', 108),
            ('20121016', 109),
            ('20121017', 110),
            ('20121018', 110),
            ('20121019', 108),
            ('20121020', 108),
            ('20121021', 108),
            ('20121022', 108),
            ('20121023', 107),
            ('20121024', 107),
            ('20121025', 107),
            ('20121026', 107),
            ('20121027', 107),
            ('20121028', 107),
            ('20121029', 107),
            ('20121030', 107),
            ('20121031', 109),
            ('20121101', 111),
            ('20121102', 109),
            ('20121103', 109),
            ('20121104', 109),
            ('20121105', 110),
            ('20121106', 111),
            ('20121107', 108),
            ('20121108', 107),
            ('20121109', 107),
            ('20121110', 107),
            ('20121111', 107),
            ('20121112', 107),
            ('20121113', 106),
            ('20121114', 104),
            ('20121115', 104),
            ('20121116', 105),
            ('20121117', 105),
            ('20121118', 105),
            ('20121119', 107),
            ('20121120', 107),
            ('20121121', 108),
            ('20121122', 108),
            ('20121123', 109),
            ('20121124', 109),
            ('20121125', 109),
            ('20121126', 109),
            ('20121127', 109),
            ('20121128', 109),
            ('20121129', 110),
            ('20121130', 110),
            ('20121201', 110),
            ('20121202', 110),
            ('20121203', 110),
            ('20121204', 110),
            ('20121205', 110),
            ('20121206', 110),
            ('20121207', 110),
            ('20121208', 110),
            ('20121209', 110),
            ('20121210', 111),
            ('20121211', 112),
            ('20121212', 112),
            ('20121213', 111),
            ('20121214', 111),
            ('20121215', 111),
            ('20121216', 111),
            ('20121217', 112),
            ('20121218', 114),
            ('20121219', 114),
            ('20121220', 114),
            ('20121221', 113),
            ('20121222', 113),
            ('20121223', 113),
            ('20121224', 113),
            ('20121225', 113),
            ('20121226', 112),
            ('20121227', 112),
            ('20121228', 112),
            ('20121229', 112),
            ('20121230', 112),
            ('20121231', 114),
        ],
        [
            ('20120101', 100),
            ('20120102', 100),
            ('20120103', 101),
            ('20120104', 100),
            ('20120105', 101),
            ('20120106', 101),
            ('20120107', 101),
            ('20120108', 101),
            ('20120109', 101),
            ('20120110', 103),
            ('20120111', 103),
            ('20120112', 104),
            ('20120113', 103),
            ('20120114', 103),
            ('20120115', 103),
            ('20120116', 103),
            ('20120117', 103),
            ('20120118', 105),
            ('20120119', 105),
            ('20120120', 105),
            ('20120121', 105),
            ('20120122', 105),
            ('20120123', 105),
            ('20120124', 106),
            ('20120125', 107),
            ('20120126', 107),
            ('20120127', 107),
            ('20120128', 107),
            ('20120129', 107),
            ('20120130', 107),
            ('20120131', 107),
            ('20120201', 109),
            ('20120202', 109),
            ('20120203', 112),
            ('20120204', 112),
            ('20120205', 112),
            ('20120206', 111),
            ('20120207', 111),
            ('20120208', 111),
            ('20120209', 111),
            ('20120210', 109),
            ('20120211', 109),
            ('20120212', 109),
            ('20120213', 111),
            ('20120214', 110),
            ('20120215', 109),
            ('20120216', 112),
            ('20120217', 111),
            ('20120218', 111),
            ('20120219', 111),
            ('20120220', 111),
            ('20120221', 111),
            ('20120222', 110),
            ('20120223', 112),
            ('20120224', 111),
            ('20120225', 111),
            ('20120226', 111),
            ('20120227', 111),
            ('20120228', 111),
            ('20120229', 109),
            ('20120301', 110),
            ('20120302', 108),
            ('20120303', 108),
            ('20120304', 108),
            ('20120305', 108),
            ('20120306', 106),
            ('20120307', 107),
            ('20120308', 109),
            ('20120309', 110),
            ('20120310', 110),
            ('20120311', 110),
            ('20120312', 110),
            ('20120313', 112),
            ('20120314', 111),
            ('20120315', 112),
            ('20120316', 112),
            ('20120317', 112),
            ('20120318', 112),
            ('20120319', 113),
            ('20120320', 112),
            ('20120321', 112),
            ('20120322', 111),
            ('20120323', 112),
            ('20120324', 112),
            ('20120325', 112),
            ('20120326', 114),
            ('20120327', 113),
            ('20120328', 112),
            ('20120329', 112),
            ('20120330', 112),
            ('20120331', 112),
            ('20120401', 112),
            ('20120402', 113),
            ('20120403', 113),
            ('20120404', 111),
            ('20120405', 110),
            ('20120406', 110),
            ('20120407', 110),
            ('20120408', 110),
            ('20120409', 108),
            ('20120410', 106),
            ('20120411', 107),
            ('20120412', 109),
            ('20120413', 107),
            ('20120414', 107),
            ('20120415', 107),
            ('20120416', 108),
            ('20120417', 109),
            ('20120418', 108),
            ('20120419', 108),
            ('20120420', 108),
            ('20120421', 108),
            ('20120422', 108),
            ('20120423', 107),
            ('20120424', 108),
            ('20120425', 110),
            ('20120426', 110),
            ('20120427', 111),
            ('20120428', 111),
            ('20120429', 111),
            ('20120430', 110),
            ('20120501', 110),
            ('20120502', 110),
            ('20120503', 109),
            ('20120504', 107),
            ('20120505', 107),
            ('20120506', 107),
            ('20120507', 107),
            ('20120508', 107),
            ('20120509', 106),
            ('20120510', 107),
            ('20120511', 107),
            ('20120512', 107),
            ('20120513', 107),
            ('20120514', 105),
            ('20120515', 105),
            ('20120516', 104),
            ('20120517', 102),
            ('20120518', 101),
            ('20120519', 101),
            ('20120520', 101),
            ('20120521', 103),
            ('20120522', 103),
            ('20120523', 103),
            ('20120524', 103),
            ('20120525', 103),
            ('20120526', 103),
            ('20120527', 103),
            ('20120528', 103),
            ('20120529', 105),
            ('20120530', 103),
            ('20120531', 103),
            ('20120601', 100),
            ('20120602', 100),
            ('20120603', 100),
            ('20120604', 100),
            ('20120605', 101),
            ('20120606', 103),
            ('20120607', 103),
            ('20120608', 104),
            ('20120609', 104),
            ('20120610', 104),
            ('20120611', 101),
            ('20120612', 103),
            ('20120613', 102),
            ('20120614', 103),
            ('20120615', 104),
            ('20120616', 104),
            ('20120617', 104),
            ('20120618', 104),
            ('20120619', 106),
            ('20120620', 106),
            ('20120621', 103),
            ('20120622', 105),
            ('20120623', 105),
            ('20120624', 105),
            ('20120625', 103),
            ('20120626', 103),
            ('20120627', 105),
            ('20120628', 105),
            ('20120629', 108),
            ('20120630', 108),
            ('20120701', 108),
            ('20120702', 109),
            ('20120703', 111),
            ('20120704', 111),
            ('20120705', 111),
            ('20120706', 109),
            ('20120707', 109),
            ('20120708', 109),
            ('20120709', 109),
            ('20120710', 108),
            ('20120711', 107),
            ('20120712', 107),
            ('20120713', 108),
            ('20120714', 108),
            ('20120715', 108),
            ('20120716', 108),
            ('20120717', 108),
            ('20120718', 109),
            ('20120719', 109),
            ('20120720', 107),
            ('20120721', 107),
            ('20120722', 107),
            ('20120723', 105),
            ('20120724', 104),
            ('20120725', 104),
            ('20120726', 105),
            ('20120727', 108),
            ('20120728', 108),
            ('20120729', 108),
            ('20120730', 107),
            ('20120731', 107),
            ('20120801', 104),
            ('20120802', 104),
            ('20120803', 107),
            ('20120804', 107),
            ('20120805', 107),
            ('20120806', 108),
            ('20120807', 109),
            ('20120808', 108),
            ('20120809', 109),
            ('20120810', 109),
            ('20120811', 109),
            ('20120812', 109),
            ('20120813', 108),
            ('20120814', 108),
            ('20120815', 109),
            ('20120816', 110),
            ('20120817', 111),
            ('20120818', 111),
            ('20120819', 111),
            ('20120820', 111),
            ('20120821', 110),
            ('20120822', 110),
            ('20120823', 109),
            ('20120824', 110),
            ('20120825', 110),
            ('20120826', 110),
            ('20120827', 110),
            ('20120828', 110),
            ('20120829', 111),
            ('20120830', 110),
            ('20120831', 110),
            ('20120901', 110),
            ('20120902', 110),
            ('20120903', 110),
            ('20120904', 111),
            ('20120905', 111),
            ('20120906', 114),
            ('20120907', 114),
            ('20120908', 114),
            ('20120909', 114),
            ('20120910', 114),
            ('20120911', 114),
            ('20120912', 115),
            ('20120913', 116),
            ('20120914', 117),
            ('20120915', 117),
            ('20120916', 117),
            ('20120917', 117),
            ('20120918', 116),
            ('20120919', 116),
            ('20120920', 116),
            ('20120921', 116),
            ('20120922', 116),
            ('20120923', 116),
            ('20120924', 116),
            ('20120925', 114),
            ('20120926', 113),
            ('20120927', 115),
            ('20120928', 114),
            ('20120929', 114),
            ('20120930', 114),
            ('20121001', 114),
            ('20121002', 114),
            ('20121003', 114),
            ('20121004', 115),
            ('20121005', 114),
            ('20121006', 114),
            ('20121007', 114),
            ('20121008', 114),
            ('20121009', 112),
            ('20121010', 112),
            ('20121011', 113),
            ('20121012', 112),
            ('20121013', 112),
            ('20121014', 112),
            ('20121015', 113),
            ('20121016', 113),
            ('20121017', 114),
            ('20121018', 114),
            ('20121019', 112),
            ('20121020', 112),
            ('20121021', 112),
            ('20121022', 111),
            ('20121023', 111),
            ('20121024', 111),
            ('20121025', 111),
            ('20121026', 110),
            ('20121027', 110),
            ('20121028', 110),
            ('20121029', 110),
            ('20121030', 110),
            ('20121031', 111),
            ('20121101', 113),
            ('20121102', 111),
            ('20121103', 111),
            ('20121104', 111),
            ('20121105', 111),
            ('20121106', 112),
            ('20121107', 109),
            ('20121108', 108),
            ('20121109', 108),
            ('20121110', 108),
            ('20121111', 108),
            ('20121112', 108),
            ('20121113', 107),
            ('20121114', 105),
            ('20121115', 105),
            ('20121116', 106),
            ('20121117', 106),
            ('20121118', 106),
            ('20121119', 108),
            ('20121120', 108),
            ('20121121', 109),
            ('20121122', 109),
            ('20121123', 110),
            ('20121124', 110),
            ('20121125', 110),
            ('20121126', 110),
            ('20121127', 110),
            ('20121128', 111),
            ('20121129', 112),
            ('20121130', 112),
            ('20121201', 112),
            ('20121202', 112),
            ('20121203', 112),
            ('20121204', 112),
            ('20121205', 112),
            ('20121206', 112),
            ('20121207', 112),
            ('20121208', 112),
            ('20121209', 112),
            ('20121210', 112),
            ('20121211', 114),
            ('20121212', 113),
            ('20121213', 112),
            ('20121214', 112),
            ('20121215', 112),
            ('20121216', 112),
            ('20121217', 114),
            ('20121218', 115),
            ('20121219', 116),
            ('20121220', 116),
            ('20121221', 116),
            ('20121222', 116),
            ('20121223', 116),
            ('20121224', 115),
            ('20121225', 115),
            ('20121226', 114),
            ('20121227', 114),
            ('20121228', 113),
            ('20121229', 113),
            ('20121230', 113),
            ('20121231', 116),
        ],
    ]
    chart.xValueAxis.niceMonth = 1

    # title
    title = String(10, 10, 'text')
    title.text = 'Simple Time Series Plot'
    title.fontName = font_name
    title.fontSize = 16
    title.y = 160
    title.x = 115

    drawing = Drawing(width, height)
    drawing.add(chart, 'chart')
    drawing.add(title, 'title')

    return drawing


if __name__ == "__main__":  # NORUNTESTS
    # draw = line_with_smiley_marker_serious()
    # draw = line_with_smiley_marker_silly()
    # draw = line_with_background_color()
    # draw = dashed_line_and_number_format()
    draw = line_with_time_series_plot()
    draw.save(formats=['pdf'], outDir='.', fnRoot=None)
