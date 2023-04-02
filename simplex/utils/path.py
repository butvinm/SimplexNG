import os
import sys


def get_path(path: str) -> str:
    '''Get path to resource in exe or in source'''

    MEIPASS = getattr(sys, '_MEIPASS', None)
    if MEIPASS:
        return os.path.join(MEIPASS, path)
    else:
        return os.path.join(os.path.abspath("."), path)
