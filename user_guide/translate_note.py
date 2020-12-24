# Copyright ReportLab Europe Ltd. 2000-2017
# see license.txt for license details
# history https://hg.reportlab.com/hg-public/reportlab/log/tip/docs/userguide/app_demos.py
from utils import (
    Appendix1,
    cn_Appendix1,
    disc,
    cn_disc,
    bullet,
    cn_bullet,
    heading2,
    cn_heading2,
    cn_heading3,
    eg,
)

# Appendix1("ReportLab Demos")
cn_Appendix1("译者备注")

cn_disc(
    """后面的信息为译者在翻译本手册时，学习，查询资料做的备注，或者说总结，没有对应的英文版..."""
)

cn_heading2("$Win Ansi$ 编码 和 $Mac Roman$ 编码")

cn_disc('参考: <font color="blue"><u>'
        '<a href="https://www.ziti163.com/Item/2054.aspx">'
        '$ANSI$，$ISO-8859-1$和$MacRoman$字符集之间的差异'
        '</a></u></font>')

cn_disc('以下为原文和译文:')

disc('Of the three main 8-bit character sets, '
     'only ISO-8859-1 is produced by a standards organization.  '
     'The three sets are identical for the 95 characters from 32 to 126, '
     'the ASCII character set.  '
     'The ANSI character set, also known as Windows-1252, '
     'has become a Microsoft proprietary character set; '
     'it is a superset of ISO-8859-1 with the addition of 27 characters '
     'in locations that ISO designates for control codes.  '
     'Apple’s proprietary MacRoman character set '
     'contains a similar variety of characters from 128 to 255, '
     'but with very few of them assigned the same numbers, '
     'and also assigns characters to the control-code positions.')

disc('The characters that appear in the first column '
        'of the following tables are generated '
        'from Unicode numeric character references, '
        'and so they should appear correctly in any Web browser '
        'that supports Unicode and that has suitable fonts available, '
        'regardless of the operating system.')

bullet('ANSI characters not present in ISO-8859-1')
bullet('ANSI characters not present in MacRoman')
bullet('ISO-8859-1 characters not present in ANSI')
bullet('ISO-8859-1 characters not present in MacRoman')
bullet('MacRoman characters not present in ANSI')
bullet('MacRoman characters not present in ISO-8859-1')

cn_disc('译文:')

cn_disc('在三种主要的8位字符集中，只有$ISO-8859-1$是由标准组织制作的。 '
        '这三个字符集对于32到126这95个字符，即$ASCII$字符集是相同的。 '
        '$ANSI$字符集，也就是$Windows-1252$，已经成为微软的专有字符集；'
        '它是$ISO-8859-1$的超集，在ISO指定控制代码的位置增加了27个字符。 '
        '苹果公司专有的$MacRoman$字符集包含从128到255个类似的各种字符，'
        '但其中很少有相同的数字，而且还将字符分配到控制码的位置。')

cn_disc('下表第一栏中显示的字符是从$Unicode$数字字符引用生成的，'
        '因此，无论使用什么操作系统，'
        '它们都应该在支持$Unicode$并具有合适的可用字体的任何$Web$浏览器中正确显示。')

cn_bullet('$ISO-8859-1$ 中不存在 $ANSI$ 字符')
cn_bullet('$MacRoman$ 中不存在 $ANSI$ 字符')
cn_bullet('$ANSI$ 中不存在 $ISO-8859-1$ 字符')
cn_bullet('$MacRoman$ 中不存在 $ISO-8859-1$ 字符')
cn_bullet('$ANSI$ 中不存在 $MacRoman$ 字符')
cn_bullet('$ISO-8859-1$ 中不存在 $MacRoman$ 字符')

cn_heading3('其他参考:')

cn_disc('$Win Ansi$ 编码总体来说就是, '
        '微软公司根据$windows$系统的本地化和国际化地区，'
        '默认采取的某种编码.'
        '参考:<font color="blue"><u>'
        '<a href="https://www.cnblogs.com/malecrab/p/5300486.html">'
        '$ANSI$是什么编码？</a></u></font>')
