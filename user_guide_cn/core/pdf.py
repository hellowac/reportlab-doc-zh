import os
import logging
import glob

import reportlab
from reportlab import rl_settings, rl_config
from reportlab.lib.utils import open_and_read
from reportlab.rl_config import defaultPageSize
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.cidfonts import UnicodeCIDFont, defaultUnicodeEncodings
from reportlab import rl_settings
from reportlab.lib.units import inch
from reportlab.lib.sequencer import getSequencer
from reportlab.lib.colors import tan, green
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    CondPageBreak,
    NextPageTemplate,
    Spacer,
    XPreformatted,
    KeepTogether,
    Image,
)
from reportlab.platypus.xpreformatted import PythonPreformatted

from components.constant import (
    CAPTION_IMAGE,
    CAPTION_TABLE,
    CAPTION_IMAGE_PREFIX,
    CAPTION_TABLE_PREFIX,
)
from components import constant
from components.exception import FontNameNotFoundError, HeadingLevelError
from components.utils import find_file_name, quick_fix

from core.figure import Illustration, GraphicsDrawing, ParaBox, ParaBox2
from core.flowable import NoteAnnotation, HandAnnotation
from core.style.default import get_default_style_sheet
from core.toc import TableOfContents
from core.templates import RLDocTemplate


logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(__file__)


class PDF(object):
    _default_font_regular = 'SourceHanSans-ExtraLight'  # 将加细细的作为正常体
    _default_font_normal = 'SourceHanSans-Normal'  # 将细体的作为常规体
    _default_font_bold = 'SourceHanSans-Normal'  # 将正常的作为粗体
    _default_font_italic = 'SourceHanSans-Light'  # 忽略，没有斜体，留在这儿只为说明有这个功能
    _default_font_bold_italic = (
        'SourceHanSans-ExtraLight'  # 忽略，没有斜体，留在这儿只为说明有这个功能
    )

    def __init__(
        self,
        filename,
        pagesize=None,
        fonts_dir=None,
        font_regular=None,
        font_normal=None,
        font_bold=None,
        font_italic=None,
        font_bold_italic=None,
        toc_cls=None,
    ):
        default_font_dir = os.path.join(BASE_DIR, 'fonts')

        self.filename = filename

        # 处理页面大小
        self.pagesize = pagesize or rl_config.defaultPageSize

        # 处理字体
        self.fonts_dir = fonts_dir or default_font_dir
        self.fonts_map = {}

        # 外部字体包
        self._load_fonts(fonts_dir)
        # reportlab字体包
        reportlab_fonts_dir = os.path.join(
            os.path.dirname(reportlab.__file__), 'fonts'
        )
        self._load_fonts(reportlab_fonts_dir)
        # 检查字体名称是否在指定目录下和默认是否支持
        self._check_font_name(
            font_regular, font_normal, font_bold, font_italic, font_bold_italic
        )
        self.font_regular = font_regular or self._default_font_regular
        self.font_normal = font_normal or self._default_font_normal
        self.font_bold = font_bold or self._default_font_bold
        self.font_italic = font_italic or self._default_font_italic
        self.font_bold_italic = (
            font_bold_italic or self._default_font_bold_italic
        )
        # 注册字体
        self.registered_fonts = []
        self._register_font()

        # 保持一致flag
        self._keep_together_index = None

        # 初始化样式
        self.stylesheet = get_default_style_sheet(
            font_name=self.font_regular, font_bold=self.font_bold
        )
        self.toc_class = toc_cls or TableOfContents

        # 计数器
        # 计数器flag
        self._SEQ_CHAPTER_FLAG = 'Chapter'
        self._SEQ_SECTION_FLAG = 'Section'
        self._SEQ_APPENDIX_FLAG = 'Appendix'
        self._SEQ_FIGURE_FLAG = 'Figure'

        self.seq = getSequencer()
        self.seq.setFormat(self._SEQ_CHAPTER_FLAG, '1')  # 一级标题
        self.seq.setFormat(self._SEQ_SECTION_FLAG, '1')  # 二级标题
        self.seq.setFormat(self._SEQ_APPENDIX_FLAG, 'A')  # 附录
        self.seq.setFormat(self._SEQ_FIGURE_FLAG, '1')  # 图
        self.seq.chain(self._SEQ_CHAPTER_FLAG, self._SEQ_SECTION_FLAG)
        self.seq.chain(self._SEQ_CHAPTER_FLAG, self._SEQ_FIGURE_FLAG)

        # 示例函数宽高定义
        self.example_function_x_inches = constant.EXAMPLE_FUNCTION_X_INCHES
        self.example_function_y_inches = constant.EXAMPLE_FUNCTION_Y_INCHES
        self.example_function_display_sizes = (
            self.example_function_x_inches * inch,
            self.example_function_y_inches * inch,
        )

        # 构建的流对象
        self.store = []

        # 底层canv对象
        self._doc = RLDocTemplate(
            self.filename, self.font_regular, pagesize=defaultPageSize
        )

    def _load_fonts(self, fonts_dir):
        """
        加载指定字体文件目录中字体名称和文件映射。

        1. 初始化扩展字体, 参考用户手册: 3.5 支持TrueType字体
        """

        # 默认思源黑体, 仅支持ttf文件
        ttf_files = glob.glob(os.path.join(fonts_dir, '*.ttf'))
        fonts = self.fonts_map

        for file in ttf_files:
            font_name = find_file_name(file)
            fonts[font_name] = file

        return fonts

    def _register_font(self):
        """ 注册字体 """
        font_names = {
            self.font_regular,
            self.font_normal,
            self.font_bold,
            self.font_bold_italic,
            self.font_italic,
        }
        # reportlab包cid字体声明
        cid_font_names = defaultUnicodeEncodings.keys()

        for name in font_names:
            try:
                pdfmetrics.registerFont(TTFont(name, self.fonts_map[name]))
            except KeyError as e:
                if name in cid_font_names:
                    pdfmetrics.registerFont(UnicodeCIDFont(name))
                else:
                    raise
            else:
                self.registered_fonts.append(name)

        font_family = self.font_regular
        pdfmetrics.registerFontFamily(
            font_family,
            normal=None,  # self.font_normal,
            bold=None,  # self.font_bold,
            # 有限支持斜体，在文本中加入 ^斜体^ 表示某个英文为斜体，且不支持中文
            # italic=self.font_italic,
            # boldItalic=self.font_bold_italic or self.font_italic,
        )

    def _check_font_name(
        self,
        font_regular,
        font_normal,
        font_bold,
        font_italic,
        font_bold_italic,
    ):
        """检查字体名称是否合法"""

        font_names = list(self.fonts_map.keys())
        # reportlab包默认的unicode字体名称
        font_names.extend(list(defaultUnicodeEncodings.keys()))
        # reportlab包默认的扩展字体名称

        for font in (
            font_regular,
            font_normal,
            font_bold,
            font_italic,
            font_bold_italic,
        ):
            if font and font not in font_names:
                raise FontNameNotFoundError(f'未发现该字体: {font}')

    def quick_fix(self, text):
        return quick_fix(text, self.font_bold)

    def add_page_break(self):
        """ 添加一个新页 """
        self.store.append(PageBreak())

    def add_cond_page_break(self, inches=1):
        """ 添加一个高度间隔 """
        self.store.append(CondPageBreak(inches * inch))

    def add_title(self, text, style=None):
        """ 添加标题 """
        _style = style or self.stylesheet[constant.STYLE_TITLE]
        self.store.append(Paragraph(self.quick_fix(text), _style))

    def add_centred(self, text, style=None):
        """ 添加居中文本 """
        _style = style or self.stylesheet[constant.STYLE_CENTRED]
        self.store.append(Paragraph(self.quick_fix(text), _style))

    def add_toc_title(self, text, style=None):
        """ 添加目录标题 """
        # cn_headingTOC('目录')
        self.store.append(PageBreak())  # 分页

        _style = style or self.stylesheet[constant.STYLE_H1]
        self.store.append(Paragraph(self.quick_fix(text), _style))

    def add_toc(self):
        """ 添加目录内容处理模板 """
        self.store.append(PageBreak())
        self.store.append(self.toc_class(self.font_regular))

    def add_heading(self, text, level=1, style=None):
        """ 添加标题 level """

        style_map = {
            1: constant.STYLE_H1,
            2: constant.STYLE_H2,
            3: constant.STYLE_H3,
            4: constant.STYLE_H4,
        }

        if not style and level not in style_map:
            raise HeadingLevelError(
                f'标题等级: {level} 不在指定范围: {set(style_map.keys())}'
            )
        _style = style or self.stylesheet[style_map[level]]
        _text = self.quick_fix(text)

        if level == 1:
            self.add_page_break()
            self.store.append(
                Paragraph(
                    f'第 <seq id="{self._SEQ_CHAPTER_FLAG}"/> 章  {_text}', _style
                )
            )
        elif level == 2:
            self.add_cond_page_break()
            self.store.append(
                Paragraph(
                    f'<seq template="%({self._SEQ_CHAPTER_FLAG})s.'
                    f'%({self._SEQ_SECTION_FLAG}+)s "/> {_text}',
                    _style,
                )
            )
        elif level in (3, 4):
            self.add_cond_page_break()
            self.store.append(Paragraph(_text, _style))

    def add_caption(
        self, text, prefix=CAPTION_IMAGE_PREFIX, category=CAPTION_IMAGE
    ):
        _text = self.quick_fix(text)
        if category == CAPTION_TABLE:
            self.store.append(
                f'{prefix} <seq template="%(Chapter)s-%(Table+)s"/> - {_text}'
            )

        elif category == CAPTION_IMAGE:
            self.store.append(
                f'{prefix} <seq template="%(Chapter)s-%(Table+)s"/> - {_text}'
            )

    def add_paragraph(self, text, style=None):
        """ 添加段落 """

        _style = style or self.stylesheet[constant.STYLE_BODY_TEXT]
        self.store.append(Paragraph(self.quick_fix(text), _style))

    def add_bullet(self, text, style=None):
        """ 添加列表 """

        _style = style or self.stylesheet[constant.STYLE_BULLET]
        self.store.append(
            Paragraph(
                f'<bullet><font name="Symbol">\u2022</font></bullet>'
                f' {self.quick_fix(text)}',
                _style,
            )
        )

    def add_space(self, inches=1.0 / 6):
        """ 添加空格 """
        if inches:
            self.store.append(Spacer(0, inches * inch))

    def add_code_eg(
        self, text, before=0.1, after=0, style=None, format_cls=None
    ):
        """
        添加代码示例
        """
        _format_cls = format_cls or PythonPreformatted
        _style = style or self.stylesheet[constant.STYLE_CODE]

        self.add_space(before)
        self.store.append(_format_cls(text, _style))
        self.add_space(after)

    def add_np_eg(self, text, before=0.1, after=0, style=None, format_cls=None):
        """ 添加文本示例， 不是代码 """

        _format_cls = format_cls or XPreformatted
        self.add_code_eg(
            self.quick_fix(text),
            before=before,
            after=after,
            format_cls=_format_cls,
            style=style,
        )

    def add_embedded_code(self, code, name='t'):
        """ 执行嵌入的代码 """
        self.add_code_eg(code)
        self.add_paragraph("结果:")
        var = {}  # globals locals
        exec(code, var, var)
        self.store.append(var[name])

    def add_image(self, path, width=None, height=None):
        """ 添加图片 """
        s = self.start_keep_together()
        self.add_space(0.2)
        self.store.append(Image(path, width, height))
        self.add_space(0.2)
        self.end_keep_together(s)

    def add_todo(self, text, style=None):
        """ 添加todo """
        _style = style or self.stylesheet[constant.STYLE_COMMENT]
        self.store.append(Paragraph(self.quick_fix(text), _style))

    def add_illustration(self, operation, caption, width=None, height=None):
        """ 添加插图 """
        _caption = (
            f'图 <seq template="%({self._SEQ_CHAPTER_FLAG})s - %('
            f'{self._SEQ_FIGURE_FLAG}+)s"/> : {caption}'
        )
        illus = Illustration(
            operation,
            _caption,
            width=width,
            height=height,
            font_name=self.font_regular,
        )
        self.store.append(illus)

    def add_draw(self, drawing, caption):
        """ 添加绘制 """
        _caption = (
            f'图 <seq template="%({self._SEQ_CHAPTER_FLAG})s - '
            f'%({self._SEQ_FIGURE_FLAG}+)s"/> : {caption}'
        )
        self.store.append(GraphicsDrawing(drawing, caption))

    def add_para_box(self, text, style, caption):
        self.store.append(
            ParaBox(
                self.quick_fix(text),
                style,
                f'图 <seq template="%(Chapter)s-%(Figure+)s"/>: {caption}',
            )
        )

    def add_para_box2(self, text, caption, style=None):
        _style = style or self.stylesheet[constant.STYLE_BODY_TEXT]
        _caption = (
            f'图 <seq template="%({self._SEQ_CHAPTER_FLAG})s'
            f'-%({self._SEQ_FIGURE_FLAG}+)s"/>: {caption}'
        )
        self.store.append(ParaBox2(self.quick_fix(text), caption, _style))

    def add_pencil_note(self):
        """ 添加铅笔标识 """
        self.store.append(NoteAnnotation())

    def add_text_note(self, text, style=None):
        """ 添加文本注意 """
        _style = style or self.stylesheet[constant.STYLE_BODY_TEXT]
        _text = f"<font color=red>注意：</font>{self.quick_fix(text)}"
        self.store.append(Paragraph(_text, _style))

    def add_hand_note(
        self, xoffset=0, size=None, fillcolor=tan, strokecolor=green
    ):
        """ 添加手掌标识 """
        self.store.append(HandAnnotation(xoffset, size, fillcolor, strokecolor))

    def start_keep_together(self):
        """ 记录开始索引 """
        idx = len(self.store)
        return idx

    def end_keep_together(self, index_flag):
        """ 根据开始索引，将后续内容保持在一起 """
        keep_together = KeepTogether(self.store[index_flag:])
        self.store[index_flag:] = [keep_together]

    def next_toc_template(self):
        """ 后面使用目录模板 """
        self.store.append(NextPageTemplate(constant.TEMPLATE_TOC))

    def next_normal_template(self):
        """ 后面使用常规模板 """
        # nextTemplate("Normal")
        self.store.append(NextPageTemplate(constant.TEMPLATE_NORMAL))

    def build_2_save(self):
        self._doc.multiBuild(self.store)

    @property
    def canv(self):
        if not self._doc.canv:
            raise AttributeError('该属性不存在')
        return self._doc.canv
