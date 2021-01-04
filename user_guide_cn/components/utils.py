import os
import json
import logging

from contextlib import redirect_stderr
# from fontTools import ttLib

from components.t_parse import Template

logger = logging.getLogger(__name__)

QF_CODE_TEMPLATE = Template("X$X$", "X")
QF_REP_TEMPLATE = Template("X^X^", "X")


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


def quick_fix(text, code_font):
    """inside text find any subsequence of form $subsequence$.
    Format the subsequence as code.  If similarly if text contains ^arg^
    format the arg as replaceable.  The escape sequence for literal
    $ is $\\$ (^ is ^\\^.
    """
    # logger.info('<<' + '=' * 100)
    # logger.info(f'text: {text}')

    # Courier
    code_subst = f"%s<font name={code_font}><nobr>%s</nobr></font>"  # 粗体
    qf_subst = f"%s<font name=Courier><i><nobr>%s</nobr></i></font>"  #
    # 斜体，不支持中文

    for (template, subst) in [
        (QF_CODE_TEMPLATE, code_subst),
        (QF_REP_TEMPLATE, qf_subst),
    ]:
        fragment = text
        parts = []
        try:
            while fragment:
                try:
                    matches, index = template.PARSE(fragment)
                except Exception as e:
                    raise ValueError
                else:
                    prefix, code = matches
                    if code == "\\":
                        part = fragment[:index]
                    else:
                        part = subst % (prefix, code)
                    parts.append(part)
                    fragment = fragment[index:]
        except ValueError:
            parts.append(fragment)
        text = ''.join(parts)

    # logger.info(f'quickfix text: {text}')
    # logger.info('=' * 100 + '>> \n\n')
    return text
