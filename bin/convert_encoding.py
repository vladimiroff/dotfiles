#!/usr/bin/env python
# coding: utf-8
"""
Program that convert text files from one encoding to another.
By default it is used to convert windows-1251 to UTF-8.
Tested on Python 2.7+ and Python 3.2+

Created by Venelin Stoykov <vkstoykov@gmail.com>
"""
from __future__ import unicode_literals
import sys
import os
from optparse import make_option, OptionParser

__version__ = (0, 4)

DEFAULT_INPUT_ENCODING = 'windows-1251'
DEFAULT_OUTPUT_ENCODING = 'utf-8'

FAILSAFE_CHARACTERS = {
    '\u2122': 'TM',
    '\u201c': '"',
    '\u201d': '"',
    '\u2026': '...',
}


def get_version():
    return '.'.join(str(x) for x in __version__)


def get_failsafe_char(char, output_encoding):
    return FAILSAFE_CHARACTERS.get(char, '?').encode(output_encoding)


def convert_to(in_file_name, input_encoding=DEFAULT_INPUT_ENCODING,
               output_encoding=DEFAULT_OUTPUT_ENCODING):
    out_file_name = "%s.%s%s" % (in_file_name[:-4],
                                 output_encoding, in_file_name[-4:])

    with open(in_file_name, 'rb') as in_file:
        try:
            content = in_file.read().decode(input_encoding)
        except Exception as ex:
            print("Can't read '%s' because: %s" % (in_file_name, ex))
        else:
            new_content = []
            for char in content:
                try:
                    new_content.append(char.encode(output_encoding))
                except Exception as ex:
                    new_content.append(get_failsafe_char(char, output_encoding))

            with open(out_file_name, 'wb') as out_file:
                for char in new_content:
                    out_file.write(char)


def main(*args, **options):
    for in_file in args:
        convert_to(in_file, **options)


if __name__ == '__main__':
    prog_name = os.path.basename(sys.argv[0])
    opt_parser = OptionParser(
        prog=prog_name,
        version="%prog " + get_version(),
        usage='usage: %prog [options] file1 [[file2] ... [fileN]]',
        option_list=(
            make_option('-i', '--input-encoding', dest='input_encoding',
                        default=DEFAULT_INPUT_ENCODING,
                        help="Encoding on the input file"),
            make_option('-o', '--output-encoding', dest='output_encoding',
                        default=DEFAULT_OUTPUT_ENCODING,
                        help="Encoding on the output file"),
        )
    )
    options, args = opt_parser.parse_args(sys.argv[1:])
    main(*args, **options.__dict__)
