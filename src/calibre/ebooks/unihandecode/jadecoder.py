__license__ = 'GPL 3'
__copyright__ = '2010, Hiroshi Miura <miurahr@linux.com>'
__docformat__ = 'restructuredtext en'

'''
Decode unicode text to an ASCII representation of the text for Japanese.
 Translate unicode string to ASCII roman string.

API is based on the python unidecode,
which is based on Ruby gem (http://rubyforge.org/projects/unidecode/)
and  perl module Text::Unidecode
(http://search.cpan.org/~sburke/Text-Unidecode-0.04/).

This functionality is owned by Kakasi Japanese processing engine.

Copyright (c) 2010 Hiroshi Miura
'''

import re
from calibre.ebooks.unihandecode.unidecoder import Unidecoder
from calibre.ebooks.unihandecode.unicodepoints import CODEPOINTS
from calibre.ebooks.unihandecode.jacodepoints import CODEPOINTS as JACODES
from calibre.ebooks.unihandecode.pykakasi.kakasi import Kakasi



class Jadecoder(Unidecoder):
    kakasi = None
    codepoints = {}

    def __init__(self):
        self.codepoints = CODEPOINTS
        self.codepoints.update(JACODES)
        self.kakasi = Kakasi()

    def decode(self, text):
        # try:
        # print("test", Kakasi().convert(text))
        result=self.kakasi.convert(text)
        # print("test12", text)
        return ''.join([d['hepburn'] for d in data])
        # except:
        #     return re.sub('[^\x00-\x7f]', lambda x: self.replace_point(x.group()),text)
