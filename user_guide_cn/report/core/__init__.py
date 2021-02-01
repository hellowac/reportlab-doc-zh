import os
import glob
import logging

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.cidfonts import UnicodeCIDFont, defaultUnicodeEncodings

from report.components.utils import find_file_name, quick_fix

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)

FONTS_DIR = os.path.join(PARENT_DIR, 'fonts')

logger = logging.getLogger(__name__)

VALIDATED_FONT_NAMES = {}


def _load_and_register_fonts():
    """
    加载指定字体文件目录中字体名称和文件映射 并注册

    1. 初始化扩展字体, 参考用户手册: 3.5 支持TrueType字体
    """
    global VALIDATED_FONT_NAMES

    # 默认思源黑体, 仅支持ttf文件
    ttf_files = glob.glob(os.path.join(FONTS_DIR, '*.ttf'))
    fonts = {find_file_name(file): file for file in ttf_files}

    # reportlab包默认的cid字体声明
    cid_font_names = defaultUnicodeEncodings.keys()

    for name in [*fonts.keys(), *cid_font_names]:
        try:
            path = fonts[name]
            pdfmetrics.registerFont(TTFont(name, path))
        except KeyError as e:
            if name in cid_font_names:
                pdfmetrics.registerFont(UnicodeCIDFont(name))
                path = f'BuildIn Font {name}'
            else:
                raise e
        else:
            VALIDATED_FONT_NAMES[name] = path
        logger.debug(f'注册字体: {name}')


_load_and_register_fonts()
