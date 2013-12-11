from mediacrush.config import _cfg
from mediacrush.fileutils import EXTENSIONS, get_mimetype

import os

class ProcessingException(Exception): pass
class TimeoutException(Exception): pass

class Processor(object):
    def __init__(self, tmppath, f):
        self.path = tmppath
        self.output = os.path.join(_cfg("storage_folder"), f.hash)

        self.f = f

    def _execute(self, command, important=True):
        extension = EXTENSIONS[get_mimetype(self.f.original)]

        tlc = command(self.path, self.output, extension=extension)
        tlc.run()

        if tlc.exited and important:
            raise TimeoutException

        if tlc.returncode != 0 and important:
            raise ProcessingException

    def sync(self):
        pass

    def async(self):
        pass