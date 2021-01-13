"Scatter plot with legend"
from reportlab.lib.colors import (
    black,
    rgb2cmyk,
    toColor,
    red,
    green,
    blue,
    fade,
    PCMYKColor,
    CMYKColor,
)
from reportlab.graphics.charts.lineplots import ScatterPlot
from reportlab.graphics.charts.legends import Legend
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
from reportlab.graphics.charts.textlabels import Label


def scatter_plot_with_legend(
    width=144, height=85, font_name='Helvetica', font_size=6
):
    """
    Chart Features
    --------------

    - The maximum number of rows in the legend is ONE, which forces the legend to grow
    horizontally.

    - There is some dynamic bit of code there that decides through the data where the crosshair
    should go.
    """

    # common values
    strokeDashArray = 1, 1
    main_color = PCMYKColor(32, 0, 18, 44)

    # scatter chart
    chart = ScatterPlot()
    chart.leftPadding = 0
    chart.rightPadding = 0
    chart.topPadding = 0
    chart.bottomPadding = 0
    chart.lineLabelFormat = None
    chart.outerBorderColor = black
    # chart x axis
    chart.xValueAxis.labels.fontName = font_name
    chart.xValueAxis.labels.fontSize = font_size
    # chart.xValueAxis.valueStep             = 2
    chart.xValueAxis.visibleGrid = 1
    chart.xValueAxis.gridStrokeDashArray = strokeDashArray
    chart.xValueAxis.minimumTickSpacing = 10
    chart.xValueAxis.maximumTicks = 8
    chart.xValueAxis.forceZero = 1
    chart.xValueAxis.avoidBoundFrac = 1  # 0.5
    chart.xValueAxis.visibleTicks = False
    # chart y axis
    chart.yValueAxis.labels.fontName = font_name
    chart.yValueAxis.labels.fontSize = font_size
    chart.yValueAxis.labelTextFormat = None
    chart.yValueAxis.visibleGrid = 1
    chart.yValueAxis.gridStrokeDashArray = strokeDashArray
    chart.yValueAxis.drawGridLast = False
    chart.yValueAxis.minimumTickSpacing = 10
    chart.yValueAxis.maximumTicks = 8
    chart.yValueAxis.forceZero = 1
    chart.yValueAxis.avoidBoundFrac = 1  # 0.5
    chart.yValueAxis.visibleTicks = False
    # chart labels
    chart.xLabel = ''
    chart.yLabel = ''

    for i, color in enumerate(fade(main_color, [100, 75, 50, 25])):
        chart.lines[i].strokeColor = color
    # chart.lines[0].strokeColor = toColor(rgb2cmyk(*red.rgb()))
    # chart.lines[1].strokeColor = toColor(rgb2cmyk(*green.rgb()))
    # chart.lines[2].strokeColor = toColor(rgb2cmyk(*blue.rgb()))
    chart.width = 250
    chart.height = 125
    chart.y = 50
    chart.x = 50
    chart.lines.symbol.size = 6
    chart.lines[0].strokeColor = PCMYKColor(100, 0, 90, 50, alpha=100)
    chart.lines[2].strokeColor = PCMYKColor(100, 60, 0, 50, alpha=100)
    chart.lines.strokeWidth = 1
    chart.data = [[(2.25, 4.48)], [(3.59, 4.42)], [(3.52, 3.58)]]
    chart.lines[1].strokeColor = PCMYKColor(0, 100, 100, 40, alpha=100)
    # symbol styles
    chart.lines.symbol = makeMarker('FilledSquare')

    # chart legend
    legend = Legend()
    legend.x = 50
    legend.y = 15
    legend.fontSize = 8
    legend.fontName = font_name
    legend.strokeWidth = 0
    legend.strokeColor = None
    legend.boxAnchor = 'w'
    legend.alignment = 'right'
    legend.dx = legend.dy = 6
    legend.deltax = 30
    legend.deltay = 0
    legend.dxTextSpace = 2
    legend.columnMaximum = 1
    legend.variColumn = 1
    # xal
    xal = Label()
    xal.fontName = font_name

    # yal
    yal = Label()
    yal.fontName = font_name
    yal.angle = 90
    xal.x = 50
    xal.y = 30
    xal.fontSize = 8
    xal.boxAnchor = 'w'
    # yal.boxAnchor='s'
    yal.textAnchor = 'middle'
    yal.y = 100
    yal.x = 25
    yal.fontSize = 8
    # _crossHairStrokeColor = black
    xal._text = '5-year annualized standard deviation'
    yal._text = '5-year average\nannual return (%)'
    yal.boxAnchor = 'c'

    # get the data using a helper function. Put into the plot in the right way
    d = [
        (u'Portfolio', 2.25, 4.4800000000000004),
        (u'Index', 3.5899999999999999, 4.4199999999999999),
        (u'Universe Mean', 3.52, 3.48),
    ]
    sd = [tuple(x[1:]) for x in d]
    nd = len(sd)
    chart.data = [[x] for x in sd]
    for i in range(nd):
        chart.lines[i].symbol = chart.lines.symbol
    for i in range(nd):
        chart.lines[i].symbol.size = chart.lines.symbol.size
    # make up the legend text using the helper instance
    legend.colorNamePairs = [(Auto(obj=chart), d[i][0]) for i in range(nd)]
    primary = 2
    # for valid primary add a cross
    if 0 < primary < nd:
        chart.addCrossHair(
            'pch',
            sd[primary][0],
            sd[primary][1],
            strokeColor=chart.lines[primary].strokeColor,
            strokeWidth=2,
        )

    drawing = Drawing()
    drawing.add(chart, 'chart')
    drawing.add(legend, 'legend')
    drawing.add(xal, 'xal')
    drawing.add(yal, 'yal')

    return drawing
