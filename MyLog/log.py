import logging
import sys

PATH = "log.txt"
LOGGER = logging.getLogger(PATH)

LOGGER_HANDLER = None
try:
    from .ansistrm.ansistrm import ColorizingStreamHandler

    disableColor = False

    for argument in sys.argv:
        if "disable-col" in argument:
            disableColor = True
            break

    FILE_HANDLER = logging.FileHandler(PATH)

    if disableColor:
        LOGGER_HANDLER = logging.StreamHandler(sys.stdout)
    else:
        LOGGER_HANDLER = ColorizingStreamHandler(sys.stdout)
except ImportError as e:
    print(e)
    FILE_HANDLER = logging.FileHandler(PATH)
    LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

FORMATTER1 = logging.Formatter(
    '\r[%(asctime)s] [%(levelname)s] %(message)s', '%H:%M:%S')
FORMATTER2 = logging.Formatter(
    '[%(asctime)s] [%(levelname)s] %(message)s', '%H:%M:%S')


LOGGER_HANDLER.setFormatter(FORMATTER1)
LOGGER.addHandler(LOGGER_HANDLER)
LOGGER.setLevel(logging.DEBUG)

FILE_HANDLER.setFormatter(FORMATTER2)
LOGGER.addHandler(FILE_HANDLER)
FILE_HANDLER.setLevel(logging.ERROR)
