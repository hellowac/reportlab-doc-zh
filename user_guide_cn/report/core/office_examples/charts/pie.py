"Pie with multi-column legend"
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.colors import PCMYKColor, white, CMYKColor
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing, Rect, Line
from reportlab.lib.validators import Auto
from reportlab.lib.formatters import DecimalFormatter


def basic_pie(width=400, height=200, font_name='Times-Roman', font_size=7):
    """
    A Pie Chart
    ===========

    This is a simple pie chart that contains a basic legend.
    """
    # pie
    pie = Pie()
    pie.strokeWidth = 1
    pie.slices.strokeColor = PCMYKColor(0, 0, 0, 0)
    pie.slices.strokeWidth = 1
    # sample data
    colors = [
        PCMYKColor(100, 67, 0, 23, alpha=100),
        PCMYKColor(70, 46, 0, 16, alpha=100),
        PCMYKColor(50, 33, 0, 11, alpha=100),
        PCMYKColor(30, 20, 0, 7, alpha=100),
        PCMYKColor(20, 13, 0, 4, alpha=100),
        PCMYKColor(10, 7, 0, 3, alpha=100),
        PCMYKColor(0, 0, 0, 100, alpha=100),
        PCMYKColor(0, 0, 0, 70, alpha=100),
        PCMYKColor(0, 0, 0, 50, alpha=100),
        PCMYKColor(0, 0, 0, 30, alpha=100),
        PCMYKColor(0, 0, 0, 20, alpha=100),
        PCMYKColor(0, 0, 0, 10, alpha=100),
    ]
    pie.data = [56.0, 12.199999999999999, 28.5, 3.3999999999999999]
    for i in range(len(pie.data)):
        pie.slices[i].fillColor = colors[i]
    pie.strokeColor = PCMYKColor(0, 0, 0, 0, alpha=100)
    pie.slices[1].fillColor = PCMYKColor(100, 60, 0, 50, alpha=100)
    pie.slices[2].fillColor = PCMYKColor(0, 100, 100, 40, alpha=100)
    pie.slices[3].fillColor = PCMYKColor(66, 13, 0, 22, alpha=100)
    pie.slices[0].fillColor = PCMYKColor(100, 0, 90, 50, alpha=100)
    pie.width = 150
    pie.height = 150
    pie.y = 25
    pie.x = 25

    # legend
    legend = Legend()
    legend.columnMaximum = 99
    legend.alignment = 'right'
    legend.dx = 6
    legend.dy = 6
    legend.dxTextSpace = 5
    legend.deltay = 10
    legend.strokeWidth = 0
    legend.subCols[0].minWidth = 75
    legend.subCols[0].align = 'left'
    legend.subCols[1].minWidth = 25
    legend.subCols[1].align = 'right'

    legend.boxAnchor = 'c'
    legend.x = 350
    legend.y = 100
    legend.colorNamePairs = [
        (PCMYKColor(100, 0, 90, 50, alpha=100), ('BP', '56.0%')),
        (PCMYKColor(100, 60, 0, 50, alpha=100), ('BT', '12.2%')),
        (PCMYKColor(0, 100, 100, 40, alpha=100), ('Tesco', '28.5%')),
        (PCMYKColor(66, 13, 0, 22, alpha=100), ('Persimmon', '3.4%')),
    ]

    drawing = Drawing(width, height)
    drawing.add(pie, 'pie')
    drawing.add(legend, 'legend')

    return drawing


def pie_with_multi_column_legend(
    width=540, height=177, font_name='Times-Roman', font_size=7
):
    """
    Chart Features
    --------------

    This is a Pie Chart that contains a multi column Legend Widget. We add
    both a legend and legendHeader:

    - _add(self,Legend(),name='legend',validate=None,desc=None)
    - _add(self,Legend(),name='legendHeader',validate=None,desc=None)

    The legend has sub-columns for the various data series:

    - legend.subCols[0].align = 'left'
    - legend.subCols[0].minWidth = 90
    - legend.subCols[1].align = 'left'
    - legend.subCols[1].align='numeric'
    - legend.subCols[1].dx = -45
    - legend.subCols[1].minWidth = 60
    - legend.subCols[2].align = 'left'
    - legend.subCols[2].align='numeric'
    - legend.subCols[2].dx = -40
    - legend.subCols[2].minWidth = 50
    - legend.subCols[3].align='numeric'
    - legend.subCols[3].dx = -10
    - legend.subCols[3].dx = -15

    And likewise for the header:

    - legendHeader.colorNamePairs = [(black, ('Company','Previous Year',
    'This Year','Change'))]
    - legendHeader.subCols[0].minWidth = 100
    - legendHeader.subCols[0].align = 'left'
    - legendHeader.subCols[1].minWidth = 60
    - legendHeader.subCols[1].align = 'left'
    - legendHeader.subCols[2].minWidth = 50
    - legendHeader.subCols[2].align = 'left'
    - legendHeader.subCols[3].minWidth = 50
    - legendHeader.subCols[3].align = 'left'
    """
    # pie
    chart = Pie()
    chart.width = chart.height = 148  # its a circle
    chart.sameRadii = 1
    # chart.x = 1
    # chart.y = 18
    chart.y = 40
    chart.x = 12
    chart.slices.strokeColor = PCMYKColor(0, 0, 0, 0)
    chart.slices.strokeWidth = 0.5

    chart.height = 125
    chart.width = 120
    chart.height = 120

    # sample data
    _seriesNames = (
        'BP',
        'Shell Transport & Trading',
        'Liberty International',
        'Persimmon',
        'Royal Bank of Scotland',
        'Land Securities',
        'BT',
        'Standard Chartered',
        'Bovis Homes',
        'HSBC Holdings',
        'Natwest',
        'Barclays',
        'Sainsburys',
    )
    _seriesData1 = (
        27.40,
        0,
        10.33,
        0.6,
        27.38,
        0,
        0,
        8.21,
        9.30,
        3.65,
        0,
        0,
        10.37,
        2.4,
        2.5,
        2.4,
        2.55,
        1.6,
    )
    chart.data = _seriesData1

    # apply colors to slices
    _colors = (
        PCMYKColor(100, 55, 0, 55),
        PCMYKColor(55, 24, 0, 9),
        PCMYKColor(0, 70, 60, 5),
        PCMYKColor(10, 0, 49, 28),
        PCMYKColor(47, 64, 28, 0),
        PCMYKColor(10, 10, 73, 0),
        PCMYKColor(22, 3, 0, 0),
        PCMYKColor(22, 0, 100, 8),
        PCMYKColor(0, 64, 100, 0),
        PCMYKColor(0, 100, 99, 4),
        PCMYKColor(0, 30, 72, 11),
        PCMYKColor(50, 0, 25, 30),
        PCMYKColor(64, 100, 0, 14),
        PCMYKColor(75, 0, 7, 0),
        PCMYKColor(23, 2, 0, 77),
        PCMYKColor(30, 56, 100, 37),
        PCMYKColor(0, 4, 22, 32),
        PCMYKColor(0, 30, 100, 0),
    )
    for i, v in enumerate(chart.data):
        chart.slices[i].fillColor = _colors[i]

    _seriesData2 = (
        37.89,
        0,
        12.73,
        0.74,
        24.71,
        0,
        0,
        6.94,
        7.87,
        0,
        0,
        0,
        3.4,
        1.79,
        1.8,
        1.81,
        1.82,
        0.5,
    )

    _seriesData3 = [x - y for (x, y) in zip(_seriesData1, _seriesData2)]
    formatter = DecimalFormatter(
        places=2, thousandSep=',', decimalSep='.', suffix='%'
    )
    names = list(
        zip(
            _seriesNames,
            map(formatter, _seriesData1),
            map(formatter, _seriesData2),
            map(formatter, _seriesData3),
        )
    )

    black = PCMYKColor(0, 0, 0, 100)
    col_name_min_width = 100
    col_p_year_min_width = 60
    col_t_year_min_width = 50
    col_change_min_width = 50

    # legend_header
    legend_header = Legend()
    # legend_header.x = 160
    legend_header.x = 150
    legend_header.y = height
    legend_header.fontSize = font_size
    legend_header.fontName = font_name  # 'Times-Bold'  # fontName
    # legend_header.subCols[0].minWidth = 240
    legend_header.subCols[0].minWidth = col_name_min_width
    legend_header.subCols[0].align = 'left'

    legend_header.subCols[1].minWidth = col_p_year_min_width
    legend_header.subCols[1].align = 'left'

    legend_header.subCols[2].minWidth = col_t_year_min_width
    legend_header.subCols[2].align = 'left'

    legend_header.subCols[3].minWidth = col_change_min_width
    legend_header.subCols[3].align = 'left'

    legend_header.colorNamePairs = [
        (black, ('Company', 'Previous Year', 'This Year', 'Change'))
    ]

    legend = Legend()
    # legend.x = 160
    legend.x = 150
    legend.y = 163
    legend.fontSize = font_size
    legend.fontName = font_name
    legend.dx = 6
    legend.dy = 6
    legend.dxTextSpace = 5
    legend.yGap = 0
    legend.deltay = 12
    legend.strokeColor = PCMYKColor(0, 0, 0, 0)
    legend.strokeWidth = 0
    legend.columnMaximum = 99
    legend.alignment = 'right'
    legend.variColumn = 0
    legend.dividerDashArray = None
    legend.dividerWidth = 0.5
    legend.dividerOffsX = (0, 0)
    legend.dividerLines = 7
    legend.dividerOffsY = 6
    legend.subCols[0].align = 'left'
    legend.subCols[0].minWidth = col_name_min_width  # 90

    legend.subCols[1].align = 'left'
    legend.subCols[1].align = 'numeric'
    legend.subCols[1].dx = -45
    legend.subCols[1].minWidth = col_p_year_min_width

    legend.subCols[2].align = 'left'
    legend.subCols[2].align = 'numeric'
    legend.subCols[2].dx = -40
    legend.subCols[2].minWidth = col_t_year_min_width

    legend.subCols[3].align = 'numeric'
    legend.subCols[3].dx = -10
    legend.subCols[3].dx = -15
    legend.subCols[2].minWidth = col_change_min_width

    # legend.colorNamePairs   = Auto(obj=chart)
    legend.colorNamePairs = list(zip(_colors, names))
    legend.deltax = 75
    legend.subCols[0].minWidth = 90

    drawing = Drawing(width, height)
    drawing.add(chart, 'chart')
    drawing.add(legend, 'legend')
    drawing.add(legend_header, 'legend_header')

    return drawing


def exploding_pie(width=524, height=300, font_name='Helvetica', font_size=8):
    """
    Chart Features
    --------------

    This Pie chart itself is a simple chart with exploded slices:

    - **pie.slices.popout = 5**
    """
    padding_left = 25

    pie = Pie()

    pie.width = pie.height = width * 0.4
    pie.x = padding_left
    pie.y = padding_left
    pie.sameRadii = 1
    pie.direction = 'clockwise'
    pie.startAngle = 90
    # pie.slices[0].fillColor             = PCMYKColor(0,0,0,100)
    colors = [
        PCMYKColor(100, 0, 0, 0),
        PCMYKColor(100, 67, 0, 23),
        PCMYKColor(0, 95, 100, 0),
        PCMYKColor(0, 0, 0, 40),
        PCMYKColor(10, 0, 100, 11),
    ]
    for i, color in enumerate(colors):
        pie.slices[i].fillColor = color
    # pie.slices.strokeColor      = PCMYKColor(0,0,0,0)
    # pie.slices.strokeWidth      = 0.5
    # sample data
    pie.data = [30.0, 21.0, 21.0, 14.0, 14.0]
    pie.slices[0].fillColor = PCMYKColor(100, 0, 90, 50, alpha=85)
    pie.slices[1].fillColor = PCMYKColor(0, 100, 100, 40, alpha=85)
    pie.slices[2].fillColor = PCMYKColor(100, 60, 0, 50, alpha=85)
    pie.slices[3].fillColor = PCMYKColor(23, 51, 0, 4, alpha=85)
    pie.slices[4].fillColor = PCMYKColor(66, 13, 0, 22, alpha=85)
    pie.slices.popout = 5

    legend = Legend()
    legend.x = pie.width + padding_left + 50
    legend.y = height * (3 / 4)
    legend.fontSize = font_size
    legend.fontName = font_name
    legend.dx = 8
    legend.dy = 8
    legend.yGap = 0
    legend.deltay = 16
    legend.strokeColor = PCMYKColor(0, 0, 0, 0)
    legend.strokeWidth = 0
    legend.columnMaximum = 6
    legend.alignment = 'right'
    legend.colorNamePairs = [
        (PCMYKColor(100, 0, 90, 50, alpha=100), ('BP', '30%')),
        (
            PCMYKColor(0, 100, 100, 40, alpha=100),
            ('Shell Transport & Trading', '21%'),
        ),
        (
            PCMYKColor(100, 60, 0, 50, alpha=100),
            ('Liberty International', '21%'),
        ),
        (PCMYKColor(23, 51, 0, 4, alpha=100), ('Persimmon', '14%')),
        (
            PCMYKColor(66, 13, 0, 22, alpha=100),
            ('Royal Bank of Scotland', '14%'),
        ),
    ]
    legend.subCols.rpad = 12

    background = Rect(
        0,
        0,
        width,
        height,
        strokeColor=PCMYKColor(100, 0, 0, 0),
        fillColor=PCMYKColor(15, 0, 0, 0),
    )
    background.strokeWidth = 0.25
    background.fillColor = None

    drawing = Drawing(width, height)
    drawing.add(pie, 'pie')
    drawing.add(legend, 'legend')
    drawing.add(background, 'background')
    return drawing


def pie_with_nested_legend(
    width=524, height=300, font_name='Helvetica', font_size=8
):
    padding_top = 25
    padding_left = 25

    # chart
    chart = Pie()
    chart.width = width * 0.4  # 150
    chart.height = width * 0.4  # 150
    chart.x = width * 0.5  # 200
    chart.y = 25  # 25
    chart.slices.strokeColor = white
    chart.slices.strokeWidth = 0.25
    # colours
    colorsList = [
        PCMYKColor(100, 0, 90, 50),
        PCMYKColor(65.1, 72.16, 33.33, 14.51),
        PCMYKColor(50.98, 28.63, 41.18, 1.18),
        PCMYKColor(30.2, 30.59, 16.08, 0),
        PCMYKColor(0, 0, 0, 0),
        PCMYKColor(0, 0, 0, 0),
        PCMYKColor(0, 0, 0, 0),
    ]
    for i, color in enumerate(colorsList[:4]):
        chart.slices[i].fillColor = color
    # sample data
    chart.data = [
        41.600000000000001,
        29.999999999999996,
        26.400000000000002,
        2.0,
    ]
    chart.slices[0].fillColor = PCMYKColor(100, 60, 0, 50, alpha=100)
    chart.slices[1].fillColor = PCMYKColor(100, 0, 90, 50, alpha=100)
    chart.slices[2].fillColor = PCMYKColor(0, 100, 100, 40, alpha=100)
    chart.slices[3].fillColor = PCMYKColor(66, 13, 0, 22, alpha=100)

    # legend
    legend = Legend()
    legend.x = padding_left  # 12
    legend.y = height - padding_top  # 185
    legend.alignment = 'right'
    legend.boxAnchor = 'nw'
    legend.fontName = font_name
    legend.fontSize = 6
    legend.strokeWidth = 0
    legend.strokeColor = None
    legend.dy = 6
    legend.dx = 6
    legend.dxTextSpace = 4  # space between swatch and text
    legend.deltay = 6  # space between legend rows
    legend.columnMaximum = 99
    legend.variColumn = 1  #
    legend.deltax = 175
    legend.colorNamePairs = [
        (PCMYKColor(100, 60, 0, 50, alpha=100), (u'Relative Value', '41.6%')),
        (None, (u' Mortgage Arbitrage', '10.2%')),
        (None, (u' Relative Value Credit', '8.7%')),
        (None, (u' Equity L/S High Hedge', '6.1%')),
        (None, (u' Convertible Arbitrage', '4.9%')),
        (None, (u' Fixed Income Arbitrage', '3.9%')),
        (None, (u' Statistical Arbitrage', '3.1%')),
        (None, (u' Volatility Arbitrage', '2.5%')),
        (None, (u' Closed End Fund', '1.7%')),
        (None, (u' Other Arbitrage', '0.5%')),
        (PCMYKColor(100, 0, 90, 50, alpha=100), (u'Event Driven', '30.0%')),
        (None, (u' Restructurings and Value', '13.8%')),
        (None, (u' Merger/Risk Arbitrage', '5.6%')),
        (None, (u' Event Driven Credit', '4.9%')),
        (None, (u' Distressed', '3.7%')),
        (None, (u' Private Placements', '2.0%')),
        (PCMYKColor(0, 100, 100, 40, alpha=100), (u'Opportunistic', '26.4%')),
        (None, (u' Equity L/S Opportunistic', '18.8%')),
        (None, (u' Macro', '3.7%')),
        (None, (u' Other Opportunistic', '2.1%')),
        (None, (u' CTA/Managed Futures', '1.8%')),
        (PCMYKColor(66, 13, 0, 22, alpha=100), (u'Cash', '2.0%')),
    ]

    drawing = Drawing(width, height)
    drawing.add(chart, 'chart')
    drawing.add(legend, 'legend')
    return drawing


def pie_with_a_pie(width=524, height=300, font_name='Helvetica', font_size=8):
    """
    Chart Features
        --------------

        This chart is created by adding two pies and some graphics on the same canvas. It may seem a bit
        fiddly to do all this to lay out a single chart, but if you consider the fact that this single
        python module can now be used to generate batches of thousands of charts, with different
        data for each passed in dynamically, you can appreciate that a bit of work up front to get an
        exact template can save massively.
    """
    colorsList1 = [
        PCMYKColor(0, 0, 0, 100, spotName='XXX X', alpha=100),
        PCMYKColor(50, 0, 25, 30, spotName='7475C', alpha=100),
        PCMYKColor(50, 0, 25, 30, spotName='7475C', density=40, alpha=100),
        PCMYKColor(0, 0, 0, 50, spotName='XXX X', alpha=100),
        PCMYKColor(0, 0, 0, 25, spotName='XXX X', alpha=100),
        PCMYKColor(0, 0, 0, 40, spotName='XXX X', alpha=100),
        PCMYKColor(50, 0, 25, 30, spotName='7475C', density=25, alpha=100),
        PCMYKColor(0, 0, 0, 25, spotName='XXX X', alpha=100),
    ]
    colorsList2 = [
        CMYKColor(0, 0, 0, 0.64, spotName='XXX X', density=0.8, alpha=1),
        CMYKColor(0, 0, 0, 0.48, spotName='XXX X', density=0.6, alpha=1),
        CMYKColor(0, 0, 0, 0.32, spotName='XXX X', density=0.4, alpha=1),
        CMYKColor(0, 0, 0, 0.2, spotName='XXX X', density=0.25, alpha=1),
        CMYKColor(0, 0, 0, 0.8, spotName='XXX X', alpha=1),
    ]

    # pie 1
    pie1 = Pie()
    pie1.y = 112
    pie1.x = 12
    pie1.data = [
        85.799999999999997,
        1.5,
        11.199999999999999,
        1.6000000000000001,
    ]
    pie1.width = 77
    pie1.height = 77
    pie1.sameRadii = 1
    for i in range(len(pie1.data)):
        pie1.slices[i].fillColor = colorsList1[i]
    pie1.slices.strokeColor = PCMYKColor(0, 0, 0, 0)
    pie1.slices.strokeWidth = 0.5
    pie1.slices[0].fillColor = PCMYKColor(
        100, 60, 0, 50, spotName='XXX X', alpha=100
    )
    pie1.slices[1].fillColor = PCMYKColor(
        66, 13, 0, 22, spotName='7475C', alpha=100
    )
    pie1.slices[2].fillColor = PCMYKColor(0, 100, 100, 40, alpha=100)
    pie1.slices[3].fillColor = PCMYKColor(
        100, 0, 90, 50, spotName='XXX X', alpha=100
    )

    # pie2
    pie2 = Pie()
    pie2.x = 105
    pie2.y = 112
    pie2.data = [86.0, 14.0]
    pie2.width = 46
    pie2.height = 46
    pie2.sameRadii = 1
    for i in range(len(pie2.data)):
        pie2.slices[i].fillColor = colorsList2[i]
    pie2.slices.strokeColor = PCMYKColor(0, 0, 0, 0)
    pie2.slices.strokeWidth = 0.5

    # legend 1
    legend1 = Legend()
    legend1.y = 100
    legend1.x = 12
    legend1.boxAnchor = 'nw'
    legend1.alignment = 'right'
    legend1.fontName = font_name
    legend1.fontSize = font_size
    legend1.dx = 7
    legend1.dy = 7
    legend1.yGap = 0
    legend1.deltax = 10
    legend1.deltay = 20
    legend1.strokeWidth = 0
    legend1.strokeColor = PCMYKColor(0, 0, 0, 0)
    legend1.columnMaximum = 10
    legend1.colorNamePairs = [
        (
            PCMYKColor(100, 60, 0, 50, spotName='XXX X', alpha=100),
            u'Government\nFunds: 85.8%',
        ),
        (
            PCMYKColor(66, 13, 0, 22, spotName='7475C', alpha=100),
            u'Contributions: 1.5%',
        ),
        (PCMYKColor(0, 100, 100, 40, alpha=100), u'Investments: 11.2%'),
        (
            PCMYKColor(100, 0, 90, 50, spotName='XXX X', alpha=100),
            u'other: 1.6%',
        ),
    ]

    # legend 2
    legend2 = Legend()
    legend2.y = 100
    legend2.x = 100
    legend2.alignment = 'right'
    legend2.fontName = font_name
    legend2.fontSize = font_size
    legend2.dx = 7
    legend2.dy = 7
    legend2.yGap = 0
    legend2.deltax = 10
    legend2.deltay = 20
    legend2.strokeWidth = 0
    legend2.strokeColor = PCMYKColor(0, 0, 0, 0)
    legend2.columnMaximum = 10
    legend2.colorNamePairs = [
        (
            CMYKColor(0, 0, 0, 0.64, spotName='XXX X', density=0.8, alpha=1),
            u'Grants: 86.0%',
        ),
        (
            CMYKColor(0, 0, 0, 0.48, spotName='XXX X', density=0.6, alpha=1),
            u'Loans: 14.0%',
        ),
    ]
    vline = Line(85, 230, 85, 184)
    vline.x1 = 97
    vline.x2 = 97
    vline.y2 = 112
    vline.y1 = 160
    vline.strokeColor = PCMYKColor(0, 0, 0, 75)

    topline = Line(85, 230, 93, 230)
    topline.x1 = 97
    topline.x2 = 105
    topline.y1 = 112
    topline.y2 = 112
    topline.strokeColor = PCMYKColor(0, 0, 0, 75)

    midline = Line(77, 207, 85, 207)
    midline.x1 = 89
    midline.x2 = 97
    midline.y1 = 137
    midline.y2 = 137
    midline.strokeColor = PCMYKColor(0, 0, 0, 75)

    butline = Line(85, 184, 93, 184)
    butline.x1 = 97
    butline.y1 = 160
    butline.x2 = 105
    butline.y2 = 160
    butline.strokeColor = PCMYKColor(0, 0, 0, 75)

    drawing = Drawing(width, height)
    drawing.add(pie1, 'pie1')
    drawing.add(pie2, 'pie2')
    drawing.add(legend1, 'legend1')
    drawing.add(legend2, 'legend2')
    drawing.add(vline, 'vline')
    drawing.add(topline, 'topline')
    drawing.add(midline, 'midline')
    drawing.add(butline, 'butline')

    return drawing


def legend_with_text_wrapping(
    width=155, height=138, font_name='Helvetica', font_size=8
):
    """
    Chart Features
    --------------

    - The legend text is wrapped and the extra wrapped text goes below the first line.

    - The maximum number of rows in the legend is four, then the legend moves to the right
    to start a new column of rows.
    """
    pie = Pie()
    pie.height = 150
    pie.width = 150
    pie.x = 25
    pie.y = 25
    colors = [
        PCMYKColor(40, 0, 7, 40, alpha=100),
        PCMYKColor(0, 12, 9, 87, alpha=100),
        PCMYKColor(30, 0, 6, 33, alpha=100),
        PCMYKColor(0, 4, 4, 69, alpha=100),
        PCMYKColor(21, 0, 5, 25, alpha=100),
        PCMYKColor(0, 2, 2, 52, alpha=100),
    ]
    pie.data = [
        30.600000000000001,
        8.5,
        39.299999999999997,
        7.7000000000000002,
        11.6,
        2.2000000000000002,
    ]
    pie.sameRadii = 1
    for i in range(len(pie.data)):
        pie.slices[i].fillColor = colors[i]
    pie.slices.strokeColor = PCMYKColor(0, 0, 0, 0)
    pie.slices.strokeWidth = 0.5
    pie.slices[0].fillColor = PCMYKColor(23, 51, 0, 4, alpha=100)
    pie.slices[1].fillColor = PCMYKColor(0, 100, 100, 40, alpha=100)
    pie.slices[5].fillColor = PCMYKColor(0, 61, 22, 25, alpha=100)
    pie.slices[2].fillColor = PCMYKColor(100, 60, 0, 50, alpha=100)
    pie.slices[3].fillColor = PCMYKColor(100, 0, 90, 50, alpha=100)
    pie.slices[4].fillColor = PCMYKColor(66, 13, 0, 22, alpha=100)

    legend = Legend()
    legend.x = 325
    legend.y = 100
    legend.alignment = 'right'
    legend.fontName = font_name
    legend.fontSize = font_size
    legend.dx = 6.5
    legend.dy = 6.5
    legend.yGap = 0
    legend.deltax = 10
    legend.deltay = 10
    legend.strokeColor = PCMYKColor(0, 0, 0, 0)
    legend.strokeWidth = 0
    legend.columnMaximum = 4
    legend.boxAnchor = 'c'
    legend.colorNamePairs = [
        (PCMYKColor(23, 51, 0, 4, alpha=100), u'Europe: 30.6'),
        (PCMYKColor(0, 100, 100, 40, alpha=100), u'Japan: 8.5'),
        (PCMYKColor(100, 60, 0, 50, alpha=100), u'US/Canada: 39.3'),
        (PCMYKColor(100, 0, 90, 50, alpha=100), u'Asia ex Japan: 7.7'),
        (PCMYKColor(66, 13, 0, 22, alpha=100), u'Latin\nAmerica/Other: 11.6'),
        (PCMYKColor(0, 61, 22, 25, alpha=100), u'Australia/New\nZealand: 2.2'),
    ]

    drawing = Drawing(width, height)
    drawing.add(pie, 'pie')
    drawing.add(legend, 'legend')
    return drawing
