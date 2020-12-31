import os
import logging
from datetime import datetime

import reportlab
from core.pdf import PDF


BASE_DIR = os.path.dirname(__file__)


def setup_logging():
    # Define the log format
    log_format = '%(filename)s %(funcName)s:%(lineno)s %(message)s'

    # Define basic configuration
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[logging.StreamHandler()],
    )


def chapter1(pdf):
    pdf.add_title('用户手册')
    pdf.add_centred(f'版本 {reportlab.Version}')
    pdf.add_centred(datetime.now().strftime('文档生成自 $%Y/%m/%d %H:%M:%S %Z$'))
    pdf.next_toc_template()
    pdf.add_toc()
    pdf.next_normal_template()
    pdf.add_heading('介绍', level=1)
    pdf.add_heading('关于', level=2)
    pdf.add_text(
        '本文档是 ReportLab PDF 库的简介。阅读本文档我们已经假定您熟悉Python编程语言是。'
        '如果您是 Python 编程的新手，我们将在下一小节告诉您该去哪儿学习 Python 编程。'
    )


def main(filename):
    fonts_dir = os.path.join(os.path.dirname(BASE_DIR), 'fonts')
    pdf = PDF(filename, fonts_dir=fonts_dir)

    chapter1(pdf)


if __name__ == '__main__':

    setup_logging()
    main('test.pdf')
