# https://hg.reportlab.com/hg-public/reportlab/log/tip/tools/docco/t_parse.py

"""
Template parsing module inspired by REXX (with thanks to Donn Cave for
discussion).

Template initialization has the form:
   T = Template(template_string, wild_card_marker, single_char_marker,
             x = regex_x, y = regex_y, ...)
Parsing has the form
   ([match1, match2, ..., matchn], lastindex) = T.PARSE(string)

Only the first argument is mandatory.

The resultant object efficiently parses strings that match the template_string,
giving a list of substrings that correspond to each "directive" of the template.

Template directives:

  Wildcard:
    The template may be initialized with a wildcard that matches any string
    up to the string matching the next directive (which may not be a wild
    card or single character marker) or the next literal sequence of characters
    of the template.  The character that represents a wildcard is specified
    by the wild_card_marker parameter, which has no default.

    For example, using X as the wildcard:


    >>> T = Template("prefixXinteriorX", "X")
    >>> T.PARSE("prefix this is before interior and this is after")
    ([' this is before ', ' and this is after'], 47)
    >>> T = Template("<X>X<X>", "X")
    >>> T.PARSE('<A HREF="index.html">go to index</A>')
    (['A HREF="index.html"', 'go to index', '/A'], 36)

    Obviously the character used to represent the wildcard must be distinct
    from the characters used to represent literals or other directives.

  Fixed length character sequences:
    The template may have a marker character which indicates a fixed
    length field.  All adjacent instances of this marker will be matched
    by a substring of the same length in the parsed string.  For example:

      >>> T = Template("NNN-NN-NNNN", single_char_marker="N")
      >>> T.PARSE("1-2-34-5-12")
      (['1-2', '34', '5-12'], 11)
      >>> T.PARSE("111-22-3333")
      (['111', '22', '3333'], 11)
      >>> T.PARSE("1111-22-3333")
      ValueError: literal not found at (3, '-')

    A template may have multiple fixed length markers, which allows fixed
    length fields to be adjacent, but recognized separately.  For example:

      >>> T = Template("MMDDYYX", "X", "MDY")
      >>> T.PARSE("112489 Somebody's birthday!")
      (['11', '24', '89', " Somebody's birthday!"], 27)

  Regular expression markers:
    The template may have markers associated with regular expressions.
    the regular expressions may be either string representations of compiled.
    For example:
      >>> T = Template("v: s i", v=id, s=str, i=int)
      >>> T.PARSE("this_is_an_identifier: 'a string' 12344")
      (['this_is_an_identifier', "'a string'", '12344'], 39)
      >>>

    Here id, str, and int are regular expression conveniences provided by
    this module.

  Directive markers may be mixed and matched, except that wildcards cannot
  precede
  wildcards or single character markers.
  Example:
>>> T = Template("ssnum: NNN-NN-NNNN, fn=X, ln=X, age=I, quote=Q", "X", "N",I=int, Q=str)
>>> T.PARSE("ssnum: 123-45-6789, fn=Aaron, ln=Watters, age=13, quote='do bedo be do'")
(['123', '45', '6789', 'Aaron', 'Watters', '13', "'do be do be do'"], 72)
>>>

"""

import re
import string
from reportlab.lib.utils import ascii_letters

"""
受REXX启发的模板解析模块（感谢Donn Cave的讨论）。

模板初始化具有以下形式:
    T = Template(template_string, wild_card_marker, single_char_marker,
             x = regex_x, y = regex_y, ...)
解析形式:
    ([match1, match2, ..., matchn], lastindex) = T.PARSE(string)

只有第一个参数是必须的。

结果对象有效地解析了与template_string相匹配的字符串，
给出了与模板的每个 "指令"(directive) 相对应的子串列表。

模板指令：
    通配符：
        可以使用通配符来初始化模板，通配符可以匹配任何字符串，
        直到匹配下一个指令（不能是通配符或单个字符标记）或模板的下一个文字序列的字符串为止。
        代表通配符的字符由wild_card_marker参数指定，该参数没有默认值。

        例如，使用X作为通配符。

        >>> T = Template("prefixXinteriorX", "X")
        >>> T.PARSE("prefix this is before interior and this is after")
        ([' this is before ', ' and this is after'], 47)
        >>> T = Template("<X>X<X>", "X")
        >>> T.PARSE('<A HREF="index.html">go to index</A>')
        (['A HREF="index.html"', 'go to index', '/A'], 36)

        显然，用于表示通配符的字符必须与用于表示文字或其他指令的字符不同。

    固定长度的字符序列:
        模板可以有一个标记字符，表示一个固定长度的字段。
        该标记的所有相邻实例将在解析后的字符串中被一个相同长度的子串匹配。
        例如：

        >>> T = Template("NNN-NN-NNNN", single_char_marker="N")
        >>> T.PARSE("1-2-34-5-12")
        (['1-2', '34', '5-12'], 11)
        >>> T.PARSE("111-22-3333")
        (['111', '22', '3333'], 11)
        >>> T.PARSE("1111-22-3333")
        ValueError: literal not found at (3, '-')

        一个模板可以有多个固定长度标记，
        这使得固定长度的字段可以相邻，但可以分别识别。
        例如：

        >>> T = Template("MMDDYYX", "X", "MDY")
        >>> T.PARSE("112489 Somebody's birthday!")
        (['11', '24', '89', " Somebody's birthday!"], 27)

    正则表达式标记:

        模板可以具有与正则表达式相关联的标记，正则表达式可以是编译后的字符串表示。
        例如:

        >>> T = Template("v: s i", v=id, s=str, i=int)
        >>> T.PARSE("this_is_an_identifier: 'a string' 12344")
        (['this_is_an_identifier', "'a string'", '12344'], 39)
        >>>

        这里的id、str、int是本模块提供的正则表达式便利。

    指令标记可以混合和匹配，除非通配符不能在通配符或单个字符标记之前。
    例如:

    >>> T = Template("ssnum: NNN-NN-NNNN, fn=X, ln=X, age=I, quote=Q", "X", "N",I=int, Q=str)
    >>> T.PARSE("ssnum: 123-45-6789, fn=Aaron, ln=Watters, age=13, quote='do bedo be do'")
    (['123', '45', '6789', 'Aaron', 'Watters', '13', "'do be do be do'"], 72)
    >>>
"""

# some useful regular expressions
# 一些有用的常用表达式
_id = re.compile(f"[{ascii_letters}][{ascii_letters}{string.digits}_]*")
_str = re.compile("'[^\n']*'")
_int = re.compile(f"[{string.digits}]+")


#
# template parsing
#
# EG: T = Template("(NNN)NNN-NNNN X X", "X", "N")
#     ([area, exch, ext, fn, ln], index) = T.PARSE("(908)949-2726 Aaron
#     Watters")
#
class Template:

    def __init__(
        self,
        template,
        wild_card_marker=None,
        single_char_marker=None,
        **marker_to_regex_dict,
    ):
        self.template = template
        self.wild_card = wild_card_marker
        self.char = single_char_marker
        # determine the set of markers for this template (确定此模板的标记集)
        markers = list(marker_to_regex_dict.keys())
        if wild_card_marker:
            markers.append(wild_card_marker)
        if single_char_marker:
            for ch in single_char_marker:  # allow multiple scm's (允许多个scm)
                markers.append(ch)
            self.char = single_char_primary = single_char_marker[0]
        self.markers = markers
        for mark in markers:
            if len(mark) > 1:
                raise ValueError(
                    "Marks must be single characters(标记必须是单个字符): " + repr(mark)
                )
        # compile the regular expressions if needed (如果需要，编译正则表达式)
        self.marker_dict = marker_dict = {}
        for mark, rgex in marker_to_regex_dict.items():
            if isinstance(rgex, str):
                rgex = re.compile(rgex)
            marker_dict[mark] = rgex
        # determine the parse sequence (确定解析顺序)
        parse_seq = []
        # dummy last char (虚拟最后一个字符)
        lastchar = None
        index = 0
        last = len(template)
        # count the number of directives encountered (计算遇到的指令数量)
        ndirectives = 0
        while index < last:
            start = index
            thischar = template[index]
            # is it a wildcard? (它是通配符吗？)
            if thischar == wild_card_marker:
                if lastchar == wild_card_marker:
                    raise ValueError(
                        "two wild cards in sequence is not allowed"
                    )
                parse_seq.append((wild_card_marker, None))
                index = index + 1
                ndirectives = ndirectives + 1
            # is it a sequence of single character markers? (它是一个单字符标记序列吗？)
            elif single_char_marker and thischar in single_char_marker:
                if lastchar == wild_card_marker:
                    raise ValueError(
                        "wild card cannot precede single char marker"
                        "(通配符不能在单个字符标记之前)"
                    )
                while index < last and template[index] == thischar:
                    index = index + 1
                parse_seq.append((single_char_primary, index - start))
                ndirectives = ndirectives + 1
            # is it a literal sequence? (这是字面上的序列吗？)
            elif not thischar in markers:
                while index < last and not template[index] in markers:
                    index = index + 1
                parse_seq.append((None, template[start:index]))
            # otherwise it must be a re marker (否则必须是重新标记)
            else:
                rgex = marker_dict[thischar]
                parse_seq.append((thischar, rgex))
                ndirectives = ndirectives + 1
                index = index + 1
            lastchar = template[index - 1]
        self.parse_seq = parse_seq
        self.ndirectives = ndirectives

    def PARSE(self, s, start=0):
        ndirectives = self.ndirectives
        wild_card = self.wild_card
        single_char = self.char
        parse_seq = self.parse_seq
        lparse_seq = len(parse_seq) - 1
        # make a list long enough for substitutions for directives
        # (列出足够长的时间来替换指令)
        result = [None] * ndirectives
        current_directive_index = 0
        currentindex = start
        # scan through the parse sequence, recognizing
        # (扫描解析序列，识别)
        for parse_index in range(lparse_seq + 1):
            (indicator, data) = parse_seq[parse_index]
            # is it a literal indicator?
            if indicator is None:
                if s.find(data, currentindex) != currentindex:
                    raise ValueError(
                        "literal not found at " + repr((currentindex, data))
                    )
                currentindex = currentindex + len(data)
            else:
                # anything else is a directive (其他任何东西都是指令)
                # is it a wildcard? (它是通配符吗？)
                if indicator == wild_card:
                    # if it is the last directive then it matches the rest of
                    # the string
                    # 如果它是最后一个指令，则它与字符串的其余部分匹配
                    if parse_index == lparse_seq:
                        last = len(s)
                    # otherwise must look at next directive to find end of
                    # wildcard
                    # 否则必须查看下一个指令以找到通配符的结尾
                    else:
                        # next directive must be re or literal
                        # 下一个指令必须是re或文字
                        (nextindicator, nextdata) = parse_seq[parse_index + 1]
                        if nextindicator is None:
                            # search for literal
                            # 搜索文字
                            last = s.find(nextdata, currentindex)
                            if last < currentindex:
                                raise ValueError(
                                    "couldn't terminate wild with lit (无法用文字解析)"
                                    + repr(currentindex)
                                )
                        else:
                            # data is a re, search for it
                            # 数据是一个re，搜索它
                            last = nextdata.search(s, currentindex)
                            if last < currentindex:
                                raise ValueError(
                                    "couldn't terminate wild with re (无法用正则解析)"
                                    + repr(currentindex)
                                )
                elif indicator == single_char:
                    # data is length to eat (数据长度刚刚好)
                    last = currentindex + data
                else:
                    # other directives are always regular expressions
                    # 其他指令始终是正则表达式
                    print(f'data: {data} \n'
                          f's: {s} \n'
                          f'currentindex: {currentindex}')
                    last = data.match(s, currentindex) + currentindex
                    if last < currentindex:
                        raise ValueError(
                            "couldn't match re at(无法正则匹配) " + repr(currentindex)
                        )
                # print("accepting", s[currentindex:last])
                result[current_directive_index] = s[currentindex:last]
                current_directive_index = current_directive_index + 1
                currentindex = last

        # sanity check
        # 完整性检查
        if current_directive_index != ndirectives:
            raise SystemError("not enough directives found(没有足够指令)?")
        return result, currentindex


def test():
    global T, T1, T2, T3

    T = Template("(NNN)NNN-NNNN X X", "X", "N")
    print(T.PARSE("(908)949-2726 Aaron Watters"))

    # T1 = Template("s --> s blah", s=_str)
    # s = "' <-- a string --> ' --> 'blah blah another string blah' blah"
    # print(T1.PARSE(s))

    # T2 = Template("s --> NNNiX", "X", "N", s=_str, i=_int)
    # print(T2.PARSE("'A STRING' --> 15964653alpha beta gamma"))

    T3 = Template("XsXi", "X", "N", s=_str, i=_int)
    print(T3.PARSE("prefix'string'interior1234junk not parsed"))

    T4 = Template("MMDDYYX", "X", "MDY")
    print(T4.PARSE("122961 Somebody's birthday!"))


if __name__ == "__main__":
    test()
