# copyright ReportLab Europe Limited. 2000-2016
# see license.txt for license details
__version__ = '3.3.0'
"""
Handy constructor for a decent range of Excel-like charts.

Our current model assumes that you explicitly position
things on a drawing, and there is no automatic layout.
In some cases - particularly when embedding the chart library
in another app - there is a need for something 'quick and simple'
which makes some automatic layout decisions.

This adds a 'layer over the top' which can quickly create
a drawing to order, with title, legend, chart, various
labels and so on - and which will make vaguely sensible
decisions about the space taken up by each.

A second goal is to provide a finite and consistent
set of properties, so that anyone trying to make
(for example) a simple chart-editing GUI in their
app can do so.  If you are working with, say, the Quark
API, it is almost impossible to create a drill-down
property editor.

Anyone wishing to do further customisation than this
function permits can then set properties on the Drawing
which it returns.

The layout logic first looks at the number of
'things' in the drawing:  title, legend, chart,
axis labels.  It notes which are present or
absent, and the position of the legend.  It divides

方便的构造函数，用于制作一系列类似Excel的图表。

我们当前的模型假定您在图纸上明确放置了东西，并且没有自动布局。 
在某些情况下，尤其是在将图表库嵌入另一个应用程序时，需要“快速而简单”的方法来做出一些自动布局决策。

这样会在顶部上方添加一个“图层”，该图层可以快速创建包含标题，图例，图表，各种标签等的图纸，从而对每个图纸所占空间做出明智的决策。

第二个目标是提供一组有限且一致的属性，以便任何尝试在其应用程序中制作（例如）简单的图表编辑GUI的人都可以这样做。 
例如，如果使用Quark API，则几乎不可能创建下钻属性编辑器。

任何希望进行超出此功能允许范围的自定义的人都可以在返回的图形上设置属性。

布局逻辑首先查看图形中“事物”的数量：标题，图例，图表，轴标签。 它记录存在或不存在的图例以及图例的位置。 它分裂
"""
import sys
from functools import reduce

from reportlab.lib.colors import *
from reportlab.rl_config import _FUZZ
from reportlab.lib.extformat import magicformat
from reportlab.graphics.shapes import Drawing, String, Rect, Line, Group
from reportlab.graphics.widgetbase import Widget, ScaleWidget
from reportlab.graphics.widgets.markers import Marker
from reportlab.lib.validators import _isColor
from reportlab.lib.utils import isStr, asBytes, safer_globals
from reportlab.graphics.charts.axes import TickLabeller

from report.core.graphics.layout import getBounds, Sizer


# area 面积图
CHART_TYPE_AREA = 'area'
CHART_TYPE_AREA_STACKED = 'stacked_area'
CHART_TYPE_AREA_PERCENT = 'percent_area'
# bar 柱状图
CHART_TYPE_BAR = 'bar'
CHART_TYPE_BAR_3D = 'bar3d'
CHART_TYPE_BAR_CLUSTERED = 'clustered_bar'
CHART_TYPE_BAR_PERCENT = 'percent_bar'
CHART_TYPE_BAR_STACKED = 'stacked_bar'
# bubble 泡沫
CHART_TYPE_BUBBLE = 'bubble'
# column 柱状图
CHART_TYPE_COLUMN = 'column'
CHART_TYPE_COLUMN_3D = 'column3d'
CHART_TYPE_COLUMN_CLUSTERED = 'clustered_column'
CHART_TYPE_COLUMN_PERCENT = 'percent_column'
CHART_TYPE_COLUMN_STACKED = 'stacked_column'
# doughnut 甜甜圈
CHART_TYPE_DOUGHNUT = 'doughnut'
# line chart 折线图
CHART_TYPE_LINE_CHART = 'linechart'
CHART_TYPE_LINE_CHART_MARKERS = 'linechart_markers'
CHART_TYPE_LINE_CHART_3D = 'linechart3d'
CHART_TYPE_LINE_PLOT = 'lineplot'
CHART_TYPE_LINE_PLOT_MARKERS = 'lineplot_markers'
CHART_TYPE_LINE_PLOT_3D = 'lineplot3d'
# pie 饼图
CHART_TYPE_PIE = 'pie'
CHART_TYPE_PIE_3D = 'pie3d'
CHART_TYPE_PIE_EXPLODED = 'exploded_pie'
CHART_TYPE_PIE_EXPLODED_3D = 'exploded_pie3d'
# radar 雷达
CHART_TYPE_RADAR = 'radar'
CHART_TYPE_RADAR_FILLED = 'filled_radar'
CHART_TYPE_RADAR_MARKERS = 'radar_markers'
# scatter 分散
CHART_TYPE_SCATTER = 'scatter'
CHART_TYPE_SCATTER_LINES = 'scatter_lines'
CHART_TYPE_SCATTER_LINES_MARKERS = 'scatter_lines_markers'

CHART_TYPES = [
    CHART_TYPE_AREA,
    CHART_TYPE_AREA_STACKED,
    CHART_TYPE_AREA_PERCENT,
    CHART_TYPE_BAR,
    CHART_TYPE_BAR_3D,
    CHART_TYPE_BAR_CLUSTERED,
    CHART_TYPE_BAR_PERCENT,
    CHART_TYPE_BAR_STACKED,
    CHART_TYPE_BUBBLE,
    CHART_TYPE_COLUMN,
    CHART_TYPE_COLUMN_3D,
    CHART_TYPE_COLUMN_CLUSTERED,
    CHART_TYPE_COLUMN_PERCENT,
    CHART_TYPE_COLUMN_STACKED,
    CHART_TYPE_DOUGHNUT,
    CHART_TYPE_LINE_CHART,
    CHART_TYPE_LINE_CHART_MARKERS,
    CHART_TYPE_LINE_CHART_3D,
    CHART_TYPE_LINE_PLOT,
    CHART_TYPE_LINE_PLOT_MARKERS,
    CHART_TYPE_LINE_PLOT_3D,
    CHART_TYPE_PIE,
    CHART_TYPE_PIE_3D,
    CHART_TYPE_PIE_EXPLODED,
    CHART_TYPE_PIE_EXPLODED_3D,
    CHART_TYPE_RADAR,
    CHART_TYPE_RADAR_FILLED,
    CHART_TYPE_RADAR_MARKERS,
    CHART_TYPE_SCATTER,
    CHART_TYPE_SCATTER_LINES,
    CHART_TYPE_SCATTER_LINES_MARKERS,
]

LEGEND_POSITION_NONE = None
LEGEND_POSITION_LEFT = 'left'
LEGEND_POSITION_RIGHT = 'right'
LEGEND_POSITION_TOP = 'top'
LEGEND_POSITION_BOTTOM = 'bottom'
LEGEND_POSITION_TOP_LEFT = 'top_left'
LEGEND_POSITION_TOP_RIGHT = 'top_right'
LEGEND_POSITION_BOTTOM_RIGHT = 'bottom_right'
LEGEND_POSITION_BOTTOM_LEFT = 'bottom_left'
LEGEND_POSITION_MIDDLE = 'middle'

LEGEND_POSITIONS = [
    LEGEND_POSITION_NONE,
    LEGEND_POSITION_LEFT,
    LEGEND_POSITION_RIGHT,
    LEGEND_POSITION_TOP,
    LEGEND_POSITION_BOTTOM,
    LEGEND_POSITION_TOP_LEFT,
    LEGEND_POSITION_TOP_RIGHT,
    LEGEND_POSITION_BOTTOM_RIGHT,
    LEGEND_POSITION_BOTTOM_LEFT,
    LEGEND_POSITION_MIDDLE,
]

MARKER_NONE = None
MARKER_SEQUENCE = 'Sequence'  # 序列
MARKER_FILLED_CIRCLE = 'FilledCircle'  # 圈
MARKER_FILLED_SQUARE = 'FilledSquare'  # 矩形
MARKER_FILLED_DIAMOND = 'FilledDiamond'  # 菱形
MARKER_FILLED_CROSS = 'FilledCross'  # 十字架、叉
MARKER_FILLED_TRIANGLE = 'FilledTriangle'  # 三角形
MARKER_FILLED_STAR_SIX = 'FilledStarSix'  # 六角星
MARKER_FILLED_PENTAGON = 'FilledPentagon'  # 五角星
MARKER_FILLED_HEXAGON = 'FilledHexagon'  # 六边形
MARKER_FILLED_HEPTAGON = 'FilledHeptagon'  # 七边形
MARKER_FILLED_OCTAGON = 'FilledOctagon'  # 八边形

MARKERS = [
    MARKER_NONE,
    MARKER_SEQUENCE,
    MARKER_FILLED_CIRCLE,
    MARKER_FILLED_SQUARE,
    MARKER_FILLED_DIAMOND,
    MARKER_FILLED_CROSS,
    MARKER_FILLED_TRIANGLE,
    MARKER_FILLED_STAR_SIX,
    MARKER_FILLED_PENTAGON,
    MARKER_FILLED_HEXAGON,
    MARKER_FILLED_HEPTAGON,
    MARKER_FILLED_OCTAGON,
]

# colour names as comments at the end of each line are as a memory jogger ONLY
# NOT HTML named colours!
# 在每行末尾作为注释的颜色名称仅作为内存慢跑器使用，而不是HTML命名颜色！

# Main colours as used for bars etc
# 用于bars等的主要颜色
mainColours = [
    PCMYKColor(40, 40, 0, 0),  # Lavender  薰衣草
    PCMYKColor(0, 66, 33, 39),  # Maroon  栗色
    PCMYKColor(0, 0, 20, 0),  # Yellow  黄色
    PCMYKColor(20, 0, 0, 0),  # Cyan 青色
    PCMYKColor(0, 100, 0, 59),  # Purple 紫色
    PCMYKColor(0, 49, 49, 0),  # Salmon 鲑鱼色
    PCMYKColor(100, 49, 0, 19),  # Blue  蓝色
    PCMYKColor(20, 20, 0, 0),  # PaleLavender 淡 薰衣草色
    PCMYKColor(100, 100, 0, 49),  # NavyBlue 深蓝色
    PCMYKColor(0, 100, 0, 0),  # Purple 紫色
]
# Highlight colors - eg for the tops of bars
# 突出显示颜色-例如条形图的顶部
highlightColours = [
    PCMYKColor(39, 39, 0, 25),  # Light Lavender  淡薰衣草
    PCMYKColor(0, 66, 33, 54),  # Light Maroon 栗色
    PCMYKColor(0, 0, 19, 25),  # Light Yellow 黄色
    PCMYKColor(19, 0, 0, 25),  # Light Cyan 青色
    PCMYKColor(0, 100, 0, 69),  # Light Purple 紫色
    PCMYKColor(0, 49, 49, 25),  # Light Salmon 鲑鱼色
    PCMYKColor(100, 49, 0, 39),  # Light Blue 蓝色
    PCMYKColor(19, 19, 0, 25),  # Light PaleLavender  淡 薰衣草色
    PCMYKColor(100, 100, 0, 62),  # Light NavyBlue 深蓝色
    PCMYKColor(0, 100, 0, 25),  # Light Purple 紫色
]
# Lowlight colors - eg for the sides of bars
# 弱光颜色-例如条形的侧面
darkColours = [
    PCMYKColor(39, 39, 0, 49),  # Dark Lavender 淡薰衣草
    PCMYKColor(0, 66, 33, 69),  # Dark Maroon 栗色
    PCMYKColor(0, 0, 20, 49),  # Dark Yellow 黄色
    PCMYKColor(20, 0, 0, 49),  # Dark Cyan 青色
    PCMYKColor(0, 100, 0, 80),  # Dark Purple 紫色
    PCMYKColor(0, 50, 50, 49),  # Dark Salmon 鲑鱼色
    PCMYKColor(100, 50, 0, 59),  # Dark Blue 蓝色
    PCMYKColor(20, 20, 0, 49),  # Dark PaleLavender 淡 薰衣草色
    PCMYKColor(100, 100, 0, 79),  # Dark NavyBlue 深蓝色
    PCMYKColor(0, 100, 0, 49),  # Dark Purple 紫色
]
# for standard grey backgrounds
# 对于标准的灰色背景
backgroundGrey = PCMYKColor(0, 0, 0, 24)  # 灰色


class ChartError(Exception):
    pass


class LegendPositionError(Exception):
    pass


def getTestDrawing():
    """Helper for testing other programs.  Always returns the same chart!
    用于测试其他程序的助手。 始终返回相同的图表！"""
    d = Drawing(300, 200)
    d.add(
        String(
            150,
            180,
            'Test Drawing with column chart and bar code',
            textAnchor='middle',
        )
    )

    chart = getColumnChart(chartColors=mainColours)
    chart.x = 50
    chart.y = 65
    chart.width = 225
    chart.height = 100
    d.add(chart)

    from reportlab.graphics.barcode.widgets import BarcodeCode128

    bc = BarcodeCode128()
    bc.value = 'AB-12345678'
    bc.x = 100
    bc.y = 20
    d.add(bc)
    d.add(
        String(
            130,
            10,
            'AB-12345678',
            textAnchor='start',
            fontName='Courier',
            fontSize=7,
        )
    )
    return d


class DrawingLayout:
    """Data packet for where things go
    数据包的去向"""

    pass


def _simpleData(data):
    """
    if list of sequences return first else return thing itself
    如果序列列表首先返回，否则返回事物本身
    @param data:
    @return:
    """
    if isinstance(data[0], (list, tuple)):
        return data[0]
    return data


def _makeFakes(n, names, label):
    if names is None:
        return None
    elif isinstance(names, str):
        names = names.split()
        if len(names) == 1:
            if names[0].lower() == 'none':
                return None
            if names[0] == 'auto':
                return tuple(
                    map(lambda i, label=label: ('%s %d' % (label, i)), range(n))
                )
    i = len(names)
    if i > n:
        names = names[:n]
    elif i < n:
        names = list(names[:]) + (n - i) * ['']
    return tuple(names)


def _convertAngle(angle, default=0):
    if not angle or isinstance(angle, str) and angle.lower() == 'none':
        angle = default
    return float(angle)


def _boxConstrain(obj, width, height):
    x1, y1, x2, y2 = getBounds(obj)
    w = x2 - x1
    h = y2 - y1
    if w > width + _FUZZ or h > height + _FUZZ:
        scale = min(width / float(w), height / float(h))
        w = scale * w
        h = scale * h
        obj = ScaleWidget(scale=scale, contents=obj)
    return obj, w, h


def _bestHorizontalLegendColumnMaximum(n, aW, aH, w, h):
    """
    @param n: number of legend elements 图例元素数量
    @param aW: available width 可用宽度
    @param aH: available height 可用高度
    @param w: one row width 一排宽度
    @param h: one row height 一排高度
    @return:
    """
    w = w / float(n)
    m = n / (int(n ** 0.5) + 1)
    bc = 1e308
    for r in range(1, m + 1):
        c = int(n / r)
        eW = w * c
        eH = r * h
        if r == 1 and eW <= aW:
            return r
        c = abs(min(aW / float(eW), aH / float(eH)) - 1)
        if c < bc:
            bc = c
            br = r
    return br


def _showBBox(obj, d, strokeColor=pink, strokeWidth=0.5):
    x0, y0, x1, y1 = getBounds(obj)
    d.add(
        Rect(
            x0,
            y0,
            x1 - x0,
            y1 - y0,
            strokeWidth=0.5,
            strokeColor=strokeColor,
            fillColor=None,
        )
    )


def quickChart(
    chartType=CHART_TYPE_COLUMN,
    width=400,
    height=270,
    # array of data for the chart. 图表的数据数组。
    data="100 120 140 160\n110 130 150 180",
    textData=None,
    categoryNames=None,
    seriesNames=None,
    # series arrangement 系列安排
    seriesRelation=None,  # or 'stacked' or 'percent'
    # colors for chart
    # 图表颜色
    chartColors=None,
    # chart title
    # 图表标题
    titleText='',
    titleFontName='Helvetica',
    titleFontSize=None,
    titleFontColor=black,
    # big labels saying what each axis is
    # 大标签说出每个轴是什么
    xTitleText='',
    xTitleFontName='Helvetica',
    xTitleFontSize=None,
    xTitleFontColor=black,
    yTitleText='',
    yTitleFontName='Helvetica',
    yTitleFontSize=None,
    yTitleFontColor=black,
    # visibility and text properties for each axis
    # 每个轴的可见性和文本属性
    xAxisVisible=1,
    xAxisGridLines=0,  # 0 or 1
    xAxisFontName='Helvetica',
    xAxisFontSize=None,
    xAxisFontColor=black,
    xAxisLabelAngle=None,
    xAxisLabelTextFormat=None,
    xAxisLabelTextScale=None,
    yAxisVisible=1,
    yAxisGridLines=0,  # 0 or 1
    yAxisFontName='Helvetica',
    yAxisFontSize=None,
    yAxisFontColor=black,
    yAxisLabelAngle=None,
    yAxisLabelTextFormat=None,
    yAxisLabelTextScale=None,
    # data labels.
    # 数据标签。
    dataLabelsType=None,
    # None, values, percentage, labels/fields(?)
    # 无，值，百分比，标签/字段（？）
    dataLabelsFontName='Helvetica',
    dataLabelsFontSize=None,
    dataLabelsFontColor=black,
    dataLabelsAlignment=None,
    # top, bottom, center or None (for default)
    # 顶部，底部，中心或无（默认）
    # markers for lines eg, in scatter_lines_markers
    # 线标记，例如散布线标记
    markerType=None,
    markerSize=6,
    # legend properties.
    # 图例属性。
    legendPos='right',
    legendText=None,
    legendFontName='Helvetica',
    legendFontSize=None,
    legendFontColor=None,
    # background of entire drawing
    # 整个图纸的背景
    bgColor=None,
    plotColor=backgroundGrey,
    bgStrokeColor=None,
    chartFillColors=None,
    chartStrokeColors=None,
    chartStrokeWidth=None,
    chartSeparation=0,
    # 'advanced' arguments which may be needed by a power user
    # 高级用户可能需要的“高级”参数
    showBoundaries=0,  # show how space is divided up, 展示如何划分空间，
    drawingClass=Drawing,
    pad=None,
    padMax=None,
    padMin=None,
    padFrac=0.05,
    checkLabelOverlap=0,
    orderMode='fixed',
    pointerLabelMode=None,
    legendVariColumn=1,
    legendXPad=None,
    legendYPad=None,
    legendMaxHFrac=None,
    legendMaxWFrac=None,
    hleg=None,  # force horizontal legend, 强制水平图例
    legendMode='fullWidth',
):
    """
    Returns a drawing containing chart, title, and possibly legend.
    返回包含图表，标题和可能的图例的图形。
    """

    ###########################################################################
    #
    #  Phase 1 - check and normalize inputs.  Accept string input where possible
    #  阶段1-检查并归一化输入。 尽可能接受字符串输入
    #
    ###########################################################################

    # check inputs as early as possible.  IN general we allow string inputs
    # 尽早检查输入。 一般来说，我们允许字符串输入
    if chartType not in CHART_TYPES:
        raise ChartError(f'图表类型: {chartType} 不支持, 仅支持: {"、".join(CHART_TYPES)}')

    if legendPos not in LEGEND_POSITIONS:
        raise LegendPositionError(
            f'图例位置: {chartType} 不支持, 仅支持: {"、".join(LEGEND_POSITIONS)}'
        )

    width = float(width)
    height = float(height)
    _3d = chartType.endswith('3d')

    # sort out types:
    if seriesRelation in ['None', None]:
        seriesRelation = 'sidebyside'  # default

    # BAR subtypes
    if chartType in (CHART_TYPE_BAR_CLUSTERED, CHART_TYPE_BAR_3D):
        chartType = CHART_TYPE_BAR  # subtype same as basic bar
        seriesRelation = 'sidebyside'
    elif chartType == CHART_TYPE_AREA_STACKED:
        chartType = CHART_TYPE_AREA
        seriesRelation = 'stacked'
    elif chartType == CHART_TYPE_BAR_STACKED:
        chartType = CHART_TYPE_BAR
        seriesRelation = 'stacked'
    elif chartType == CHART_TYPE_AREA_PERCENT:
        chartType = CHART_TYPE_AREA
        seriesRelation = 'percent'
    elif chartType == CHART_TYPE_BAR_PERCENT:
        chartType = CHART_TYPE_BAR
        seriesRelation = 'percent'

    # COLUMN subtypes
    elif chartType in (CHART_TYPE_COLUMN_CLUSTERED, CHART_TYPE_COLUMN_3D):
        chartType = CHART_TYPE_COLUMN  # subtype same as basic column
        seriesRelation = 'sidebyside'
    elif chartType == CHART_TYPE_COLUMN_STACKED:
        chartType = CHART_TYPE_COLUMN
        seriesRelation = 'stacked'
    elif chartType == CHART_TYPE_COLUMN_PERCENT:
        chartType = CHART_TYPE_COLUMN
        seriesRelation = 'percent'

    if data is not None:
        if isinstance(data, str):
            data = parseDataBlock(data)
    if textData and isinstance(textData, str):
        textData = parseDataBlock(
            textData, asText=1, maxLen=max(list(map(len, data)))
        )

    _data = data

    oneLevel = chartType in (
        CHART_TYPE_PIE,
        CHART_TYPE_PIE_3D,
        CHART_TYPE_PIE_EXPLODED,
        CHART_TYPE_PIE_EXPLODED_3D,
    )

    reqDim = 1
    if chartType in (
        CHART_TYPE_SCATTER,
        CHART_TYPE_SCATTER_LINES,
        CHART_TYPE_SCATTER_LINES_MARKERS,
        CHART_TYPE_LINE_PLOT,
        CHART_TYPE_LINE_PLOT_3D,
        CHART_TYPE_LINE_PLOT_MARKERS,
    ):
        reqDim = 2
    elif chartType == CHART_TYPE_BUBBLE:
        reqDim = 3

    if oneLevel:
        nSeries = 1
        if not isinstance(_data[0], (list, tuple)):
            _data = [_data]
        data = _simpleData(data)
        nCategories = len(data)
    else:
        nSeries = len(data)
        nCategories = len(data[0])
        if reqDim > 1:
            data = data[:]
            zData = None
            if nSeries == 1:
                xData = 'auto'
                if reqDim == 3:
                    zData = [data]
                    data = [list(range(nCategories))]
            elif reqDim == 3:
                if nSeries & 1:
                    xData = data.pop(0)
                else:
                    xData = 'auto'
                oData, data = data, []
                zData = []
                while oData:
                    data.append(oData.pop(0))
                    zData.append(oData.pop(0))
            else:
                xData = data.pop(0)
            nSeries = len(data)

    if chartType.endswith('markers'):
        # make sure there are markers
        markerType = markerType or MARKER_SEQUENCE
        # make sure they are visible
        markerSize = 8 if markerSize < 3 else markerSize

    # check series and category names - fake them if required
    seriesNames = _makeFakes(nSeries, seriesNames, 'series')
    categoryNames = _makeFakes(nCategories, categoryNames, 'category')

    # compute font sizes to pass into chart.  There are many optional font sizes
    # and it saves us code to assign the default values early.
    FONT_SIZE_BIG = 0.075 * height
    FONT_SIZE_MEDIUM = 0.05 * height
    FONT_SIZE_SMALL = 0.0375 * height
    if titleFontSize is None:
        titleFontSize = FONT_SIZE_BIG
    if xTitleFontSize is None:
        xTitleFontSize = FONT_SIZE_MEDIUM
    if yTitleFontSize is None:
        yTitleFontSize = FONT_SIZE_MEDIUM
    if xAxisFontSize is None:
        xAxisFontSize = FONT_SIZE_SMALL
    if yAxisFontSize is None:
        yAxisFontSize = FONT_SIZE_SMALL
    if dataLabelsFontSize is None:
        dataLabelsFontSize = FONT_SIZE_SMALL
    if dataLabelsFontColor is None:
        dataLabelsFontColor = black
    if legendFontSize is None:
        legendFontSize = FONT_SIZE_SMALL
    if legendFontColor is None:
        legendFontColor = black
    xAxisLabelAngle = _convertAngle(xAxisLabelAngle, default=0)
    yAxisLabelAngle = _convertAngle(yAxisLabelAngle, default=0)

    # sort out chart colours
    if chartColors == None:
        chartColors = mainColours
    else:
        newcols = []

        def addcol(col, newcols=newcols):
            try:
                newcol = toColor(col)
                newcols.append(newcol)
            except:
                raise ValueError("unknown color %s in chartColors" % col)

        if isinstance(chartColors, (list, tuple)):
            for col in chartColors:
                if isStr(col):
                    addcol(col)
                elif isinstance(col, Color):
                    newcols.append(col)
                else:
                    raise ValueError("unknown color %s in chartColors" % col)
        else:
            listfound = 0
            try:
                # is it already a list/tuple which has been converted to a
                # string?
                cols = eval(chartColors, safer_globals())
                for col in cols:
                    if isStr(col):
                        addcol(col)
                    else:
                        coltest = _isColor()
                        if coltest.test(col):
                            newcols.append(col)
                        else:
                            raise ValueError(
                                "unknown color %s in chartColors" % col
                            )
                listfound = 1
            except:
                pass  # OK, maybe not. silently fail
            if not listfound:
                # allow comma separated lines
                C = chartColors.split(',')
                if len(C) > 1:
                    for col in C:
                        addcol(col.strip())
                # allow space separated lines
            else:
                C = chartColors.split(' ')
                for col in C:
                    if col:
                        addcol(col)
        if newcols != []:
            chartColors = newcols

    if isinstance(titleFontSize, str):
        titleFontSize = float(titleFontSize)
    if isinstance(xTitleFontSize, str):
        xTitleFontSize = float(xTitleFontSize)
    if isinstance(yTitleFontSize, str):
        yTitleFontSize = float(yTitleFontSize)
    if isinstance(xAxisFontSize, str):
        xAxisFontSize = float(xAxisFontSize)
    if isinstance(yAxisFontSize, str):
        yAxisFontSize = float(yAxisFontSize)
    if isinstance(legendFontSize, str):
        legendFontSize = float(legendFontSize)

    if isinstance(titleFontColor, str):
        titleFontColor = toColor(titleFontColor)
    if isinstance(xTitleFontColor, str):
        xTitleFontColor = toColor(xTitleFontColor)
    if isinstance(yTitleFontColor, str):
        yTitleFontColor = toColor(yTitleFontColor)
    if isinstance(xAxisFontColor, str):
        xAxisFontColor = toColor(xAxisFontColor)
    if isinstance(yAxisFontColor, str):
        yAxisFontColor = toColor(yAxisFontColor)
    if isinstance(legendFontColor, str):
        legendFontColor = toColor(legendFontColor)

    # make one up
    if drawingClass is Drawing:
        d = drawingClass(width, height)
    else:
        d = drawingClass()

    if bgColor == 'None':
        bgColor = None
    elif isinstance(bgColor, str):
        bgColor = toColor(bgColor)

    if bgStrokeColor == 'None':
        bgStrokeColor = None
    elif isinstance(bgStrokeColor, str):
        bgStrokeColor = toColor(bgStrokeColor)

    d.add(
        Rect(
            0,
            0,
            width,
            height,
            strokeColor=bgStrokeColor,
            strokeWidth=1,
            fillColor=bgColor,
        )
    )

    rect_stroke_color = bgStrokeColor
    rect_stroke_width = 1
    rect_fill_color = bgColor

    if bgColor is None and bgStrokeColor is not None:
        rect_fill_color = None
    elif bgColor is not None and bgStrokeColor is None:
        rect_stroke_color = None
        rect_stroke_width = 0

    d.add(
        Rect(
            0,
            0,
            width,
            height,
            strokeColor=rect_stroke_color,
            strokeWidth=rect_stroke_width,
            fillColor=rect_fill_color,
        )
    )

    if dataLabelsFontName in ('None', None):
        dataLabelsFontName = 'Helvetica'
    if isinstance(dataLabelsFontSize, str):
        dataLabelsFontSize = float(dataLabelsFontSize)
    elif dataLabelsFontSize in ('None', None):
        dataLabelsFontSize = labelFontSize
    if isinstance(dataLabelsFontColor, str):
        dataLabelsFontColor = toColor(dataLabelsFontColor)
    #    if dataLabelsAlignment in ('None', None):
    #        dataLabelsAlignment = "top"
    # ZZZ - delete me if successful
    if dataLabelsType in ('None', None):
        dataLabelsFormat = None
    elif dataLabelsType in ('values', 'ivalues'):
        dataLabelsFormat = makeDataLabels(
            '%(value)s',
            _data,
            textData,
            None,
            None,
            oneLevel,
            tryInt=dataLabelsType == 'ivalues',
        )
        if oneLevel:
            dataLabelsFormat = dataLabelsFormat[0]
    elif dataLabelsType.startswith('percent'):
        _ = dataLabelsType.split(',')
        decimals = len(_) > 1 and int(_[1]) or 0
        dataLabelsFormat = percentLabels(
            _data, decimals=decimals, oneLevel=oneLevel
        )
        if oneLevel:
            dataLabelsFormat = dataLabelsFormat[0]
    elif dataLabelsType == 'label':
        dataLabelsFormat = makeDataLabels(
            '%(category)s', _data, textData, None, None, oneLevel
        )
        if oneLevel:
            dataLabelsFormat = dataLabelsFormat[0]
    elif isinstance(dataLabelsType, str) and dataLabelsType.find('%(') >= 0:
        dataLabelsFormat = makeDataLabels(
            dataLabelsType,
            _data,
            textData,
            categoryNames,
            seriesNames,
            oneLevel,
        )
        if oneLevel:
            dataLabelsFormat = dataLabelsFormat[0]
    elif chartType in [
        CHART_TYPE_PIE,
        CHART_TYPE_PIE_EXPLODED,
        CHART_TYPE_PIE_3D,
        CHART_TYPE_PIE_EXPLODED_3D,
        CHART_TYPE_DOUGHNUT,
    ]:
        fmt = dataLabelsType
        if fmt.find('%') >= 0 and fmt.find('%(') < 0:
            fmt = fmt.replace('%', '%(value)')
        dataLabelsFormat = makeDataLabels(
            fmt, _data, textData, categoryNames, seriesNames, oneLevel
        )
        if oneLevel:
            dataLabelsFormat = dataLabelsFormat[0]
    else:
        dataLabelsFormat = dataLabelsType

    if plotColor == 'None':
        plotColor = None
    elif plotColor == '(default)':
        plotColor = backgroundGrey
    elif isinstance(plotColor, str):
        plotColor = toColor(plotColor)
    elif plotColor == '(default)':
        plotColor = backgroundGrey
    elif isinstance(plotColor, str):
        plotColor = toColor(plotColor)

    ########################################################
    #
    #    Lay out the chart
    #
    ########################################################

    # compute the regions needed based on some heuristics

    # first step is to divide the space into 9 regions,
    # and assign a relative weight to each.  These will
    # be used to get proportions.  prefix w = weight
    # here are the defaults:
    PAD = pad
    if PAD is None:
        if padFrac is not None:
            PAD = (
                min(height, width) * padFrac
            )  # generic padding between objects
    if not PAD:
        PAD = 0
    if padMin is not None:
        PAD = max(padMin, PAD)
    if padMax is not None:
        PAD = min(padMax, PAD)

    TOP_USED = LEFT_USED = RIGHT_USED = BOTTOM_USED = PAD

    # figure out what objects to place
    if titleText:
        title = String(
            0,
            0,
            titleText,
            fontName=titleFontName,
            fontSize=titleFontSize,
            textAnchor='start',
            fillColor=titleFontColor,
        )
        (x1, y1, x2, y2) = getBounds(title)
        titleHeight = y2 - y1
        titleWidth = x2 - x1
        title.x = 0.5 * (width - titleWidth)
        from reportlab.pdfbase.pdfmetrics import getFont

        ascent = getFont(titleFontName).face.ascent * (titleFontSize / 1000.0)
        title.y = height - PAD - ascent
        TOP_USED = PAD + 1.1 * ascent - y1
        d.add(title, 'title')
        if showBoundaries:
            _showBBox(title, d)

    if legendPos is not None:
        leg = getLegend()
        # showBoundary = 0
        leg.fontName = legendFontName
        leg.fontSize = legendFontSize
        leg.fillColor = legendFontColor
        lc = []
        if chartType in (
            CHART_TYPE_PIE,
            CHART_TYPE_PIE_EXPLODED,
            CHART_TYPE_PIE_3D,
            CHART_TYPE_PIE_EXPLODED_3D,
            CHART_TYPE_DOUGHNUT,
        ):
            # pies etc
            for i in range(nCategories):
                t = (
                    chartColors[i % len(chartColors)],
                    categoryNames and str(categoryNames[i]) or '',
                )
                lc.append(t)
        else:
            # bars/columns or other multi-series charts
            for i in range(nSeries):
                t = (
                    chartColors[i % len(chartColors)],
                    seriesNames and str(seriesNames[i]) or '',
                )
                lc.append(t)
        if hleg is None:
            hleg = legendPos in (LEGEND_POSITION_TOP, LEGEND_POSITION_BOTTOM)
        leg.colorNamePairs = lc
        leg.dx = leg.dy = legendFontSize
        leg.deltay = legendFontSize - 2 + legendFontSize * 0.6
        leg.variColumn = legendVariColumn
        if legendXPad is None:
            legendXPad = PAD
        if legendYPad is None:
            legendYPad = PAD
        aW = width - (legendXPad + PAD)
        aH = height - (TOP_USED + 2 * legendYPad)
        if legendMaxWFrac and (
            (legendMaxWFrac < 0 and not hleg) or legendMaxWFrac > 0
        ):
            aW = min(max(legendXPad, abs(legendMaxWFrac * width)), aW)
        if legendMaxHFrac and (
            (legendMaxHFrac < 0 and hleg) or legendMaxHFrac > 0
        ):
            aH = min(max(legendYPad, abs(legendMaxHFrac * height)), aH)
        n = len(lc)
        if hleg:
            leg.columnMaximum = 1
            if n >= 3:
                x1, y1, x2, y2 = getBounds(leg)
                leg.columnMaximum = _bestHorizontalLegendColumnMaximum(
                    n, aW, aH, x2 - x1, y2 - y1
                )
        else:
            leg.columnMaximum = int(aH / legendFontSize * 1.2)
        if 1:
            leg, legendWidth, legendHeight = _boxConstrain(leg, aW, aH)
        else:
            x1, y1, x2, y2 = getBounds(leg)
            legendWidth = x2 - x1
            legendHeight = y2 - y1
        d.add(leg, 'legend')

        if legendMode is None:
            legendMode = ('fullHeight', 'fullWidth')[hleg]

        # what's the x coordinate of the legend?
        if legendPos in (
            LEGEND_POSITION_LEFT,
            LEGEND_POSITION_TOP_LEFT,
            LEGEND_POSITION_BOTTOM_LEFT,
        ):
            if legendMode == 'fullHeight' or legendPos == 'left':
                LEFT_USED = legendXPad + legendWidth + legendXPad
            leg.x = legendXPad
        elif legendPos in (
            LEGEND_POSITION_RIGHT,
            LEGEND_POSITION_TOP_RIGHT,
            LEGEND_POSITION_BOTTOM_RIGHT,
        ):
            if legendMode == 'fullHeight' or legendPos == 'right':
                RIGHT_USED = legendXPad + legendWidth + legendXPad
            leg.x = width - legendWidth - legendXPad
        elif legendPos in (
            LEGEND_POSITION_TOP,
            LEGEND_POSITION_MIDDLE,
            LEGEND_POSITION_BOTTOM,
        ):
            leg.x = 0.5 * width - 0.5 * legendWidth  # left column has nothing

        if legendPos in (
            LEGEND_POSITION_TOP,
            LEGEND_POSITION_TOP_RIGHT,
            LEGEND_POSITION_TOP_LEFT,
        ):
            if titleText:
                leg.y = (
                    height - (PAD + legendYPad) - titleHeight
                )  # allows for title
                # if it's there
                if legendMode == 'fullWidth' or legendPos == 'top':
                    TOP_USED = max(
                        TOP_USED,
                        PAD + 2 * legendYPad + titleHeight + legendHeight,
                    )
            else:
                leg.y = height - legendYPad
                if legendMode == 'fullWidth' or legendPos == 'top':
                    TOP_USED = max(TOP_USED, 2 * legendYPad + legendHeight)
        # center in slab
        elif legendPos in [
            LEGEND_POSITION_LEFT,
            LEGEND_POSITION_MIDDLE,
            LEGEND_POSITION_RIGHT,
        ]:
            leg.y = BOTTOM_USED + 0.5 * (
                height - TOP_USED - BOTTOM_USED + legendHeight
            )
        elif legendPos in (
            LEGEND_POSITION_BOTTOM,
            LEGEND_POSITION_BOTTOM_LEFT,
            LEGEND_POSITION_BOTTOM_RIGHT,
        ):
            leg.y = PAD + legendHeight
            if legendMode == 'fullWidth' or legendPos == 'bottom':
                BOTTOM_USED = legendYPad + legendHeight + legendYPad

        if showBoundaries:
            _showBBox(leg, d, strokeColor=palegreen)

    # for debugging, show the bounds box
    if showBoundaries:
        d.add(
            Rect(
                LEFT_USED,
                BOTTOM_USED,
                width - RIGHT_USED - LEFT_USED,
                height - TOP_USED - BOTTOM_USED,
                fillColor=None,
                strokeWidth=0.5,
                strokeColor=red,
            )
        )

    chart = None
    if chartType == CHART_TYPE_COLUMN:
        chart = getColumnChart(
            width,
            height,
            seriesRelation=seriesRelation,
            fontSize=dataLabelsFontSize,
            data=data,
            chartColors=chartColors,
            categoryNames=categoryNames,
            seriesNames=seriesNames,
            plotColor=plotColor,
            xAxisVisible=xAxisVisible,
            xAxisGridLines=xAxisGridLines,
            xAxisFontName=xAxisFontName,
            xAxisFontSize=xAxisFontSize,
            xAxisFontColor=xAxisFontColor,
            xAxisLabelAngle=xAxisLabelAngle,
            xAxisLabelTextFormat=xAxisLabelTextFormat,
            xAxisLabelTextScale=xAxisLabelTextScale,
            yAxisVisible=yAxisVisible,
            yAxisGridLines=yAxisGridLines,
            yAxisFontName=yAxisFontName,
            yAxisFontSize=yAxisFontSize,
            yAxisFontColor=yAxisFontColor,
            yAxisLabelAngle=yAxisLabelAngle,
            yAxisLabelTextFormat=yAxisLabelTextFormat,
            yAxisLabelTextScale=yAxisLabelTextScale,
            dataLabelsFormat=dataLabelsFormat,
            dataLabelsFontName=dataLabelsFontName,
            dataLabelsFontSize=dataLabelsFontSize,
            dataLabelsFontColor=dataLabelsFontColor,
            dataLabelsAlignment=dataLabelsAlignment,
            _3d=_3d,
        )

    elif chartType == CHART_TYPE_BAR:
        chart = getBarChart(
            width,
            height,
            seriesRelation=seriesRelation,
            fontSize=dataLabelsFontSize,
            data=data,
            chartColors=chartColors,
            categoryNames=categoryNames,
            seriesNames=seriesNames,
            plotColor=plotColor,
            xAxisVisible=xAxisVisible,
            xAxisGridLines=xAxisGridLines,
            xAxisFontName=xAxisFontName,
            xAxisFontSize=xAxisFontSize,
            xAxisFontColor=xAxisFontColor,
            xAxisLabelAngle=xAxisLabelAngle,
            xAxisLabelTextFormat=xAxisLabelTextFormat,
            xAxisLabelTextScale=xAxisLabelTextScale,
            yAxisVisible=yAxisVisible,
            yAxisGridLines=yAxisGridLines,
            yAxisFontName=yAxisFontName,
            yAxisFontSize=yAxisFontSize,
            yAxisFontColor=yAxisFontColor,
            yAxisLabelAngle=yAxisLabelAngle,
            yAxisLabelTextFormat=yAxisLabelTextFormat,
            yAxisLabelTextScale=yAxisLabelTextScale,
            dataLabelsFormat=dataLabelsFormat,
            dataLabelsFontName=dataLabelsFontName,
            dataLabelsFontSize=dataLabelsFontSize,
            dataLabelsFontColor=dataLabelsFontColor,
            dataLabelsAlignment=dataLabelsAlignment,
            _3d=_3d,
        )

    elif chartType in (
        CHART_TYPE_LINE_CHART,
        CHART_TYPE_LINE_CHART_MARKERS,
        CHART_TYPE_LINE_CHART_3D,
    ):
        chart = getLineChart(
            width,
            height,
            seriesRelation=seriesRelation,
            fontSize=dataLabelsFontSize,
            data=data,
            chartColors=chartColors,
            categoryNames=categoryNames,
            seriesNames=seriesNames,
            plotColor=plotColor,
            xAxisVisible=xAxisVisible,
            xAxisGridLines=xAxisGridLines,
            xAxisFontName=xAxisFontName,
            xAxisFontSize=xAxisFontSize,
            xAxisFontColor=xAxisFontColor,
            xAxisLabelAngle=xAxisLabelAngle,
            xAxisLabelTextFormat=xAxisLabelTextFormat,
            xAxisLabelTextScale=xAxisLabelTextScale,
            yAxisVisible=yAxisVisible,
            yAxisGridLines=yAxisGridLines,
            yAxisFontName=yAxisFontName,
            yAxisFontSize=yAxisFontSize,
            yAxisFontColor=yAxisFontColor,
            yAxisLabelAngle=yAxisLabelAngle,
            yAxisLabelTextFormat=yAxisLabelTextFormat,
            yAxisLabelTextScale=yAxisLabelTextScale,
            dataLabelsFormat=dataLabelsFormat,
            dataLabelsFontName=dataLabelsFontName,
            dataLabelsFontSize=dataLabelsFontSize,
            dataLabelsFontColor=dataLabelsFontColor,
            markerType=markerType,
            markerSize=markerSize,
            _3d=_3d,
        )

    elif chartType in (
        CHART_TYPE_LINE_PLOT,
        CHART_TYPE_LINE_PLOT_MARKERS,
        CHART_TYPE_LINE_PLOT_3D,
    ):
        chart = getLinePlot(
            width,
            height,
            seriesRelation=seriesRelation,
            fontSize=dataLabelsFontSize,
            data=blockToMultiSeries(xData, data, None),
            chartColors=chartColors,
            categoryNames=categoryNames,
            seriesNames=seriesNames,
            plotColor=plotColor,
            xAxisVisible=xAxisVisible,
            xAxisGridLines=xAxisGridLines,
            xAxisFontName=xAxisFontName,
            xAxisFontSize=xAxisFontSize,
            xAxisFontColor=xAxisFontColor,
            xAxisLabelAngle=xAxisLabelAngle,
            xAxisLabelTextFormat=xAxisLabelTextFormat,
            xAxisLabelTextScale=xAxisLabelTextScale,
            yAxisVisible=yAxisVisible,
            yAxisGridLines=yAxisGridLines,
            yAxisFontName=yAxisFontName,
            yAxisFontSize=yAxisFontSize,
            yAxisFontColor=yAxisFontColor,
            yAxisLabelAngle=yAxisLabelAngle,
            yAxisLabelTextFormat=yAxisLabelTextFormat,
            yAxisLabelTextScale=yAxisLabelTextScale,
            dataLabelsFormat=dataLabelsFormat,
            dataLabelsFontName=dataLabelsFontName,
            dataLabelsFontSize=dataLabelsFontSize,
            dataLabelsFontColor=dataLabelsFontColor,
            markerType=markerType,
            markerSize=markerSize,
            _3d=_3d,
        )
    elif chartType == CHART_TYPE_SCATTER:
        if markerType in (None, "None", "none"):
            markerType = MARKER_SEQUENCE
        chart = getScatterPlot(
            width,
            height,
            seriesRelation=seriesRelation,
            fontSize=dataLabelsFontSize,
            xData=xData,
            yData=data,
            zData=zData,
            chartColors=chartColors,
            categoryNames=categoryNames,
            seriesNames=seriesNames,
            plotColor=plotColor,
            xAxisVisible=xAxisVisible,
            xAxisGridLines=xAxisGridLines,
            xAxisFontName=xAxisFontName,
            xAxisFontSize=xAxisFontSize,
            xAxisFontColor=xAxisFontColor,
            xAxisLabelAngle=xAxisLabelAngle,
            xAxisLabelTextFormat=xAxisLabelTextFormat,
            xAxisLabelTextScale=xAxisLabelTextScale,
            yAxisVisible=yAxisVisible,
            yAxisGridLines=yAxisGridLines,
            yAxisFontName=yAxisFontName,
            yAxisFontSize=yAxisFontSize,
            yAxisFontColor=yAxisFontColor,
            yAxisLabelAngle=yAxisLabelAngle,
            yAxisLabelTextFormat=yAxisLabelTextFormat,
            yAxisLabelTextScale=yAxisLabelTextScale,
            dataLabelsFormat=dataLabelsFormat,
            dataLabelsFontName=dataLabelsFontName,
            dataLabelsFontSize=dataLabelsFontSize,
            dataLabelsFontColor=dataLabelsFontColor,
            markerType=markerType,
            markerSize=markerSize,
        )

    elif chartType in (
        CHART_TYPE_SCATTER_LINES,
        CHART_TYPE_SCATTER_LINES_MARKERS,
    ):
        chart = getScatterLinesPlot(
            width,
            height,
            seriesRelation=seriesRelation,
            fontSize=dataLabelsFontSize,
            xData=xData,
            yData=data,
            zData=zData,
            chartColors=chartColors,
            categoryNames=categoryNames,
            seriesNames=seriesNames,
            plotColor=plotColor,
            xAxisVisible=xAxisVisible,
            xAxisGridLines=xAxisGridLines,
            xAxisFontName=xAxisFontName,
            xAxisFontSize=xAxisFontSize,
            xAxisFontColor=xAxisFontColor,
            xAxisLabelAngle=xAxisLabelAngle,
            xAxisLabelTextFormat=xAxisLabelTextFormat,
            xAxisLabelTextScale=xAxisLabelTextScale,
            yAxisVisible=yAxisVisible,
            yAxisGridLines=yAxisGridLines,
            yAxisFontName=yAxisFontName,
            yAxisFontSize=yAxisFontSize,
            yAxisFontColor=yAxisFontColor,
            yAxisLabelAngle=yAxisLabelAngle,
            yAxisLabelTextFormat=yAxisLabelTextFormat,
            yAxisLabelTextScale=yAxisLabelTextScale,
            dataLabelsFormat=dataLabelsFormat,
            dataLabelsFontName=dataLabelsFontName,
            dataLabelsFontSize=dataLabelsFontSize,
            dataLabelsFontColor=dataLabelsFontColor,
            markerType=markerType,
            markerSize=markerSize,
        )
    elif chartType == CHART_TYPE_BUBBLE:
        chart = getBubblePlot(
            width=width,
            height=height,
            seriesRelation=seriesRelation,
            fontSize=dataLabelsFontSize,
            xData=xData,
            yData=data,
            zData=zData,
            chartColors=chartColors,
            categoryNames=categoryNames,
            seriesNames=seriesNames,
            plotColor=plotColor,
            xAxisVisible=xAxisVisible,
            xAxisGridLines=xAxisGridLines,
            xAxisFontName=xAxisFontName,
            xAxisFontSize=xAxisFontSize,
            xAxisFontColor=xAxisFontColor,
            xAxisLabelAngle=xAxisLabelAngle,
            xAxisLabelTextFormat=xAxisLabelTextFormat,
            xAxisLabelTextScale=xAxisLabelTextScale,
            yAxisVisible=yAxisVisible,
            yAxisGridLines=yAxisGridLines,
            yAxisFontName=yAxisFontName,
            yAxisFontSize=yAxisFontSize,
            yAxisFontColor=yAxisFontColor,
            yAxisLabelAngle=yAxisLabelAngle,
            yAxisLabelTextFormat=yAxisLabelTextFormat,
            yAxisLabelTextScale=yAxisLabelTextScale,
            dataLabelsFormat=dataLabelsFormat,
            dataLabelsFontName=dataLabelsFontName,
            dataLabelsFontSize=dataLabelsFontSize,
            dataLabelsFontColor=dataLabelsFontColor,
            markerType=markerType,
            markerSize=markerSize,
        )

    elif chartType in (
        CHART_TYPE_PIE,
        CHART_TYPE_PIE_3D,
        CHART_TYPE_PIE_EXPLODED,
        CHART_TYPE_PIE_EXPLODED_3D,
    ):
        chart = getPieChart(
            width,
            height,
            data=data,
            chartColors=chartColors,
            dataLabelsFormat=dataLabelsFormat,
            dataLabelsFontName=dataLabelsFontName,
            dataLabelsFontSize=dataLabelsFontSize,
            dataLabelsFontColor=dataLabelsFontColor,
            popout=chartType.startswith('exploded_') and 10 or 0,
            chartType=chartType,
            checkLabelOverlap=checkLabelOverlap,
            orderMode=orderMode,
            pointerLabelMode=pointerLabelMode,
        )

    elif chartType == CHART_TYPE_DOUGHNUT:
        chart = getDoughnutChart(
            width,
            height,
            data=data,
            chartColors=chartColors,
            categoryNames=categoryNames,
            seriesNames=seriesNames,
            dataLabelsFormat=dataLabelsFormat,
            dataLabelsFontName=dataLabelsFontName,
            dataLabelsFontSize=dataLabelsFontSize,
            dataLabelsFontColor=dataLabelsFontColor,
        )

    elif chartType == CHART_TYPE_RADAR:
        chart = getRadarChart(
            width,
            height,
            data=data,
            chartColors=chartColors,
            categoryNames=categoryNames,
            seriesNames=seriesNames,
            plotColor=plotColor,
            dataLabelsFormat=dataLabelsFormat,
            dataLabelsFontName=dataLabelsFontName,
            dataLabelsFontSize=dataLabelsFontSize,
            dataLabelsFontColor=dataLabelsFontColor,
            spokeLabelFontName=yAxisFontName,
            spokeLabelFontSize=yAxisFontSize,
            spokeLabelFontColor=yAxisFontColor,
        )

    elif chartType == CHART_TYPE_RADAR_FILLED:
        chart = getFilledRadarChart(
            width,
            height,
            data=data,
            chartColors=chartColors,
            categoryNames=categoryNames,
            seriesNames=seriesNames,
            plotColor=plotColor,
            dataLabelsFormat=dataLabelsFormat,
            dataLabelsFontName=dataLabelsFontName,
            dataLabelsFontSize=dataLabelsFontSize,
            dataLabelsFontColor=dataLabelsFontColor,
            spokeLabelFontName=yAxisFontName,
            spokeLabelFontSize=yAxisFontSize,
            spokeLabelFontColor=yAxisFontColor,
        )

    elif chartType == CHART_TYPE_RADAR_MARKERS:
        chart = getRadarMarkersChart(
            width,
            height,
            data=data,
            chartColors=chartColors,
            categoryNames=categoryNames,
            seriesNames=seriesNames,
            plotColor=plotColor,
            dataLabelsFormat=dataLabelsFormat,
            dataLabelsFontName=dataLabelsFontName,
            dataLabelsFontSize=dataLabelsFontSize,
            dataLabelsFontColor=dataLabelsFontColor,
            spokeLabelFontName=yAxisFontName,
            spokeLabelFontSize=yAxisFontSize,
            spokeLabelFontColor=yAxisFontColor,
            markerType=markerType,
            markerSize=markerSize,
        )

    elif chartType == CHART_TYPE_AREA:
        chart = getLinePlotArea(
            width,
            height,
            seriesRelation=seriesRelation,
            fontSize=dataLabelsFontSize,
            data=data,
            chartColors=chartColors,
            categoryNames=categoryNames,
            seriesNames=seriesNames,
            plotColor=plotColor,
            xAxisVisible=xAxisVisible,
            xAxisGridLines=xAxisGridLines,
            xAxisFontName=xAxisFontName,
            xAxisFontSize=xAxisFontSize,
            xAxisFontColor=xAxisFontColor,
            xAxisLabelAngle=xAxisLabelAngle,
            xAxisLabelTextFormat=xAxisLabelTextFormat,
            xAxisLabelTextScale=xAxisLabelTextScale,
            yAxisVisible=yAxisVisible,
            yAxisGridLines=yAxisGridLines,
            yAxisFontName=yAxisFontName,
            yAxisFontSize=yAxisFontSize,
            yAxisFontColor=yAxisFontColor,
            yAxisLabelAngle=yAxisLabelAngle,
            yAxisLabelTextFormat=yAxisLabelTextFormat,
            yAxisLabelTextScale=yAxisLabelTextScale,
            dataLabelsFormat=dataLabelsFormat,
            dataLabelsFontName=dataLabelsFontName,
            dataLabelsFontSize=dataLabelsFontSize,
            dataLabelsFontColor=dataLabelsFontColor,
            markerType=markerType,
            markerSize=markerSize,
        )

    if chart is None:
        chart = String(
            width * 0.5,
            height * 0.5,
            'Not done yet: %s chart (%d x %d)' % (chartType, width, height),
            textAnchor='middle',
        )
    elif chartType in [
        'pie',
        'exploded_pie',
        'pie3d',
        'exploded_pie3d',
        'radar',
        'filled_radar',
        'radar_markers',
        'doughnut',
    ]:

        # square bounds box
        # simple for the moment - just centres square bounds box in the
        # middle of
        # the drawing unless it would overlap the legend etc
        # no allowance for labels and other furniture
        availWidth = width - RIGHT_USED - LEFT_USED
        availHeight = height - TOP_USED - BOTTOM_USED
        chart = scale_chart(
            chart,
            LEFT_USED,
            BOTTOM_USED,
            availWidth,
            availHeight,
            square=not _3d,
        )
    else:  # rectangular plot
        # first we must position the x and y axis text.

        if yTitleText:
            yTitle = String(
                0,
                0,
                yTitleText,
                fontName=yTitleFontName,
                fontSize=yTitleFontSize,
                fillColor=yTitleFontColor,
                textAnchor='middle',
            )
            (x1, y1, x2, y2) = getBounds(yTitle)
            yTitleWidth = x2 - x1
            yTitleHeight = y2 - y1 + 0.25 * yTitleFontSize
            LEFT_TITLE_SPACE = 0 + yTitleHeight
        else:
            LEFT_TITLE_SPACE = 0.0

        if xTitleText:
            xTitle = String(
                0,
                0,
                xTitleText,
                fontName=xTitleFontName,
                fontSize=xTitleFontSize,
                fillColor=xTitleFontColor,
                textAnchor='middle',
            )
            (x1, y1, x2, y2) = getBounds(xTitle)
            xTitleWidth = x2 - x1
            xTitleHeight = y2 - y1
            BOTTOM_TITLE_SPACE = xTitleHeight
        else:
            BOTTOM_TITLE_SPACE = 0

        # position axis text
        if yTitleText:
            group = Group()
            group.transform = (
                0,
                1,
                -1,
                0,
                LEFT_USED + yTitle.fontSize,
                BOTTOM_USED
                + BOTTOM_TITLE_SPACE
                + 0.5 * (height - BOTTOM_USED - BOTTOM_TITLE_SPACE - TOP_USED),
            )
            group.add(yTitle)
            d.add(group)
        if xTitleText:
            xTitle.x = (
                LEFT_USED
                + LEFT_TITLE_SPACE
                + 0.5 * (width - LEFT_USED - LEFT_TITLE_SPACE - RIGHT_USED)
            )
            xTitle.y = BOTTOM_USED
            d.add(xTitle)

        # initial guess filling the available space with the plot rectangle.
        x = LEFT_USED + LEFT_TITLE_SPACE
        y = BOTTOM_USED + BOTTOM_TITLE_SPACE
        availWidth = width - RIGHT_USED - x
        availHeight = height - TOP_USED - y
        chart.x = 0
        chart.y = 0
        chart.width = availWidth
        chart.height = availHeight

        # find out how much the labels and ticks 'stick out' on all sides.
        (x1, y1, x2, y2) = getBounds(chart)
        CHART_LEFT_MARGIN = -x1
        CHART_BOTTOM_MARGIN = -y1
        CHART_RIGHT_MARGIN = x2 - chart.width
        CHART_TOP_MARGIN = y2 - chart.height

        # shrink the plot rectangle accordingly
        if _3d:
            CHART_RIGHT_MARGIN -= chart._3d_dx
            CHART_TOP_MARGIN -= chart._3d_dy
            sfx = availWidth / (availWidth + chart._3d_dx)
            sfy = availHeight / (availHeight + chart._3d_dy)
            chart.width = (
                availWidth - CHART_LEFT_MARGIN - CHART_RIGHT_MARGIN
            ) * sfx
            chart.height = (
                availHeight - CHART_TOP_MARGIN - CHART_BOTTOM_MARGIN
            ) * sfy
        else:
            chart.width = chart.width - CHART_LEFT_MARGIN - CHART_RIGHT_MARGIN
            chart.height = chart.height - CHART_TOP_MARGIN - CHART_BOTTOM_MARGIN

        chart.x = x + CHART_LEFT_MARGIN
        chart.y = y + CHART_BOTTOM_MARGIN

    d.add(chart, 'chart')
    return d


def scale_chart(chart, x, y, width, height, square=None):
    chart.x = 0
    chart.y = 0
    if square:
        side = min(width, height)
        chart.width = side
        chart.height = side
    else:
        chart.width = width
        chart.height = height
    (x1, y1, x2, y2) = getBounds(chart)
    expectedWidth = x2 - x1
    expectedHeight = y2 - y1
    sf = min(width / float(expectedWidth), height / float(expectedHeight), 1)
    if sf < 1:
        g = Group(
            transform=(
                sf,
                0,
                0,
                sf,
                x - sf * x1 + 0.5 * (width - sf * expectedWidth),
                y - sf * y1 + (height - sf * expectedHeight) * 0.5,
            )
        )
        g.add(chart, 'chart')
        chart = g
    elif square:
        chart.x = x + (width - side) * 0.5
        chart.y = y + (height - side) * 0.5
    else:
        chart.x = x
        chart.y = y
    return chart


def checkArgs(dict):
    """Verify all arguments, converting from string representation if needed.

    Raise relevant exceptions if bad argument types are given"""
    pass


###########################################################################
#
#  Data block manipulation helpers - turn 2d array into whatever needed
#
###########################################################################
def parseDataBlock(text, asText=0, maxLen=None):
    lines = text.split('\n')
    data = []
    if asText:
        default = ''
    else:
        default = None
    for line in lines:
        stripped = line.strip()
        if stripped != '':
            words = stripped.split()
            if asText:
                data.append(words)
            else:
                data.append(list(map(float, words)))

    # now check all same length
    if len(data):
        maxLen = maxLen or max(list(map(len, data)))
        for row in data:
            n = maxLen - len(row)
            if n > 0:
                row += n * [default]
    return data


def getLegendSize(rowCount, fontSize):
    "Quick guesstimate at legend size"
    height = 12 * rowCount + 5
    width = 20 + (15 * fontSize)
    return (width, height)


def normalizeData(data, decimals=None):
    "Return new data set where each group nsums to 100"
    colCount = len(data[0])
    rowCount = len(data)

    # make an empty matrix
    newBlock = []
    for row in range(rowCount):
        newBlock.append([0.0] * colCount)

    # fill it normalized
    for col in range(colCount):
        colTotal = 0.0
        for row in range(rowCount):
            assert data[row][col] is not None, (
                "Cannot accept null data points in " "percent style charts!"
            )
            colTotal = colTotal + data[row][col]
        if decimals is None:
            for row in range(rowCount):
                newBlock[row][col] = 100 * data[row][col] / colTotal
        else:
            from rlextra.utils.vecround import vecRound

            d = rowCount * [0]
            m = float(10 ** decimals)
            for row in range(rowCount):
                d[row] = 100 * data[row][col] / colTotal
            d = vecRound(d, m * 100, m)
            for row in range(rowCount):
                newBlock[row][col] = d[row]
    return newBlock


_DF = {}


def decfmt(n, dp=2, ds='.', ts=','):
    try:
        t = dp, ds, ts
        _df = _DF[t]
    except KeyError:
        from reportlab.lib.formatters import DecimalFormatter

        _df = _DF[t] = DecimalFormatter(
            places=dp, decimalSep=ds, thousandSep=ts
        )
    return _df(n)


def makeDataLabels(
    fmt,
    data,
    textData,
    categoryNames,
    seriesNames,
    oneLevel,
    decimals=0,
    tryInt=0,
):
    dpc = fmt.find('(percent') >= 0
    if dpc:
        if oneLevel:
            ndata = _simpleData(data)
            from operator import add

            ndata = list(
                map(
                    lambda x, sum=0.01 * float(reduce(add, ndata)): x / sum,
                    ndata,
                )
            )
            from rlextra.utils.vecround import vecRound

            f = float(10 ** decimals)
            ndata = [vecRound(ndata, f * 100, f)]
        else:
            ndata = normalizeData(data, decimals=decimals)
    else:
        ndata = data

    colCount = len(data[0])
    rowCount = len(data)
    if oneLevel:
        rowCount = min(rowCount, 1)
    category = ''
    series = ''

    if tryInt:
        from reportlab.graphics.charts.axes import _allInt
        from reportlab.lib.utils import flatten

        if _allInt(flatten(data)):
            data = [list(map(int, x)) for x in data]
    R = []
    textData = textData or data
    for row in range(rowCount):
        if seriesNames:
            series = seriesNames[row]
        r = []
        R.append(r)
        r = r.append
        for col in range(colCount):
            if categoryNames:
                category = categoryNames[col]
            value = textData[row][col]
            if dpc:
                try:
                    percent = ndata[row][col]
                except:
                    percent = 0
            r(magicformat(fmt))
    return R


class MakeTickLabels(TickLabeller):
    def __init__(self, fmt, **ns):
        self._fmt = fmt
        self._ns = ns

    def __call__(self, axis, value):
        ns = globals()
        ns.update(self._ns)
        ns['notAllInt'] = not axis._allIntTicks()
        ns['value'] = value
        return eval('magicformat(%r)' % self._fmt, ns)


def makeTickLabeller(fmt, **ns):
    if fmt is not None:
        return MakeTickLabels(fmt, **ns)


def percentLabels(data, decimals=0, oneLevel=None):
    "Return data block of strings with e.g. '67%'"
    return makeDataLabels(
        '%%(percent)%s%%%%' % (decimals and ('0.%df' % decimals) or 'd'),
        data,
        None,
        None,
        None,
        oneLevel,
        decimals=decimals,
    )


def setMarkers(aggr, markerType, markerSize, symbol='symbol'):
    """sets markers directly onto the lines/strands object"""
    if markerType == "Sequence":
        for i in range(2, len(MARKERS)):
            setattr(
                aggr[i - 2], symbol, Marker(kind=MARKERS[i], size=markerSize)
            )
    else:
        if markerType is not None:
            markerType = Marker(kind=markerType, size=markerSize)
        setattr(aggr, symbol, markerType)


def matrixToMultiSeries(data):
    "Turns tabular block into serieses with implicit x values 0,1,2..."
    colCount = len(data[0])
    newData = []
    for row in data:
        newSeries = []
        for i in range(colCount):
            newSeries.append((i, row[i]))
        newData.append(newSeries)
    return newData


def blockToMultiSeries(xData, yData, zData=None):
    "Turns tabular block yData into series with xData as first element"
    if xData == 'auto':
        xData = list(range(1, len(yData[0]) + 1))
    newData = []
    if zData:
        for y, z in zip(yData, zData):
            newData.append(list(zip(xData, y, z)))
    else:
        for y in yData:
            newData.append(list(zip(xData, y)))
    return newData


def _setColors(obj, C, a='fillColor'):
    for i, c in enumerate(C):
        setattr(obj[i], a, c)


def getColumnChart(
    width=200,
    height=150,
    fontSize=6,
    data=None,
    chartColors=None,
    categoryNames=None,
    seriesNames=None,
    plotColor=backgroundGrey,
    seriesRelation='sidebyside',
    xAxisVisible=1,
    xAxisGridLines=0,
    xAxisFontName='Helvetica',
    xAxisFontSize=6,
    xAxisFontColor=black,
    xAxisLabelAngle=0,
    xAxisLabelTextFormat=None,
    xAxisLabelTextScale=None,
    yAxisVisible=1,
    yAxisGridLines=1,
    yAxisFontName='Helvetica',
    yAxisFontSize=6,
    yAxisFontColor=black,
    yAxisLabelAngle=0,
    yAxisLabelTextFormat=None,
    yAxisLabelTextScale=None,
    dataLabelsFormat=None,
    dataLabelsFontName='Helvetica',
    dataLabelsFontSize=6,
    dataLabelsFontColor=black,
    dataLabelsAlignment=None,
    _3d=None,
):
    # raise Exception("format=%s" % dataLabelsFormat)
    if _3d:
        from reportlab.graphics.charts.barcharts import (
            VerticalBarChart3D as Klass,
        )
    else:
        from reportlab.graphics.charts.barcharts import (
            VerticalBarChart as Klass,
        )
    chart = Klass()
    valueAxis = chart.valueAxis
    categoryAxis = chart.categoryAxis

    _setColors(chart.bars, chartColors)
    chart.bars.strokeWidth = 0.5
    chart.fillColor = plotColor

    if isinstance(dataLabelsFormat, (list, tuple)):
        chart.barLabelFormat = 'values'
        chart.barLabelArray = dataLabelsFormat
    else:
        chart.barLabelFormat = dataLabelsFormat
    chart.barLabels.fontName = dataLabelsFontName
    chart.barLabels.fontSize = dataLabelsFontSize
    chart.barLabels.fillColor = dataLabelsFontColor

    valueAxis.labelTextFormat = makeTickLabeller(yAxisLabelTextFormat)
    valueAxis.labelTextScale = yAxisLabelTextScale
    valueAxis.visible = yAxisVisible
    categoryAxis.visible = xAxisVisible

    if seriesRelation == 'sidebyside':
        categoryAxis.style = 'parallel'
        chart.barLabels.dy = 0
        chart.barLabels.boxAnchor = 's'
    else:
        chart.barLabels.boxAnchor = 'n'
        chart.barLabels.dy = 0
        if seriesRelation == 'stacked':
            categoryAxis.style = 'stacked'
        elif seriesRelation == 'percent':
            categoryAxis.style = 'stacked'
            valueAxis.labelTextPostFormat = '%s%%'
            data = normalizeData(data)

    if dataLabelsAlignment not in (None, 'None'):
        if dataLabelsAlignment == "top":
            chart.barLabels.dy = 0.1 * dataLabelsFontSize
            chart.barLabels.boxAnchor = 's'
        elif dataLabelsAlignment == "bottom":
            chart.barLabels.dy = -(0.1 * dataLabelsFontSize)
            chart.barLabels.boxAnchor = 'n'
            chart.barLabels.boxFillColor = white
        elif dataLabelsAlignment == "center":
            chart.barLabels.dy = 0
            chart.barLabels.boxAnchor = 'c'
    else:
        if seriesRelation == 'percent' or seriesRelation == 'stacked':
            chart.barLabels.boxFillColor = white

    valueAxis.labels.fontName = yAxisFontName
    valueAxis.labels.fontSize = yAxisFontSize
    valueAxis.labels.fillColor = yAxisFontColor
    valueAxis.labels.angle = yAxisLabelAngle
    valueAxis.labels.textAnchor = 'boxauto'
    valueAxis.labels.boxAnchor = 'autoy'
    categoryAxis.labels.fontName = xAxisFontName
    categoryAxis.labels.fontSize = xAxisFontSize
    categoryAxis.labels.fillColor = xAxisFontColor
    categoryAxis.labels.angle = xAxisLabelAngle
    categoryAxis.labels.textAnchor = 'boxauto'
    categoryAxis.labels.boxAnchor = 'autox'
    if _3d:
        chart.barWidth = 10
        chart.barSpacing = 0
        chart.zSpace = 3
        chart.zDepth = 7.5

    if seriesRelation != 'percent':
        valueAxis.forceZero = 0  # 'near'
        valueAxis.avoidBoundFrac = (0.1, 0.1)
    else:
        valueAxis.valueMin = 0
        valueAxis.valueMax = 100
        valueAxis.avoidBoundFrac = None
    valueAxis.rangeRound = 'both'

    if data is not None:
        chart.data = data
        categoryAxis.categoryNames = categoryNames
    else:
        chart.data = [(100, 150, 180), (125, 180, 200)]
        categoryAxis.categoryNames = ['North', 'South', 'Central']
    chart.groupSpacing = 15
    if yAxisGridLines:
        valueAxis.visibleGrid = 1
    else:
        valueAxis.visibleGrid = 0
    if xAxisGridLines:
        categoryAxis.visibleGrid = 1
    else:
        categoryAxis.visibleGrid = 0

    valueAxis.tickLeft = 3
    categoryAxis.tickDown = 3

    return chart


def getBarChart(
    width=200,
    height=150,
    fontSize=6,
    data=None,
    chartColors=None,
    categoryNames=None,
    seriesNames=None,
    plotColor=backgroundGrey,
    seriesRelation='sidebyside',
    xAxisVisible=1,
    xAxisGridLines=0,
    xAxisFontName='Helvetica',
    xAxisFontSize=6,
    xAxisFontColor=black,
    xAxisLabelAngle=0,
    xAxisLabelTextFormat=None,
    xAxisLabelTextScale=None,
    yAxisVisible=1,
    yAxisGridLines=1,
    yAxisFontName='Helvetica',
    yAxisFontSize=6,
    yAxisFontColor=black,
    yAxisLabelAngle=0,
    yAxisLabelTextFormat=None,
    yAxisLabelTextScale=None,
    dataLabelsFormat=None,
    dataLabelsFontName='Helvetica',
    dataLabelsFontSize=6,
    dataLabelsFontColor=black,
    dataLabelsAlignment=None,
    _3d=None,
):
    # raise Exception("format=%s" % dataLabelsFormat)
    if _3d:
        from reportlab.graphics.charts.barcharts import (
            HorizontalBarChart3D as Klass,
        )
    else:
        from reportlab.graphics.charts.barcharts import (
            HorizontalBarChart as Klass,
        )
    chart = Klass()
    _setColors(chart.bars, chartColors)
    chart.bars.strokeWidth = 0.5
    chart.fillColor = plotColor
    valueAxis = chart.valueAxis
    categoryAxis = chart.categoryAxis

    if isinstance(dataLabelsFormat, (list, tuple)):
        chart.barLabelFormat = 'values'
        chart.barLabelArray = dataLabelsFormat
    else:
        chart.barLabelFormat = dataLabelsFormat
    chart.barLabels.fontName = dataLabelsFontName
    chart.barLabels.fontSize = dataLabelsFontSize
    chart.barLabels.fillColor = dataLabelsFontColor

    valueAxis.labels.fontName = xAxisFontName
    valueAxis.labels.fontSize = xAxisFontSize
    valueAxis.labels.fillColor = xAxisFontColor
    valueAxis.labels.angle = xAxisLabelAngle
    valueAxis.labels.textAnchor = 'boxauto'
    valueAxis.labels.boxAnchor = 'autox'
    valueAxis.visibleGrid = not not xAxisGridLines
    valueAxis.tickUp = 3
    valueAxis.visible = xAxisVisible
    valueAxis.labelTextFormat = makeTickLabeller(xAxisLabelTextFormat)
    valueAxis.labelTextScale = xAxisLabelTextScale

    categoryAxis.labels.fontName = yAxisFontName
    categoryAxis.labels.fontSize = yAxisFontSize
    categoryAxis.labels.fillColor = yAxisFontColor
    categoryAxis.labels.angle = yAxisLabelAngle
    categoryAxis.labels.textAnchor = 'boxauto'
    categoryAxis.labels.boxAnchor = 'autoy'
    categoryAxis.visibleGrid = not not yAxisGridLines
    categoryAxis.tickLeft = 3
    categoryAxis.visible = yAxisVisible

    chart.reversePlotOrder = 1
    if _3d:
        chart.barWidth = 10
        chart.barSpacing = 0
        chart.zSpace = 3
        chart.zDepth = 7.5

    if seriesRelation != 'percent':
        if seriesRelation == 'sidebyside':
            categoryAxis.style = 'parallel'
        elif seriesRelation == 'stacked':
            categoryAxis.style = 'stacked'
        valueAxis.forceZero = 0  # 'near'
        valueAxis.avoidBoundFrac = (0.1, 0.1)
        ba = seriesRelation == 'sidebyside' and 'w' or 'e'
    else:
        ba = 'e'
        categoryAxis.style = 'stacked'
        data = normalizeData(data)
        valueAxis.labelTextPostFormat = '%s%%'
        valueAxis.valueMin = 0
        valueAxis.valueMax = 100
        valueAxis.avoidBoundFrac = None
    chart.barLabels.dx = ba == 'w' and 2 or -2
    chart.barLabels.boxAnchor = ba

    if dataLabelsAlignment not in (None, 'None'):
        if dataLabelsAlignment == "top":
            chart.barLabels.dx = 0.1 * dataLabelsFontSize
            chart.barLabels.boxAnchor = 'w'
        elif dataLabelsAlignment == "bottom":
            chart.barLabels.dx = -(0.1 * dataLabelsFontSize)
            chart.barLabels.boxAnchor = 'e'
            chart.barLabels.boxFillColor = white
        elif dataLabelsAlignment == "center":
            chart.barLabels.dx = 0
            chart.barLabels.boxAnchor = 'c'
    else:
        if seriesRelation == 'percent' or seriesRelation == 'stacked':
            chart.barLabels.boxFillColor = white

    valueAxis.rangeRound = 'both'
    if data is not None:
        chart.data = data
        categoryAxis.categoryNames = categoryNames
    else:
        chart.data = [(100, 150, 180), (125, 180, 200)]
        categoryAxis.categoryNames = ['North', 'South', 'Central']
    chart.groupSpacing = 15
    return chart


def getLinePlot(
    width=200,
    height=150,
    fontSize=6,
    data=None,
    chartColors=None,
    categoryNames=None,
    seriesNames=None,
    plotColor=backgroundGrey,
    seriesRelation='sidebyside',
    xAxisVisible=1,
    xAxisGridLines=0,
    xAxisFontName='Helvetica',
    xAxisFontSize=6,
    xAxisFontColor=black,
    xAxisLabelAngle=0,
    xAxisLabelTextFormat=None,
    xAxisLabelTextScale=None,
    yAxisVisible=1,
    yAxisGridLines=1,
    yAxisFontName='Helvetica',
    yAxisFontSize=6,
    yAxisFontColor=black,
    yAxisLabelAngle=0,
    yAxisLabelTextFormat=None,
    yAxisLabelTextScale=None,
    dataLabelsFormat=None,
    dataLabelsFontName='Helvetica',
    dataLabelsFontSize=6,
    dataLabelsFontColor=black,
    markerType=None,
    markerSize=0,
    LinePlot=None,
    _3d=None,
):
    style = 'normal'
    if LinePlot is None:
        if _3d:
            from reportlab.graphics.charts.lineplots import (
                LinePlot3D as LinePlot,
            )

            style = 'parallel_3d'
        else:
            from reportlab.graphics.charts.lineplots import LinePlot
    chart = LinePlot()
    _setColors(chart.lines, chartColors, 'strokeColor')
    chart.fillColor = plotColor

    if isinstance(dataLabelsFormat, (list, tuple)):
        chart.lineLabelFormat = 'values'
        chart.lineLabelArray = dataLabelsFormat
    else:
        chart.lineLabelFormat = dataLabelsFormat
    chart.lineLabels.fontName = dataLabelsFontName
    chart.lineLabels.fontSize = dataLabelsFontSize
    chart.lineLabels.fillColor = dataLabelsFontColor

    xA = chart.xValueAxis
    yA = chart.yValueAxis
    xA.visible = xAxisVisible
    yA.visible = yAxisVisible

    yA.labelTextFormat = makeTickLabeller(yAxisLabelTextFormat)
    yA.labelTextScale = yAxisLabelTextScale
    yA.labels.fontName = yAxisFontName
    yA.labels.fontSize = yAxisFontSize
    yA.labels.fillColor = yAxisFontColor
    yA.labels.angle = yAxisLabelAngle
    yA.labels.textAnchor = 'boxauto'
    yA.labels.boxAnchor = 'autoy'
    yA.rangeRound = 'both'
    xA.labelTextFormat = makeTickLabeller(xAxisLabelTextFormat)
    xA.labelTextScale = xAxisLabelTextScale
    xA.labels.fontName = xAxisFontName
    xA.labels.fontSize = xAxisFontSize
    xA.labels.fillColor = xAxisFontColor
    xA.labels.angle = xAxisLabelAngle
    xA.labels.textAnchor = 'boxauto'
    xA.labels.boxAnchor = 'autox'
    xA.rangeRound = 'both'
    xA.style = style

    if seriesRelation != 'percent':
        yA.forceZero = 0  # 'near'
        yA.avoidBoundFrac = (0.1, 0.1)
    else:
        yA.valueMin = 0
        yA.valueMax = 100
        yA.labelTextPostFormat = '%s%%'
        yA.avoidBoundFrac = None

    chart.data = data
    if xAxisGridLines:
        xA.visibleGrid = 1
    else:
        xA.visibleGrid = 0
    if yAxisGridLines:
        yA.visibleGrid = 1
    else:
        yA.visibleGrid = 0

    yA.tickLeft = 3
    xA.tickUp = 3

    setMarkers(chart.lines, markerType, markerSize)
    return chart


def getLineChart(
    width=200,
    height=150,
    fontSize=6,
    data=None,
    chartColors=None,
    categoryNames=None,
    seriesNames=None,
    plotColor=backgroundGrey,
    seriesRelation='sidebyside',
    xAxisVisible=1,
    xAxisGridLines=0,
    xAxisFontName='Helvetica',
    xAxisFontSize=6,
    xAxisFontColor=black,
    xAxisLabelAngle=0,
    xAxisLabelTextFormat=None,
    xAxisLabelTextScale=None,
    yAxisVisible=1,
    yAxisGridLines=1,
    yAxisFontName='Helvetica',
    yAxisFontSize=6,
    yAxisFontColor=black,
    yAxisLabelAngle=0,
    yAxisLabelTextFormat=None,
    yAxisLabelTextScale=None,
    dataLabelsFormat=None,
    dataLabelsFontName='Helvetica',
    dataLabelsFontSize=6,
    dataLabelsFontColor=black,
    markerType=None,
    markerSize=0,
    LineChart=None,
    _3d=None,
):
    if LineChart is None:
        if _3d:
            from reportlab.graphics.charts.linecharts import (
                HorizontalLineChart3D as LineChart,
            )

            style = 'parallel_3d'
        else:
            from reportlab.graphics.charts.linecharts import (
                HorizontalLineChart as LineChart,
            )

            style = 'parallel'
    chart = LineChart()
    valueAxis = chart.valueAxis
    categoryAxis = chart.categoryAxis
    _setColors(chart.lines, chartColors, 'strokeColor')
    chart.fillColor = plotColor

    if isinstance(dataLabelsFormat, (list, tuple)):
        chart.lineLabelFormat = 'values'
        chart.lineLabelArray = dataLabelsFormat
    else:
        chart.lineLabelFormat = dataLabelsFormat
    chart.lineLabels.fontName = dataLabelsFontName
    chart.lineLabels.fontSize = dataLabelsFontSize
    chart.lineLabels.fillColor = dataLabelsFontColor

    categoryAxis.visible = xAxisVisible
    valueAxis.visible = yAxisVisible

    valueAxis.labelTextFormat = makeTickLabeller(yAxisLabelTextFormat)
    valueAxis.labelTextScale = yAxisLabelTextScale
    valueAxis.labels.fontName = yAxisFontName
    valueAxis.labels.fontSize = yAxisFontSize
    valueAxis.labels.fillColor = yAxisFontColor
    valueAxis.labels.angle = yAxisLabelAngle
    valueAxis.labels.textAnchor = 'boxauto'
    valueAxis.labels.boxAnchor = 'autoy'
    ####categoryAxis.labelTextFormat      = None
    if categoryNames:
        categoryAxis.categoryNames = categoryNames
    categoryAxis.labels.fontName = xAxisFontName
    categoryAxis.labels.fontSize = xAxisFontSize
    categoryAxis.labels.fillColor = xAxisFontColor
    categoryAxis.labels.angle = xAxisLabelAngle
    categoryAxis.labels.textAnchor = 'boxauto'
    categoryAxis.labels.boxAnchor = 'autox'

    if seriesRelation != 'percent':
        valueAxis.forceZero = 0  # 'near'
        valueAxis.avoidBoundFrac = (0.1, 0.1)
    else:
        valueAxis.valueMin = 0
        valueAxis.valueMax = 100
        valueAxis.labelTextPostFormat = '%s%%'
        valueAxis.avoidBoundFrac = None
    valueAxis.rangeRound = 'both'

    chart.data = data
    if xAxisGridLines:
        categoryAxis.visibleGrid = 1
    else:
        categoryAxis.visibleGrid = 0
    categoryAxis.style = style
    if yAxisGridLines:
        valueAxis.visibleGrid = 1
    else:
        valueAxis.visibleGrid = 0

    valueAxis.tickLeft = 3
    categoryAxis.tickUp = 3

    setMarkers(chart.lines, markerType, markerSize)
    return chart


def getLinePlotArea(
    width=200,
    height=150,
    fontSize=6,
    data=None,
    chartColors=None,
    categoryNames=None,
    seriesNames=None,
    plotColor=backgroundGrey,
    seriesRelation='sidebyside',
    xAxisVisible=1,
    xAxisGridLines=0,
    xAxisFontName='Helvetica',
    xAxisFontSize=6,
    xAxisFontColor=black,
    xAxisLabelAngle=0,
    xAxisLabelTextFormat=None,
    xAxisLabelTextScale=None,
    yAxisVisible=1,
    yAxisGridLines=1,
    yAxisFontName='Helvetica',
    yAxisFontSize=6,
    yAxisFontColor=black,
    yAxisLabelAngle=0,
    yAxisLabelTextFormat=None,
    yAxisLabelTextScale=None,
    dataLabelsFormat=None,
    dataLabelsFontName='Helvetica',
    dataLabelsFontSize=6,
    dataLabelsFontColor=black,
    markerType=None,
    markerSize=0,
):
    n = len(data[0])
    if seriesRelation in ['stacked', 'percent']:
        from reportlab.graphics.charts.lineplots import AreaLinePlot

        if seriesRelation == 'percent':
            data = normalizeData(data)
        odata, data = data, []
        for j in range(n):
            d = [j]
            for i in range(len(odata)):
                d.append(odata[i][j])
            data.append(tuple(d))
    else:
        AreaLinePlot = None
        data = matrixToMultiSeries(data)

    chart = getLinePlot(
        width=200,
        height=150,
        fontSize=fontSize,
        data=data,
        chartColors=chartColors,
        categoryNames=categoryNames,
        seriesNames=None,
        plotColor=plotColor,
        seriesRelation=seriesRelation,
        xAxisVisible=xAxisVisible,
        xAxisGridLines=xAxisGridLines,
        xAxisFontName=xAxisFontName,
        xAxisFontSize=xAxisFontSize,
        xAxisFontColor=xAxisFontColor,
        xAxisLabelAngle=xAxisLabelAngle,
        xAxisLabelTextFormat=xAxisLabelTextFormat,
        xAxisLabelTextScale=xAxisLabelTextScale,
        yAxisVisible=yAxisVisible,
        yAxisGridLines=yAxisGridLines,
        yAxisFontName=yAxisFontName,
        yAxisFontSize=yAxisFontSize,
        yAxisFontColor=yAxisFontColor,
        yAxisLabelAngle=yAxisLabelAngle,
        yAxisLabelTextFormat=yAxisLabelTextFormat,
        yAxisLabelTextScale=yAxisLabelTextScale,
        dataLabelsFormat=dataLabelsFormat,
        dataLabelsFontName=dataLabelsFontName,
        dataLabelsFontSize=dataLabelsFontSize,
        dataLabelsFontColor=dataLabelsFontColor,
        markerType=markerType,
        markerSize=markerSize,
        LinePlot=AreaLinePlot,
    )
    if AreaLinePlot is None:
        chart._inFill = 1
    chart.xValueAxis.labelTextFormat = (
        chart.xValueAxis._labelTextFormat
    ) = categoryNames
    chart.xValueAxis.valueMin = 0
    chart.xValueAxis.valueMax = n - 1
    chart.xValueAxis.valueStep = 1
    return chart


def getScatterPlot(
    width=200,
    height=150,
    fontSize=6,
    xData=None,
    yData=None,
    zData=None,
    chartColors=None,
    categoryNames=None,
    seriesNames=None,
    plotColor=backgroundGrey,
    seriesRelation='sidebyside',
    xAxisVisible=1,
    xAxisGridLines=0,
    xAxisFontName='Helvetica',
    xAxisFontSize=6,
    xAxisFontColor=black,
    xAxisLabelAngle=0,
    xAxisLabelTextFormat=None,
    xAxisLabelTextScale=None,
    yAxisVisible=1,
    yAxisGridLines=1,
    yAxisFontName='Helvetica',
    yAxisFontSize=6,
    yAxisFontColor=black,
    yAxisLabelAngle=0,
    yAxisLabelTextFormat=None,
    yAxisLabelTextScale=None,
    dataLabelsFormat=None,
    dataLabelsFontName='Helvetica',
    dataLabelsFontSize=6,
    dataLabelsFontColor=black,
    markerType=None,
    markerSize=0,
    reqDim=2,
):
    # raise Exception("format=%s" % dataLabelsFormat)
    from reportlab.graphics.charts.lineplots import ScatterPlot

    chart = ScatterPlot()
    _setColors(chart.lines, chartColors, 'strokeColor')
    chart.fillColor = plotColor
    xA = chart.xValueAxis
    yA = chart.yValueAxis

    if isinstance(dataLabelsFormat, (list, tuple)):
        chart.lineLabelFormat = 'values'
        chart.lineLabelArray = dataLabelsFormat
    else:
        chart.lineLabelFormat = dataLabelsFormat
    chart.lineLabels.fontName = dataLabelsFontName
    chart.lineLabels.fontSize = dataLabelsFontSize
    chart.lineLabels.fillColor = dataLabelsFontColor

    xA.visible = xAxisVisible
    yA.visible = yAxisVisible

    yA.labelTextFormat = makeTickLabeller(yAxisLabelTextFormat)
    yA.labelTextScale = yAxisLabelTextScale
    yA.labels.fontName = yAxisFontName
    yA.labels.fontSize = yAxisFontSize
    yA.labels.fillColor = yAxisFontColor
    yA.labels.angle = yAxisLabelAngle
    yA.labels.textAnchor = 'boxauto'
    yA.labels.boxAnchor = 'autoy'
    xA.labelTextFormat = makeTickLabeller(xAxisLabelTextFormat)
    xA.labelTextScale = xAxisLabelTextScale
    xA.labels.fontName = xAxisFontName
    xA.labels.fontSize = xAxisFontSize
    xA.labels.fillColor = xAxisFontColor
    xA.labels.angle = xAxisLabelAngle
    xA.labels.textAnchor = 'boxauto'
    xA.labels.boxAnchor = 'autox'

    yA.forceZero = 0  # 'near'
    yA.avoidBoundFrac = (0.1, 0.1)
    yA.rangeRound = 'both'

    chart.data = blockToMultiSeries(xData, yData, zData)
    if xAxisGridLines:
        xA.visibleGrid = 1
    else:
        xA.visibleGrid = 0
    if yAxisGridLines:
        yA.visibleGrid = 1
    else:
        yA.visibleGrid = 0

    yA.tickLeft = 3
    xA.tickUp = 3

    setMarkers(chart.lines, markerType, markerSize)

    return chart


def getScatterLinesPlot(
    width=200,
    height=150,
    fontSize=6,
    xData=None,
    yData=None,
    zData=None,
    chartColors=None,
    categoryNames=None,
    seriesNames=None,
    plotColor=backgroundGrey,
    seriesRelation='sidebyside',
    xAxisVisible=1,
    xAxisGridLines=0,
    xAxisFontName='Helvetica',
    xAxisFontSize=6,
    xAxisFontColor=black,
    xAxisLabelAngle=0,
    xAxisLabelTextFormat=None,
    xAxisLabelTextScale=None,
    yAxisVisible=1,
    yAxisGridLines=1,
    yAxisFontName='Helvetica',
    yAxisFontSize=6,
    yAxisFontColor=black,
    yAxisLabelAngle=0,
    yAxisLabelTextFormat=None,
    yAxisLabelTextScale=None,
    dataLabelsFormat=None,
    dataLabelsFontName='Helvetica',
    dataLabelsFontSize=6,
    dataLabelsFontColor=black,
    markerType=None,
    markerSize=0,
):
    chart = getScatterPlot(
        width=width,
        height=height,
        fontSize=fontSize,
        xData=xData,
        yData=yData,
        zData=zData,
        chartColors=chartColors,
        categoryNames=categoryNames,
        seriesNames=None,
        plotColor=plotColor,
        seriesRelation=seriesRelation,
        xAxisVisible=xAxisVisible,
        xAxisGridLines=xAxisGridLines,
        xAxisFontName=xAxisFontName,
        xAxisFontSize=xAxisFontSize,
        xAxisFontColor=xAxisFontColor,
        xAxisLabelAngle=xAxisLabelAngle,
        xAxisLabelTextFormat=xAxisLabelTextFormat,
        xAxisLabelTextScale=xAxisLabelTextScale,
        yAxisVisible=yAxisVisible,
        yAxisGridLines=yAxisGridLines,
        yAxisFontName=yAxisFontName,
        yAxisFontSize=yAxisFontSize,
        yAxisFontColor=yAxisFontColor,
        yAxisLabelAngle=yAxisLabelAngle,
        yAxisLabelTextFormat=yAxisLabelTextFormat,
        yAxisLabelTextScale=yAxisLabelTextScale,
        dataLabelsFormat=dataLabelsFormat,
        dataLabelsFontName=dataLabelsFontName,
        dataLabelsFontSize=dataLabelsFontSize,
        dataLabelsFontColor=dataLabelsFontColor,
        markerType=markerType,
        markerSize=markerSize,
    )
    chart.lines.strokeWidth = 1
    for i in range(0, 10):
        chart.lines[i].strokeColor = chartColors[i % len(chartColors)]
    chart.joinedLines = 1
    return chart


def getBubblePlot(
    width=200,
    height=150,
    fontSize=6,
    xData=None,
    yData=None,
    zData=None,
    chartColors=None,
    categoryNames=None,
    seriesNames=None,
    plotColor=backgroundGrey,
    seriesRelation='sidebyside',
    xAxisVisible=1,
    xAxisGridLines=0,
    xAxisFontName='Helvetica',
    xAxisFontSize=6,
    xAxisFontColor=black,
    xAxisLabelAngle=0,
    xAxisLabelTextFormat=None,
    xAxisLabelTextScale=None,
    yAxisVisible=1,
    yAxisGridLines=1,
    yAxisFontName='Helvetica',
    yAxisFontSize=6,
    yAxisFontColor=black,
    yAxisLabelAngle=0,
    yAxisLabelTextFormat=None,
    yAxisLabelTextScale=None,
    dataLabelsFormat=None,
    dataLabelsFontName='Helvetica',
    dataLabelsFontSize=6,
    dataLabelsFontColor=black,
    markerType=None,
    markerSize=8,
):
    if markerType == None:
        markerType = "Sequence"  # make sure there are markers

    chart = getScatterPlot(
        width=width,
        height=height,
        fontSize=fontSize,
        xData=xData,
        yData=yData,
        zData=zData,
        chartColors=chartColors,
        categoryNames=categoryNames,
        seriesNames=None,
        plotColor=plotColor,
        seriesRelation=seriesRelation,
        xAxisVisible=xAxisVisible,
        xAxisGridLines=xAxisGridLines,
        xAxisFontName=xAxisFontName,
        xAxisFontSize=xAxisFontSize,
        xAxisFontColor=xAxisFontColor,
        xAxisLabelAngle=xAxisLabelAngle,
        xAxisLabelTextFormat=xAxisLabelTextFormat,
        xAxisLabelTextScale=xAxisLabelTextScale,
        yAxisVisible=yAxisVisible,
        yAxisGridLines=yAxisGridLines,
        yAxisFontName=yAxisFontName,
        yAxisFontSize=yAxisFontSize,
        yAxisFontColor=yAxisFontColor,
        yAxisLabelAngle=yAxisLabelAngle,
        yAxisLabelTextFormat=yAxisLabelTextFormat,
        yAxisLabelTextScale=yAxisLabelTextScale,
        dataLabelsFormat=dataLabelsFormat,
        dataLabelsFontName=dataLabelsFontName,
        dataLabelsFontSize=dataLabelsFontSize,
        dataLabelsFontColor=dataLabelsFontColor,
        markerType=markerType,
        markerSize=markerSize,
    )
    chart._bubblePlot = 1
    return chart


def getPieChart(
    width=100,
    height=100,
    data=[1, 2, 3, 4],
    chartColors=None,
    dataLabelsFormat=None,
    dataLabelsFontName='Helvetica',
    dataLabelsFontSize=6,
    dataLabelsFontColor=black,
    popout=None,
    chartType='',
    checkLabelOverlap=0,
    orderMode='fixed',
    pointerLabelMode=None,
):
    if chartType.endswith('3d'):
        from reportlab.graphics.charts.piecharts import Pie3d as Pie
    else:
        from reportlab.graphics.charts.piecharts import Pie
    chart = Pie()
    _setColors(chart.slices, chartColors)
    chart.data = _simpleData(data)
    chart.labels = dataLabelsFormat
    chart.slices.fontName = dataLabelsFontName
    chart.slices.fontSize = dataLabelsFontSize
    chart.slices.fontColor = dataLabelsFontColor
    chart.startAngle = 90
    chart.simpleLabels = 0
    chart.slices.labelRadius = 1.05
    chart.slices.strokeWidth = 1
    chart.slices.popout = popout
    if not chartType.endswith('3d'):
        chart.pointerLabelMode = pointerLabelMode
    chart.orderMode = orderMode
    chart.checkLabelOverlap = checkLabelOverlap
    return chart


def getDoughnutChart(
    width=100,
    height=100,
    data=[[1, 2, 3, 4], [2, 4, 6, 10]],
    chartColors=None,
    startAngle=90,
    direction='clockwise',
    categoryNames=None,
    seriesNames=None,
    dataLabelsFormat=None,
    dataLabelsFontName='Helvetica',
    dataLabelsFontSize=6,
    dataLabelsFontColor=black,
):
    from reportlab.graphics.charts.doughnut import Doughnut

    chart = Doughnut()
    chart.data = data
    _setColors(chart.slices, chartColors)
    chart.labels = categoryNames
    if categoryNames is None:
        categoryNames = []
        for i in range(len(data[0])):
            categoryNames.append(str(i))
    chart.startAngle = 0
    return chart


def getRadarChart(
    width=100,
    height=100,
    data=[(125, 180, 200), (100, 150, 180)],
    chartColors=None,
    plotColor=backgroundGrey,
    categoryNames=None,
    seriesNames=None,
    dataLabelsFormat=None,
    dataLabelsFontName='Helvetica',
    dataLabelsFontSize=6,
    dataLabelsFontColor=black,
    spokeLabelFontName='Helvetica',
    spokeLabelFontSize=7,
    spokeLabelFontColor=black,
    markerType=None,
    markerSize=0,
):
    from reportlab.graphics.charts.spider import SpiderChart

    chart = SpiderChart()
    setMarkers(chart.strands, markerType, markerSize)
    for i in range(len(data)):
        chart.strands[i].fillColor = None
        chart.strands[i].strokeWidth = 1
        col = chart.strands[i].strokeColor = chartColors[i % len(chartColors)]
        try:
            chart.strands[i].symbol.fillColor = col
        except:
            pass
    chart.strandLabels.fontName = dataLabelsFontName
    chart.strandLabels.fontSize = dataLabelsFontSize
    chart.strandLabels.fillColor = dataLabelsFontColor
    if isinstance(dataLabelsFormat, list):
        chart.strandLabels.format = 'values'
        for i, r in enumerate(dataLabelsFormat):
            for j, v in enumerate(r):
                chart.strandLabels[i, j]._text = v
    else:
        chart.strandLabels.format = dataLabelsFormat
    chart.fillColor = plotColor
    chart.data = data
    if categoryNames is None:
        categoryNames = []
        for i in range(len(data[0])):
            categoryNames.append(str(i))
    chart.labels = categoryNames
    chart.spokes.labelRadius = 1.05
    chart.spokeLabels.fontName = spokeLabelFontName
    chart.spokeLabels.fontSize = spokeLabelFontSize
    chart.spokeLabels.fillColor = spokeLabelFontColor
    return chart


def getFilledRadarChart(
    width=100,
    height=100,
    data=[(125, 180, 200), (100, 150, 180)],
    chartColors=None,
    plotColor=backgroundGrey,
    categoryNames=None,
    seriesNames=None,
    dataLabelsFormat=None,
    dataLabelsFontName='Helvetica',
    dataLabelsFontSize=6,
    dataLabelsFontColor=black,
    spokeLabelFontName='Helvetica',
    spokeLabelFontSize=6,
    spokeLabelFontColor=black,
):
    chart = getRadarChart(
        width=width,
        height=height,
        data=data,
        chartColors=chartColors,
        plotColor=plotColor,
        categoryNames=categoryNames,
        seriesNames=None,
        dataLabelsFormat=dataLabelsFormat,
        dataLabelsFontName=dataLabelsFontName,
        dataLabelsFontSize=dataLabelsFontSize,
        dataLabelsFontColor=dataLabelsFontColor,
        spokeLabelFontName=spokeLabelFontName,
        spokeLabelFontSize=spokeLabelFontSize,
        spokeLabelFontColor=spokeLabelFontColor,
    )
    _setColors(chart.strands, chartColors)
    return chart


def getRadarMarkersChart(
    width=100,
    height=100,
    data=[(125, 180, 200), (100, 150, 180)],
    chartColors=None,
    plotColor=backgroundGrey,
    categoryNames=None,
    seriesNames=None,
    dataLabelsFormat=None,
    dataLabelsFontName='Helvetica',
    dataLabelsFontSize=6,
    dataLabelsFontColor=black,
    spokeLabelFontName='Helvetica',
    spokeLabelFontSize=6,
    spokeLabelFontColor=black,
    markerType=MARKER_FILLED_TRIANGLE,
    markerSize=8,
):
    chart = getRadarChart(
        width=width,
        height=height,
        data=data,
        chartColors=chartColors,
        plotColor=plotColor,
        categoryNames=categoryNames,
        seriesNames=None,
        dataLabelsFormat=dataLabelsFormat,
        dataLabelsFontName=dataLabelsFontName,
        dataLabelsFontSize=dataLabelsFontSize,
        dataLabelsFontColor=dataLabelsFontColor,
        spokeLabelFontName=spokeLabelFontName,
        spokeLabelFontSize=spokeLabelFontSize,
        spokeLabelFontColor=spokeLabelFontColor,
        markerType=markerType,
        markerSize=markerSize,
    )
    for i, c in enumerate(chartColors):
        chart.strands[i].fillColor = None
        chart.strands[i].strokeColor = c
        chart.strands[i].strokeWidth = 1
    return chart


def getLegend():
    # needs some smarts.  How to do this?
    from reportlab.graphics.charts.legends import Legend

    legend = Legend()
    legend.colorNamePairs = [
        (mainColours[0], 'Widgets'),
        (mainColours[1], 'Sprockets'),
    ]
    legend.fontName = 'Helvetica'
    legend.fontSize = 7
    legend.dxTextSpace = 5
    legend.dy = 5
    legend.dx = 5
    legend.deltay = 5
    legend.alignment = 'right'
    return legend


from reportlab.lib.validators import (
    isNumber,
    isNumberOrNone,
    isListOfStringsOrNone,
    isListOfNumbers,
    isListOfNumbersOrNone,
    isColorOrNone,
    OneOf,
    isBoolean,
    SequenceOf,
    isString,
    EitherOr,
    isColorOrNone,
    NoneOr,
    isListOfColors,
    isStringOrNone,
    isListOfShapes,
)

from reportlab.lib.attrmap import *


_isLabelAngle = NoneOr(EitherOr((isNumber, isString)))


class QuickChart(Widget):
    _attrMap = AttrMap(
        chartType=AttrMapValue(OneOf(*tuple(CHART_TYPES)), "chart type"),
        width=AttrMapValue(isNumber, "Width of the quickchart"),
        height=AttrMapValue(isNumber, "Height of the quickchart"),
        data=AttrMapValue(
            NoneOr(
                EitherOr(
                    (SequenceOf(isListOfNumbersOrNone, emptyOK=0), isString)
                )
            ),
            "Data for the quickchart",
        ),
        textData=AttrMapValue(
            isStringOrNone, "Textual data for use in place of data in " "labels"
        ),
        categoryNames=AttrMapValue(None, ""),
        seriesNames=AttrMapValue(None, ""),
        seriesRelation=AttrMapValue(None, ""),
        chartColors=AttrMapValue(NoneOr(isListOfColors), ""),
        titleText=AttrMapValue(None, ""),
        titleFontName=AttrMapValue(None, ""),
        titleFontSize=AttrMapValue(None, ""),
        titleFontColor=AttrMapValue(isColorOrNone, ""),
        xTitleText=AttrMapValue(None, ""),
        xTitleFontName=AttrMapValue(None, ""),
        xTitleFontSize=AttrMapValue(None, ""),
        xTitleFontColor=AttrMapValue(isColorOrNone, ""),
        yTitleText=AttrMapValue(None, ""),
        yTitleFontName=AttrMapValue(None, ""),
        yTitleFontSize=AttrMapValue(None, ""),
        yTitleFontColor=AttrMapValue(isColorOrNone, ""),
        xAxisVisible=AttrMapValue(isBoolean, ""),
        xAxisGridLines=AttrMapValue(isBoolean, ""),
        xAxisFontName=AttrMapValue(None, ""),
        xAxisFontSize=AttrMapValue(None, ""),
        xAxisFontColor=AttrMapValue(isColorOrNone, ""),
        xAxisLabelAngle=AttrMapValue(_isLabelAngle, ""),
        xAxisLabelTextFormat=AttrMapValue(isStringOrNone, ""),
        xAxisLabelTextScale=AttrMapValue(isNumberOrNone, ""),
        yAxisVisible=AttrMapValue(isBoolean, ""),
        yAxisGridLines=AttrMapValue(isBoolean, ""),
        yAxisFontName=AttrMapValue(None, ""),
        yAxisFontSize=AttrMapValue(None, ""),
        yAxisFontColor=AttrMapValue(isColorOrNone, ""),
        yAxisLabelAngle=AttrMapValue(_isLabelAngle, ""),
        yAxisLabelTextFormat=AttrMapValue(isStringOrNone, ""),
        yAxisLabelTextScale=AttrMapValue(isNumberOrNone, ""),
        dataLabelsType=AttrMapValue(None, ""),
        dataLabelsFontName=AttrMapValue(None, ""),
        dataLabelsFontSize=AttrMapValue(None, ""),
        dataLabelsFontColor=AttrMapValue(isColorOrNone, ""),
        dataLabelsAlignment=AttrMapValue(
            NoneOr(OneOf(('top', 'bottom', 'center'))), 'DataLabels Alignment'
        ),
        markerType=AttrMapValue(None, ""),
        markerSize=AttrMapValue(None, ""),
        legendPos=AttrMapValue(None, ""),
        legendText=AttrMapValue(None, ""),
        legendFontName=AttrMapValue(None, ""),
        legendFontSize=AttrMapValue(None, ""),
        legendFontColor=AttrMapValue(isColorOrNone, ""),
        legendVariColumn=AttrMapValue(isBoolean, ""),
        legendXPad=AttrMapValue(isNumberOrNone, ""),
        legendYPad=AttrMapValue(isNumberOrNone, ""),
        legendMaxHFrac=AttrMapValue(isNumberOrNone, ""),
        legendMaxWFrac=AttrMapValue(isNumberOrNone, ""),
        bgColor=AttrMapValue(None, ""),
        bgStrokeColor=AttrMapValue(None, ""),
        plotColor=AttrMapValue(None, ""),
        chartFillColors=AttrMapValue(None, ""),
        chartStrokeColors=AttrMapValue(None, ""),
        chartStrokeWidth=AttrMapValue(None, ""),
        chartSeparation=AttrMapValue(None, ""),
        showBoundaries=AttrMapValue(isBoolean, ""),
        drawingClass=AttrMapValue(None, 'The drawing class to use'),
        x=AttrMapValue(isNumber, desc='x offset.'),
        y=AttrMapValue(isNumber, desc='y offset.'),
        pad=AttrMapValue(isNumberOrNone, desc='pad value or None'),
        padMax=AttrMapValue(isNumberOrNone, desc='maximum pad allowed'),
        padMin=AttrMapValue(isNumberOrNone, desc='minimum pad allowed'),
        padFrac=AttrMapValue(
            isNumberOrNone, desc='pad specified as a fraction of width'
        ),
        checkLabelOverlap=AttrMapValue(
            isBoolean, desc='true check pie label overlap'
        ),
        orderMode=AttrMapValue(
            isString,
            desc='pie slice order mode \'fixed\'(default) ' 'or \'alternate\'',
        ),
        pointerLabelMode=AttrMapValue(
            isStringOrNone,
            desc='None don\'t do pointers or '
            '\'LeftRight\' or \'leftAndRight\'',
        ),
    )

    def __init__(self):
        self.chartType = CHART_TYPE_COLUMN
        self.width = 400
        self.height = 270
        self.data = [[100, 120, 140, 160], [110, 130, 150, 180]]
        self.textData = None
        self.categoryNames = None
        self.seriesNames = None
        self.seriesRelation = None
        self.chartColors = None
        self.titleText = ''
        self.titleFontName = 'Helvetica'
        self.titleFontSize = None
        self.titleFontColor = black
        self.xTitleText = ''
        self.xTitleFontName = 'Helvetica'
        self.xTitleFontSize = None
        self.xTitleFontColor = black
        self.yTitleText = ''
        self.yTitleFontName = 'Helvetica'
        self.yTitleFontSize = None
        self.yTitleFontColor = black
        self.xAxisVisible = 1
        self.xAxisGridLines = 0
        self.xAxisFontName = 'Helvetica'
        self.xAxisFontSize = None
        self.xAxisFontColor = black
        self.xAxisLabelAngle = None
        self.xAxisLabelTextFormat = None
        self.xAxisLabelTextScale = None
        self.yAxisVisible = 1
        self.yAxisGridLines = 0
        self.yAxisFontName = 'Helvetica'
        self.yAxisFontSize = None
        self.yAxisFontColor = black
        self.yAxisLabelAngle = None
        self.yAxisLabelTextFormat = None
        self.yAxisLabelTextScale = None
        self.dataLabelsType = None
        self.dataLabelsFontName = 'Helvetica'
        self.dataLabelsFontSize = None
        self.dataLabelsFontColor = black
        self.dataLabelsAlignment = None
        self.markerType = None
        self.markerSize = 6
        self.legendPos = 'right'
        self.legendText = None
        self.legendFontName = 'Helvetica'
        self.legendFontSize = None
        self.legendFontColor = None
        self.legendVariColumn = 1
        self.legendXPad = None
        self.legendYPad = None
        self.legendMaxHFrac = None
        self.legendMaxWFrac = None
        self.bgColor = None
        self.bgStrokeColor = None
        self.plotColor = backgroundGrey
        self.chartFillColors = None
        self.chartStrokeColors = None
        self.chartStrokeWidth = None
        self.chartSeparation = 0
        self.showBoundaries = 0
        self.drawingClass = Group
        self.pad = None
        self.padMax = None
        self.padMin = None
        self.padFrac = 0.05
        self.checkLabelOverlap = 0
        self.orderMode = 'fixed'
        self.pointerLabelMode = None
        self.x = 0
        self.y = 0

    def draw(self):
        g = quickChart(
            chartType=self.chartType,
            width=self.width,
            height=self.height,
            data=self.data,
            textData=self.textData,
            categoryNames=self.categoryNames,
            seriesNames=self.seriesNames,
            seriesRelation=self.seriesRelation,
            chartColors=self.chartColors,
            titleText=self.titleText,
            titleFontName=self.titleFontName,
            titleFontSize=self.titleFontSize,
            titleFontColor=self.titleFontColor,
            xTitleText=self.xTitleText,
            xTitleFontName=self.xTitleFontName,
            xTitleFontSize=self.xTitleFontSize,
            xTitleFontColor=self.xTitleFontColor,
            yTitleText=self.yTitleText,
            yTitleFontName=self.yTitleFontName,
            yTitleFontSize=self.yTitleFontSize,
            yTitleFontColor=self.yTitleFontColor,
            xAxisVisible=self.xAxisVisible,
            xAxisGridLines=self.xAxisGridLines,
            xAxisFontName=self.xAxisFontName,
            xAxisFontSize=self.xAxisFontSize,
            xAxisFontColor=self.xAxisFontColor,
            xAxisLabelAngle=self.xAxisLabelAngle,
            xAxisLabelTextFormat=self.xAxisLabelTextFormat,
            xAxisLabelTextScale=self.xAxisLabelTextScale,
            yAxisVisible=self.yAxisVisible,
            yAxisGridLines=self.yAxisGridLines,
            yAxisFontName=self.yAxisFontName,
            yAxisFontSize=self.yAxisFontSize,
            yAxisFontColor=self.yAxisFontColor,
            yAxisLabelAngle=self.yAxisLabelAngle,
            yAxisLabelTextFormat=self.yAxisLabelTextFormat,
            yAxisLabelTextScale=self.yAxisLabelTextScale,
            dataLabelsType=self.dataLabelsType,
            dataLabelsFontName=self.dataLabelsFontName,
            dataLabelsFontSize=self.dataLabelsFontSize,
            dataLabelsFontColor=self.dataLabelsFontColor,
            dataLabelsAlignment=self.dataLabelsAlignment,
            markerType=self.markerType,
            markerSize=self.markerSize,
            legendPos=self.legendPos,
            legendText=self.legendText,
            legendFontName=self.legendFontName,
            legendFontSize=self.legendFontSize,
            legendFontColor=self.legendFontColor,
            legendVariColumn=self.legendVariColumn,
            legendXPad=self.legendXPad,
            legendYPad=self.legendYPad,
            legendMaxHFrac=self.legendMaxHFrac,
            legendMaxWFrac=self.legendMaxWFrac,
            bgColor=self.bgColor,
            bgStrokeColor=self.bgStrokeColor,
            plotColor=self.plotColor,
            chartFillColors=self.chartFillColors,
            chartStrokeColors=self.chartStrokeColors,
            chartStrokeWidth=self.chartStrokeWidth,
            chartSeparation=self.chartSeparation,
            showBoundaries=self.showBoundaries,
            drawingClass=self.drawingClass,
            pad=self.pad,
            padMax=self.padMax,
            padMin=self.padMin,
            padFrac=self.padFrac,
            checkLabelOverlap=self.checkLabelOverlap,
            orderMode=self.orderMode,
            pointerLabelMode=self.pointerLabelMode,
        )
        g.transform = [1, 0, 0, 1, self.x, self.y]
        g.__dict__['width'] = self.width
        g.__dict__['height'] = self.height
        return g


class QuickChartDrawing(Drawing):
    def __init__(self, width=400, height=200, *nodes, **keywords):
        Drawing.__init__(*(self, width, height) + nodes, **keywords)

        qc = QuickChart()
        qc.width = self.width
        qc.height = self.height

        self._add(self, qc, name='qc', validate=None, desc=None)


def testCommandLine(args):
    usage = """quickchart.py - high level interface for easy charts.
    usage 1: runs all tests
      quickchart.py -test

    usage 2:
      quickchart.py chartType width height [option1=value1] [option2=value2] ..
    Options are the arguments to the quickchart function.  The resulting
    chart will be stored in quickchart_output.pdf.

    """
    kwargs = {}
    positionals = []
    for arg in args:
        stuff = arg.split('=')
        if len(stuff) == 2:
            key, value = stuff
            kwargs[key] = value
            args.remove(arg)
        else:
            positionals.append(arg)
    if len(positionals) != 3:
        print(usage)
        return
    chartType = args[0]
    width = float(args[1])
    height = float(args[2])

    data = [[1, 2, 3, 4], [1, 4, 9, 16]]
    print('type=%s, width=%0.2f, height=%0.2f' % (chartType, width, height))

    d = quickChart(chartType, width, height, data, **kwargs)
    open('quickchart_custom.pdf', 'wb').write(d.asString('pdf'))
    print('saved quickchart_custom.pdf')


def testAll(verbose=True, dir=None):
    from reportlab.lib.utils import annotateException

    data = [[1, 2, 3, 4], [1, 4, 9, 16]]
    for chartType in CHART_TYPES:
        try:
            d = quickChart(chartType, 300, 200, data)
        except:
            annotateException(
                '\n!!!!! quickChart(chartType=%r... failed\n' % chartType
            )
    try:
        getLegend()
    except:
        annotateException('\n!!!!! getLegend failed\n')
    if verbose:
        print('created %d chart types OK' % len(CHART_TYPES))

    try:
        d = getTestDrawing()
    except:
        annotateException('\n!!!!! d = getTestDrawing() failed\n')
    import os

    fmt = 'quickchart_test.%s'
    if dir:
        fmt = os.path.join(dir, fmt)
        if not os.path.isdir(dir):
            os.makedirs(dir)
    for format in ['pdf', 'eps', 'gif', 'png', 'pict']:
        fn = fmt % format
        try:
            stuff = d.asString(format)
            if verbose:
                print('d.asString(%r) --> %s' % (format, type(stuff)))
            with open(fn, 'wb') as f:
                f.write(asBytes(stuff))
        except:
            annotateException(
                '\n!!!!! d.asString(%r) failed %s\n' % (format, type(stuff))
            )
        if verbose:
            print('saved %s' % fn)


if __name__ == '__main__':
    if '-test' in sys.argv:
        testAll()
    else:
        testCommandLine(sys.argv[1:])
