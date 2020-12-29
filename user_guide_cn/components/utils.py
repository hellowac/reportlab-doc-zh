import os
import json
import logging

from contextlib import redirect_stderr
from fontTools import ttLib

logger = logging.getLogger(__name__)


def find_font_name(font_path):
    """查找ttf文件中字体名称

    print(find_font_name('myfont.ttf'))
    # ('Century Bold Italic', 'Century', 'Bold Italic') – name, family, style

    # 参考: https://gist.github.com/pklaus/dce37521579513c574d0#gistcomment-3507444
    """

    font = ttLib.TTFont(font_path, ignoreDecompileErrors=True)
    with redirect_stderr(None):
        names = font['name'].names

    details = {}
    for x in names:
        if x.langID == 0 or x.langID == 1033:
            try:
                details[x.nameID] = x.toUnicode()
            except UnicodeDecodeError:
                details[x.nameID] = x.string.decode(errors='ignore')

    name, family, style = details[4], details[1], details[2]
    logger.info(f'name: {name}, family: {family}, style: {style}')
    logger.info(json.dumps(details))
    # ''.join([family, name,])

    return name


def find_file_name(file_path):
    """ 获取文件名称 """
    basename = os.path.basename(file_path)
    name, ext = os.path.splitext(basename)

    return name
