import os, glob

__all__ = [
    os.path.split(os.path.splitext(file)[0])[1]
    for file in glob.glob(os.path.join(os.path.dirname(__file__), '[a-zA-Z0-9]*.py'))
]

## Logger Setup
from logging import getLogger, DEBUG, NullHandler

def getModuleLogger(modname):
    logger = getLogger(modname)
    logger.addHandler(NullHandler())
    logger.setLevel(DEBUG)
    logger.propagate = True
    return logger
