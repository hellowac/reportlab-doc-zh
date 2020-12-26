import os
import logging
from time import time
from datetime import datetime

from reportlab.lib.utils import open_and_read
from reportlab.rl_config import defaultPageSize
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab import rl_settings

from utils import (
    setStory,
    getStory,
    RLDocTemplate,
)

rl_settings.verbose = 1


# Define the log format
log_format = '%(filename)s %(funcName)s:%(lineno)s %(message)s'


# Define basic configuration
logging.basicConfig(
    # Define logging level
    level=logging.NOTSET,
    # Declare the object we created to format the log messages
    format=log_format,
    # Declare handlers
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(__file__)


def run():
    G = {}
    pdf_file = datetime.now().strftime('userguide-%Y%m%d%H%M%S.pdf')

    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
    pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
    # pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

    registerFontFamily(
        'Vera',
        normal='Vera',
        bold='VeraBd',
        italic='VeraIt',
        boldItalic='VeraBI',
    )

    # 思源黑体

    pdfmetrics.registerFont(TTFont('SourceHanSansSC',
                                   os.path.join(BASE_DIR, 'fonts',
                                                'SourceHanSans-ExtraLight.ttf')))
    pdfmetrics.registerFont(TTFont('SourceHanSansBd',
                                   os.path.join(BASE_DIR, 'fonts',
                                                'SourceHanSans-Bold.ttf')))
    pdfmetrics.registerFont(TTFont('SourceHanSansIt',
                                   os.path.join(BASE_DIR, 'fonts',
                                                'SourceHanSans-ExtraLight.ttf')))

    pdfmetrics.registerFontFamily('SourceHanSansSC',
                                  normal='SourceHanSansSC',
                                  bold='SourceHanSansSCBd',
                                  italic='SourceHanSansSC',
                                  boldItalic='SourceHanSansSC')


    exec('from utils import *', G, G)
    doc = RLDocTemplate(pdf_file, pagesize=defaultPageSize)

    logger.info(type(doc))

    # this builds the story
    setStory()

    for filename in (
        'ch1_intro.py',
        'ch2_graphics.py',
        'ch2a_fonts.py',
        'ch3_pdffeatures.py',
        'ch4_platypus_concepts.py',
        'ch5_paragraphs.py',
        'ch6_tables.py',
        'ch7_flowable.py',
        'ch8_custom_flowable.py',
        'graph_01_intro.py',
        'graph_02_concepts.py',
        'graph_03_charts.py',
        'graph_04_shapes.py',
        'graph_05_widgets.py',
        'app_demos.py',
        'translate_note.py'
    ):
        logger.info(filename)
        script = open_and_read(filename)
        exec(script, G, G)
    del G

    story = getStory()

    logger.info('Built story contains %d flowables...' % len(story))

    doc.multiBuild(story)

    logger.info(f'Saved {pdf_file}')


def makeSuite():
    "standard test harness support - run self as separate process"
    from tests.utils import ScriptThatMakesFileTest

    return ScriptThatMakesFileTest(
        '../docs/userguide', 'genuserguide.py', 'reportlab-userguide.pdf'
    )


def main():
    t0 = time()
    run()
    logger.info('Generation of userguide took %.2f seconds' % (time() - t0))


if __name__ == "__main__":
    main()
