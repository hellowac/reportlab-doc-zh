"An Area Chart"
# Autogenerated by ReportLab guiedit do not edit
from rlextra.graphics.quickchart import QuickChartDrawing, QuickChart
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.lib.corp import white, black


class QuickAreaChart01(_DrawingEditorMixin, QuickChartDrawing):
    def __init__(self, width=400, height=200, *args, **kw):
        titleFontName = kw.pop('titleFontName', 'Helvetica')

        QuickChartDrawing.__init__(self, width, height, *args, **kw)
        self.qc.chartType = 'area'
        self.qc.titleText = '面积图'  # 'Quick Area Chart'
        self.qc.titleFontName = titleFontName
        self.qc.categoryNames = '2002', '2003', '2004', '2005'
        self.qc.seriesNames = 'England', 'France'


class Drawing3DBarChart(_DrawingEditorMixin, Drawing):
    """
    3d Bar Chart - with 2 series & gridlines
    """

    def __init__(self, width=400, height=200, *args, **kw):

        titleFontName = kw.pop('titleFontName', 'Helvetica')

        Drawing.__init__(self, width, height, *args, **kw)
        self._add(self, QuickChart(), name='chart', validate=None, desc=None)
        self.chart.height = 200
        self.chart.seriesNames = 'profit', 'sales'
        self.chart.yAxisFontSize = 9
        self.chart.yAxisGridLines = 1
        self.chart.yAxisLabelTextFormat = None
        self.chart.chartSeparation = 1
        self.chart.titleText = '3D 条形图'  # '3d Bar Chart'
        self.chart.titleFontName = titleFontName
        self.chart.yAxisVisible = 1
        self.chart.yTitleFontSize = 9
        self.chart.yAxisLabelTextScale = None
        self.chart.yTitleText = None
        self.chart.pointerLabelMode = 'LeftRight'
        self.chart.chartType = 'bar3d'
        self.chart.categoryNames = ('2009', '2010', '2011', '2012')
        self.chart.xTitleText = 'Euro (thousands)'
        self.chart.xAxisGridLines = 1
        self.chart.x = 0
        self.chart.showBoundaries = 0
        self.chart.seriesRelation = 1


class QuickBarChart01(_DrawingEditorMixin, QuickChartDrawing):
    def __init__(self, width=400, height=200, *args, **kw):
        titleFontName = kw.pop('titleFontName', 'Helvetica')

        QuickChartDrawing.__init__(self, width, height, *args, **kw)
        self.qc.categoryNames = ('2000', '2001', '2002', '2003')
        self.qc.titleText = '背景柱状图'
        self.qc.seriesNames = 'US', 'UK'
        self.qc.titleFontName = titleFontName


class QuickBarChart02(_DrawingEditorMixin, Drawing):
    """
    Column Chart - with 3 series on a white background
    """

    def __init__(self, width=400, height=200, *args, **kw):
        titleFontName = kw.pop('titleFontName', 'Helvetica')

        Drawing.__init__(self, width, height, *args, **kw)
        self._add(self, QuickChart(), name='chart', validate=None, desc=None)
        self.chart.height = 200
        self.chart.seriesNames = 'a', 'b', 'c'
        self.chart.seriesRelation = None  #
        self.chart.dataLabelsFontSize = 12
        self.chart.chartSeparation = 1
        self.chart.data = [[100, 120, 140], [110, 130, 150], [200, 100, 100]]
        self.chart.chartType = 'column'
        self.chart.titleText = '柱状图'  # 'Column Chart'
        self.chart.xTitleText = ''
        self.chart.categoryNames = ('2009', '2010', '2012')
        self.chart.pointerLabelMode = 'leftAndRight'
        self.chart.bgColor = 'white'
        self.chart.plotColor = white
        self.chart.titleFontColor = black
        self.chart.titleFontName = titleFontName


class Quick3DBarChart01(_DrawingEditorMixin, Drawing):
    """
    3d Column Chart - with 3 series with grid lines
    """

    def __init__(self, width=400, height=200, *args, **kw):
        titleFontName = kw.pop('titleFontName', 'Helvetica')
        Drawing.__init__(self, width, height, *args, **kw)
        self._add(self, QuickChart(), name='chart', validate=None, desc=None)
        self.chart.height = 200
        self.chart.seriesNames = 'a', 'b', 'c'
        self.chart.seriesRelation = None  #
        self.chart.dataLabelsFontSize = 12
        self.chart.chartSeparation = 1
        self.chart.data = [[100, 120, 140], [110, 130, 150], [200, 100, 100]]
        self.chart.titleText = '3D背景柱状图'  # 'Column Chart'
        self.chart.xTitleText = ''
        self.chart.categoryNames = ('2009', '2010', '2012')
        self.chart.chartType = 'column3d'
        self.transform = (1, 0, 0, 1, 0, 0)
        self.chart.xAxisGridLines = 1
        self.chart.yAxisGridLines = 1
        self.chart.titleFontName = titleFontName


class QuickDohnotChart01(_DrawingEditorMixin, QuickChartDrawing):
    def __init__(self, width=400, height=200, *args, **kw):
        titleFontName = kw.pop('titleFontName', 'Helvetica')

        QuickChartDrawing.__init__(self, width, height, *args, **kw)
        self.qc.categoryNames = ['2000', '2001', '2002', '2003']
        self.qc.chartType = 'doughnut'
        self.qc.checkLabelOverlap = 1
        self.qc.data = [[100, 120, 140, 160], [40, 70, 180, 200]]
        self.qc.titleText = '嵌套饼图'  # 'A Quick Chart'
        self.qc.titleFontName = titleFontName


class QuickExplodedPie01(_DrawingEditorMixin, QuickChartDrawing):
    def __init__(self, width=400, height=200, *args, **kw):
        titleFontName = kw.pop('titleFontName', 'Helvetica')
        QuickChartDrawing.__init__(self, width, height, *args, **kw)
        self.qc.titleText = '分裂饼图'
        self.qc.seriesNames = 'UK', 'US'
        self.qc.chartType = 'exploded_pie'
        self.qc.categoryNames = '2003', '2004', '2005', '2006'
        self.qc.titleFontName = titleFontName


class Quick3DExplodedPie01(_DrawingEditorMixin, QuickChartDrawing):
    def __init__(self, width=400, height=200, *args, **kw):
        titleFontName = kw.pop('titleFontName', 'Helvetica')
        QuickChartDrawing.__init__(self, width, height, *args, **kw)
        self.qc.seriesNames = 'UK', 'US'
        self.qc.categoryNames = '2003', '2004', '2005', '2006'
        self.qc.chartType = 'exploded_pie3d'
        self.qc.titleText = '3D 分裂饼图'
        self.qc.titleFontName = titleFontName
