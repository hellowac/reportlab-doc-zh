import os
import logging

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


def main(filename):
    fonts_dir = os.path.join(os.path.dirname(BASE_DIR), 'fonts')
    pdf = PDF(filename, fonts_dir=fonts_dir)


if __name__ == '__main__':

    setup_logging()
    main('test.pdf')
