"Area chart with lines"
from reportlab.lib.colors import black, PCMYKColor
from reportlab.graphics.charts.lineplots import LinePlot, AreaLinePlot
from reportlab.graphics.charts.legends import LineLegend, Legend
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin, Rect, String
from reportlab.lib.formatters import DecimalFormatter
from reportlab.graphics.charts.axes import (
    XValueAxis,
    YValueAxis,
    AdjYValueAxis,
    NormalDateXValueAxis,
)
from reportlab.lib.normalDate import NormalDate
from reportlab.graphics.charts.lineplots import AreaLinePlot, LinePlot
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin, Line
from reportlab.lib.colors import PCMYKColor, black, white
from reportlab.lib.formatters import DecimalFormatter
from reportlab.graphics.charts.textlabels import Label


class AreaWithLinesChart(_DrawingEditorMixin, Drawing):
    """
    Chart Features
    --------------

    This is an Area Chart that contains a Legend Widget to compare company performance
    againt a market index.

    - **legend.boxAncho=sw:** The Legend is anchored south, so adding more swatch boxes means the legend will
    grow up and no need to re-adjust the chart.

    - **chart.lines[0].inFills=True:** Makes it an area rather than a line

    Two rectangles are added to color in the bottom and left sides of the chart:

    - self._add(self,Rect(0,0,self.width,self.height,fillColor=self._colors[5],strokeColor=None),name='bgrect0',validate=None,desc=None)
    - self._add(self,Rect(0,0,self.width,self.height,fillColor=self._colors[5],strokeColor=None),name='bgrect1',validate=None,desc=None)
    - self.bgrect0.width = self.chart.x
    - self.bgrect0.height = self.height
    - self.bgrect1.x = self.chart.x
    - self.bgrect1.width = self.chart.width
    - self.bgrect1.height = self.chart.y

    - The X Axis is a date axis and can choose a suitable range of dates depending on your
    preferences, there are dozens of attributes that allow all possibilities
    if you navigate to chart.xValueAxis you see properties such as:

        - forceDatesEachYear
        - forceEndDate
        - forceFirstDate
        - forceZero
        - niceMonth

    - **chart.xValueAxis.labels.angle=45:** Angles the X Axis labels 45 degrees
    """

    def __init__(self, width=648, height=306, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        self._colors = (
            PCMYKColor(66, 13, 0, 22, alpha=40),
            PCMYKColor(0, 100, 100, 40),
            PCMYKColor(100, 0, 90, 50),
            PCMYKColor(0, 0, 0, 40),
            PCMYKColor(10, 0, 100, 11),
            PCMYKColor(15, 0, 0, 0),
            PCMYKColor(0, 0, 0, 50),
        )
        legend_width = 120
        self._add(
            self,
            Rect(
                0,
                0,
                self.width,
                self.height,
                fillColor=self._colors[5],
                strokeColor=None,
            ),
            name='bgrect0',
            validate=None,
            desc=None,
        )
        self._add(
            self,
            Rect(
                0,
                0,
                self.width,
                self.height,
                fillColor=self._colors[5],
                strokeColor=None,
            ),
            name='bgrect1',
            validate=None,
            desc=None,
        )
        # chart
        self._add(self, LinePlot(), name='chart', validate=None, desc=None)
        self.chart.x = 70
        self.chart.y = 36
        self.chart.width = width - self.chart.x - legend_width
        self.chart.height = height - self.chart.y
        self.chart.lines[0].inFill = True
        self.chart.lines[0].strokeColor = self._colors[0]
        self.chart.lines[1].strokeColor = self._colors[1]
        self.chart.lines[2].strokeColor = self._colors[2]
        # drawing background
        self.bgrect0.width = self.chart.x
        self.bgrect0.height = self.height
        # chart background
        self.bgrect1.x = self.chart.x
        self.bgrect1.width = self.chart.width
        self.bgrect1.height = self.chart.y
        # x axis
        self.chart.xValueAxis = (
            NormalDateXValueAxis()
        )  # we change the axis type here
        self.chart.xValueAxis.bottomAxisLabelSlack = 0
        self.chart.xValueAxis.dailyFreq = 0
        self.chart.xValueAxis.forceEndDate = True
        self.chart.xValueAxis.forceFirstDate = True
        self.chart.xValueAxis.gridEnd = 0
        self.chart.xValueAxis.gridStart = 0
        self.chart.xValueAxis.gridStrokeWidth = 0.25
        self.chart.xValueAxis.joinAxisMode = 'bottom'
        self.chart.xValueAxis.labels.angle = 45
        self.chart.xValueAxis.labels.boxAnchor = 'e'
        self.chart.xValueAxis.labels.dx = -2
        self.chart.xValueAxis.labels.dy = -10
        self.chart.xValueAxis.labels.fontName = 'Times-Roman'
        self.chart.xValueAxis.labels.fontSize = 10
        self.chart.xValueAxis.maximumTicks = 7
        self.chart.xValueAxis.minimumTickSpacing = 20  # in points
        self.chart.xValueAxis.strokeColor = self._colors[6]
        self.chart.xValueAxis.strokeWidth = 0.5
        self.chart.xValueAxis.tickDown = 10
        self.chart.xValueAxis.valueSteps = None
        self.chart.xValueAxis.visibleGrid = False
        self.chart.xValueAxis.xLabelFormat = '{mm}/{yyyy}'
        # y axis
        self.chart.yValueAxis.avoidBoundFrac = 0.1
        self.chart.yValueAxis.drawGridLast = True
        self.chart.yValueAxis.forceZero = True
        self.chart.yValueAxis.gridStrokeColor = self._colors[6]
        self.chart.yValueAxis.gridStrokeWidth = 0.5
        self.chart.yValueAxis.labels.dy = 0
        self.chart.yValueAxis.labels.fontName = 'Times-Roman'
        self.chart.yValueAxis.labels.fontSize = 10
        self.chart.yValueAxis.labels.rightPadding = 10
        self.chart.yValueAxis.labelTextFormat = DecimalFormatter(
            places=0, thousandSep=',', decimalSep='.', prefix='$'
        )
        self.chart.yValueAxis.maximumTicks = 4
        self.chart.yValueAxis.rangeRound = 'floor'
        self.chart.yValueAxis.strokeColor = self._colors[6]
        self.chart.yValueAxis.strokeWidth = 0.5
        self.chart.yValueAxis.tickLeft = 5
        self.chart.yValueAxis.tickRight = 0
        self.chart.yValueAxis.valueMax = None
        self.chart.yValueAxis.valueMin = None
        self.chart.yValueAxis.valueStep = None
        self.chart.yValueAxis.visibleAxis = False
        self.chart.yValueAxis.visibleGrid = True
        self.chart.yValueAxis.visibleTicks = True
        # legend
        self._add(self, Legend(), name='legend', validate=None, desc=None)
        self.legend.alignment = 'right'
        self.legend.boxAnchor = 'sw'
        self.legend.columnMaximum = 10
        self.legend.deltax = 50
        self.legend.deltay = 0
        self.legend.dx = 8
        self.legend.dxTextSpace = 5
        self.legend.dy = 8
        self.legend.fontName = 'Times-Roman'
        self.legend.fontSize = 12
        self.legend.strokeColor = None
        self.legend.strokeWidth = 0
        self.legend.x = self.chart.x + self.chart.width + 25
        self.legend.yGap = 0
        self.legend.y = self.chart.y
        # sample data
        self.chart.data = [
            [
                (19960901, 100000.0),
                (19961201, 109034.00000000001),
                (19970301, 110105.00000000001),
                (19970601, 127487.0),
                (19970901, 134702.0),
                (19971201, 136920.0),
                (19980301, 153788.0),
                (19980601, 158997.0),
                (19980901, 141245.0),
                (19981201, 171859.0),
                (19990301, 179215.0),
                (19990601, 193963.0),
                (19990901, 181679.0),
                (19991201, 202828.0),
                (20000301, 216832.0),
                (20000601, 218377.0),
                (20000901, 222553.0),
                (20001201, 220915.00000000003),
                (20010301, 204568.0),
                (20010601, 212621.0),
                (20010901, 185524.0),
                (20011201, 202977.0),
                (20020301, 204425.0),
                (20020601, 176716.0),
                (20020901, 143573.0),
                (20021201, 158079.0),
                (20030301, 153953.0),
                (20030601, 181898.0),
                (20030901, 186917.0),
                (20031201, 210109.0),
                (20040301, 214340.99999999997),
                (20040601, 217241.00000000003),
                (20040901, 207773.0),
                (20041201, 226420.99999999997),
                (20050301, 219802.0),
                (20050601, 224784.0),
                (20050901, 234346.0),
                (20051201, 238378.99999999997),
                (20060301, 244329.99999999997),
                (20060601, 237279.00000000003),
                (20060901, 250893.0),
            ],
            [
                (19960901, 100000.0),
                (19961201, 107756.00000000001),
                (19970301, 109009.0),
                (19970601, 127193.0),
                (19970901, 137804.0),
                (19971201, 140379.0),
                (19980301, 159140.0),
                (19980601, 163192.0),
                (19980901, 145219.0),
                (19981201, 177235.0),
                (19990301, 185424.0),
                (19990601, 199092.0),
                (19990901, 186227.0),
                (19991201, 217680.0),
                (20000301, 225952.99999999997),
                (20000601, 218523.99999999997),
                (20000901, 222131.0),
                (20001201, 199163.0),
                (20010301, 171684.0),
                (20010601, 182742.0),
                (20010901, 150187.0),
                (20011201, 167530.0),
                (20020301, 166471.0),
                (20020601, 141964.0),
                (20020901, 116748.99999999999),
                (20021201, 126703.00000000001),
                (20030301, 122520.0),
                (20030601, 142817.0),
                (20030901, 147424.0),
                (20031201, 165744.0),
                (20040301, 169164.0),
                (20040601, 171480.0),
                (20040901, 167844.0),
                (20041201, 183880.0),
                (20050301, 177886.0),
                (20050601, 182389.0),
                (20050901, 189194.0),
                (20051201, 194098.0),
                (20060301, 202789.00000000003),
                (20060601, 199425.0),
                (20060901, 208632.99999999997),
            ],
            [
                (19960901, 100000.0),
                (19961201, 108335.0),
                (19970301, 111239.0),
                (19970601, 130658.99999999999),
                (19970901, 140444.0),
                (19971201, 144476.0),
                (19980301, 164629.0),
                (19980601, 170065.0),
                (19980901, 153148.0),
                (19981201, 185764.0),
                (19990301, 195021.0),
                (19990601, 208768.00000000003),
                (19990901, 195733.0),
                (19991201, 224858.0),
                (20000301, 230015.0),
                (20000601, 223903.0),
                (20000901, 221735.00000000003),
                (20001201, 204384.0),
                (20010301, 180154.0),
                (20010601, 190697.0),
                (20010901, 162707.0),
                (20011201, 180094.0),
                (20020301, 180588.0),
                (20020601, 156393.0),
                (20020901, 129375.0),
                (20021201, 140290.0),
                (20030301, 135871.0),
                (20030601, 156793.0),
                (20030901, 160942.0),
                (20031201, 180538.0),
                (20040301, 183594.0),
                (20040601, 186752.0),
                (20040901, 183261.0),
                (20041201, 200178.0),
                (20050301, 195875.0),
                (20050601, 198549.0),
                (20050901, 205708.0),
                (20051201, 210001.00000000003),
                (20060301, 218838.0),
                (20060601, 215685.0),
                (20060901, 227904.99999999997),
            ],
        ]
        self._seriesNames = 'Index', 'Europe Market', 'Asia Market'
        self.bgrect0.fillColor = PCMYKColor(10, 10, 10, 10, alpha=100)
        self.bgrect1.fillColor = PCMYKColor(10, 10, 10, 10, alpha=100)
        self.chart.lines.strokeWidth = 2.5

    def getContents(self):
        self.legend.colorNamePairs = list(zip(self._colors, self._seriesNames))
        for i in range(len(self._seriesNames)):
            self.chart.lines[i].strokeColor = self._colors[i]
        return Drawing.getContents(self)


class DynamicLabel(Label):
    def __init__(self, text, ux, uy, **kw):
        Label.__init__(self, **kw)
        self._text = text
        self._ux = ux
        self._uy = uy

    def asAnnotation(self, chart, xscale, yscale):
        self.x = xscale(self._ux)  # - 3 # moves it off the edge
        self.y = yscale(self._uy)  # + 7 # lift it up the chart
        return None


def addConditionalSubTicks(chart):
    """
    if the dates of the axis jumps one year then this will add subticks between
    """
    chart.xValueAxis.configure([chart.data])
    if (
        int(str(chart.xValueAxis._tickValues[-1])[:4])
        - int(str(chart.xValueAxis._tickValues[-2])[:4])
        > 1
    ):
        chart.xValueAxis.subTickNum = 1
        chart.xValueAxis.visibleSubTicks = True
        chart.xValueAxis.subTickLo = chart.xValueAxis.tickDown


class AreaWithDynamicLabelChart(_DrawingEditorMixin, Drawing):
    """
    Chart Features
    --------------

    This is an Area Chart that demonstrates a dynamic labels that holds the ending value of the
    charting period.

    - The Chart vertical axis (the value axis) can show different formatting for last label

    - A label that can fit itself automatically by looking for an empty space to fit itself.
    The label text can be of any choice and has access to the data of the chart so can display
    them in any given format. ReportLab can also show different types of labels such as highest
    value, lowest value, begining value, etc ...

    **NOTE**: placing the label is done with python code so is not shown to the attributes list
    in the side pane.

    - The X Axis can show extra tick when the distance between teh first and the second ticks are
    longer than the distances between other ticks.
    see chart.xValueAxis.specialTickClear=True

    - The labels formats can be achieved with different ways, we support Microsoft Excel Formatting
    Notation such as chart.xValueAxis.xLabelFormat={m}/{yy}  and we also support any Python Function
    for advanced formatting.
    """

    def __init__(self, width=340, height=126, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        # font
        fontName = 'Helvetica'
        # chart
        self._add(self, AreaLinePlot(), name='chart', validate=None, desc=None)
        self.chart.x = 25
        self.chart.y = 17.5
        self.chart.width = 305
        self.chart.height = 100
        self.chart.lines[0].strokeColor = PCMYKColor(100, 0, 90, 50, alpha=40)
        gridStickOut = 4
        strokeDashArray = (0.4, 0.4)
        # x axis
        self.chart.xValueAxis = NormalDateXValueAxis()
        self.chart.xValueAxis.labels.boxAnchor = 'autox'
        self.chart.xValueAxis.labels.fontName = fontName
        self.chart.xValueAxis.labels.fontSize = 6
        self.chart.xValueAxis.strokeWidth = 0.5
        self.chart.xValueAxis.strokeDashArray = strokeDashArray
        self.chart.xValueAxis.labels.topPadding = 3
        self.chart.xValueAxis.maximumTicks = 15
        self.chart.xValueAxis.visibleTicks = True
        self.chart.xValueAxis.forceFirstDate = 1
        self.chart.xValueAxis.maximumTicks = 6
        self.chart.xValueAxis.niceMonth = 0
        self.chart.xValueAxis.xLabelFormat = '{m}/{yy}'
        # y axis
        self.chart.yValueAxis.labels.fontName = fontName
        self.chart.yValueAxis.labels.fontSize = 6
        self.chart.yValueAxis.forceZero = 1
        self.chart.yValueAxis.gridStrokeDashArray = strokeDashArray
        self.chart.yValueAxis.visibleGrid = 1
        self.chart.yValueAxis.labelTextFormat = (
            lambda v, a=self.chart.yValueAxis: (
                abs(v - a._valueMax) < 1e-6 and '$%2d' or '%2d'
            )
            % v
        )
        self.chart.yValueAxis.strokeWidth = 0
        self.chart.yValueAxis.strokeDashArray = strokeDashArray
        self.chart.yValueAxis.labels.rightPadding = 0
        # self.chart.yValueAxis.origShiftIPC          = 1
        self.chart.yValueAxis.maximumTicks = 6
        self.chart.yValueAxis.rangeRound = 'both'
        # self.chart.yValueAxis.avoidBoundFrac        = 0.1
        self.chart.yValueAxis.gridStart = self.chart.x - gridStickOut
        self.chart.yValueAxis.gridEnd = (
            self.chart.x + self.chart.width + gridStickOut
        )
        # subgrid settings
        self.chart.yValueAxis.subTickNum = 1  # one minor ticks between ticks
        self.chart.yValueAxis.visibleSubGrid = True
        self.chart.yValueAxis.visibleSubTicks = True
        self.chart.yValueAxis.subGridStrokeWidth = (
            self.chart.yValueAxis.gridStrokeWidth
        )
        self.chart.yValueAxis.subGridStrokeDashArray = strokeDashArray
        self.chart.yValueAxis.subGridStart = self.chart.yValueAxis.gridStart
        self.chart.yValueAxis.subGridEnd = self.chart.yValueAxis.gridEnd
        self.chart.yValueAxis.visibleTicks = False
        self._label_format = DecimalFormatter(
            0, prefix='$', suffix=None, thousandSep=','
        )
        # sample data
        # self.chart.data = [(20030228, 10020.0), (20030331, 9910.0), (20030430, 10240.0), (20030530, 10660.0), (20030630, 10680.0), (20030731, 10690.0), (20030829, 10850.0), (20030930, 10760.0)]
        self.chart.data = [
            (20030228, 10020.0),
            (20030331, 9910.0),
            (20030430, 10240.0),
            (20030530, 10660.0),
            (20030630, 10680.0),
            (20030731, 10690.0),
            (20030829, 10850.0),
            (20030930, 10760.0),
            (20031031, 11170.0),
            (20031128, 11280.0),
            (20031231, 11553.190000000001),
            (20040130, 11635.57),
            (20040227, 11707.65),
            (20040331, 11635.57),
            (20040430, 11388.440000000001),
            (20040528, 11460.52),
            (20040630, 11651.870000000001),
            (20040730, 11233.110000000001),
            (20040831, 11306.4),
            (20040930, 11358.74),
            (20041029, 11536.709999999999),
            (20041130, 11945.0),
            (20041231, 12295.450000000001),
            (20050131, 11966.209999999999),
            (20050228, 12102.450000000001),
            (20050331, 11932.15),
            (20050429, 11716.440000000001),
            (20050531, 12034.33),
            (20050630, 11991.209999999999),
            (20050729, 12426.84),
            (20050831, 12254.879999999999),
            (20050930, 12289.280000000001),
            (20051031, 12128.780000000001),
            (20051130, 12564.41),
            (20051230, 12584.99),
            (20060131, 12967.76),
            (20060228, 12921.360000000001),
            (20060331, 13257.74),
            (20060428, 13338.93),
            (20060531, 12874.969999999999),
            (20060630, 12857.6),
            (20060731, 12834.35),
            (20060831, 12985.48),
            (20060929, 13171.49),
            (20061031, 13555.120000000001),
            (20061130, 13776.0),
            (20061229, 13886.870000000001),
            (20070131, 14053.4),
            (20070228, 13848.43),
            (20070330, 13925.299999999999),
            (20070430, 14335.24),
            (20070531, 14655.51),
            (20070629, 14460.98),
            (20070731, 14190.08),
            (20070831, 14319.08),
            (20070928, 14770.59),
            (20071031, 14925.389999999999),
            (20071130, 14460.98),
            (20071231, 14494.120000000001),
            (20080131, 13829.26),
            (20080229, 13637.18),
            (20080331, 13651.959999999999),
        ]
        # chart horizonatl line on the axis
        self.chart.annotations = [
            lambda c, cA, vA: Line(
                c.x,
                c.y - gridStickOut,
                c.x,
                c.y + c.height + gridStickOut,
                strokeColor=black,
                strokeWidth=0.5,
            )
        ]
        # chart vertical line on the right of the chart
        self.chart.annotations.append(
            lambda c, cA, vA: Line(
                c.x + c.width,
                c.y - gridStickOut,
                c.x + c.width,
                c.y + c.height + gridStickOut,
                strokeColor=black,
                strokeWidth=0.5,
            )
        )
        self._add(
            self,
            DynamicLabel(
                '', NormalDate(self.chart.data[0][0]), self.chart.data[0][1]
            ),
            name='label',
            validate=None,
            desc=None,
        )
        fontName = 'Helvetica'
        fontSize = 7
        self.label.fontName = fontName
        self.label.fontSize = fontSize
        self.label.fillColor = self.chart.lines[0].strokeColor
        self.label.boxFillColor = white
        self.label.textAnchor = 'end'
        self.label.boxAnchor = 'se'
        self.label.textAnchor = 'start'
        self.label.dx = -1
        self.chart.annotations.append(self.label.asAnnotation)
        self.chart.xValueAxis.specialTickClear = 1

    def getContents(self):
        # self.chart.debug            = 1
        # font bold
        # label - ending value
        dates = [d[0] for d in self.chart.data]
        values = [d[1] for d in self.chart.data]
        # if the sequence is 1,3,5 or 2,4,6 add subticks
        addConditionalSubTicks(self.chart)
        # look for the highest value under the final label - last 25% of data points
        mg = max(values)
        sf = mg / self.chart.height
        m = max(values[int(0.75 * len(values)) :]) + sf * 5
        mq = m + sf * self.label.fontSize
        self.chart.yValueAxis.valueMax = max(mg, mq)
        format = self._label_format
        self.label._ux = NormalDate(dates[-1])
        self.label._uy = m
        self.label._text = ' Ending Value %s ' % format(values[-1] * 1000)
        self.label.fillColor = black
        return Drawing.getContents(self)
