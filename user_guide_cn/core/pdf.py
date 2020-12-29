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

from components.exception import FontNameNotFoundError
from components.utils import find_file_name


logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(__file__)


class PDF(object):
    _default_font = 'SourceHanSans-Normal'  # reportlab 支持的默认中文字体名称

    def __init__(
        self,
        filename,
        fonts_dir=None,
        font_regular=None,
        font_normal=None,
        font_bold=None,
        font_italic=None,
        font_bold_italic=None,
    ):
        default_font_dir = os.path.join(BASE_DIR, 'fonts')

        self.filename = filename
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
        self.font_regular = font_regular or self._default_font
        self.font_normal = font_normal or self._default_font
        self.font_bold = font_bold or self._default_font
        self.font_italic = font_italic or self._default_font
        self.font_bold_italic = font_bold_italic or self._default_font
        # 注册字体
        self.registered_fonts = []
        self._register_font()

        # 构建的流对象
        self.store = []

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

    def _register_font(
        self,
    ):
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
            normal=self.font_normal,
            bold=self.font_bold,
            italic=self.font_italic,
            boldItalic=self.font_bold_italic or self.font_italic,
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
