# MIT License
#
# Copyright (c) 2020 Jonathan T. Moore
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging
import os

from util import random_string

def _set_logging():
    lvl = os.environ.get('LOG_LEVEL','INFO')
    names = { 'DEBUG' : logging.DEBUG, 'INFO' : logging.INFO,
              'WARN' : logging.WARN, 'WARNING' : logging.WARNING,
              'ERROR' : logging.ERROR, 'CRITICAL' : logging.CRITICAL,
              'FATAL' : logging.FATAL }
    if lvl not in names:
        logging.warn("unexpected LOG_LEVEL %s" % (lvl,))
        lvl = 'INFO'
    logging.getLogger().setLevel(names[lvl])

def set_config(app):
    _set_logging()
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', random_string(16))
